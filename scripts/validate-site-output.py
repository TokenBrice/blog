#!/usr/bin/env python3
"""Check generated references, language prefixes, indexability and social metadata."""
from __future__ import annotations

import json
import re
import struct
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
HOST = "tokenbrice.xyz"
DEV_ARTIFACTS = ("localhost:1313", "127.0.0.1:1313", "livereload.js")
# Owner decision D19 retains this governance archive link; all other tag links stay guarded.
APPROVED_TAG_LINKS = {("fr/guide-defian/index.html", "/fr/tags/defi-france/")}


class RefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.canonical = None
        self.robots = []
        self.alias = False
        self.alternates = []
        self.lang = ""
        self.og = {}
        self.jsonld = []
        self.script = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for attr in ("href", "src", "srcset"):
            if attrs.get(attr):
                self.refs.append((tag, attr, attrs[attr]))
        rel = (attrs.get("rel") or "").lower().split()
        if tag == "html":
            self.lang = attrs.get("lang") or ""
        if tag == "link" and "canonical" in rel:
            self.canonical = attrs.get("href")
        if tag == "link" and "alternate" in rel and attrs.get("hreflang"):
            self.alternates.append((attrs["hreflang"].lower(), attrs.get("href") or ""))
        if tag == "meta":
            if (attrs.get("name") or "").lower() in {"robots", "googlebot"}:
                self.robots.append(attrs.get("content") or "")
            if (attrs.get("http-equiv") or "").lower() == "refresh":
                self.alias = True
            prop = (attrs.get("property") or "").lower()
            if prop.startswith("og:image"):
                self.og[prop] = attrs.get("content") or ""
        if tag == "script" and (attrs.get("type") or "").lower() == "application/ld+json":
            self.script = []

    def handle_data(self, data):
        if self.script is not None:
            self.script.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.script is not None:
            self.jsonld.append("".join(self.script))
            self.script = None

    @property
    def noindex(self):
        return any("noindex" in re.split(r"[\s,]+", value.lower()) for value in self.robots)


def normalized_url(value, base="https://tokenbrice.xyz/"):
    parsed = urlsplit(urljoin(base, value))
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), unquote(parsed.path), parsed.query, ""))


def local_path(value, base):
    parsed = urlsplit(urljoin(base, value))
    if parsed.scheme not in {"http", "https"} or parsed.hostname != HOST:
        return None
    return unquote(parsed.path)


def output_file(public, path):
    rel = path.lstrip("/")
    direct = public / rel
    if path.endswith("/") or not rel:
        return direct / "index.html"
    if direct.is_file() or Path(rel).suffix:
        return direct
    index = direct / "index.html"
    return index if index.is_file() else public / (rel + ".html")


def page_url(public, path):
    rel = path.relative_to(public).as_posix()
    if rel == "index.html":
        rel = ""
    elif rel.endswith("/index.html"):
        rel = rel[:-10]
    return "https://" + HOST + "/" + rel


def case_insensitive_output(paths):
    """Probe an existing output file without writing to the generated directory."""
    for path in paths:
        probe = path.with_name(path.name.swapcase())
        if probe != path:
            return probe.exists() and probe.samefile(path)
    return False


def file_key(path, case_insensitive):
    value = path.as_posix()
    return value.casefold() if case_insensitive else value


def urls_equal(left, right, case_insensitive=False):
    """Only relax local path casing when the output filesystem collapses it."""
    left_parts, right_parts = urlsplit(left), urlsplit(right)
    if case_insensitive and left_parts.hostname == right_parts.hostname == HOST:
        left_parts = left_parts._replace(path=left_parts.path.casefold())
        right_parts = right_parts._replace(path=right_parts.path.casefold())
    return left_parts == right_parts


def verification_stub(relative_path):
    """Root engine-ownership documents are not editorial/generated content pages."""
    return re.fullmatch(r"(?:google[^/]*|bingsiteauth|yandex_[^/]*)\.html", relative_path, re.IGNORECASE) is not None


def image_dimensions(path):
    """Read PNG, JPEG and all three WebP bitstream headers without a decoder."""
    with path.open("rb") as stream:
        header = stream.read(24)
        if header.startswith(b"\x89PNG\r\n\x1a\n") and header[12:16] == b"IHDR":
            return struct.unpack(">II", header[16:24])
        if header[:2] == b"\xff\xd8":
            stream.seek(2)
            while True:
                marker = stream.read(1)
                if not marker:
                    break
                if marker != b"\xff":
                    continue
                while marker == b"\xff":
                    marker = stream.read(1)
                if not marker or marker in {b"\xda", b"\xd9"}:
                    break
                code = marker[0]
                if code == 0 or code == 1 or 0xD0 <= code <= 0xD8:
                    continue
                raw = stream.read(2)
                if len(raw) != 2:
                    break
                size = int.from_bytes(raw, "big")
                if size < 2:
                    break
                if code in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
                    data = stream.read(5)
                    if len(data) == 5:
                        height, width = struct.unpack(">HH", data[1:])
                        return width, height
                    break
                stream.seek(size - 2, 1)
        if header[:4] == b"RIFF" and header[8:12] == b"WEBP":
            stream.seek(12)
            while True:
                chunk = stream.read(8)
                if len(chunk) != 8:
                    break
                kind, size = chunk[:4], int.from_bytes(chunk[4:], "little")
                data = stream.read(min(size, 10))
                if kind == b"VP8X" and len(data) == 10:
                    return int.from_bytes(data[4:7], "little") + 1, int.from_bytes(data[7:10], "little") + 1
                if kind == b"VP8 " and len(data) == 10 and data[3:6] == b"\x9d\x01\x2a":
                    width, height = struct.unpack("<HH", data[6:10])
                    return width & 0x3FFF, height & 0x3FFF
                if kind == b"VP8L" and len(data) >= 5 and data[0] == 0x2F:
                    bits = int.from_bytes(data[1:5], "little")
                    return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
                stream.seek(size - len(data) + size % 2, 1)
    raise ValueError("unsupported or malformed PNG/JPEG/WebP header")


def breadcrumb_errors(value):
    if isinstance(value, list):
        for child in value:
            yield from breadcrumb_errors(child)
    elif isinstance(value, dict):
        types = value.get("@type", [])
        if types == "BreadcrumbList" or isinstance(types, list) and "BreadcrumbList" in types:
            items = value.get("itemListElement", [])
            if isinstance(items, list):
                for item in items[:-1]:
                    if not isinstance(item, dict) or not item.get("item"):
                        yield "BreadcrumbList non-terminal item has no item URL"
        for child in value.values():
            yield from breadcrumb_errors(child)


def validate(public):
    errors = []
    pages = {}
    sitemap = set()
    for path in sorted(public.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(public).as_posix()
        if rel.startswith("fr/fr/"):
            errors.append(f"{rel}: duplicated French language prefix")
        if path.suffix not in {".html", ".xml", ".json"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for artifact in DEV_ARTIFACTS:
            if artifact in text:
                errors.append(f"{rel}: dev-server artifact {artifact}")
        if path.suffix == ".html":
            parser = RefParser()
            parser.feed(text)
            pages[path] = parser
        elif path.name.startswith("sitemap") and path.suffix == ".xml":
            try:
                root = ET.fromstring(text)
                if root.tag.rsplit("}", 1)[-1] == "urlset":
                    sitemap.update(normalized_url(loc.text.strip()) for loc in root.findall("./{*}url/{*}loc") if loc.text)
            except ET.ParseError as exc:
                errors.append(f"{rel}: sitemap XML parse: {exc}")

    case_insensitive = case_insensitive_output(pages)
    pages_by_key = {file_key(path, case_insensitive): parser for path, parser in pages.items()}

    for url in sorted(sitemap):
        target = local_path(url, url)
        parser = pages_by_key.get(file_key(output_file(public, target), case_insensitive)) if target is not None else None
        if parser is None:
            errors.append(f"{url}: sitemap URL has no generated HTML")
            continue
        if parser.alias:
            errors.append(f"{url}: alias/meta-refresh page is in sitemap")
        if parser.noindex:
            errors.append(f"{url}: noindex page is in sitemap")
        if not parser.canonical or not urls_equal(normalized_url(parser.canonical, url), url, case_insensitive):
            errors.append(f"{url}: sitemap canonical mismatch ({parser.canonical})")

    dimensions = {}
    for path, parser in pages.items():
        rel = path.relative_to(public).as_posix()
        url = page_url(public, path)
        canonical = normalized_url(parser.canonical, url) if parser.canonical else None
        external_canonical = canonical and urlsplit(canonical).hostname != HOST
        content_page = not verification_stub(rel)
        indexable = content_page and not parser.noindex and not parser.alias and not external_canonical
        if content_page and not parser.noindex and not parser.alias:
            if not canonical or not urls_equal(canonical, url, case_insensitive) and not (external_canonical and url not in sitemap):
                errors.append(f"{rel}: indexable page canonical is not self ({parser.canonical})")
        parts = path.relative_to(public).parts
        if len(parts) >= 3 and parts[-3] == "page" and parts[-2].isdigit() and int(parts[-2]) >= 2 and not parser.noindex:
            errors.append(f"{rel}: paginated page beyond page 1 lacks noindex")
        if "404/page/" in rel:
            errors.append(f"{rel}: generated paginated 404 page")
        for tag, attr, value in parser.refs:
            values = [candidate.strip().split()[0] for candidate in value.split(",") if candidate.strip()] if attr == "srcset" else [value]
            for raw in values:
                if raw.startswith("#"):
                    continue
                target = local_path(raw, url)
                if target is None:
                    continue
                if rel.startswith("fr/") and target.startswith("/glossary/") and tag == "a":
                    errors.append(f"{rel}: French page links to English glossary {target}")
                if not output_file(public, target).is_file():
                    errors.append(f"{rel}: broken local ref {raw}")
                if tag == "a" and attr == "href" and indexable and target.startswith(("/tags/", "/fr/tags/")) and not rel.startswith(("tags/", "fr/tags/")) and (rel, target) not in APPROVED_TAG_LINKS:
                    errors.append(f"{rel}: indexable page links to noindexed tag archive {target}")
        if indexable:
            for lang, href in parser.alternates:
                target = local_path(href, url)
                alternate = pages_by_key.get(file_key(output_file(public, target), case_insensitive)) if target is not None else None
                if alternate is None or alternate.noindex or alternate.alias:
                    errors.append(f"{rel}: hreflang {lang} target is missing or not indexable ({href})")
                    continue
                alternate_url = page_url(public, output_file(public, target))
                if not alternate.canonical or not urls_equal(normalized_url(alternate.canonical, alternate_url), alternate_url, case_insensitive):
                    errors.append(f"{rel}: hreflang {lang} target is noncanonical ({href})")
                if not any(urls_equal(normalized_url(back, alternate_url), url, case_insensitive) and (not parser.lang or back_lang == parser.lang.lower() or back_lang == "x-default") for back_lang, back in alternate.alternates):
                    errors.append(f"{rel}: hreflang {lang} is not reciprocal ({href})")
        for raw in parser.jsonld:
            try:
                errors.extend(f"{rel}: {error}" for error in breadcrumb_errors(json.loads(raw)))
            except json.JSONDecodeError as exc:
                errors.append(f"{rel}: invalid JSON-LD: {exc}")
        if not parser.alias and "og:image" in parser.og:
            target = local_path(parser.og["og:image"], url)
            image = public / target.lstrip("/") if target is not None else None
            if image is None or not image.is_file():
                errors.append(f"{rel}: og:image is not an existing local file")
                continue
            try:
                if image not in dimensions:
                    dimensions[image] = image_dimensions(image)
                declared = (int(parser.og.get("og:image:width", "")), int(parser.og.get("og:image:height", "")))
                if declared != dimensions[image]:
                    errors.append(f"{rel}: og:image dimensions {declared} differ from {dimensions[image]}")
                elif indexable and declared != (1200, 630):
                    errors.append(f"{rel}: og:image must be a generated 1200x630 card, got {declared}")
            except (OSError, ValueError, struct.error) as exc:
                errors.append(f"{rel}: og:image dimensions invalid: {exc}")
    return errors


if __name__ == "__main__":
    public = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "public"
    if not public.is_dir():
        print(f"Missing public directory: {public}")
        sys.exit(1)
    failures = validate(public)
    for failure in failures:
        print(failure)
    if failures:
        print(f"FAIL: {len(failures)} generated-site errors")
        sys.exit(1)
    print("OK: generated site references and SEO metadata passed")

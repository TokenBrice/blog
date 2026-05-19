#!/usr/bin/env python3
"""Validate generated static output for broken local references and SEO leaks."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
OUTPUT_EXTENSIONS = {".html", ".xml", ".json"}
DEV_ARTIFACTS = ("localhost:1313", "127.0.0.1:1313", "livereload.js")


class RefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str, str]] = []
        self.canonical: str | None = None
        self.robots: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        for attr in ("href", "src", "srcset"):
            value = attr_map.get(attr)
            if value:
                self.refs.append((tag, attr, value))
        rel_tokens = (attr_map.get("rel") or "").lower().split()
        if tag == "link" and "canonical" in rel_tokens:
            self.canonical = attr_map.get("href")
        if tag == "meta" and (attr_map.get("name") or "").lower() == "robots":
            content = attr_map.get("content")
            if content:
                self.robots.append(content)


def srcset_urls(value: str) -> list[str]:
    return [candidate.strip().split(" ")[0] for candidate in value.split(",") if candidate.strip()]


def is_external(value: str) -> bool:
    return value.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "#", "//"))


def exists_for_path(path: str) -> bool:
    rel = path.lstrip("/")
    if not rel:
        return True
    if path.endswith("/"):
        return (PUBLIC / rel / "index.html").exists()
    suffix = Path(rel).suffix
    if suffix:
        direct = PUBLIC / rel
        if direct.exists():
            return True
        # A URL such as /rss.xml/ is malformed, but tolerate it only if /rss.xml exists
        # so legacy content does not create a false broken-file result.
        return (PUBLIC / rel.rstrip("/") ).exists()
    return (PUBLIC / rel / "index.html").exists() or (PUBLIC / f"{rel}.html").exists()


def output_path_for_url(url: str) -> Path:
    parsed = urlparse(url)
    rel = unquote(parsed.path).lstrip("/")
    if not rel:
        return PUBLIC / "index.html"
    if parsed.path.endswith("/"):
        return PUBLIC / rel / "index.html"
    if Path(rel).suffix:
        return PUBLIC / rel
    return PUBLIC / rel / "index.html"


def has_noindex(parser: RefParser) -> bool:
    for content in parser.robots:
        tokens = {token.strip().lower() for token in content.split(",")}
        if "noindex" in tokens:
            return True
    return False


def collect_sitemap_urls() -> tuple[set[str], set[str]]:
    urls: set[str] = set()
    content_hosts: set[str] = set()
    sitemap_hosts: set[str] = set()
    for sitemap in sorted(PUBLIC.rglob("sitemap*.xml")):
        try:
            root = ET.parse(sitemap).getroot()
        except ET.ParseError as exc:
            print(f"{sitemap.relative_to(PUBLIC)}: XML parse: {exc}")
            sys.exit(1)
        for loc in root.findall(".//{*}loc"):
            if loc.text:
                value = loc.text.strip()
                urls.add(value)
                host = urlparse(value).netloc
                if host:
                    if urlparse(value).path.endswith(".xml"):
                        sitemap_hosts.add(host)
                    else:
                        content_hosts.add(host)
    return urls, sitemap_hosts or content_hosts


missing: dict[str, list[str]] = {}
fr_glossary_leaks: list[str] = []
dev_artifact_hits: list[str] = []
tag_archive_links: list[str] = []
parsed_pages: dict[Path, RefParser] = {}

for path in sorted(PUBLIC.rglob("*")):
    if not path.is_file() or path.suffix not in OUTPUT_EXTENSIONS:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    found = [artifact for artifact in DEV_ARTIFACTS if artifact in text]
    if found:
        rel_path = str(path.relative_to(PUBLIC))
        dev_artifact_hits.append(f"{rel_path}: {', '.join(found)}")

for html in sorted(PUBLIC.rglob("*.html")):
    parser = RefParser()
    parser.feed(html.read_text(encoding="utf-8", errors="ignore"))
    parsed_pages[html] = parser
    rel_html = str(html.relative_to(PUBLIC))
    rel_page = f"/{rel_html}"

    for tag, attr, value in parser.refs:
        values = srcset_urls(value) if attr == "srcset" else [value]
        for raw in values:
            if not raw or is_external(raw):
                continue
            path = unquote(urlparse(raw).path)
            if not path.startswith("/"):
                continue
            if rel_html.startswith("fr/") and path.startswith("/glossary/"):
                fr_glossary_leaks.append(f"{rel_html} -> {path}")
            if not exists_for_path(path):
                missing.setdefault(path, []).append(rel_html)
        if tag == "a" and attr == "href":
            parsed_href = urlparse(value)
            href_path = parsed_href.path
            if (
                (href_path.startswith("/tags/") or href_path.startswith("/fr/tags/"))
                and not rel_page.startswith("/tags/")
                and not rel_page.startswith("/fr/tags/")
            ):
                tag_archive_links.append(f"{rel_html} -> {href_path}")


generated_404_pagination = [
    path
    for path in sorted(PUBLIC.glob("**/404/page/**/*.html"))
    if path.is_file()
]

if generated_404_pagination:
    print("Generated output contains paginated 404 pages:")
    for path in generated_404_pagination[:40]:
        print(path.relative_to(PUBLIC))
    if len(generated_404_pagination) > 40:
        print(f"... {len(generated_404_pagination) - 40} more")
    sys.exit(1)

if tag_archive_links:
    print("Indexable pages link to noindexed tag archives:")
    for item in tag_archive_links[:80]:
        print(item)
    if len(tag_archive_links) > 80:
        print(f"... {len(tag_archive_links) - 80} more")
    sys.exit(1)


if dev_artifact_hits:
    print("Generated output contains localhost/dev-server artifacts:")
    for item in dev_artifact_hits[:80]:
        print(item)
    if len(dev_artifact_hits) > 80:
        print(f"... {len(dev_artifact_hits) - 80} more")
    sys.exit(1)

sitemap_urls, sitemap_hosts = collect_sitemap_urls()
sitemap_indexing_errors: list[str] = []

for url in sorted(sitemap_urls):
    parsed_url = urlparse(url)
    if not parsed_url.netloc or parsed_url.netloc not in sitemap_hosts:
        continue
    if parsed_url.path.endswith(".xml"):
        continue
    html = output_path_for_url(url)
    parser = parsed_pages.get(html)
    if parser is None:
        # Only enforce page-level SEO metadata checks where generated HTML exists.
        continue
    if has_noindex(parser):
        sitemap_indexing_errors.append(f"{url} is in a sitemap but has robots noindex")
    if parser.canonical:
        canonical = urlparse(parser.canonical)
        if canonical.netloc and canonical.netloc not in sitemap_hosts:
            sitemap_indexing_errors.append(
                f"{url} is in a sitemap but canonicalizes externally to {parser.canonical}"
            )

if sitemap_indexing_errors:
    print("Sitemap/indexing consistency errors:")
    for item in sitemap_indexing_errors[:80]:
        print(item)
    if len(sitemap_indexing_errors) > 80:
        print(f"... {len(sitemap_indexing_errors) - 80} more")
    sys.exit(1)

if fr_glossary_leaks:
    print("French pages link to English glossary URLs:")
    for item in fr_glossary_leaks[:50]:
        print(item)
    if len(fr_glossary_leaks) > 50:
        print(f"... {len(fr_glossary_leaks) - 50} more")
    sys.exit(1)

if missing:
    print(f"Broken local refs: {sum(len(v) for v in missing.values())} refs across {len(missing)} URLs")
    for url, pages in sorted(missing.items(), key=lambda item: (-len(item[1]), item[0]))[:80]:
        print(f"{url} <- {', '.join(pages[:3])}")
    sys.exit(1)

print("OK: generated site local refs passed")

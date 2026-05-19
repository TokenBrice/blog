#!/usr/bin/env python3
"""Validate generated static output for broken local references."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"


class RefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = dict(attrs)
        for attr in ("href", "src", "srcset"):
            value = attr_map.get(attr)
            if value:
                self.refs.append((tag, attr, value))


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


missing: dict[str, list[str]] = {}
fr_glossary_leaks: list[str] = []

for html in sorted(PUBLIC.rglob("*.html")):
    parser = RefParser()
    parser.feed(html.read_text(encoding="utf-8", errors="ignore"))
    rel_html = str(html.relative_to(PUBLIC))

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

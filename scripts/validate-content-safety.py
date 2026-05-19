#!/usr/bin/env python3
"""Validate content safety rules that Hugo's build does not cover."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
GLOSSARY = ROOT / "data" / "glossary.json"

errors: list[tuple[Path, int, str]] = []
warnings: list[str] = []


def strip_fenced_code(text: str) -> str:
    return re.sub(r"(?ms)^```.*?^```", "", text)


def line_no(text: str, offset: int) -> int:
    return text[:offset].count("\n") + 1


for path in sorted(CONTENT.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    body = strip_fenced_code(text)

    for match in re.finditer(r"<script\b", body, flags=re.I):
        errors.append((path, line_no(body, match.start()), "raw <script> is not allowed in content; use a shortcode or layout partial"))

    for match in re.finditer(r"<iframe\b([^>]*)>", body, flags=re.I):
        attrs = match.group(1)
        if "youtube-nocookie.com" not in attrs or "title=" not in attrs:
            errors.append((path, line_no(body, match.start()), "raw <iframe> must use youtube-nocookie.com and include a title"))

    for match in re.finditer(r"!\[\s*\]\(", body):
        errors.append((path, line_no(body, match.start()), "Markdown image is missing alt text"))


if GLOSSARY.exists():
    data = json.loads(GLOSSARY.read_text(encoding="utf-8"))
    for lang in ("en", "fr"):
        terms = data.get(lang, {}).get("terms", [])
        known = {term.get("id") for term in terms}
        missing: dict[str, set[str]] = {}
        for term in terms:
            for related in term.get("related_terms", []) or []:
                if related not in known:
                    missing.setdefault(term.get("id", "unknown"), set()).add(related)
        if missing:
            count = sum(len(values) for values in missing.values())
            sample = ", ".join(f"{term}->{next(iter(values))}" for term, values in list(missing.items())[:5])
            warnings.append(f"{lang}: {count} unresolved glossary related_terms ({sample})")


for warning in warnings:
    print(f"WARN {warning}")

if errors:
    for path, lineno, message in errors:
        rel = path.relative_to(ROOT)
        print(f"{rel}:{lineno}: {message}")
    sys.exit(1)

print("OK: content safety validation passed")

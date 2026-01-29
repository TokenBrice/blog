#!/usr/bin/env python3
"""Generate individual glossary term pages from data/glossary.json.

Reads the glossary data and creates one markdown file per term per language
under content/glossary/. Each file has frontmatter that references the term ID;
the layout template pulls actual content from glossary.json at build time.

Usage:
    python scripts/generate-glossary-pages.py
"""

import json
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
GLOSSARY_JSON = os.path.join(PROJECT_ROOT, "data", "glossary.json")
CONTENT_DIR = os.path.join(PROJECT_ROOT, "content", "glossary")


def slugify(text):
    """Convert text to URL-safe slug."""
    return re.sub(r"[^a-z0-9-]", "", text.lower().replace(" ", "-"))


def escape_yaml(s):
    """Escape a string for YAML double-quoted scalar."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def generate_page(term, lang, is_default_lang):
    """Generate a single term page markdown file."""
    term_id = term["id"]
    title = term["term"]
    full_term = term.get("full_term", title)
    if full_term and full_term != title:
        title_display = f"{title} ({full_term})"
    else:
        title_display = title

    short_def = term.get("short_definition", term.get("definition", "")[:160])
    category = term.get("category", "")
    tags = term.get("tags", [])

    # Build frontmatter
    tags_yaml = "\n".join(f'  - "{escape_yaml(t)}"' for t in tags)

    frontmatter = f"""---
title: "{escape_yaml(title_display)}"
description: "{escape_yaml(short_def)}"
date: 2024-01-01
lastmod: 2024-01-01
layout: glossary-term
type: glossary
glossary_id: "{term_id}"
glossary_category: "{category}"
tags:
{tags_yaml}
sitemap:
  priority: 0.7
  changefreq: monthly
---
"""

    # Determine filename
    if is_default_lang:
        filename = f"{term_id}.md"
    else:
        filename = f"{term_id}.{lang}.md"

    filepath = os.path.join(CONTENT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(frontmatter)

    return filepath


def main():
    with open(GLOSSARY_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    os.makedirs(CONTENT_DIR, exist_ok=True)

    created = 0
    for lang_code, is_default in [("en", True), ("fr", False)]:
        lang_data = data.get(lang_code, {})
        terms = lang_data.get("terms", [])
        print(f"Generating {len(terms)} pages for '{lang_code}'...")

        for term in terms:
            path = generate_page(term, lang_code, is_default)
            created += 1

    print(f"Done. Created {created} files in {CONTENT_DIR}/")


if __name__ == "__main__":
    main()

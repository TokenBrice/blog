#!/usr/bin/env python3
"""Validate front-matter on every post and page.

Posts (content/post/**) require: title, description, image, categories, date.
Pages (content/page/**) require: title, description.

For both, `categories` (if present) must be a list, not a bare string.
Missing `image` is downgraded to a warning instead of a hard error,
so cover-less posts don't break CI while still surfacing in logs.
"""
import glob
import sys

import yaml

POST_REQUIRED = ['title', 'description', 'image', 'categories', 'date']
PAGE_REQUIRED = ['title', 'description']
WARN_FIELDS = {'image'}

errors = []
warnings = []


def collect(pattern_dir):
    """Return all .md files under pattern_dir, deduped."""
    paths = set(glob.glob(f'{pattern_dir}/**/index.md', recursive=True))
    paths |= {p for p in glob.glob(f'{pattern_dir}/**/*.md', recursive=True)
              if not p.endswith('/index.md')}
    return sorted(paths)


def parse(path):
    with open(path) as fh:
        text = fh.read()
    if not text.startswith('---'):
        return None
    fm_text = text.split('---', 2)[1]
    return yaml.safe_load(fm_text)


def check(path, fm, required, soft=False):
    """Validate `fm`. When soft=True, missing required fields warn instead of error.
    The categories-must-be-list check stays a hard error in all modes."""
    if not isinstance(fm, dict):
        errors.append((path, 'front-matter is not a mapping'))
        return
    for field in required:
        missing = field not in fm or fm[field] in (None, '', [])
        if missing:
            msg = f'missing {field}'
            if soft or field in WARN_FIELDS:
                warnings.append((path, msg))
            else:
                errors.append((path, msg))
    if 'categories' in fm and fm['categories'] not in (None, ''):
        if not isinstance(fm['categories'], list):
            errors.append((path, 'categories must be a list (use brackets)'))


post_paths = collect('content/post')
page_paths = collect('content/page')

for path in post_paths:
    try:
        fm = parse(path)
    except Exception as e:
        errors.append((path, f'YAML parse: {e}'))
        continue
    if fm is None:
        continue
    check(path, fm, POST_REQUIRED)

for path in page_paths:
    try:
        fm = parse(path)
    except Exception as e:
        errors.append((path, f'YAML parse: {e}'))
        continue
    if fm is None:
        continue
    # Pages are softer: warn on missing fields rather than fail CI.
    # The structural categories check still fails hard if violated.
    check(path, fm, PAGE_REQUIRED, soft=True)

for p, w in warnings:
    print(f'WARN {p}: {w}')

if errors:
    for p, e in errors:
        print(f'{p}: {e}')
    sys.exit(1)

total = len(post_paths) + len(page_paths)
print(f'OK: {len(post_paths)} posts + {len(page_paths)} pages validated '
      f'({total} files, {len(warnings)} warnings)')

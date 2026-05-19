#!/usr/bin/env python3
"""Validate front-matter on every post and page.

Posts (content/post/**) require: title, description, image, categories, date.
Pages (content/page/**) require: title, description.

For both, `categories` (if present) must be a list, not a bare string.
Missing `image` is downgraded to a warning instead of a hard error,
so cover-less posts don't break CI while still surfacing in logs.
"""
import glob
import re
import sys
from datetime import date, datetime
from urllib.parse import urlparse

import yaml

POST_REQUIRED = ['title', 'description', 'image', 'categories', 'date']
PAGE_REQUIRED = ['title', 'description']
WARN_FIELDS = {'image'}
TITLE_MIN = 5
TITLE_MAX = 70
DESCRIPTION_MIN = 50
DESCRIPTION_MAX = 160
EVERGREEN_STALE_DAYS = 180
TODAY = date.today()
SLUG_SEGMENT_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')

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
        return None, text
    fm_text = text.split('---', 2)[1]
    return yaml.safe_load(fm_text), text


def scalar_text(value):
    if value in (None, ''):
        return ''
    return str(value).strip()


def parsed_date(value):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value.strip().replace('Z', '+00:00')).date()
        except ValueError:
            return None
    return None


def check_seo_lengths(path, fm):
    title = scalar_text(fm.get('title'))
    description = scalar_text(fm.get('description'))
    if title and not TITLE_MIN <= len(title) <= TITLE_MAX:
        warnings.append((path, f'title length {len(title)} outside {TITLE_MIN}-{TITLE_MAX} chars'))
    if description and not DESCRIPTION_MIN <= len(description) <= DESCRIPTION_MAX:
        warnings.append((
            path,
            f'description length {len(description)} outside '
            f'{DESCRIPTION_MIN}-{DESCRIPTION_MAX} chars',
        ))


def check_series_order(path, fm):
    if fm.get('series') and fm.get('series_order') in (None, '', []):
        errors.append((path, 'missing series_order for series post'))


def check_legacy_post_alias(path, fm):
    url = scalar_text(fm.get('url')).strip('/')
    if not url or '://' in url:
        return
    expected = f'p/{url}'
    aliases = fm.get('aliases') or []
    if isinstance(aliases, str):
        aliases = [aliases]
    normalized = {scalar_text(alias).strip('/') for alias in aliases}
    if expected not in normalized:
        errors.append((path, f'missing legacy /p/ alias: {expected}'))


def check_slug_normalization(path, fm):
    for field in ('slug', 'url'):
        value = scalar_text(fm.get(field))
        if not value:
            continue
        parsed = urlparse(value)
        raw_path = parsed.path if parsed.scheme else value
        segments = [segment for segment in raw_path.strip('/').split('/') if segment]
        for segment in segments:
            if not SLUG_SEGMENT_RE.match(segment):
                warnings.append((
                    path,
                    f'{field} segment "{segment}" should be lowercase kebab-case; '
                    'preserve legacy URLs with aliases when renaming',
                ))


def check_evergreen_freshness(path, fm, body):
    if not path.startswith('content/page/'):
        return
    marker_text = f"{scalar_text(fm.get('type'))} {scalar_text(fm.get('description'))} {body[:500]}"
    if 'evergreen' not in marker_text.lower():
        return
    lastmod = parsed_date(fm.get('lastmod'))
    if lastmod is None:
        warnings.append((path, 'evergreen page missing lastmod'))
        return
    age = (TODAY - lastmod).days
    if age > EVERGREEN_STALE_DAYS:
        warnings.append((path, f'evergreen page lastmod is stale ({age} days old)'))


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
    check_seo_lengths(path, fm)
    check_slug_normalization(path, fm)


post_paths = collect('content/post')
page_paths = collect('content/page')

for path in post_paths:
    try:
        fm, body = parse(path)
    except Exception as e:
        errors.append((path, f'YAML parse: {e}'))
        continue
    if fm is None:
        continue
    check(path, fm, POST_REQUIRED)
    check_series_order(path, fm)
    check_legacy_post_alias(path, fm)

for path in page_paths:
    try:
        fm, body = parse(path)
    except Exception as e:
        errors.append((path, f'YAML parse: {e}'))
        continue
    if fm is None:
        continue
    # Pages are softer: warn on missing fields rather than fail CI.
    # The structural categories check still fails hard if violated.
    check(path, fm, PAGE_REQUIRED, soft=True)
    check_evergreen_freshness(path, fm, body)

for p, w in warnings:
    print(f'WARN {p}: {w}')

if errors:
    for p, e in errors:
        print(f'{p}: {e}')
    sys.exit(1)

total = len(post_paths) + len(page_paths)
print(f'OK: {len(post_paths)} posts + {len(page_paths)} pages validated '
      f'({total} files, {len(warnings)} warnings)')

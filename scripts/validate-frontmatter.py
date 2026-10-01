#!/usr/bin/env python3
"""Validate front-matter on every post and page.

Posts (content/post/**) require: title, description, image, categories, date.
Pages (content/page/**) require: title, description.

For both, `categories` (if present) must be a list, not a bare string.
Missing `image` is downgraded to a warning instead of a hard error,
so cover-less posts don't break CI while still surfacing in logs.

Related post paths must resolve to an English post's URL or alias.
French aliases must omit /fr/: Hugo adds the language prefix itself.
"""
import glob
import json
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path
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


try:
    glossary_data = json.loads(Path('data/glossary.json').read_text(encoding='utf-8'))
    glossary_ids = {
        lang: {term['id'] for term in data['terms']}
        for lang, data in glossary_data.items()
        if isinstance(data, dict) and 'terms' in data
    }
    project_data = yaml.safe_load(Path('data/projects.yaml').read_text(encoding='utf-8'))
    project_ids = {project['id'] for project in project_data['projects']}
except (OSError, ValueError, KeyError, TypeError) as exc:
    errors.append(('data', f'cannot load schema IDs: {exc}'))
    glossary_ids = {}
    project_ids = set()

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
        errors.append((path, f'title length {len(title)} outside {TITLE_MIN}-{TITLE_MAX} chars'))
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
    aliases = fm.get('aliases') or []
    if isinstance(aliases, str):
        aliases = [aliases]
    normalized = {scalar_text(alias).strip('/') for alias in aliases}
    year = os.path.basename(os.path.dirname(path))
    stem = re.sub(r'(\.fr)?\.md$', '', os.path.basename(path))
    for expected in (f'p/{url}', f'posts/{year}/{stem.lower()}'):
        if expected not in normalized:
            errors.append((path, f'missing legacy alias: {expected}'))


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


def https_url(value):
    return isinstance(value, str) and urlparse(value).scheme == 'https' and bool(urlparse(value).netloc)


def site_path(value):
    return isinstance(value, str) and value.startswith('/') and not value.startswith('//') and value.endswith('/') and not urlparse(value).query and not urlparse(value).fragment


def check_optional_schema(path, fm):
    def fail(message):
        errors.append((path, message))

    if 'format' in fm and fm['format'] not in ('analysis', 'thesis', 'practical', 'tutorial'):
        fail('format must be analysis, thesis, practical or tutorial')
    for field in ('noindex', 'og_panel'):
        if field in fm and not isinstance(fm[field], bool):
            fail(f'{field} must be bool')
    if 'imagePosition' in fm and not isinstance(fm['imagePosition'], str):
        fail('imagePosition must be a string')
    if 'context' in fm:
        context = fm['context']
        if not isinstance(context, dict):
            fail('context must be a mapping')
        else:
            if context.get('kind') not in ('historical', 'status', 'update'):
                fail('context.kind must be historical, status or update')
            checked = parsed_date(context.get('checked'))
            if checked is None or checked > TODAY:
                fail('context.checked must be a valid date not in the future')
            text = context.get('text')
            if not isinstance(text, str) or not text.strip() or len(text) > 400:
                fail('context.text must be non-empty and at most 400 characters')
            sources = context.get('sources')
            if 'sources' in context and (not isinstance(sources, list) or not all(https_url(source) for source in sources)):
                fail('context.sources must be a list of https URLs')
            if context.get('kind') == 'status' and (not isinstance(sources, list) or not sources):
                fail('context.sources is required and non-empty for status')
    if 'takeaways' in fm:
        value = fm['takeaways']
        if not isinstance(value, list) or not 2 <= len(value) <= 3 or not all(isinstance(item, str) and item.strip() for item in value):
            fail('takeaways must contain 2-3 non-empty strings')
    if 'related_posts' in fm:
        value = fm['related_posts']
        if not isinstance(value, list) or len(value) > 2 or not all(site_path(item) for item in value):
            fail('related_posts must contain at most 2 slash-delimited site paths')
    language = 'fr' if path.endswith('.fr.md') or '/fr/' in path else 'en'
    if language == 'fr':
        aliases = fm.get('aliases') or []
        if isinstance(aliases, str):
            aliases = [aliases]
        if isinstance(aliases, list) and any(isinstance(alias, str) and alias.startswith('/fr/') for alias in aliases):
            fail('French aliases must not start with /fr/: Hugo adds the language prefix')
    if isinstance(fm.get('related_posts'), list):
        for target in fm['related_posts']:
            if site_path(target) and target.strip('/') not in en_post_references:
                fail(f'related_posts target does not resolve to an EN post URL or alias: {target}')
    for field, allowed in (('glossary_terms', glossary_ids.get(language, set())), ('disclosure', project_ids)):
        if field in fm:
            value = fm[field]
            if not isinstance(value, list) or not all(isinstance(item, str) and item in allowed for item in value):
                fail(f'{field} must be a list of declared IDs ({language})')
    if 'image_meta' in fm:
        value = fm['image_meta']
        if not isinstance(value, dict) or not all(
            isinstance(src, str) and isinstance(meta, dict)
            and all(key in ('alt', 'caption') and isinstance(text, str) for key, text in meta.items())
            for src, meta in value.items()
        ):
            fail('image_meta must map string sources to optional alt/caption strings')


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
    check_optional_schema(path, fm)


post_paths = collect('content/post')
page_paths = collect('content/page')
post_frontmatter = {}
en_post_references = set()

for path in post_paths:
    try:
        fm, body = parse(path)
    except Exception as e:
        errors.append((path, f'YAML parse: {e}'))
        continue
    if not isinstance(fm, dict):
        if fm is not None:
            check(path, fm, POST_REQUIRED)
        continue
    post_frontmatter[path] = fm
    if not path.endswith('.fr.md') and '/fr/' not in path:
        aliases = fm.get('aliases') or []
        if isinstance(aliases, str):
            aliases = [aliases]
        for target in [fm.get('url'), *aliases]:
            if isinstance(target, str) and target.strip('/') and not urlparse(target).scheme and not target.startswith('//'):
                en_post_references.add(target.strip('/'))

for path, fm in post_frontmatter.items():
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
    if isinstance(fm, dict):
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

#!/usr/bin/env python3
"""Validate bilingual glossary identity, taxonomy and related destinations."""
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit


def site_path(value):
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    return value.startswith('/') and not value.startswith('//') and not parsed.query and not parsed.fragment


def article_url(value):
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    if parsed.scheme == 'https' and parsed.netloc and parsed.hostname != 'tokenbrice.xyz':
        return True
    return site_path(value) and value.endswith('/') and value == value.lower()


def validate(data):
    errors = []
    languages = {lang: value for lang, value in data.items() if isinstance(value, dict) and 'terms' in value}
    ids_by_language = {}
    for lang, value in languages.items():
        terms = value['terms']
        categories = {category['id'] for category in data.get('categories', {}).get(lang, [])}
        ids = set()
        names = set()
        for term in terms:
            identifier = term.get('id')
            name = term.get('term')
            if not isinstance(identifier, str) or not identifier.strip() or identifier in ids:
                errors.append(f'{lang}: missing or duplicate ID {identifier}')
            if not isinstance(name, str) or not name.strip() or name.strip().casefold() in names:
                errors.append(f'{lang}: missing or duplicate term name {name}')
            if isinstance(identifier, str):
                ids.add(identifier)
            if isinstance(name, str):
                names.add(name.strip().casefold())
        ids_by_language[lang] = ids
        for term in terms:
            label = f"{lang}/{term.get('id')}"
            if term.get('category') not in categories:
                errors.append(f'{label}: category is not declared')
            related = term.get('related_terms', [])
            if not isinstance(related, list) or not all(isinstance(target, str) and target in ids for target in related):
                errors.append(f'{label}: related_terms contains unknown IDs')
            aliases = term.get('aliases', [])
            if not isinstance(aliases, list) or not all(site_path(alias) for alias in aliases):
                errors.append(f'{label}: aliases must be site paths')
            if 'index' in term and not isinstance(term['index'], bool):
                errors.append(f'{label}: index must be bool')
            articles = term.get('related_articles', [])
            if not isinstance(articles, list) or not all(isinstance(article, dict) and article_url(article.get('url')) for article in articles):
                errors.append(f'{label}: related_articles URLs must be lowercase slash-delimited site paths or external https URLs')
    if 'en' not in ids_by_language or 'fr' not in ids_by_language:
        errors.append('glossary requires both en and fr terms')
    elif ids_by_language['en'] != ids_by_language['fr']:
        errors.append(f"EN/FR ID parity: EN only {sorted(ids_by_language['en'] - ids_by_language['fr'])}; FR only {sorted(ids_by_language['fr'] - ids_by_language['en'])}")
    return errors


if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('data/glossary.json')
    try:
        failures = validate(json.loads(path.read_text(encoding='utf-8')))
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        failures = [f'{path}: invalid glossary data: {exc}']
    for failure in failures:
        print(failure)
    if failures:
        sys.exit(1)
    print('OK: glossary identity, taxonomy and URLs passed')

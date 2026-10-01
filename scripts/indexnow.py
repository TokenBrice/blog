#!/usr/bin/env python3
"""Prepare a pre-deploy live-sitemap diff, then submit it after deployment."""
import argparse
import importlib.util
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

HOST = 'tokenbrice.xyz'
KEY = '69be76f58f52061d7a60b37f25278c4c'
ORIGIN = f'https://{HOST}'
KEY_LOCATION = f'{ORIGIN}/{KEY}.txt'


def fetch(url):
    with urlopen(Request(url, headers={'User-Agent': 'TokenBrice-IndexNow/1.0'}), timeout=30) as response:
        return response.read()


def sitemap_entries(root):
    return {
        entry.findtext('{*}loc', '').strip(): entry.findtext('{*}lastmod', '').strip()
        for entry in root.findall('./{*}url')
        if entry.findtext('{*}loc', '').strip()
    }


def live_sitemaps():
    pending = [f'{ORIGIN}/sitemap.xml']
    seen = set()
    entries = {}
    while pending:
        url = pending.pop()
        if url in seen:
            continue
        if urlsplit(url).scheme != 'https' or urlsplit(url).hostname != HOST:
            raise ValueError(f'Unexpected live sitemap origin: {url}')
        seen.add(url)
        root = ET.fromstring(fetch(url))
        if root.tag.rsplit('}', 1)[-1] == 'sitemapindex':
            pending.extend(loc.text.strip() for loc in root.findall('./{*}sitemap/{*}loc') if loc.text)
        elif root.tag.rsplit('}', 1)[-1] == 'urlset':
            entries.update(sitemap_entries(root))
        else:
            raise ValueError(f'Not a sitemap: {url}')
    if not entries:
        raise ValueError('Live sitemap is empty; refusing a full-site bootstrap submission')
    return entries


def built_sitemaps(public):
    # Reuse the output parser, so alias/noindex/canonical policy cannot drift.
    spec = importlib.util.spec_from_file_location('site_output', Path(__file__).with_name('validate-site-output.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    entries = {}
    for path in sorted(public.rglob('sitemap*.xml')):
        root = ET.parse(path).getroot()
        if root.tag.rsplit('}', 1)[-1] != 'urlset':
            continue
        for url, lastmod in sitemap_entries(root).items():
            if urlsplit(url).scheme != 'https' or urlsplit(url).hostname != HOST:
                continue
            page = module.output_file(public, module.local_path(url, url))
            if not page.is_file() or page.suffix != '.html':
                continue
            parser = module.RefParser()
            parser.feed(page.read_text(encoding='utf-8'))
            if not parser.alias and not parser.noindex and parser.canonical and module.normalized_url(parser.canonical, url) == module.normalized_url(url):
                entries[url] = lastmod
    return entries


def prepare(public, output, dry_run):
    # Fetch failure is deliberate: never treat an unreachable live site as zero URLs.
    before = live_sitemaps()
    after = built_sitemaps(public)
    changed = sorted(url for url, lastmod in after.items() if url not in before or lastmod != before[url])
    payload = {'host': HOST, 'key': KEY, 'keyLocation': KEY_LOCATION, 'urlList': changed}
    if dry_run:
        print(json.dumps(payload, indent=2))
    else:
        output.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(f'Prepared {len(changed)} new/lastmod-changed canonical URLs', file=sys.stderr)


def submit(path, dry_run):
    payload = json.loads(path.read_text(encoding='utf-8'))
    if any(payload.get(field) != expected for field, expected in (('host', HOST), ('key', KEY), ('keyLocation', KEY_LOCATION))):
        raise ValueError('Manifest identity does not match this site')
    urls = payload.get('urlList')
    if not isinstance(urls, list) or not all(isinstance(url, str) and urlsplit(url).scheme == 'https' and urlsplit(url).hostname == HOST for url in urls):
        raise ValueError('Manifest contains non-site URLs')
    if not urls:
        print('No canonical URLs changed; nothing to submit')
        return
    if not dry_run and fetch(KEY_LOCATION).decode('utf-8').strip() != KEY:
        raise ValueError('Live IndexNow verification key does not match')
    for offset in range(0, len(urls), 10000):
        batch = {**payload, 'urlList': urls[offset:offset + 10000]}
        if dry_run:
            print(json.dumps(batch, indent=2))
            continue
        request = Request('https://api.indexnow.org/indexnow', data=json.dumps(batch).encode('utf-8'), headers={'Content-Type': 'application/json; charset=utf-8'}, method='POST')
        with urlopen(request, timeout=30) as response:
            print(f'IndexNow received {len(batch["urlList"])} URLs: HTTP {response.status} (receipt is not indexing)')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest='command', required=True)
    prepare_parser = subcommands.add_parser('prepare')
    prepare_parser.add_argument('--public', type=Path, default=Path('public'))
    prepare_parser.add_argument('--output', type=Path, default=Path('indexnow-urls.json'))
    prepare_parser.add_argument('--dry-run', action='store_true')
    submit_parser = subcommands.add_parser('submit')
    submit_parser.add_argument('manifest', type=Path)
    submit_parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        if args.command == 'prepare':
            prepare(args.public.resolve(), args.output, args.dry_run)
        else:
            submit(args.manifest, args.dry_run)
    except (OSError, ValueError, ET.ParseError) as exc:
        print(f'IndexNow skipped: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())

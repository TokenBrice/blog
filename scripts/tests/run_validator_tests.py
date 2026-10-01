#!/usr/bin/env python3
"""Subprocess regressions using only disposable synthetic sites and fixture data."""
import copy
import importlib.util
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
CLEAN = Path(__file__).resolve().parent / 'fixtures' / 'clean'


def png(width=1200, height=630):
    def chunk(kind, data):
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))
    # Header-only raster fixture: the validator does not decode image pixels.
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)) + chunk(b'IEND', b'')


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(CLEAN, self.root, dirs_exist_ok=True)
        self.public = self.root / 'public'
        (self.public / 'tiny.png').write_bytes(png())
        self.frontmatter = json.loads((self.root / 'frontmatter.json').read_text())
        self.glossary = json.loads((self.root / 'data/glossary.json').read_text())

    def run_validator(self, script, *args, failure=None):
        result = subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)], cwd=self.root, capture_output=True, text=True)
        output = result.stdout + result.stderr
        self.assertEqual(result.returncode, 1 if failure else 0, output)
        if failure:
            self.assertIn(failure, output)

    def write_frontmatter(self, fm, filename='fixture.md'):
        path = self.root / 'content/page' / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('---\n' + json.dumps(fm) + '\n---\nFixture body.\n', encoding='utf-8')

    def mutate_html(self, filename, old, new):
        path = self.public / filename
        path.write_text(path.read_text().replace(old, new), encoding='utf-8')

    def test_local_url_casing_comparison_modes(self):
        spec = importlib.util.spec_from_file_location('site_output', SCRIPTS / 'validate-site-output.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        canonical = 'https://tokenbrice.xyz/eco-crypto/'
        alias_case = 'https://tokenbrice.xyz/Eco-Crypto/'
        self.assertFalse(module.urls_equal(canonical, alias_case, False))
        self.assertTrue(module.urls_equal(canonical, alias_case, True))
        self.assertFalse(module.urls_equal(canonical, 'https://tokenbrice.xyz/other/', True))
        self.assertFalse(module.urls_equal(canonical + '?q=lower', canonical + '?q=LOWER', True))
        self.assertFalse(module.urls_equal('https://example.org/Lower/', 'https://example.org/lower/', True))
        fixture_path = self.public / 'fr/index.html'
        different_case = self.public / 'FR/index.html'
        self.assertNotEqual(module.file_key(fixture_path, False), module.file_key(different_case, False))
        self.assertEqual(module.file_key(fixture_path, True), module.file_key(different_case, True))

    def test_clean_output(self):
        self.run_validator('validate-site-output.py', self.public)

    def test_engine_verification_stubs_keep_reference_checks(self):
        for name in ('google9db48b7a1be2e0ee.html', 'BingSiteAuth.html', 'yandex_123.html'):
            (self.public / name).write_text('Engine ownership verification.')
        self.run_validator('validate-site-output.py', self.public)
        (self.public / 'google9db48b7a1be2e0ee.html').write_text('<a href="/missing/">Broken verification reference</a>')
        self.run_validator('validate-site-output.py', self.public, failure='broken local ref')

    def test_clean_frontmatter(self):
        self.write_frontmatter(self.frontmatter)
        self.write_frontmatter(self.frontmatter, 'fixture.fr.md')
        self.run_validator('validate-frontmatter.py')

    def test_clean_glossary(self):
        self.run_validator('validate-glossary.py', self.root / 'data/glossary.json')

    def test_glossary_legacy_alias_paths(self):
        self.glossary['en']['terms'][0]['aliases'] = ['/old-path', '/legacy.html']
        path = self.root / 'data/glossary.json'
        path.write_text(json.dumps(self.glossary))
        self.run_validator('validate-glossary.py', path)

    def test_glossary_hub_permalink_resolution(self):
        for filename, fields, target in (
            ('hub/index.md', {'slug': 'yield-handbook'}, '/yield-handbook/'),
            ('hub/index.fr.md', {'slug': 'rendement'}, '/fr/rendement/'),
            ('hub/index.md', {'title': 'Yield Handbook'}, '/yield-handbook/'),
            ('hub/index.md', {'slug': 'ignored', 'url': '/custom-hub/'}, '/custom-hub/'),
            ('hub/index.fr.md', {'url': 'guide-rendement'}, '/fr/guide-rendement/'),
            ('hub/index.fr.md', {'url': '/shared-hub/'}, '/shared-hub/'),
        ):
            with self.subTest(filename=filename, target=target):
                self.write_frontmatter({'title': 'Hub fixture', **fields}, filename)
                self.glossary['en']['terms'][0]['related_guides'] = [target]
                path = self.root / 'data/glossary.json'
                path.write_text(json.dumps(self.glossary))
                self.run_validator('validate-glossary.py', path)
                self.glossary['en']['terms'][0]['related_guides'] = ['/absent-hub/']
                path.write_text(json.dumps(self.glossary))
                self.run_validator('validate-glossary.py', path, failure='related_guides target does not resolve')

    def test_related_post_url_and_alias_resolution(self):
        post = self.root / 'content/post/2020/guide.md'
        # Both bare and slash-delimited front-matter URLs identify the same post.
        for url in ('guide', '/guide/'):
            post.write_text(post.read_text().replace('url: guide', 'url: ' + url))
            for target in ('/guide/', '/legacy-guide/', '/posts/2020/guide/'):
                with self.subTest(url=url, target=target):
                    fm = dict(self.frontmatter, related_posts=[target])
                    self.write_frontmatter(fm)
                    self.write_frontmatter(fm, 'fixture.fr.md')
                    self.run_validator('validate-frontmatter.py')

    def test_related_post_rejects_french_only_destination(self):
        post = self.root / 'content/post/2020/guide.md'
        post.rename(post.with_name('guide.fr.md'))
        self.write_frontmatter(self.frontmatter)
        self.run_validator('validate-frontmatter.py', failure='related_posts target does not resolve to an EN post')

    def test_related_post_rejects_page_destination(self):
        self.write_frontmatter(dict(self.frontmatter, related_posts=[]), 'guide/index.md')
        self.write_frontmatter(dict(self.frontmatter, related_posts=['/missing-post/']))
        self.write_frontmatter(dict(self.frontmatter, related_posts=[], url='missing-post'), 'other/index.md')
        self.run_validator('validate-frontmatter.py', failure='related_posts target does not resolve to an EN post')

    def test_frontmatter_french_alias_prefix(self):
        fm = dict(self.frontmatter, aliases=['/fr/old-guide/'])
        self.write_frontmatter(fm, 'fixture.fr.md')
        self.run_validator('validate-frontmatter.py', failure='French aliases must not start with /fr/')

    def test_glossary_french_alias_prefix(self):
        self.glossary['fr']['terms'][0]['aliases'] = ['/fr/old-apy/']
        path = self.root / 'data/glossary.json'
        path.write_text(json.dumps(self.glossary))
        self.run_validator('validate-glossary.py', path, failure='French aliases must not start with /fr/')

    def test_generated_french_prefix_duplication(self):
        directory = self.public / 'fr/fr/legacy'
        directory.mkdir(parents=True)
        (directory / 'index.html').write_text('<meta http-equiv="refresh" content="0;url=/fr/"><link rel="canonical" href="https://tokenbrice.xyz/fr/">')
        self.run_validator('validate-site-output.py', self.public, failure='duplicated French language prefix')

    def test_intentional_external_canonical(self):
        (self.public / 'external.html').write_text('<link rel="canonical" href="https://example.org/original/">')
        self.run_validator('validate-site-output.py', self.public)

    def test_alias_and_noindex_outside_sitemap(self):
        (self.public / 'old.html').write_text('<meta http-equiv="refresh" content="0;url=/"><link rel="canonical" href="https://tokenbrice.xyz/">')
        (self.public / 'hidden.html').write_text('<meta name="robots" content="noindex,follow"><link rel="canonical" href="https://tokenbrice.xyz/">')
        self.run_validator('validate-site-output.py', self.public)

    def test_noindex_pagination(self):
        directory = self.public / 'page/2'
        directory.mkdir(parents=True)
        (directory / 'index.html').write_text('<meta name="robots" content="noindex,follow"><link rel="canonical" href="https://tokenbrice.xyz/">')
        self.run_validator('validate-site-output.py', self.public)

    def test_owner_approved_tag_link(self):
        target = self.public / 'fr/tags/defi-france'
        target.mkdir(parents=True)
        (target / 'index.html').write_text('<meta name="robots" content="noindex"><link rel="canonical" href="https://tokenbrice.xyz/fr/tags/defi-france/">')
        source = self.public / 'fr/guide-defian'
        source.mkdir(parents=True)
        (source / 'index.html').write_text('<link rel="canonical" href="https://tokenbrice.xyz/fr/guide-defian/"><a href="/fr/tags/defi-france/">Governance</a>')
        self.run_validator('validate-site-output.py', self.public)
        self.mutate_html('index.html', '</body>', '<a href="/fr/tags/defi-france/">Not approved here</a></body>')
        self.run_validator('validate-site-output.py', self.public, failure='indexable page links to noindexed tag archive')

    def test_all_failures_reported(self):
        self.mutate_html('index.html', '</body>', '<a href="/missing/">Missing</a>localhost:1313</body>')
        result = subprocess.run([sys.executable, str(SCRIPTS / 'validate-site-output.py'), str(self.public)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('broken local ref', result.stdout)
        self.assertIn('dev-server artifact', result.stdout)

    def test_png_jpeg_webp_headers(self):
        # The validator deliberately reads headers rather than decoding pixels.
        headers = {
            'jpg': b'\xff\xd8\xff\xe0\x00\x04xx\xff\xc0\x00\x0b' + struct.pack('>BHH', 8, 630, 1200) + b'\x01\x01\x11\x00',
            'webp-vp8x': b'RIFF' + struct.pack('<I', 22) + b'WEBPVP8X' + struct.pack('<I', 10) + bytes(4) + (1200 - 1).to_bytes(3, 'little') + (630 - 1).to_bytes(3, 'little'),
            'webp-vp8': b'RIFF' + struct.pack('<I', 22) + b'WEBPVP8 ' + struct.pack('<I', 10) + b'\x00\x00\x00\x9d\x01\x2a' + struct.pack('<HH', 1200, 630),
            'webp-vp8l': b'RIFF' + struct.pack('<I', 18) + b'WEBPVP8L' + struct.pack('<I', 5) + b'\x2f' + (((630 - 1) << 14) | (1200 - 1)).to_bytes(4, 'little') + b'\x00',
        }
        for kind, header in headers.items():
            with self.subTest(kind=kind):
                (self.public / 'tiny.png').write_bytes(header)
                self.run_validator('validate-site-output.py', self.public)
                self.mutate_html('index.html', 'og:image:width" content="1200"', 'og:image:width" content="1201"')
                self.run_validator('validate-site-output.py', self.public, failure='og:image dimensions')
                shutil.copyfile(CLEAN / 'public/index.html', self.public / 'index.html')

    def test_indexable_og_card_size(self):
        (self.public / 'tiny.png').write_bytes(png(1, 1))
        self.mutate_html('index.html', 'og:image:width" content="1200"', 'og:image:width" content="1"')
        self.mutate_html('index.html', 'og:image:height" content="630"', 'og:image:height" content="1"')
        self.run_validator('validate-site-output.py', self.public, failure='og:image must be a generated 1200x630 card')


SITE_DEFECTS = {
    'absolute_internal_missing': ('index.html', '</body>', '<a href="https://tokenbrice.xyz/missing/">Missing</a></body>', 'broken local ref'),
    'protocol_relative_missing': ('index.html', '</body>', '<a href="//tokenbrice.xyz/missing/">Missing</a></body>', 'broken local ref'),
    'percent_encoded_missing': ('index.html', 'caf%C3%A9/', 'absent%C3%A9/', 'broken local ref'),
    'sitemap_missing_html': ('sitemap.xml', '</urlset>', '<url><loc>https://tokenbrice.xyz/absent/</loc></url></urlset>', 'sitemap URL has no generated HTML'),
    'sitemap_alias': ('fr/index.html', '</head>', '<meta http-equiv="refresh" content="0;url=/"></head>', 'alias/meta-refresh page is in sitemap'),
    'sitemap_noindex': ('fr/index.html', '</head>', '<meta name="robots" content="noindex,follow"></head>', 'noindex page is in sitemap'),
    'sitemap_wrong_canonical': ('fr/index.html', 'rel="canonical" href="https://tokenbrice.xyz/fr/"', 'rel="canonical" href="https://tokenbrice.xyz/"', 'sitemap canonical mismatch'),
    'sitemap_external_canonical': ('fr/index.html', 'rel="canonical" href="https://tokenbrice.xyz/fr/"', 'rel="canonical" href="https://example.org/"', 'sitemap canonical mismatch'),
    'hreflang_missing_target': ('index.html', 'hreflang="fr" href="https://tokenbrice.xyz/fr/"', 'hreflang="fr" href="https://tokenbrice.xyz/missing/"', 'hreflang fr target is missing'),
    'hreflang_noindex_target': ('fr/index.html', '</head>', '<meta name="robots" content="noindex"></head>', 'hreflang fr target is missing or not indexable'),
    'hreflang_alias_target': ('fr/index.html', '</head>', '<meta http-equiv="refresh" content="0;url=/"></head>', 'hreflang fr target is missing or not indexable'),
    'hreflang_nonreciprocal': ('fr/index.html', '<link rel="alternate" hreflang="en" href="https://tokenbrice.xyz/">', '', 'not reciprocal'),
    'breadcrumb_missing_item': ('index.html', ',"item":"https://tokenbrice.xyz/"', '', 'BreadcrumbList non-terminal item'),
    'breadcrumb_empty_item': ('index.html', '"item":"https://tokenbrice.xyz/"', '"item":""', 'BreadcrumbList non-terminal item'),
    'og_missing_file': ('index.html', '/tiny.png', '/absent.png', 'og:image is not an existing local file'),
    'og_external_file': ('index.html', 'https://tokenbrice.xyz/tiny.png', 'https://example.org/tiny.png', 'og:image is not an existing local file'),
    'og_wrong_width': ('index.html', 'og:image:width" content="1200"', 'og:image:width" content="1201"', 'og:image dimensions'),
    'og_wrong_height': ('index.html', 'og:image:height" content="630"', 'og:image:height" content="631"', 'og:image dimensions'),
    'og_missing_dimensions': ('index.html', '<meta property="og:image:width" content="1200">', '', 'og:image dimensions invalid'),
    'dev_artifact': ('index.html', '</body>', 'livereload.js</body>', 'dev-server artifact'),
}


def site_test(case):
    def test(self):
        filename, old, new, error = case
        self.mutate_html(filename, old, new)
        self.run_validator('validate-site-output.py', self.public, failure=error)
    return test


for name, case in SITE_DEFECTS.items():
    setattr(ValidatorTests, 'test_site_' + name, site_test(case))


def canonical_outside_sitemap(self):
    (self.public / 'extra.html').write_text('<link rel="canonical" href="https://tokenbrice.xyz/">')
    self.run_validator('validate-site-output.py', self.public, failure='indexable page canonical is not self')


def canonical_missing(self):
    (self.public / 'extra.html').write_text('<html lang="en"><body>No canonical</body></html>')
    self.run_validator('validate-site-output.py', self.public, failure='indexable page canonical is not self')


def pager_defect(self):
    directory = self.public / 'page/2'
    directory.mkdir(parents=True)
    (directory / 'index.html').write_text('<link rel="canonical" href="https://tokenbrice.xyz/page/2/">')
    self.run_validator('validate-site-output.py', self.public, failure='paginated page beyond page 1 lacks noindex')


ValidatorTests.test_nonself_canonical_outside_sitemap = canonical_outside_sitemap
ValidatorTests.test_missing_canonical = canonical_missing
ValidatorTests.test_pager_noindex_guard = pager_defect

FM_DEFECTS = {
    'title_too_long': ('title', 'x' * 71, 'title length 71 outside 5-70 chars'),
    'title_too_short': ('title', 'x' * 4, 'title length 4 outside 5-70 chars'),
    'format': ('format', 'essay', 'format must be'),
    'noindex': ('noindex', 'true', 'noindex must be bool'),
    'context_mapping': ('context', 'note', 'context must be a mapping'),
    'context_kind': ('context.kind', 'current', 'context.kind must be'),
    'context_date': ('context.checked', '2020-02-30', 'context.checked must be'),
    'context_future': ('context.checked', '9999-01-01', 'context.checked must be'),
    'context_empty_text': ('context.text', '  ', 'context.text must be'),
    'context_long_text': ('context.text', 'x' * 401, 'context.text must be'),
    'context_http_source': ('context.sources', ['http://example.org/'], 'context.sources must be'),
    'context_sources_type': ('context.sources', 'https://example.org/', 'context.sources must be'),
    'status_missing_source': ('context.sources', None, 'context.sources is required'),
    'status_empty_sources': ('context.sources', [], 'context.sources is required'),
    'takeaways_too_few': ('takeaways', ['One'], 'takeaways must contain'),
    'takeaways_too_many': ('takeaways', ['One', 'Two', 'Three', 'Four'], 'takeaways must contain'),
    'takeaways_empty': ('takeaways', ['One', ''], 'takeaways must contain'),
    'related_posts_limit': ('related_posts', ['/one/', '/two/', '/three/'], 'related_posts must contain'),
    'related_posts_path': ('related_posts', ['guide'], 'related_posts must contain'),
    'related_posts_unknown': ('related_posts', ['/missing-post/'], 'related_posts target does not resolve to an EN post'),
    'glossary_unknown': ('glossary_terms', ['missing'], 'glossary_terms must be'),
    'glossary_type': ('glossary_terms', 'apy', 'glossary_terms must be'),
    'disclosure_unknown': ('disclosure', ['unknown'], 'disclosure must be'),
    'disclosure_type': ('disclosure', 'pharos', 'disclosure must be'),
    'og_panel': ('og_panel', 0, 'og_panel must be bool'),
    'image_position': ('imagePosition', 50, 'imagePosition must be a string'),
    'image_meta_mapping': ('image_meta', [], 'image_meta must map'),
    'image_meta_entry': ('image_meta', {'/image.png': 'alt'}, 'image_meta must map'),
    'image_meta_alt': ('image_meta', {'/image.png': {'alt': False}}, 'image_meta must map'),
    'image_meta_caption': ('image_meta', {'/image.png': {'caption': 1}}, 'image_meta must map'),
}


def fm_test(case):
    def test(self):
        field, value, error = case
        fm = copy.deepcopy(self.frontmatter)
        target = fm
        parts = field.split('.')
        for part in parts[:-1]:
            target = target[part]
        if value is None:
            target.pop(parts[-1], None)
        else:
            target[parts[-1]] = value
        self.write_frontmatter(fm)
        self.run_validator('validate-frontmatter.py', failure=error)
    return test


for name, case in FM_DEFECTS.items():
    setattr(ValidatorTests, 'test_frontmatter_' + name, fm_test(case))


def french_ids(self):
    self.glossary['fr']['terms'] = [term for term in self.glossary['fr']['terms'] if term['id'] != 'apy']
    (self.root / 'data/glossary.json').write_text(json.dumps(self.glossary))
    self.write_frontmatter(self.frontmatter, 'fixture.fr.md')
    self.run_validator('validate-frontmatter.py', failure='glossary_terms must be')


ValidatorTests.test_frontmatter_language_specific_ids = french_ids

GLOSSARY_DEFECTS = {
    'duplicate_id': ('id', 'apr', 'duplicate ID'),
    'duplicate_name': ('term', 'apr', 'duplicate term name'),
    'category': ('category', 'missing', 'category is not declared'),
    'related_target': ('related_terms', ['missing'], 'related_terms contains unknown IDs'),
    'alias': ('aliases', ['https://example.org/'], 'aliases must be site paths'),
    'index': ('index', 'false', 'index must be bool'),
    'guide_unknown': ('related_guides', ['/missing-hub/'], 'related_guides target does not resolve to a hub page'),
    'guide_type': ('related_guides', '/yield/', 'related_guides must be site paths'),
    'guide_external': ('related_guides', ['https://example.org/hub/'], 'related_guides must be site paths'),
    'article_case': ('related_articles', [{'url': '/Guide/'}], 'related_articles URLs'),
    'article_slash': ('related_articles', [{'url': '/guide'}], 'related_articles URLs'),
    'article_relative': ('related_articles', [{'url': 'guide/'}], 'related_articles URLs'),
    'article_http': ('related_articles', [{'url': 'http://example.org/guide/'}], 'related_articles URLs'),
    'article_protocol_relative': ('related_articles', [{'url': '//example.org/guide/'}], 'related_articles URLs'),
    'article_absolute_internal': ('related_articles', [{'url': 'https://tokenbrice.xyz/guide/'}], 'related_articles URLs'),
}


def glossary_test(case):
    def test(self):
        field, value, error = case
        self.glossary['en']['terms'][0][field] = value
        path = self.root / 'data/glossary.json'
        path.write_text(json.dumps(self.glossary))
        self.run_validator('validate-glossary.py', path, failure=error)
    return test


for name, case in GLOSSARY_DEFECTS.items():
    setattr(ValidatorTests, 'test_glossary_' + name, glossary_test(case))


def parity_defect(self):
    self.glossary['fr']['terms'].pop()
    path = self.root / 'data/glossary.json'
    path.write_text(json.dumps(self.glossary))
    self.run_validator('validate-glossary.py', path, failure='EN/FR ID parity')


ValidatorTests.test_glossary_language_parity = parity_defect

if __name__ == '__main__':
    unittest.main(verbosity=2)

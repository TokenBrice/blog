## tokenbrice.xyz

> Brutally honest DeFi, built on a privacy-respecting static stack.

This repository contains the bilingual EN/FR TokenBrice blog. It is built with Hugo Extended `0.161.1`, a fork of `hugo-theme-stack`, self-hosted assets, and Matomo analytics.

[![Generator is Hugo](https://img.shields.io/badge/Generator%20is-Hugo-ff4088?&logo=hugo)](https://github.com/gohugoio/hugo)
[![Source on GitHub](https://img.shields.io/badge/Source%20on-GitHub-181717?&logo=github)](https://github.com/tokenbrice/blog/)

### Local development

```sh
make setup
make serve
```

Open `http://localhost:1313`.

Docker is also available:

```sh
docker-compose up -d --build
```

### Verification

Use the same checks CI uses before shipping:

```sh
make verify
```

The verification path runs:

- validator regression fixtures (synthetic sites, independent of `public/`)
- bilingual glossary IDs, categories, references and URL validation
- front matter validation, including context notes, takeaways, disclosures and image metadata
- content safety validation for raw scripts/iframes and missing image alt text
- TypeScript typechecking
- modern image freshness and dimension generation
- Hugo production build
- generated-site references, sitemap/canonical/noindex consistency, reciprocal hreflang, breadcrumbs and OG image dimensions

Individual commands are also available:

```sh
make validate
npm run validate:glossary
npm run test:validators
make validate-content
make typecheck
make build
make validate-site
```

Python validators need Python 3 and PyYAML (`python3 -m pip install PyYAML`).
Title length remains a warning. Output validation accepts an explicit disposable build directory:
`python3 scripts/validate-site-output.py /path/to/build`.

The publishing workflow runs Lighthouse independently of deploy on the exact Pages artifact:
three mobile samples per URL, median assertions and warn-only performance/byte budgets.
Reports stay in the `lighthouse-reports` GitHub Actions artifact, not public temporary storage.
Lighthouse failures never block deployment.

IndexNow is also non-blocking. Before deployment, `scripts/indexnow.py prepare` fetches the
live sitemap index and its children, then saves only new or `lastmod`-changed canonical URLs
from the build. Alias and noindex pages are excluded. After a successful deployment,
`scripts/indexnow.py submit indexnow-urls.json` verifies the live key and submits batches of
at most 10,000 URLs. A failed live-sitemap fetch skips submission rather than treating the
entire site as new; unchanged deployments send nothing. This does not replace Google
Search Console or guarantee indexing. The key is published at
`/69be76f58f52061d7a60b37f25278c4c.txt`.

Inspect a diff without writing or submitting it:
`python3 scripts/indexnow.py prepare --public public --dry-run`.
Inspect an already prepared payload without network submission:
`python3 scripts/indexnow.py submit indexnow-urls.json --dry-run`.

### Assets

Static images live under `static/img`. All three image targets use the same freshness-aware
pipeline; run any one after adding or replacing a master:

```sh
bash scripts/build-images.sh
# Equivalent: make webp, make avif, or make imgdims
```

The script regenerates missing or stale WebP/AVIF siblings, then refreshes
`data/imageDims.json` in a batched scan, including AVIF entries. It requires Python 3,
ImageMagick, `cwebp` and `avifenc` (the encoders are used only for missing/stale siblings).
The dimensions are used by render hooks to reduce layout shift.

### Search

The site uses the theme JSON search index at `/search/index.json` and `/fr/search/index.json`. Pagefind is intentionally not built in CI so there is a single search path.

### Privacy

The client-side Matomo integration disables cookies and avoids sending raw search terms or clicked URLs. Search analytics are bucketed by query length, and social clicks are recorded by host only.

IP anonymization, retention, and opt-out behavior must be enforced in the Matomo server configuration. Keep those settings aligned with the CNIL-friendly privacy claim before changing analytics behavior.

### Content Rules

- Do not add raw `<script>` tags in Markdown content.
- Raw `<iframe>` embeds must use `youtube-nocookie.com` and include a `title`.
- Markdown images must include alt text.
- Prefer shortcodes or layout partials for embeds and structured data.

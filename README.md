## tokenbrice.xyz

> Brutally honest DeFi, built on a privacy-respecting static stack.

This repository contains the bilingual EN/FR TokenBrice blog. It is built with Hugo Extended `0.161.1`, a fork of `hugo-theme-stack`, self-hosted assets, and Matomo analytics.

[![Generator is Hugo](https://img.shields.io/badge/Generator%20is-Hugo-ff4088?&logo=hugo)](https://github.com/gohugoio/hugo)
[![Source on GitHub](https://img.shields.io/badge/Source%20on-GitHub-181717?&logo=github)](https://github.com/tokenbrice/blog/)

### Local development

Use Node.js 24 LTS (see `.nvmrc`) and npm, alongside Hugo Extended `0.161.1`.
The browser/audit tooling no longer supports Node.js 20. With nvm, run `nvm use`
before installing dependencies.

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
- generated-site references, sitemap/canonical/noindex consistency, reciprocal hreflang, breadcrumbs and OG image dimensions (1200×630 cards for indexable pages)

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
Titles must be 5–70 characters. Output validation accepts an explicit disposable build directory:
`python3 scripts/validate-site-output.py /path/to/build`.

Pull requests run a separate, read-only validation workflow; they do not deploy.
After building, run `npm run test:browser` with Chrome or Chromium installed
(`CHROME_PATH=/path/to/chrome` if it is not in a standard Linux location).
These smoke tests serve the production artifact locally, block third-party
requests, and cover keyboard navigation, short/mobile layouts, bilingual
project links, search, glossary filters, and responsive images. Screenshots are
saved to `lighthouse-reports/browser-smoke` and retained as a PR CI artifact.

The publishing workflow runs Lighthouse independently of deploy on the exact Pages artifact:
three mobile samples per URL, median assertions and warn-only performance/byte budgets.
Run the same locked audit locally with `npm run lighthouse:ci` after building.
PR validation also exercises this full audit; missing reports, invalid metrics, or a
broken audit tool fail validation, while ordinary budget warnings remain non-blocking.
`npm run test:tooling` tests those report checks. See
[`docs/dependency-audit.md`](docs/dependency-audit.md) for upgrade rationale and override maintenance.
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

### Writing and front matter

Start posts with `hugo new content/post/YYYY/slug.md`. Fill the draft's title
(5–70 characters), description (aim for 50–160), date, category list, tags,
cover image and difficulty (`beginner`, `intermediate`, `expert`). Keep existing
category URLs: `format` describes the writing, it does not replace categories.
Tags are displayed as plain text, not links to the noindex tag archives.

Optional post fields, in YAML:

```yaml
format: analysis # analysis | thesis | practical | tutorial
noindex: true # Use only when intentionally keeping a page out of indexes.
lastmod: 2026-10-01 # Set lastmod to context.checked, never cosmetically.
context:
  kind: historical # historical | status | update
  checked: 2026-10-01
  text: "This analysis records the design at publication, not today's configuration."
  sources: [] # Primary HTTPS links; non-empty for status notes.
takeaways:
  - "Check the current parameters before acting."
  - "Separate the mechanism from its implementation."
related_posts: ["/money-markets-risk/", "/vaults/"]
glossary_terms: ["apy", "vault"]
disclosure: ["pharos"] # IDs from data/projects.yaml; roles, never holdings.
imagePosition: "50% 20%"
og_panel: false
image_meta:
  "/img/2021/reflexer-rai/control-theory.png":
    alt: "Feedback loop adjusting the redemption rate."
    caption: "The controller's feedback loop."
```

Omit fields you do not need. `noindex` emits `noindex,follow` and excludes the
page from the sitemap and search index. Context text supports inline Markdown,
is limited to 400 characters, and must have a verified, non-future `checked`
date. Any current-status claim needs primary-source links, whatever its kind.
Takeaways contain 2–3 short localized bullets and can appear without a context
note. `related_posts` accepts at most two **EN canonical paths**, including in
French posts: the template finds the same-language translation, otherwise EN,
then fills remaining slots with automatic related posts. `glossary_terms`
overrides automatic concept detection; use `glossary_terms: []` to opt out.
`imagePosition` controls cover cropping. `image_meta` keys must match the image
source exactly as written in Markdown; `alt` and `caption` are optional strings.

Hub pages use EN canonical paths too. Core entries must precede historical ones;
`note` is optional localized plain text:

```yaml
reading_path:
  - path: /money-markets-risk/
    group: core
  - path: /vaults/
    group: historical
    note: "Read for the mechanism, then verify the current deployment."
```

Place `{{< reading-path >}}` in the hub body. Optional `group="core"` or
`group="historical"` splits the sequence without renumbering. Missing French
translations remain EN links with a visible label. The guides landing page uses
`mode="tiles"` and a `category` slug on each entry for local category artwork.

Glossary terms live in both language records in `data/glossary.json`, with the
same term ID. Optional additions to an existing term record:

```json
{
  "aliases": ["/glossary/old-term/"],
  "difficulty": "beginner",
  "related_guides": ["/stablecoins-guide/"],
  "index": false
}
```

`aliases` creates redirects, `difficulty` uses the same three levels as posts,
`related_guides` links to guide pages, and `index: false` makes the generated term
page noindex. Omit `index` to keep it indexable.

Hugo generates localized 1200×630 JPEG OG cards at build time from local fonts
and artwork. Posts use a dark ink text column plus an available PNG/JPG cover
panel on the right; `og_panel: false` forces text-only. Hubs, pages and glossary
terms are text-only. There is no separate OG generation command. After changing
image masters, run `bash scripts/build-images.sh` as described above. Lighthouse
and IndexNow are independent, warn-only/non-blocking publishing jobs; see
Verification for their reports and submission rules.

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

# SEO Plan — September 2026

Source: Google Search Console (sc-domain:tokenbrice.xyz, data to 2026-09-09) cross-checked against the live site and this repo at commit 73b2da1.

## 1. Snapshot

| Metric | Value | Note |
|---|---|---|
| Indexed / not indexed | 410 / 458 | 231 of the 410 are glossary terms |
| Clicks / impressions (3 mo) | 97 / 24.8K | CTR 0.4 %, avg position 11.4 |
| Clicks / impressions (property lifetime, since mid-May 2026) | 126 / 33.2K | |
| Crawl requests (90 d) | 3.9K | 10 % are 404s (358 hits), 13 % discovery |
| Sitemaps | index OK; `/en/` 647 errors, `/fr/` 292 errors, 0 URLs discovered | children last read Jan 2026 |
| External links | 303 (medium, gate, reddit, listennotes) | |
| Internal links | 8.3K; #2 target is `http://tokenbrice.xyz/archives/` (421) | HTTP, not HTTPS |
| Rich results | Breadcrumbs 87 valid, Profile page 1 valid | no errors |
| Manual actions / security | none | |
| Core Web Vitals | no field data (traffic too low) | |

Traffic split: France 37 clicks / 1.8K impressions; United States 7 clicks / 12.5K impressions (CTR 0.1 %). Desktop 21K impressions at 0.2 % CTR, mobile 3.7K at 1.2 %.

## 2. What the 458 "not indexed" URLs actually are

| Bucket | Count | Breakdown | Verdict |
|---|---|---|---|
| Excluded by noindex | 252 | 243 tag pages (130 FR) + `/series/`, `/categories/`, `/page/`, `/fr/search/`, one external-canonical post | Working as designed. Nothing to do. |
| Crawled, currently not indexed | 156 | ~55 glossary terms, ~25 posts (mostly FR translations and 2017–2019 posts), ~40 tag/category/pagination URLs, ~15 dead `index.xml` feeds, ~8 http/query-string/no-slash variants | Half is noise that Tier 0–1 removes; the rest is a content-quality signal (see §5). |
| Not found (404) | 30 | legacy `/posts/YYYY/slug/` scheme, lowercase forms of mixed-case URLs, `/fr/about/`, `/es/` | Fixable with aliases (Tier 1). |
| Alternate page with proper canonical | 13 | 10 are `http://` variants, 3 are query-string variants | Disappears once HTTPS is enforced. |
| Page with redirect | 4 | www variants, `/Stablecoins/`, no-trailing-slash | Fine. |
| Duplicate without user-selected canonical | 2 | `http://…/index.xml`, `http://…/fr/index.xml` | Disappears with HTTPS enforcement. |
| Blocked by robots.txt | 1 | `http://tokenbrice.xyz/search/` | Fine. |

Verified as correct and needing no work: hreflang pairs (EN/FR/x-default on posts and category hubs), `www` → apex 301s, robots.txt, canonical tags, tag-page noindex, BreadcrumbList / BlogPosting / DefinedTerm JSON-LD, `<html lang>` on FR pages, self-hosted fonts, image `srcset`/lazy-loading.

## 3. Tier 0 — settings only, do today (no code, no content)

### 3.1 Enforce HTTPS on GitHub Pages
`http://tokenbrice.xyz/`, `/archives/`, `/fr/`, `/pharos/` all return **200 over plain HTTP with no redirect**. Consequences visible in GSC: `http://tokenbrice.xyz/archives/` is *indexed*, 10 of the 13 "alternate canonical" URLs and both "duplicate" URLs are `http://`, GSC counts 421 internal links to the HTTP archive URL, and Googlebot spends crawl on both schemes.
Fix: repository → Settings → Pages → tick **Enforce HTTPS**. GitHub then 301s every HTTP request. Zero code.

### 3.2 Resubmit sitemaps and delete the typo
GSC last read `/en/sitemap.xml` on 2026-01-29 and `/fr/sitemap.xml` on 2026-01-04 and still shows 647 / 292 "Invalid URL" errors and 0 discovered URLs from that read. The live files are valid today (266 EN + 254 FR URLs). Also `/fr/sidemap.xml` (typo, submitted 2022) is still listed as "couldn't fetch".
Fix in GSC → Sitemaps: remove `/fr/sidemap.xml`; submit `https://tokenbrice.xyz/en/sitemap.xml` and `https://tokenbrice.xyz/fr/sitemap.xml` again so they get a fresh read. Do this after 4.2 ships if you can, otherwise now and again later.

### 3.3 After Tier 1 ships: URL-inspect and request indexing
Inspect `/page/2/`, `/glossary/`, `/fr/glossary/`, `/categories/dex/page/2/` to confirm the new robots/sitemap state, and use "Request indexing" on `/glossary/` and `/fr/glossary/`.

## 4. Tier 1 — template / config / front-matter fixes (no content changes)

### 4.1 Pagination pages are indexable (bug) — HIGH
`layouts/partials/head/head.html:21` detects pagination with `strings.Contains .RelPermalink "/page/"`. Hugo does not change `.RelPermalink` on pager pages, so this is never true. Live result: `/page/2/` … `/page/9/`, `/fr/page/N/`, `/categories/*/page/2/` ship **no noindex**, canonical pointing at page 1, and the title `Pager 2 | TokenBrice` (the `%s` of a Pager object). GSC has 7 of them indexed and another ~10 in "crawled, not indexed".
Fix (templates only):
1. Add `layouts/partials/helper/paginator.html` that computes the page set the way `layouts/index.html:4`, `layouts/_default/list.html:106` and `layouts/_default/taxonomy.html:89` do and returns `.Paginate $pages`. Hugo initialises a page's paginator once (first call wins, later calls return the same pager), so the head partial can call it first as long as it uses the same set; switch the three list templates to the same partial.
2. In `head.html` replace line 21 with: paginated = kind in (home, section, taxonomy, term) **and** `(partial "helper/paginator.html" .).PageNumber` > 1.
3. In `themes/hugo-theme-stack/layouts/partials/data/title.html:12` render `Page N | TokenBrice` from `.Paginator.PageNumber` instead of printing the Pager object.
4. Extend `scripts/validate-site-output.py` to fail if any `**/page/[2-9]*/index.html` lacks `noindex`.

### 4.2 Sitemap: dishonest lastmod, missing glossary hubs — HIGH
- Every `<lastmod>` in `/en/sitemap.xml` (114 of them) is `2026-05-19`, the date of the mass "add p/ aliases" commit, because `enableGitInfo: true` and no post has a `lastmod` field. A single identical date across the site tells Google the value is unreliable, so it ignores it. The same value feeds `dateModified` in JSON-LD for the 70 posts without `reviewed`.
- `/glossary/` and `/fr/glossary/` (345 and 304 internal links, the site's biggest hubs) are absent from the sitemap because `layouts/_default/sitemap.xml:1` seeds from `RegularPages`, which excludes section pages.
Fix:
1. Rename `reviewed:` → `lastmod:` in the 87 posts that have it (mechanical sed; update `jsonld.html:92-97` and `validate-frontmatter.py:124` which already expect `lastmod`), and set in `hugo.yaml`: `frontmatter: { lastmod: ["lastmod", "date"] }` to stop using git dates. Sitemap, JSON-LD and `article:modified_time` become truthful with one config line.
2. In `sitemap.xml`, append the glossary section pages (`where .Site.Pages "Type" "glossary" | where Kind section`).
3. Optional: emit `<xhtml:link rel="alternate" hreflang>` per URL (Hugo's default template does; the custom one dropped it). In-page hreflang already works, so this is a nice-to-have.

### 4.3 Legacy URL scheme still crawled → 404 — MEDIUM
88 of the 358 404 crawl hits in 90 days and ~20 of the 30 GSC 404s are the pre-2020 pattern `/posts/YYYY/<file-stem>/` (also `/fr/posts/…`, `/es/posts/…`), e.g. `/posts/2019/attention-economy/`, `/posts/2020/algorithmic-stablecoins/`, `/posts/2021/seigniorage-basis-vs-esd/`. Each maps to `content/post/YYYY/<stem>.md`.
Fix: one script (same shape as commit 6e68495) adding `posts/YYYY/<lowercase stem>` to each post's `aliases`, FR posts get `fr/posts/YYYY/<stem>`. Extend the `validate-frontmatter.py` alias rule to require it. Aliases are meta-refresh pages on GitHub Pages, but GSC already treats them as redirects (see the "Page with redirect" bucket).

### 4.4 Mixed-case and accented URLs — MEDIUM
Google requests the lowercase / unaccented form and gets a 404: `/ecocrypto-manifesto/`, `/users-privacy/`, `/venft-infrastructure/`, `/fr/dex-echanges-decentralisees-capture-valeur/`. Live URLs are `EcoCrypto-manifesto`, `users-Privacy`, `veNFT-infrastructure`, `dex-echanges-decentralisées-capture-valeur`, `nft-cas-d'utilisation`, `Blockchain-telco`.
Fix (front matter only, 10 files under `content/post/`): set `url:` to the lowercase ASCII slug and move the old value into `aliases`. Also add `recettes-marches-d-actifs`-style aliases for the accented FR legacy URLs seen in the 404 log.

### 4.5 Small crawl-waste items — LOW
- `ads.txt`: 179 of the 358 404 hits. Add an empty `static/ads.txt` (a comment line is enough) to stop the daily 404.
- `/page/` and `/fr/page/page/2/`: the `content/page` section renders a paginated listing nobody links to (noindexed, still crawled). Add `content/page/_index.md` with `build: { render: never, list: never }`.
- Category and tag `<title>`s read `Category: DEX | TokenBrice`, `Tag: Defi | TokenBrice` (`data/title.html:24`). For the 22 indexable category hubs use the hub's own `title` from `_index.md`; drop the `Category:` prefix.
- `hugo.yaml:39` `rssLimit` is a legacy key ignored by `layouts/_default/rss.xml:17`; move to `services.rss.limit`.
- `data/title.html:8-12` calls `.Paginate` inside a `partialCached` title partial; once 4.1's helper exists, use it there too and drop the duplicate paginator build.

## 5. Tier 2 — CONTENT CHANGES REQUIRED (explicit)

Nothing in this section can be done from templates alone.

### 5.1 Click-through rate — rewrite titles and descriptions on the pages that already rank
24.8K impressions produced 97 clicks. The site ranks on page 1 for queries it never gets clicked on. Highest-leverage pages (3 months):

| Page | Impressions | Clicks | Avg pos |
|---|---|---|---|
| `/pharos/` | 2,263 | 15 | 7.0 |
| `/attention-economy/` | 1,478 | 5 | 11.2 |
| `/reflexer-rai/` | 1,381 | 1 | 7.4 |
| `/defi-bullshit-detector/` | 675 | 3 | 14.6 |
| `/` (home) | 651 | 25 | 5.4 |
| `/lusd-chicken-bonds/` | 289 | 1 | 11.9 |
| `/badger-digg/` | 244 | 1 | 8.3 |
| `/pegged-assets-swap/` | 238 | 1 | 12.9 |
| `/fr/glossary/vault/` | 231 | 3 | 6.4 |
| `/glossary/health-factor/` | 223 | 2 | 7.2 |
| `/pool-together/` | 204 | 1 | 28.7 |

Queries with volume and zero clicks: "attention economy" (894 impressions, position 9.3), "the attention economy" (108), "pmav.fun hook beforeremoveliquidity" family (~250, Maverick), "mav xyz" (141), "health factor" (96), "l'attaque sandwich" (92), "grid trading" (83), "twap"/"twap meaning" (90), "velodrome v2 defi protocol review" (55).
Action: for each of the ~12 pages above, rewrite the front-matter `title` (the search snippet headline) and `description` to match the query intent, and check the H1/opening paragraph answers it in the first 100 words. `validate-frontmatter.py` already enforces the 5–70 / 50–160 character bounds.

### 5.2 Thin glossary terms (≈55 "crawled, not indexed")
Examples: `/glossary/ve-3-3/`, `/glossary/price-impact/`, `/glossary/honeypot/`, `/glossary/staking/`, `/glossary/market-cap/`, `/glossary/bridge/`, `/glossary/amm/`, `/glossary/dex/`, `/fr/glossary/ethereum/`, `/fr/glossary/smart-contract/`, `/fr/glossary/defi/`, `/fr/glossary/liquidation/` … Google crawled them and chose not to index: the definitions are too short or too generic to beat existing results. 231 other terms *are* indexed, so the format works when the entry has substance.
Action: in `data/glossary.json`, expand the ~55 entries (worked example, why it matters, one internal link to the post that uses it) or merge the generic ones into a richer parent term. Template work is not the lever here.

### 5.3 Posts crawled but not indexed (~25)
Mostly FR translations (`/fr/balancer-wars/`, `/fr/defi-vs-inflation/`, `/fr/unstoppable-defi/`, `/fr/algorithmic-stablecoins/`, `/fr/defi-collective/`, `/fr/money101/` …) and 2017–2019 posts (`/hello-world/`, `/advertising-model/`, `/reddit-hitchhiker-guide/`, `/demise-ns/`, `/seo-content-tools/`). Decide per post: refresh (content), leave as is, or add `hidden: true` so it drops out of the sitemap (front matter, but an editorial call).

### 5.4 Tag normalisation backlog
`docs/seo/taxonomy-normalization.md` already lists the duplicates (88MPH/88mph, PoolTogether/Pooltogether …). Tags are noindexed so this has no direct ranking effect; it only matters if a tag is later promoted to a hub.

## 6. Verification and monitoring

- After 4.1 + 4.2 deploy: `curl -s https://tokenbrice.xyz/page/2/ | grep -o '<meta name=robots[^>]*>'` must print `noindex,follow`; `/en/sitemap.xml` must contain `/glossary/` and varied `<lastmod>` values.
- After 3.1: `curl -sI http://tokenbrice.xyz/` must return 301 → https.
- GSC, 4–6 weeks later: "Alternate page with proper canonical" → ~3, "Duplicate without user-selected canonical" → 0, "Not found" ≤ 10, pagination URLs gone from Indexed, glossary hubs in "View data about indexed pages", sitemaps showing ~270 / ~255 discovered.
- Keep the monthly loop in `docs/seo/search-measurement.md`; feed the GSC page export through `scripts/summarize-search-console.py` and track CTR on the §5.1 pages specifically.

## 7. Suggested order and effort

| # | Item | Effort | Content change |
|---|---|---|---|
| 3.1 | Enforce HTTPS | 1 min | no |
| 3.2 | Resubmit sitemaps, delete typo | 2 min | no |
| 4.1 | Pagination noindex + title | ~1 h | no |
| 4.2 | lastmod truthfulness + glossary hubs in sitemap | ~1 h | no (front-matter key rename) |
| 4.3 | Legacy `/posts/YYYY/` aliases | ~30 min scripted | no |
| 4.4 | Lowercase 5 mixed-case URLs | 15 min | no |
| 4.5 | ads.txt, page-section listing, titles, rssLimit | ~45 min | no |
| 5.1 | Title/description rewrites on ~12 ranking pages | 2–3 h | **yes** |
| 5.2 | Expand ~55 thin glossary entries | days | **yes** |
| 5.3 | Decide on ~25 unindexed old/FR posts | editorial | **yes** |

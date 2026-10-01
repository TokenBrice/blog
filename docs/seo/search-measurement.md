# Organic Search Measurement Loop

Review monthly, and after template or content-architecture releases.

## Search Console

- Export clicks, impressions, CTR, and average position by page and query.
- Save the monthly CSV export outside the repo or under a dated private notes folder, then summarize it with:
  `python3 scripts/summarize-search-console.py path/to/search-console.csv > path/to/baseline-summary.csv`
- Group pages by language, page type, and topic cluster: posts, categories, series, glossary terms, pillar pages, and utility pages.
- Track decay for older DeFi content, especially stablecoins, lending, Curve/veCRV, Aave, Liquity, and yield articles.
- After structured-data releases, inspect representative URLs and watch rich-result/error reports for Articles and Breadcrumbs.
- Use sitemap submission as a crawl hint, then compare sitemap URLs against indexed/canonical URLs.

## Matomo Events

Pageview URLs contain only the current origin and pathname, site-wide: query strings
and fragments are removed before `trackPageView`. Same-origin referrer URLs are
also reduced to origin and pathname. This keeps `/search/?keyword=…` and search
referrers from sending raw queries to Matomo; external referrers are unchanged.

The local tracking script records:

- `Search / Site search`: one event for each `tb:search-settled` update. The name is
  `lengthBucket / resultBucket`, never the raw query, result title or URL. Length buckets
  are `1-10`, `11-30`, `31-60`, `61+`; result buckets are `0`, `1-5`, `6-20`, `21+`.
  Empty queries should not dispatch a settled event. There are no submit/change search
  handlers, so a settled query is not counted again on blur or submission.
- `Distribution / <purpose> / <placement>`: CTA hooks distinguish intent and location.
  Purpose is `rss`, `announcements`, `follow`, `watch` or `contact`; placement is
  `sidebar`, `post-end`, `subscribe`, `footer` or `home`. Annotated CTA clicks emit only
  this event, not the fallback RSS/social event as well.
- `Distribution / RSS click / feed`: unannotated feed links.
- `Distribution / Social click / <host>`: unannotated Telegram, X/Twitter,
  Farcaster/Warpcast and YouTube links. Hosts only, never clicked URL paths.
- `Navigation / Language switch`: translation anchors and the language select in
  `#i18n-switch`. Select changes use the target language's visible label as the name.
- `Content / Project click / internal-project`: internal project-oriented pages.

The client keeps Matomo cookieless. These events measure click/search intent, not
completed subscriptions, platform follows, identifiable users or cross-platform funnels.
Compare post-end versus sidebar intent and zero-result query buckets, rather than
assuming a social exit was a successful subscription.

## Bing and IndexNow

- Verify Bing Webmaster ownership and submit `https://tokenbrice.xyz/sitemap.xml`.
- The publishing workflow prepares a live-versus-built sitemap diff before deploy.
  Only new canonical URLs or changed `lastmod` values qualify; aliases and noindex pages
  are filtered out. No raw user data is involved.
- A successful deployment triggers a non-blocking IndexNow submission after checking
  the live verification key. Reports are in Actions logs; HTTP receipt is not indexing.
- A failed live-sitemap fetch does not fall back to a full-site submission.
- Continue the Search Console URL-inspection/export loop for Google: IndexNow is not
  Google's indexing API and does not replace sitemaps or engine verification.

## Decisions

- Refresh pages with high impressions, low CTR, and stable rankings before creating new content.
- Add internal links from pages with traffic to relevant pillar, glossary, and series hubs.
- Promote series or tags into indexable hubs only when they have enough supporting content and clear search demand.
- Keep tag pages noindexed unless a tag is promoted into a curated category, series, or pillar page.

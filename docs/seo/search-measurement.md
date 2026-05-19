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

The local tracking script records:

- `Search / Site search` for internal search terms.
- `Distribution / RSS click` for feed links.
- `Distribution / Social click` for Telegram, X/Twitter, Farcaster/Warpcast, and YouTube exits.
- `Navigation / Language switch` for translation links.
- `Content / Project click` for project-oriented pages.

## Decisions

- Refresh pages with high impressions, low CTR, and stable rankings before creating new content.
- Add internal links from pages with traffic to relevant pillar, glossary, and series hubs.
- Promote series or tags into indexable hubs only when they have enough supporting content and clear search demand.
- Keep tag pages noindexed unless a tag is promoted into a curated category, series, or pillar page.

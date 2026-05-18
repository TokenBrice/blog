# Taxonomy normalization

This note records the current taxonomy cleanup rules for the blog. It is data guidance only; post front matter should be updated in a separate content pass.

## Rules

- Use canonical title case for broad category names: `Analysis`, `DEX`, `Lending`, `NFT`, `Practical`, `Privacy`, `Projects`, `Stablecoin`, `Thesis`, `Tutorial`, `Yield`.
- Keep protocol, product, and token tickers in their official casing: `Aave`, `Curve`, `CRV`, `LUSD`, `veCRV`, `veVELO`, `GHO`, `RAI`.
- Use one spelling per concept across languages unless the tag is intentionally locale-specific.
- Prefer singular conceptual tags for topic pages unless the product or common industry name is plural, for example `Stablecoins` can remain a cluster tag.
- Prefer specific tags over duplicated broad tags when both are present and one is redundant.
- Do not create new spelling variants for aliases; map them to the canonical tag in the cleanup backlog first.

## Current backlog

- Casing variants: `88MPH`/`88mph`, `EcoCrypto`/`ecocrypto`, `PoolTogether`/`Pooltogether`, `SushiSwap`/`Sushiswap`, `Stablecoins`/`stablecoins`.
- Spelling fixes: `data harversting` -> `data harvesting`, `Impermanent Lossses` -> `Impermanent Loss`, `Yean Finance` -> `Yearn Finance`.
- Concept aliases: `ad model` -> `advertising model`, `Decentralisation` -> `decentralization`, `Leveraging` -> `Leverage`, `Aggregator` -> `Aggregation` or a more specific protocol tag.
- NFT aliases: `non fungible tokens`, `Non Fungible Tokens`, `NFT Farming`, `Farming NFT`, and `Achat de NFT` need one intentional canonical structure.
- DeFi locale variants: `Finance Décentralisée` and `Finance décentralisée` should either normalize to `DeFi` or be kept only on French-language posts.
- Risk tags: `aave risk`, `compound risk`, `cream risk`, `money market risk`, `Risk assessment`, `Risk Management`, and `Risk Scoring` need a consistent risk taxonomy.
- Project/site tags: `TokenBric.xyz` should be corrected or merged into `TokenBrice.xyz`.
- Glossary tags should remain lowercase, hyphenated where needed, and should not be mixed directly with post tags until a mapping layer exists.

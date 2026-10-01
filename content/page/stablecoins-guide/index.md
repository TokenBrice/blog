---
title: "Stablecoins: Pegs, Backing and Depeg Risks"
description: "Understand stablecoin pegs, collateral, control and liquidity. A no-hype reading path through TokenBrice's design comparisons and risk analysis."
slug: stablecoins-guide
date: 2026-05-18
lastmod: 2026-10-01
toc: true
readingTime: false
reading_path:
  - { path: "/stablecoin-marauder-map/", group: core, note: "Start with the map: AMOs, PSMs, redemptions and pegKeepers." }
  - { path: "/reflexer-rai/", group: core, note: "ETH collateral and a floating redemption price, not a dollar peg." }
  - { path: "/liquity-protocol/", group: core, note: "Liquity V1: LUSD, redemptions and the Stability Pool. Not a V2 guide." }
  - { path: "/pharos/", group: core, note: "Stablecoin monitoring, built by me. A dashboard is not a safety guarantee." }
  - { path: "/why-polaris/", group: core, note: "The stablecoin thesis behind a project I co-founded and now advise." }
  - { path: "/lusd-chicken-bonds/", group: historical, note: "The 2022 LUSD bonding design, not current operating instructions." }
  - { path: "/aave-gho-stablecoin/", group: historical, note: "The 2022 GHO design proposal and its lending roots." }
  - { path: "/ethereum-stable-assets/", group: historical, note: "The 2021 taxonomy of stable and pegged assets." }
  - { path: "/seigniorage-basis-esd/", group: historical, note: "A 2021 comparison of Basis and ESD seigniorage mechanics." }
  - { path: "/algorithmic-stablecoins/", group: historical, note: "The 2020 supply-adjustment experiments and their fragility." }
  - { path: "/stablecoins/", group: historical, note: "The 2018 adoption thesis, before today's stablecoin landscape." }
---

Stablecoins are DeFi's main unit of account, source of liquidity, and largest bridge between crypto markets and real-world balance sheets. Understanding them requires more than sorting tokens by market cap: the useful question is what keeps the peg, what backs the liability, who can intervene, and where the liquidity comes from.

## Reading Path

{{< reading-path >}}

## Core Concepts

- [Stablecoin](/glossary/stablecoin/) explains the basic primitive.
- [Depeg](/glossary/depeg/) is the failure mode every design must manage.
- [Collateral](/glossary/collateral/) and [overcollateralization](/glossary/overcollateralization/) define the backing side.
- [Seigniorage](/glossary/seigniorage/) covers one family of algorithmic designs.
- [Money markets](/glossary/money-market/) explain why stablecoin demand is so tied to borrowing.

## Related Hubs

- [Stablecoin category](/categories/stablecoin/)
- [Stablecoin Arc](/series/stablecoin-arc/)
- [Pegged Assets](/series/pegged-assets/)
- [Lending and Money Markets](/lending-money-markets/)
- [DeFi Risk](/defi-risk/)

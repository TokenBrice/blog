---
title: "DeFi Lending: Collateral, Rates and Risks"
description: "DeFi lending without the marketing fog: collateral, liquidation, rate models and aggregation. Follow the core analysis and risk-checking path."
slug: lending-money-markets
date: 2026-05-18
lastmod: 2026-10-01
toc: true
readingTime: false
reading_path:
  - { path: "/money-markets-risk/", group: core, note: "Risk first: the framework, not a ranking of today's markets." }
  - { path: "/lending-aggregation/", group: core, note: "What the aggregation layer changes, and what it merely hides." }
  - { path: "/lending-protocol-renaissance/", group: core, note: "The 2024 CDP and money-market designs and their trade-offs." }
  - { path: "/leverage-sir/", group: core, note: "A different leverage mechanism and the risks that come with it." }
  - { path: "/venft-infrastructure/", group: core, note: "When voting positions become collateral and leveraged yield." }
  - { path: "/reflexer-rai/", group: historical, note: "The 2021 RAI design: ETH collateral and a floating redemption price." }
  - { path: "/liquity-protocol/", group: historical, note: "Liquity V1's 2021 LUSD design, not Liquity V2 or BOLD." }
  - { path: "/money-market-innovations/", group: historical, note: "The 2021 design taxonomy, including Alchemix-style loans." }
  - { path: "/money-market-recipes/", group: historical, note: "The original 2021 strategy patterns. Parameters are not current instructions." }
  - { path: "/leveraging-eth/", group: historical, note: "A 2020 Maker borrowing recipe, not a current rate recommendation." }
---

Lending protocols are one of DeFi's root primitives. They let users borrow against collateral, supply assets for yield, build leveraged strategies, and issue stable assets. The surface looks simple, but the risk sits in collateral listings, oracle assumptions, liquidation design, governance, liquidity, and rate models.

## Reading Path

{{< reading-path >}}

## Core Concepts

- [Money market](/glossary/money-market/) and [lending](/glossary/lending/) define the primitive.
- [Borrowing](/glossary/borrowing/), [LTV](/glossary/ltv/), [health factor](/glossary/health-factor/), and [liquidation](/glossary/liquidation/) cover user-level risk.
- [Price oracle](/glossary/price-oracle/) is a core protocol dependency.
- [CDP](/glossary/cdp/) connects lending to stablecoin issuance.

## Related Hubs

- [Lending category](/categories/lending/)
- [Money Markets series](/series/money-markets/)
- [Stablecoins](/stablecoins-guide/)
- [DeFi Risk](/defi-risk/)
- [Yield](/yield/)

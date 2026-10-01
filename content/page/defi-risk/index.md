---
title: "DeFi Risk"
description: "An evergreen guide to DeFi risk across smart contracts, governance, oracles, collateral, liquidity, liquidations, bridges, market structure, and user operations."
slug: defi-risk
date: 2026-05-18
lastmod: 2026-10-01
toc: true
readingTime: false
reading_path:
  - { path: "/money-markets-risk/", group: core, note: "Start with dependencies and failure paths, not a safety score." }
  - { path: "/unstoppable-defi/", group: core, note: "Ask what can still be stopped, upgraded or captured." }
  - { path: "/defi-ux-disaster/", group: core, note: "Curation and user-facing risk are part of the protocol story." }
  - { path: "/defi-bullshit-detector/", group: core, note: "A research workflow for confronting claims, not a magic audit." }
  - { path: "/pharos/", group: core, note: "The stablecoin monitoring project I build. Signals are not guarantees." }
  - { path: "/farewell-glc/", group: historical, note: "My 2024 GHO committee departure: incentives, conflicts and governance language." }
  - { path: "/risk-tranching-defi/", group: historical, note: "The 2021 Saffron case: distributing risk does not remove it." }
  - { path: "/great-filter-defi/", group: historical, note: "The 2020 filter for separating durable mechanisms from fragile noise." }
---

DeFi risk is not one thing. It is a stack of technical, economic, governance, liquidity, and operational dependencies. The goal is not to find a risk-free protocol, but to understand what can fail, how losses propagate, and whether the compensation is worth the exposure.

## Reading Path

{{< reading-path >}}

## Risk Checklist

- Contract risk: audits, upgradeability, admin keys, bug bounties, and dependency contracts.
- Oracle risk: price source quality, update cadence, manipulation resistance, and fallback behavior.
- Collateral risk: liquidity, volatility, token permissions, bridge exposure, and centralization.
- Liquidation risk: market depth, keeper competition, bad debt, and cascading failures.
- Governance risk: multisigs, timelocks, quorum, capture, delegation, and emergency powers.
- User risk: approvals, phishing, wrong network, leverage, and position monitoring.

## Core Concepts

- [Smart contract](/glossary/smart-contract/), [audit](/glossary/audit/), and [bug bounty](/glossary/bug-bounty/) cover code risk.
- [Price oracle](/glossary/price-oracle/), [liquidation](/glossary/liquidation/), and [liquidation cascade](/glossary/liquidation-cascade/) cover market mechanics.
- [Multisig](/glossary/multisig/), [timelock](/glossary/timelock/), and [governance attack](/glossary/governance-attack/) cover control risk.
- [Bridge](/glossary/bridge/), [exploit](/glossary/exploit/), and [rug pull](/glossary/rug-pull/) cover common failure paths.

## Related Hubs

- [Analysis category](/categories/analysis/)
- [Money Markets](/series/money-markets/)
- [Lending and Money Markets](/lending-money-markets/)
- [Stablecoins](/stablecoins-guide/)
- [Governance](/governance/)

---
title: "Pharos: Free and Open Research-Grade Stablecoin Intelligence"
description: "150+ stablecoins tracked, peg monitoring, early warning scores, safety ratings, liquidity analysis, and more: a public good built to fill the stablecoin information vacuum."
date: '2026-03-12T01:13:50.191Z'
categories: [Projects]
tags: [DeFi, Stablecoin, Analytics, Public Good, Open Source]
url: pharos
image: /img/2026/pharos/pharos-cover.png
toc: true
draft: false
type: post
difficulty: "intermediate"
---

Stablecoins are the backbone of crypto. By every metric that matters — volume, users, real-world utility — they're the most successful thing DeFi has produced. Over $300B in circulating supply. Hundreds of billions in daily settlement. The bridge between onchain finance and the rest of the world. And yet, the information infrastructure around them is embarrassingly thin.

Want to know if a stablecoin is safe? Good luck. You can check its price on CoinGecko, maybe find a supply chart on DeFiLlama. For the most popular ones, [Bluechip](https://bluechip.org/) provides excellent economic ratings. But that's about it. **There is no systematic way to monitor peg stability, assess liquidity depth, detect early warning signals, track freeze events, or evaluate risk across the many stablecoins now in circulation.** The information layer is stuck in 2021 while the market has 10x'd in complexity.

This matters. When Terra collapsed, people didn't know their stablecoin was at risk until it was too late. When USDC depegged during the SVB crisis, panic spread because nobody had a clear picture of the actual exposure. Every depeg event follows the same pattern: information asymmetry benefits insiders and punishes everyone else.

So I built [Pharos](https://pharos.watch).

![Pharos dashboard homepage: Stability Index at 92.7 (BEDROCK), $329B total stablecoin supply, 128 of 148 coins at peg, daily digest headline, and the full stablecoin data table](/img/2026/pharos/pharos-homepage.png)


## What Pharos Is

Pharos is a stablecoin analytics dashboard that tracks **156 stablecoins** across 18 peg currencies, multiple backing types, and governance models. It monitors pegs in real time, computes composite risk scores, rates safety across multiple dimensions, tracks DEX liquidity, detects early warning signals, and publishes a daily AI-generated market digest.

It's entirely [open source](https://github.com/TokenBrice/stablecoin-dashboard). No accounts. No wallet connectivity. No monetization, now or ever. **Pharos is a public good**: free, open, and designed to give everyone the same level of stablecoin intelligence that used to require building your own infrastructure.

If you have read my [previous article on DeFi's curation layer crisis](/defi-ux-disaster/), you already know the thesis: the space desperately needs better information services. Pharos is me putting my money where my mouth is — literally. This is entirely self-funded, solo-built, and will remain freely accessible.


## Thinking About Stablecoins Properly

Before you can monitor stablecoins intelligently, you need a proper taxonomy. Most dashboards treat stablecoins as a flat list: name, ticker, supply, price. That tells you almost nothing about the actual risk profile.

Pharos classifies every stablecoin along three axes:

- **Governance model**: CeFi, CeFi-Dependent, or DeFi: based on the actual dependency on centralized infrastructure, not the marketing narrative. USDC is CeFi (obviously). But DAI/USDS? CeFi-Dependent — it has onchain governance, but its backing is overwhelmingly tied to centralized assets. This distinction matters enormously for risk assessment.
- **Backing type**: RWA-backed, crypto-backed, or algorithmic: what actually stands behind the peg.
- **Peg currency**: Not just USD. Pharos tracks EUR, GBP, CHF, BRL, JPY, gold, silver, CPI-linked tokens, and many other currencies. All non-USD supplies are FX-adjusted so cross-currency totals are meaningful, not naive face-value sums.

This taxonomy is foundational. Every feature in Pharos builds on it, because **you can't assess risk if you don't first understand what you're looking at**.


## Watching the Peg

Peg monitoring sounds simple: check the price, see if it's at $1. In practice, it's a nightmare.

Stablecoin prices are noisy. A single CEX having a thin order book can produce a false "depeg" signal. A large swap on Curve can temporarily push a price off-peg before arbitrage corrects it. CoinGecko and other aggregators sometimes report stale data. If you naively alert on every price deviation, you'll drown in false positives.

Pharos uses a **two-stage depeg detection pipeline**:

1. **Stage 1** runs every 15 minutes. It detects price deviations but cross-validates against DEX prices to suppress false alerts caused by thin liquidity or stale data.
2. **Stage 2** kicks in for large-cap stablecoins (>$1B supply). It requires multi-source confirmation before declaring a depeg event. Crying wolf about USDT costs credibility.

On top of detection, every stablecoin gets a **Composite Peg Score (0–100)** that measures stability over time: how long it's been at peg, how many depeg events it's had, the severity of those events. This turns "is it at $1 right now?" into a much more useful question: "how reliably does it stay at $1?"

![Pharos Depeg Tracker showing the DEWS orbital visualization with stablecoins positioned by risk level, 10 active depegs out of 148 tracked, and the Peg Leaderboard ranking coins by composite peg score](/img/2026/pharos/pharos-peg-tracker.png)


## Systemic Risk: The Stability Index

Individual peg monitoring is useful, but it misses the forest for the trees. The really dangerous moments in crypto aren't when one coin depegs — it's when the contagion spreads.

The **Pharos Stability Index (PSI)** is a composite ecosystem health score (0–100) computed every 15 minutes. It answers a simple question: **how healthy is the stablecoin ecosystem right now?**

PSI factors in:
- **Severity**: The impact of current depegs, weighted by market cap — a $50B stablecoin depegging 2% matters more than a $10M one depegging 20%.
- **Breadth**: How many stablecoins are depegging simultaneously — contagion is what kills.
- **Stress breadth**: How many coins show elevated stress signals (from DEWS, described below), even if they haven't depegged yet.
- **Trend**: 7-day total market cap momentum — capital flowing out is a leading indicator.

The index maps to six condition bands, from **BEDROCK** (all clear) to **MELTDOWN** (systemic crisis). Think of it as the DeFi equivalent of a financial stability report, except it updates every 15 minutes instead of every quarter.

![Pharos Stability Index at 92.8 (BEDROCK), with a historical chart color-coded from green (BEDROCK) to red (MELTDOWN), and a Notable Events timeline of past stablecoin crises including Terra, USDC/SVB, and FTX](/img/2026/pharos/pharos-stability-index.png)

One design decision worth noting: **chronically depegged coins gradually fade from the index.** A stablecoin that's been off-peg for 120+ days shouldn't dominate the severity score forever — it's a known condition, not an active crisis. This "depreciation factor" prevents zombie depegs from masking fresh instability.

If you have been around for a while, have a look at the PSI history chart: you'll see all your past stable-traumas reflected in large PSI dips.


## Early Warning: DEWS

PSI tells you the current state. But what about what's coming? That's what the **Depeg Early Warning Score (DEWS)** is for.

DEWS is a forward-looking stress score (0–100) that estimates depeg probability by combining eight sub-signals:

- **Supply Velocity** — Is there a bank-run pattern? Capital fleeing fast is the clearest danger sign.
- **Pool Balance Drift** — Are DEX pools becoming one-sided? This means concentrated selling pressure.
- **Liquidity Erosion** — Are LPs pulling out? When sophisticated market participants leave, pay attention.
- **Price Confidence** — Are price sources reliable, or is the data degraded?
- **Cross-Source Divergence** — Do different exchanges agree on the price? Fragmented pricing signals trouble.
- **Blacklist Activity** — Is the issuer emergency-freezing addresses? That's never routine.
- **Mint/Burn Flow** — Is there a redemption surge happening?
- **Yield Anomaly** — Are yield patterns signaling something abnormal?

Each signal is weighted (supply velocity and pool drift carry the most weight, because they're the most predictive), and the composite score maps to five threat bands from **CALM** to **DANGER**.

Here's what makes DEWS genuinely useful: it includes a **systemic amplifier**. When PSI is below 75 (meaning the ecosystem is already stressed), DEWS scores get boosted by up to 30%. This captures a real dynamic: individual vulnerabilities become more dangerous when the whole system is under pressure. A stablecoin that would score "WATCH" in calm conditions might score "ALERT" during a market-wide sell-off — and that's correct.


## Safety Ratings

Scores and indices are useful for monitoring, but sometimes you need a straight answer: **is this stablecoin safe?** Pharos provides multi-dimensional safety ratings, grading each coin from A+ to F across five dimensions:

- **Peg Stability**: Historical depeg events, severity, current streak.
- **Liquidity**: DEX availability and depth across chains.
- **Resilience**: Blacklist/freeze capabilities and vulnerability to administrative actions.
- **Decentralization**: Governance model, custody risk.
- **Dependency Risk**: Upstream collateral and wrapper dependencies — if your stablecoin is backed by another stablecoin, you inherit its risk.

The result is a **report card** that gives you the full picture, not just a single letter grade. A coin might score A on peg stability but D on decentralization (hello, USDC). The dimensions are visualized as a radar chart so you can compare risk profiles at a glance.

For the 17 stablecoins covered by [Bluechip](https://bluechip.org/), Pharos also surfaces their independent SMIDGE ratings alongside its own: nothing beats a manual analysis like Bluechip does, Pharos' safety score edge lies in its real-time factoring of onchain data and broad coverage.

![Safety Scores page showing a grade distribution bar and a grid of stablecoin cards, each with a radar chart scoring peg stability, liquidity, resilience, decentralization, and dependency risk](/img/2026/pharos/pharos-safety-scores.png)


## Liquidity, Yields, Freezes, and Flows

Beyond the core risk framework, Pharos tracks four additional dimensions that matter for anyone seriously engaging with stablecoins:

### DEX Liquidity Scoring

A stablecoin's price means nothing if you can't actually trade it. Pharos computes a **composite liquidity score (0–100)** per stablecoin by aggregating pool data from Curve, Uniswap V3, Aerodrome, DexScreener, and more. It factors in TVL, volume, pool composition, cross-chain coverage, and concentration risk (via HHI — the same index regulators use to measure market monopoly). **A stablecoin with $1B in supply but all its liquidity concentrated in a single pool on one chain is fragile**, and the score reflects that.

### Yield Intelligence

Pharos tracks **risk-adjusted yields** for 40+ yield-bearing stablecoins and lending opportunities. The **Pharos Yield Score (PYS)** combines yield magnitude with safety rating, consistency, and sustainability. High yield with a low safety grade gets penalized — because 20% APY means nothing if the protocol depegs or gets frozen. Yield sources are resolved from multiple tiers: on-chain exchange rates, DeFiLlama pools, price-derived NAV appreciation, and T-bill proxies. Each coin also gets a set of warning signals (yield spikes, TVL outflows, data staleness) so you can spot trouble before committing capital.

### Freeze & Blacklist Tracker

USDC, USDT, EURC, PAXG, and XAUT all have freeze/blacklist capabilities. Pharos tracks these events across 8 chains (Ethereum, Arbitrum, Base, Optimism, Polygon, Avalanche, BSC, Tron), syncing every 20 minutes. You can see when addresses get frozen, how much was affected, and whether assets were seized. This is one of the most undermonitored aspects of stablecoins: **the power to freeze is the power to confiscate**, and most users have zero visibility into how often it's exercised. You can now monitor censorship in quasi-real time.

### Mint/Burn Flow Tracker

Supply changes tell a story. Pharos ingests mint and burn events for 81 stablecoins on Ethereum, bucketed into hourly flows. It computes a **Pressure Shift** metric (how current burn activity compares to the 30-day baseline), a **Bank Run Gauge** (market-cap-weighted composite stress), and a **Flight-to-Quality** detector (when capital moves from risky stablecoins to safe havens). If there's a silent bank run happening, Pharos will surface it.


## Tools for Analysis

Data is only useful if you can act on it. Pharos provides three analysis tools that go beyond passive monitoring:

### Comparison Tool

Select up to 5 stablecoins and compare them side-by-side across every dimension: supply, price, peg stability, safety grades, liquidity, DEWS, mint/burn flows. The comparison includes a multi-series chart (supply or price over time) and a radar overlay for safety profiles. You can export the comparison as an image for sharing.

![Comparison tool showing 5 gold-backed stablecoins (PAXG, Tether Gold, Kinesis Gold, Matrixdock Gold, DGLD) side-by-side with key metrics, a market cap history chart, and an overlaid radar chart for safety score comparison](/img/2026/pharos/pharos-compare.png)

### Dependency Map & Contagion Analysis

This might be Pharos's most unique feature. The **dependency map** visualizes collateral relationships between stablecoins as a force-directed graph. Many stablecoins are backed by other stablecoins (or wrapped versions of them), creating chains of dependency that are invisible unless you map them. The **stress test mode** lets you simulate a failure: select any coin and see which others would be affected, and how badly. If USDC fails, which coins go down with it? Now you can see.

![Force-directed dependency map showing collateral relationships between stablecoins on a dark background, with USDT and USDC as the dominant central nodes and dozens of smaller coins connected around them](/img/2026/pharos/pharos-dependency-map.png)

### The Cemetery

80 stablecoins have already died. Pharos documents them all — name, cause of death, peak market cap, obituary with sources. It's a graveyard that serves as both a historical record and a reminder: **stablecoins fail more often than most people think**, and understanding how they failed is essential context for evaluating the ones still standing.


## The Daily Digest

Every morning at 08:00 UTC, Pharos publishes an AI-generated market digest that synthesizes overnight data into a concise narrative. It draws from 12 data sources: market cap changes, active depegs, PSI movements, blacklist activity, supply velocity signals, safety grade transitions, mint-burn flows, DEWS stress distribution, and more.

The digest adapts to the current regime: during calm periods, it highlights subtle shifts; during crises, it leads with the most urgent developments. It's distributed via [Twitter/X](https://x.com/PharosWatch), the [Telegram channel](https://t.me/pharoswatch), and archived on the site. For more granular alerts (DEWS changes, depeg events, safety grade shifts), the [Telegram bot](https://t.me/PharosWatchBot) lets you subscribe to specific coins and tune your own thresholds.

## Open Source, Public Good, Forever Free

I want to be explicit about this because it's essential.

**Pharos has no monetization, no token, no plans for either.** The entire codebase is open source. There are no premium tiers, no gated features, no "contact us for enterprise." Every metric, score, and dataset that Pharos computes is freely available to everyone. There is an API available to all.

This is a deliberate choice. I've spent years arguing that DeFi needs better information infrastructure, that the [curation layer is underfunded and underappreciated](/defi-ux-disaster/). Pharos is my answer to my own criticism. The stablecoin ecosystem is too important and too complex for risk intelligence to be gatekept behind paywalls.

The project is solo-built and self-funded. The tech stack (Next.js frontend, Cloudflare Workers + D1 backend) is designed to keep operating costs minimal while handling the scale of data involved — 20+ cron jobs, 15+ data sources, 68 database migrations worth of schema. It's architected to be sustainable as a public good, not to maximize revenue.


## Start Using Pharos

If you interact with stablecoins in any capacity — trading, lending, providing liquidity, building products — Pharos gives you the information layer you've been missing.

**Explore:** [pharos.watch](https://pharos.watch) — new here? The [onboarding guide](https://pharos.watch/start/) walks you through every feature

**Source:** [GitHub](https://github.com/TokenBrice/stablecoin-dashboard)

**Stay informed:** follow the daily digest on [Twitter/X](https://x.com/PharosWatch) and [Telegram](https://t.me/pharoswatch), or subscribe to personalized alerts via the [Telegram bot](https://t.me/PharosWatchBot)

Pharos will keep expanding its coverage and refining its models. If you want to contribute, the repo is open. If you spot issues or have feedback, there's a feedback form on the site.

Stablecoins won the adoption race. It's time the information infrastructure catches up.

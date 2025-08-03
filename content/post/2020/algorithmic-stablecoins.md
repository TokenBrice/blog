---
title: "The state & future of algorithmic stablecoins"
description: "Looking at ESD, DSD and Basis Cash to establish a mockup of the algorithmic stablecoins and the challenge they tackle."
date: '2020-12-28T01:13:50.191Z'
categories: [DeFi, Understanding]
tags: [DeFi, Ethereum, Stablecoins, Maker, MakerDAO, Basis Cash, Empty Set Dollar, Dynamic Set Dollar, USDT, USDC, sUSD, ESD, DSD, BAC, BAS]
image: img/2020/algorithmic-stablecoins/cover.png
---

Since the beginning of December, a new trend has been shaping up in DeFi: algorithmic stablecoins. Several projects launched and saw significant growth, attracting even more interest for this subset of the space.

Before we dive into what they are and what they entail, let's first discuss the addressable markets. Stablecoins on Ethereum are massive: they are around 20B USDT circulating, 3.5B USDC & 1B DAI. As you can see, right now most of the volume is served by stablecoins requiring some forms of trust, such as **USDC or USDT: the emitting company has the power to freeze assets and manipulate balances.**

Maker explored another approach with DAI that has significantly fewer compromises - however, the scalability is lowered. Besides, it's hard to consider DAI "sufficiently trustless" today when the majority of the collaterals used to mint it are not (USDC, wBTC, TUSD, etc.)

So the recap here would be that so far, there is **an obvious unsatisfied demand** in stablecoin - the ones that scaled did it with significant compromises, which enabled them to satisfy markets despite being services requiring trust, and more or less worthy of it (especially USDT).

The reason I'm writing this piece today is that after following developments on the stablecoin space for years - it seems like we're reaching an exciting breakthrough with a new generation of stablecoins able to offer **both scalability and credible trustlessness**. The topic is neither simple nor easily accessible, especially for newcomers. I'll do my best to walk you through the thought process step by step.

---

### Why do we need uncompromisingly trustless stablecoins?

Before we dive into what project does what to what end, let's take another step back. We've established that there is a significant demand for stablecoins, and none of the current leading offers are sufficiently trustless. But what does it mean exactly?

Simply put, **trustless means that the whole system does not require any central point of trust to operate smoothly**. It's often mentioned with "censorship resistance", a different property that stems from trustlessness. So from a practical perspective, here are some question to help you assess trustlessness: the more permissive the permissions, the less trustless the project tend to be:

1. Can token balances be seized or frozen?
2. Can the protocol's code or parameters be updated? In which conditions? By who?
3. Is the protocol dependant on 3rd-party services, such as price feed (oracle) that could be manipulated?
4. Who/what can print new tokens? Is that user-initiated (someone takes an action) or protocol initiated (a decision the protocol makes based on given parameters)?

The last question is particularly insightful, as it highlights a core component of algorithmic stablecoins: **their "central bank" is a smart contract** — no one controls it, it simply reacts to the system parameters. We'll dive more into this right below.

So with this piece, we'll examine the main models available: Ampleforth, Basis Cash, Empty Set Dollar, and Dynamic Set Dollar. I'll not dive into the history of the space and the specificities of each model, feel free to check this article from Deribit Insights if you need more context:

👉 [Stability, Elasticity, and Reflexivity: A Deep Dive into Algorithmic Stablecoins](https://insights.deribit.com/market-research/stability-elasticity-and-reflexivity-a-deep-dive-into-algorithmic-stablecoins/)

So instead of diving into each system's details, I'll draw **a sketch showing the core principles this generation of stablecoin is built upon**, based on the common parameters and design approaches shared in all projects.

---

### Central Smart Contract

The first interesting dimension is the "central bank" of the system - aka who/what can print new tokens and under what conditions? **USDC & USDT pretty much replicate a central bank** - one entity is in charge of the project and emitting new tokens.

Since Maker is just a smart contract enabling its users to mint DAI from certain collaterals, the approach is different here. Essentially **Maker/DAI enables you to be your own central bank**. So the central bank of Maker is a smart contract, but it requires human input to mint DAI.

The algorithmic stablecoins go even further, as **the human input is removed from the minting process.** In these systems, no one has the capacity to mint tokens - only the smart contract operating it can. It's very elegant and minimal, but it requires a carefully designed set of incentives to make sure the stablecoin will eventually hedge towards its peg. To put it simply, **with algorithmic stablecoins, the central bank is an autonomous smart contract.**

### An Army of Stabilizers

With algorithmic stablecoins, especially in their early days, peg breaks are frequent. To push the stablecoin back to the peg, the protocols have different kinds of incentives.

When the stablecoin is worth over $1, **the protocol mints new tokens and distribute them as an incentive** to users providing liquidity or locking their token, which helps to push the price back down.

When the stablecoin trades below $1, the coupons (or bond) system kicks in: **users can burn their stablecoins for a coupon** representing it + a premium. However, they will only be able to redeem the coupon once the price is back over the dollar.

As you can see, at a high level, these mechanisms are simple. They have intricacies that you need to master if you want to partake in the system. **Users understanding them and following them can help the protocol stabilize**, and if it does they might earn in the process. So these simple rules lead to the emergence of an army of stabilizers, who make use of all the mechanisms to stabilize the price.

This design pushes both game theory and the meme-game to another level:

![DSD Meme](img/2020/algorithmic-stablecoins/dsd-meme.jpeg "A DSD meme")

### Aggressive Expansion Phase

Since the supply of algorithmic stablecoin is elastic, their mechanism is quickly battle-tested. Indeed, at launch, the circulating supply of the stablecoin is usually low and the attractive incentives create a lot of demand.

For instance, **Basis Cash launched with 50 000 BAC tokens** distributed to the first stakers. Roughly a month after, there are now **40M BAC circulating**: they were produced because BAC has been trading >$1 most days since the launch. So far, there was no phase where BAC's TWAP &lt; $1, so the Basis' coupon system (BAB) has not been tested yet.

{{< notice info >}}
Expansion/Contraction are phased in "epochs". Basis Cash has 24h epoch. ESD is 8h and DSD is 2h.
{{< /notice >}}

On the other hand, ESD and DSD already saw several cycles of expansion and contraction each, with the protocol operating as intended:

![DSD Market Cap over the last 7 days](img/2020/algorithmic-stablecoins/dsd-mktcap.png "DSD Market Cap clearly shows the expansion/contraction phases")

### Harnessing DeFi composability

Another key principle of algorithmic stablecoins is composability. We often think of it as "how can I plug my finished product/service into others?". These projects go much further, as **they use other protocols like Uniswap as a central part of their system.** Basis, ESD and DSD all have three main components:

1. An internal locking/staking mechanism for expansion phases (DAO or Boardroom)
2. A burn&redeem mechanism for contraction phases
3. A Uniswap pair (/USDC or /DAI)

Their very structure demonstrates an understanding of DeFi and its composability. By placing the Uniswap-pair(s) at the core of the protocol, it helps on so many levels - since **Uniswap is staple DeFi users are familiar with.**

While Uniswap is the main pool, the liquidity on other DEXes is increasingly looked at. With the launch of Omakase, Sushi added two new incentivized algorithmic stablecoin pools: ESD/ETH & DSD/USDC.

Composability is key for algorithmic stablecoins and several projects are already taking steps to get more integrated within the ecosystem. Within the next few months, we should see the next steps of this with the arrival of some algorithmic stablecoin as collateral on lending platforms. 

### Oracle Minimalism

Oracle are used as a base parameter in the algorithmic stablecoin system:: they are the **source of truth for the price of the stablecoin**. Making sure the oracle is resilient and cannot be gamed is critical.

To do so, the previous generation of projects, especially Maker, tended to overengineer things. In the early days, Maker's input parameter was almost the pure & raw price of ETH. However, to make the system less prone to "flash liquidations", Maker built their own oracle, and use several delays and averages with the liquidation price to **add some inertia to their system**.

On the other hand, as we've seen before our algorithmic stablecoins tend to be minimalist and harness the composability of DeFi. **With their Uniswap pairs, they already have a decent price feed with significant liquidity, making it hard to manipulate**. So the Uniswap price is used as the based, but generally computed as a TWAP (Time Weighted Average Price) to avoid price manipulations right before rebases.

While being minimalist, the systems are efficient and elegant: as these stablecoins projects grow, so should their liquidity on Uniswap, making the oracle more resilient and the price harder to manipulate.

I for one am excited as to where this subset of the space is heading. Whether you intend to partake or not in the bootstrapping phase of such stablecoins, I think it's highly valuable to document yourself on them as they are a good tell of the main trends of the space.

---

### 🧰 Algorithmic Stablecoin Toolbox

Before we part way, allow me to share some useful tools to track the evolution of these stablecoins. First, each project has its own tracker providing the main metrics for the current epoch:

- **[Basis Cash Tools](https://bc.tools/)**
- **[ESD Tools](https://esd.tools/)**
- **[DSD Tools](https://dsd.tools/)**

Finally, you can view more granual details about the ESD and DSD system on this dashboard: **[ESD/DSD Bonding](https://duneanalytics.com/tongnk/esd_1)**

### Disclaimer

{{< notice warning >}}
**THIS ARTICLE DOES NOT CONSTITUTE INVESTMENT ADVICE.**

I'm not a qualified financial advisor, but who gives a fuck really? This is DeFi we're talking about.
{{< /notice >}}

I've felt legitimate to write this piece because I've been following closely Basis Cash, Empty Set Dollar, and Dynamic Set Dollar closely, as well as Basis Dollar & Share less attentively. Frax is another hybrid project that is worth looking at - I did not discus it as I'm not familiar enough with it yet. 

{{< notice note >}}
**💰 Bag Disclosure**: I own BAC/BAS (Basis Cash), ESD (Empty Set Dollar) and DSD (Dynamic Set Dollar).
{{< /notice >}}

I hope this read was insightful for you. If that's the case, you can **[follow me on Twitter](https://twitter.com/tokenbrice/)** or this blog through RSS (at the very bottom of the page 👇) to get notified when the next article is published.

---
title: "⚖ The tale of two seigniorage models: Basis vs ESD"
description: "A comparative analysis of the two main seigniorage token models currently explored to produce new types of stablecoins on the Ethereum network."
date: '2021-01-16T01:13:50.191Z'
categories: [🌌 DeFi, 💸 Practical DeFi]
tags: [DeFi, Ethereum, Stablecoins, Seigniorage, Basis Cash, Empty Set Dollar, Dynamic Set Dollar, USDT, USDC, ESD, DSD, BAC, BAS, MithCash, MIC, MIS, DAIQ, ZAI]
toc: true
tocNum: false
---

A few weeks ago, I shared my first post on algorithmic stablecoins highlighting the key characteristics that made such projects interesting in my eyes. In this piece, we'll go deeper into the topics, with a **comparative analysis of the two main models**: the Basis model and the ESD model. 

Both are successfully used by the projects bearing their names but also a sizable trail of forks, more or less relevant. As the field of algorithmic stablecoin grows, there seems to be a **consensus around these two models, now used as a template** to quickstart newer projects trying various alterations, such as pegging the system to another currency other than the dollar, like gold or the euro.

![seigniorage-esd-basis-tokenbrice](/img/2021/seigniorage-basis-vs-esd/cover.png)

The plethora of existing forks enables the latest ones to pick and build upon the existing or pending improvements of the live systems, further leapfrogging the innovation. But before you dive into the arcane of the latest gold elastic token, it's worth making sure you understand the underlying models behind these projects. That's why we are here today.

---

## 1. Ample Bases for Elastic Currencies

To put it simply, both models are building on the previous Ampleforth model which pioneered "elastic currencies" that have a supply reacting to the markets' conditions. The main issue with Ampleforth is that everyone is exposed to the rebases, hindering the usability of the AMPL as a medium of exchange.

So the two new iterations address that with a different take:

*   With the seigniorage model, **the rebase mechanism is split into a different token**, the share - paving the way for a more usable stablecoin.
*   In the ESD model, there is still one token only but the DAO and LP lockup achieve a similar result.

Both models also introduce the mechanism of bond/coupons to **add a positive incentive when the price is below peg**, helping to further stabilize the stablecoin.

So today, after we brush up on the basics, we will compare the Basis model (forked by MithCash, OneCoin, and more) to the ESD model (used in DSD, ZAI, DAIQ, etc.).

I will not explain the models in-depth but this table recaps the main differences:


|                   /                    | BASIS MODEL (Seigniorage)                                    | ESD MODEL                                                    |
| :------------------------------------: | ------------------------------------------------------------ | ------------------------------------------------------------ |
|               **TOKENS**               | BAC = stablecoin <br> BAS = a share of the protocol <br>BAB = 1 BAC claim while in expansionary phases | ESD = stablecoin <br> ESDS = 1 ESD claim while in expansionary phases |
|        **STABLECOIN LIQUIDITY**        | BAC/DAI Uniswap pair: continuous BAS incentives (1y) <br>No lockup | ESD/USDC ESD incentives if >1 <br>  5 epoch lockup              |
| **"BRING BACK TO PEG" (<1) MECHANISM** | Bonds (BAB): BAB = BAC(twap)^2 <br>  No expiration date         | Coupons (ESDS) Premium-based pricing expire after 90 epochs (30 days) |
| **WHEN EXPANSION (>1), WHO GETS IT?**  | Boardroom BAS stakers (once treasury has its fill)            | Dynamic split between LP and DAO depending on the protocol debt |
|     **OTHER IMPORTANT MECHANISMS**     | BAS/DAI Uni pair with BAS incentives <br>BAS/DAI & BAC/DAI pools farmable through vaults - Harvest, Pickle, etc. | DAO auto compounds but has a long lockup<br>Lockups -> limited third party integrations |

---

## 2. ⛽ Gas Efficiency Overview

Before I dive into the details of each item, here's another key part of the systems to consider if you want to partake in them: how gas efficient are they, for the user?

You'll find here some pointers on the amount of transaction and transaction flows required to partake in different parts of the system we described, helping you assess if it would make sense for you, gas-wise.

Overall, the **liquidity providing positions are the most transaction-intensive**, especially in the ESD model where you need to bound and unbound your LP tokens & claim rewards.

#### 2.1. LP - Basis ⭐⭐⭐

*   Entry: Stake LP token
*   Reward: Claim (stream)
*   Exit: Unstake LP token

#### 2.2. LP - ESD ⭐

*   Entry: Stage -> Bound
*   Reward Claim: Unstage-> Stage-> (wait 5 epochs) -> Claim
*   Exit: Unstage -> (wait 5 epochs) -> Unbound

On the share/DAO side, **the flow is less transaction-heavy**, so it's better for smaller holders:

#### 2.3. Basis - Boardroom ⭐⭐⭐

*   Entry: Stake BAS
*   Reward: Claim (after the end of an epoch when BAC>1.05)
*   Exit: Unstake BAS

Note: During expansion phases, you can let BAC accumulate in the boardroom and claim several days of reward at once.

#### 2.4. ESD - DAO ⭐⭐⭐⭐

*   Entry: Stage ESD -> Bound ESD
*   Reward: no transaction required
*   Exit: Unstage ESD -> (wait 15 epochs) -> Unbound ESD

Note: During expansion phases, the rewards produced by the DAO are automatically compounded (=bounded) without action required from the user-end.

---

## 3. Comparative algorithmic stablecoin analysis: Seigniorage vs ESD

You'll find the bulk of my analysis in the following table. If you are familiar with both projects, that should be enough, else you can read the explanations for each benefit and downside right after the table.


|                 |                           Basis Model                           |                          ESD Model                            |
| :-------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| **👍Benefits** | More liquid stablecoin pair <br>  Fluid share <br>Better coupon system<br>Farmable (3rd party integrations) | More committed holders <br>Faster cycles: can adjust more dynamically to the markets  |
|  **👎Downsides**  | Share has limited utility when BAC<1 <br>  Share price heavily correlated to stablecoin price | Less accessible system <br>  Riskier coupon system (expiration) <br>  Newly minted ESD batches |

---

{{< notice warning >}}
**Necessary Disclaimer: This is not financial advice**. I’m not qualified to provide any. It’s a mere technical analysis of two seigniorage systems implemented live in production: a farmer’s report 🚜
{{< /notice >}}

Now that we are up to date on each model and their gas efficiency, let's details their benefits and downsides:

---

### 3.1. 👍 Benefits of the Basis model

#### 3.1.1. More liquid pools

In the Basis model, the **BAC/DAI liquidity pool is continuously rewarded with BAS token**. Since the BAS reward continues even when BAC is in a contraction phase, we're not observing the same compounded reduction of liquidity seen in contraction on the ESD model: when the ESD price is on a downtrend & liquidity providers are pulling out at the same time.

![liquidity-esd-bac-tokenbrice](/img/2021/seigniorage-basis-vs-esd/liquidity-esd-bac.png "The total liquidity available on the ESD/USDC and BAC/DAI pairs since inception.")

We can see that **ESD's liquidity tends to be more spikey** while BAC's is correlated mostly to BAC price (expected).

#### 3.1.2. Fluid share

The share is fluid in the sense that there is currently no commitment required to be eligible for the Boardroom BAC. While this can also make the BAS price harder to stabilize, it makes the expansion-reward component of the system more broadly accessible and less game-able.

#### 3.1.3. Better Coupons

**Basis Coupons (BAB - Bounds) have no expiration date**. They can be redeemed for 1 BAC as long as BAC is > 1.05. It makes buying coupons less of a gamble than on ESD where they expire.

#### 3.1.4. Third Party Integradable

Rewards in the Basis model are distributed through **standard staking contract**, enabling and facilitating the integration by third parties. There are already Harvest & Pickle vaults to streamline the farming of the BAC/DAI, BAS/DAI, MIC/USDT & MIS/USDT pools.

![harvest-basis-cash-mith-cash](/img/2021/seigniorage-basis-vs-esd/harvest.png "BasisCash & MithCash related vaults on Harvest Finance.")

### 3.2. 👎 Downsides of the Basis model

#### 3.2.1. The share has low utility when BAC&lt;1

The main and by far biggest weakness so far of the current implementation of the Basis model is the **overall weak utility of the share token**. In expansion phases, its price is usually appreciating because of the newly minted BAC it gives access to. However, there is very little utility for BAS in contraction phases, except for its governance power. In contraction, the only potential earning option is to commit to the BAS/DAI pool for additional BAS, but it's very risky play with a bearing BAS price action (contraction).

Several projects are already working on solutions to address this.

#### 3.2.2. Share price 100% correlated to stable price

The second downside is a direct consequence of the first. Because of the lack of utility of BAS outside of BAC in expansion, **its price is directly correlated to the BAC price**. Additional utility on BAS could enable both tokens to have more independent cycles, bringing more stability overall to the model.

---

### 3.3. 👍 Benefits of the ESD model

#### 3.3.1. More committed holders

In the ESD model, there is **no access to the newly minted ESD without committing for several epochs**, at least 5 with the LP. It makes large holders more likely to be actively involved in the minting and stabilizing process.

#### 3.3.2. Adjust more dynamically to markets' conditions

Overall, the ESD system operates on a **timeframe three times shorter than Basis**, allowing for more fluid and dynamic adjustments. DSD goes even further with 2 hours epoch (= 12x Basis pace).

### 3.4. 👎 Downsides of the ESD model

#### 3.4.1. Overall complexity of the system

Because of the additional lockups, staging, and bounding required to implement the share functionality directly at the stablecoin level, ESD-based systems tend to be more **complex to apprehend**, especially for newcomers. You can even see it in the memes, where ESD/DSD players love to meme themselves as high-IQ masterminds. The coupon expiration makes the stabilization system extremely unfriendly for newcomers, which is not necessarily a bad thing per se, but see the next point.

#### 3.4.2. Weaker coupon incentive	

ESD coupons have an expiration date, turning the coupon system into a bit of Russian roulette. Because of this design, there are serious risks of losing all the capital committed while burning ESD for coupons, even if the ESD system sustains itself in the long run. Indeed, once ESD is burnt into coupon, the owner has **90 epochs (~30 days) to redeem them before they expire.**

#### 3.4.3. Newly minted ESD batches

Finally, the emission logic of ESD-based systems, coupled with the lockups period tend to produce **“raindrop epochs”** where most of the newly minted ESD is unlocked, which can trigger violent price action on the stablecoin price.

During the last expansion phase, the period around epoch 396 was famous and scared because most of the newly minted DSD was made transferrable over a very short window:

![DSD-epoch-396-397-tokenbrice](/img/2021/seigniorage-basis-vs-esd/dsd-raindrop.png "After the last expansion phase, over 30M DSD were released in just two epochs (396 and 397), a dreaded moment for DSD and coupon holders.")

*Yes this is DSD, but similar patterns are observed on ESD. It's due to the DAO lockups and emission schedule.*

## 4. The Algostable Toolbox

Before I let you go, here's a quick overview of the main tools useful to monitor and manage positions for all four projects. We're lucky! There are some amazing community-build tools made to help you track algorithmic stablecoins. 

{{< notice tip >}}
**[Vfat in particular](https://vfat.tools/)** has been super reactive updating his tracking and management tools for the newer projects. It even includes a **[seigniorage tokens overview](https://vfat.tools/seigniorage/)** now:

![vfat-seigniorage-overview](/img/2021/seigniorage-basis-vs-esd/vfat.png "Overview of the main seigniorage tokens on Vfat")
{{< /notice >}}

*   For ESD, your main dashboard is [ESDTools](https://esd.tools/)
*   For DSD, [DSDTools](https://dsd.tools/).
*   For Basis Cash, **[BCTools](https://bc.tools/)**. 

You can use [this dashboard to track the release of newly minted ESD and DSD](https://duneanalytics.com/tongnk/esd_1).

Finally, all four projects are supported in both [Zapper](https://zapper.fi/) and [DeBank](https://debank.com/) to track your investments. You can also use [Pickle](https://pickle.finance/) or [Harvest](https://harvest.finance/) to manage your position in the BAC/DAI, BAS/DAI, MIC/USDT, and MIS/USDT pools.

### 4.1. Additional Resources

- To learn more about the context behind algorithmic stablecoins, feel free to **[read my previous article on the topic]({{< relref path="/content/posts/2020/algorithmic-stablecoins.md" >}})**. 
- To learn more, French-speaker will enjoy this **[🇫🇷 50 min video explainer of both models](https://www.youtube.com/watch?v=TuenkIZZEq0)** 
- English speakers can explore further with this extensive research/recap piece published on Derebit: **[Stability, Elasticity, and Reflexivity: A Deep Dive into Algorithmic Stablecoins](https://insights.deribit.com/market-research/stability-elasticity-and-reflexivity-a-deep-dive-into-algorithmic-stablecoins/)**.
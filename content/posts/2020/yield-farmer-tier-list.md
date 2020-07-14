---
title: "💦 The Yield Farmer Tier List"
description: "A structured list of **incentivised liquidity pools on Balancer Labs, Curve Finance and Uniswap**, ranked by their yield earning potential: let's stack!"
date: '2020-07-07T01:13:50.191Z'
categories: [🌌 DeFi, 💸 Practical DeFi]
tags: [DeFi, Ethereum, Lending, Liquidity Providing, Balancer, Curve, Liquidity Incentives, Liquidity Mining, Ampleforth, mUSD]
toc: true
tocNum: true
---

![cover-Yield-Farmer-Tier-List](/img/2020/yield-farmer-tier-list/cover.png)

DeFi is like a layered yield cake. When you first walk through the door, making a deposit on Aave and seeing your balance grow puts you in awe. Shortly thereafter, through your own research or discussions with the community, you realize there is more to it **- there could be icing on the cake too!**

There are many ways you could find several streams of yields on a given capital utilizing Ethereum's decentralized finance. **Today, we'll exclude out of the box any strategy involving leverage** - the easiest way to achieve such a feat. There are still a lot of high-quality crops to plant, even without leverage! 

Indeed, capital efficiency is increasing at a rapid pace in DeFi thanks to novel financial primitives like Compound, Balancer or Curve. It's now possible to **achieve up to 3 layers of returns**, and there are pools for any risk appetite, from pure stablecoins ones to 100% ERC-20 tokens exposure.

**The Liquidity Wars are merely beginning.** Follow the governance of the protocol you're invested in closely, it's even more critical now. Meanwhile, since DeFi feels more and more like gaming, allow me to import a concept inherited from there: tier list. 

In video games, tier lists are useful to navigate the different types of characters or builds. They establish both a typology and a ranking. Today, we'll bring this concept back to DeFi to arrange the most attractive liquidity pools into coherent groups.

## BEFORE WE START

ℹ Please note - This content assumes a basic understanding of the world of Ethereum's decentralized finance. Refer to my earlier articles if that's the first time you've heard of it:

1. This piece will not cover basic DeFi investment strategies, detailed in the **[📖 DeFinancial Services Guide]({{< relref path="/content/posts/2020/definancial-services-guide.md" >}})**. 
2. For more information regarding the tools you can use to implement and manage these strategies, please check **[🧰 The DeFinancial Farming Toolbox]({{< relref path="/content/posts/2020/defi-farmer-toolbox.md" >}})**.

**_This is not investment advice and reading this document as anything more than a structured list of incentivised liquidity pools would be a misrepresentation._**

### Suggest yours!

This post can be a living document. Feel free to suggest incentivised pools I've missed. If you are familiar with Github, **[you can do a pull request](https://github.com/TokenBrice/blog/blob/master/content/posts/2020/yield-farmer-tier-list.md)**. If not, just reach out and share documentation about the pool and its incentive program.

Finally, allow me to make the distinction between:

1. **Liquidity Mining**: a base action of the platform (such as supply liquidity) is rewarded with the platform native token (ex: BAL on Balancer)
2. **Liquidity Incentive Programs**: a specific liquidity pool is eligible for extra rewards, through staking of the pool token or weekly distributions (ex: Wednesday for JRT Balancer pools).

The good news is: you can stack both! Let's see how.

---

![TokenBrice-Yield-Farmer-Tier-List-DeFi](/img/2020/yield-farmer-tier-list/yield-farmer-tier-list.png)

---

## Tier 1: DeFi Yield Trifecta

As I walk you through the main earning-staking opportunities I've found, I will also share broader considerations about providing liquidity on AMMs, such as thoughts on the pool weighting to help you make informed decisions.

So before we chase our wildest dream, the highly-thought-after yield trifecta, let's take a minute to consider what it looks like. When it comes to yields, the cream of the crop is usually an incentivised & balanced Balancer pool with low fees, meaning it's eligible for the maximum amount of BAL liquidity mining rewards, on top of the liquidity incentive program (& the commissions on swaps).

**There is exactly one Balancer pool matching these criteria with 2 stablecoins** to my knowledge, so this is where we start:

### The 50% mUSD / 50% USDC Balancer Pool

mstable[^1] is a meta-stablecoin. You can go on their app to lock your USDT, USDC, DAI & TUSD to mint mUSD. Once you own mUSD, several earning opportunities are available.

The most direct one is the "Save" feature on the mStable app. It will lock your mStable tokens and generate a return through lending.

![mstable](/img/2020/yield-farmer-tier-list/mstable.png)

Now that's a simple yield and won't deserve a feature here by itself. 

However, it's the perfect introduction to the Balancer mUSD/USDC pool, our first trifecta of the day. What's a trifecta you ask? Pretty simple: 3 layers of yields:

1. **Commissions on swaps**: It's a liquidity pool facilitating trades and earning a fee.
2. **BAL liquidity mining**- this is a balanced 50/50 pool with low fee (5 bps) earning the maximum amount of BAL possible (mining factor = 1).
3. **[MTA liquidity incentives](https://medium.com/mstable/introducing-meta-mta-mstables-protocol-token-6e1032291ccf)** program on this pool.

|  EXPOSURE | REWARDS IN | AVAILABLE SINCE | L1 APY | L2 APY | L3 APY / INCENTIVE BUDGET |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  50% USDC<br/>50 %mUSD | Native<br/>BAL<br/>MTA | June 26 2020 | Variable | ?? BAL | 50 000 MTA/week |

_*Native rewards = earned in the same token as the exposure (usually a commission fee taken on trades facilitated)_

Please note: The respective ratios of four stablecoins backing the mUSD (half of the exposure) can vary, go to the m stable app[^2] to view it:

![mstable-asset-distribution](/img/2020/yield-farmer-tier-list/musd.png)

This pool is particularly attractive because the exposure is 100% stablecoin-based, despite a very solid yield thanks to the max BAL mining ratio + the incentive program paid in the highly anticipated MTA token.

_Note/Warning: 💬 Discussions are ongoing in the [Balancer Discord](https://discord.com/invite/ARJWaeF) governance channel to lower the BAL mining ratio on this pool. It was lowered to 0.1 for tokens tracking the same asset._

### 90/10 Incentivised Balancer Pools


#### 90% SNX / 10% USDC Balancer Pool

Feel like you missed out on SNX rise? For medium capitals (&lt; 5000 SNX) it makes little sense to stake if you account for the gas costs. This pool is a great alternative for a bullish SNX exposure with great yield potential.

|  EXPOSURE | REWARDS IN | AVAILABLE SINCE | L1 APY | L2 APY | L3 APY / INCENTIVE BUDGET |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  90% SNX<br/>10% USDC | Native<br/>BAL<br/>SNX | 5 Jun 2020 | Variable | 23 % for a $10 BAL | DONE |

Here, since the pool is heavily skewed towards SNX, the BAL mining is not maximized. Remember the factor of 1 for the BAL mining on the mUSD pool? Here it's 0.36: you get about a third of the amount of BAL you would mine in a 50/50 & low-fee pool. 

However, 90/10 pools are great to heavily minimize impermanent losses risk if you believe the token has a lot of upside potential.

The [incentive program on this pool is now over](https://blog.synthetix.io/balancer-snx-usdc-liquidity-trial/), so it's back to being a regular twofecta pool.

#### JRT Balancer Pools

Jarvis Network offers an incentive program over three pools, all 90 % JRT + 10% DAI, ETH or USDC. The reward model is similar to the previous pool:

|  EXPOSURE | REWARDS IN | AVAILABLE SINCE | L1 APY | L2 APY | L3 APY / INCENTIVE BUDGET |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  90% JRT<br/>10% ETH, DAI or USDC | Native<br/>BAL<br/>JRT | Jun 17 2020 | Variable | 23 % for a $10 BAL | 70 000 JRT/week |

[📖 Incentive Program Introduction](https://medium.com/jarvis-network/liquidity-program-with-balancer-db23aa0ce10)

_Please note: JRT price's action has been quite explosive lately. DYOR._

⚡ Update (_July 08_): JRT rewards are now distributed to ANY Balancer pool (whitelisted):

{{< tweet 1280887456339046400 >}}

### AMPL Geyser

AMPL is a beast of its own, so I invite you to read more on it [^3] before you dive into this one. Here, the exposure is 50 % ETH and 50 % AMPL. On top of your commissions, you're eligible for extra AMPL & as well as the AMPL rebalances (on your AMPL = 50% of the exposure).

|  EXPOSURE | REWARDS IN | AVAILABLE SINCE | L1 APY | L2 APY | L3 APY / INCENTIVE BUDGET |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  50 % ETH<br/>50 % AMPL | Native<br/>AMPL | April 21st 2020 | Variable | Variable - AMPL Rebalances | 36 911 AMPL/month |

[📖 AMPL Geyser Incentive Program Introduction](https://www.ampltalk.org/app/forum/ampl-geyser-19/topic/about-the-geyser-21/)

Rebalances compounded impact can be hard to calculate. This spreadsheet recently emerged to [🧮 help AMPL investors calculate the impact of the rebalances.](https://www.publish0x.com/canuhodl/ampleforth-dollar-ampl-calculator-spreadsheet-for-investors-xmdjxvy) 

![ampleforth-geyser](/img/2020/yield-farmer-tier-list/ampl-geyser.png)

The Geyser code is audited[^4] and insured on Nexus Mutual[^5]. The reward calculation here takes into account the time staked - so this pool is best utilised over the long-term.

---

## Tier 2: How many fecta can there be?

### Synthetix Incentivised Pools

Synthetix has been pioneering liquidity incentive programs with the early Uniswap sETH/ETH pool (+SNX incentives). Synthetic pools are still highly attractive, we'll consider the two main ones of interest for yield stakers.

Please note the Curve's token (CRV), one of the liquidity mining rewards of both pools presented below, is not live yet. [CRV currently documented mechanisms](https://github.com/curvefi/curve-dao-contracts/blob/master/doc/readme.pdf) can change before the launch.

### The OG: Curve sUSD Pool

Just like the mUSD/USDC pool, this pool exposure is 100% in stablecoins, yet the rewards are paid in SNX. 

|  EXPOSURE | REWARDS IN | AVAILABLE SINCE | L1 APY | L2 APY | L3 APY / INCENTIVE BUDGET |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  31.58 % USDT<br/>30.67% USDC<br/>24.62% suSD<br/>13.13% DAI | Native<br/>SNX | Aprill 22 2020 | ~5 % | CRV (not live yet) | 48 000 SNX / week |

[📖Incentive Program Introduction](https://blog.synthetix.io/new-curve-pool-launch/)

This pool is one of the earliest liquidity mining programs there is yet still quite competitive. If you've read my previous guides, you know about this already[^6]. 

### The BTC-OG Variant: Curve renBTC/sBTC/wBTC

![curve-synthetix-balancer-ren-btc-pool](/img/2020/yield-farmer-tier-list/curve-btc.png)

This is similar to the first one, with different tokens. Here, your price exposure is 100% in BTC, while your liquidity mining rewards are made of four hot DeFi tokens: BAL, SNX, REN & CRV. 

|  EXPOSURE | REWARDS IN | AVAILABLE SINCE | L1 APY | L2 APY | L3 APY / INCENTIVE BUDGET |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  44.54% renBTC<br/>32.21% wBTC<br/>23.26% sBTC | Native<br/>SNX, REN, BAL & CRV | June 19 2020 | ~5 % | BAL<br/>CRV | 10 000 SNX/week<br/>25 000 REN/week |

[📖Incentive Program Introduction](https://blog.synthetix.io/btc-yield-farming-pool/)

Because these two Curve pools have full exposure in a stable (USD) or relatively stable assets (BTC), they are a great resource to "park" profits realised on more risky ERC-20 based pools. You still **maintain a decent APR on the base asset (~3-5%) while having a nice upside potential on the liquidity mining rewards**.

---

## Tier 3: Twofecta are nice too!

### Your Favorite ERC-20 Balancer Pool

The Balancer exchange comes with built-in BAL mining incentives. They apply to any pool involving whitelisted tokens. Therefore, any Balancer pool is already a twofecta: you're eligible for commissions on the swaps facilitated + the BAL mining rewards. Please keep in mind that the pool weighting (ideally balanced) and fees (ideally low) affect the BAL mining ratio. The table below assume a ratio of 1, observed for instance on 50/50 pairs with 5 bps fees (0.05%).

Let's look at the return profile generic Balancer pools:

|  EXPOSURE | REWARDS IN | AVAILABLE SINCE | L1 APY | L2 APY | L3 APY / INCENTIVE BUDGET |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  50% wETH<br/>50% ERC20 | Native<br/>BAL | June | Variable | ~60% for a $10 BAL | - |

Beyond Balancer, Liquidity incentives programs are getting into fashion, expect more to be revealed, as well as liquidity mining programs. You can **use a service like [Pool FYI](https://pools.fyi/) which now has an "Incentivised" tag to check for the best opportunities**. For Balancer, use [this website](http://www.predictions.exchange/balancer/%5B%5D) to explore the pools and check their BAL mining factor.

### Compound Deposit

Since the launch of COMP, a Compound deposit could also be considered a twofecta. Indeed, on top of the base APR the deposit is earning, users are also now eligible for COMP rewards. You can [calculate them here](http://www.predictions.exchange/compound/None).

|  EXPOSURE | REWARDS IN | AVAILABLE SINCE | L1 APY | L2 APY | L3 APY / INCENTIVE BUDGET |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  Depends | Native<br/>COMP | June | Variable | Variable in COMP | - |

## ⚠ RISK BREAKDOWN - READ THIS

Each pool comes with its own sets of risk, here's an overview to help you account for them. When you invest in a liquidity pool, you're assuming the following risk:

1. /ALWAYS/ The base Ethereum network risk (51% attack, etc.)
2. /ALWAYS/ You're also assuming the risk carried by the token contracts of any token involved in the pool.
3. /ALWAYS/ As well as the risk involved to the exchange's contracts, which can be hacked or faulty to begin with.
4. /ALWAYS/ An economic risk, the impermanent losses (loss vs raw holding) - that will be heavily affected by your token choices & the pool weighting.
5. /WHILE ENTERING & EXITING/ The risks associated with any service you use, such as [Zapper.fi](https://zapper.fi), for the time of the transaction.

I will walk you through the risk profile of one of the pools to help you model it: the mUSD/USDC pool. Just like the returns, the risk profile is a cake with many layers:

1. I won't develop on the Ethereum network risk
2. Here, we have two tokens in the pool: mUSD & USDC. To compute the risk, we need to look at what's backing mUSD - unwrapping, we're exposed to: USDC, USDT, TUSD. Each of these tokens carry their own risks, since for instance [Circle can freeze USDC balances of any account](https://support.usdc.circle.com/hc/en-us/articles/360001314526-Circle-USDC-Risk-Factors).
3. Here, we're using Balancer. Their contracts were audited by Trail of Bits recently[^4]. Still, the protocol is quite recent. We're also relying on mStable contracts for the mUSD.
4. We're lucky on the impermanent losses - considering the pool involves two stablecoins, the risk is minimized.
5. It all depends on the tools you're using here. Bear in mind that you're also assuming a risk associated with mUSD/Mstable.


Happy farming!

---

*Thanks to [Grégoire](https://twitter.com/gregoireljda) for his help proofreading this article.*
*Thanks to [Jon](https://twitter.com/otherbright) for his careful review of the FR translation.*

[^1]:[mStable](https://mstable.org) is a "meta stablecoin" aggregating several stablecoins together (USDC, USDT, TUSD & DAI) under the mUSD token, while the underlying supply is mobilised similarly to Curve (lending and liquidity providing).
[^2]: You can view the current mUSD underlying distribution on the [mStable app](https://app.mstable.org/).
[^3]: [Ampleforth (AMPL)](http://ampleforth.org/) is "adaptive money built on sound economics". It intends to provide a new type of asset which price movement is uncorrelated from any other.
[^4]: [Certik - Audit Report 28 Feb 2020](https://github.com/ampleforth/ampleforth-audits/blob/master/token-geyser/v1.0.0/CertiK_Verification_Report.pdf)
[^5]: There are currently 51 643 NXM staked on the AMPL Geyser Contract [`0xd36132e0c1141b26e62733e018f12eb38a7b7678`](https://etherscan.io/address/0xd36132e0c1141b26e62733e018f12eb38a7b7678). ![cover-Yield-Farmer-Tier-List](/img/2020/yield-farmer-tier-list/ampl-geyser-insurance.png)
[^6]: The Curve sUSD pool was already mentioned as part of a DeFi investment strategy built on an SNX stake in the [DeFinancial Service Guide](https://tokenbrice.xyz/posts/2020/definancial-services-guide/#5-a-the-synthetixcurve-yieldstack-aka-the-4-steaks-yieldburger)
---
title: "Subtles nuances with great consequences: a cross analysis of Curve and Velodrome"
description: "The Velodrome model, inspired by veCRV, achieves superior alignment between the three key participants of a DEX - LPs, tokenholders, and projects needing liquidity. Yet, most of the DeFi space still fails understand why: but not you anon - once you read this post."
date: '2024-03-21T01:13:50.191Z'
categories: [DeFi]
tags: [DeFi, Ethereum, Decentralized Finance, Curve Finance, veCRV, Velodrome, veVELO, Aerodrome, veAERO]
url: crv-vs-velo
image: img/2024/crv-vs-velo/cover.png
difficulty: "expert"
---

Today, I want to address Velodrome/Aerodrome, a genuine success story in DeFi. I’ve covered DEXes extensively on this blog, especially Curve: this article will compare the two models and explain how Velodrome improved on the veCRV template.

First, let me start with a disclaimer: there are two core components to a DEX that everyone needs to be aware of to understand what follows:



1. The liquidity structures it provides (x\*y=k, stableswap, CL, stableswap-NG, curve V2, etc.)
2. The incentives model, which for a DEX is synonymous with its tokenomics.

This post focuses on the latter, the core of [Velodrome](https://www.defiscan.info/protocols/velodrome-v2/optimism)'s innovation. This post assumes basic familiarity with Curve’s veCRV tokenomics; if not, I urge you to [read my previous writing about it](https://tokenbrice.xyz/fr/crv-wars), posted three years ago but still helpful to understand the model.


## A/ veCRV/veVELO Fees Collection & Distribution

Fee collection and redistribution are the lifelines of a decentralized exchange. Here, simplicity is usually good, as the DEX segment leader Uniswap is still operating under an extremely simple yet brutally efficient model, where 100% of the collected money goes to the liquidity providers.

With the launch of its CRV token in August 2020, Curve explored an alternative path, where 50% of the fees collected on a given pair go to liquidity providers and the remaining 50% to the “DAO” (admin fees), meaning the veCRV holders. Curve introduced the concept of “liquidity gauges,” where locked token holders (veCRV) can direct emissions to be received by liquidity providers, creating an incentive baseline independent of the volume processed.

Velodrome launched two years later, at the end of May 2022, and explored yet another split, inspired by a previous project iterating on the Curve model: Solidly. Here, **LPs get no exposure to the fees collected on the pairs they provide liquidity for and are fully incentivized by token emissions**.

The core difference between veCRV and veVELO lies in how they handle the fees collected at the DEX/DAO level, where we observe differences in the amount of fees collected and their distribution model.

Let’s dive into the nuances of this topic: they are key to understanding the pros and cons of each mode.


### A.1/ Amount of fees distributed: VELO = 2 x Curve

Curve and Velodrome operate under the same base logic: every week, a given amount of CRV/VELO tokens are emitted and distributed to liquidity providers. Each pool has an associated gauge for which veCRV/veVELO holders can vote, and the weekly budget allocation follows the proportion of the “gauge vote”: if a gauge receives 1% of the total veCRV/veVELO vote, 1% of all the emissions produced that week will be directed to it.

These emissions are essentially the main cost for the DEX: the price paid to attract and retain liquidity. What matters then is what comes on the other side of the balance sheet – the revenues: in our case, it’s the fees collected.

On Curve, revenues stem from the “admin fees” of each pool, which are usually set at 50%. This means the fees collected on a given pool are split 50/50 between the LP and the DAO/veCRV holders. 

![curve-revenues](img/2024/crv-vs-velo/curve-revenues.png "Overview of Curve Revenues: the light blue are admin fees, in yellow fees paid to the LP, and in deep blue revenues stemming from the crvUSD stablecoin - source: curvemonitor.com") 

On Velodrome, it's straightforward: liquidity providers get no exposure to the fees collected on the pool they supply; they are incentivized through $VELO emissions only, meaning that the DAO/veVELO holders get 100% of the fees generated on the DEX.

While this core difference already has a massive impact, the following one is even more meaningful as it pertains to how those fees are distributed to veCRV/veVELO holders.


### A.2/ Model for the distribution of fees: a fairer and more efficient approach

Curve harnesses a model that could be described as **a fee mutualization system**: the fees veCRV holders receive depend only on the amount of veCRV they control. Without getting too technical, those fees are collected in the various tokens involved in the pool (such as USDC/USDT/DAI for the 3pool), and every week, harvested, swapped for 3pool LP token, and then made available for claiming to veCRV holders – as you can see, this means somewhat of an infrastructure to operate, the cost of which scale with the number of pools on the Curve DEX.

On the other hand, Velodrome provides a superior model on all dimensions, as it achieves better DEX/LP/token holder alignment without any infrastructure required. Let’s see how.

Simply put, **Velodrome connects gauge-voting activity with fee distribution**. Here, the amount of veVELO one controls matters, but even more important is which pool one votes for since the **voters are exposed to the fees collected on the pairs they vote for only.** They collect the fees as such (i.e., a voter of the ETH/USDC pool gets ETH and USDC), meaning the infrastructure required is much more manageable.

Velodrome ties fee distribution to the gauge-voting activity: veVELO holders receive the fees collected on the pool they vote ONLY, paid as such every week. It enables the better alignment of veVELO holders with the best interest of Velodrome as a DEX compared to Curve.

This simple twist creates an interesting voting flywheel. High-volume pairs collect lots of fees, meaning high incentives for voters. This leads to many votes, which direct sensible emissions to the pair, attracting more liquidity providers, enabling more volume processing, etc., until an equilibrium point is reached. This means that high-volume pairs sustain themselves without bribes or a benevolent profit-minimizer whale-voter needed, which is not the case with Curve.

![velodrome-revenues](img/2024/crv-vs-velo/velodrome-revenues.png)
Velodrome Revenues Overview - [source: 0xkhmer dashboard](https://dune.com/0xkhmer/velodrome)

![aerodrome-revenues](img/2024/crv-vs-velo/aerodrome-revenues.png)
Aerodrome Revenues Overview - [source: 0xkhmer dashboard](https://dune.com/0xkhmer/aerodrome)


### A.3/ What it means in practice

Enough with the explainer; let’s illustrate by considering the case of a veCRV/veVELO voter, who decided to vote for a pair processing minimal volume (the situation is common).

On Curve:



1. A significant veCRV holder votes for a pool processing a marginal amount of volume compared to its TVL, either to collect a bribe or because he wants to support the tokens involved in the pool.
2. His voting activity is detrimental to Curve as a DEX because he directs emissions where they are unnecessary.
3. He receives the same amount of 3CRV as a more Curve-aligned voter with an equivalent veCRV bag trying to direct incentives to maximize volume.

Now on Velodrome: 



1. A significant veVELO holder votes for a pool processing a marginal amount of volume compared to its TVL, either to collect a bribe or because he wants to support the tokens involved in the pool.
2. His voting activity is detrimental to Velodrome as a DEX because he directs emissions where they are unnecessary. 
3. He receives a marginal amount of fees since the pool he is voting for is processing a marginal volume.

The situation is the same in reverse for voting on a high-volume pool that would be of interest to the DEX:



* On Curve, this DEX-aligned voter will receive the same amount of 3CRV as anyone holding the same bag.
* On Velodrome, this DEX-aligned voter will be well rewarded, as he will be a majority voter on a high-volume pair: an ideal situation to maximize fees earned.

On both sides, bribes are paid to voters and can lead to situations where votes are directed to pools that are not optimal in terms of volume processed. However, on Curve, there is no penalty for doing so. On Velodrome, bribers of such pools compete with high-volume pools offering attractive APR to voters, with or without bribes. 

The same thing, from another angle: on Curve, the cost of bribes depends only on the value of CRV emissions. On Velodrome, the baseline price a project must pay to gather votes depends on the total bribes + fees collected on other pools. This means that high-volume pools push the cost of bribes upward, entertaining yet another flywheel in the flywheel.

Understanding the above means understanding the core difference between the Curve and Velodrome models. However, to get the full picture, more elements must be considered. Let’s discuss the LP boost now.


## B/ LP boosts & its impact on the ecosystem

LP boost, as it is called, is a Curve-specific feature. Many protocols forking the veCRV tokenomics, such as Balancer with its veBAL, also use it. It enables veCRV holders to earn more CRV rewards on their LP, factoring in several elements, including the size of their veCRV bag and the size of their various LPs. Thus, with appropriate veCRV ownership, an LP can get an “LP Boost” of up to 2.5x compared to the base emission rate.


### B.1/ LP Boost explained

To maximize the boost obtained, up to 2.5x maximal, one must:



1. Own as much veCRV as possible
2. Have LP positions in as many pools as possible.
3. Have a proportionate/balanced amount of TVL in those various pools.

**Simply put, LP Boost is a rugged game from the get-go**. It is not designed to benefit individual veCRV holders over their LP but to attract meta-protocol, such as Convex, who can achieve 1+2+3 consistently. **The growth of Convex is not a success story; it is by design (Curve’s design)**. If it were not for Convex, another similar protocol would own most of the veCRV supply. We observed similar patterns with other protocols that adopted LP Boost: Balancer has Aura. Convex and Aura control > 50% of the veCRV/veBAL supply.

Velodrome and Aerodrome completely avoid the possibility of a new protocol to gobble up the supply by not having any boosting mechanism. As we’ve seen with Curve, Convex emerged and captured most of the supply; now, all LPs are earning with a boost, and none are benefiting from any disproportionate amount of CRV. The system has converged to everyone earning about the same effective boost, or in Velodrome/Aerodrome’s case, no boost since the future outcome would’ve been LPs earning the same effective boost. The other fact remains that since Convex has a majority of CRV locked, they control the future governance of CRV. 


### B.2/ Consequences of LP Boost

The existence of the LP-Boost calls for a Convex-like layer on top of the DEX; there is no avoiding it. At this point, some could think: "So you have a protocol gobbling most of your emissions and locking them forever; what's the problem?"

The answer is simple: it's simply inefficient design since those meta-layers provide features that could be delivered less convoluted at the base level (by the DEX itself) and without the fees.

Curve needs Convex and the bribe marketplace: Votium, Warden, and Hidden Hands. But also the auto-compounder/vote delegation manager: Airforce Union, Concentrator, etc. You end up with dozens of protocols taking some fees here and there to deliver something that Velodrome manages to pack in natively. This makes the experience more complex for the users, who must know about these dozens of protocols and their subtleties to make the most of Curve.

Also, remember how, while discussing the fee distribution, we mentioned that Curve required a much more dense infrastructure to operate? Well, imagine the mess that veCRV+LP Boost is in the backend. There is a reason why both Curve and Balancer are taking ages to ship on a new L2, and often with partial functionality (such as no LP boost, surprise surprise.).


## Seamlessly expanding beyond what Curve offers

On Velodrome, the bribe marketplace is built-in: projects can post their bribes directly on the Velodrome frontend, and voters can check available bribes and vote in the same place. New features keep being delivered and added to the same interface used by all participants: LPs, projects, and tokenholders.


### Velodrome Relays

They go from quality-of-life / gas-saving upgrades, such as the “auto-max-lock”, saving lockers for those who wish to remain max-locked to maximize their gauge-voting power the hassle of doing it manually, to much more extensive features, like Relay, a veVELO position management system.

![velodrome-relay](img/2024/crv-vs-velo/relay.png)

It’s a tool catering to projects using Velodrome to grow liquidity on their pairs. It enables them to set up their voting and bribing strategy and implement it automatically: no need to submit weekly transactions anymore. Relay has another benefit, since currently, the strategy available is a veVELO-maxi one, compounding all fees & bribes collected into VELO and relocking it to maximize voting power: it creates a sizeable VELO sink, directly indexed on the fees distributed by the exchange. [Almost 1/5 of all veVELO are already there](https://twitter.com/VelodromeFi/status/1762908204894445834).

As the Relay feature matures, more strategies will be available to its users, including some that compound all the fees and bribes earned into veVELO but, for instance, make them claimable in ETH or USDC. It will prove very convenient for veVELO holders that are not looking to support a project in particular.


### veNFT: Tokenized locked positions

Velodrome has other neat innovations packed in, such as the still under-appreciated veNFT: with Curve, veCRV is non-transferable, making their management painful. Velodrome can achieve the same alignment but enables transferability: veVELO positions are represented by a veNFT that can be transferred. There is no way of redeeming a given veNFT for the underlying VELO tokens apart from waiting for the lock to expire. However, it eases the management of such a position by enabling its transfer. There is also [an OTC market for veVELO veNFTs](https://decode.market/), where holders can sell their position to interested buyers at a fluctuating discount compared to the value of underlying VELO tokens.


### A deep understanding of the nature of the game

Exchanges like Curve or Velodrome are a particular product type in the DeFi landscape. In regular business terms, **they could be described as B2B2C: Business to Business to Consumer**. They are B2B because their first customers are other projects – the various protocols looking for liquidity. If they successfully service this market, the projects they onboard to their DEX will do the B2C work for them, as their liquidity pools present opportunities to their respective token holders.

In that regard, I feel like Curve utterly failed. With its pyramid of solutions nested on top of one another, Curve is particularly unfriendly to onboard for projects. They wanna bribe? All right, decide between veCRV or vlCVX bribes on Bribe.crv, Votium, Warden, or StakeDAO. Do they want to manage their own CRV? Fine, just pick between veCRV, aCRV, cvxCRV, sdCRV, vlCVX, uCRV, etc. While this myriad of options might ravish Curve-enthusiasts, it turns, in my perspective, into a negative quality for the B2B side of things. 

In contrast, the experience with Velodrome is seamless: one place where everything happens, one option for each – without needing to compare between half a dozen cryptic and sometimes misleading alternatives. Coupled with the previous characteristics of the veCRV games discussed before, especially the LP Boost, it makes the [Curve ecosystem particularly unfriendly to new entrants](https://tokenbrice.xyz/farewell-glc/#the-case-of-the-crv-wars): **who would want to enter a race rigged in favor of the first entrants three years after it began**?

![tour-de-op](img/2024/crv-vs-velo/tour-de-op.png)

Moreover, the Velodrome BD efforts are remarkable; the team is broadly available to help onboard new projects, and several programs are designed to make the experience as simple and compelling for new entrants, regrouped under the “Tour de OP” umbrella, which includes a bribe matching program, lock bonuses and vote boosting.


## PARTING WORDS

As you might have seen, both Velodrome & Aerodrome have attracted much attention lately, thanks to their token seeing positive momentum: I think it's well deserved. The release of Slipstream, Velodrome’s implementation of Concentrated Liquidity, will increase the volume processed per unit of TVL, unlocking the flywheel's next growth phase. Aerodrome, Velodrome’s fork on the Base network, has seen spectacular growth since it launched six months ago, further demonstrating the model's viability.

In the longer term, the Velodrome team is starting to [refer to Velo as a "MetaDEX"](https://medium.com/@VelodromeFi/velodrome-the-metadex-48e4af1ef9a4), hinting at Velodrome becoming the base liquidity hub not just of Optimism but for the whole Superchain: all chains built on the OP stack.

Time will tell, but Velodrome is already a resounding success on Optimism, so managing a cross-chain DEX properly would be a game changer. This is especially true considering how much Curve & Balancer has failed there—not because they did not try, but simply because their convoluted infrastructure with LP boost makes cross-chain deployment painful (Hello AuraFinance distributing AURA on chains where... there is no liquidity for $AURA).

PS: I’m addressing the DEX part of the product suite here, which is the complete product for Velodrome but not for Curve, which now has crvUSD and Llamalend. Still, even with crvUSD included, Aerodrome is now collecting and redistributing more fees than Curve, all of this while being present on one chain only vs 13 for Curve. While Curve-DEX has been sub-par for a while, the team has repeatedly proven innovative and able to bounce back. crvUSD revenues have already flipped those of Curve-DEX, and who knows what Llamalend could achieve.

Game on: let’s wait and see.

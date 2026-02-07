---
title: "The Cycle of Aggregation Spins On, Now with Lending"
description: "The real edge isn’t in finding the rate; it’s in owning the rails that connect them all."
date: '2025-08-10T01:13:50.191Z'
categories: [Lending]
tags: [DeFi, Ethereum, Decentralized Finance, Lending, Aggregation, Fluid, Euler]
url: lending-aggregation
image: https://raw.githubusercontent.com/TokenBrice/blog/refs/heads/master/static/img/2025/lending-aggregation/aggregration-lending-cover.png
toc: true
draft: false
type: post
difficulty: "intermediate"
---

Something big is happening in onchain lending. Beneath the surface, a quiet shift is reshaping how liquidity moves, how markets connect, and how users access yield. A wave of new models, integrations, and rising stars like Euler and Fluid rewrote the rules with unprecedented efficiency and flexibility. A new layer of coordination is emerging and could redefine lending itself: today, we pull back the curtain on lending aggregation.

## The Cycle of Aggregation

I’ve seen a similar scenario unfold on the DEX side, with the rise of Uniswap, followed by competition from Sushi, aggregators, and the arrival of UNIv3. The core concepts required to analyze both transitions are similar, and I’ll explain them in this article.

The first thing to note is that it’s a pattern, in which I see four moments: 

1. **Vertical Inception**: First, a new vertical is discovered. 
2. **Product Proliferation**: As more teams enter the vertical, the number of options available to users increases, leading to a situation of offer saturation.
3. **Aggregation**: Aggregators emerge as they deliver tangible value to users (better price, faster, safer, etc.) compared to the underlying site-per-site experience.
4. **Offer-Side Customization**: With aggregators now commonplace, the market is ripe for greater customizability of the offer side, which aggregators can now process and distribute to users.

This scenario represents the base level, typically complemented by another stream that is observed for both exchanges and lending: **the increasing customizability of the offer side**, resulting from a shift from a pool model to more on-demand and personalized offers (OTC). As this happens, the aggregators become even more crucial as they now deliver to the user what they would not necessarily discover on their own. To put it another way: while **aggregators find their PMF harnessing pooled underlying **(ex, UNIv2, Curve), **their utility truly shines once the more customized offer layer is developed**.

Note that while we will discuss instances of this pattern for lending and decentralized exchanges, the situation is similar for bridging, with the aggregation layer growing strong (Jumper, Bungee, Infinex Swidge, etc.).


## The “Problem”: Densification of Lending Offers

Lending aggregation emerged to solve a tangible problem, manifested by the demultiplication of chains, lending protocols, and their models, together enabling **an exponentially rising number of ways to collateralize onchain**.

First, you have the broad, **generalist money markets** like Aave or Compound. They have similar collateral coverage and offerings. Both support many flavors of staked ETH, yield-bearing stables, and tokenized BTC as collateral.

CDP protocols **deliver tools more suited for advanced use cases, such as looping or high-LTV borrowing. Here again, the options are multiplying: it’s **[BOLD forks season](https://www.liquity.org/blog/forkonomics-collaboration-not-competition)**!

You also need to factor in the chain problem: those protocols mentioned above often exist on **several chains with segregated markets**, which adds a whole other layer of opportunities. You also have smaller but impactful trends, such as relending, where stables issued by another protocol and already mobilized are used as collateral, with [Level](https://www.level.money/), [Resupply](https://resupply.fi/), or [Asymmetry](http://asymmetry.finance/).

And finally, there is the **industry-wide trend towards greater customizability of the offer side**, kick-started by Euler and Morpho, and soon to be followed by Aave with the V4 release. The main goal here is to be able to accommodate institutional players (KYC, restricted access, etc.).

On this front, another OG worth mentioning is [GearBox](https://gearbox.fi/), since it’s been doing it for almost half a decade already, although their angle is less institutional-focused: Gearbox wraps the borrowing activity of the users in a smart contract, enabling it to implement logic pertaining to the usage of funds, such as allowing users to borrow, but only to acquire specific exposures.

**The customizability of the lending experience can be mapped on a spectrum bounded by Aave and ETHLend:**

* ETHLend being the most customizable with each situation specific to its borrower
* While Aave v1/2 is the most standardized, since all borrowers are under the same terms

![lending-customizaility-spectrum](/img/2025/lending-aggregation/lending-customizability-spectrum.png)

## Aggregation From Every Angle

So, with the multiplication of offers and their increasing diversity, the only logical answer is aggregation:


### Information Aggregation

The first problem is to identify the various options available for a specific collateral/borrowed asset pair on a given chain. This is precisely what [DeFillama Borrow Aggregator](https://defillama.com/borrow) does:


![defillama-borrow-aggregator](/img/2025/lending-aggregation/defillama-borrow-aggregator.png)


This facilitates the users’ **discovery of the options** they could harness, but they still have to research the venues they are unfamiliar with and proceed with the execution themselves. So some projects go one step further, factoring in the execution and management as well: enters [DeFiSaver](https://defisaver.com/).


### Interface Aggregation

[DeFiSaver’s](https://defisaver.com) promise is straightforward yet salvatory: **a single interface to manage your lending positions on all protocols, plus some neat automations, migration, or tracking tools on top**. This is particularly handy for users harnessing several protocols at once, or looking to make use of the automation to auto-leverage or deleverage their positions when certain conditions are met.


![defisaver-discover](/img/2025/lending-aggregation/defisaver-discover.png)


Thus, while DeFiSaver is not a protocol per se, it does deliver more options borrowers can harness to create and manage positions, and is worth mentioning. In addition to management, it facilitates the discovery process through analytics and the [Discover](https://app.defisaver.com/discover) tool, enabling users to find the best venues for their positions, similar to DeFiLlama.


### Protocol Aggregation

The next and last step is, of course, to aggregate several protocols themselves. While this idea is commonplace for yield with Yearn and its vaults, it’s rarer in lending. Here, a prime example is [Altitude](https://app.altitude.fi/?referrer=tokenbrice):

It's essentially a borrowing position manager doing two things: 



1. Refinances between protocols to optimize borrowing costs (Aave or Morpho)
2. Deploying the overcollateralized capital to generate yield used to auto-repay the debt (on Curve, Pendle, or Morpho) 

It is to me **a wild example of effective lending aggregation**: I deposit my collateral on Altitude and borrow; in the background I might have used Aave or Morpho, or maybe switched several times between the two if I held the position long enough; I don’t even need to know, I just know I got the best rate.


## What About Curators?

The recent spark of lending customizability we are experiencing stems from the emergence of a model harnessed by many to **challenge Aave’s dominant position on the bluechip lending markets**, since at this point, it’s impossible to challenge Aave on available size or perceived safety. Euler or Morpho are infrastructure builders as much as protocol operators. They provide building blocks, harnessed by Curators, to deliver customized and optimized lending experiences to specific communities.

Yet, they also make the solution even more complex to unpack, since that, on top of [assessing the protocol (DeFiScan can help)](https://www.defiscan.info/), you now also need to **evaluate curators**, which is a wholly different logic (track record, AUM, etc.). On the other hand, on the Aave side, so far, there was no curator, or only a single omnipotent one: the Aave DAO, the entity handling the risk management and parametrizations through its various providers (AGI, LLamaRisk, etc.).

Curators and aggregators work hand in hand. Curators harness pieces of infrastructure to deliver novel lending markets, while aggregators connect all the already existing offers to facilitate the user experience.

Lending aggregation is becoming the connective tissue of an increasingly fragmented credit market. As protocols splinter across chains, models, and customizations, the role of aggregators shifts from “helpful tool” to “market infrastructure.” Just as DEX aggregators became indispensable once liquidity fractured, lending aggregators will define how capital flows, who captures the spread, and which strategies remain competitive. The next cycle of DeFi lending won’t be about discovering the best venue—it will be about routing, composing, and automating across all of them. And in that race, the winners won’t just lend smarter; they’ll aggregate better.

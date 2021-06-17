---
title: "🎡 DeFi Flywheel : engineering protocol to protocol synergies through tokens"
description: "We analyze the race to accumulate CRV with the launch of Convex to understand the flywheel concept in DeFi: protocols that evolve in synergy thanks to their tokenomics."
date: '2021-06-17T01:13:50.191Z'
categories: [🌌 DeFi, 💸 Practical DeFi]
tags: [DeFi, Ethereum, DeFi, Money Markets, Liquity, Curve Finance, CRV, Polygon, Convex, CVX, Yearn Finance, Pickle Finance, Adamant Finance]
toc: true
tocNum: true
url: defi-flywheel
---

In three weeks, the Convex protocol attracted over $3 billion in deposits, while becoming the largest 🐳 whale of CRV, today and probably forever. Luck is never a negligible factor, but with such a smashing entry into DeFi top protocols, we must look much further. Indeed, the key to understanding the meteoric rise of Convex is tokenomics, and this is our topic of the day!

In DeFi, besides the technical, you also have to be a fine sociologist, or rather a "game theorist" as we say around here: to know how to anticipate the reactions of crowds to a given set of rules.

The emergence of liquidity mining programs last year showed that the right set of rules can move huge amounts of capital. The question now is how to do it wisely, i.e. with an awareness of what is at stake **in the long run.**

Indeed, liquidity mining by itself only attracts **mercenary and opportunistic deposits**. In fact, liquidity mining is more a tool to make a project known than to perpetuate it. 

To last in DeFi, it is a matter of tokenomics: i.e. the mechanics of the native tokens of protocols. **Tokenomics is in a way the gameplay of a DeFi protocol**.

![flywheel-defi-cover](/img/2021/defi-flywheel/defi-flywheel-cover-en.png)

As you probably know, I am a big fan of the CRV model. It's perfect, since the game around the CRV token has never been as lively as it has been in the last few weeks. Some people even talk about #lockening to describe **the race to accumulate CRVs** that Convex, Yearn and StakeDAO are engaged in.

Let's go into details to understand the concept of flywheel with the example of Convex / Curve. I will finish by analyzing protocols that could be used in a similar scenario.

## The rise of the first 🎡 DeFi flywheel

With the launch of Convex, a new term began to be used to describe its operation and tokenomics: 🎡 flywheel.

There isn't a precise definition yet, but I'll try one: it describes a protocol that achieves a winning trifecta:

1. A tokenomics that offers interesting opportunities to token owners optimistic about the future of the model.
2. A protocol that is itself relevant and meets a real need, ideally in direct synergy with another protocol.
3. A liquidity mining program (+airdrop) to start the loop and attract the first token owners.

I generalized the Convex model, but it has an additional feature: Convex is a kind of "meta-protocol": it is **built entirely on top of Curve Finance and in synergy with it.**

Thus, the forerunner of the flywheel would probably be found among protocols built in synergy with others. For example, although it is built on top of BSC and [suffered a significant attack recently](https://rekt.news/pancakebunny-rekt/), the Bunny protocol helped the DEX PancakeSwap to develop.

Bunny offers to manage Pancake liquidity provider positions, while issuing its own token based on the returns generated. This simplifies the management of liquidity providers positions on Pancake while generating an additional source of return (BUNNY token).

So to fully understand the concept of 🎡 flywheel, let's analyze the best one we've had the opportunity to see so far: Convex. It turns out to be a bit more complicated because it relies on Curve, so you first need to understand the curve tokenomics.

## CRV: a tokenomics for 🎡 flywheels?

Curve Finance's tokenomics is almost a year old and yet it is still often misunderstood

The great elegance of the CRV tokenomics resides in **aligning the interests of several actors better than any other tokenomics known to date**: the liquidity providers, the CRV holders and the Curve protocol itself.

Indeed, the model tends over time to merge the two populations (CRV holders and LP) through two mechanics:

1. Liquidity providers are incensitivised in CRV.
2. CRV stakers (VeCRV holders) can "boost" the CRV yield of their liquidity provision on Curve.

This model creates an interesting path for protocol users, who are **strongly encouraged to make a long-term commitment**. Indeed, locking CRVs into VeCRVs becomes more and more efficient the longer the commitment is - the maximum being 4 years.

To go further, I invite you to read [this article](https://stakecapital.substack.com/p/curve-tokenomics-and-first-mover)

![crv-tokenomics](/img/2021/defi-flywheel/crv-tokenomics.png "Basics of the CRV tokenomics")

Nevertheless, the CRV model also has its limitations, the most obvious one being the impact of Ethereum transaction fees: large sums of money can be required for the game to start making sense.

The thing is, for a long time now, the biggest contributors of liquidity on Curve have not been users but **other protocols**. Pooling funds reduces the impact of gas fees while potentially developing a VeCRV accumulation strategy.

As a result, various solutions have emerged to **manage liquidity positions on Curve**, the best known being Yearn, but there are also Harvest and StakeDAO. While they can be useful for depositors, they suffer from two major limitations: high management fees and a parasitic approach. Yearn, Harvest or StakeDAO immediately sell any farmed tokens. This results in increasing selling pressure on the native token of the protocols used to produce the return.

## The Convex model : the first flywheel 🎡

The Convex way to operate offers a "Yearn-like" service  to liquidity providers on Curve: automated management of their position to maximize returns. Like Yearn, Convex has a VeCRV accumulation strategy to maximize the return of depositors in CRV through the boost mechanism.

Nevertheless, the underlying approach is totally different from Yearn and is part of a virtuous synergy with Curve :

1. **No systematic selling**: unlike Yearn, Convex does not sell the tokens it farms. Liquidity providers are thus remunerated in CRV but also in CVX, the native token of Convex.

2. **The fees collected by Convex are 100% dedicated to the protocol**, while Yearn for example pays strategists - obviously quite redundant on a simple strategy like this.

3. Thanks to the distribution of the collected fees, Convex creates two **interesting staking opportunities** to compose its returns, detailed below.

4. Finally, **the liquidity** on the token that represents a CRV in Convex (CvxCRV) is more optimal than the Yearn equivalent: CvxCRV trades in a pool directly against the CRV, with an incentive program in CVX.

### Fees : the lifeblood of success

Understanding the fee structure is key to get what has happened with Convex. The protocol now controls over 32M VeCRVs, which is **almost twice Yearn's total, and that's just after three weeks of existence**.**

![convex-curve-stats](/img/2021/defi-flywheel/convex-curve-stats.png "Yield generated by Convex on Curve Finance")

Convex charges a total fee of 16% on all CRVs farmed on the protocol (compared to 20/2 on all tokens for Yearn, or 30% for Harvest for example). Of the 16%, 1% is used to cover operational costs such as the gas cost of collections.

![convex-synergies-CRV](/img/2021/defi-flywheel/convex-synergies-CRV-en.png "Convex / Curve : Synergies and value capture ")

The most interesting part is the redistribution of the remaining 15%, i.e. 15% of all CRVs farmed by Convex (**over 400,000 CRVs per day** at Convex charges a total fee of 16% on all CRVs farmed on the protocol (compared to 20/2 on all tokens for Yearn, or 30% for Harvest for example). Of the 16%, 1% is used to cover operational costs such as the gas cost of collections.rythme actuel). You can view the [Convex Curve position via CurveMarketCap here](https://curve.fi/pools?see=0x989aeb4d175e16225e39e87d0d97a3360524ad80) Two staker populations are eligible for this juicy pie:

1. **10% is paid back to CvxCRV** stakers, in CRV, in addition to their return in 3pool and CVX tokens (+airdrops VeCRV holder). Owning CvxCRV becomes much more attractive than VeCRV for a simple depositor.

2. **5% is returned to the CVX stakers**, in the form of CvxCRV. This means that 5% of all CRVs farmed by Convex are captured and locked within the protocol. This mechanically increases the pool of VeCRVs even if no third party CRV deposits are made.

**The situation is still ongoing and there are still surprising gaps: for example, at the time of writing (June 07) the total capitalization of the CVX token is not even half of the value of the CRVs that the protocol has ($30M vs $80M). I think the situation will harmonize in the long run.**

## How to anticipate the next flywheels?

With some notions about Curve and an analysis of the flywheel 🎡 Convex, we now have the cards in hand to venture into the game of foresight. Before that however I propose instead to go look into the past to analyze an almost failed flywheel : Pickle Finance.

### Pickle Finance : the wrong timing

On paper, Pickle has all the makings of a flywheel: it is a system to increase the returns on Yearn deposits through the additional issue of PICKLE tokens. PICKLE has elements of the VeCRV system, with a locking mechanism (DILL) that allows to boost PICKLE returns on deposits on Pickle Finance.

Except that... Pickle does not technically add anything to Yearn, apart from issuing PICKLE. Moreover, Pickle does not specialize: farms are offered on Yearn vaults but also some Sushi pairs. Unlike Convex, Pickle is therefore not able to develop a unique advantage (moat) on farmed services.

In DeFi, nothing is definitive. Pickle's situation could evolve, if the tokenomics of the underlying protocols (YFI and SUSHI) evolve. Both protocols seem to be moving towards a reappropriation of the VeCRV model, so it is quite possible. A model that combines the Adamant/Ellipsis burn logic and the Curve boosting has even been proposed for Sushi: **[oSUSHI](https://forum.sushi.com/t/sushinomics-introducing-osushi/4055)**.

![veYFI](/img/2021/defi-flywheel/veYFI.png "Interface example for the YFI lock/boost mechanism (veYFI)")

### Adamant Finance : 🎡 a flywheel on Polygon's LP ?

Adamant is a still new protocol that exists on the Polygon sidechain. It allows the easy management of liquidity positions on the main exchange services: QuickSwap, Cometh, SushiSwap, etc.

In addition to automatic compounding of returns, Adamant also offers additional ADDY rewards (based on profits generated). All ADDY earned are vested (locked) for 3 months and can be withdrawn earlier with a 50% penalty. This is redistributed to those who agree to staker + lock their ADDY for 3 months.

In addition, all ADDY stakers (even vested ones) benefit from a share of the fees collected by the platform, distributed in wMATIC. The protocol thus has a tokenomics already quite elaborate with different retention mechanisms, but it still has some improvements to find to become a flywheel.

The first one would be to introduce a greater incentive to lock in ADDYs through a boost system similar to Curve. Depositors with ADDYs in stake+lock will have a better return in ADDYs on their LP position. This is already under discussion or even in development.

Adamant still has to develop a synergy with the farmed protocols as strong as Convex with Curve. This is difficult or impossible for the moment because none of them have tokenomics as subtle as CRV.

### An "X" Liquity service : 🎡 money market flywheel

So far, we have discussed flywheels built on decentralized exchange services, which seems the most obvious. Nevertheless, we can consider similar models on other types of services, like money markets.

So I propose to finish with a theoretical flywheel of my own. To my knowledge, such a protocol does not exist yet: it's up to you!

The basic equation is simple:

1. There is a strong demand for "ETH passive" products - products that develop strategies on ETH in order to accumulate ETH.

2. One option is to borrow stablecoins using ETH as collateral. This way, stablecoins can earn an additional return.

3. For this strategy, Liquity would be **the platform of choice without question**. Indeed, the cost of borrowing is the lowest in the market (almost 12x cheaper than Maker over a year) and there is no shortage of opportunities for yield on the LUSD stablecoin.**

![protocole-x-liquity](/img/2021/defi-flywheel/protocole-x-liquity-en.png "Example of a flywheel protocol built on Liquity (fictional for the moment)")

The challenge of such a pooled strategy is to **manage the collateralization ratio** and to be able to balance it quickly if the market moves. Here again, Liquity lends itself well to this since the stability pool offers an attractive return on the LUSD while allowing **the rapid mobilization of LUSD to repay the debt if necessary**.

The X protocol in question would offer **a passive ETH investment product** for users who would not have to manage the position themselves. We can also consider that the X protocol has its own token with a tokenomics that addresses one of the main dangers of the strategy: the lack of predictability. Thus the native token of protocol X could be used to encourage long deposits of a predictable duration (users lock their ETH over 3/6/9/12 months for example).

Long term commitments also allow to **develop a strategy on the LQTY farmed by the LUSDs.** By committing ETH for one year in the protocol for example, the user will be able to claim a portion of the LQTYs farmed by the whole protocol, and benefited, for life, from the LUSDs and ETHs they generate. The synergy of the protocol with Liquity as well as the long term returns are maximized if protocol X does not sell any LQTY, as is the case in the concept proposed above.

I hope this article will help you better understand what has been going on with Convex, Yearn and Curve over the past few weeks and use the lessons learned from this episode to identify similar opportunities in the future.

The nice thing about different incentive mechanisms is that they precede action. In game theory, there are no certainties, but some behaviors are almost mechanical - for those who really understand incentives and their issues.

Try it for yourself !

_🙏 Huge thanks to HHK, Charles, Thomas, Erwan & FrenchTony for proofreading the French version of this article and translating it integrally into English._
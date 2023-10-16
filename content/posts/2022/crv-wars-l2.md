---
title: "⚔ Advanced CRV warfare: analysis of protocols built on top of Curve and Convex "
description: "Votium, Warden, Concentrator, CCRV, Conic, etc. The layer of protocols involved in the Curve Wars is getting denser: I offer a tour to better understand the dynamics around CRV and CVX tokens."
date: '2022-04-05T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Understanding]
tags: [DeFi, Ethereum, Decentralized Finance, Curve Finance, CRV, Polygon, Convex, CVX, Votium, vlCVX, veCRV, bribe.crv, Conic Finance, CCRV, Bent Finance, Warden, Concentrator, Lendflare, Curvance, CVE, LFT, CNC, BENT]
toc: true
tocNum: false
url: crv-wars-l2
---

The game and the fight around CRV and CVX tokens have changed in scope since my last article describing the original Curve Wars, now almost primitive. The infrastructure around Curve has become much denser with the arrival of Convex of course, but also Votium, Union Llama Airforce, Concentrator, CCRV, Lendflare, Warden, and many other protocols still in development.

![curve-wars-l2-cover-tokenbrice](/img/2022/curve-wars-l2/curve-wars-l2-cover-tokenbrice.png)

To assume a strategic position on CRV or CVX, one must now be able to support an investment of several tens of millions of dollars. Thus, the race to accumulate CVX and CRV has become primarily a game for DAOs or whales. More specifically, DAOs seem to prefer CVX to CRV, which represents a more favorable trade-off: 

1. **Boosts LP Curve**: ability to build liquidity via votes on Curve gauges
2. **Yields**: 4-5% in cvxCRV + potential bribe yields if capacity is not used (or the protocol also use bribes)
3. **Flexibility**: CVX can be used to its maximum capacity by committing 16 weeks + 3 days (vlCVX) while CRV requires up to 4 years of commitment (1 CRV = veCRV).

So to extract the utility of CRV, CVX is a credible and more flexible alternative, which is why most DAOs focus on this token. Convex Finance has become a "functional L2" of Curve: a second layer that brings new features and a different set of tradeoffs.

However, Convex is not the only project that tried to realize this vision: there was also Yearn, which has now capitulated: Yearn's Curve vaults are essentially through Convex, which is now more profitable. Since then, many projects are trying to offer a synergistic brick with the Curve/Convex behemoth.


## CRV or CVX?

I won't go back to the basics of the separation between the two tokens here, that's a matter for an entire article if you're new to the subject: [⚔ CRV wars: understanding the race to accumulate the ability to influence the Curve Finance protocol]({{< relref path="/content/posts/2021/crv-wars.md" >}})

It should be kept in mind that despite the computable equivalence between CVX and CRV (1vl CVX controls about 4.8 veCRV - [source](https://dune.xyz/Marcov/Convex-Finance)), the two tokens have different tradeoffs as described above. 

The balance between CRV and CVX tends to hold, despite frequent swings: lately, the pendulum seems to swing more towards CVX. Nevertheless I think there is still room for other approaches that start from the source (CRV) and they are starting to emerge. 

Paladin's [Warden](https://app.warden.vote/) is proposing a protocol that helps liquidity providers on Curve maximize their returns and perhaps achieve the desirable 2.5x bonus by borrowing the capacity of veCRV tokens (provided by others) paid directly in CRV.

But there are so many other subtleties and interactions to keep in mind in order to understand the relevance of the strategies deployed by the different projects, DAOs and protocols to win the Curve Wars.

That's why this article proposes to review the CRV and CVX wars **by visualizing and detailing the whole ecosystem** that has developed around these two protocols.


## Curve's functional layer 2

{{< notice note >}}
In this article, I'm going to talk about "functional L2", or simply Curve or Convex L2. This is an image to describe this trend of multiplication of supports used to interact with Curve/Convex. 

Be careful not to confuse the term with "true L2s" / scaling L2s: the term in its original sense to describe a new chain that inherits the security of its parent while allowing for higher transaction throughput and more moderate costs. 
{{< /notice >}}

So we start with Curve's **Functional L2s**, then Convex's (itself a Curve L2), then borrowing services to leverage the many sources of return offered by the entire Curve ecosystem, and we'll finish with the CRV/CVX protocol-whales.

It's a dense and colorful adventure, but as is often the case with my articles, I'm offering you a summary of my research on the subject: enjoy your reading!

To lose you on the way, I propose you this map which summarizes the main actors of the Curve/Convex ecosystem:

![Curve/Convex L2 map](/img/2022/curve-wars-l2/curve-convex-l2-map-en.png "Summary of the main functional L2 protocols Curve/Convex")

### Convex Finance: Curve by the slice

Convex is the first functional L2 of Curve; other projects preceded it (yveCRV and sdveCRV) but they were not as synergistic with Curve and therefore only marginally successful.

In summary, Convex provides access to maximized and liquid CRV token returns through cvxCRV. The ability to govern and vote on the Curve gauges corresponding to the underlying veCRV tokens is redirected to the owners of vlCVX. Convex thus provides easy access to the Curve ecosystem (for veCRV owners).

Although Convex controls a large amount of vlCVX, the centralization of voting power on gauges is avoided by offering this capability to the highest bidder through Votium (bribes).

Convex is now basic, so I won't detail it further here. My previous article on CRV Warfare went into more depth on the model and the contributions of Convex: [⚔ CRV Warfare: Understanding the race to accumulate the ability to influence Curve Finance protocol]({{< relref path="/content/posts/2021/crv-wars.md" >}})


### Warden of Paladin: Curve on steroids?

[Warden](https://app.warden.vote/) is another possible path for Curve LPs, which offers a different set of tradeoffs to Convex. Warden does not directly control veCRVs, but instead offers to rent the boosting capacity of LP Curve from veCRVs owned by others.

The rental is paid directly in CRVs and by the week. It comes from veCRV owners who make it available, for the price and duration of their choice. The deal is concluded through the delegation of the corresponding veCRVs.

![LP Ve boost rental on Warden](/img/2022/curve-wars-l2/warden-veboost.png "LP Ve boost rental on Warden")

Warden thus returns to the LP Curve boost game. On Convex, most pools are boosted between 1.5 and 1.7x via Convex. Having your own stock of veCRV, increased by a Warden loan, allows you to reach 2x or even 2.5x maximum on certain pools.

Recently, Warden even offers a handy calculator to visualize the amount of veCRV needed to reach a given multiplier:

![Warden Calculator](/img/2022/curve-wars-l2/warden-calc.gif "A calculator to estimate the impact of a boost ve rental with Warden")


Warden is therefore a credible alternative for protocols, DAOs and large carriers who would like to optimize their LP Curve in a perspective of maximizing the obtained CRV.


## L2 Convex

Convex is not yet one year old (May 2021) but given the preponderant place that the service already occupies, abstractions built on top of it were quick to appear.



### Votium: Convex vote auction

The Convex protocol concentrates the largest amount of veCRVs owned by a single entity. Nevertheless, the voting capacity corresponding to the veCRVs owned by Convex (obtained thanks to the cvxCRV) is distributed among all the owners of the CVX token that "vote lock" it (vlCVX) for 16 weeks + 7 days).

Via snapshot, they can mobilize their voting power directly on the Curve pool gauge of their choice. [Votium](https://votium.app/) is an additional layer built on top of this feature: Votium allows any project to allocate a budget to support a given Curve gauge. At the end of the round, the vlCVX owners who voted on this gauge share the rewards, according to their voting power: these are the famous bribes.

![Votium bribes](/img/2022/curve-wars-l2/votium-bribes.png "More than $15M of bribes are paid every two weeks to influence the play of Curve gauges.")

Thanks to the impressive amount of veCRVs controlled by Convex, Votium has quickly emerged as **an essential tool to establish and sustain a presence on Curve**: consistent bribes on Votium can quickly make a Curve pool very attractive. 

We detail below the example of Frax Finance which offers around $5-7M of bribes each round; this allows to maintain attractive returns on the Frax/3CRV pool despite the massive dilution (the pool contains almost $3B of assets), and this without issuing their own token (FXS) for liquidity mining.


### Llama Airforce Union: shared management of vlCVX

The bribes offered on Votium are very attractive: this allows vlCVX to reach a return **of about 40% APR - most of which (90%) comes from the bribes**. However, managing your own vlCVX position has several constraints:

1. **Gas costs**, to lock in your vlCVX, but also to harvest the bribes.
2. Although it is possible to delegate, this leads to a dispersion of the rewards (paid in a dozen different tokens -> gas fees). So small and medium vlCVX holders generally prefer to concentrate their vote on a given project: more practical, but it implies not forgetting to **vote at each round**!

The Llama Airforce Union proposes to remedy these two main limitations, for the happiness of small holders as well as those who prefer a **100% passive management of their vlCVX**.

The concept is simple: the Union pools the management of vlCVX. The only action required from the users is the delegation of their vlCVX voting power to the Union contract. Thereafter, the Union takes care of everything:



* In each round, the Union takes care of claiming all the obtained bribes, and sells them for cvxCRV (=mutualization/immense reduction of the impact of transaction fees).
* The obtained cvxCRV are then deposited in the Pounder, which stakes them with Convex and composes the yield automatically (uCRV).

The Union thus offers a relevant alternative for CVX owners who intend to maintain and compound their position over the long term. As always, don't forget to pay attention to the fees:



* Gas fees are passed on and distributed to all Union users.
* A fee of 2% of the total bribes received is also charged in each round.

![Llama Air Force Union](/img/2022/curve-wars-l2/llama-airforce-union.png "Evolution of the Union TVL ⚠️")

{{< notice warning >}}
This TVL only takes into account the yields of the bribes compounded into cvxCRVs by the Union (uCRV). The vlCVX are not taken into account since they are simply delegated to the Union (about 2.5M CVX).
{{< /notice >}}


The Union has been a rapid success. The project originated from the [Llama Airforce](https://llama.airforce/#/convex/flyer), an already well-known source of information within the Curve/Convex ecosystem, which no doubt contributed to its adoption.


### Concentrator (AladdinDAO)

In short, the [Concentrator](https://concentrator.aladdin.club/) is a bit like the Union, but this time for liquidity providers. Thus the Concentrator proposes to manage LP Curve for its depositors: the rewards (CRV, CVX and potential other tokens) are automatically sold for cvxCRV and automatically composed (staking on Convex) via the aCRV wrapper.

The proposal is interesting and rather synergistic with Curve and Convex: it's a bit unfortunate to see that CVX are sold for the moment, but explained by the lack of available wrapper for vlCVX. The service offered by Concentrator is therefore rather relevant for **small and medium sized carriers who want to use their LP Curve to maximize their CRV** token exposure in an efficient way.


### Congruent CCRV: Curve/Convex flywheel optimization


One of the current limitations of Convex (or feature for some) is that despite the fairly dense liquidity in the cvxCRV/CRV Curve pool, it is often unbalanced. CvxCRV is liquid against CRV, but rarely at 1:1.

[CCRV](https://ccrv.finance/) is therefore designed as a mechanism to help rebalance this pool, using both Curve and Convex. The principle is quite simple if you understand the mechanisms of Curve and Convex:

![CCRV.finance](/img/2022/curve-wars-l2/ccrv.png)

1. Creation of the cCRV token, backed by 1 cvxCRV. The protocol stakes all the cvxCRVs deposited to back cCRVs in Convex, in order to obtain a return.
2. Creation of the Curve 3CRV pool: CRV, cvxCRV and cCRV
3. Bribes on the 3CRV pool to help it grow.

The mechanism will launch with an initial allocation of 1M CRV (provided by Congruent DAO). This will airdrop 1M cCRV (via bribes) over the first few weeks of the token's existence to help it launch quickly. 

While the launch plan seems pretty solid, the sustainability of the mechanism still seems uncertain. The addition of fees could allow the CCRV protocol to have its own liquidity (and therefore return in CRV, CVX and 3 pool) which could fuel the bribes while reducing their effective cost in the long run.

cCRV is not yet launched but is intended to be a **new optimization of the flywheel Curve/Convex**. Interestingly, cCRV is being developed by [Congruent](https://congruent.fi/), a DAO that develops "Governance as a Service" (GaaS) products.  


### Bent: the Convex of Convex?

[Bent](https://app.bentfinance.com/) is a true L2 Convex / L3 of Curve. The main question that arises with this project is whether there is anything to gain by going down to this level of depth.

Concretely, Bent works like Convex works for Curve: Bent allows you to stake Curve LP tokens: they are then staked in Convex (by Bent), and you benefit from an additional return paid with their native token - BENT, in exchange for fees collected by Bent:

![Bentfinance-fees](/img/2022/curve-wars-l2/bentfinance-fees.png "Fee structure on Bent, very similar to Convex")


As you may notice, the fee structure is almost identical to Convex. Finally, just as Convex created its own representation of CRV (cvxCRV), Bent creates its representation of CVX, the bentCVX. This can also be locked (weBENT) exactly like CVX->vlCVX, for 8 weeks to get an additional yield corresponding to the bribes.

Every two weeks (Curve gauge round), weBENT holders vote on Snapshot to allocate their voting capacity on the gauges of their choice. The votes of the weBENT holders are echoed via the CVX owned by BentFinance, themselves echoed in CRV vote by Convex: two levels of depth!

![bentCVX-lock.png](/img/2022/curve-wars-l2/bentCVX-lock.png "Locking BENTs gives access to the bribes collected on the underlying tokens (vlCVX).")



#### A relevant abstraction?

As I said when discussing Bent, the question here is not whether the model is relevant since Convex is living proof of that. Nevertheless, Convex is not a zero-sum game compared to Curve, since the protocol has brought new features that did not exist with just Curve:

1. Farm with LP Curve optimized, without having veCRV
2. "Liquid Locking" (⚠ cvxCRV/CRV exchange rate)
3. And the third point which is a bit of a consequence of the other two: Convex is now the biggest veCRV owner, and can therefore offer the bribe service (via Votium) with the most potential while being the most convenient (delegation, no need to claim every week, etc.)

If I detail the contributions of Convex, it is obviously to ask the question: what does Bent bring **functionally** compared to Convex?

1. Farming option with LP Curve without owning a veCRV even more optimized than Convex, but all the outperformance comes from the BENT emissions.
2. A less restrictive locking of CVX than direct locking via vlCVX (8 weeks at Bent, 16 weeks + 7 days at Convex)

For me, the third element is still missing to make Bent an interesting option, a mechanism that would create a real added value compared to Curve/Convex, in addition to farm optimization and a reduction of constraints.

Finally, I would be dishonest if I did not add one last point: the security and durability of the protocol. Indeed, Bent Finance has been attacked by an insider in December 2021 for several weeks. The attack was made possible by the fact that at that time, Bent's contracts were not secured by a multisig: [more information here](https://halborn.com/explained-the-bent-finance-hack-december-2021/).


### Conic Finance (CNC) 🚧: collective liquidity management on Curve/Convex.

{{< notice tip >}}
🚧 reports a protocol not yet launched
{{< /notice >}}

Similar to Bent, [Conic](https://twitter.com/ConicFinance) offers an additional abstraction from Curve LPs staked on Convex. However I think that this time the model has relevance.

Conic introduces the concept of "omnipools", which would simplify the management for Curve LPs by going back to the primitive level: here, it is directly the tokens that are deposited (e.g. USDC or DAI). The Conic omnipools will then distribute the tokens on different LP Curve positions which are then staked on Convex.

The depositors receive their CRV, CVX and CNC tokens from Conic. In a similar way to CVX, the CNC can be "vote locked" to :



1. Participate in bi-weekly gauge votes that determine the distribution of Curve pools by assets accepted on Conic.
2. Vote on the whitelist and blacklist of accepted Curve pools (and thus eligible for gauges)
3. Participate in the vote to decide which assets are supported on Conic
4. And any other governance decisions, including the potential activation of fees for the service (initially there will be none).

Conic's approach thus seems relevant and could be described as pooled asset management. It is a model reminiscent of [Tokemak](https://tokemak.xyz/) and goes one step further than Curve/Convex which remains at the level of governance determination of incitations. Here, governance votes will result in the actual movement of assets between different Curve pools. If the protocol manages to attract sufficient liquidity, it could become a major player in the Curve Wars, potentially with its own bribe system in the future.

![conic-finance-en](/img/2022/curve-wars-l2/conic-finance-en.png "How Conic Finance works, a collective liquidity management solution on Curve")


The project has just been unveiled and the approach being considered for launch is also interesting. Part of the CNC supply will be airdropped to vlCVX owners. For the rest, it will be distributed with community fundraising, liquidity mining on CNC/ETH and to depositors on Conic. To learn more, there is [only one article available for now](https://medium.com/@ConicFinance/conic-finance-pre-launch-announcement-7b9f485f59f2).


## Borrowing services with LP Curve/Convex tokens as collateral

At this point, you may start to get saturated just by mentioning a new potential wrapper on CRV, CVX or even cvxCRV: this is probably normal. Most of the protocols involved in the Curve Wars develop synergies directly at the token level, which remains the most direct. But we should not forget two other important types of actors:

1. Protocols offering a synergistic service with the Curve/Convex LP, such as using it as collateral.
2. Protocols / DAOs that have large amounts of CVX and CRV and can use them to develop a strategic position.

Before going to the whales and their strategies, I offer you two last analyses of protocols that allow you to borrow from an LP Curve position.


### Lendflare (LFT)

[Lendflare](https://lendflare.finance/) allows Curve LPs to borrow from their position an asset that follows the same peg, for example a DAI borrow with the LP 3pool token (USDC/DAI/USDT) as collateral. This limitation avoids liquidations due to price changes between assets: with Lendflare as long as a borrower pays back his debt on or before the due date he is not liquidated.

The critical point, as with any money market, is to attract enough depositors to make borrowing as cheap as possible and therefore competitive. Lendflare follows the logic of Curve's boosts: users who bring in cash (USDC, DAI, ETH or wBTC) to facilitate borrowing are rewarded with the LFT token.

Just like on Curve, here they can also benefit from a multiplier of up to 2.5x by locking in a quantity of LFT (veLFT) proportional to the deposit. There is even a very dense diagram that summarizes everything and will make you appreciate the special care I put into my home-made infographics:

![LendFlare](/img/2022/curve-wars-l2/lendflare.jpeg)

The protocol is still in the midst of deployment, although the borrowing functionality is already available. An initial sale (IDO) of the LFT token is underway, and an airdrop is also being discussed.


### Curvance (CVE) 🚧

Curvance tackles the same problem but with a different approach. Here the protocol is not interested in Curve LPs as collateral, but rather "wrapped assets" in general like cvxCRV, bveCVX (Badger) or yvBOOST (Yearn). To enable the borrowing of stablecoins with these assets as collateral, they plan to isolate the risk by relying on Fuse pools.

Again, the CVE token will be distributed to liquidity providers and a veCVE-like system is envisioned with a new subtlety: yet another wrap, a liquid version of the veCVE, the cveCVE that gives access to the veCVE's yield but delegates governance capabilities to the DAO. Again, boosts, gauges, and even potentially bribes are envisioned

For the curious, [documentation is here](https://docs.curvance.com/cve/).


## DAOs whales in CVX

Finally, to finish this overview of the Curve/Convex ecosystem, we should not forget to look directly at the tokens - and in particular the DAOs that have large amounts of CRV or CVX.

For CRV, there is not yet a clear dashboard summarizing the situation to my knowledge. For CVX on the other hand, there is a site for that: [daocvx.com](Daocvx.com). The protocols we will detail now do not have any synergy built natively with Curve or Convex, but they have a lot of CVX and use them to improve their competitive position in the CRV war.

![daocvx.png](/img/2022/curve-wars-l2/daocvx.png "Distribution of CVX tokens among different DAOs (⚠️DAO only)")

I'll let you dig through the list on your own, we'll just detail two: Frax and Badger.



### Frax Finance: Dominating the Curve Gauge Game

Frax has a long-standing strategy of dominating the Curve Gauge game to help drive FRAX adoption. It was one of the first DAOs to gain a consistent position in CVX; it is now the DAO with the **largest position with over 2.1M CVX**.

Frax is also known to be the most aggressive project with bribes and frequently offers the largest Votium bribe for its FRAX/3crv pool. In the last round (14), Frax's bribe was about **40% of the total value of all bribes** paid in that round ($6.5M / $16.2).

The reason Frax can afford to be so aggressive is that their vlCVX position reduces the effective cost of these bribes: thanks to their own votes, the protocol is able to [recover](https://etherscan.io/tx/0x090777069299e6e292363c6131b5cc5b463d598a7f89d3c7207148c0497587f8) a significant portion of the FXS used in each round. 

With this strategy, the FRAX/3CRV pool is able to **maintain a CRV issuance rate almost five times higher than the 3pool, for a similar total liquidity** (3pool: $3.3B, FRAX: $2.7B).


### Badger: a small corner for Bitcoin

Since the beginning, Badger has focused on optimizing farming with BTC on Ethereum. Initially, before Convex, Badger worked closely with Yearn, but with the launch of Convex and its rapid dominance, Badge's position has evolved.

Unlike Frax, Badger did not buy its CVX. Instead, Badger is developing a model similar to Convex's to accumulate CRV under control; the bveCVX vault. It offers a similar return to direct locking on Convex, but includes itself in the Badger ecosystem.

For example, the bveCVX scales contribute to Badger's internal boost system that is effective on most vaults. In addition, in each round the BadgerDAO uses the corresponding bveCVX voting power to support the Curve pools supported in Badger, which are essentially pools that involve one or more variants of wBTC.

![bvecvx.png](/img/2022/curve-wars-l2/bvecvx.png)


Rather than acquiring its position in CVX, Badger is able to obtain control of CVX tokens thanks to incentives - so it's a sort of CVX rental. There is also a Curve bveCVX/CVX pool to allow early exit from the vault. There are now almost 1.7M CVX in the vault, so the strategy has proven itself.

### Other DAOs

I focused on two projects that develop two very distinct strategies to accumulate CVX and weigh in on the Curve Wars. As you can see on the graph above, there are many others.

When a protocol develops a substantial position on CVX (say >300K CVX), it benefits directly from its tokens, especially in terms of liquidity. Nevertheless it doesn't stop there: large CVX owners are in a strategic position and will also be courted very soon for different partnerships. 

We can already see the mechanics at work, with the discussion around a potential 4pool (USDC/USDT/FRAX/UST), made possible thanks to the combined influences of Frax, Luna, Redacted and Olympus. The CVX protocols-whales thus become interfaces for the Curve Wars, it remains to be seen who will be able to make them the best offer.
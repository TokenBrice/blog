---
title: "⚔ CRV wars: understanding the race to accumulate power to influence Curve Finance protocol"
description: "A concise guide to tracking the CRV accumulation race by any means possible including vote buying (Bribes) and evaluating the Curve strategies of DeFi protocols"
date: '2021-09-28T01:13:50.191Z'
categories: [🌌 DeFi, 💸 DeFi Pratique]
tags: [DeFi, Ethereum, Finance décentralisée, Curve Finance, CRV, Polygon, Convex, CVX, Votium, vlCVX, veCRV, bribe.crv]
toc: true
tocNum: true
url: crv-wars
---

Since the early days of Curve Finance and the launch of the CRV token, we have been waiting, contemplating and assuming what the CRV war could bring. Now, with the launch of Convex, then Bribe.crv and finally Votium, everything is accelerating: VeCRV votes can now be bought! So let's see how this impacts Curve and DeFi as a whole.

![curve-wars-cover-tokenbrice](/img/2021/crv-wars/curve-wars-cover-tokenbrice.png)

At first glance, the question is quite simple and straightforward:

1. Curve is the largest decentralized DeFi exchange in terms of total value deposited.
2. The CRV token provides access to 1/ a share of the fees collected 2/ **a voting power to influence the issuance of future CRVs.**
3. => Having control over a large CRV voting power makes it **much easier to develop a Curve pool**, since it offers the possibility to vote for large CRV returns on the pool in question.

Nevertheless, as often in DeFi, everything is not so simple and the devil is in the details. To understand the stakes of the CRV war, you need to have **a good understanding of the different tools built on it**. This will allow you to judge the relevance of the strategies deployed by the different projects that seek to influence Curve.

## Convex and the VeCRV separation

Before analyzing the battlefields - i.e. the different tools used in this CRV war - we need to look more deeply at one in particular: Convex. I've already talked about it on this blog, explaining [the flywheel dimension of Convex with the CvxCRV]({{< relref path="/content/posts/2021/defi-flywheel.md" >}}).

The interactions of Convex with Curve go far beyond the CvxCRV, which is only one element.

In fact, **one could describe Convex as a separation between governance and returns on VeCRV** by amplifying each of the elements on a separate token. Let me explain:


### CvxCRV = VeCRV-yield++

CvxCRV corresponds to a VeCRV owned by Convex. They are locked in forever, but the liquidity available on CvxCRV/CRV allows depositors to close out their position.


**In terms of governance, CvxCRV loses all its capabilities** : VeCRV owner can vote on gauges (CRV issue) and governance votes. A CvxCRV owner has no other benefit than the return.

Nevertheless, **the return is amplified compared to a simple possession of VeCRV**:

1. Return in 3pool token - the share of fees collected on Curve - exactly like VeCRV
2. Return in CRV (10% of all CRV farmed by Convex shared between all CvxCRV stakers)
3. Virtually the same yield in CVX
4. Potential airdrops like Ellipsis

CvxCRV corresponds to a simple compromise compared to VeCRV: governance capabilities are lost (-> vlCVX) but in return the performance is greatly amplified and diversified.

### vlCVX = VeCRV-gov++

At the other end of the spectrum, Convex offers another interesting abstraction from Curve. It is its native CVX token. Indeed, **each CVX corresponds to a VeCRV** voting capability (which comes from CvxCRV).

To mobilize it, the depositor must "vote lock" his CVX in vlCVX. They are locked for 16 weeks + 3 days and so provide access to governance capacity. Currently, vlCVX is by far the most economically efficient way to accrue Curve voting capacity:


<table>
  <tr>
   <td>
   </td>
   <td>Price
   </td>
   <td>Voting power
   </td>
   <td>VeCRV-vote/$
   </td>
   <td>Commitment
   </td>
  </tr>
  <tr>
   <td>VeCRV
   </td>
   <td>$2.42
   </td>
   <td>1 veCRV
   </td>
   <td>0.41
   </td>
   <td>4 years
   </td>
  </tr>
  <tr>
   <td>vlCVX
   </td>
   <td>$8.2
   </td>
   <td>12,75 VeCRV
   </td>
   <td>1.55
   </td>
   <td>16 weeks + 3 days
   </td>
  </tr>
</table>


In addition to the increased profitability of CVX to influence Curve, the commitment is also less than on VeCRV. For the comparison table, I assumed a 4-year lock on CRV. The difference is even more in favor of vlCVX for shorter commitments.

{{< notice warning >}}
The vlCVX does have one drawback: after the initial 16 weeks of lock-in, penalties are applied to depositors if the tokens remain inactive for more than 4 weeks.
{{< /notice >}}

If you want to further analyze the returns offered by the delegation of CVX and the associated vote buying, feel free to [read this article (https://medium.com/@portiadog/convex-finance-1cc6c9c1c733) which offers more detailed calculations :

![bribes-rewards](/img/2021/crv-wars/bribes-rewards.png "Estimating the performance of Curve voting delegation via vlCVX")

### Bribes: a not so clean separation

The situation was clear, but it did not remain so for long. Indeed, it should first be noted that vlCVX is not without returns: **vlCVX owners share 6% of all CRVs farmed by Convex, in the form of CvxCRV**.

Furthermore, this is potentially not the only return for which vlCVX owners are eligible. Indeed, **governance capacity can also offer a substantial return via bribe mechanisms** (vote buying).

Different projects offer incentives for voting on the gauge of a given Pool Curve. For example, Alchemix offers rewards in ALCX, its native token, which can be claimed each week by all those who used their VeCRV to vote to increase the CRV allocation of the AlUSD pool.

In the long run, it is not impossible that the initial separation planned by Convex is not the most honest. Currently, the yield on cvxCRV is about 60% while it is only 15% on CVX. Nevertheless, **when you add the bribes into the equation, it is not impossible that the yield on vlCVX is much higher than on cvxCRV.**

## The battlefields

"Bribes" services are an essential part of the Curve governance equation. However, before digging into them, we need to recall the basic path (veCRV) that defines the framework for all its variants.

VeCRV is obtained by locking CRV for up to 4 years. The longer the lock, the closer the VeCRV/CRV ratio is to 1. **The lock gradually depletes over time as does the voting capacity**.

This is why vaults built on VeCRV operate on a 4-year perpetual locking logic: in order to preserve a voting capacity that is always as close to the maximum possible, **they "refresh" the locking frequently.**


![vecrv-ecosystem-tokenbrice](/img/2021/crv-wars/vecrv-ecosystem-tokenbrice.png "Overview of the ecosystem built on veCRV")

### Bribe v0 : direct incentive on pools

Before we talk about bribes, it is worth remembering there is a primitive form that has been available since the early days of Curve: additional incentives (on top of CRVs) for liquidity providers. Synthetix pioneered this with the SNX liquidity mining program on the sUSD pool.

Direct incentives can be combined with bribes, and are even recommended. We will see below how MIM, for example, obtained much more activity by sharing its budget between incentives and bribes (after an initial phase without bribes).


### Bribe.crv by Cronje [with veCRV]

As you can see, the "bribes" are purchases of VeCRV votes. They are paid by the week, generally on Friday (the day the votes are taken into account).

However, just as there are several systems for interacting with VeCRV, there are also several mechanisms for bribes. So we start with the one that was available first: [http://bribe.crv.finance/](http://bribe.crv.finance/)


The basic unit is the VeCRV. Bribe.crv is a simple interface that summarizes the different offers and allows to collect its bribes. Voting is done directly on Curve.

After a somewhat timid start, the service is being used more and more and many projects are now proposing bribes. The returns in the first few weeks have been excellent, it remains to be seen if they will last. For example, I got **about 10% return on my VeCRV (/ current price) in 5 weeks** by voting for the MIM pool and receiving SPELL tokens in bribes.

We'll come back to the results below.

### Votium [with vlCVX]

The alternative available is [Votium](http://votium.app/). Here, the basic unit is the vlCVX, so the two services are not competitors but complementary.

Votium is more recent so the available bribes are more limited. On the other hand, **Votium already controls an impressive voting power: about 8M CVX or more than 102M VeCRV**.

The system is potentially more passive than with bribe.crv since depositors can delegate to Votium who will take care of voting each week for them and collect the corresponding bribes.

Even with an active delegation, a depositor can at any time take back control and vote for a given pool, directly on snapshot (-> no gas cost). The system is therefore more flexible than bribe.crv in this respect

Other services to handle bribes are also in development with a release in the near future. So far the bribe game has focused mainly on CRV, but [Paladin](https://www.paladin.vote/), for example, intends to offer a similar mechanism with other protocols as well.

## Putting it into practice: tactics and results

The conceptual bases are a bit heavy on this subject, but it is essential to understand them. To make it more explicit, let's move on to the practical side with concrete examples.

### The Spell/MIM case

[Abracadabra](http://abracadabra.money/) is a Maker service. Various assets are accepted as collateral, including productive assets such as xSUSHI or cvx3pool.

Just as Maker produces DAI, Abracadabra produces a stablecoin (on the dollar) called MIM. The liquidity available on MIM, as well as the opportunity for returns, is therefore a key factor in the platform's success.

This is why Abracadabra has progressively gone through all forms of direct or indirect bribes on Curve :

1. It started with a SPELL incentive (governance token) on the Curve/MIM pool.
2. When bribe.crv arrived, **a portion of that incentive was reallocated to bribe** - thus distributed to veCRV owners who vote for the MIM gauge.
3. Now, with the arrival of vlCVX, the team is considering reallocating the budget through this.

In a few weeks, the MIM pool has exploded on Curve, at all levels:

* CRV yields were really good in some weeks
* This has attracted liquidity and volume, slightly reducing the yield but increasing the ability to boost the pool
* As a result of this momentum, MIM is now the fifth largest pool curve in terms of volume, with a nice volume/TVL ratio.

![curve-pools](/img/2021/crv-wars/crv-pools.png "Overview of the largest pools on Curve (volume)")

Moreover, the pool is now well balanced and rather dense (> $700M total liquidity).

The example of Abracadabra is extremely instructive, as it demonstrates the relevance of the abstractions built on VeCRV: **without increasing its total budget, Abracadabra has been able to attract much more liquidity than at the time of the simple direct incentive in SPELL.**

You therefore understand that DeFi projects that take advantage of the veCRV, cvxCRV and vlCVX mechanisms have an undeniable advantage (**economic AND political**) over those who have not yet grasped all their subtleties.

### sdveCRV VS cvxCRV

Indeed, **I now consider understanding Curve and the ability to effectively influence its governance to be an essential and required capability in most DeFi projects, especially for stablecoin projects.**

No need to take my word for it though, let's compare in practice two approaches implemented by projects with similar issues: liquidity strategies on cvxCRV (from Convex) and sdveCRV (from StakeDAO) - two abstractions built on veCRV.

Although the situations are similar, there are some important differences:

1. Let's start by recalling that Convex controls more than 30 times the amount of CRV controlled by Stake (102M vs 3M).
2. Furthermore, sdveCRV has serious problems with its peg: 1 sdveCRV ~= 0.5 CRV


![sdvecrv-peg](/img/2021/crv-wars/sdvecrv-peg.png "Échange sdveCRV/CRV")

#### sdveCRV liquidity plan: total misunderstanding and abject failure

So let's move on to the analysis. Initially the liquidity of sdveCRV was against ETH just like Yearn. Since Convex, the Stake team is trying to react to make sdveCRV more attractive.

Nevertheless, the team clearly did not take the time to analyze the situation and rushed into what turned out to be **one of the biggest governance failures ever seen on Curve**

After creating an anemic sdveCRV/CRV pool via the Curve Factory, a vote was taken to add the gauge control (= CRV incentives). Not only was [the vote overwhelmingly rejected](https://dao.curve.fi/vote/ownership/83) but also **the sdveCRV pool is set up in an aberrant and absolutely dangerous way for depositors.**

Indeed, the factor A (amplification parameter) of the pool is [set to 200](https://curve.fi/factory/34) --- a correct value for assets that follow the same peg, but **delusional if one asset is worth twice the other**. 

![sdvecrv-mim-crv-pools](/img/2021/crv-wars/sdvecrv-mim-crv-pools.png "Curve pools (factory) sdvecrv and MIM comparison")

To give you an idea, even the aforementioned absolutely massive MIM pool (7000x the liquidity of the sdveCRV pool) has not yet reached 200 of A factor (119 currently, increasing).

Thus, not only did Stake fail to solve its liquidity problem on sdveCRV, but **such a course of events clearly raises the question of the Stake team's understanding of the intricacies of Curve/Convex**.

To get sdveCRV back to peg and develop its liquidity, they will need a lot of effort, in order: 

* Review the pool parameters
* Direct incentives in SDT on the pool?
* Bribes in SDT on the pool?

Once these steps are completed, the team would then have a chance to get the CRV gauge on this pool, but not before. So the current situation looks like a costly dead end: **no way out unless the TDS board is heated (even more)**.

#### cvxCRV liquidity plan: immediate take-off

On the contrary, the liquidity plan on cvxCRV demonstrates how effective the process can be. Initially (and still today), the main pool for cvxCRV is on Sushiswap, against CRV.

This situation does not really make sense: **Sushi is far from optimal for optimizing liquidity across assets that follow the same peg**. So when Curve launched factory pools (V2), the [cvxCRV/CRV pool](https://curve.fi/factory/22) was one of the first to emerge.

(Note here the A Factor at 50 - while cvxCRV holds its peg much better than sdveCRV...)

![cvxcrv-pool](/img/2021/crv-wars/cvxcrv-pool.png "Pool (factory) cvxCRV/CRV")

Without any incentive from Convex or Curve, the pool has already seen significant volume flow through DEX aggregators like Paraswap. Soon, there was a vote to add the CRV gauge which passed - and this pool is now farmable directly through Convex.

The pool remains slightly unbalanced (there is so much to do with CRVs, which are becoming increasingly rare...) but it already brings a competitive alternative to the SLP cvxCRV/CRV pool with still a fraction of its liquidity. 

## Conclusion

I hope this article has helped you grasp the intricacies of the extended veCRV ecosystem and their implications for the CRV battle. 

Before concluding, I would like to remind you that as usual the alpha is in the dips. If you have understood this article, feel free to export the liquidity strategy analysis to other projects: I am sure it will be instructive!

I tell you often, but it will never be enough: not only Curve is the most important DEX in DeFi but it is also **the most advanced protocol in terms of governance and tokenomics by far compared to anything else**. Even if you have no interest in Curve/Convex, it's essential to understand these protocols in order to properly consider what's going on in DeFi... Hopefully this article will help you!
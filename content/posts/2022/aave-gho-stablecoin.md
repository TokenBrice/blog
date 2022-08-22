---
title: "Can Aave's GHO stablecoin help the protocol further grow and overtake MakerDAO and DAI?"
description: "Looking at GHO's design and anticipating its key challenges to grow as well as the value it can deliver to the Aave DAO."
date: '2022-08-22T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Understanding]
tags: [DeFi, Ethereum, Decentralized Finance, Stablecoins, Stable Assets, Money Markets, Aave, GHO, Interest Rate]
toc: true
tocNum: true
url: aave-gho-stablecoin
---

A few weeks ago, the concept for the GHO stablecoin was introduced on the Aave Governance Forum and triggered a wave of excitement across DeFi. Indeed, the idea of a decentralized, collateral-backed stablecoin, pegged to USD and native to the Aave DAO makes a lot of sense as a next step for the protocol.

In this article, we'll examine the design introduced before considering how the Aave DAO and team could bring it to market and turn it into a stablecoin potentially as significant as DAI. Of course, the information is still scarce, so the second part of the article will be primarily extrapolations stemming from my DeFi experience.

![aave-gho-stablecoin-cover](/img/2022/aave-gho-stablecoin/aave-gho-stablecoin-cover.png)

## Introduction to GHO, Aave's native stablecoin

Since its early days, one of Aave's main challenges has been attracting sufficient stablecoin deposits since it's a preferred choice for most borrowers. Thus, creating a stablecoin native to the DAO is a natural next step and should also allow lowering costs for borrowers. Since this stablecoin is minted, there is no need to pay the APR of the depositors on the other side.

So let's dive into the main characteristics of GHO as presented on the governance forum.


### An overcollateralized USD-pegged stablecoin

GHO will be an overcollateralized stablecoin, minted using aTokens as collateral. So in a sense, it's similar to MakerDAO but slightly more efficient since all collateral will be productive assets generating some interest (aTokens) – depending on their borrowing demand.

Regarding the naming, it's also interesting to see Aave not including "USD" in the name. Considering how aggressive the US regulators can be, it's probably a net benefit from a legal perspective. Still, it doesn't seem to be the only driver of the decision, as Aave's founder Stani hinted at a potential peg swap further down the line:


> The reference to a currency has limitations over long term, potentially you might want to swap the peg from one underlying asset to another (for various reasons) or track something else and being bound to a USD in the ticker would be a limiting factor. On top of that everyone is doing that already which makes it a bit repetitive and restrictive from the messaging perspective. DAI follows the same path actually and has been helpful to build a narrative over the years.
> - Stani on [Aave's GHO introduction post](https://governance.aave.com/t/introducing-gho/8730/27)


### Interest model and stkAAVE discount

The interest rate model for GHO is currently its most underwhelming component, as the initial post envisioned an interest rate directly determined by the Aave DAO, just like how it works on Maker. However, that would be inefficient and add unnecessary bloat to the governance. 

The community feedback will dictate where it goes. Still, I genuinely hope for Aave that the final call lands on a model where the interest rate is algorithmically determined by market conditions, just like with other tokens on Aave where the supply/demand on the pool dictates the interest rate.

If the Aave community feels like it is a necessity to involve the DAO in determining the interest rate — an absurdity in my book since a DAO is absolutely unfit to manage the operational parameters of a system — then a hybrid model could be envisioned with a fixed base rate voted on by the DAO, and modulated within a range depending on the market condition.

Indeed, having the interest rate evolve dynamically can help protect GHO's peg by deterring against massive minting events, just like [how the baseRate works on Liquity](https://docs.liquity.org/faq/lusd-redemptions#how-is-the-baserate-calculated) to protect LUSD from de-pegging downward. Initially, at 0.5%, the fee rises when demand surges to progressively decays back to 0.5% as the demand stabilizes.

The post also mentions a discount for GHO borrowers staking AAVE tokens, creating further synergies. Finally, 100% of the interest rates paid by depositors will go to the Aave DAO (vs. a Reserve Factor in the ~10% range for most other tokens), meaning that if GHO grows to a significant market cap, it could turn into a goldmine for the DAO. **With a market cap similar's to DAI, and an average interest rate of 3.5% (high-end), AaveDAO would earn close to $150K daily from GHO's interest rate.**

Here are some quick napkin maths with different GHO market cap and interest rate assumptions to give you an idea:


<table>
  <tr>
   <td>GHO Marketcap
   </td>
   <td>Avg. Interest Rate
   </td>
   <td>DAO Yearly Earning
   </td>
   <td>DAO Daily Earning
   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$1.5B (FRAX market cap)</p>

   </td>
   <td><p style="text-align: center">
1%</p>

   </td>
   <td><p style="text-align: center">
$15,000,000.00</p>

   </td>
   <td><p style="text-align: center">
$41,095.89</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$6.6B (DAI market cap) </p>

   </td>
   <td><p style="text-align: center">
1%</p>

   </td>
   <td><p style="text-align: center">
$66,000,000.00</p>

   </td>
   <td><p style="text-align: center">
$180,821.92</p>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$52B (USDC market cap)</p>

   </td>
   <td><p style="text-align: center">
1%</p>

   </td>
   <td><p style="text-align: center">
$520,000,000.00</p>

   </td>
   <td><p style="text-align: center">
$1,424,657.53</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$1.5B</p>

   </td>
   <td><p style="text-align: center">
3.50%</p>

   </td>
   <td><p style="text-align: center">
$52,500,000.00</p>

   </td>
   <td><p style="text-align: center">
$143,835.62</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$6.6B</p>

   </td>
   <td><p style="text-align: center">
3.50%</p>

   </td>
   <td><p style="text-align: center">
$231,000,000.00</p>

   </td>
   <td><p style="text-align: center">
$632,876.71</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$52B</p>

   </td>
   <td><p style="text-align: center">
3.50%</p>

   </td>
   <td><p style="text-align: center">
$1,820,000,000.00</p>

   </td>
   <td><p style="text-align: center">
$4,986,301.37</p>

   </td>
  </tr>
</table>


Table references:

1. GHO Marketcap: 1.5B = FRAX's current supply, 6.6B is DAI's, and 52B is USDC — one can dream.
2. GHO Average Interest Rate: 1% would be highly competitive, 3.5% in the higher-end of the usual rates.


### Facilitators and RWA

GHO's design envisions "Facilitators," onboarded by Aave's governance, that would be able to mint GHO. The first facilitator would be the Aave protocol itself, but others will follow suit, be they protocols or entities. This part is exciting, as it widely opens up GHO's design space. Following the release, we could see other protocols applying to become facilitators and building on top of Aave and GHO.


![gho-facilitators](/img/2022/aave-gho-stablecoin/gho-facilitators.png)


There are also explicit mentions of undercollateralized positions based on credentials such as a credit score. Each facilitator will have a maximal GHO minting capacity determined by the DAO.


### "Decentralization" and absence of censorship resistance

GHO is presented as a decentralized stablecoin by the Aave team, with even some mentions of censorship resistance. However, it's never directly associated with GHO:

> The usage of stablecoins will only continue to grow as cryptoassets become further integrated with a user base that is less crypto-native. Decentralized stablecoins provide censorship-resistant fiat-denominated currency on the blockchain. Introducing, GHO, a decentralized multi-collateral stablecoin that is fully backed and native to the Aave Protocol.

Unless I've misunderstood the design, GHO will be **as "decentralized" as DAI and have weak censorship resistance** because of its collateral composition. Indeed, assuming that all aTokens that can be currently used as collateral to borrow on Aave will also be used to borrow GHO, GHO's collateral composition will be mostly made of censorable tokens such as USDC:


![aave-collateral](/img/2022/aave-gho-stablecoin/aave-collateral.png)


Source: [DeFiLlama](https://defillama.com/protocol/aave-v2)

Indeed excluding stETH used as collateral to leverage the ETH staking yield (borrowing ETH), USDC is the top collateral used on Aave, with another trusted token (wBTC) not far behind. **Still, the collateral composition would be much better than DAI,** which is >50% backed by pure USDC. 

![dai-collateral](/img/2022/aave-gho-stablecoin/dai-collateral.png "Over 75% of the tokens backing DAI are censorable")

Another ~25% of the backing comes from other trust-required collateral or reflexive liquity providing positions (such as DAI/USDC LP used as collateral to mint DAI).

For more information on the envisioned design for GHO, feel free to read [the governance forum post](https://governance.aave.com/t/introducing-gho/8730) and the replies.


## GHO to market: What could Aave with GHO look like?

Now that the stage is set regarding GHO, we can move into a more speculative territory and consider how the GHO release could unfold in practice.

Indeed, the interaction between the Aave protocol and GHO is quite exciting to consider: while the initial post mention Aave x GHO, as well as the enablement of the eMode (enabling significant leverage on selected pairs such as USDC/DAI) on GHO, it quite scarce in details, so let me share instead how I envision it.

aGHO would be fascinating collateral on Aave, but it could also create significant reflexive risks if allowed to borrow GHO. Thus, **I expect aGHO to be blocked from minting GHO** to prevent reflexive backing like we're currently seeing on DAI.

Still, it would allow for exciting stablecoin arbitrage loops, such as aUSDC > Mint GHO > aGHO > Borrow another stablecoin. With the eMode, this would make Aave & GHO a very effective protocol for stablecoin arbitrage. Besides, the GHO interest rate would become a kind of "base stablecoin interest rate" and maybe help keep the interest rate of other stablecoins like USDC in check.


### GHO's Liquidity Strategy

Another critical and essential part of any stablecoin's design is its liquidity strategy. Since CRV, CVX, and BAL are accepted as collateral on Aave, there could be exciting things done with the CRV, CVX, and BAL accumulated by the treasury, thanks to the Reserve Factor. Locking them into their native protocols would enable the Aave DAO to direct incentives to GHO-related pools.


![aaveDAO-treasury](/img/2022/aave-gho-stablecoin/aaveDAO-treasury.png "Current state of Aave's treasury with ~615K CRV")
Source: [Aave’s Treasury Report](https://governance.aave.com/t/aave-treasury-report/5575/37) (July 2022)

Just like Frax is currently pivoting away from USDT and DAI and trying to establish the Frax Basepool (FRAX/USDC) as a pairing currency on Curve for other stablecoins, we could envision a similar move from Aave. Moreover, many projects currently exposed to USDC and DAI are looking to diversify their liquidity away from them. GHO might arrive with perfect timing to enable DeFi to be less reliant on USDC.

However, while Frax controls sizeable governance and gauge-voting power in the Curve Wars, this is not the case for the Aave DAO. Current treasury CRV/CVX balances will clearly be insufficient to incentivize pools to grow into the billion dollar range, so it could drive the AaveDAO to look into acquiring more liquidity-incentive-driver tokens. With the significant revenues that the DAO will collect from GHO's interest rate, it should have sufficient means to support appropriate liquidity, whatever GHO's market cap ends up being.

Finally, Aave has been historically close to Balancer, with the 80% AAVE / 20% wETH Balancer Pool used in the Safety Module since the transition to the AAVE token. Thus we could expect an exciting play for GHO on Balancer. Yet when it comes to stablecoin, Curve remains both the king and king-maker: I don't see how Aave could sufficiently grow GHO's liquidity without getting involved one way or another in [the CRV wars]({{< relref path="/content/posts/2021/crv-wars.md" >}}).

On top of the base protocol incentives (such as the dynamic or DAO-governed borrowing interest rate) and liquidation mechanism, the liquidity strategy is probably one of the most crucial element for a stablecoin since it also has an impact on how well the peg is held.


## Parting Words 

I hope this article helped you better understand what is at stake in the stablecoin wars. The end of the year will be interesting, with the GHO release approaching and Curve's stablecoin, also overcollateralized, which was hinted to release before the end of this year. The multiplication of stablecoin is a natural next step for DeFi, as most established protocols see their design converge:



* Frax started as a stablecoin only, now has FraxSwap and soon FraxLend.
* Aave started as a money market, soon with its own native stablecoin.
* Curve started as a DEX, but the addition of its own stablecoin soon could enable efficient borrowing for liquidity providers.

At the end of the day, as shown with my napkin maths earlier, the main reason for a protocol to create its stablecoin is quite apparent: it's where there is the most money to be made, as well as massive demand and product/market fit.


{{< notice note >}}
The "artist" of the cover image for this article is an impressive (and slightly scary) AI called [Midjourney](https://www.midjourney.com/). It was given the following prompt: `a cute and friendly glowing ghost minting the coins of his own currency in a cyberpunk environement, 4k,cartoon,fully details,high contracts,unreal engine. --ar 19:10`
{{< /notice >}}

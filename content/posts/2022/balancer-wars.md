---
title: "Liquity-driver token races beyond Curve: a look at the Balancer Wars"
description: "Cornering the lay of the land of the Balancer Wars: we look at the DEX specificities to anticipate what's next for the BAL races."
date: '2022-11-24T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Understanding]
tags: [DeFi, Ethereum, Decentralized Finance, Balancer Finance, BAL, Polygon, Aura Finance, AURA, PowerPool, CVP, veBAL, vlAURA, Hidden Hand, Warden, Vote Bribing, Liquidity Driver Tokens]
toc: true
tocNum: false
url: balancer-wars
---

Liquidity-driver tokens, as I call them, are an emergent and fascinating construction. Simply put, these tokens enable you to direct incentives (CRV, BAL, etc.) to the liquidity pool of your choice. To do so, you must usually own and lock the corresponding token (veCRV, veBAL, etc.) within their governance contract, ensuring continuous commitment from participating projects. 

Thus, the liquidity-driver tokens quickly became highly sought after by DAOs with constant and usually growing liquidity needs. It led to what we call “races” (or "wars"): a term that refers to the various strategies projects harness to constantly increase their veTokens stash, ideally faster than the other participants of the races, to grow a competitive advantage.

![balancer-wars-cover](/img/2022/balancer-wars/balancer-wars-cover.png)

I’ve covered the CRV tokenomics, the pioneer of the veToken model, and their consequences in this blog extensively:

1. [⚔ CRV wars: understanding the race to accumulate power to influence Curve Finance protocol]({{< relref path="/content/posts/2021/crv-wars.md" >}})
2. [⚔ Advanced CRV warfare: analysis of protocols built on top of Curve and Convex]({{< relref path="/content/posts/2022/crv-wars-l2.md" >}})

## veTokenomics, beyond the Curve ecosystem

While Curve is fascinating to study, as it’s the veCRV pioneer and still the most mature and dense implementation of ve tokenomics to date, there are now many other race instances with their twists worth looking at.

Indeed, the veCRV tokenomics is more than two years old, and many other projects have launched or revamped their tokenomics since, drawing inspiration from Curve’s model. Without being exhaustive, here are the other “races” I follow the most closely:

1. Solidly pioneered the “ve(3,3)” model (attempting to build and improve on the base ve model) on Fantom in February 2022, quickly attracting billions of TVL before [failing dramatically because of very poor execution](https://hackmd.io/@c30/BJ2PNCwgs).
2. [Velodrome](https://app.velodrome.finance/), a fork of Solidly fixing its critical issues, quickly found its place on Optimism after launching in June 2022.
3. [Balancer](https://balancer.finance/) — a historical alternative to Curve and Uniswap, a chain agnostic DEX packing interesting innovations, [recently switched to a vemodel in March 2022.](https://medium.com/balancer-protocol/vebal-is-live-aeda1ae13e20)
4. [Solidly](https://twitter.com/SolidlyETH), again. Indeed, while the first project failed, the community gathered to take over and is about to re-launch Solidly, this time on mainnet, making it much more interesting.

I am myself a liquidity-driver addict, as I was sharing recently on Twitter:

All projects have constant liquidity needs; addressing them sustainably is highly valuable. Indeed, the value of liquidity-driver tokens exceeds what DAOs/projects can draw from them: $1 worth of vote-bribing can move >$1 worth of incentives. Individual participants can also gain a lot by being able to position themselves early in a relevant race.

So with the stage set, let’s dive into today’s matter: Balancer, their BAL races, and the “BAL-Layer-2” infrastructure that emerged on top of it, just like it happened with Curve.

## Mapping the Balancer Trinity

![balancer-trinity](/img/2022/balancer-wars/balancer-trinity.png)

While we documented Curve, we watched the ecosystem grow together on this blog. With [Balancer](https://balancer.finance/), I’m covering it extensively for the first time and already looking at a mature ecosystem. Balancer already has “its Convex,” called [Aura Finance](https://aura.finance/). It already controls over 25% of the veBAL (vs >50% of veCRV for Convex). 

However, the Balancer base infrastructure calls for a third component: an automation network necessary to enable the most advanced type of pools. At this stage, it’s still unclear who is leading this race, so I’ve used one of their most prominent participants – [PowerPool](https://powerpool.finance/) and its PowerAgents network — to play the part.

For those familiar with UniswapV3 liquidity provisioning, one could say PowerAgents play a role similar to [Gelato](https://www.gelato.network/): it handles the automation of operations required to enable specific use cases, such as rewards harvesting and auto-compounding.

## What makes Balancer different?

Along with Uniswap and Curve, Balancer has been one of the longest-standing DEX with significant traction today. Indeed, looking at the DEX market from a global perspective, Balancer is scoring fifth place with about 3% of the total volume processed:

![defillama-dex-overview](/img/2022/balancer-wars/dex-overview.png)

_Overview of observed trading volume on main decentralized exchanges from [DeFiLlama](https://defillama.com/dexs)_

{{< notice note >}}
Balancer is only launched on mainnet, Polygon, and Arbitrum – meaning fewer chains than most of the other top 5 DEXes, something to keep in mind in a global-level comparison.
{{< /notice >}}

Balancer's first version launched in March 2020, and many iterations have been shipped since then, improving the BAL token model and liquidity structure. However, Balancer had **specificities since V1** that are probably key in explaining why it’s still standing today. I’ll focus on the most emblematic, Balancer-specific ones:

### Pool supporting 2 to 8 assets

Balancer is still, to this day, one of the only DEX offering such a wide range of pool structures. Indeed, a Balancer pool can be made of **any number ranging from 2 to 8 assets**, while most other DEX only support pairs, so two assets at once.

It enables novel types of pools, such as: 

* 3 assets pools, such as the wBTC/USDC/wETH pool similar to Curve’s TriCrypto pool, or to diversify the pairing of a given token, like the OHM/ETH/DAI pool.
* Or even 7-8 asset pools that start acting as token indexes as much as liquidity pools, such as the YFI/wBTC/COMP/wETH/UNI/CHZ/LINK pool.

### Arbitrary pool weighting

On top of the flexible support in terms of the number of tokens, **pool weighting does not need to be even across tokens** and can be extensively customized.

This enables unbalanced pool structures that are very useful in certain situations:

* For instance, the OHM/DAI/ETH pool mentioned above is **50%OHM, 25%DAI, and 25%wETH** – enabling the maximization of the OHM liquidity available against both DAI and ETH at the same time.
* Another frequently used distribution is the **98/2**, particularly fitting to start building the liquidity of a newly released token with minimal IL risk (since 98% of the pool is composed of the safe pairing asset, like a stable or ETH)
* Finally, the **80% Token / 20% pairing asset** such as 80% BAL / 20% wETH is also a highly sought-after liquidity distribution, as it enables token holders to partake in liquidity providing activities with minimized IL risks if the token was to appreciate.

### Dynamic pool weighting

Finally, Balancer can adjust the pool weighting distribution as needed through a specific type of pool called a [Liquidity Boostraping Pool (LBP)](https://docs.balancer.fi/products/balancer-pools/liquidity-bootstrapping-pools-lbps). Such pools are particularly fitting for launching tokens & building their liquidity at the same time, as they enable the streamlined go-to-market token flow. For instance:

1. A given project wants to quickstart its token liquidity — the associated DAO controls a significant amount of the token, but usually none of the potential pairing asset (usually ETH or stablecoin)
2. So they start with a 98% USDC / 2% Token pool, enabling them to provide liquidity with minimal pairing token requirements.
3. The pool acts as a token initiation event and price discovery mechanism at the same time. The token starts at a given price, which decreases as time goes on if no one purchases the token.

![balancer-trinity](/img/2022/balancer-wars/LBP.png "Evolution of the price of a token during an LBP if there is no purchase")

LBPs are designed to enable users interested in the project to purchase tokens fairly over a given period, protecting them against the usual attacks seen on more classical tokens launches (such as MEV bots sniping initial supply).

It enables the user-DAO to accumulate the pairing token and first price discovery of the DAO’s token, making it easy to jump to the next step: quickstart the token liquidity with protocol-owned seeding.

### Specificities of Balancer’s veModel

Balancer also has implemented its twist on their Curve’s inspired locking mechanism. Here, instead of locking the token directly (CRV ⇒ veCRV), governance participants must **lock an LP token** corresponding to the Balancer **80% BAL / 20% wETH** pool.

As said above, this liquidity distribution limits IL risks for depositors on a BAL upside. Thanks to this twist, Balancer can capture significant liquidity reserves through the normal operations of its governance participation mechanism.

Finally, as of late, it seems like Balancer is focusing on interest-bearing tokens and developing new use cases to cater to them. For instance, [BIP#19](https://medium.com/balancer-protocol/vebal-pt-2-bribing-and-bip19s-free-bribes-b2f8334eba14) introduces “free bribes” for pools involving interest-bearing assets: the yield produced by the pool asset is recycled as a bribe to sustain its liquidity.

## Lay of the land of the Balancer Wars

Like Curve, Balancer has one dominant player of its race which developed a protocol optimized for synergy with Balancer: Aura. Aura is one of many services available in the Balancer-functional-L2 ecosystem, but a vastly dominant one with ~25% of all veBAL under the protocol control.

Aura offers efficient farming to holders of Balancer LP tokens, with BAL rewards boosted thanks to the protocol's sizeable veBAL stash and additional AURA incentives. In that regard, it is the same thing as Convex to Curve.

![defiwars-balancer](/img/2022/balancer-wars/defiwars-balancer.png)

_Overview of the veBAL liquid wrappers — [courtesy of defiwars.xyz](https://www.defiwars.xyz/wars/balancer)_

### Protocols with veBAL/vlAURA positions

On top of the protocols working on liquid-wrapper for veBAL like Aura, some other DAOs and projects built sizeable veBAL/vlAURA positions to grow and sustain their liquidity, like Frax is doing on Curve.

### Balancer Bribe Markets

Many bribe markets are enabling the purchase of veBAL or vlAURA votes; here are the main ones:

1. [Hidden Hand — Aura](https://hiddenhand.finance/aura) and [Hidden Hand – Balancer](https://hiddenhand.finance/balancer)
2. [Paladin’s Warden Balancer Quest](https://app.warden.vote/quest/)
3. [And StakeDAO BAL Votemarket](https://votemarket.stakedao.org/), a sort of bribing marketplace aggregator

To follow the Balancer wars, make sure to harness the amazing data computed by the Llama Airforce:

![llama-airforce-aura](/img/2022/balancer-wars/llama-airforce-aura.png)

As seen on the graph, the bribing markets took off quickly before finding an equilibrium at around **$0.06 per AURA vote, translating into 1.50x bribes efficiency**: $1 spent bribing the vote results in $1.50 worth of BAL emission added to the targeted pool over the epoch.

This figure is lower on the Curve races, around 1.25x for the Convex vlCVX bribing. It’s logical since Curve races are much older. 

## What’s next for Balancer?

To complement the traction achieved thanks to the tokenomics revamp and switch to veBAL, several technical developments have been shipped/are coming to the Balancer DEX and should help further cement its position.

### Boosted Pools

The first one is the boosted pool, which is already live. They optimize the yields produced by liquidity providers by harnessing additional IL-free yield sources with tokens not needed to stomach the liquidity-providing activity. The bb-a-USD, Balancer’s 3pool equivalent, is the top Boosted Pool currently, but more are coming, including a LUSD-based one: LUCY.

[Introduction to PowerPool's LUCY pool and what it brings to $LUSD](https://www.liquity.org/blog/introduction-to-powerpool-lucy-pool-and-what-it-brings-to-lusd)

### Aave x Balancer

Aave and Balancer have historic ties, with Aave Safety Module harnessing Balancer V1, and Aave even shipping a V2 market a few years ago to leverage Balancer LP tokens.

Further collaborations are anticipated, as [Aave acquired BAL tokens recently](https://app.aave.com/governance/proposal/87/) and will face dramatically increased liquidity needs with the GHO release.


### Balancer: home of the LSDs?

Finally, looking at the current top pool TVL-wise on Balancer, a clear fit is emerging: liquid staked derivatives, such as Rocket Pool’s rETH or Lido’s stETH. Both have sizeable pools properly incentivized on Balancer mainnet. 

Lido’s wstETH/wETH pool even flipped the 80BAL/20wETH pool and became the top one of the DEX with $200M TVL. Similarly, stMATIC/wMATIC is the top Balancer/Polygon pool, followed by MATICX/wMATIC, featuring another liquid MATIC staking derivative. On Arbitrum, the third and last chain where Balancer is live, here again, the wstETH/wETH pool tops the chart. 


## Conclusion

If you’d like to take part in the Balancer Wars, make sure to harness all the great resources available:

1. [Llama Airforce](https://llama.airforce/#/bribes/overview/hh/aura-bal)
2. [DeFiwars - Balancer](https://www.defiwars.xyz/wars/balancer)
3. [Dune Analytics](https://dune.com/balancerlabs/balancer-pools)

While I hope this article provided you with actionable insights regarding liquidity-driver tokens, I wanted to add another layer: it seems like a **subcategory** of liquidity-driver is emerging – **the lending liquidity-driver token**. 

They work very similarly, but instead of enabling their holders to direct incentives to liquidity pools, they allow them to **direct incentives to select lending markets**. So, in the end, they accomplish a different goal through a similar mean: controlling a lot of these lending-liquidity-driver tokens, like [Euler Finance’s](https://euler.finance/) EUL, allows for sustaining deep liquidity in lending markets.

It’s probably worth looking at; I’ve been anticipating the arrival of ve and ve(3,3) based tokenomics to money markets for a while.


🙏 Thanks to [Disiaque](https://twitter.com/disiaque_eth) for his help proofreading this article. 
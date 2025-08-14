---
title: "ve(3,3), the logical next step after veCRV?"
description: "A deeper look at the Solidly and then later Velodrome model for understanding their improvement on the base Curve / veCRV template."
date: '2023-04-28T01:13:50.191Z'
categories: [DeFi, Understanding]
tags: [DeFi, Ethereum, Decentralized Finance, Curve Finance, veCRV, Velodrome, veVELO, Aerodrome, veAERO]
toc: true
tocNum: false
url: solidly-velodrome-fork
image: img/2023/solidly-velodrome-template/cover.png
---

Solidly/Velodrome forks have been popping up like mushrooms, especially across the popular layer 2 like Arbitrum or zkSync. Solidly is now the top #3 forked protocol in DeFi and one of the rare cases where the forks (such as Velodrome) are the market leaders. At first glance, it could seem like just another fork hype train, like when we had the Uni/Sushi fork season, Olympus fork season, etc.

And indeed, it’s overblown: an absurd amount of such DEXes are launching weekly, and 95% of them won’t be relevant six months from now. However, like with most of such hype trains, there is deep down, below the fluff, an actual fundamental innovation in how decentralized exchanges are designed that is worth looking into.

So this article will dive deep into the Solidly and Velodrome models to understand why they became a standard fork template. With that said, we’ll be in an excellent position to ponder the next steps for these DEXes and what this market might look like in a few months.

Let’s get right to it!


{{< notice note >}}
This article assumes a minimal understanding of decentralized finance and a thorough understanding of the veCRV model. If you need a refresher, check: [⚔ CRV Wars: understanding the race to accumulate power to influence Curve Finance protocol](https://tokenbrice.xyz/content/posts/2021/crv-wars.md")
{{< /notice >}}

## Introduction to ve(3,3) DEXes

Before we dive into how Solidly built on top and tried to improve the veCRV model, let’s take a step back to consider the scope first.


### AMM Structure VS Incentivization Layer

Indeed, to grasp the ve(3,3) DEXes story, we need to distinguish between two layers that are equally important for a decentralized exchange:



1. **The liquidity structure layer**: the various AMM models used to sustain liquidity, such as UNIv2’s x\*y=k or Curve’s stableswap.
2. **The incentivization layer**: fees + all other incentives directed to the liquidity provider, including token emissions (such as in the CRV model).

While at the end of the day, 1 – the liquidity structure – is the heart of the game, the second layer – incentives – is crucial in attracting and sustaining sufficient liquidity.

Curve innovated on both. While the models we'll discuss today harnessed it, they **focus entirely on improving the incentivization layer**. Indeed at the current stage, most of ve(3,3) DEXes harnessing the Solidly or Velodrome model only offer two well-known liquidity structure types: x\*y=k & stableswap.

{{< notice info >}}
Depending on the DEXes, those two liquidity models are called correlated/volatile or stable/volatile.
{{< /notice >}}

So, let’s talk about what was so interesting about Andre’s Cronje original Solidly and what insights we can draw from its failure.


## Andre Cronje’s Solidly Innovations

Introduced in early 2022 on [Cronje’s medium](https://andrecronje.medium.com/ve-3-3-44466eaa088b), the crucial part of Solidly’s vision was a significant improvement in the utility for lockers. On Curve, lockers are committed for four years with non-transferable vote-escrowed tokens. While it’s great for the long-term incentives alignment of all the participants of the Curve ecosystem, it also creates a sizable barrier to entry.

Thus came ve(3,3), with at its core **the veNFT**. While veCRV are illiquid, veSOLID positions are represented by the veNFT, enabling their transfer or OTC sale/purchase. It helps make locking less scary. To further incentivize it, Cronje introduced “**anti-dilutive rebases**”, a concept drawn from Ampleforth/Olympus.

The idea here is simple: since the Curve/Solidly DEX model emits tokens weekly to liquidity providers, vetokens holders are constantly diluted. They must keep increasing their position even to maintain their current vote share. To compensate for this, veSOLID holders receive a weekly rebase proportional to the weekly emissions under the Solidly model. This allows them to maintain their voting share even if no new tokens are locked.

Apart from these changes, Solidly inherited most of the Curve model, including **the LP boost** feature, enabling vetokens holders to earn boosted yields on their liquidity position. This feature has real consequences since it pretty much “calls for a Convex.” Indeed, the logical conclusion of such a feature is one/a few actors seizing significant amounts of vetokens and providing their LP boost to depositors for a fee.

The presence/absence of this feature is the critical difference between the Solidly and Velodrome models, so we’ll touch back on it later.

Finally, there one last critical twist to the voter incentives model. On Curve, LP get half of the trading fees collected + CRV emissions, while voters have no exposure to the fees of the pool they are voting on. It can lead to situation where voters are voting for pools just for the bribes, even if the pool provides no volume to the exchange.

On Solidly, the LPs are only rewarded with SOLID emission, and the LP fees are redirected to the voters of the pool. Thus, as a veSOLID holder, to optimize your earnings, you are incentivized to consider the volume on the pool you are voting on, and not just the bribes. This leads to a better alignment of the incentives of the main participants of the protocol (swapper, liquidity provider, veHolder)

Solidly also innovated on the launch strategy, with **an airdrop targeted at protocols**, depending on their onchain activity on Fantom, where Solidly was. Together, all those innovations and the hype led to a massive amount of liquidity quickly attracted to the exchange.

But Solidly’s initial implementation had a few key weaknesses, including an aggressively steep decline in emissions and fully permissionless gauge creation that allowed any pools to receive SOLID rewards. It was gamable, so it was gamed. Soon, tokens were created for the sole purpose of farming SOLID, and the price quickly spiraled, along with the TVL.

![cover-image](img/2023/solidly-velodrome-template/solidly-tvl.png)

The TVL disappeared as quickly as it came, and Solidly became a part of history for most. But those who followed the events closely knew that Solidly’s failure did not come from a weakness in the ve(3,3) model but more of **an overlooked detail of its implementation**, meaning that while Solidly was no more, ve(3,3) would likely resurface. And it did, a few months later, on another chain made by another team: enter Velodrome.


## Velodrome’s refinements to the Solidly model

[Velodrome](https://www.defiscan.info/protocols/velodrome-v2/optimism) harnessed the Solidly model and fixed the issue with emissions by implementing a **whitelist for gauges**, helping to avoid the situation where rewards are allocated to made-up tokens, as seen on Solidly. 

Velodrome went far beyond a mere fork, though, and implemented further improvements; among them were a more sustainable emissions model and **removing the LP boost feature**, meaning there is no preferential treatment for veVELO holders in terms of yield. Velodrome also streamlines the experience for first-time LPs who might be confused with the yield range you see on DEXes with LP boost implemented.

Beyond the technical features, a large part of Velodrome’s success is due to the **team’s execution and care for the business development strategies**, an essential part of the ve(3,3) model. Built on Optimism, Velodrome found its PMF as the chain liquidity layer. Thanks to its model, sustaining liquidity on Velodrome is much more cost-effective for projects than, say, on Uniswap.

Like Solidly, **Velodrome airdropped several protocols with a veVELO NFT,** no strings attached, which helped immensely to attract the initial voting and bribing activity. The protocol found a good fit, mostly with other protocols emitting stablecoins or ETH liquid stake derivatives:

![defiwars-velodrome](img/2023/solidly-velodrome-template/defiwars-velodrome.png "DeFiwars.xyz - veVELO ownership overview")


It’s been almost a year, and the activity has sustained, thanks to careful and progressive adjustments of the **OP incentives allocated on the protocol**, known as [Tour de OP](https://medium.com/@VelodromeFi/tour-de-op-updates-631268181baa). Most of them are used to incentivize two behaviors essential to sustain the flywheel:

1. Bribes from protocols, incentivized by OP bribes matching.
2. Locking of veVELO, incentivized by an OP lock bonus.

The bribe matching is further increased for projects which lock veVELO or deploy sizeable amounts of protocol-owned liquidity to the exchange, helping further amplify the reinforcing effect: those who want to build liquidity sustained over the long term on Velodrome have been given solid reasons to buy VELO, lock and vote, bribe, and supply POL, **ideally all at once**.

It leads to Velodrome topping the protocols TVL charts on Optimism and processing about 30% of the total volume of the chain vs 50% for Uniswap, which has roughly ¼ of Velodrome’s TVL.

![optimism-DEX-volume](img/2023/solidly-velodrome-template/optimism-volume.png "Volume on DEXes on Optimism, from DeFiLlama")

So, why such a spread between the both? Simple: Uniswap's Volume/TVL ratio is ~9x above Velodrome right now because the liquidity on Uniswap is much more concentrated and thus more efficient. But it’s about to change as Velodrome V2 is arriving soon.


### Introducing Velodrome V2

While Uniswap had a headstart with concentrated liquidity, it will change rapidly. The v3 license [expired on April 1st 2023](https://docs.uniswap.org/contracts/v3/guides/governance/liscense-modifications), meaning the model is now much easier to re-implement. Many DEXes, including Solidly/Velodrome forks, intend to harness this. Still, to keep this article focused, we’ll only cover what is announced for Velodrome V2, expected in the next few weeks/months.

Indeed, Velodrome V2 will not just mark **the introduction of UNI-v3 style of LP on the DEX** but also significant UX/UI improvements, a relayer to ease the management of veNFT, artwork for the veNFT, and much more. Check the [V2 announcement article](https://medium.com/@VelodromeFi/velodrome-the-road-ah-43488531bb0e) for details.

## Conclusion

I hope this article helped you understand the benefits of the Solidly and Velodrome models. While I mention the myriad of forks in the introduction, I’ve stayed on course with this article. I guess this calls for a follow-up where I comb through their main forks and the modifications they implement into the template: stay tuned.

## Key Takeaways

* **Importance of Business Development** | ve(3,3), just like Curve, are protocols for protocols. The team's professionalism and ability to efficiently prioritize and executive on BD is a sizable success factor of the DEX over the long term.
* **Quality of the launch/airdrop/top racers rooster** | Even if BD is done well, a given ve(3,3) DEX is only as good as its top racers. Yes, you want them bribing, voting, and driving awareness, but not only. The quality of the liquidity driven to the DEX also matters (volume/TVL ratio).
* **LP Boost and its consequences** | If a ve(3,3) implements LP boost, it calls for Convex-like protocols. The success of the ve(3,3) will be impacted by how much and how well its Convex-likes do. To follow the key stats on the various wrappers and main veTokens holders, check - [DeFiWars](https://www.defiwars.xyz/wars).
* **ve(3,3) + Liquidity Concentration** | While ve(3,3) is a significant innovation for the incentives layer of the DEX, it currently harnesses sub-par liquidity structures. Properly matching the ve(3,3) incentives model with an efficient UNIv3-style liquidity structure will help further improve the effectiveness of the flywheel. 

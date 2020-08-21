---
title: "An introduction to Lien Finance & trustless stablecoins"
description: "Lien.Finance offers a compelling alternative with a stablecoin avoiding two common traps: over-collateralization and overengineered governance. Let's see how."
date: '2020-08-21T01:13:50.191Z'
categories: [🌌 DeFi, 🔮 Discovery]
tags: [DeFi, Ethereum, Lending, Derivatives, Stablecoins, MakerDao, DAI, USDC, USDT]
---

![Lien Finance](/img/2020/lien-finance/cover.png)

Stablecoins are the base currency of DeFi - we could even argue they were key to get the scene started - indeed, volatility makes most of the lending/borrowing scenario complex if not impossible.

Luckily for us, **the "stablecoin offer" expanded dramatically over the last few years**. On top of habitual DAI and USDT, we saw USDC & sUSD getting increasingly adopted in DeFi. USDC has obvious advantages - most notably a peg well maintained and very decent liquidity. 

However, **just like USDT, an USDC balance can be seized or frozen at any time** - at the sole discretion of Circle. As USDC is used more and more as collateral, this issue raises serious concerns. 

For instance, you can now mint DAI on Maker from USDC. But what happens to the DAI minted if the underlying USDC balance is seized because it was involved in a hack for instance? Right now, it's uncharted territory.


## So, why do we need reasonably trustless stablecoins?

**Stablecoins are two-dimensional objects: they bear an economic layer as well as a trust layer.**

On the economic side, you have questions such as:



*   Is it really maintaining its peg (1 coin = $1 as much as possible)?
*   Is the liquidity sufficient even for large needs?

**The economic dimension is usually enough for most traders as they won't be holding the stablecoin long-term or using it as collateral.** However, for reliable usage in decentralised finance, a stablecoin project must figure out the trustless dimension:



*   Can the system be shut down by a central authority / 3rd party?
*   Who controls it?
*   Can stablecoin balance be frozen/seized?
*   Could other parameters of the system be changed, resulting in potential losses for investors?

While **USDT and USDC are an obvious economic success, their model instantly excludes them from trustlessness**. So if we exclude stablecoins that can be seized or frozen, we're left with essentially either DAI or sUSD.

To learn more on trustlessness and understand the different models, I recommend giving Ryan's writing on Bankless a read - especially [this one proposing a taxonomy for economic bandwidth](https://bankless.substack.com/p/eth-is-irreplaceable).


### Chose one: trustlessness or economic viability?

**Currently, we have no stablecoins nailing both.** DAI used to be reasonably trustless, but operating at a low volume. Starting with the Multi Collateral DAI release, the governance decisions were made to boost the usage volume to the detriment of the trustless of the whole system: Maker now accepts collateral that can be seized, like wBTC, USDC, and soon real-world assets.

What we tend to observe is that trustlessness usually hinders economic efficiency, let me unpack this. Take the first Maker model, for instance, enabling you to mint DAI from ETH. Because of the system design, you can at a grand maximum mint ⅔ of the ETH value in DAI. 

The effective observed reality is much lower, as minting ⅔ puts you at risks of liquation. We call this model "over-collateralization", as there is - at any given time - more collateral (in value) than debt generated. **While over-collateralization enabled Maker to offer a stablecoin that can be minted directly from ETH, it's now one of the main factors hindering the scaling of the platform.**

Luckily, since the launch of Maker, the industry evolved dramatically. And since the beginning of the year, we're seeing again projects trying to deliver the stablecoin we direly need: both trustless and economically scalable. I know of two projects credibly exploring this path:



1.   [Reflexer](https://medium.com/reflexer-labs/stability-without-pegs-8c6a1cbc7fbd) - technically not a stablecoin but it will deliver a similar value proposition using reflex bonds.
2.   [Lien.Finance](http://lien.finance/), our focus for the rest of this article. Like Reflexer, Lien uses one level abstraction on top of ETH which is split into two distinct synthetic assets when deposited, as we’ll see below.

I've explored Reflexer, but I'm not familiar enough with it yet. Check the link above to learn more; the rest of this article will focus on Lien.Finance, since I'm more knowledgeable about it.


## Lien: The missing link between trustlessness and economic viability?

Considering our topic today, do not expect a simple and straightforward system. Indeed, with a goal set of providing reasonably trustless stablecoins without over-collateralization, the simple & straightforward routes do not work anymore.

{{< notice info >}}
Lien Finance is a fully fledged self-regulating protocol for creating unique derivative contracts. For clarity, this article focuses on iDOL, a decentralised stablecoin powered by Lien protocol. 
{{< /notice >}}

Another key diction of Lien is qualified under the umbrella of **"governance minimised"**. While it's accurate, it's not the most explicit. What is meant by that is that iDOL (the stablecoin produced by the Lien Finance system) is **effectively emitted and managed by a smart contract adjusting to market conditions**: or to put it in simpler terms, "the central bank of Lien" is a smart contract.

What this means is that the key parameters governing the system are not decided by humans or by a DAO like it is on Maker (such as the stability fee) - it's adjusting depending on the market's conditions.

So how does Lien.Finance pull this off? You're in for an insightful ride:


### Lien Finance: Infrastructure Overview

The graph below is pretty comprehensive, so it's a good starting point. No stress if you have no idea what's happening yet, we will go step by step following this illustration:


![Flows of Ether, SBT, and LBT in the iDOL/Lien System](/img/2020/lien-finance/eth-flow.png "Flows of Ether, SBT, and LBT in the iDOL/Lien System")


Before I dive in, allow me one reminder: **you do not have to interact with the whole system described below if you just want to interact with iDOL, the trustless stablecoin.** Just like DAI and others, you will be able to get them through other means too.


### Splitting the ETH: SBT+LBT

One of the core promises of Lien is to deliver a stablecoin that does not rely on over-collateralization. **Because of this, ETH itself is not suitable as collateral** - indeed the price volatility is too high to achieve the expected results.

Yet there is no asset with more "moneyness" than ETH on Ethereum, so how does Lien pull it off? The key lies with derivative assets. Instead of using the ETH itself as the base unit of the system, as Maker does, **Lien adds another layer of abstraction by splitting the ETH entering the system into 2 derivatives assets: LBT & SBT**.

Let's start with the common point: both are bond tokens - these are quite different from your usual ERC-20 tokens since they have a **maturity date**. These new asset types led Lien to also develop [FairSwap](https://lien.finance/White_paper.html#white_2), a DEX optimised for exchanging bonds tokens.

![The decomposition of ETH into SBT and LBT](/img/2020/lien-finance/eth-sbt-lbt.png "The decomposition of ETH into SBT and LBT")

Now for the differences, it's essentially light and day:



*   **🧱 The rock that is hard to move: the SBT**. The Solid Bond Token is more like a regular bond. SBT is stable against USD and payout a fixed value to its holder upon maturity, with a very high probability.
*   **🎈 The feather carried by the wind: LBT**. The Liquid Bond Token is a derivative packing the price volatility of ~2ETH in one. It's a very efficient way to gamble on ETH price, but also a tough game, as you're overexposed to the market downside.

Don't let this split scare you, the system is actually quite elegant and easy to follow once you've understood this.

So when the ETHs enter the system, it's split between one very volatile derivative, and one more stable. **Picture the LBT (the uber volatile one) as a way to "externalise" volatility.** We'll focus on SBTs for now, since they are the derivatives backing the stablecoin iDOL.


### From SBT to iDOL

SBT by itself is already roughly stable, the main wild card being the maturity date: the closer the SBT is to it, the safer. From here, savvy investors looking for stable assets could already compose their own basket of SBT with different maturity dates to hedge their risks.

But why should we have them do the work, when a smart contract could do it better and safer? This is where the iDOL contracts depicted in the top-right of the earlier graph shines. The **iDOL contract is essentially a rolling basket of SBT with diverse maturity dates.**

Depending on the markets conditions - most notably the observed volatility of ETH, the iDOL contract adjust its risk preferences:



*   If price volatility is low, the iDOL contract will be able to accept more SBTs that are farther away from their maturity date.
*   In times of rising volatility, the iDOL contract will recenter the exposure on SBTs approaching their maturity dates (-> less risk).

 

And that's precisely what got me on board - the whole system is agile and adjusting to the market - and not just the price of ETH itself. **The main driver of the risk-parameters decision in the Lien system is the volatility of ETH.**

To me, it makes so much sense!  Indeed, looking at volatility as well as the price is like observing the acceleration of a car instead of its raw speed:



*   The speed gives you an instant absolute: _the car is going at X Mph._
*   The acceleration paints a trend: _all things kept as such, the car will be going at X in Y time._

There is so much more to Lien, but this is an introduction article so let's keep this short. Before I let you go, let's explicit one last dimension of Lien: the "governance minimised" aspect. As we've seen above, the day-to-day parameter adjustments with Lien are done programmatically, adapting to the markets. 

That's a sensible innovation by itself if you consider for instance the Maker system where even basic parameters like the Stability Fee (fee paid to borrow) is decided through the voting system - and sometimes suffer from the delay coming with it. 


## Learning more on Lien Finance

Did I spark your curiosity on Lien.Finance? You can learn more about the project by watching this discussion on stablecoins I took part in **[#mDeFi 5 - The next generation of stablecoins](https://www.youtube.com/watch?v=jPrwinPvwv4)**. It's a 2h panel where I present Lien Finance, next to James ([mStable](http://mstable.org/)), Michael Egorov ([Curve.Fi](https://www.curve.fi/)) & moderated by my friend Abel ([AbelAbstracts](https://abelsabstracts.substack.com/)).

Finally, **[to follow Lien Finance, you can join their 🎮 community Discord](https://discord.gg/stCABfA)**.
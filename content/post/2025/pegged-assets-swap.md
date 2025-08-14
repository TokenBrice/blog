---
title: "The Pegged Asset Swap Wars"
description: "What if constant incentivization is not the best way to sustain liquidity, particularly for pegged assets? Exploring the impact of debt-driven liquidity for pegged assets swap."
date: '2025-07-08T01:13:50.191Z'
categories: [DeFi]
image: img/2025/pegged-assets-swap/pegged-assets-swap-cover.png
tags: [DeFi, Ethereum, Velodrome, Velo, veCRV, veVELO, Aerodrome, veAERO, Ekubo, Uniswap, Fluid, EulerSwap, Euler, Smart Debt, Smart Collateral]
url: pegged-assets-swap
---

Dear readers, it’s been a while! As you likely know, liquidity management is both my passion and profession. In this article, I aim to revisit the basics and offer a brief history through the lens of pegged asset swaps. As we detail the liquidity structure and venues that best support those pairs, we will gain a deeper understanding of key concepts that remain critical to navigating that space today. We also get the chance to cover Fluid DEX and EulerSwap, the two most interesting releases of the year for liquidity-building who definitely deserved more airtime around here.


## The Early Days of Pegged Asset Swaps (2018-2019)

Once upon a time, more than half a decade ago, **all we had to swap on the mainnet were Uniswap, Bancor, and some clunky order-book-based DEXes like EtherDelta.** So, when it came to pegged asset swaps, the options were minimal, and we were using the Uniswap V2 USDC/USDT pool, which was akin to sheer insanity.

Let’s zoom in on this historical trivia to understand **the level of waste that was achieved** at that time. When it comes to liquidity pools, the key parameter is the relative evolution of the two assets' prices: if you have done any volatile LPing, you’re deeply familiar with that. If you LP say LINK/ETH, the max pain for you, in terms of impermanent loss, is, for instance, ETH shooting up while LINK is dumping: your LP position decreases in ETH (which goes up in price), and accrues LINK (which is falling).

USDC/USDT is another story, though, as the two assets are deeply correlated, with a maximum price difference ever seen between them of around 10% during a specific event (the USDC SVB depeg); in regular times, the two have a price difference in the basis point range. However, UNIv2 distributes the liquidity across the entire price range, meaning it allocates an equal amount of liquidity anywhere from 1 USDC = 0.0000000001 USDT to 1 USDC = 10000000000000 USDT. To put it simply: 99.9% of the liquidity in a UNIv2_USDC/USDT will never be utilized. I think it’s clearer on the graph:


![liquidity-structures](/img/2025/pegged-assets-swap/liquidity-structure.png "x*y=k vs StableSwap")


The only valuable liquidity there (assuming 1 USDC ≃ 1 USDT) is located at the intersection of the two green lines, making up a very minimal share of the entire liquidity distribution curve.

On the other hand, note the stableswap liquidity distribution, displayed in blue, on the same graph. For assets at similar prices, the area covered by the curve is much greater than with the Uniswap invariant.


## The StableSwap Revolution for Pegged Assets Swaps (2020)

Once StableSwap was available, stablecoin liquidity quickly migrated there, as it was significantly more efficient (we’re talking >100x improvements in efficiency vs UNIv2). It was **the first live instance ever seen of Concentrated Liquidity on mainnet, before UNIv3**. The two are difficult to compare, as UNIv3 is much more flexible, while Curve-StableSwap is more specialized; however, kudos must be given where due. Along with increased efficiency, Curve provided an incentive model - veCRV+CRV emissions, which has been [covered several times on this blog already](https://tokenbrice.xyz/crv-wars/).

Incentives are critical for pegged asset pairs, as they have some specific characteristics:



1. They tend to be overall **low-volume** (compared to a volatile pairing)
2. **The fees LP can charge are much lower **(up until recently, the convention was 0.3% to 1% per trade for volatile assets, and 0.05% for pegged assets)
3. **Their volume comes in spikes** correlated to events associated with the coin (ex, USDC depeg was one of the highest volume days ever for USDC)

Because of all of the above, I thought until very recently that incentivization structures were even more critical for pegged asset pairs than for volatile assets. With the arrival of Fluid DEX and EulerSwap, I don’t think it’s the case anymore. However, before we delve into them, we must first address another significant historical milestone in pegged assets liquidity: the release of Uniswap V3.


## The arrival of Uniswap V3 Concentrated Liquidity (2021)

Uniswap V3 released and delivered customizable concentrated liquidity to essentially every asset type, enabling massive efficiency gains for all liquidity providers. However, since it wasn’t just for pegged assets, it almost meant amplified impermanent losses for volatile assets LPs. Considering the novelty of the liquidity structure, along with the lack of infrastructure in the early days, the launch of UNIv3 was initially slow.

However, the customizable concentration delivered tangible benefits, especially for a subcategory of pegged assets I branded “loosely pegged assets”: think of pairs like:



* wstETH/ETH (correlated, but wstETH is up-only against ETH), 
* LUSD/USDC (correlated, but LUSD can slightly over/under-peg)

In such cases, **UNIv3 concentrated liquidity enabled LPs to replicate a distribution similar in efficiency to Curve’s Stableswap but adjusted to the tokens' price action particularities**, and it translated once again into massive efficiency gains. However, the final unlock (as of the current industry state) was only to come years later with the arrival of Fluid DEX and EulerSwap.


## Debt as liquidity (2025)

I won't delve too deeply into the models of Fluid and EulerSwap in this post for conciseness, as I want to focus more on what it means for liquidity building. Simply put, Fluid found a creative way to transform debt into liquidity with “Smart Debt”.

Picture an average user supplying ETH collateral and borrowing USDC. Does he specifically want USDC? Most likely, he doesn’t care as long as he’s borrowing a safe and stable USD-pegged coin. He’d likely take USDT as well.

That is precisely what smart debt does. In a smart debt vault, our borrower borrows a mix of USDC and USDT, which constantly evolves: his debt now serves as liquidity for the USDC/USDT pair. What that means for the borrowers is **reduced borrowing cost, as he now earns trading fees**, potentially enabling him to offset the borrowing interest.

![fluid-smart-debt](img/2025/pegged-assets-swap/fluid-smart-debt.png)

That’s from the borrower’s perspective, but now let’s switch to a protocol mindset. What does this mean for Circle and Tether? Essentially, **liquidity at virtually 0 costs, with no form of incentivization whatsoever.** Nothing really new there for Circle who has been sponsored by the whole ecosystem for years – but for another stablecoin, say a GHO, BOLD, or FRAX, that is huge.

I focused on Fluid here, but the thought process is similar for EulerSwap, although the implementation is different. EulerSwap is still in testing mode and already printing serious volume on USDC/USDT.

If you understand this, you can reach my thesis, which simply states, “I don’t see a DeFi where Euler/Fluid/Similar do not eventually dominate pegged-assets swaps.”

Not seeing it yet? Remember the following:



* Pegged assets pairs are usually low volume ⇒ low fees
* Thus, they require heavy incentivization to maintain on a classical DEX
* Fluid and Euler can sustain this liquidity at close to no cost.

⇒ If (it already started) there is a race to the bottom in terms of fees for pegged asset swaps, regular DEXes have exactly 0% chances of winning it.


### 0xOrb, a potential challenger (~2026)?

Now, to give you an accurate picture of the whole pegged asset swap landscape, I must mention another project not live yet, but promising: [0xOrb](https://orbswap.org/). The promise is simple: **stableswap, but with n assets, n being able to go up to 1000**.

So for instance, for stablecoin, you could picture a mega-pool well supplied in USDC and USDT, that then proceed to onboard “alternative” stablecoins and offer them great liquidity against the majors. The approach has merits for the long-tail of pegged assets, but I don’t see such pools dominating the core volume (USDC&lt;>USDT or cbBTC&lt;>wBTC).

On top of that, such pools could be cross-chain, although I think the benefit here is absolutely marginal if not **detrimental** (⇒ increases the risks and complexity of the infra for no benefits), **since USDC and USDT are increasingly bridgable 1:1 fast between chains thanks to product like [CCTP](https://www.circle.com/cross-chain-transfer-protocol)**.


## What does it mean for incumbent pure-DEX players?

First, the most significant caveat: we’re discussing pegged asset swaps here. Replicating the same playbook on volatile pairs is much more challenging, [as seen in Fluid’s Smart Debt+Collateral ETH/USDC vault and the losses its LP incurred](https://gov.fluid.io/t/current-issues-with-eth-usdc-pool/1606).

DEXes that generate most of their volume and fees through volatile pairs, such as Aerodrome, are likely not to be impacted by these new entrants. **The reality is, however, much grimmer for DEXes focusing on pegged assets**, and I want to consider two of these to wrap this article up:


### Curve: game over unless there are sizeable changes

Pegged assets swaps remain critical for Curve, still seen as the home of stablecoin liquidity. Indeed, there were attempts to capture volatile volume with CryptoSwap, but it proved unsuccessful.

With the arrival of Fluid and EulerSwap, I think Curve is the DEX with the most to lose, and I don’t see it maintaining a prominent volume (they have already been kicked out of the top 10 a while ago) unless sizable changes are happening:

* **veCRV revamp**: harnessing the learnings from newer models like veAERO to optimize the CRV emissions allocation.
* **Increased DEX efficiency harnessing crvUSD**: for instance, by enabling crvUSD loans to Curve LPs.
* **A new liquidity structure for volatile assets** : so that Curve can capture the associated volume.


### Ekubo: the confident latecomer rushing to its demise

Ekubo’s situation is arguably even worse, as they came only recently to the party. At face value, Ekubo on Ethereum is a fast-growing DEX printing serious volumes. Ekubo is essentially a UNIv4-alt, with slightly more liquidity structure customization and a DAO that proved less extractive than Uniswap’s (the lowest bar of all, but still).

The problem lies in where the volume comes from: the vast majority (>95%) of it is on a USDC/USDT pair with 0.00005% fees and heavily incentivized. Ekubo is essentially playing a race to the bottom it cannot win because Ekubo cannot sustain extremely low fees in the long term (LPs must eat), while Fluid/Euler can (if borrowers receive even a 0.1% yield on their debt, thanks to smart debt, they are better off than without smart debt and thus happy).

![ekubo-stats](/img/2025/pegged-assets-swap/ekubo.png "Ekubo Stats, as of July 07 2025")

With a $2.6M TVL pool, processing ~$130M volume daily for $662 of fees collected daily, incentivized ~8% in EKUBO, they are already fast approaching the limit of what they can do.

The most amusing aspect of all this is that **Ekubo itself initiated the race to the bottom with the USDC/USDT swap fees and will be spectacularly vainquished at its own game**. DeFi never ceases to entertain.

As always, I hope this article was insightful and deepened your understanding of the pegged assets swap game. I look forward to getting my character trashed by the Ekubo community simply for stating an opinion driven by facts: their reaction gave me extreme confidence in my assessment, as I have observed the same response when:

* I denounced MAI's absurd security practices, and it got hacked + depegged shortly after.
* I denounced R/David Garai's gaslighting and lies, and R proceeded to get hacked into oblivion &lt;6 months later.
* I criticized Prisma’s team behavior, and they proceeded to get hacked and shut down the protocol &lt;12 months later.

And the list goes on. Best of luck to all, especially the EKUBO bag holders – try to have some class in your dismay that would serve you well.

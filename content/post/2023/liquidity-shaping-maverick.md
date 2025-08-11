---
title: "Staying Ahead of the Curve: the shift from Liquidity Mining to Liquidity Shaping"
description: "The DEX war rages on, more competitive than ever. Next to the unicorn, llama and scale cartels, a fourth center is emerging thanks to unprecedented features: umatched liquidity structures paired with an immensely more efficient incentivization models: **liquidity shaping**. Will it be enough for Maverick to prevail?"
date: '2023-07-07T01:13:50.191Z'
categories: [DeFi, Understanding]
tags: [DeFi, Ethereum, Decentralized Finance, Maverick, DEX, Liquidity Management, Liquidity Shaping, Concentrated Liquidity, veCRV, Solidly, Velodrome]
toc: true
tocNum: true
url: maverick-liquidity-shaping
image: img/2023/liquidity-shaping-maverick/cover.png
---

It's been four months since Maverick is out, and a few days since the MAV token joined the fray. Yet, most of DeFi is still scratching its head regarding how Maverick delivers 2-3x the capital efficiency of its top competitor, Uniswap. 

So the time was right for a deep dive into the innovations brought by the model and the new paradigm it fosters regarding liquidity management: **liquidity shaping**.

## Innovations on DEX? More like tools for LP to express themselves

Fundamentally, a decentralized exchange can innovate at two levels: 

1. **The liquidity structure**: the options offered to liquidity providers to design the supply activity that best matches their thesis.
2. And/or **the incentivization model**: the tools and modalities enabling DAOs & projects to incentivize customized or not liquidity structures.

Most new DEX being released recycle an existing infrastructure and focus on innovating on only one dimension - usually the incentivization model - as seen recently with the wave of Solidly/Velodrome forks - **[ve(3,3), the logical next step after veCRV?](https://tokenbrice.xyz/content/posts/2023/solidly-velodrome-template.md** 

There are, however, a few critical moments in the industry when a new DEX was released and provided **critical innovation on both fronts:**

1. **[Uniswap V1/V2](https://www.defiscan.info/protocols/uniswap-v2/ethereum)** established a solid infrastructure for `x*y=k` pools & basic incentivization model: 30 bps fees auto compounded & the possibility of having Liquidity Mining programs on the staked LP tokens (ERC20).
2. **Curve** provided an innovative and efficient liquidity model for pegged assets (stableswap) while pioneering a ve/gauge-based model for liquidity provider incentivization introducing a revenue capture at the token level (admin fee).
3. **[UniswapV3]( https://www.defiscan.info/protocols/uniswap-v3/ethereum)** delivered the tools to manage a more advanced liquidity structure harnessing concentrated liquidity efficiently and providing more flexibility fee-wise (1, 5, 30, 100 bps fees, not auto-compounded)
4. And finally came **[Maverick](https://www.defiscan.info/protocols/maverick-v2/ethereum)**, which goes even further than UniswapV3 in the customization of the liquidity structure it provides, offers streamlined position management (native rebalancing) and an unprecedented level of control regarding incentivization options, marking the birth of a new paradigm: liquidity shaping.

Each core innovations **enable more expressivity for LPs: they get access to increasingly refined and customized tools enabling even the most intricate thesis to find a proper medium to be expressed onchain**.

Yet, before diving into the depth of liquidity shaping, some pointers on Maverick are necessary. Indeed, to fully understand the impact of liquidity shaping on Maverick, you first need to master its liquidity structures and their consequences.

## MAVERICK'S LIQUIDITY STRUCTURES

Indeed, one of Maverick's critical innovations is its liquidity structures, enabling the exchange to reach an unprecedented level of capital efficiency.

Maverick offers four options to LP that could be regrouped into two categories for simplicity:

1. The static mode is similar to a UNIv3 liquidity providing across a custom range, with **immensely more flexibility**.
2. And three dynamic modes offer **various flavors of rebalancing to LP** to optimize further their earning: left (follows price to the left), right (follows price to the right), and both (follows price both ways).

### Why Maverick's Static Mode is a game changer

Many still have to understand how much of an improvement Maverick's static mode is over UNIv3, so let us focus on it for a minute. Here's a quick table recapping the main difference to get started:

| Item                                                         | Uniswap v3            | Maverick Static Pools         |
| ------------------------------------------------------------ | --------------------- | ----------------------------- |
| Supply liquidity in an arbitrary custom range, even potentially only with one token | ✅                     | ✅                             |
| Support an uneven liquidity distribution within that range   | ❌                     | ✅                             |
| Supports customized fees and width                           | 4 fees tiers, 1 width | Near-infinite fee/width tiers |
| Supports the creation of ERC-20-wrapped LP tokens to ease LP onboarding & incentivization | ❌                     | ✅ (Boosted Pools)             |
| Supports natively the distribution of rewards (Liquidity Mining) | ✅                     | ✅                             |
| Supports natively the weighted & customized distribution of rewards to LP (Liquidity Shaping) | ❌                     | ✅                             |

Like UniswapV3, Maverick supports supplying liquidity in **an arbitrary custom range,** even potentially only with one token, for instance, an LP on ETH/USDC from $2000 to $2400.

If the current price is below $2000 (at the time of writing: $1900), the LP will be supplied purely with ETH and progressively rebalances to USDC as the price moves upwards, ending entirely in USDC at $2400.

![eth-lp-univ3.png](img/2023/liquidity-shaping-maverick/eth-lp-univ3.png "The $2000-2400 ETH/USDC LP on UniswapV3")

But what about LPs that have an even more refined thesis? What about the LP that sees ETH in that range for a week but mainly in the $2150-2250 area? Wouldn't it be nice for him to be able to express this thesis through the liquidity structure he chooses? It is precisely what Maverick enables:

![eth-lp-mav.png](img/2023/liquidity-shaping-maverick/eth-lp-mav.png "The same $2000-2400 ETH/USDC LP on Maverick, with about x4 more liquidity in the $2150-$2250 range")

In the screenshot above, you see a distribution from $2000 to $2400 on the ETH/USDC pair; however, **unlike Uniswap, which necessarily distributes liquidity evenly across the range, Maverick enables LPs to choose**. To better fit our LP thesis, most of the liquidity is concentrated over the three ticks covering the $2150-2250 price zone.

### Maximizing the expressivity offered to LPs

The expressivity offered to LP on Maverick is virtually infinite. I expect to see some interesting use cases emerge soon, especially for the protocols that will harness Maverick from the get-go ("Maverick-native" protocols). For instance, y**ou could envision Maverick as a price stabilization mechanism for a stablecoin or a pegged asset**.

Assuming the stablecoin project controls some liquidity, it could supply it in very expressive ways in times of need to constraint the price range. Here's a "buy wall" liquidity structure on LUSD: the whole liquidity of this LP is supplied on a single tick, the first one where LUSD is worth below 1.00 USDC.

![mav-buy-wall.png](img/2023/liquidity-shaping-maverick/mav-buy-wall.png "A stablecoin buying wall liquidity structure on Maverick")

With a current price >1.00 USDC, this LP is supplied 100% in USDC and acts like a buying reserve: if the price of LUSD falls, the LP will rebalance. Such positions are promising, as they can exert buy/sell pressure helping to better constrain peg assets within narrower ranges, which massively reduces the cost of their liquidity incentivization.

### What about the dynamic modes?

Maverick dynamic modes offer a convenient and easy solution for LPs who maximize their exposure to market prices to maximize the volume processed. All three modes essentially harness the same structure but give different options to LP:

- Follow the price just one way (left or right) - there are tons of pairs where it makes a lot of sense, like wstETH/ETH (wstETH being "up-only" against ETH thanks to the staking yield)
- Follow the price both ways, a good match for LP looking to maximize adequate liquidity and fees collected at the expense of increased IL risk on the principal. It's particularly suited for stable and pegged asset pairs, but not only.

![mav-both.gif](img/2023/liquidity-shaping-maverick/mav-both.gif "Visual explainer of Maverick's both mode")

The key thing to understand here is that **Maverick delivers native rebalancing to its LP**, and here again, it goes above and beyond what preceded in terms of customization options. "Native" is the keyword here, meaning the rebalancing can be **done cleverly and gas-efficiently**. While this is not new by itself, here again, the devil lies in the details:

On Curve, LPs have no options: their liquidity is concentrated, but all LPs of a given pair are under the same regime. It eases the management, but kills the expressivity. With Uniswap, LPs can dynamically rebalance their position using third-party tools like Arrakis; it comes with sizable trust assumptions, potential fees, and hefty gas costs. It allows more expressivity but requires more active management.

While there are some limits to Maverick's liquidity rebalancing, based on a TWAP and with some delays to avoid manipulations, it remains a crucial tool to help LPs maximize the time effectively spent in range / in the current price tick.

## MAVERICK'S INCENTIVIZATION MODEL: LIQUIDITY SHAPING

With a better understanding of the first fundamental innovation brought by Maverick - the unprecedented expressivity offered to LP in the design and management of their position - we can now explore Maverick's second leg: its novel incentivization model.

The story here is both short and long. **In short, Maverick provides the same level of customization at the incentivization layer as at the pool creation level.**

It leads us to a longer story, with examples to be more explicit. Replicating most existing liquidity structures and incentivization models on Maverick is possible. But what's even more interesting are the new ones previously never tried because they were not technically feasible before Maverick: it's time to explore and experiment!

### Dynamic contract-triggered buy/sell walls

Remember the example from earlier about the stablecoin project posting liquidity as a buying wall to constrain the price? **The project does not even needs its liquidity to do it**, as the same process can be replicated with a boosted pool:

1. The project creates a boosted pool where all the liquidity is distributed on one tick below the price like above.
2. The project supplies incentives to the boosted pool for the duration of its choice & apes will do the rest.

This whole process can be automated and triggered entirely through smart contracts, meaning another contract could dynamically manage the incentives.

### The case of cvxCRV/CRV

Let's study another checkmate case, the one of cvxCRV. Indeed, the cvxCRV/CRV Curve pool is the absolute worst offender:

- It harnesses a **a regular structure, absolutely sub-optimal for an asset trading in a constrained range like cvxCRV**.
- It harnesses a **"dumb" liquidity mining model where all LPs are paid equally**, leading to cvxCRV deposits, which make 75% of the pool, earning 75% of the rewards - while being close to useless liquidity-wise (as there are already too much cvxCRV in that pool).

#### So what can be done better?

First, the concentration could be finetuned much more at the liquidity structure level. cvxCRV is a "one-way asset": you can wrap CRV to cvxCRV 1:1 through the Convex contracts, but converting cvxCRV to CRV is done on a DEX at a discount.

=> This means cvxCRV has a price ceiling against CRV: in no world, cvxCRV could be worth >1 CRV, and the current price is around 0.95 CRV per cvxCRV.

==> The ideal structure for such a pool could be **a concentration going from 1cvxCRV = 0.9 CRV to 1 cvxCRV = 0.99 CRV, offering vastly superior liquidity efficiency**.

Now, for the incentivization layer, massive gains are to be made with a switch. Instead of paying all LPs equally while the pool is massively unbalanced, why not focus on those who bring the most value to the pool, aka the CRV component?

=> I'd go with two joint pools to best cover that pair incentivize-wise: **first, a static LP over ten bins** centered around the current price - it provides room for the price to express itself with sufficient liquidity & this structure is already >100x more efficient than the existing Curve V2 pool.

==> For the nail in the coffin, we can **add a one-tick left-right pool one top to maximize liquidity efficiency**. 

The details of this example help you understand that if you take this pool to Maverick, the compounded effect of the superior liquidity structure with a vastly more efficient incentivization model leads to results from a different league. 

![curve-cvxcrv-crv.png](img/2023/liquidity-shaping-maverick/curve-cvxcrv-crv.png "The cvxCRV/CRV pool on Curve")

There are currently $54M TVL in Curve cvxCRV/CRV pool for a daily volume of around $300k daily (0.5% utilization). With a base incentive of 12% CRV, ~**$6M of CRV tokens are expanded yearly to maintain this liquidity**.

**On Maverick, a ~$500K  properly structured pool** ($250k static broad range + $250k left-right) **would be sufficient to consistently process the $300k daily volume** with better prices than on Curve. Assuming the same incentivization intensity, **it would cost $60k a year to maintain**.

### Proto Liquidity Shaping with Bunni?

I hope that, at this point, you get a better sense of why liquidity shaping is genuinely revolutionary, as it will allow another order-of-magnitude leap regarding the efficiency of both the liquidity structures and the incentivization models. 

There are earlier, less complete iterations on such a concept, provided by the liquidity manager built on top of UniswapV3 that allows incentivization on a customized range, for instance, rewards for LUSD/USDC LP, but only for the LUSD = 0.999 USDC to LUSD = 1.01 USDC range. [Bunni](https://bunni.pro/) is a good example of such services.

Those could be described as "proto liquidity shaping," as they enable to force a specific price range but cannot apply different weights to each tick in that range: they are limited by the Uniswap V3 pool model that offers less flexibility than Maverick. In the end, both are quite complimentary as Bunni can be used to force a wide range, which can be further refined with a uneven static Maverick pool & finally maintained uber liquid at current price with a left-right on Maverick too.

## MAV TOKEN

With clear perspectives on both the novel pool structure and incentivization model and their consequences, we're now ready to add the last piece of a puzzle, one you're likely more familiar with, but here too, there are key differences: the MAV token. 

Released just a few weeks ago, the MAV token has been airdropped to early liquidity providers and protocol users. The initial airdrop is just **the first of many**, and more are planned, for LPs, but also protocols harnessing Maverick or building on top of it. For more details on the intended distribution, check this [Maverick Ecosystem Incentive Program](https://medium.com/maverick-protocol/maverick-ecosystem-incentive-program-95cf76dbfa5e) article.

As readers of this blog, I imagine you are extensively familiar with the veCRV model and its implications. If not, you've got some reading to do:

**[⚔ CRV wars: understanding the race to accumulate power to influence Curve Finance protocol](https://tokenbrice.xyz/content/posts/2021/crv-wars.md)**

### veMAV & Liquidity Directing Voting (vote-directed liquidity shaping)

![vemav](img/2023/liquidity-shaping-maverick/vemav.png)

The launch of the MAV token is sequential, currently in phase 1, where users can claim their drop, LP MAV, or lock it to obtain veMAV. **Stage 2 will introduce Maverick's Liquidity Directing Voting and mark the true beginning of the MAV races.** 

The main difference here is, of course, the expressivity enabled by Maverick that will also impact the tokenomics: unlike on veCRV or veBAL, where projects allocate liquidity to a whole pool, here, with Maverick, **protocols will be able to target their voting power to a specific part of the AMM distribution**. You'll find more information on veMAV here: [Introducing Maverick Protocol's Voting-Escrow Model](https://medium.com/maverick-protocol/introducing-maverick-protocols-voting-escrow-model-c29a60120339).

### Maverick & veMAV X-chain strategy

Another critical thing to note with the MAV token is that it implements [Layer Zero's Omnichain Fungible Token (OFT) standard](https://layerzero.gitbook.io/docs/evm-guides/layerzero-omnichain-contracts/oft), greatly facilitating cross-chain operations. It enables MAV to exist natively on every chain and should ease the operational overhard for the team to launch the gauge system on a new network.

It might not seem much at first glance, but it could make a massive difference. Indeed, Curve and Balancer have been slow to export their full gauge model to networks other than the mainnet they initially operate on. **I expect Maverick to move much more quickly**, and the early empirical data validate it. In ~3 months of existence, Maverick has already launched two chains apart from mainnet: zkSync and BSC.

### Another main difference with veCRV

veMAV implements several other changes compared to a base veCRV model, and I invite you to identify them all. Here are some other ones:

- The veMAV per MAV weighting is not linear here, even if it still favors max lockers (4 years); the min lock of 1 week gives one veMAV/MAV, while max locking gives 5veMAV/MAV.
- **There is no linear decay** like on veCRV - which is a significant UX improvement. It could also have very positive consequences for veMAV liquid wrappers, making it easier to keep close to the peg.
- Yet there are still incentives to stay committed. Indeed, The veMAV/MAV ratio is computed with the formula `1.5^(lock end - contract launch)`. With the lock end as the main parameter, veMAV lockers who want to maximize their power must extend their lock frequently.

Regarding wrappers, several existing projects have already expressed their intention of building on top of Maverick or veMAV, including Paladin, SpiralDAO, and StakeDAO. The MAV wars will be vicious, so read the fine print before locking your MAV somewhere else than in the veMAV contract.

## Forward outlook & parting words

Maverick is currently live on mainnet, zkSync, and BSC. It's interesting to remark on how much it dominates the volume on zkSync, even with a fraction of its competitor TVL:

![zksync-dex-volume.png](img/2023/liquidity-shaping-maverick/zksync-dex-volume.png "Overview of volume processed by the main DEXes on zkSync (DeFiLlama)")

![zksync-dex-tvl.png](img/2023/liquidity-shaping-maverick/zksync-dex-tvl.png "Overview of the TVL attracted by the main DEXes on zkSync (DeFiLlama)")

On mainnet, most of the success has been found with ETH-LSDs pairs (wstETH, swETH, etc.) and stablecoins. Maverick's efficient liquidity structure is highly competitive with Curve, Uniswap, and Balancer.

On volatile tokens, LPs are a bit shy still, just like it took a few months for people to get used to the novelty brought in by Uniswap V3. Interestingly, LPs are experimenting more on zkSync, especially on pairs such as ETH/USDC, thanks to the lowered gas costs, leading to an overall capital efficiency even more significant than on mainnet, here are the stats for today (July 06 2023): 

- Uniswap V3 - mainnet: 0.23
- Maverick - mainnet: 0.3
- Maverick - zkSync: 0.93

### Getting started with Maverick as a user

There is a learning curve for Maverick, as understanding how to structure liquidity properly can be intimidating because of all the options provided. Yet more options mean more expressivity and, thus, more efficiency and returns when adequately harnessed.

**To make the most of Maverick as a user and discover the protocol in an environment with low fees, I'd recommend supplying your first LPs on zkSync** - as it will enable you to modify them at a low cost if needed. Like most new DeFi products, the best way to master it is to use it and see it behaves in various market conditions, so get at it: you might also be double-dipping on airdrops so that it can be quite a rewarding experience.

Don't hesitate to check out the Boosted Pools, which - in addition to their incentives - have a pre-defined liquidity configuration, making them more accessible to LPs.

### Liquidity Managers, it's time to wake up!

On the project side, **it's an absolute necessity for liquidity managers to understand and master Maverick**, as it's by far the venue delivering the most liquidity efficiency. I'd be happy to help them in the process, since it has become a specialty of mine. Feel free to reach out if you'd like to discuss how your project could harness liquidity shaping.

{{< notice note >}}
Disclosure: In case you missed the news, I've been advising the Maverick team since last year.

**[Announcement: TokenBrice 🤝 Maverick](https://tokenbrice.xyz/content/posts/2023/maverickxtokenbrice.md)** 
{{< /notice >}}

It will be interesting to see how the next few months of the DEX wars will unfold; with Maverick already consistently in the top 5 of Ethereum DEXes by volume processed, I think it's no stretch to envision it breaking into the top 3 by the end of year latest as the veMAV gauges will be released.

I hope this article helped you better understand the paradigm shift that lies with the transition from liquidity mining / basic ve(3,3) to Maverick's powerhouse implementing vote-directed liquidity shaping. Feel free to follow the events live, monitoring onchain data like as OGs do.

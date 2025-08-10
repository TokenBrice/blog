---
title: "Announcement: TokenBrice 🤝 Maverick"
description: "I am supporting the Maverick team as an advisor, helping with the growth strategy, tokenomics, and BD."
date: '2023-04-21T01:13:50.191Z'
categories: [Projects]
tags: [DeFi, Ethereum, Decentralized Finance, DEX, Liquidity]
toc: false
tocNum: false
url: maverick-x-tokenbrice
image: /img/2023/maverickxtokenbrice/maverick-x-tokenbrice-cover.png

---

This post is more of a personal announcement: I wanted to let you know what I am up to and what's happening with Maverick. So let's not beat around the bush: I'm thrilled to announce that **I'm supporting the Maverick team as an advisor, helping with the growth strategy, tokenomics, and business development.**

### Storytime

Just like me, you must be over-saturated with DEXes. If you follow DeFi closely, you've seen several of these launches daily. Yet most still adopt fundamental liquidity structures: x\*y=k for volatile pairs and stableswap, and focus on innovating on the tokenomics instead: the now famous ve(3,3) DEXes.

**I've been looking for a DEX that would innovate at the fundamental level** for a while, so in May last year, when Bob reached out to let me know about Maverick, I was all ears. I quickly realized Maverick could reshape how we envision liquidity in DeFi and help further improve its efficiency. So I’m glad to announce my involvement today: Maverick is already live, growing quickly, and poised for even exponential growth.

But before we dive into what makes Maverick so interesting, we need to take a step back and consider the broader context of liquidity in DeFi:


### Liquidity Structuring Deep Dive

**In the beginning, there was Uniswap**, and its ease of use for liquidity providers led people to believe it was a trivial activity. Yet, any liquidity-providing activity on a DEX involves two decisions:

1. Picking a pair (or more) of tokens (ex: ETH/USDC)
2. **<span style="text-decoration:underline;">Forming price assumptions regarding one/both tokens (🐂, 🐻, or 🦀)</span>**

The second decision is **often implicit**, like with UniswapV2, where you get no option but only one choice: 50/50, meaning that your optimal scenario is both tokens going sideways in price with a large trading volume.

When Uniswap V3 emerged, the second assumption was suddenly more explicit to DeFi users thanks to concentrated liquidity. However, V3 added complexity to the liquidity provider experience and active management. It **mainly caters to power-users who can afford frequent rebalancing**, or **require external tooling** to be harnessed effectively by LPs, the liquidity manager – Arrakis, Bunni, etc.


### What's unique about Maverick?

Simply put, Maverick is the spiritual descendant of UniV3 and CurveV2. It offers infinite flexibility in the design of liquidity-providing position, similar to Uniswap V3, but with streamlined and autonomous execution, just like on Curve. Indeed, LPs on Maverick can decide to redistribute their liquidity to follow the price in one or both directions. **If needed, the rebalancing is done at the DEX level, ensuring gas efficiency.** Maverick also supports “static pools” that are range-bound too.

**This feature makes Maverick a fantastic fit for pegged assets, especially those that are not continually trading precisely at the peg** and so underserved by the usual liquidity structures, such as a LUSD/USDC pair:

* Curve stableswap, which optimizes liquidity for a 1/1 price, is not ideal when LUSD is overpeg.
* Uniswap v3, where LPs usually end up super concentrated around the current market price, which is efficient, but also quickly through them out of range as the price move

![mav-mode-both](/img/2023/maverickxtokenbrice/mav-both.gif "Maverick both mode, where the liquidity follow the price left and right")

On Maverick, such a pair can be harnessed optimally by each LP, depending on their actual goal. **It enables each LP to craft an automatically adjusting position that enforces a strategy fitting his assumptions and needs**. Here are some examples of goals &lt;-> liquidity structure matching:

* 🎚️ | Looking for a safe yield with minimal risk? A static LP might be preferable, as the outcomes are predictable.
* 🐂/🐻 | Thinking LUSD is currently over/undervalued: you can supply directional liquidity and earn extra if your assumption verifies.
* 🦀 | Want to bet on volume with prices going sideways? You can simply focus your liquidity a few bins around the price and activate the **left-right mode** to constantly rebalance the current price, thus maximizing the available liquidity and fees collected but also the potential impermanent loss.

So far, Maverick has found **a beast of a product/market fit on pools like wstETH/ETH**, often averaging over 100% daily utilization rate. Here’s today, for instance (4/20):

* Curve: TVL = $1.5B, Volume =$34M, Utilization = 2,26%
* Maverick: TVL = $10.6M, Volume =$10.45M, **Utilization = 98,5%** 

![Maverick Top Pools](/img/2023/maverickxtokenbrice/mav-pools.png "Top pools on Maverick today (4/20/23)")


### What's next?

Launched just a few weeks ago on the Ethereum mainnet, Maverick is already seeing an impressive volume and unprecedented liquidity utilization rate, especially on pegged asset pairs.

Maverick was also launched on zkSync, its first L2, a few days ago. As more staple DeFi projects roll out service there, Maverick will have many opportunities to demonstrate the superior efficiency its liquidity designs can offer to LPs.

I’m excited about the next steps: as a DeFi Strategist at Liquity, the release of Maverick felt like early Christmas to me; I think it's just getting started! 

I’ll contribute to Maverick as an advisor, meaning that my main focus remains my commitment to immutable protocols, especially Liquity, helping them grow through various onchain and offchain activities. I’m confident Maverick will quickly prove to be a decisive tool in achieving that purpose.

Just hearing about Maverick? **[Check it out](https://mav.xyz/)** or [join the Discord server.](https://discord.gg/mavprotocol)

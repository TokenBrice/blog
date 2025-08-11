---
title: "🧭 DeFi Moneygames: Assessing risk and avoiding wreckage"
description: "A quick primer to help players of DeFi food-based moneygames to understand the basic template (go WINE!), assess the risk & save their precious tokens."
date: '2020-08-26T01:13:50.191Z'
categories: [DeFi, Practical]
tags: [DeFi, Ethereum, Staking, Memecoin, Foodcoin]
image: /img/2020/defi-moneygames/cover.png
---

Food-based social moneygames are all the rage in decentralised finance. Today, I wanted to write a quick piece to provide some context on them, as well as some tips for those who want to. I'll not pass moral judgement on such projects, I leave it up to you.

The launch of Yearn Finance last month was probably the most significant event of the year for DeFi. If you are not familiar at all with Yearn, check this intro: **[YearnFinance - DeFi on autopilot?](https://tokenbrice.xyz/content/posts/2020/yearn-finance-YFI.md)** - it will be helpful to better understand today's article.

The launch of Yearn's token, YFI was highly innovative back then: 100% of the supply has been distributed to users providing liquidity on different pools tied to the protocol. This launch framework has now become a template replicated by countless projects which spun out in the wake of Yearn's tremendous success: YFII, YFL, YAM, SHRIMP, PASTA, BASED, etc.

On top of this base building block of "the farming cooperative" provided by Yearn, many projects add a tokonomics twist to their base asset, hoping to make it more sticky. Here are the usual suspects:

1. **A deflationary model** (this is usually stupid) - **RUN**. Example: PASTA. (RIP)
2. **A rebase mechanism** (it can get interesting - increases information asymmetry). What matters here is finding a relevant price target & making sure the rebase code is not faulty / not leading to issues with other parts of the protocol such as the liquidity pools (Hello YAM). Sadly, it also contributes to turning the game into a ponzi-esque situation where inexperienced investors get plundered by experienced farmers - rebase mechanisms make it tricky to calculate returns.
3. **Social-based mechanisms**, such as a daily/weekly bonus for the top X holders, like [TACO](https://twitter.com/Taconomics101), or double rewards every Tuesday because Taco Tuesdays are REAL!
4. For some, the **main value stems from the community angle** rather than the tokonomics, like for [Shrimp](http://shrimp.finance/) which ambitions to become more community-driven than other similar projects by enabling the creation of advanced pool (incentivised in SHRIMP) by anyone.

{{< notice tip >}}
If you want a common thread to filter the noise, **governance is a good one. It's a necessity and ultimately a key factor in the success of all these projects**. Look at the kind of decisions that are made, what is the process, and who is shaping the project, ect.
{{< /notice >}}

---

So there you have the base concept and it's so simple and plug and play that we **could create a foodcoin together for the fun**:

Picture $WINE. You farm it by locking DeFi tokens for the first week. Then a WINE/ETH pool will be incentivized for longer (high potential to be a dumping pool, more on this below).

WINE is already highly memable and has an emoji, good starting point! However we need more, we need some fun and stickiness to it, how about:

1. The top holder has a 20% chance of getting "Drunk" daily. If that happens, he will be a generous drunkie donating 20% of all his WINE to 100 random daily active addresses.
2. Don’t get too tipsy either: each WINE transaction has a 1% chance of sending 50% of the value transferred to the reward contract instead - increasing the rewards for farmers.

Those mechanisms are profoundly uninspired, but they give you a picture of how easy those concepts are to come by. They can also be implemented very quickly thanks to code blocks (such as the staking contracts) forked from standards (such as Synthetix staking contract).

{{< notice warning >}}
$WINE does not exist. DO NOT buy $WINE. DO buy wine! 🍷
{{< /notice >}}

---

Enough for the context and the theory - I might dive into the community dimensions of the game in the next post. But for today, allow me to share some practical wisdom on these games earned sweating my gwei out:

### Practical tips if you are playing food-based moneygames

**First and foremost, mind the gas!** Farming the meme-food coins usually require you to at least stake and then claim/exit. Depending on the pools you are farming you might also have to add liquidity to decentralized exchanges - making the position more intricate and costlier to unfurl.

**Secondly, NEVER BUY THE FOOD TOKENS - farm them.** Buying such a token is taking on an incredible amount of risk - you are against an army of people farming them for free who can be eager to dump.

Finally, let's get a bit more practical by looking at real examples to explicit the risk scenario of each farming pool types: 


#### LEVEL = 1 - ERC 20 STAKING POOL - OK IF THE CODE IS SAFU

With such pools, you stake a DeFi token (usually MKR, COMP, SNX, LEND, wETH and YFI) to earn the meme food token, YAM for instance.

The risk is minimized: if you can compare the staking code with an existing one to ensure there are no shenanigans. Since you're simply staking and not providing liquidity - you're not taking any economic risks. As long as you can ensure the safety of the protocol - your farm capital is not endangered.

Past this point (SAFU confirmed), the main risk you are taking is that the coin you are farming might be worth little to nothing by the time you have enough to dump. Stick to reasonable projects to avoid such a scenario known as as the "death spiral" - when a meme coin enters the final phase of its existence:

![defi-moneygames-PASTA-deathloop](/img/2020/defi-moneygames/pasta-deathloop.png "The end of PASTA was quite abrupt.")


#### LEVEL = 2 - 98%/2% POOLS

These pools are usually more tricky, as they involve providing liquidity to a decentralised exchange. Often, they are heavily skewed towards a sound & reputable token: for instance, the YFLink 98% aLINK / 2% YFL pool.

Here, **you are facing a new type of risk: impermanent losses.** IL are greatest when the two assets involved in the pool are moving fast in opposite directions, price-wise. 98/2% pools have their own category because they are a bit safer, although they are not fully immune to IL.

![defi-moneygames-YFV](/img/2020/defi-moneygames/yfv.png "YFV is another moneygame following the 98/2 pool model")

#### LEVEL = REK'T - THE DUMPING POOLS

These pools are the MOST dangerous. I'd advise anyone needing guidance to simply avoid them - the game is too risky to be played. A great example of why is the PASTA yyCRV / PASTA Uniswap pool.

Let's put it like this: if some can farm PASTA essentially for free by locking some DeFi tokens - why would they not dump them all for yyCRV, the soundest money-making machine of the industry? That is precisely what happened. 

As soon as the incentivised pool launched, PASTA farmers dumped heavily to claim those precious yyCRV fools put up for grabs. Why would they not? The price of PASTA tanked from roughly $1 to $0.04, butchering any profit made by those who committed to the pools on top of them losing their precious yyCRV.

So what qualifies a pool as the dumping pool? **Allow me to be super explicit here to make sure you're not going hara-kiri with your precious tokens**:

1. **The dumping pool is usually 50/50**: 50 of the meme shitcoin, 50 of a sound asset like ETH, wETH or yyCRV.
2. **The dumping pool is incentivized with a high budget**- how else would you get plebs to commit? Of course, this profit is hard to realise as most of the capital is lost to IL, and the returns are earned in the foodcoin which can enter the death spiral.
3. **The dumping pool usually launches a few days after the first ones**, and last longer. Indeed, you need to give a few days for the farmers to accumulate.

Don't trust me, I'm just a simple farmer - follow a legend like [DegenSpartan](https://twitter.com/DegenSpartan/status/1296619171984232448?s=20) - he's nice enough to announce his dumps publicly (shortly) after they started.

Best of luck, and remember one thing if you recently joined the space: the food money games are played against experienced traders with years of crypto experience. 

{{< notice note >}}
Most are 0 sum games: no value is created, it's just a complex 3-4 layers value transfer mechanism.''
{{< /notice >}}

**Are you confident enough in your experience to venture into the lions' den?** If not, stand clear of anything past the basic staking pools.

---

{{< notice info >}}
I am not a financial advisor - you make your own decision. I have no formal training or certification when it comes to investing. I'm merely sharing my personal experience with decentralised finance services, with the goal of helping my peers to better understand the value provided by such services.

**I am NOT responsible for <u>YOUR INVESTMENT DECISIONS</u>**, may they bring you Lambos or bankruptcy.
{{< /notice >}}
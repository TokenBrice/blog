---
title: "🎚 ETH exposure or DeFi yields: why choose?"
description: "A pratical perspetive looking at Maker as a solution to maintain an ETH exposure while providing extra capital to harness DeFi yields."
date: '2020-08-03T01:13:50.191Z'
categories: [🌌 DeFi, 💸 Practical]
tags: [DeFi, Ethereum, Lending, Maker, Lending, Leveraging, Minting DAI]
toc: true
tocNum: true
image: /img/2020/leveraging-ETH/leveraging-ETH.png
---

As the Ether giant seems to be waking up, you might be considering your **options to recenter your exposure on ETH**. This is precisely what I've been looking at and executed on lately, and now is the time for the feedback session! 

Indeed, DeFi is heating up and yields are attractive. However, **even crazy liquidity mining returns (on stablecoins) might not beat the ETH price appreciation once its time comes.** So, instead of having to choose, why not have not both?

With this one goal in mind, the most obvious solution was [Maker](http://makerdao.com/). The position can, of course, be achieved using other services; I consider them at the end.

So there you have the base idea: instead of investing directly in ERC20 or stablecoins and putting them to work, you maintain an ETH base, use it to generate DAI and then diversify into your positions. This way, you maintain a healthy ETH exposure - the tradeoff being the additional risk, including liquidation that are discussed below.

## Re-investing the minted DAI

The options to re-invest your DAI are pretty much infinite, so I will focus on these that make the most sense - aka the best at harnessing the current DAI premium. Feel free to check my previous publications covering incentivised liquidity pools investment opportunities & the useful tools to harness them:
1. **[💦 The Yield Farmer Tier List](https://tokenbrice.xyz/content/posts/2020/yield-farmer-tier-list.md)** 
2. **[🧰 The DeFinancial Farming Toolbox](https://tokenbrice.xyz/content/posts/2020/defi-farmer-toolbox.md)**.

So essentially when it comes to what makes of the DAI, you have several options, here are the broad categories:

*   **SIMPLE STABLECOIN RETURNS** - Put your DAI to work, with a simple deposit on Compound or Aave, or using a yield optimiser.
*   **ADV. STABLECOIN RETURNS** - Invest in Curve Ypool for decent returns + extra earning opportunities on your pool tokens.
*   **ERC20 EXPOSURE (+LP)** - Purchase ERC20 tokens and hold or purchase ERC20 tokens and provide liquidity.
*   **MORE ETH LEVERAGE** - Use the DAI to buy more ETH. Can be potentially repeated for more leverage (CAREFUL). This obviously makes the most sense when you're expecting positive price action on ETH.

DAI is currently trading at a premium ($~1.03), some strategies are better than others to harness the impact of this spread. I detail them in the last section.


### Vault Management: How to Increase Gas Efficiency?

When it comes to making sure you're not burning yourself on the gas costs, I've already covered several critical tools that we won't detail again, such as [Zapper.Fi](http://zapper.fi/), or [ParaSwap](http://paraswap.io/) for some token swaps. Today, I want to discuss services that are helpful to manage Maker vaults.

1. While interacting with your vaults, you'll find yourself make series of transactions (deposit ETH -> mint DAI -> do something with the DAI). To reduce your gas costs, you can **use [FuruCombo](https://furucombo.app/) to build your series of operations and execute it in one transaction.**
2. You might find yourself in need of a "flash capital" to close a position somewhere and re-open it somewhere else. If that's the case, an Aave flash loan will be useful. Now for the best part: **flash loans are available on FuruCombo!**

![Collateral swap using Furucombo](/img/2020/leveraging-ETH/furucombo.png "ETH -> USDC collateral swap using FuruCombo.")

Keep in mind that in these times of high gas cost, each interaction is costly. To reduce the impact of gas on your strategy, try to minimize the amount of operations you're doing - FuruCombo is simply amazing for that!

If you have many positions to close/open, you might also want to wait for an opportunistic time to do so, where gas costs are low. The weekend evenings (Europe time) are usually best.


## 🚨 PLEASE READ: How to not get liquidated?

### Understanding Maker's Liquidation Mechanism

When you get liquidated, (a part of) your collateral is seized to cover your debt. **The existence of liquidation on Maker means you could lose potentially all of your ETH** if you are careless.

Here are my tips and recommendations to make sure this does not happen to you:

**If you are just starting with leverage, maintain a very healthy collateralization ratio**. I’d recommend > 300 % for new users, simply for peace of mind during your discovery phase.

**Don't put all of your eggs in one basket**: on Maker, you can open as many vaults as you want. While you don’t want to open hundreds of positions to keep the gas costs in check, you might also want to consider splitting your stash to not put all of your ETH under the same risk and be able to more gradually manage the positions as they grow.

**Easy Vault Management**: if you'd like a less stressful approach, you can use [DeFiSaver](https://defisaver.com/) to make sure your vault is automatically kept at a certain ratio with the Save function.

![Automating Maker Vault Management with DeFi Saver](/img/2020/leveraging-ETH/defisaver-automation.png "Automation Options on DeFi Saver.")

### Advanced Vault Management

If you have several vaults, you can use a tool to re-distribute capital between them in one transaction, again with FuruCombo:
```
Mint DAI on Vault1 (currently safe) 
> Burn DAI on Vault2 to lower its risk
```

Using a flash loan, you can even fully close a vault “into” another vault for instance:
```
Flash loan DAI (=debt of Vault-1) 
> Burn on Vault-1, to free the ETH 
>> Deposit the ETH in Vault-2 (the one you keep) 
>>> Mint DAI on Vault2 
>>>> Pay back the flash loan.
```

**Be mindful with what you do with the DAI you mint: it's a debt.** Prefer safer investment options. If you invest in something stupid & get rekt at the same time the ETH price is depreciating, you could be putting your ETH at risk.


## Why Maker is the best service to leverage ETH right now

I decided to focus this article on Maker only, considering the angle is to leverage ETH and Maker is currently the best platform to do so, as well as probably the safest (running track record). Here are my main three reasons:


1. **Fits the bill** - It enables you to keep an ETH exposure while generating extra DAI to re-invest.
2. **0 fee if not liquidated - (⚠ gas costs)** The current stability fee is 0 (on ETH) - it costs you nothing but gas to open a position on Maker.[^1]
3. **DAI Premium -** DAI is frequently trading at $ 1.02-1.03 meaning minting DAI can result in a 2-3% instant profit on the amounts reinvested (more on this later - DAI premium section).

Please keep in mind that **this is NOW**, several weeks from now there might be better options for such positions, as Aave implements its new tokenomics for instance. A similar position could already be achieved today using Compound, but it doesn't seem profitable to do so right now (vs Maker).


## Who is this strategy for?

Since it's quite a flexible strategy, **it can be used by pretty much anyone owning ETH and looking for a way to put them to work.** However, allow me to highlight some use case scenarios that should give you ideas:

1. You've entered the markets recently (2019), and made profits but not really on ETH. While your ERC-20 positions are up, you might be wary about missing on ETH gains. To increase your exposure to ETH, you could settle some of your positions to ETH, open a vault, and reopen up to ⅔ of the closed ERC-20 positions.
2. You've been harnessing neat gains on the stablecoins farming lately, but even the best yields can't beat a waking giant. You might consider buying ETH with your stablecoins, to then open a vault and reopen part of your stablecoin position - you keep some of your yields while adding a sweet exposure to ETH's price.

### Harnessing the DAI Premium

To conclude, let's consider the best options if your goal is to make the most of the current DAI premium - what does it impact most?

Obviously, it's very nice for ETH-leveraged long. Indeed, if DAI trades at $1.03, buying ETH from DAI is more efficient.

If you are considering investing in the Curve y pool, I'd recommend going 100% from DAI. You'll save gas cost massively on the swaps that are not required (+ less deposit and approve tx). On top of these savings, entering the Curve y pool fully in DAI usually has a positive price slippage.

Currently it sits ~1.5% over 5000 DAI: that is 1.5% instant profit as you enter the position, quite attractive right?

![Curve DAI Premium](/img/2020/leveraging-ETH/curve-dai-premium.png "Positive slippage while entering the y Curve pool full DAI")

Depending on your risk preference and your capital, you might want to time your entry. I was able to harness up to a 3.5% positive bonus entering the ypool, so waiting can be worth it!

Thanks to Grégoire for proof reading this content & [Jimmy](https://twitter.com/jimmyragosa) for suggesting [DeFiSaver](https://defisaver.com/), try it out!

## Key Takeaways

1. You can **[put your ETH to work](http://oasis.app/)**, without selling them! Try out with a first safe (>300%) position.
2. Liking it? Start exploring other strategies but remember to account for gas costs. Use **[FuruCombo](https://furucombo.app)** to build more complex flows.
3. Using vaults more and more? It might be a good time to consider **[DeFiSaver](https://defisaver.com/)** to reduce your risk and manage your vault without stress.

[^1]: [The Stability Fee is now = 0](https://twitter.com/MakerDaiBot/status/1290243544670785536) for all collaterals on Maker.
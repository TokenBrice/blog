---
title: "🌽 Defi money markets cookbook"
description: "Money markets like Aave or Alchemix are essential in DeFi. This article explains and illustrates some strategies to take advantage of the different options they offer."
date: '2021-05-10T01:13:50.191Z'
categories: [🌌 DeFi, 🔮 Discovery]
tags: [DeFi, Ethereum, Decentralized Finance, Money Markets, Aave, Curve, Liquity, Mimo Capital, Alchemix, Aave, Polygon, Liquidation]
toc: true
tocNum: true
url: money-market-recipes
---

On this blog, I frequently discuss about money markets and assets market in DeFi. Basically, they allow you to **loan and borrow tokens**. These two actions have become like **deFi verbs**: they are used directly or indirectly in almost every strategy.

So while it is crucial to understand the protocols you are using and especially **the different [money market risks]({{< relref path="/content/posts/2021/money-market-risks.md" >}})**, Today, I would like to focus on the why and the how:

1. Which strategies can be implemented using money markets?

2. How can they be deployed in practice?

We're going to break down different "recipes" to take advantage of the money markets. Take these recipes as **inspiration to develop your own strategies**.

![money-market-recipes-cover-tokenbrice](/img/2021/money-market-recipes/money-market-recipes-cover.png)


{{< notice warning >}}

**This article does not constitute investment advice: I am not authorized to dispense it. Rather than mechanically reproducing the strategies presented as examples, I invite you to try to understand the approach.**

{{< /notice >}}

---
## Leveraged bets on a money market via the market itself


Every money markets have an associated token, for example the AAVE token for Aave. It is generally used for the governance of the protocol and sometimes also allows to capture part of the value it generates. With this strategy, we will **use a money market to borrow assets that will then be used to gain exposure to the native token of the desired platform**.

* **⚙ Condition:** Optimism about the future of a given money market. It's native token in this scenario is expected to appreciate in line with the growth of the market over the medium/long term.
* **📅 Time horizon:** 3 - 24 months. ~3 months is a recommended minimum so that gas fees and borrowing costs don't impact the returns of the strategy too much.
* **🔮 Expected result**: the acquired token appreciates, which allows to pay back the debt (+ possible interest) at term by reselling part of the initial position. Once the debt is repaid, part of the acquired tokens can be kept. 
* **🃏 Bonus / Facilitator:** If the token in question can produce a return (e.g. AAVE in the Safety Module), this will allow the debt to be repaid even faster or to accumulate "free" tokens if the scenario of its price appreciation is verified.

Although this strategy is quite basic, it is one of my favorites. I recently shared with you on Twitter an example of how to put it into practice, which we will detail here:

<div align ="center">

{{< tweet 1385873962404614144 >}}

</div>

Here, the concerned protocol is [Liquity](https://liquity.org) and the implementation of the strategy is quite simple, but has two variations:

### Direct exposure to the native token

Either by directly exposing yourself to the LQTY token, which is of course more risky:

![mm-long-tokenbrice](/img/2021/money-market-recipes/mm-long-token-tokenbrice-en.png "Long exposure on Liquity via the native token LQTY")

---
1. Deposit ETH on [Liquity](https://www.liquity.org/) via one of the frontends, they will serve as collateral for the position.
2. Borrow LUSD
3. Swap LUSD (via ParaSwap for the best rate!) for LQTY, the native token of Liquity
4. Stake LQTY, which generates LUSD and some ETH
5. Eventually repayment of debt (2) via LUSD yield (4) and resale of some of the LQTY acquired in step 3 after price appreciation.


Or more conservatively, with a strategy using Liquity to borrow LUSDs and make them productive:

### Exposure mainly in stablecoins

![mm-long-token-tokenbrice](/img/2021/money-market-recipes/mm-long-tokenbrice-en.png "Long exposure to Liquity via Liquity/Curve")

1. Deposit ETH on [Liquity](https://www.liquity.org/) via one of the frontends, they will serve as collateral for the position.
2. Borrow LUSD
3. Stake LUSD via either the Stability Pool (-> LQTY + ETH) or the LUSD pool on Curve Finance (-> Native + LQTY + CRV).
4. Eventually repayment of debt (2) via yield (3)

{{< notice note >}}
Yearn Finance also offers a LUSD vault that automatically manages the position on Curve.
{{< /notice >}}

---

## Investing time rather than money


Alchemix arrival has opened up new perspectives in terms of strategy. On Alchemix, the debt repays itself over time. Indeed, **the collateral used (yDAI) is a stablecoin that produces a return (via Yearn)**. Thus with the current conditions the loan is self-repaying in three years.

I suggest a simple strategy to take advantage of Alchemix to make a profit. The main drawback is that **only half of the amount of DAI initially placed in Alchemix can be borrowed in AlUSD** and then invested.
Nevertheless, as this strategy is based on stablecoins, it does not - (⚠ oracles) - involve any price risk and therefore does not require daily monitoring.

* **⚙ Condition:** DAI that will be locked in for ~3 years. Only half of the deposited amount is mobilizable.
* **📅 Time horizon:** ~3 years (depends on DAI return rate on Yearn).
* **🔮 Expected result**: In 3 years, the AlUSD debt is fully repaid and the DAI initially mobilized on Alchemix are free again. It remains to be seen what happened with the investment made with the borrowed AlUSD: it all depends on the choices made, I do not predict the future.
* **🃏 Bonus / Facilitator:** Use the borrowed AlUSD to invest in a token that can produce a return. This allows you to make a compound investment or even pay off Alchemix debt faster.

### Long ALCX via Alchemix

To illustrate the concept, I propose another simple strategy which is equivalent to long Alchemix via its token ALCX :

![alchemix-investment-tokenbrice](/img/2021/money-market-recipes/alchemix-investment-tokenbrice-en.png "Investment financed by a stable debt on Alchemix")

1. Deposit DAI as collateral on Alchemix. Alchemix deploys it on Yearn Finance to generate a return.
2. Borrow up to 50% of the initial value deposited in AlUSD, a stablecoin.
3. Invest the AlUSD in the desired token. Here for the example it is ALCX the native governance token of Alchemix.
4. Stake the acquired token to produce a return
5. The repayment of the debt in AlUSD contracted on Alchemix is done automatically with time. It is possible to repay in advance thanks to the generated returns (4).

---
## Putting a "hodl" collateral to work over the long term

I came to DeFi several years ago with a simple ambition: I wanted to put my Ethers to work. At the time it was not an easy task but nowadays there are many very interesting solutions. I will focus on one of them, Aave, for two reasons.

1. Aave has launched **a liquidity mining** program paid in StkAave[^aaveLMmainnet] (Aave V2 - Mainnet).
2. Aave is accessible on the **sidechain Polygon** where the low fees allow to deploy DeFi strategies efficiently even with small capital. There is also a liquidity mining program there, in MATIC [^aaveLMmatic].

To make this strategy as accessible as possible, we will develop the example on the Polygon sidechain. It is therefore possible to use any of the tokens supported as collateral on the Aave/Polygon market: MATIC, AAVE, wETH, wBTC, USDC, and DAI.


### How-to


The strategy is to **produce returns through the borrowing of stablecoins used to provide liquidity on the Curve exchange service**. With the liquidity mining program on Aave, every step of the process is potentially lucrative at least in MATIC.


* **⚙ Condition:** Having tokens accepted as collateral on Aave, and bring them back to Polygon for example using [the POS bridge](https://wallet.matic.network/bridge/).
* **📅 Time horizon:** Short / medium term.
* **🔮 Expected outcome:** Returns in MATIC, stablecoins and ETH.
* **🃏 Bonus / Facilitator:/**. Prospective: mining CRV & potential leverage when LP Curve Polygon tokens are accepted as collateral on Aave.

### Putting ETH to work on Polygon

To illustrate this strategy, I start with the assumption of generating a return from ETH.

![polygon-aave-curve-eth-farming-tokenbrice](/img/2021/money-market-recipes/polygon-aave-curve-eth-farming-tokenbrice-en.png "Farming on Polygon via Aave and Curve using ETH as collateral")

1. ETH deposit as collateral on Aave/Polygon (+native +MATIC)
2. Borrowing stablecoins (-APR +MATIC)
3. Deposit and staking of stablecoins on Curve/Polygon (+natif +MATIC)

Note that Curve LP Polygon tokens are being considered for potential addition as collateral in the Aave market. We can also expect potential CRV rewards on Polygon LP positions if the DAO decides to do so.

{{< notice note >}}
It is possible to implement this strategy by keeping the tokens used as collateral on the L1 Aave in order to benefit from the mining of StkAAVE. It will be necessary to migrate the borrowed stablecoins from the Ethereum network to Polygon using for example [Matic's POS bridge](https://wallet.matic.network/bridge/).
{{< /notice >}}

---

## Protect yourself against the price risk of the $: farming in €.

In DeFi, everything is done in dollars. It makes sense, everyone knows, but for a European user it is a significant additional  risk. Indeed, if your ambition is to generate enough to live on with DeFi, then this means your output will eventually be in Euro.

![eur-usd-1y](/img/2021/money-market-recipes/eur-usd-1y.png "Evolution of the €/$ exchange rate over the last year")

For a European farmer, it may therefore be **interesting to have a DeFi exposure in € to avoid this risk**. At the moment, there are simply no Euro borrowing options other than [Mimo Capital](https://mimo.capital/).

This service allows you to borrow PAR from ETH, wBTC or USDC. The MIMO governance token is also distributed to owners of active vaults as well as to liquidity providers on the PAR/ETH and PAR/USDC Balancer pools.

Nevertheless, the protocol is still recent and the PAR token is not yet supported in the ecosystem, as a collateral on Aave or in a Curve pool for example. So the situation is not yet ideal but it has the merit to exist!

Other DeFi-€ solutions are in development. MakerDAO, for example, has mentioned a Euro-DAI, while Jarvis Network is working on a synthetic stablecoin €, the jEUR.

### How-to

To farm natively in Euros, the best option is still what you can do with EURS. Since the launch of the pool on Curve, there are many options.

*  **⚙ Condition:** Owning EURS / sEUR
* **📅 Time horizon:** 1 month - years
* **🔮 Expected result:** Growing a capital in Euro-stable
* **🃏 Bonus / Enabler:** Owning VeCRVs.

![EURS-farming-tokenbrice](/img/2021/money-market-recipes/EURS-farming-tokenbrice-en.png "Farming with the EURS stablecoin")

* The **pool Curve** directly offers an attractive yield in CRV even when it is not boosted.
* To automatically sell the farmed CRVs to compound the return, a vault is ideal. **[Yearn](https://yearn.finance) offers a vault on EURS**.
* Farming is also possible via the EURS vault of [StakeDAO](https://stakedao.org/), in order to accumulate SDT as well.
* Or [Harvest](https://harvest.finance) also offers a vault that makes up the bulk of the returns while paying in FARM.

---

I hope these different recipes will inspire you. Make sure you are **[aware of the different money market risks]({{< relref path="/content/posts/2021/money-market-risks.md" >}})**, used for all these strategies.

*🙏 Huge thanks to HHK, Charles, Thomas, Erwan & FrenchTony for proofreading the French version of this article and translating it integrally into English.*

---

[^aaveLMmainnet]: The liquidity mining program StkAAVE was launched on Mars 26 following a governance vote. [More info here](https://twitter.com/AaveAave/status/1386753673104134155?s=20)
[^aaveLMmatic]: Polygon sponsors a liquidity mining program in MATIC, both on [Aave](https://blog.polygon.technology/defiforall-kicking-off-l2-defi-summer-with-40-million-usd-in-liquidity-mining-rewards-from-4937d7c6e287) and [Curve](https://blog.polygon.technology/continuing-scalability-defi-summer-with-5-million-usd-in-liquidity-mining-rewards-from-polygon-e73a76c5a8ad?gi=9a7b7e130606)
---
title: "🍷 Yields are like fine wines, the secret lies in the brewing process"
description: "An introduction to Fixed Interest Rate Protocols (FIRPs) through the lense of APWine to better understand what they enable and bring to DeFi."
date: '2021-02-11T01:13:50.191Z'
categories: [🌌 DeFi, 🔮 Discovery]
tags: [DeFi, Ethereum, Decentralized finance, DEX, Money Markets, Aave, Compound, ApWine, 88MPH, Fixed Interest Rate Protocol, FIRP]
toc: true
tocNum: true
url: fixed-interest-rate-protocol-firp-apwine
image: /img/2021/firp-apwine/pac-man.png
---

Yields are like fine wines, the secret lies in the brewing process. As DeFi is developing faster than ever, with now more than $ 50 billion of total value locked across all protocols, **the yield offering is diversifying**.

Our topic today strikes at the heart of this trend, with a solution offering a potentially instant payout for deposits on DeFi protocols like Yearn or Aave: APWine. Before we get to this point however, we need to place back some context on money markets and FIRPs in general since they are still novel types of products for most DeFi users.

---

## Money Market = PacMan

![the interest bearing stablecoin pacman-tokenbrice](/img/2021/firp-apwine/pac-man.png "Several abstraction layers are building up on top of money markets - will they soon be part of the native experience?")

Tranching, insurance, and FIRPs are essentially like **abstraction-layers built on top of a money market** to provide additional features:
1. **🔪 Tranching** ➡ better separation of the different type of risks
2. **🛡 Insurance** ➡ coverage against technical failures (& more!)
3. **🔮 FIRPs** ➡ "coverage" against variations of APY

While they are interesting as a features by themselves, what fascinates me is what happens **when/if they are integrated at the base level**. It would enable other protocols to harness these features. For instance, Harvest could offer a "de-risked" USDC vault & essentially bringing the whole DeFi to another level. 

Indeed, DeFi's different value set is not only a benefit for transparency and audibility: it's **also at least <ins>an order of magnitude</ins> more efficient** than the dying patchwork of finance it's bound to replace.

---

## Fixed Interest Rate Protocols (FIRPs)

Before we start, let's define what Fixed Interest Rate Protocols are and what are their role within the broader ecosystem of decentralized finance on Ethereum. 

With DeFi, the goal for most is **to produce yields from a given asset.** Usually one of the easiest ways to achieve this will be to lend it for instance, for a return. Doing so means assuming several layers of risk you can insure yourself against (-> Unslashed) or simply avoid taking with tranching (-> Saffron).

Even if you're super responsible and try to insure & further protect your deposits, you are left with one sizable issue: **the base return produced by the asset is usually volatile**, making the pricing of the whole package (lended deposit + insurance + tranching) hard to navigate.

![coingecko-crypto-2020-report](/img/2021/firp-apwine/coingecko-report.png "CoinGecko highligthed the different approaches to FIRP as a growing subset of DeFi in the last report")

Check the [full report here](https://assets.coingecko.com/reports/2020-Year-End-Report/CoinGecko-2020-Report.pdf).

This is precisely where FIRPs get a chance to shine: **since they make the interest predictable, FIRPs help promote a more responsible attitude** for the whole space - by making it easier to use all the meta-structure now available to protect deposits on money markets or DeFi asset managers.

This article addresses fixed interest rate protocols only. For a broader perspective on risk management for DeFi deposits, **[read my introduction piece touching on insurance, tranching and FIRPs](https://tokenbrice.xyz/content/posts/2021/risk-tranching.md)**. In there, we addressed how insurance, tranching, and fixed interest might eventually be integrated natively into money-markets, enabling to **[envision "risk-free" interest bearing stablecoins](https://tokenbrice.xyz/content/posts/2021/risk-tranching.md)**.

From now on, this article assume a minimal understanding of the topic. If something is still unclear, please refer to the previous article ☝


## APWine: Fixed-yield Sauternes 🍷

So with the hell of an intro and without further ado, let's dive into today's matter: **understanding what FIRPs are and what they bring to the table through the lense of APWine**.

🍷 Even better, it's wine-themed and Frenchies are involved - what's not to love already?

### The difference between APWine and 88MPH

From a high-level perspective, both projects could be described as FIRPs, yet they achieve this result through different means:

*   With 88MPH, the yield of your deposits are fixed thanks to a secondary prediction market built for it.
*   With APWine, you can lock your assets for a month for instance to instantly earn the yield.

So to be more explicit, both are not interchangeable nor operating on the same time frame: with 88MPH, the income becomes **predictable but it's still an iterative process**. With APWine, the income becomes **predictable & instantly delivered**.

It also means different tradeoffs on the risk management side. With 88MPH, the yield is calculated algorithmically - there's always a buyer, which is neat for convenience, but also means the protocol can accrue debt if there is a mismatch.

The opposite is true for APWine: since it's market-based, no mismatch can occur (-> no protocol debt), but it means there can be demand/offer issues (such as heavy discount on FYTs).

![apwine-deposit-process](/img/2021/firp-apwine/apwine.png "The deposit process on ApWine explained (source: official website)")

### APWine: Instant Payday?

With APWine, the logic is quite straightforward. It all starts by depositing a token earning some yield, such as a stablecoin deposited on Aave or a Yearn vault token onto the platform. 

At the beginning of each period, users receive FYT (Future Yield Tokens) representing their yields for the period. **The FYT are standard ERC-20 tokens** that will be tradable shortly after launch on APWine.

The deposit is locked for the period, however users can withdraw early with a fee, by burning their FYT tokens. The slashing is deactivated for the beta period.

Since the yield is instantly available and usable, APWine should provide ample opportunities for both hedging and arbitraging. 

{{< notice note >}}
After several weeks of testnet, APWine is coming to mainet! The beta will start in a couple of weeks with a first period starting on March 1st for 30 days. The APW token and liquidity mining should could shortly after. 

**[More information on APWine beta & launch](https://apwine.medium.com/our-beta-is-live-on-the-ethereum-mainnet-3860491a365c)**.
{{< /notice >}}

## What's next for APWine?

In the short term, I'll be following closely the upcoming launch of the platform next week. Several upcoming releases have already been announced such as the arrival of more services and pools on the platform and the release of the APW token and its associated liquidity mining plan.

Like always though, what gets me really excited is the endgame!


### The Endgame: a yield hedging protocol

Before we envision the end-game here, first we need to see if the idea works and **if there is a real fit.** In the APWine case, **success will be measured by looking at the health of the markets for FYT tokens**. I don't expect them to settle at parity with expected yields, but if users can really get an **instant payday even with a 20% fee**, I'm sure there will be demand. 

Achieving this means having really liquid FYT markets, which is perfectly doable especially if there is a liquidity mining plan in APW token to bootstrap them. Regarding the APW token itself, diving in the FAQ will give you a bit more insight into what the team envisions:

> At each future expiration, 10% of the generated yield is shared between all APW token holders (percentage subject to change in the future based on the market demand). The token will also enable them to participate in the governance mechanisms of APWine.
> 
> - Source: [ApWine FAQ](https://apwine.fi/faq)

So on top of the usual governance right of the protocol, it seems like there is already a revenue stream considered for the APW token, on top of any potential liquidity mining plan involving an APW-based pair.

---

French being the language of DeFi, it was about time we got some fine wine-makers involved in the yield brewing process! If you are interested in the protocol, you can **[read more about the beta here](https://apwine.medium.com/our-beta-is-live-on-the-ethereum-mainnet-3860491a365c)**.

I'll be following closely as I'm having **[a chat with Antoine](https://www.youtube.com/watch?v=Zo0B64swtPI)**, one of the persons involved with APWine next week (in French).

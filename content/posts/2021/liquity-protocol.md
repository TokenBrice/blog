---
title: "⚖️ Liquity: an unstoppable, efficient and innovative borrowing service"
description: "Liquity is the first borrowing service that operates without the need for governance, while being low cost and highly efficient. I explain the protocol to understand how it innovates and what it brings to DeFi."
date: '2021-12-02T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Understanding]
tags: [DeFi, Ethereum, Decentralized Finance, Stablecoins, Borrow, Liquity, LUSD, LQTY]
toc: true
tocNum: false
url: liquity-protocol
---


[Liquity](https://www.defiscan.info/protocols/liquity/ethereum) is still a unique protocol: it allows borrowing on ETH and mint of a stablecoin (LUSD) without requiring governance which makes it "unstoppable".

The term is not always well understood, so let's make it clear: the contracts necessary for the existence of Liquity and LUSD have been deployed and since they have no administrative functions, **nothing can stop them as long as the Ethereum network is synchronizing**.

If that's not enough to excite your curiosity, the good news is that to achieve such a result, Liquity implements several new ideas that are really relevant. Indeed, in addition to its resilience, Liquity is also **the least expensive** protocol for long term borrowing on ETH and also **the most permissive in leverage**, outside of recovery mode.

The purpose of this article is therefore to introduce Liquity while expliciting several critical dimensions for any loan/money market service in DeFi.

![liquity-cover-tokenbrice](/img/2021/liquity-protocol/cover-en.png)

## OPERATION OF THE PROTOCOL

I propose an exhaustive tour of the protocol to understand the issues and contributions made to DeFi. Ideally, it would be to understand all the dynamics. However, I realize that my explanations can sometimes be dense, so I will offer them by level of complexity:

### 🏗 Liquity's fundamentals

At a high level, Liquity works in a similar logic to Maker: users create "Troves" where they can deposit ETH in order to borrow stablecoins, LUSD, directly from the protocol.

#### Money market or loan service?

Both Liquity and Maker are borrowing services but not money markets. What's the difference? Who is lending to you? 
1. Either the protocol directly (borrowing service), 
2. Or other users via a pooling model like Aave or Compound (money market).

The difference is extremely important in terms of the competitiveness of the protocol: **it is almost impossible, even theoretically, to envision a money market offering low stablecoin borrowing costs (&lt;3 or 4% annual) on a sustainable basis**.

This is because money markets need to offer an attractive return to their stablecoin depositors, who have many, many alternatives for generating returns. Thus, **if efficiency is a key objective, the borrowing service model that does not require deposits from other users is inherently more efficient** - the user borrows directly from the protocol at a lower cost.

Finally, let's test the theory against the hard absurdity of practice: these considerations are valid for analyzing the design of a money market / borrowing service. There are **borrowing services (which are supposed to be very efficient) which nevertheless manage to be expensive for borrowers, like MakerDAO**. The reasons for this are various, but the fact that the DAO still decides on the protocol fees (potentially in a totally arbitrary way) seems to me to be one of the main ones.


#### Borrowing with Liquity

From a potential user's point of view, Liquity basically works as an alternative to Maker or something else: the user arrives with ETH that he deposits in his trove to mint the desired amount of LUSD.

However, the parallel stops here because although at a high level the process is similar, the underlying logic is totally different.

##### Fees management

First, the crux of the matter: borrowing costs. On this subject and in addition to very low absolute borrowing costs, Liquity has the merit of bringing **predictability and clarity.** Indeed, where Maker, Aave and Compound for example practice a variable annual rate (via governance for Maker, market conditions for Aave/Compound), **at Liquity the rate is fixed and clearly announced at the time of the loan**.

In addition, at Liquity the fees are paid in one go, at the time of the loan's implementation: these are the "**initiation fees", by default at 0.5%**. This is the only fee that the borrower pays, even if he keeps his trove for years.

![liquity-trove](/img/2021/liquity-protocol/trove.png "Trove's opening on Liquity")


This is why Liquity is **ideal for long term positions**, such borrowing costs are effectively 5-10x lower than what you can find on the main alternatives.

#### Stability pool: liquidations backstop


While Liquity's model already provides relevant benefits from a user's perspective, its design also explores relevant solutions. 

One of the main issues for borrowing services is of course that the protocol remains solvent: there are therefore, if necessary, liquidations to restore the balance. Liquidation of positions requires equity and a certain infrastructure when it is the users who do it directly, as on Marker or Aave. To optimize the process, the idea of a liquidity "backstop" has emerged.

It is about having **a reserve of funds, generally stablecoins that the protocol uses if necessary to manage liquidations**: it is the Stability Pool on Liquity. The users who wish to do so can deposit their LUSD in this pool: they are remunerated in LQTY (which we will detail next).

The funds in the Stability Pool are used when necessary for liquidations. As the system is now quite mature, liquidations tend to happen mostly in case of a sharp drop in the ETH price. A position in the Stability Pool therefore allows one to profit from these juicy liquidations without having the skills or infrastructure to execute them.
 
The Stability Pool thus offers a rather gas-light and attractive native return option on the LUSD. With a conservative collateralization ratio, it may even be suitable for an almost entirely passive position.

Although the backstop concept is not implemented natively in the other major money markets, [the B.Protocol project](https://www.bprotocol.org/) acts as an abstraction layer offering the equivalent of this service to Maker, Aave and Compound (without the benefits of having it in-house).


#### LQTY token & staking

I told you above: Liquity has no governance. The system automatically adjusts itself according to different parameters observed on the markets as we will see below. But then, what is the purpose of LQTY?

In its most basic form, it is an accounting mechanism for allocating the revenues generated by the protocol. LQTY can be staked to obtain LUSD corresponding to its share of the initiation fee and ETH from the redemption fee:

![lqty-staking-returns](/img/2021/liquity-protocol/lqty-staking-returns.png "Returns of LQTY stackers")

That's it for the essential points about Liquity and its main differences with the existing solutions. However, as always, the devil is in the details, so now that the basics are established, I propose to explore the arcana of the protocol.

### 🧙 Complete understanding and advanced use

So far, we have stayed as much as possible in the perspective of a potential user. For this section, we'll have to broaden our horizons to understand the subtleties of Liquity's design. Let's get started!


#### Risks & limits

Now that I have your attention, let's talk about risks: this is also part of the subtleties to understand and take advantage of Liquity.

##### 🔮 Dependence on the oracle

If you have been reading me for a while, this sentence will probably tell you something: "**the truth about money markets is what the oracle says**". The oracle is the device that allows to obtain the necessary data on-chain, to be used by smart contracts. The critical data in question here is the price of ETH in USD, which determines whether a given position is solvent or needs to be liquidated.

In this case, the choice is classic: the main stream used is [ETH/USD ChainLink](https://data.chain.link/ethereum/mainnet/crypto-usd/eth-usd), with a fallback to Tellor ([more info](https://docs.liquity.org/faq/stability-pool-and-liquidations#what-oracle-are-you-using-to-determine-the-price-of-eth)). ChainLink is very widespread and robust, but one has to be aware of the fact that a problem with the ETH/USD ChainLink stream can quickly lead to serious consequences on Liquity (and pretty much the whole DeFi).

##### ⚖ The LUSD against its $1 peg

LUSD is a stablecoin, it's great to mine it directly to push down borrowing costs as much as possible. But what about the stability of the LUSD?

Stablecoin pegging is a pretty dense science, so we won't necessarily go into detail, just the basics. The LUSD has various characteristics that allow it to establish a floor and a ceiling via arbitrage:


* Floor: the redemption mechanism: an LUSD can be redeemed against ETH via a mechanism that we will explore next
* Ceiling: the protocol guarantees an absolute minimum collateralization of LUSD with ETH at 110% under all conditions

Thus, although the LUSD is holding its peg at $1 relatively well, the fluctuations in amplitude are more consistent than on a centralized stablecoin.

![lusd-price](/img/2021/liquity-protocol/lusd-price.png "Price of LUSD over 90 days")

<!--Différentes situations extrêmes au niveau du marché (et donc du protocole) peuvent également amener à envisager un LUSD qui s'écarte plus ou moins durablement du peg. Dans l'ensemble, les mécanismes de stabilisation sont là pour ramener l'équilibre sur le long-terme.-->
 
Various extreme situations in the market (and therefore in the protocol) can also lead to the possibility of an LUSD that deviates more or less permanently from the peg. On the whole, the stabilization mechanisms are there to bring back the balance in the long term.

#### A "protocol-level" game


Liquity brings us to a very interesting notion that I call "protocol-level", for lack of a better word. It is about the possible interactions with the protocol whose consequences depend on the actions of the other players.

In a way and to use my favorite metaphor of MMORPGs :

1. **PvE = Player versus Environment (AI)**, in DeFi: simple farming & consequences of other players only secondary (e.g. dilution of yield when a 🐳 happens)
2. **PvP = Player versus Player** and that's not missing even in DeFi!
3. But the most interesting thing today is **RvR (Realm vs Realm)**. Here again there is fighting between players, but it is **a structured fight by faction**, with objectives to reach. The DeFi equivalent here is of course the CRV game on Curve!

We can see on Liquity some "protocol-level" mechanics that could be similar to RvR in this metaphor, so let's see how they work : 

##### Dynamic initiation/redemption rate

First of all, the most basic: fees. I mentioned above that the initiation fee is 0.5%: this is true, but slightly simplified. In reality this rate can vary between 0.5% and 5%: it is the `baseRate` that governs the fee paid on both loans and redemptions.

When Liquity is used heavily, the `baseRate` increases. This is also a defensive mechanism for the protocol, which otherwise could be "emptied" of ETH by arbitrageurs (massive redemption LUSD->ETH). The "decay" rate when the use calms down to come back nicely to 0.5% and I let you go see [the math behind it](https://docs.liquity.org/faq/lusd-redemptions#how-is-the-baserate-calculated) on the doc for the curious. 

{{< notice note >}}
Since the depositor pays his fees at the time of borrowing on Liquity, the evolution of the rate afterwards has no consequence for him.
{{< /notice >}}


##### "Recovery Mode": as terrifying as it is effective?

In normal use, **Liquity is the most permissive protocol for leveraging on ETH, tolerating a collateralization ratio as low as 110%** (~90% of the net collateral value is borrowed). This is out of line with what is found elsewhere in DeFi, some references on ETH:


* Maker offers collateralization ratios ranging from 58.8% for ETH-C to 76.9% for ETH-B (min collateral ratio of 130% to 170%)
* Aave is at 82.5% on ETH 
* Compound at 75%.


If the protocol can be so permissive, it is not because it takes more risks, but rather because several solutions are implemented to push users to re-collateralize when necessary: recovery mode and redemptions.

![recovery-mode](/img/2021/liquity-protocol/recovery-mode.png)


The recovery mode is a protocol-level game on Liquity: its triggering depends on the "Total Collateral Ratio" of the protocol: the ratio between the total collateral and the LUSD due. 

When this ratio falls **below 150%, the Recovery Mode is activated to restore the balance**: the minimum collateralization threshold for a trove falls to 110%. Risky users are thus invited to re-collateralize or pay off debt - and/or will be liquidated if necessary when the recovery mode is activated.

The recovery mode is not a surprise, however, since it depends on a parameter that everyone can easily follow. Such a system makes it possible to maximize the efficiency of the protocol most of the time, while quickly reverting to more conservative settings if necessary.


##### The redemption game

Finally, there is one last mechanism to detail: redemptions, an arbitrage mechanism to exchange LUSD for ETH.

Again, this is a protocol-level game: redemptions are made using the liquidity available in the users' troves. **When there is a redemption, the protocol starts by using the liquidity of the least collateralized trove on Liquity** and goes up as much as necessary.

Thus, being **the** least collateralized trove on Liquity is not a very enviable position, since your collateral is at risk of being used for redemptions. If this is the case, the user will lose ETH, but they will also see their debt decrease (in proportion to the LUSDs traded).

This mechanism pushes players to remain reasonable, even when the recovery mode is not activated: to avoid redemptions, one should not be the most aggressive. It is a sort of **regulation mechanism whose exact threshold depends on the average leverage appetite of the other players**: in other words, a very elegant design.


##### Decentralized front-ends

Finally, this may be a detail for you but for me it means a lot: **the Liquity team does not operate the application site**. Instead, they have made available a [Frontend SDK](https://docs.liquity.org/documentation/sdk) to help other developers operate an instance of a Liquity frontend themselves. There is also a kickback mechanism to encourage these integrators.

This approach allows Liquity to go even **further than other protocols in terms of decentralization** and to offer solid guarantees that at least one of the front-ends will remain available no matter what.

Liquity's uniqueness is just like the rest of the protocol: innovative, different, and truly relevant that you simply can't ignore.


## Liquity and LUSD in the DeFi ecosystem

I wrote this article because I see Liquity as an essential DeFi primitive and I'd like to help you understand why. I'm not the only one who understands what's at stake here, many protocols are interested in Liquity and LUSD in one way or another. Let's take a look.


### DeFi Liquity Integrations

First of all, there are the various protocols that integrate one or more parts of Liquity and thus offer new opportunities to LQTY or LUSD owners.


#### Liquity LUSD/LQTY and farming

[Harvest Finance](https://harvest.finance/) offers an LQTY vault based on staking: the LUSD and ETH obtained are frequently composed of more LQTY.

[Pickle Finance](https://app.pickle.finance/farms) proposes a similar product (pJar 0.98l) as well as a particular vault in partnership with B.Protocol to maximize the obtained LQTY:


![pickle-lusd](/img/2021/liquity-protocol/pickle-lusd.png "Vault LUSD B.Protocol on Pickle Finance")


The main source of liquidity for LUSD is the [Curve Pool](https://curve.fi/lusd), also available with Convex.

![visor-uni-lqty](/img/2021/liquity-protocol/visor-uni-lqty.png)


Liquity is also supported on [DeFiSaver](https://defisaver.com/), to manage leverage more easily and protect troves.

So much for the quick overview of the main integrations. DAOs are also interested in LUSD because it is the only unstoppable stablecoin.


### LUSD: A DAO cash snack?

LUSD's inherent properties have already earned it some attention in DeFi. For example, after accumulating a lot of liquidity on DAI and FRAX, Olympus turned to LUSD with the accumulation of LUSD and LP Sushi LUSD/OHM via the bond mechanism. LUSD is now one of the main assets owned by OlympusDAO ([stats](https://dune.xyz/shadow/Olympus-(OHM)).


![olympus-lusd](/img/2021/liquity-protocol/olympus-lusd.png)


The ohmies are not going to stop there: they love productive assets, and Liquity is not lacking in them: [the plan](https://forum.olympusdao.finance/d/177-tap-5-whitelist-liquity-lusd-stability-pool-and-lqty-staking) is therefore that the protocol deploys its LUDS in the Stability Pool to accumulate LQTYs which will also be staked.

There was even classic liquidity mining on the LUSD/OHM pair, but revisited. With Alchemist's [Crucible ](https://crucible.alchemist.wtf/)a smart contract wallet NFT to easily manage LP positions, a [35 day program ](https://www.liquity.org/blog/how-to-earn-rewards-on-the-lusd-ohm-pool-using-alchemists-crucible)was offered, with rewards in OHM, LUSD and MIST.

Other protocols seeking resilience, diversification and stability for their cash flow have also taken the plunge:



* Fei, a protocol offering a different type of stablecoin, has diversified its collateral into LUSD and now has over 50M LUSD: [Analytics Fei Money](https://app.fei.money/analytics)
* The Synthetix team is also interested in bringing the LUSD onto Optimism, which could help stabilize the LUSD.

[The top holder LUSD ](https://etherscan.io/token/0x5f98805A4E8be255a32880FDeC7F6728C6568bA0#balances) already has several DAOs and **as with RAI** I think the trend may grow:

![lusd-holders](/img/2021/liquity-protocol/lusd-holders.png "Top 15 LUSD holders on EtherScan")


Other integrations are still possible, like for example the direct integration of the stability pool on a pool fuse to allow a more optimal use of the stability pool's assets.

I hope this article has aroused your curiosity: Liquity has been available since last April and yet very few people realize the elegance and minimalism of this protocol that offers credible solutions to real challenges.

To go further, there are no secrets:

* [The documentation](https://docs.liquity.org/)
* [The discord](https://discord.gg/j7hHaR4G6S)
* And to go further, I propose you this recent live where I discuss about borrowing in DeFi (in french of course...)

Have fun!

{{< youtube LXDSxRCMsDE >}}

_🙏 Huge thanks to HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony for proofreading the French version of this article and translating it integrally into English._

---
title: "🗿 Reflexer Labs (RAI) : the What, How and Why"
description: "Reflexer's RAI is a new type of asset still unique in DeFi. It is also based on a system with a de-governance scheme. So let's look at how to stay safe from the risks associated with fiat currencies, centralization and trust thanks to RAI's design!"
date: '2021-09-17T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Understanding]
tags: [DeFi, Ethereum, Stablecoins, Reflexer, RAI, Maker, Liquity]
toc: true
tocNum: false
url: reflexer-rai
---

RAI is a strange beast that many people still don't understand or care about, including people who are really knowledgeable about DeFi. So it was time to offer you a rather exhaustive article dedicated to its subject. I've included everything I thought was relevant to understand why an asset like RAI is needed, what it does and how it works.

So get a cup of coffee and hang on, we're in for a great ride!

![cover](/img/2021/reflexer-rai/cover.gif)

## Understanding RAI's context

Before we even begin to get into the nitty-gritty, I think it's essential to understand the context around RAI, i.e. the main stable assets used today and their limitations.

The context for understanding RAI is quite dense, but the good news is that this is not the first time I have covered this topic on the blog. So I'll refer you to some relevant reading to go deeper into the subject :

1. [Exploring stable assets on Ethereum: approaches & endgame]({{< relref path="/content/posts/2021/pegged-assets.md" >}})
2. [Understanding innovations in money markets to envision their future]({{< relref path="/content/posts/2021/money-market-innovations.md" >}})

If you don't have time to explore the concept in depth with the articles proposed above, here are the two essential points to remember to fully understand the rest:

1. Currently, **the overwhelming majority of the stablecoin demand is covered by centralized solutions requiring trust**, the most used being USDT (~66 billion) and USDC (~27 billion).

2. Whatever your preferred economic theses, especially in terms of inflation, I think we can easily agree on the need for stable assets that are not correlated to a fiduciary currency (= managed by a state). 

### The wUSDC trick

I use the term "wrapped USDC" (wUSDC) to describe a situation that is common in alternative stablecoins: it is used to concisely and appropriately describe **solutions that essentially use USDC as collateral**, a trusted stablecoin guaranteed by a central agency (Circle).

In such a situation, there is no need to go further, not even to analyze the details of the system: since their main collateral can be frozen or seized, **stablecoins produced** in this way cannot be considered decentralized or trustless.**

This kind of assets has a surprisingly large following, the main ones being Maker and Frax.

### Maker = a majority of collateral requiring trust

With Maker (DAI), **approximately 60% of DAI are minted with USDC as collateral**, to which figure we need to add those minted from other collaterals requiring trust: wBTC, TUSD, GUSD, PAX, USDT, renBTC + all UniV2 pairs involving at least one of these tokens + all collaterals from the real world such as Centrifuge: New Silver. [Details on DAIStats](https://daistats.com/#/).

![dai-collateral](/img/2021/reflexer-rai/dai-collateral.png "Overview of the distribution of collateral used to secure DAI in the MakerDAO system.")

Note: PSM is a module that prevents excessive price volatility of DAI. It is therefore automatically minted by the PSM when necessary.

The first version of Maker, before the Multi Collateral DAI update ([MCD - 18/11/2019](https://medium.com/@MakerDAO/update-the-road-to-multi-collateral-dai-2d4c48092270)) used only ETH as collateral and thus presented much more credible guarantees. This is no longer the case at all.

🙏 Nevertheless, I warmly thank the MakerDAO team for their very many contributions to the ecosystem - the Maker MCD model is even used as a basis by Reflexer!

#### FRAX ? Guaranteed by USDC or nothing (algorithmic)


**On the FRAX side, only USDC is used as collateral**, in various forms - either in Yearn/Compound/Aave to produce a return, or via [AMOs (Algorithmic Market Operations Controller)](https://docs.frax.finance/amo/overview). Here are the details of the assets that are used to collateralize FRAX, [available on the official website](https://app.frax.finance/).

![frax-collateral](/img/2021/reflexer-rai/frax-collateral.png "Overview of collateral used in Frax: USDC and all its yield-bearing variants (additional technical risks) + a variable algorithmic (collateral-free) portion.")

Both Frax and DAI are developing a myriad of interesting approaches, but since their basis is centralized, **they cannot be considered anything more than a mechanism for amplifying the liquidity available on USDC, at best**. They do, however, make **interesting contributions in terms of fundamental research** that may help establish a more optimal solution that does not require trustlessness.

### Are there relevant alternatives to RAI?

To date, RAI is a unique asset with no comparable alternative. However, there are systems that share certain characteristics with RAI, such as **the exclusive use of ETH as collateral**. 

So, if you are ready to expose yourself to the dollar, Liquity offers a very relevant alternative which also has **the merit of being totally unstoppable** (which is not yet the case with RAI): the contracts have no administrative function, exactly like Uniswap V1/V2. However, there are still the oracles (necessary for a loan service) and the associated risks.

Now that the stage is set, let's move on to the main course: it's time to study the underlying mechanisms of RAI. We'll start by how to mint it from a user's perspective before going into more detail about what RAI actually is and how it works.

## How is the RAI created ?


Reflexer's RAI is in some ways **both the primary and final form of Maker's DAI**. First, in the sense that it returns to the promises of the original DAI (the SAI): only the ETH is used as collateral, and final in the sense that RAI manages to extricate itself from the dollar dependency.

Reflexer is based on a Maker MCD with several changes, including the incorporation of the PID controller, protection against liquidations and many others. We will slowly unfold all this but let's start by seeing how the system works from the user's perspective.

Just like on Maker, RAI is created directly by Reflexer users. Users can open **a safe that allows them to stake ETH and mine a proportional amount of RAI**. Each user can choose the amount of RAI minted for the same amount of ETH at stake (-> different risk levels) and must manage his position. **Liquidation is possible and necessary** because it ensures that there is always enough ETH in the system to guarantee the RAI issued.

Nevertheless, the system here is innovating compared to Maker thanks to its "Savior" function. It allows **to use a RAI/ETH liquidity position on Uniswap V2 as a guarantee for a safe**. Thus, if the ETH price were to fall suddenly, which could put an open safe protected by this function at risk of liquidation, **the Savior automatically withdraws the quantity of liquidity necessary to bring the safe back to the desired collateralization level**.

This allows users who mint RAI and then use it to provide liquidity to sleep much more peacefully!

## But what is RAI exactly ?

RAI is a new asset class in its own way. It aims to be **low volatility, without relying on another stable asset** (fiat currency or gold are the most traditional sources). To do this, RAI relies on a system that reacts dynamically to market conditions.

In the case of RAI, there are two key parameters to consider:

1. **The redemption price** = value of a unit of debt in the system
2. **The market price** = everything is in the name !

Of course, the system has no control over the RAI price observed in the market, which is determined by buyers and sellers. Nevertheless, it can gradually adjust certain parameters to modify the redemption price and **converge the two prices in the future**.

We are therefore faced with a situation that can be generalized quite easily, embodied by an entire field of engineering and called **control theory**:

![control-theory](/img/2021/reflexer-rai/control-theory.png)

In the case of RAI, **the controller is algorithmic** and again quite standard: it is the famous **"PID controller "**. It is based on a fairly dense mathematical formula that it is not necessary to understand in order to understand the relevance of the system.

Nevertheless, one essential point must be understood: the inherent inertia of the system. The controller cannot afford to make sudden changes in the parameters (which would be detrimental to its relative stability), so it must operate in a more iterative and progressive logic.


Once this is understood, let me remind you that the system by itself cannot affect the price of RAI. All it can do is vary the redemption rate, which modulates the incentives of system participants. This creates **arbitrage opportunities** for those participants whose execution brings them closer to the equilibrium between the redemption price and the market price.

Let's look at this in practice.

There is a logic here that is reminiscent of [algorithmic stablecoins]({{< relref path="/content/posts/2020/algorithmic-stablecoins.md" >}}), although the end product of the system is totally different.

### When market price > redemption price

We start with this situation because I think it is simpler to understand. In the case where the market price exceeds the redemption price, that means anyone with ETH available could potentially generate a profit by arbitraging the market:

1. ETH deposit and RAI mint;
2. Sale of RAI in the market for a profit;
3. (When market price &lt; redemption) repurchase of RAI to pay off debt and release ETH. The difference between the 2 prices on RAI - fees in gas is the profit generated.

![marchesupredemption](/img/2021/reflexer-rai/marchesupredemption-en.PNG)

This situation is all the more interesting for those who already have safes with available capacity: they save themselves a step in the scenario presented above.

In this scenario, there is therefore an incentive to mint RAI (->increase supply) and to sell it on the market (->bearish pressure) which gradually reduces the price on the market, making it converge towards the redemption price.

### When market price < redemption price

In the opposite case, the redemption rate becomes positive, making the existing debt more expensive. Users with active safes have an interest in paying off their debt, which reduces the available supply of RAI.

![marcheinfredemption](/img/2021/reflexer-rai/marcheinfredemption-en.png)

In addition, if they had converted their RAI to another asset (e.g. ETH for leveraged exposure), they will have to acquire RAI in the market (->bullish pressure) in order to be able to repay their debt.

As you can see, it is in the best interest of the Reflexer system players to monitor the redemption rate and react accordingly. If you have an active safe, I invite you to consult it regularly - [it can be seen on the Reflexer website](https://stats.reflexer.finance/)

This rate impacts simple RAI owners less directly, especially if they use them to produce a return (which can offset a negative rate) but it is still a metric to keep in mind.

### Dynamic adjustment of the redemption rate

**Dynamic adjustment of the redemption rate is one of the essential features of Reflexer / RAI**. To better understand why this is critical, let's analyze the situation on Maker pre-MCD:

1. The demand for IADs is (part of) the demand for stablecoins.
2. However, IADs are created by leveraging ETH, so they depend on the need/appetite for leverage on ETH, which is independent of the demand for stablecoins, which mostly depends on general market conditions (bear or bull and others).
3. If demand is higher than supply, on Maker, there is no dynamic adjustment. You have to wait for a vote of the governance (and the delays that go with it) to lower the Stability Fee. And it's the same in the other direction (too much supply).

Thus, **the balance between the supply and demand side of the equation is almost impossible to maintain**, which is why the pre-MCD DAI could often end up above its peg. Maker solved this problem by adding many types of collateral, including non-trustless stablecoins and then the PSM which automatically mints DAI from USDC when needed. The solution proposed by Reflexer (dynamic adjustment of the redemption rate) has the merit of **solving the problem at the level of the system itself**, which allows to keep ETH as the only collateral.

## FLX and RAI's "de-governance" strategy.

In addition to the RAI, Reflexer's system also has a second token, FLX, the "ungovernance" token. It is used for system governance and also serves as a last resort liquidity mechanism (in case of bad debt), with a system quite similar to Aave's Safety Module.

The FLX token can be purchased on the market, but it is mostly **distributed to the main actors involved in the system** - [the exhaustive list of FLX incentives](https://app.reflexer.finance/earn/incentives) is available on the Reflexer website.

Those who are eligible for FLX (claimable on the Reflexer website, monthly distribution) are:

1. Safes owners who bring their RAI in liquidity on the UNIv2 ETH/RAI pair (migration in progress, end soon) or UNIv3 RAI/DAI.
2. But also the liquidity providers on FLX/ETH (migration in progress, end soon)
3. And finally the FLX stakers in the equivalent of the Safety Module at Reflexer.
4. There are also incentives in FLX related to the use of RAI in various DeFi services, detailed in the last part.

[FLX staking (Uni V2 FLX/ETH)](https://docs.reflexer.finance/incentives/flx-staking) serves as both an incentive mechanism to provide liquidity as well as a guarantee for the system. If the system is under-collateralized, the stakers will be diluted (->token LP liquidated) so that the module acquires RAI and brings the system back to equilibrium.

In a normal situation, the stakers simply enjoy a rather attractive return. Just like Aave's Safety Module, this module has a time limit for unstake, to avoid liquidity drain in critical periods: it is 21 days.

Now that we have the basics on FLX, let's discuss its long-term issues a bit more.

### The gouvernance exit plan

The Reflexer system is intended to be "governance-minimized". This has been the case since its inception, since decisions that are made by governance in Maker (Stability Fee of vaults) are automated in Reflexer (PID controller).

The vision is simply to automate everything that can be automated in the long term, once the system is mature, and to give the keys to the subsystems that cannot be automated to the FLX holder community. 

The team has set three main levels related to this objective [detailed in the FLX presentation article](https://medium.com/reflexer-labs/introducing-flx-20755214a465). Each level is linked to a date: 

* 14 months after launch - April 17, 2022: minimization of governance on the main subsystems (liquidation, auction and taxation)
* 18 months after launch - August 17, 2022: minimization of governance on all main contracts, except for the PID controller, oracles and the Savior mechanism.
* 3rd step (date incoming): handover (to FLX holdeurs) of the remaining mechanisms.

I think this overview is enough to understand the interest of RAI and how it works. So let's see how RAI is already used in various DeFi protocols.

## The DeFi ecosystem around RAI

RAI is gradually being adopted within the DeFi ecosystem, and that's great to see! So I'll end with a quick overview of the different RAI integrations in DeFi protocols, starting with money markets.

### RAI on Fuse (Rari Capital)

Fuse is a rather innovative money market since it allows the creation of pools by players who are not the team, and eventually anyone. It is therefore quite logical that Fuse was one of the first money markets to support RAI. Depending on the pool, it is also possible to **use RAI as collateral on Fuse**.

RAI is currently available in 3 asset pools with different risk levels and borrowable tokens:

![fuse-rai](/img/2021/reflexer-rai/fuse-rai.png)

### RAI on Aave

After adding support for RAI already a few weeks ago, Aave recently allocated a (very moderate) amount of StkAAVE to incentivize borrowing and depositing on RAI. It was necessary to shed light on one of the main contradictions of the platform: Aave is a decentralized money market that (still) uses the vast majority of its budget to encourage borrowing/deposits on stablecoins that are not stablecoins at all (USDC and USDT).

<div align = "center">
{{< tweet 1426577620695719944 >}}</tweet>
</div> 

Note: for the moment **the max LTV of RAI is 0: RAI cannot be used as collateral on Aave**. No discrimination here, this is pretty standard on Aave's part - this is the "classic" and prudent procedure when adding a new type of collateral. Governance can vote to increase this value.

### RAI on Cream

Cream was one of the first money markets to support RAI. However, it is an extremely risky and non-value-added, even deleterious, second-tier money market over the long term. So I'll stop there, and [invite you to read this article if you're wondering why]({{< relref path="/content/posts/2021/money-market-risks.md" >}}).

### RAI on Idle Finance

Idle Finance is a service that allows, as the name suggests, to set up passive return strategies. In the case of RAI, Idle leverages the returns available on Fuse as well as Aave. Initially, there was also Cream but the governance chose to refocus the strategies to contain the risk:

<div align = "center">
{{< tweet 1429907701081989121 >}}</tweet>
</div>

In addition to the native RAI return, a deposit on Idle Finance also allows you to benefit from:


1. From a FLX output, visible here.
2. A StkAAVE yield (corresponding to the share of RAI deployed on Aave)
3. And finally, also a yield in IDLE (soon - voted by the governance but not yet implemented)

So if you want to own RAI over the long term to hedge against dollar/euro risks, the Idle deposit is rather attractive to produce a totally passive return. Be careful though, this means compounding several smart contract risks: Reflexer + Aave + Fuse + Idle.


### RAI + Fei Protocol

Fei is another stablecoin that seeks to maximize decentralization. Here the approach is different and is essentially based on the notion of Protocol Controlled Value (PCV). In short, the bulk of liquidity in EIF pairs is controlled by the protocol itself. The funds come from the genesis of the protocol where users have committed ETH in order to acquire FEI as well as TRIBE (governance token) at their creation.

It is a stablecoin that shares a characteristic with RAI and LUSD: it is fully collateralized by trustless assets (ETH). Nevertheless, FEI is much closer to LUSD than to RAI in the sense that it remains pegged to the dollar.

Recently, the Fei DAO voted to **diversify some of the protocol cash flow to RAI** to make it more sustainable. Thus, up to $6M (~2M RAI) will be acquired and deployed on Aave and Fuse to produce a return.  Other DAOs are also considering diversifying some of their cash to RAI (Moloch, DxDAO, Metagame, etc.), so I expect more similar initiatives.

<div align = "center">
{{<tweet 1430625935607226368 >}} </tweet>
</div>

## Conclusion

I hope you've learned a few things from this fairly comprehensive presentation of RAI. As always, keep in mind that I choose my topics carefully and this article is not intended as investment advice. In this case, Reflexer/RAI was chosen here because it is an elegant system whose analysis allows to discuss many essential notions to better understand DeFi as a whole.

I hope that reading this article has been informative for you.

_🙏 Huge thanks to HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony for proofreading the French version of this article and translating it integrally into English._

Didn't get enough? Well, the Reflexer team has some very well written articles to explain the system in more depth - in English. Here are the ones I particularly recommend reading:

* An article [to understand the approach developed to secure the protocol](https://medium.com/reflexer-labs/securing-the-money-god-ef21453a299b)
* A [series of three simulation articles, perfect for articulating your understanding of RAI in practice](https://medium.com/reflexer-labs/rai-system-simulations-part-1-safe-owners-876a6bd55385)
* Finally, for the brave among you, you can [refer to the original RAI whitepaper](https://github.com/reflexer-labs/whitepapers/blob/master/English/rai-english.pdf)

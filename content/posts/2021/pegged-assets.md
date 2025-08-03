---
title: "Exploring stable assets on Ethereum: approaches & endgame"
description: "The quest for stability on Ethereum: an overview of the different approaches to stabilization and asset indexing to understand their issues."
date: '2021-03-23T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Understanding]
tags: [DeFi, Ethereum, Finance décentralisée, DEX, Marchés Monétaires, Aave, Compound, Reflexer, Stablecoin, MakerDAO, Basis Cash, Empty Set Dollar, Dynamic Set Dollar]
toc: true
tocNum: true
url: ethereum-stable-assets
---

Today, I want to cover an essential topic for Ethereum and other blockchains and often misunderstood: **"stable" assets**, which track the price of a reference asset. Before looking at the different approaches to producing such an asset, we'll first start with a higher level of analysis:

1. Why are such assets needed?
2. What are they used for?
3. Why do we want to standardize non-native Ethereum assets on this chain?

Once these foundations are established, we will have all the tools to **figure out the different methods and what is at stake**.. I will conclude with a more detailed analysis of a project that seems to me very relevant and innovative : the RAI of Reflexer Labs

---

![reflexer-money-god-meme](/img/2021/pegged-assets/money-god-meme.png)

If you are already familiar with the different pegging mechanisms, you can jump [directly to the section on Reflexer](#focus-on-reflexers-rai).

## Assets standardization on the Ethereum's blockchain

The volume of issuance and use of pegged-assets has exploded last year, but before we look at what they are actually used for, let's understand why. The simplest use case is to produce a stable asset, most often indexed to the dollar.

To do this, **the method used at a high level is tokenization**: we represent an asset that comes from another chain / world on Ethereum, such as wBTC (corresponding to 1 BTC on the Bitcoin chain) or USDC (corresponding to 1 USD in Circle's bank account).

This **addresses one of the most common concerns for the general public: [cryptos are volatile assets](https://tokenbrice.xyz/content/posts/2018/stablecoins.md)**.

Also, **the rise of stablecoins has gone hand in hand with the rise of DeFi**, why? According to me, there are many reasons, the main ones being:

1. Borrowings 
2. Stable assets can be very productive in DeFi

### Why are borrowings mostly in stablecoins?

[The money markets](https://tokenbrice.xyz/content/posts/2021/money-market-risks.md) allow their users to borrow assets using other assets as collateral. The most frequent use case corresponds to the following pattern. 

1. The user deposits a volatile asset, such as ETH, wBTC or LINK
2. He uses it as collateral to **borrow a stable asset, like USDC or DAI**.

Why is this so? To put it simply, few people are fond of the risks associated with price changes. **Borrowing an asset, if you then mobilize it, is like shorting it**. No problem with stablecoins - in theory - but the reality is quite different with a non-stable asset: if the price goes down, good for you: the debt will only be cheaper to repay. 

However, the other way around, the scenario can be frightening since **you can end up with a debt that increases**. Let's say you borrow 1000 UNI when one UNI is worth $20. You sell them for another token, for example stablecoins. So here you are with $20,000 DAI that you mobilize in DeFi for example.

You hold your debt for several months and now you want to pay it off. Except that one UNI is now worth $30 and you no longer have any: you have to buy some back on the markets to pay off the debt and close the position. **The debt is always paid in the borrowed asset**: you therefore owe 1,000 UNIs at $30 per unit or 30,000 DAI.

{{< notice warning >}}
I am ignoring the loan interest's here for simplicity's sake. In reality you should pay back slightly more UNI, according to the interest rate and the length of exposure.
{{< /notice >}}

### Yield-farming with stable-assets

With the first point understood, the second one makes perfect sense.: **a lot of people are borrowing stablecoins**, so that means that on the other side of the market people are lending them out, for attractive interest rates considering the demand. For example, on Aave, one of the main money markets, there has been **a liquidity crunch in stablecoins** almost since the launch of v2. Depositors enjoy an average annualized return of about 10%.

The situation is quite similar elsewhere with differences due to the specificities of each money market. Nevertheless, the liquidity crisis on stablecoins goes far beyond Aave: it potentially extends to the whole DeFi.

Indeed, **there is no shortage of opportunities to produce a return with stablecoins**. I'm talking about loans here, but it is also possible to bring liquidity to stablecoin pairs and even combine the two approaches to increase returns with a product like Curve:

![curve-yield-pool](/img/2021/pegged-assets/curve-yield-pool.png "Curve offers many pools that accept productive stablecoins")

### Explosion of the pegged-assets use in 2020

Thus, we have seen a real explosion in the issuance and use of pegged-assets in 2020. On the one hand, more and more projects are being launched to propose **new asset types or new approaches to represent them**. On the other hand, the scenarios for using these pegged-assets are multiplying thanks to the growth of Curve money markets, vaults like those offered by Yearn or Harvest, and other even more complex DeFi products.

To name but one, let's talk about [Alchemix](https://alchemix.fi/), a new synthetic asset service that allows **loans secured by your future return**. Let me explain: with Alchemix, everything starts with a stable asset that produces a return. They chose the yDAI to start with (DAI productive thanks to the Yearn's vault).

The user starts by depositing yDAI. He can then **give up his future return** to borrow up to 50% of the deposited value. His loan is **reimbursed automatically thanks to the interest generated by the yDAI**. In addition, since he has access to 50% of the deposited value immediately (borrowed in alUSD), he can put it to work to increase the return of the entire strategy.

This type of product allows for an interesting across time arbitrage and leads to an even greater demand for stablecoins: at the launch of Alchemix, deposits in the yDAI vault took off up to the maximum capacity available for a while.

I've talked about stablecoins so far, but a similar scenario has played out on other pegged-assets like tokenized BTC on Ethereum.

![stablecoin-growth-ethereum-messari](/img/2021/pegged-assets/stablecoin-growth.png "Historical perspective on the evolution of the volume of stablecoins issued on the Ethereum network. Source: Messari.")

With the impressive growth of DeFi, we can only expect the demand for this type of asset to grow ever faster. So let's take a look at the different approaches used to produce them to understand their trade-off.

---

## The different methods to produce pegged-assets

So far, the vast majority of this demand for stable assets is being addressed with solutions based on a 1:1 match requiring trust. Thus, it is **mostly USDT ($38.5B issued) and USDC ($9.4B) that are leading the way**, well ahead of DAI ($2.7B). The same goes for Bitcoin, without going into detail, all the most used solutions require trust.

{{< notice note >}}
Pegged-assets" are assets that follow the price of another via a mechanism called "pegging". Therefore, the "peg" is the value that the asset must maintain, for example $1 for stablecoins that follow the dollar.
{{< /notice >}}

A growing variety of approaches are being explored to produce a pegged-asset with less compromise. They are generally grouped into large families that correspond to the main method used to maintain the peg. However, as these approaches develop, the boundaries between them become blurred as several projects explore **hybrid approaches mixing several elements of each**. We will start from the simplest to understand and progressively go to the most complex.

### Using a trusted third party (1:1 ratio)

*   **👍 Advantages:** The peg is easily maintained and rather stable. The system is solvent at all times (-> 1 USD in the bank for 1 USDC issued for example)
*   **👎 Disadvantages/Risks:** The system requires a central trusted intermediary - the issuing organization. This same organization relies on another intermediary, the bank where the USD are deposited. In addition, the presence of a trusted intermediary creates a risk: is it reliable? transparent? The risk goes beyond image, it can also be legal.

This approach has already been detailed enough, so I'll move on to the more complex methods.

### Stablecoins produced by over-collateralization: Maker DAI

*   **👍 Advantages:** The system no longer involves a central trusted intermediary (at least initially) & still manages to more or less maintain the peg.

*   **👎 Disadvantages/Risks:** It will require **always more $ collateral than $ (DAI) produced (over-collateralization)**. Governance risks. Risks at the liquidation level, carried out by third parties. The system is as trustless as its most used collateral. Maker now accepts censorable collateral (wBTC, USDC, etc.) which reintroduces a trust risk into the system.

Long before algorithmic stablecoins, MakerDAO is a pioneer when thinking about how to **produce a stable asset with less trust needed in the system than 1:1 approaches**. Maker is a more complex service because beyond the DAI - the stablecoin issued by the system, it also allows its users to use different assets to borrow (technically mint) DAIs.

In addition, it recreates risks and dangers to maintain the peg of the DAI. Many improvements have been proposed and implemented since the beginning, which allows DAI to be much more stable now than in its early days. Nevertheless, the scaling of DAI has come with additional compromises in terms of trust.

---

### More innovative approaches

Here, the approaches are more diversified - I group them into two families: the algorithmic approaches already well studied on my blog and the hybrid approaches. Both are based on an essential concept to understand: the "central bank" of these systems is a smart contract.


#### A smart contract as "central bank"

{{< notice note >}}
I use the words "central bank" because it evokes the essential concept here: the body that issues money and implements the monetary policy of the system is a smart contract. This allows for great transparency and visibility on the actions related to monetary policy.
{{< /notice >}}

To understand the systems presented below, you really need to understand this: **the decisions to create or destroy new stablecoins are "taken" by a smart contract** - it alone has this ability to issue (and destroy / burn in some systems) tokens.

When I say that the smart contract takes "decisions", I must explain myself : **to be more precise, one could say that it reacts to the evolution of various measurable parameters**. The decisions of the smart contract are therefore transparent and predictable. A change in the rules governing it is possible but only via a governance vote.

Most often, the main parameter taken into account is simply **the price of the stablecoin**. For example, in early algorithmic systems like Basis (BAC is the stablecoin), the rules are simple:

*   If BAC > $1, then the system issues and distributes new BAC to try to bring the price back towards $1.
*   When BAC < $1 the system destroys BAC to create upward pressure. The destruction is not direct but voluntary: the actors in the system are encouraged to burn their BAC for a coupon (BAB) corresponding to 1 BAC + premium, which they can collect only when BAC has a sustained price above the dollar.

For more background on this "smart contract central bank" idea, you can read my first article on algorithmic stablecoins:

**[L'état et le futur des stablecoins algorithmiques](https://tokenbrice.xyz/content/posts/2020/algorithmic-stablecoins.md)**

#### Algorithmic approaches

*   **👍 Advantages:** This makes systems without a central trust intermediary possible and thus opens the way to truly trustless pegged-assets. Community governance possible.
*   **👎 Disadvantages/Risks:** Sustained peg loss or difficulty maintaining peg. Possible governance attack.

I analyze the main approaches to produce algorithmic stablecoins in a dedicated article :

**[⚖ L'histoire de deux modèles de seigneuriage : Basis contre ESD](https://tokenbrice.xyz/content/posts/2021/seigniorage-basis-vs-esd.md)**

Thus, projects like ESD, DSD, or Basis Cash were the pioneers of algorithmic stablecoins. However, all of these systems are now in a bit of an abyss: **their stablecoins have been worth well under a dollar for a long time**.

![bac-price-90d](/img/2021/pegged-assets/bac-90days.png "Évolution du prix de BAC sur les trois derniers mois. La situation est similaire sur ESD, DSD & MIC.")

Their users are looking forward to a V2 that will bring stablecoin back to the dollar like the messiah.


#### Hybrid approaches

*   **👍 Advantages:** The best of both worlds?
*   **👎 Disadvantages / Risks:** A new potentially central and  intermediate point of trust appears in the system. You what happened next...

Given the current limitations of first generation algorithmic stablecoins, another approach has successfully emerged: the hybrid approach.  These are intrinsically algorithmic systems that **include nonetheless a reserve in stablecoin**. (different from the system) used to maintain the peg: [more info here](https://samkazemian.medium.com/frax-v2-algorithmic-market-operations-b84521ed7133).

The pioneer in this field is Frax. With Frax, **when FRAX trades above the dollar the system itself sells some to accumulate USDC**. This helps to bring the price down while building up a reserve of stablecoins not exposed to the system itself. Thus, if FRAX is trading **below the dollar, the system can buy FRAX directly** on the market (using its stock of USDC) to bring the price back down to $1.

![frax-price-90d](/img/2021/pegged-assets/frax-price.png "The FRAX stablecoin has held its peg for several months.")

While this approach has the **merit of efficiency** (FRAX has maintained its peg very well since launch), it reintroduces a trusted intermediary into the mechanism. Sure, it's not a bank like with Tether, but it's still necessary trust in the system. What happens if the USDC balance of Frax is seized or frozen: could the system survive it? For those who don't know, yes it is technically (and legally) possible.

{{< notice info >}}

I remain very high-level on FRAX and describe the system mostly as it was in the beginning. Many integrations have been implemented or are being considered, such as the ability to mint FRAX directly into the FRAX-Tornado anonymity set (directly into TornadoCash) to offer a potentially more confidential stablecoin.

{{< /notice >}}

---

## Focus on Reflexer's RAI

To finish this article, which I hope will be instructive, I suggest to analyze an innovative system: Reflexer RAI. It is a similar approach to MakerDAO, in the sense that the stable asset is produced by over-collateralization. Nevertheless, it brings many improvements over the Maker model:

1. **Trustless collateral**: Until now, RAI only accepts ETH as collateral. This means that 100% of the collaterals in the system are not censurable.
2. **Beyond the dollar**: the asset produced by the system does not follow the dollar (which is not really stable itself). The price of the RAI is determined by a consensus established by the market.
3. **The Money God** : just like algorithmic stablecoins, the system reacts to different observed parameters. However, just like MakerDAO, here it is the users themselves who directly hit the RAI.
4. **Governance** : the token of the Reflexer system (FLX), which will be distributed to the users, is intended to be used to progressively decentralize the governance.

Don't panic if you don't immediately understand why this system is innovative and significant, we will explore each of these points in more detail.


### Censorship-resistant collateral

**Initially, MakerDAO only accepted Ether as collateral**. With the first significant update of the system - the [Multi Collateral DAI](https://makerdao.com/whitepaper/White%20Paper%20-The%20Maker%20Protocol_%20MakerDAO%E2%80%99s%20Multi-Collateral%20Dai%20(MCD)%20System-FINAL-%20021720.pdf) - more tokens became usable as collateral.

The community was perplexed by this decision, especially because of the choice of accepted tokens. Thus, BAT was one of the first new collateral while LINK, a token with volume and liquidity already far superior to BAT at the time, only arrived much later.

Beyond this **difficult to understand valuation**, the crux of the problem is that **many collaterals now accepted are censorable**: wBTC, RenBTC, USDC, TUSD, etc. This reduces the trustlessness of MakerDAO since at different times up to 50% of all DAIs were minted from censorable collaterals.

The figure is now reduced, but the concern remains. Furthermore, the addition of a special USDC vault was criticized during Black Thursday for helping DAI regain its peg - but it also made MakerDAO even more dependent on such collaterals.

So Reflexer also fits in as **a reaction to this "drift" of MakerDAO**: for now, only ETH is accepted to open a vault. I will be surprised if the team or the DAO vote to accept censorable collateral.


### Beyond the US Dollar

Moreover, Reflexer goes much further than DAI in its quest for stability. Indeed, the dollar itself does not have a stable value, because of the continuous production of new units which leads to inflation: thus $10,000 in 1950 is equivalent in purchasing power to almost $110,000 in 2021 (3.42% inflation per year on average over the period).

**An asset that is intended to be stable must therefore go beyond the limitations of the dollar and this is precisely what RAI does**: it does not follow the price of the dollar. The price of RAI is determined by pure social consensus: the system takes into account the observed price of the ETH/RAI pair (market price) as well as an internal price target (redemption rate).

There are often gaps between the two, which creates an incentive to beat the RAI:

![reflexer-spread](/img/2021/pegged-assets/reflexer-spread.png "Here we observe a spread of about 3 cents USD")

**Therefore, RAI is obviously not a stablecoin, It is not a pegged-asset either**. There are not enough words to describe RAI accurately, but let me try. RAI is an abstraction on the ETH which is intended to be more stable than the ETH, while maintaining its trustlessness (with time).

### All Hail the Money God

The "Money God" is the term used to refer to the set of rules that govern the Reflexer system. The memetic potential is also enormous. To remain quite synthetic, the Money God is lenient towards those who follow a perennial and long-term logic on the protocol.

For example, the distribution mechanism of the Reflexer token, FLX, was recently modified to better align incentives ([more info here](https://medium.com/reflexer-labs/introducing-flx-20755214a465)). The essence of the change is to better compensate those who perpetuate the system, i.e.:

1. Deposit ETH to mint RAI
2. Deposit **all** the RAI minted + the equivalent in ETH in the liquidity pool on Uniswap.

As of March 8, 100% of FLX is being distributed to those who follow this scenario. [The history of FLX retroactive distribution strategies is here](https://gist.github.com/stefanionescu/e66204be990f4bc113a022341cb39186).


### The De-Governance Plan

Besides the important technical innovation on Reflexer, barely explored here, I particularly appreciate **their approach to governance and decentralization of the protocol**, as described by Stefan one of its architects:

"The principle of “ungovernance” comes from our desire to progressively remove human control from the RAI system, thus making it socially scalable."

The team has established **a plan with concrete and dated goals** to achieve this end. The first step is to make the system's liquidation and taxation mechanisms "governance minimized" - only a few parameters will remain changeable via governance (voting of FLX holders) from this point on. The target date is April 17, 2022, a little over a year after the initial launch of RAI.

At each step, the scenario is similar: a critical mechanism of the system is "governance-minimized" before it is put back under the full control of FLX holders.

You can find [the details of this plan here](https://medium.com/reflexer-labs/introducing-flx-20755214a465).

---

## Conclusion

I've been following and waiting for Reflexer for over a year, I'm thrilled to finally tell you about it, and please forgive me for the delay: I wanted to put it in context to make sure everyone grasps the innovation brought by this protocol.

{{< notice warning >}}
This article **does not constitute investment advice**. I have no credentials in this area: they do not yet exist for DeFi.

I am discussing the mechanics of several protocols and what they allow for or envision in the future. Even if I mention tokens, ditto: I discuss their utility or tokenomics but **never their relevance as an investment**. On this topic, it's up to you!
{{< /notice >}}

I hope this article helps you better understand the rise of pegged-assets on Ethereum - it is essential. It's also critical to understand the different trade-off sets associated with each approach: they are all potentially more or less relevant, depending on your situation and needs!

Finally, whether you are convinced by Reflexer or not, I strongly encourage you to dig into this system, just as I regularly invite you to explore the workings of Aave, Curve or Unslashed. All four are very relevant and innovative systems: understanding them in depth will allow you to internalize many essential things  to understand decentralized finance in general.

_🙏 Huge thanks to HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony for proofreading the French version of this article and translating it integrally into English._
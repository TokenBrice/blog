---
title: "🗡 Risk? Yes please, but exactly how I like it"
description: "Exploring what risk tranching is and why it's **the next financial primitive** in line to be incorporated into major money markets like Aave or Compound."
date: '2021-01-12T01:13:50.191Z'
categories: [Yield]
tags: [DeFi, Ethereum, Decentralized finance, Risk Management, Risk Tranching, Money Markets, DAI, aDAI, Saffron Finance, 88mph, Aave, Compound, Yearn Finance, APWineFi]
toc: true
url: risk-tranching-defi
image: /img/2021/risk-tranching/cover.gif
difficulty: "intermediate"
---

DeFi has grown tremendously over the past year, partly thanks to the appearance of more streamlined investment products such as Yearn's or Harvest's **[vaults](https://tokenbrice.xyz/content/posts/2020/vaults.md)**. Thanks to their architecture, they facilitate the mutualization of capital which enables smaller yet profitable investments on money markets and other DeFi services like Curve or SushiSwap.

It was a necessary and much-welcomed layer, and several improvements are still to be made to streamline things even further and increase gas efficiency. However, I believe the bulk of the innovation this year will come from another front: risk management on the vault-type products.

Indeed, several definancial primitives have been developed to provide more options to segregate and hedge risks. There are now credible insurance options available for DeFi, as well as a new approach (in DeFi) to better distribute the risk between consenting and informed actors: tranching.

We'll dive right in, but just before that, I think it's apt to examine the terminology too.

---

## From Lending Protocols to Money Markets

If you've been reading me for a while, you might have seen the term "lending protocol" being used. While it was suited to describe their first purpose, I believe the concept has now outgrown the word, so I'll refer to them as money market from now on. Indeed, "lending protocol" fails to capture all the subtleties now offered by services like Aave — I'm actually a bit late to the party of this one.

In a sense, the change of nomenclature reflects the different stages of evolution of these money markets. In their first months of existence, there was **a liquidity imperative**: it's essentially a fight to grow to a sizeable size, big enough to justify interest from other projects to integrate with the money market fuelling a positive growth loop as we've seen on Aave.

![Aave TVL Growth - Debank](/img/2021/risk-tranching/aave-debank.png "Historical overview of the total value locked on Aave V1 - Debank")

Once the critical mass is reached, **the focus can and must evolve**. To further expand, the money market must extend its range of features - again, like we've seen Aave do with flashloans and fixed rate loans.

To me, it seems clear now that **the second phase of growth of the money markets will be feature-driven**. Indeed, the base features available on the money market are essential, as these markets are more integrated into other DeFi protocols. The money markets with the most flexibility at the base layer will be able to handle more intricate use cases, such as credit delegation.

But today, I want to focus this piece on a risk management concept that hasn't found its way to a mainstream money market yet: **tranching**. Let's see what it can enable!

---

## Tranching: would you like another slice of risk?

To begin, let's start with **the most straightforward "risk alteration" there is - tranching**. The idea here is quite straightforward: the different risk layers taken by the depositor of a given money market are tranched - meaning segregated one from the other. 

Each depositor can choose his preferred exposure. It enables, for instance, a confident degen to **bear all available layers of risk to maximize his APY** while a more conservative whale could **downsize its risk perimeter** by exposing oneself to the technical risk only.

That's the core idea, but let's not forget we're talking about decentralized finance here, so **composability is key**. What makes tranching so exciting is its future as a **financial primitive** - a building block that other apps and projects can use to deliver new services. 

We'll explore more in-depth what tranching as financial primitive entails right after we consider how it currently works in practice, and examine the broader context of risk hedging and APY fixation.

{{< notice note >}}
If you're new to DeFi or even finance in general, you might wonder why we care so much about these different flavors of risks? 
You can picture these mechanisms enabling diverse types of risk exposure as building blocks making it possible to **build end-user products fitting all ranges of risk appetite**. 

I explain why tranching matters more explicitly in the last part of this article where we consider some end-game scenarios for it.
{{< /notice >}}

### Risk tranching in practice

This whole article was actually inspired by a tweet I published where I shared what a tranched aDAI could look like:

As of today, there is mostly one product delivering tranching on mainnet I'm looking at [Saffron Finance](https://saffron.finance/). It's essentially a tranching abstraction layer built on top of the Compound DAI market. The risk segregation is straightforward with two main tranches + one:

1. The **AA tranche**, **covered in case of platform failure**.
2. The **A tranche**, supplying the cover for the AA tranche (= slashing if a failure occurs) but earns a much **more favorable APY**.
3. There is a third tranche - the **S tranche**. However, it is simply rebalancing between the two others as needed.

![The different tranches available on Saffron Finance](/img/2021/risk-tranching/saffron.png "The different tranches available on Saffron Finance for the Compound/DAI market")

Tranching occurs on an epoch-basis, currently set at two weeks. So if you supply the A tranche, for instance, you are bearing the risk of platform failure for the AA tranche for a 2 week period.

Thanks to the excitement that followed the launch, Saffron grew to close to $60M assets deposited. Since then, the dust settled around a low bar of roughly $15M of assets.

![Saffron Finance TVL - Debank](/img/2021/risk-tranching/saffron-debank.png "Historical overview of the total value locked on Saffron Finance - Debank")

{{< notice note >}}
On the charts, we can see some sharp withdrawals: it's due to the epoch-based logic of Saffron. At the end of every epochs, depositors are not earning rewards anymore until they pull out and deposit in the next epoch tranches.
{{< /notice >}}


Saffron is looking to expand to other money markets, most obviously Aave and expand their token coverage (currently only DAI). Other projects are exploring the idea of tranching, most notably [BarnBridge](https://barnbridge.com/), but their current achievements are less enticing in my book.

*Last minute edit: BarnBridge [BOND token is now listed on Coinbase](https://twitter.com/CoinbaseCustody/status/1348739247277268997).*

Now that we have a more practical understanding of tranching and how it can work, let's take a step back to understand what it provides in the broader context of risk management in decentralized finance.

---

## Understanding the broader context of risk management in DeFi

So far, we've focused on the sole risk related to the definancial product itself: mainly smart contract risks, oracle, and economic attacks. We've left at least two layers of risk untouched:

1. **APY Variation**: The APY of the service used is usually variable, so there is an additional layer of exposure there.
2. **Token Price Fluctuation**: Sometimes, the returns are paid in token different from the ones deposited. If the payout token is not a stablecoin, its price can vary - meaning there is yet an additional layer of exposure to consider here if we want to be exhaustive.

Besides, to fully understand the broader context, let's not forget that there are several distinct "temporal approaches" to risk:

*   Using an approach such as tranching, you can be **proactive**, splitting the risk **beforehand** between participants that understand their exposure.
*   It can also go hand in hand with more **reactive approaches**, such as insurance - a system providing payout **afterward** in the event of a failure. 

The insurance markets are another fascinating topic by themselves, so we'll stick to this simple mention for now and go back to our yields.

{{< notice note >}}
While we're talking about insurance, a fascinating project just launched - Unslashed Finance. It's made in France by a builder I admire, so I'm a little biased, but feel free **[to read their manifesto](https://medium.com/unslashed/manifesto-for-a-decentralised-crypto-insurance-unslashed-finance-873078fd0ddd)** to learn more about their vision.
{{< /notice >}}

---

## Another take on risk management for yields: APY-fixation

As we were saying, the APY of the different yield products available in decentralized finance are constantly fluctuating. It makes for a less predictable income and prevents the entry of investors who are not willing to stomach several layers of risk.

To address this issue, another layer of meta-financial services is emerging - the base value proposition as an investor is quite simple: they offer a **fixed APY on depositors' investments**. It's essentially another flavor of "insurance": you'll get overall a bit of a lower yield, but it's predictable. It's very similar to a stable-interest loan on Aave (vs variable rate).

The buyer side of such services is super interesting: picture it **like a prediction market, for the yield of a given vault or investment product.** Buyers deposit some assets and place a bet on the expected average yield: the closer their prediction is, the better is the return. 

I don't see the buyer side becoming mainstream anytime soon, but it provides the backbone to yet another useful financial primitive useful to provide services more suited to more risk-averse investors.

### APY-Fixation in practice

So far, there are two projects working on delivering fixed-APY yield on popular decentralized investment products such as the Yearn vaults: [APWine](https://apwine.fi/) & [88mph](https://88mph.app/).

Just like Saffron, 88mph is another abstraction layer built on top of Compound, Aave, and Harvest deposits. It provides a **fixed APY for depositors**, while on the other side of the market buyers of floating-rate bonds are bearing the risk of the fluctuations of the APY of the underlying investment product.

![88mph main interface](/img/2021/risk-tranching/88mph.png "Fixed-rate earning opportunities on 88mph")

---

## What does the endgame look like?

Let's wrap this up with a little thought experiment. We're now leaving the present and what is currently live on the Ethereum mainnet to extrapolate a bit and consider what tranching & other risk management approaches can enable in DeFi a few months or years from now.

Assuming:

1. An investment product built, for instance, on the Aave money market:
2. With a Saffron-like product integrated into it
3. Also with an 88mph-like service integrated into it
4. And finally, an insurance such as Unslashed also natively integrated for the DAI peg.

You could envision **the first "risk-free" DeFi investment**, which would be a wrapped deposit of say DAI on Aave, coming along with tranching to only bear the price risk hedged by a coverage against DAI losing its peg on Unslashed earning a fixed APY.

It's insane to consider the different steps of the evolution of let's say DAI we witnessed or are about to witness in barely two years:

1. DAI
2. **Interest-bearing** DAI
3. Interest-bearing DAI with a **fixed APY**
4. Interest-bearing DAI with a fixed APY **not bearing the technical risks**
5. Interest-bearing DAI with a fixed APY not bearing the technical risks & **covered against DAI losing its peg**

aFIXEDAPYDAI_PEGINSURED: our new monetary overlord? The actual name will be way more catchy, rest assured!

Are you ready to witness **the future of money unfolding methodically before your very eyes as your assets receive software updates**? 

I for one cannot wait: I've been prepping for the past three years.

---

_Thanks to Waël for making the cover image featured at the top of this article (as well as the TokenBrice emblem)._

_🙏 Huge thanks to HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony for proofreading the French version of this article and translating it integrally into English._
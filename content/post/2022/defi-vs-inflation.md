---
title: "How to build an inflation-proof DeFi portfolio?"
description: "What if DeFi, more than ever, offered serious and credible answers to economic and financial issues? Example with the galloping inflation and the various products and strategies DeFi offers to guard against it."
date: '2022-03-09T01:13:50.191Z'
categories: [DeFi, Understanding]
tags: [DeFi, Ethereum, Decentralized Finance, Stablecoins, Stable Assets, Money Markets, Reflexer, RAI, Maker, Liquity, Curve, Convex, Aave, APWineFi, vlCVX, Stablecoin]
toc: true
tocNum: false
url: defi-vs-inflation
image: /img/2022/defi-vs-inflation/defi-vs-inflation-tokenbrice-cover.jpg
difficulty: "beginner"
---


Inflation is more than ever at the center of discussions and concerns: no one understands much about it, no economist has really anticipated it, but we all have an opinion about it. 

Today, we leave economics and politics aside to focus on what matters for your wallet: in decentralized finance, all kinds of protocols are developed, and a good part of them **provide credible and innovative tools to preserve and develop the purchasing power of a portfolio**, even when the macroeconomic context is most uncertain.

I propose to evaluate strategies involving different assets and protocols, all with the same goal: to preserve and develop the effective purchasing power of a given portfolio. Nevertheless, we have to start with the basics, level 0: what is inflation and why should we, DeFians, care about it?

## α/ Tutorial: Understanding the impact of inflation on a crypto portfolio

I won't venture into the details of inflation for fiat currencies here, but the basic concept is known to anyone familiar with cryptocurrencies. 

Before we get into the nitty-gritty, let's start with the term: here is how the INSEE (Institut National de la Statistique et des Études Économiques) defines inflation:

> Inflation is the loss of purchasing power of money that results in a general and lasting increase in prices. It must be distinguished from the increase in the cost of living. The loss of value of money is a phenomenon that hits the national economy as a whole (households, businesses, etc.).

Let's just remember that, **just like in DeFi where each token is associated with a protocol and potentially even an ecosystem, each fiat currency is also based on an economy as well as a set of rules** (legal system).


### Inflation, macro point of view (scale = country)

Inflation corresponds to the production of new money, the important thing is not so much the quantity of money created, but more **what is done with**. We all understand this rather well with two caricatural examples at each extreme:



1. The central bank of country A issues a large amount of money in order to invest massively in its transport infrastructure and its energy supply (= long-term investments). 

_Here, inflation can be controlled because the new money issued is used to finance investments that develop the country's economic potential in the long run (-> compensation)._

2. The central bank of country B issues a large amount of money to finance an emergency plan to compensate for the foreseeable consequences of previous pseudo-sanitary measures.

_In this second scenario, the new money is used to cover a "current expense" of the government. The personal equivalent would be to go into debt every day to pay for lunch. This is obviously unsustainable in the long run. In this scenario, inflation can only be massive as a large amount of new money is issued, while the economic potential of the country in question stagnates or deteriorates._


### Evaluating future inflation?

Enough about the macro, let's go back to our scale, with things we know well. Here is the evolution of the M1 money supply on the dollar, this allows us to visualize its "marketcap" in a way:

![USD M1 Supply](/img/2022/defi-vs-inflation/USD-m1-supply.png "A representation of the evolution of the circulating total of a PART of the dollars")

Here we only look at M1 for simplicity but the trend is similar on M2 and M3.

We are interested here in the dollar which, although challenged, remains the fiduciary currency that sets the tone. As you can see, the curve has been going vertical since the beginning of the Covid crisis. The curve is now much scarier than the worst shitcoins I have ever seen. Doubt it? Consider the same information, presented in this light:

**The dollar has been around since 1914. 20% of all dollars in circulation were created in 2020. At the current rate, the total amount of dollars in circulation doubles about every 4-5 years.**

To compare with crypto, many are concerned about inflation / new token issuance on Curve Finance (CRV). The 4 year issuance curve looks like this:

![crv-release-schedule](/img/2022/defi-vs-inflation/crv-release-schedule.png "CRV token issuance curve")



I'm no economist, but I know my shitcoins. The official US inflation figure we are given is 7.5% per year. Like unemployment figures, it's a highly political metric that's hard to really appreciate. 

The 7.5% figure may seem high, but it is still low when compared to the unprecedented money creation to deal with Covid. So I expect to see this inflation rise further, or else to be sustained over an extended period of a decade.

So inflation is here, at 7.5% minimum for several years at least. Enough with boomers' macro, let's consider the range of tools that the DeFi offers us to face it and overcome it.


## I/ Beating inflation with "classic" stablecoin returns

The first approach is as always the simplest, **the brute force method**: an inflation of 7.5% means that USD left as is will lose 7.5% of their value over the year. The point here is to find a source of return higher than inflation: the difference between the two is the effective return.

With inflation at 7.5% on the USD, I think it is prudent to make sure to **reach at least 1.5x this figure in yield** to really consider yourself inflation-proof.

Here, the game is simple and the rules fairly easy to understand:



1. You start with a position in a given stablecoin
2. The goal is to make it productive, without assuming IL risk
3. With a return that exceeds the inflation figure, once the gas costs have been amortized.


### Simple stablecoin deposit

So we would aim for **a 10.875% annual return on stablecoin $ at the very least**. With recent declines and yield compression this is increasingly difficult, but still findable even with a single stablecoin deposit without IL risk. Tools like [Coindix](https://coindix.com/?kind=stable&sort=-apy&chain=ethereum) can help you find the vault of your dreams:

![coindix](/img/2022/defi-vs-inflation/coindix.png)


Be careful though, **not all vaults are created equal**! For example, we see nice returns on Bancor on the screenshot: don't forget to consider the volatility of these returns as well as the fees in gas to deploy the position (a Bancor LP is notoriously more expensive than a Yearn deposit for example).


{{< notice warning >}}
I mention it here only to forget it just as quickly afterwards: the [Anchor protocol](https://app.anchorprotocol.com/) also offers you a "fixed" return close to 20% on UST stablecoin. Such a guaranteed rate does not come, of course, without serious compromises that raise real questions about the sustainability of this whole ecosystem (Terra/Luna).
{{< /notice >}}


### Provision of liquidity + time commitment

Still in dollars, but a bit riskier, we can consider different types of commitments, with very controlled / no IL risks. For example, a liquidity provision between FRAX and DAI.

![FRAX/DAI LP opportunities on Frax](/img/2022/defi-vs-inflation/frax-dai.png "LP opportunities on FRAX/DAI")


Here it is at [Frax Finance](https://frax.finance/), the prime rate (x1) is just our minimum target, but it is possible to reach up to x5 with two types of commitment:



* X3 by locking LP tokens for 3 years
* X2 by using your veFXS (much harder to reach)

The effective return on a position locked in for three years corresponds to about 3 times our minimum target, thus offering a credible protection against the loss of value due to the consequences of inflation, but you still have to be able to assume the three-year commitment.

The example is taken here on DAI, but the situation is similar on the other major stablecoins; for example, here are the FRAX/USDC pools:

![FRAX/USDC LP opportunities](/img/2022/defi-vs-inflation/frax-usdc.png "LP opportunities on FRAX/USDC")

{{< notice tip >}}
Convex for Frax is coming (optimizing Frax LP farming via Convex), if you don't have your own veFXS, it's probably pertinent to wait until the service is released to make a decision with all the cards in hand.
{{< /notice >}}

### Tokenizing and speculating on future yields

To beat that famous 10% return on the dollar, there are still many other options. I present you one last one here to help you consider the other possible strategies.

For this one, we rely on [APWine](https://apwine.fi/), a protocol that allows the tokenization of future yields on productive assets. The principle is both simple and complex: depositing an asset on APWine allows to separate its future yield (FYT: Future Yield Token) from the underlying principal (PT: Principal Token). 

From there, different strategies are possible, such as immediately selling the future yield (FYT) in order to increase the quantity of the productive principal. Such a tool enables better risk management considering the volatily of yields observed in DeFi

Let's keep it simple and still well above the 10% requirement: let's zoom in on the aUSDT vault of [APWine](https://app.apwine.fi/):

![APWine aUSDT vault](/img/2022/defi-vs-inflation/apwine-USDT-en.png "The aUSDT vault on APWine")


I automatically exclude the PT/FYT pool which is more complex to understand and has much higher risks than the PT/Underlying offering a 44% return in APW anyway.

Here the strategy is simple, but you have to **keep in mind the important gas costs linked to the use of APWine**. To implement the strategy using USDT in the wallet, you need to:



1. Allow + Deposit a part of them on Aave (I'd recommend 55% of the total maximum for this specific strategy)
2. Allow + Deposit the aUSDT obtained in 1 on APWine
3. Allow (x2) + Deposit the PT and Underlying (USDT) tokens as liquidity providing
4. Allow + Stake of the LPs PT/Underlying tokens to obtain the return in APW
5. Don't forget also the gas fees related to the APW claims + unwinding of the position at the end of the period (or before).

It is therefore better to wait for a day when the transactions clear under 30 gwei so as not to suffer too much from the gas costs on such a strategy.

The advantage here, compared to Frax for example, is that **the position is much more liquid**. APWine works with an epoch logic that lasts 90 days. Thus, to more easily amortize the costs in gas it is preferable to deploy the strategy at the beginning of the epoch: this is also when the returns are generally the highest.

The third winelisting (where the next tokens supported on APWine are decided) has just ended, so don't hesitate to prepare for it:

![APWine - Winelisting 3](/img/2022/defi-vs-inflation/apw-winelisting3.png "The results of the third winelisting on APWine")


APWine is still a young protocol, but the governance is dynamic. The next step is approaching: as on Curve, it will soon be the veAPW holders (locked APW) that [will decide on emissions](https://gov.apwine.fi/t/apgp-2-enable-gauges-for-apw-rewards/171) for each given vault. A redistribution of the cards is to be expected, plan ahead.


## II/ Hedged productive positions with various "alternative" stablecoins

We have stayed for now on the dollar, it's easier to begin with. Although dollar stablecoins are still largely dominant, there are now **many stablecoins based on other fiat currencies** such as EUR, JPY (Japanese Yen), CHF (Swiss Franc), KRW (Korean Won) or even CAD (Canadian Dollar).

Besides the few centralized stablecoins (EURS or EURT), this market is mostly covered by protocols that offer to create synthetic stablecoins backed by other stablecoins. This is the case for example with [Jarvis Network](https://jarvis.network/), which uses USDC to collateralize different types of stablecoins: jEUR, jCHF, jKRW, etc.


### Single deposit

Yield opportunities with no/low IL for such stablecoins are still quite rare, and usually found on Curve: providing liquidity against other stablecoins based on the same fiat currency, if any.

![CHF pool on Curve Finance](/img/2022/defi-vs-inflation/curve-chf.png "A CHF pool on Curve Finance")


Only a few stablecoins have lucrative single deposit options jEUR, jCHF, jJPY. They are based on the corresponding Curve pools, with additional incentives offered by Jarvis and other projects.

Via Jarvis (also available farmed by Harvest), it is also possible to generate a return without IL on jCAD and jJPY.

### FiatA/FiatB Liquidity Providing

However, there is a slightly different approach, more risky, but also potentially more protective against inflation: providing liquidity on two stablecoins representing two different fiat currencies, for example EURT/3pool (USD) still on Curve.

More interestingly, especially for smaller portfolios, many alternative stablecoins are available on Polygon or Avalanche, with a fairly dense ecosystem.

Jarvis offers jCHF-USDC, jEUR-USDC or jCAD-USDC pools with returns above 20%. Tools like [Harvest.Finance](https://harvest.finance/) or [Beefy.Finance](https://beefy.finance/) can also be used to automatically compose the returns obtained:

![Harvest Network Jarvis jFIAT](/img/2022/defi-vs-inflation/harvest-jarvis-2-stables.png "Vaults jFIATs on Harvest Finance")


Warning: depending on your base asset (e.g. USDC), exposure to EUR (or other currencies) can be lucrative or costly - depending on the evolution of the USDC/EUR exchange rate.

Finally, for the more adventurous among you, you should know that APWine is also available on Polygon and already supports several Jarvis tokens, such as the MooJarvis_4eur:

1. Liquidity contribution on Curve (4eur)
2. Managed by Beefy Finance (moo)
3. Which compounds return that Jarvis offers

Again, the addition of tokens voted during winelisting 3 will open new doors with the upcoming arrival on APWine/Polygon of:



* MooKyber_USDC-jEUR
* MooMai_USDC-MAI


### Forex Borrowing

Finally, if liquidations don't scare you, know that a Fuse pool on Polygon ([Pool7 - Jarvis Forex Market](https://polygon.market.xyz/pool/7)) allows you to use different jFiat as collateral as well as to borrow. 

![Fuse pool 7](/img/2022/defi-vs-inflation/fuse-pool7.png "Jarvis Forex Market (Fuse/Polygon/Pool7)")


With such a service, almost anything is possible, here are some examples to inspire you:



* Long USD + short EUR = MAI in collateral, borrow jEUR then sell jEUR and potentially loop
* Short GBP via CHF = jCHF in collateral, borrow jGBP then sell and potential loop.

{{< notice tip >}}
Also note that the productive stablecoins m2CAD and m2JPY are available as collateral while keeping their yield: they can be interesting for more traditional leverage strategies.
{{< /notice >}}

### Finding your balance

More than just one magic position, what I like about Jarvis stablecoins is the ability to **diversify easily into different types of fiat currencies**. Thanks to the low transaction fees on Polygon, it is quite possible to mix several different currencies and positions to make a coherent whole and well protected against its local inflation. 

For example, for a European (= spending €):



* 25% in stable productive € without IL, for example MooJarvis_4eur (+APWine)
* 25% in jEUR/USDC
* 20% in stable productive dollar (e.g. aUSDT APWine strategy)
* & Diversification: 15% jCHF/USDC + 15% jGBP/USDC

Finally, while we're on the subject of "exotic" stablecoins, you should know that there are also a few that track gold or silver - they can be relevant from this perspective too. For example XAUT (with Pool Curve XAUT/3crv). Gold and silver remain ~~barbaric~~ boomers' relics, personally I see very little interest in them for a competent DeFian.


## III/ Inflation resistant stablecoins

Beating inflation is nice. Hedging it? Even better. But **why not just abstract it**, using products that are naturally resistant to it? There are still very few stablecoins that are not tracking fiat currencies, but the supply is growing rapidly.


### RAI, the first dollar-free stablecoin

RAI is a strange beast, the very first "unpegged stablecoin." Launched at a value of Pi in USD (3.14) in 2021, it has been moving between 3.02 and 3.06 almost since its launch. Given its recent arrival (just over a year), it's hard to see how RAI will perform in a period of prolonged inflation.

Still, diversifying a portion of your stablecoins into RAI may be an attractive option. In addition, there are different return options available on RAI:



* Simple deposit without IL risk: Idle Finance deposits your RAI in Fuse/Aave to optimize the native return + incentives in FLX from Reflexer + incentives in IDLE.

![RAI on Idle Finance](/img/2022/defi-vs-inflation/rai-idle-0.png "The RAI vault on Idle Finance")

![Additional FLX incentives for RAI on Idle Finance](/img/2022/defi-vs-inflation/rai-idle.png "Additional FLX incentives on Idle/RAI")

* By assuming IL risk via liquidity provision on Curve vs. 3pool, a better return is possible. The crvRAI can then be staked directly on Curve or via Convex or Yearn.

RAI is based on a mechanism inspired by Maker MCD but with many modifications to make it possible. To understand how it works, I invite you to read [my dedicated article](https://tokenbrice.xyz/reflexer-rai/).

{{< notice note >}}
🚧 Signals that the mentioned protocol is still under development.
{{< /notice >}}

### 🚧 An inflation-resistant stablecoin? The FRAX FPI

The Frax Price Index is a new protocol that should arrive soon within the Frax ecosystem. The goal is to offer a new stablecoin, which would follow the CPI (Consumer Price Index) to protect against inflation. Just like Frax, **the system is based on two tokens**: 
1. the stable - Frax Price Index (FPI) 
2. and the governance token - Frax Price Index Share (FPIS).

[Frax documentation](https://docs.frax.finance/frax-price-index/inflation-hedge) offers some information about the upcoming token. **An airdrop of FPIS is planned** for veFXS or cvxFXS holders. Thus, the protocol will be independent of FRAX/FXS, although a value capture mechanism to FXS is planned beyond the initial airdrop.

It is hard to project solely on a mere design, but it is clear that a stablecoin that would maintain its value despite inflation is a very desirable product. **There are several questions as to whether the peg on FPI can be maintained**: to keep its equilibrium, people will have to take the opposite trade to FPI, i.e. "short inflation". However, in the current context of galloping inflation, it is hard to imagine who could assume such a position and massive incentives might be required.

Nevertheless, the arrival of the FPI is imminent. Traces of the token [FPIS on EtherScan](https://etherscan.io/token/0xdb68c6264e9d0f8a6df1fa5a89f205da38698d15) can be found as early as early March. I look forward to seeing the Frax team's proposed design to address these consequential issues.


### 🚧 Inflation resistance + degen = VOLT

Alongside Frax's FPI, there is another project I've been following closely, waiting for a long time and holding high hopes for. The high-level concept is very simple: an Abracadabra-like product that would not be a walking security loophole.

Indeed, Abracadabra allows borrowing from various productive collaterals, which makes the service desirable. Nevertheless, the infrastructure is close to a hack and the actions of the team members make Abracadabra a second or third grade money market. 

The idea here, with Volt, is to cover the same vertical using a proven infrastructure: the base offered by Reflexer (RAI). Three main changes are expected on this model:



1. Unlike Reflexer, which only accepts ETH as collateral, Volt will diversify the available options, notably with productive collateral such as wstETH. 
2. The value of VOLT, the system's stablecoin, will be indexed to Frax's FPI. The Reflexer infrastructure will be reused (PID controller adapted)
3. The Volt team is also working in collaboration with Fuse and Olympus.

To follow Volt, as always, the alpha lives on [the Discord](https://discord.gg/dGhvDmCNGr)!

{{< notice note >}}
I describe here the initial design of Volt Protocol, which has since evolved. The vision of creating a borrowing service with an inflation-proof stablecoin remains, but the technical choices have evolved. Read [the whitepaper available here](https://github.com/volt-protocol/whitepaper/blob/main/volt.md) for the latest information.
{{< /notice >}}

## IV/ Beating inflation with returns on volatile assets

**In a world where nothing holds and value leaks, what's left? How about good, proven DeFi assets backed by protocols with massive, recurring revenues shared directly with their holders?**

There are a few of them, very few. We will detail them one by one, as well as the different options available on them to produce a return.

### ETH: the origin and the end

There is of course ETH, which has many different sources of return - just like stablecoins, there is nothing to stop you from diversifying your ETH exposure with several sources of return, for example:



* ETH staked with [Lido Finance ](https://lido.fi/)(low yield, but a priori the safest) [~5%]
* LP [rETH](https://rocketpool.net/) on Curve (more innovative, more lucrative, more risky) [~10%]
* Vault covered call options on ETH via [Stakedao](https://stakedao.org/) or [Ribbon Finance](https://www.ribbon.finance/) [~25%, risks!]
* Cross-chain liquidity on a Bridge, for example [Celer](https://cbridge.celer.network/#/liquidity) [~10%]

A position balanced in this way tracks/exceeds inflation slightly with the returns obtained on ETH. The profitability of the position over the long term depends of course mainly on the average entry price on ETH and its evolution.


### CRV, CVX, and FXS: The three Fates of the DeFi?

Among the Romans, the Fates are three goddesses who govern the lives of humans:

1. Clotho weaves the thread of life
2. Lachesis unwinds it
3. Atropos cuts it

DeFi also knows these Fates: three protocols that play a critical role in the survival and growth of potentially any other.

Indeed, in addition to ETH, there are several DeFi projects that have already proven themselves, control substantial revenue streams, and offer a truly relevant service in a macro context of prolonged inflation; I see three essentially:

1. **Curve Finance - CRV**: the mother of all yields in DeFi + peg machine and liquidity.
2. **Convex Finance - CVX**: an option on CRV, which controls almost 50% of all locked CRVs and adds real value.
3. **Frax Finance - FXS**: innovative stable project, native DeFi, very productive via AMOs + arrival of FPI + Frax has a big position on CVX & some other protocols.

While being tokens backed by key protocols in DeFi, there is no shortage of return options on these three tokens:



1. CRV -> Deposit on Convex in CvxCRV then stake or LP cvxCRV/CRV.
2. CVX -> Locked vote on Convex in vlCVX -> Return in cvxCRV + bribes.
3. FXS -> Direct deposit on Frax (veFXS) or management via Convex (cvxFXS).


### Other promising tokens

Finally, there are still other projects that have not yet reached the profitability of Curve or Convex but represent credible bets. In a world where inflation is here to stay, the tools that will allow us to protect ourselves from it can become very popular: I propose you some other theses related to what has been already mentioned in the article.


#### APWine.fi (APW): betting on the advanced DeFi infrastructure

When inflation goes up, everyone is looking for yield. Let them run behind the %, and instead target the pick sellers in this gold rush. This is the main thesis behind a bet on APW.

As you could see in the article already, APWine offers interesting products to bet on the evolution of yields or even realize a future yield immediately. As DeFi develops, the demand for a product like APWine will keep growing. Will it be APWine, or another one? It's up to you!

With the APWine Wars coming up, it's not a stretch to envision bribes similar to what we see on Convex.

#### Reflexer (FLX): a bet on degovernance

In addition to the very interesting technical approach, Reflexer also innovates on another level. Indeed, since the launch of the protocol, the team has presented a "De-governance Plan" aiming at progressively minimizing the team's control over the protocol through two main means:



* Automation of everything that can be automated
* Management by FLX holders for situations still requiring manual analysis/decision making.

In addition, **Reflexer now exceeds RAI**. The Money God League is a set of projects building using the Reflexer infrastructure, with the support of the team. So it seems quite natural to consider an airdrop of the governance token of these new projects, including VOLT, to FLX holders.

Last tip: the stakers of the FLX/ETH LP in the Reflexer Safety Module are the last resort to guarantee the solvency of the protocol. If I were to consider an airdrop to thank the Reflexer community, I would probably target them first.


#### LooksRare (LOOKS): bet on NFTs

Think of LOOKS as an option on the NFT market. In fact, LooksRare is the first NFT marketplace that shares revenue. This translates into **an ETH yield for stakers on LOOKS that reached 3 digits sustained during the first few weeks**.


![ETH yields on LOOKS staking](/img/2022/defi-vs-inflation/looks-eth-farm.jpeg "Yields of ~69,000 LOOKS staked during the first two weeks of the protocol") 

Since then, trading volume has dropped and the ETH yield with it, but **the staking LOOKS is still one of the biggest ETH yields out there**.

I'll stop with these three suggestions, but of course there are other options - you be the judge. For example, the QI Wars have started and the protocol has good traction. Be careful, however, not to fall into the trap of thinking that all protocols that adopt the ve + bribes model will be as successful as Curve and Convex. ve tokenomics will multiply: it's about making the right choices!

---

## Good luck and happy harvesting 🚜

I'd be tempted to apologize for the length of this article, but I remain confident that it's worth a read and will be informative even for the most knowledgeable DeFians.

If you have considered other useful strategies or protocols for protecting against inflation, please feel free to suggest them to me.

For further reading, here are some recommended related articles:



1. [Understanding the Curve Wars](https://tokenbrice.xyz/crv-wars/) 
2. [Understanding the Reflexer RAI model](https://tokenbrice.xyz/reflexer-rai/)

And finally, for the practice, which remains ESSENTIAL, your best bet to warm up is to try with small amounts on inexpensive sidechains/L2:



1. The APWine protocol on Polygon to familiarize yourself with these mechanisms.
2. Minting jFIAT / Liquidity contribution on Curve + farming to discover Jarvis
3. Long/short on Forex with jFiats + Fuse.


{{< notice info >}}
Disclosure: I have invested in APWine pre-sale and I am a big user of the protocol. I am a user and frequent holder of almost all the protocols mentioned in this article. 

This article does not constitute investment advice, I'm just sharing my research to help you do yours!
{{< /notice >}}


_🙏 Thanks to [Charles](https://twitter.com/C53300), [PhilH](https://twitter.com/phil_h) and [Disiaque](https://twitter.com/disiaque_eth) for their careful proofreading and their suggestions to help improve this article._
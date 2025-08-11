---
title: "The Maurauder's Map of Decentralized Stablecoins"
description: "New stables are launching weekly, so keeping track of the relevant innovations is challenging. AMO? PSM? DSR? pegKeeper? This article examines the various mechanisms harnessed by stablecoin projects and evaluates their relevance."
date: '2023-09-15T01:13:50.191Z'
categories: [DeFi, Understanding]
tags: [DeFi, Ethereum, Decentralized Finance, Stablecoins, Stable Assets, Money Markets, Aave, GHO, crvUSD, LUSD, fETH, xETH, Interest Rate]
url: stablecoin-marauder-map
image: img/2023/stablecoin-marauder-map/stablecoin-marauder-map-cover.png
---

Wild new stablecoins are constantly appearing, and with the multiplication of chains, layers, and viable stablecoin models the trend is not stopping anytime soon. **Navigating the stablecoin landscape is turning into a critical skill for DeFi**.

While centralized stablecoin models are easier to evaluate, decentralized stablecoins harness various complex mechanisms, making it harder to compare their data face to face. Yet, dozens of relevant new decentralized stablecoins are appearing yearly, and I don’t expect the trend to stop anytime soon.

Thus, this article intends to provide a marauder map to help navigate the landscape of decentralized stablecoin designs. Before combing through the innovations for decentralized stablecoins, allow one more minute to the context: why do we care so much about (decentralized) stablecoins in the first place?


## Size matters

Simply put, **stablecoins are cryptocurrency’s top product-market fit by a wide margin**. DeFi is cool, right? We love it on this blog. Yet size-wise, there are about 3 times more value locked in stablecoins than in DeFi protocols.

Currently, the total TVL in DeFi is around $38B for $124B of stablecoins circulating, serviced mainly by centralized options: USDT makes 66% of the total, and USDC is another 20%.

{{< notice note >}}

Remember that there is a lot of redundancy between the two metrics as stablecoins are widely used across DeFi, so the effective spread is even higher.

{{< /notice >}}

Now, let’s dive in! As we consider the various designs harnessed to deliver decentralized stablecoins, I’ll illustrate the mechanisms discussed using examples from live projects: picture this article as recipe book meets marauder map on the topic of decentralized stablecoins.


## HOW TO BUILD A DECENTRALIZED STABLECOIN

There is a virtually infinite range of designs that can be harnessed to output decentralized stablecoins; however, they all rely on two essential core needs:



1. **Stablecoin Price Stabilization** | Finding an effective way to stabilize the stablecoin price without too much compromise.
2. **Stablecoin Liquidity** | The active management of the liquidity on the stablecoin to maximize its effectiveness.

While both themes address the same need: ensuring that the stablecoin can be traded at peg whatever the circumstances, they operate on different time frames. Stabilization mechanisms are built so that stablecoins tend to their peg over the mid/long time-frames. Liquidity strategies are here to ensure even sizable amounts of the stablecoin can be bought/sold as close as possible to the peg.

Those are two prerequisites for a stablecoin design to be relevant and have a chance at gathering traction. Faults on those two dimensions jeopardize the whole design, so let’s look at the leading price stabilization mechanisms harnessed and their consequences.


### PRICE STABILIZATION MECHANISMS

When faced with sizable demand, decentralized stablecoins can depeg - that is, divert from the peg, usually $1, either upwards or downwards. While similar, the two depegs stem from vastly different design challenges. Let’s start with the most common, the depeg when a $ stable is worth less than $1.


#### Underpegging illustrated with GHO

It usually happens when the stablecoin is mainly used for leverage and lacks significant direct use cases – **a current prime example is Aave’s GHO, trading around $0.97**. GHO is one of the cheapest stablecoins to borrow (1.5% max APY), creating a lot of initial demand for it. Yet, there is not much to do with GHO directly apart from providing liquidity. Thus, many borrowers swap their GHO for something else, for instance, DAI, to harness the 5% yield from the DSR.

Besides, the AaveDAO has been slow to take action to support GHO. Despite the stablecoin being live since mid-July, there are still very few incentives directed to growing GHO’s liquidity, and they are poorly allocated as most of them focus on stableswap pools where GHO is overweight because of its price. Since these pools are 80% composed of GHO, they provide little adequate liquidity at the current price:

![gho-balancer-pool](img/2023/stablecoin-marauder-map/gho-balancer-pool.png "One of the main GHO pool on Balancer")

Right now, the only pressure for GHO to repeg comes from the existing borrowers who could consider repaying their debt with a ~3% discount if they could borrow and swap GHO around $1.

GHO will need attractive earning options directly available in GHO to approach the peg again, such as liquidity-providing options. Still, a GHO-based staking module with revenue sharing would fit the task nicely. Overall, we need more GHO-sinks: mechanisms resulting in GHO being minted and held as such for long periods. Right now, it seems like governance is pushing forward increased support for GHO’s liquidity incentives and a potential GHO PSM (Peg Stability Module): more on this design is below while we address Maker/DAI.

Since it was launched a few weeks ago, most of GHO’s current challenges come from its young age, coupled with a lack of preparation for the launch on the DAO side. The DAO is improving in that regard, with many propositions pushed forward to address the situation, including establishing [a liquidity committee for GHO](https://governance.aave.com/t/arfc-treasury-management-gho-liquidity-strategy-update/14801) I should contribute to.


#### Overpegging illustrated with LUSD

[Liquity](https://www.defiscan.info/protocols/liquity/ethereum) utilizes a unique mechanism called Redemptions to maintain its price stability. In Liquity, users deposit their ETH as collateral to borrow and mint stablecoins (LUSD). The key innovation lies in the redemption mechanism, which enables users to redeem LUSD for the underlying collateral (ETH) at a fixed ratio, even if the market price of ETH drops significantly.

This mechanism incentivizes users to stabilize the price of LUSD by redeeming it when ETH prices are low, thereby reducing the circulating supply of LUSD and supporting its peg to the USD. It provides **immediate and immutable access to LUSD’s collateral to LUSD holders** without the need for liquidity on a decentralized exchange.

Redemptions provide an additional layer of guarantee to LUSD holders but add complexity on the borrowing side, pushing borrowers to monitor and adjust their LTV against other protocol users and market conditions.

Collateral redemptions provide the most direct access to the underlying backing of a stablecoin. Centralized stablecoins like USDC or USDT use a similar, although permissioned, mechanism to enable redeemability to USD.

LUSD traded at a premium for most of its existence, even though the situation has improved recently. Indeed, several factors contributed to enhancing the liquidity and the peg pressure: the success of the [Chicken Bonds](https://chickenbonds.net/), advanced liquidity strategies on novel DEXes like [Maverick](https://mav.xyz/), or the accumulation of LUSD by DAOs and treasuries.

The why of the premium still needs to be pinpointed precisely. One of the likely main factors is that **LUSD is servicing a unique niche**, the resilience-maximized stablecoin, where there is usually more demand (people wanting to hold LUSD) than offer (ETH holders borrowing LUSD and selling it). [This topic was covered in depth last year on Liquity’s blog](https://www.liquity.org/blog/the-premium-of-resiliency#:~:text=LUSD%20is%20a%20stablecoin%20fully,also%20comes%20with%20scalability%20challenges.).

While underpegging is usually more concerning, overpegging can have real consequences, too, as it can make effective borrowing costs less predictable for the users.

LUSD’s overpeg stems from mostly psychological mechanisms: the worst case of sustained overpegging was observed during movements of market panic, especially when a prominent centralized stablecoin is perceived at risk. 

Indeed, thanks to its resilience, LUSD is seen as a **safe haven stablecoin**. A remarkable feat, but it comes with a price: crowds rush to LUSD when other stablecoins are at fault, such as when USDC depegged 10% following the bank run on Silicon Valley Bank. LUSD saw an incredible trading volume that day, with sizeable purchases above $1.03, $1.04, and $1.05 as the market panicked. Amid the panic, some users are willing to pay a high price to fly to safety.


#### DAI and the PSM: solving overpegging, for a price

In its early days, before the Mutli Collateral Dai update, DAI had similar challenges to LUSD: it tended to overpeg. With the update, Maker introduced the Peg Stability Module (PSM) to manage the price stability of its stablecoin DAI. The PSM acts as a buffer between the market and the DAI ecosystem. It allows users to swap stable assets like USDC for DAI at a fixed exchange rate.

By adjusting the exchange rate in response to market dynamics, MakerDAO can influence the supply of DAI in the market and keep its price close to the USD peg. It helped MakerDAO resolve the DAI problem over pegging, observed before the PSM. Still, it came with a cost: an accumulation of USDC and other centralized stablecoins as DAI’s collateral.

![maker-psm](img/2023/stablecoin-marauder-map/maker-psm.png "$~1B of centralized stablecoins were accumulated as DAI collateral through the PSM")

#### FRAX's AMO (Algorithmic Market Operations): scale liquidity and risk to infinity

FRAX is a decentralized stablecoin that utilizes Algorithmic Market Operations to maintain its peg. FRAX employs an adaptive mechanism that adjusts its collateralization ratio based on market conditions. When the FRAX price trades above its peg, the system mints new FRAX and buys back collateral, increasing the stability of the peg.

Conversely, when the FRAX price falls below the peg, it reduces the collateralization ratio to encourage users to mint FRAX, which helps restore the peg. AMOs come with additional risks, mainly depending on the usage of the assets minted without collateral: the riskier their exposure, the bigger the threat.

The principal risks of such a design manifest when an issue with one of the services harnessed (usually money markets or DEX) arises. Say 10M FRAX are minted by the AMO and deposited into a money market to be borrowed by users. Now, the money market suffers an issue with one of its collateral and gets drained: there are now 10M more FRAX in open circulation with 0 collateral.

Mitigating this requires very active management of the AMOs - by humans, through a multisig, which is not ideal from a security perspective, as AMOs can mint FRAX at will with no backing.


#### crvUSD pegKeeper: a better PSM?

To ensure the peg-stability of crvUSD, Curve explored a path similar to the PSM, but slightly improved. Indeed, here, the need for users’ input is removed:

With Maker PSM, it’s still user-driven: when overpeg, users supply USDC as collateral to Maker PSM and mint DAI, helping to push its price back. If DAI was to underpeg, users could similarly buy DAI (below $1) to redeem it for 1 USDC, helping to restore its price to peg.

crvUSD works similarly at a high level (if crvUSD>$1 => mint, if crvusd&lt;$1 => burn) but does not require any input: the system stabilizes itself thanks to its pegKeepers contract. These special contracts can mint non-collateralized crvUSD under certain conditions and for specific use cases only.

There are 4 pegKeepers, each plugged into a different pool of crvUSD paired against a redeemable centralized stablecoin: USDC. USDT, USDP & TUSD. When crvUSD is overpeg, they can mint crvUSD to trade into the associated pool, helping to push crvUSD price back to $1. When crvUSD is underpeg, the pegKeeper can repurchase crvUSD on their associated pool (using centralized stable balances accumulated during overpeg) and burn it to push crvUSD’s price back to peg.

Thus, pegKeepers accumulate a crvUSD debt to the protocol when the stablecoin is overpegged, to be ideally resorbed once crvUSD is underpeg. The key here lies in the balance, ensuring that the spread between the supply of crvUSD (incl. Pegkeeper debt) and the borrowed supply does not grow too big.

![pegkeeper](img/2023/stablecoin-marauder-map/pegkeeper.png "Data from Curve Monitor")

While pegKeepers still pose a decent threat to the protocol, just like the FRAX’s AMO or Maker’s PSM, the risk seems more mitigated there. Yet, crvUSD is still quite a young stablecoin, and only time will tell.


### LIQUIDITY MANAGEMENT

Liquidity management, even just for a stablecoin, could be a good topic for a thesis. It’s one of the most misunderstood topics across the space. I wanted you, dear reader, to be aware of its importance.


#### Liquidity management as a non-topic

If you read this blog, you’ve likely already internalized that **liquidity strategies are the heart of the storm of the stablecoin wars.** Yet, many teams have yet to attain this realization. They picture it as something of low criticality that the DAO will handle later, which is incredibly dangerous.

Indeed, DAOs are not the best structure to manage liquidity, they tend to harness suboptimal solutions, overpay, and simply need more velocity to match the fast pace of the liquidity games. No surprise here; we’ve already established ages ago that **DAOs/governance are a good fit for strategical (long-term) orientations but inapt at mid/short term (tactics) management,** thanks to the example of MakerDAO (where, despite the absurdity of it, MKR holders are still voting on the vault’s interest rate, a purely operational parameter).

The obvious solution would be for the DAO to **appoint a liquidity committee** - a small team of liquidity specialists provided with a budget they can mobilize autonomously. The committee could be hired for a set term, while the DAO retains the right not to renew the committee or even revoke it similarly to other service providers.

I invite you to look at the main stablecoin projects run by DAOs and see which one has a committee yet. As far as I know, [only Aave is finally considering it for GHO](https://governance.aave.com/t/temp-check-treasury-management-create-and-fund-gho-liquidity-committee/14800). Besides the increased agility and operational capacity provided by the committee, it also enables the DAO to be more structured and forward-planning in its liquidity approach, allowing it to explore partnerships and collaboration with more relevant actors, such as supporting an innovative DEX from day one at launch, instead of the many months required to explain the relevancy of the innovation to the DAO’s stakeholders and have a budget being voted and implemented.


#### Competence is scarce

The hard truth about liquidity management is that competence is extremely scarce. This could explain why the topic needs to be better understood and rarely prioritized at the project's design stage or later in the governance discussions. An apt liquidity manager must have an accurate understanding of the following:



* Base liquidity structure model, x\*y=k
* Custom liquidity structures like stableswap
* Basic concentrated liquidity, UNIv3 style
* Uniswap liquidity management layer (Bunni, Merkl, etc.)
* CL liquidity manager model (Gamma, Arrakis, etc.)
* veCRV tokenomics & ecosystem // veBAL
* Vote marketplaces and bribe culture
* Advanced concentrated liquidity, Maverick style
* Maverick incentives model (Boosted Pool)
* Maverick tokenomics (veMAV)
* DEX Aggregator landscape and pathing logic

**The scope of tools, services, and protocols used for liquidity management is increasing exponentially, and very few actors are following closely**. It’s frequent to observe absurd spreads between the liquidity spending of two similar projects, with sometimes spreads of several orders of magnitude of difference in terms of $ invested / results.


## How to attract piles of ETH&LSDs onchain?

So far, we focused on stablecoins harnessing the CDP (Collateralized Debt Position) model, such as Maker, Liquity, or Reflexer, where users must deposit collateral to contract debt directly against the protocol (every borrower on a CDP protocol mints their “own” debt). It’s an elegant design that enables the protocol to implement various devices to absorb the volatility of the collateral, thus maximizing the price inertia of the stablecoin.


### The limits of CDP-based stablecoin

**Yet, CDP-based stablecoins come with one main downside: the over-collateralization requirement.** Indeed, it’s difficult, if not impossible, to dampen the volatility of collateral such as ETH without any margin of error. For instance, on Liquity, the minimum collateralization ratio tolerated is 110%, yet the average ratio observed on the protocol is 226.3%.

Overcollateralization is the central limit of the CDP model, and is hard to overcome. Indeed, lowering the collateralization requirement could attract more borrowers, increasing the risk scope of the stablecoin outputted. Thus, scaling a CDP-based stablecoin is a tough job. There are other relevant ideas to attract more borrowers, such as diversifying the collateral offering, as shown below. But here again, it comes with increased risks on the stablecoin, as seen with DAI, which observed a sizeable collateral degradation over the last years.

Nevertheless, many projects are exploring approaches that could result in a stablecoin with fewer compromises than DAI while achieving a similar scale. Let’s consider a few directions currently explored to scale decentralized stablecoin further.


#### Expand the collateral & chain offering: Liquity forks

2023 is the year of the Liquity fork: many protocols were launched this year, harnessing a model more or less similar to Liquity, with some twists. These include Gravita, Prisma, Lybra, and more.

##### Gravita

Let’s start with [Gravita](https://www.gravitaprotocol.com/), probably the closest to the base Liquity model. Here, the focus is put on making the protocol more attractive to borrowers, with several welcome additions, including the possibility of borrowing using liquid staked ETH like stETH or rETH as collateral or the protocol being made available on L2 like Arbitrum. Of course, it’s a game of balance here, as the rule specified above still applies.

{{< notice note >}}

**The conditions enforced on the borrowers dictate the guarantees provided to stablecoin holders**.

{{< /notice >}}

##### Prisma Finance

[Prisma Finance](https://prismafinance.com/) is also exploring a similar approach, another Liquity fork enabling the usage of ETH-LSD as collateral, built by a team close to the Curve/Llama ecosystem. Components of the veTokenomics are also envisioned on the fee-sharing/governance token PRISMA, but they still need to be made live.

##### Lybra Finance

Another team, [Lybra](https://lybra.finance/), experimented with a lock/escrow model on their governance token LBR. While it seems to have initially worked nicely to attract a sizeable amount of capital, the challenge with such tactics is to sustain them over time…

##### DYAD

Finally, let's talk about [DYAD](https://dyadstable.xyz/). This one is technically not a Liquity-fork per se, but more of a Liquity-inspired protocol, especially regarding the price stabilization mechanism of their stablecoin.

The main challenge they are trying to solve is onboarding new collateral on a live CDP protocol without expanding the risk scope of the base protocol more than it needs to. To do so, DYAD introduces a "Social Licensing Layer," essentially the governance layer.

Yet, it looks like none of the governance we're used to: here, there is no governance token, so that it won't be your usual plutocracy. Instead, governance power lies directly within the dNFT needed to use the protocol:  each dNFT gets to control a single "switch" for each proposed collateral type. 

They can change the position of this switch at any time from off to on or on to off and back again, as often as they want. A given collateral can comprise part of DYAD's collateral basket if it maintains a 2/3 supermajority of "on" switches. The only way to increase your governance power is to control more dNFTs.

DYAD also gets bonus points for preserving immutability as much as possible. While the protocol can be changed since it can onboard new collateral, the whole governance layer is immutable. DYAD is not fully live yet, only dNFTs are, but I'm eager to see how it goes!

I’m keeping with the majors here: LSDfi was all the rage a few months ago, and we’ve seen many protocols providing options to leverage ETH-LSD launching lately. While this sub-market is likely already crowded, there’s room for a CDP-based model delivering a stablecoin slightly less resilient than LUSD but with additional features. The question is which?


#### Be gentle with your borrowers: LLAMA/crvUSD

Another way to create a sink for ETH/ETH-LSD: make the conditions more attractive to borrowers / soften the liquidation penalties. Indeed, one of the main innovations behind crvUSD lies with the liquidation model that differs vastly from other services providing leverage.

LLAMA (Lending Liquidating AMM Algorithm) replaces the usual liquidations with “soft liquidations”, where underwater borrowers are rebalanced across “bands,” each representing a different price segment.

It provides a sizeable protection against liquidations stemming from brutal but unsustained market movements. Instead of the sudden liquidations we’ve been used to, LLAMA's soft liquidations are more gradual, as the collateral is progressively adjusted in proportion to its market price.


#### Make it rain: Dai Saving Rate & variants

Why even bother improving your design when there are more direct paths forward? MakerDAO pioneered this idea of offering a “risk-free” yield to stablecoin holders to drive the demand: the DAI Saving Rate, currently at 5%.

Sustaining it proves very costly for the DAO, which is increasingly pushed towards riskier but more lucrative collateral to keep afloat. A sizeable share of the collateral are now real-world assets (RWA) managed by custodians, some of which are slow or even fail to meet their yield or reporting obligations or simply sub-optimal (MakerDAO is currently earning 3% on its USDC while [retail can score 5% with Circle](https://cryptoslate.com/coinbase-raises-usdc-interest-rate-to-5/)).

Nevertheless, surprise, surprise: incentives work, at least at first. Thus, this brutal, low effort, and poorly efficient design over the long term is now spreading:



* [Raft launched a similar concept at 6%.](https://mirror.xyz/0xa486d3a7679D56D545dd5d357469Dd5ed4259340/1qSAAQtVdNCW_xn9cObEjwrQzFpwEshNrm0sjX0nkG8)
* Frax is also working on [sFRAX / Frax Saving Rate targeting 5%](https://gov.frax.finance/t/fip-2xx-sfrax-governance-proposal/2585).

![maker-dsr-impact](img/2023/stablecoin-marauder-map/maker-dsr-impact.png "Incentives work...")

Now, time will tell for the impact of such design over the long run. The way I see it, these protocols are **depleting most of their revenues to pay for acquisition on an ongoing basis** — they will lose most of the users acquired with DSR the minute they stop. They would have burned a massive amount of money to sustain the charade, money that could have been spent on strategic assets providing life-long incentives to the liquidity providers of their stablecoin, for instance. **This design is a great tactic but one of the most short-sighted strategies I have ever seen**.


## A shift to reserve-backed stablecoin?

A shift is brewing! While CDP-based models, such as Maker, Liquity, or Reflexer, are flourishing, **reserve-backed stablecoins** are also getting increasingly considered.

Indeed, as we highlighted above, there is an inherent tension in purely borrow–based / CDP stablecoins. To put it simply:



* Scaling a decentralized lending-based stablecoin requires attracting and retraining a sizeable amount of ETH / ETH-LSDs.
* But the more permissive the protocol is to borrowers, the less desirable the stablecoin its output will become.

The state of a CDP-based stablecoin depends entirely on its users' actions. Under the reserve model, the protocol directly manages the reserve and minting of stablecoins instead of individual positions. Thus, reserve-based models seem to offer a credible answer to CDP-based stable shortcomings, enabling the stablecoin supply to potentially scale more thanks to the native protocol reserve providing increased price inertia.

Let’s summarize this article by examining two prime examples of implementing a reserve-backed stablecoin model. I’ll keep it short and digestible and add resources for diving further.


### f(x): leverage with no fundind costs & 90% volatility dampened ETH

F(x) is a fascinating protocol freshly released! It’s a dual product, enabling stETH depositors to expose themselves to two types of assets in the proportion they desire:

1. xETH: a “high-volatility leveraged ETH”
2. fETH: a “low-volatility floating stablecoin”

Similarly to a CDP protocol, users deposit ETH (or stETH) to mint fETH or xETH. However, unlike Liquity/Maker/Other CDP, the user does not manage its position (a Trove). Instead, the protocol directly manages the stETH reserve. A redemption feature enables holders of fETH or xETH to reclaim the underlying stETH. However, how much they redeem depends on the system's state, most notably its Net Asset Value: the overall value of stETH in reserve.

![protocolfx](img/2023/stablecoin-marauder-map/protocolfx.png)

Launched just a few weeks ago, the protocol is still in its early stages with about 1300 ETH of TVL, and the liquidity on fETH is still being worked on. A third token, FXN, the governance token of the protocol, is also planned. 

The value proposition of both xETH and fETH is relevant to me and should be met with demand once the protocol is more mature. In my view, along with crvUSD, it’s one of the most exciting releases we got stablecoin-wise this year: I’m just waiting for the right time to experiment-ape into xETH.


### Liquity v2: protected LSD leveraging

“Liquity v2” (codename) is not live yet but has been [introduced by Robert Lauko at the last Stable Summit in June](https://www.youtube.com/watch?v=Zps__IMxtTs).

Like fETH, v2 will offer non-liquidatable leverage on ETH-LSD with no funding fee and even add downside protection. The novel, reserve-backed stablecoin the protocol will output is optimized for scaling. Its liquidity needs are also minimized since the protocol acts as a primary AMM for the stablecoin: users can mint and redeem the stablecoin for $1 of staked ETH.

V2 is being built in public: if you’d like to learn more about it or even get involved, make sure to come by the [Liquity’s Discord dedicated v2 channel](https://discord.gg/RCRp2CJR2S).


### Learn more on AladinDAO’s F(x) & Liquity V2

I kept it short on the reserve-backed stablecoins, as I will likely publish several articles focusing on this topic over the coming months. Meanwhile, feel free to get your alpha directly from the builder’s mouth — here’s a selection of articles & interviews to learn more about both protocols:



* [A recent community call, when Robert and I joined the AladinDAO/Protocol F(x) team to discuss decentralized stablecoins more broadly [60min]](https://twitter.com/aladdindao/status/1684141750900736000?s=20)
* [Community Call - Deep Dive into f(x) [30min]](https://www.youtube.com/watch?v=_xA6AFufGoQ&t=3871s)
* [f(x) protocol with Kmets and Crouger from AladinDAO (Leviathan News) [28min]](https://www.youtube.com/watch?v=Nzy7xO09SFw)
* [Introducing Liquity v2 — Liquity Blog](https://www.liquity.org/blog/introducing-liquity-v2)
* [Liquity v2 with Colin Platt (Leviathan News)](https://www.youtube.com/watch?v=KOnGCPE5gaU)


## KEY TAKEAWAYS

Liquidity management is the nerve of the stablecoin wars: observe & analyze the strategies deployed by the projects you monitor – their effectiveness is one of the main drivers of the success of the underlying protocol.

**👉️ TODO:** Follow the event surrounding GHO’s liquidity management on [Aave Governance Forum](https://governance.aave.com/) and try to articulate your thesis. If you can anticipate the repeg accurately, you get 3% of free profit waiting for your (GHO ~$0.97 to $1.00).

**👉️ BONUS-TODO:** GRAI, another stablecoin (Liquity fork), is currently trading at ~$0.985 with its redemption ceiling increasing over the next few weeks; a similar play can be considered there.

LSD-FI (protocols to leverage LSD) has been overcrowded over the last few months. Most protocols in the vertical are losing traction: 

**👉️ TODO:** Look at the incentive structure of protocols like Gravita, Raft, or Lybra, and confront it with their growth metrics — try to evaluate the incentive structure that seems persistent versus the ones losing steam.

After ~4 years of going autistic with the CDP-based model, it seems like the most savvy teams started to look another way.

**👉️ TODO:** Prepare for the future! Thanks to the resources shared above, deep-dive the reserve-based stablecoin models by getting familiar with protocols like f(x) or v2.

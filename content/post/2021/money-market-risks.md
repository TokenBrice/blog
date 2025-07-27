---
title: "Assessing risk in decentralized finance: a handbook for money markets"
description: "DeFi risk scoring is broken; this article shows you why with a clear breakdown of how to assess the risks of money markets; most of the observations are also applicable to DeFi protocols more broadly."
date: '2021-02-18T01:13:50.191Z'
categories: [DeFi, Discovery]
tags: [DeFi, Ethereum, Decentralized finance, DEX, Money Markets, Aave, Compound, Risk Scoring, Risk assessment, money market risk, aave risk, compound risk, cream risk, DeFiScore, CREAM, AAVE, COMP, Oracles, Liquidation, Insurance, Safety Module]
toc: true
tocNum: false
url: money-markets-risk
image: /img/2021/risk-tranching/cover.gif
---

Money markets are at the heart of DeFi. From a high-level perspective, yes, they simply enable the borrowing and lending of various assets. Yet **those functions are like the two primitive verbs of DeFi** at the base of pretty much all use cases.

There are three major money markets right now in DeFi: Aave, Compound & Cream. Yet all the following services use them, one way or another: Yearn Finance, Curve Finance, Alpha Finance, Harvest Finance, DeFiSaver, Saffron, 88MPH, Idle Finance, etc. To put it simply - **money markets are one of the root-level of DeFi**.

Money markets are amazing - simple yet very intricate. In this article, I try to provide a framework and some clues to assess the risk at different levels.

To dive more into the service layer currently being built on top of money markets, feel free to read.

---

## I/ Risk Scoring is Broken

Before we dive into the risk analysis framework, let's quickly discuss the current leading solution used to evaluate risk in DeFi: Consensys CodeFi DeFiScore.[^defiscore]

**DeFiScore is undisputedly compromised since it's still giving DAI a higher rate on [Compound](https://www.defiscan.info/protocols/compound-v3/ethereum) than [Aave](https://www.defiscan.info/protocols/aave/ethereum)** even with the oracle failure on the Compound side and the arrival of the Safety Module on Aave's side:

The Consensys CodeFi team was notified a few days ago[^1], acknowledged the issue[^8] but yet **refused any immediate to update the website even with just notice or disclaimer**. Instead, one of their members proposed a 500 USDC bounty open for anyone willing to update the formula[^2]. It has yet to be claimed.

It's no surprise that quantitative approaches so far have failed. They must achieve both sustainability (if the formula stays consistent it allows historical comparisons) and adaptability (yet the risk parameters are always evolving): it's not an easy feat.

I will not delve into the depths of risk scoring, as there is a dedicated article exploring what a decent DeFi-native risk scoring system looks like coming out shortly on this blog (hint: it does not exist yet).

---

## II/ Appreciating the Safety of a Money Market

I know it's painful to hear, but since quantitative analysis is unhelpful, you have to resort to a qualitative approaches for each project. The good news is there aren't many money markets in DeFi worth looking at:

1. Aave
2. Compound
3. Cream / Iron Bank

For each of these, you have to look at them holistically. I propose an approach that is **purely mine**, using **8 different dimensions all critical to the safety of assets** committed to the money market analyzed:

1. Protocol access & permissions
2. Oracles
3. Liquidation mechanisms
4. Collateral listing & risk analysis
5. Safety module
6. Expanded insurance ecosystem
7. Native token risk management
8. Community & Ecosystem

So what we have today is essentially a comprehensive framework you can use to assess the safety of a given money market. Feel free to challenge me on any item. Let's dive in.

{{< notice warning >}}
**Necessary Disclaimer: This is not investment advice.**

Almost no one is qualified to assess risks in DeFi: even "institutions" doing it like the DeFiscore are way off. 

This content is intended to help you better understand and appreciate the risk **<span style="text-decoration:underline;">by yourself</span>**, the most reliable way to do so.
{{< /notice >}}

---

### II.A/ Protocol Access & Permissions

At the very base level, you want to know who can update the protocol core parameters (-> the contracts), and the different limits associated with it.

For instance, there's usually a **timelock**, meaning that any significant change only applies after a set duration. For the administrative functions of the protocol, you need to make sure that they are **community-owned**, which usually means **governed by a multisig** of designed community members.

This section also includes everything related to **the "opsec" of the wallets/people** governing the multisig. "Opsec" is short for "operations security" - it's about the safety of everything digital interfaces related to the holders of these keys. Can they be hacked? Impersonated? Etc.

Such a matter is **<span style="text-decoration:underline;">CRITICAL</span>**, as we saw recently with the CEO of Nexus Mutual: his laptop was compromised, allowing the hacker to submit a fraudulent transaction on top of a real transaction he signed.[^3]

We have yet to see significant attacks based on social engineering in DeFi but expect them.

Transparency on the decisions of the protocol is key too: we address it below in the community & DAO section.

This article focuses on mature money markets like Aave or Compound. Newer projects might be less decentralized, and that can be a good thing - you might want some control and rollback options for a newer project.

#### Assessing the protocol accesses & decentralization

- __🔮Likelihood of failure__: Assess on a protocol/team-basis
- __🔥Loss of funds risk if failure__: Potentially all funds deposited on the market
- __❌Already happened?__ Not yet 🤞

{{< notice tip >}}
When it comes to evalutating opsec and decentralization plan, [Chris Blec](https://twitter.com/ChrisBlec) is your guy. He's uncompromising on opsec, and produced many helpful contributions on the topic:

You can find a **[summarized overview of the situation for the main DeFi projects here](https://docs.google.com/spreadsheets/d/13S7NRk1girTdQMajnVdU5JRlVO5BG_uJKhTO2Ef10b0/edit?usp=sharing)**
{{< /notice >}}

So to wrap this up, here are some good questions to ask to assess the safety of a money market at the protocol & permission level:

*   Who can update the contracts?
*   Do they have a credible opsec?
*   Any drain function in the contracts?
*   What do the administrative functions do?
*   How decentralized is the process to create a new lending market?

---

### II.B/ Oracles

Simply put, the oracles are the source for "outside truths". **Blockchains are only aware of themselves**, so for Ethereum, the price of ETH in dollars (or any other token) is technically an "outside truth" you need to bring on-chain in a **safe and verifiable manner**: it's precisely what oracles do!

It's essential, as the **perceived price** delivered by the oracle is the **source of truth for the protocol's liquidation decisions**. If the oracle says DAI is worth 1.30, then you are liquidated even if your DAI-borrowing position was safe on a $1 DAI and DAI is still actually worth $1 on the markets: the oracle is the source of truth. It happened already with Compound, so it's not a theoretical concern.[^4]

The good news here is that the answer is quite simple: [ChainLink](https://www.defiscan.info/protocols/chainlink-oracles/ethereum) is widely recognized as the most credible decentralized oracle solution, so any money market not using at least partly their price feeds is gambling with its users' money, as Compound did with significant lossses. It seems like the situation has not improved - despite the failure Compound still uses the same centralized oracle (Coinbase) and a proposal suggesting a switch to ChainLink was refused. [^compoundoracle]

#### Assessing oracles

- __🔮Likelihood of failure__: Significant (most impacting sub-theme to date).
- __🔥Loss of funds risk if failure__: market-based, potentially whole markets can be drained/affected.
- __✅Already happened?__ Yes, on Compound.[^4]

You can assess the oracles for a money market with the following question:

*   What is the source of truth for prices?
*   How reliable is that source?
*   Any history of abusive liquidation (stemming from oracle issues)?

---

### II.C/ Liquidation Mechanisms

The liquidation mechanisms are critical too, but they only happen once a liquidation can be triggered - which depends on the price the oracle returns. So the **liquidation mechanism cannot make up for a faulty oracle**. It's essential to first understand that.

Then, different money markets handle liquidations differently. They have different delays, fees, and restrictions with their liquidations. For instance, the Maker oracle/liquidation (internal system) has a one-hour delay to prevent flash liquidations during unsustained flash crashes.

Moreover, liquidation is not sudden neither an all-or-nothing event. There are several buffers to your positions, for instance on Aave, every token has a **maximum loan to value** and a **liquidation threshold**at least slightly higher.

So with USDC as collateral, for instance, there is a 5% spread between the two - the max LTV is 80% (*max $8000 worth borrowed from a 10 000 USDC collateral*), while the liquidation threshold is 85% (*= liquidation if collateral value &lt; $8500*)

![Aave USDC collateral parameters](/img/2021/money-market-risks/aave-usdc.png "The main metrics for USDC as a collateral on Aave.")

It gives borrowers using USDC as collateral another 5% margin so that even if the oracle reports $0.97 no abusive liquidations would occur. The situation is similar in other money markets.

#### Assessing liquidation mechanisms

- __🔮Likelihood of failure__: Mostly depends on the collateral price action - a flash crash could trigger a chain of liquidations
- __🔥Loss of funds risk if failure__: Significant (the money market can be potentially undercollateralized)
- __✅Already happened?__ Yes, on Maker where there were issues and delays with liquidations.[^makerCBT]

So here are some questions to ask yourself to assess the liquidation mechanisms:

*   When liquidations are triggered; what is the flow?
*   Any additional delay?
*   What are the liquidation fees?

{{< notice info >}}
There's another massive subtopic here: the **liquidations do not happen magically** - they are triggered by other users. So the incentives need to be on point there too so that liquidations do happen when needed and promptly. This topic is even more complex now in an age of high gas costs (liquidation profits vs gas costs of the tx). Skipping it for digestibility. 
{{< /notice >}}

---

### II.D/ Collateral Listing & Risk Analysis

Alright, now that we have a money market getting reliable prices and liquidating when needed, we can start looking at the tokens accepted as collateral and what is the process.

Assessing a token's health and overall safety is **one of the most complex tasks nowadays in DeFi** because figuring out the whole ecosystem around a token can be tricky. 

Take the SNX token, for instance, a major ERC-20 token. It's usable as collateral on Aave, but with quite a low maximum loan to value ratio (to be raised soon?) at 15%. Other ERC-20 tokens like LINK are in the 60-75% range.

Without diving too much into the details, this has to do with what you can do with each token and **SNX usage as collateral on the Synthetix platform**. 

<span style="text-decoration:underline;">Aave's risk parameters are conservative enough to essentially "front-run" Synthetix itself in the chain of liquidations if a black swan event was to happen </span>on Synthetix. It seems wise: a money market should not want to take higher exposition on a given token than the native platform itself.

Another way to look at it is the other way around: assess the overall "health" of the latest tokens added as collateral on the platform: are they liquid? Credibly decentralized? Etc.

You can also look at the overall collateral usage for any suspicious mismatch, like on Cream where almost a third of the deposits are FTT tokens (FTX exchange).

![Cream](/img/2021/money-market-risks/cream.png "Roughly 1/3 of the deposits on Cream are made of a single token, and it's not the one you'd want or expect to be here.")

#### Assessing the collateral listing strategy

- __🔮Likelihood of failure__: Depends on the collateral listing strategy risk appetite
- __🔥Loss of funds risk if failure__: If a dangerous token is accepted as collateral, the money market can potentially ends-up undercollateralized or even drained. For instance, Cream accepts COVER as collateral. The token suffered three infinite mint attacks already, exposing Cream to further risk.
- __❌Already happened?__ some tokens got minted to infinity, like COVER[^covershitcoin]. But they were used as collateral on a money market yet.

I won't expand more on this topic since Aave's risk documentation is very well done - check [the risk parameters section](https://docs.aave.com/risk/asset-risk/risk-parameters) for more information.

*   How are the collateral listing decisions made?
*   What risk framework is used for collateral?
*   How is the money market adapting to the changing circumstances of the tokens it lists?

---

### II.E/ Safety Module

Even if the risk is known at every level, **insurance is never an option and never supernumerary**. The first layer of defense is of course the platform-level if there is any compensation module.

The good news is that there is! Aave pioneered the field & even Compound has a reserve now. The second good news is that assessing the usefulness of this module is dead simple: it's a simple ratio between the total $ value of the borrows made on the money market and the total $ that can be mobilized by the safety module. 

Aave has roughly 2B in the Safety Module, of which up to 30% can be seized if needed = 600M. It covers both the V1 & V2 of the protocol. If the 30% on the slashing of the Safety Module is not sufficient, the safety module can mint additional AAVE tokens. Such a scenario is accounted for by neither Compound nor Cream.

![Aave's Safety Module](/img/2021/money-market-risks/aave-safety-module.jpeg "Overview of Aave's Safety Module.")

On top of insurance, money markets can also have reserves. Compound is the pioneer here, with about $10M in reseve[^compoundreserve]. Aave also has a reserve system that was recently launched, but I excluded it from the analysis considering the limited balance.[^10]

So looking at the available numbers, here are our quick maths:
`Safety Ratio = USD value of insurance / Total borrow on the money market`

1. **🛡 Aave =  53%** | $1.765 B (600M can be mobilized) in the Safety Module for $1.1B borrowed accross V1+V2 ($572M V1, $437M V2)
2. **🕯 Compound = 0.24%** | $4.3B borrowed on a $10M safety capital. 
3. **💀 Cream = 0%** | As far as I know, Cream has no or highly limited (low amounts) native insurance module.

ℹ Note: While Compound currently has no safety module, the team/DAO is currently sitting on a large COMP reserve that could be used to that end[^compoundCOMPstosk]. The maths were done on Feb 17 2021.

#### Evaluating the native insurance module

- __🔮Likelihood of failure__: Non-null, but not as relevant here. The SM is here to provide compensations in case of failure.
- __🔥Loss of funds risk if failure__: Depositors know they can get slashed if needed.
- __✅Already happened?__ Aave's pioneering the field. The slashing launched weeks ago. So far no events required Aave to harness the safety module, but it's great to know it's here!

To get a sense of how protecting the native safety and insurance modules are, here are some decent questions to ask:

*   Is there any native insurance module covering the platform?
*   How does it work?
*   What are the withdrawal delays & safeguards?
*   What's the coverage ratio (USD TVL exposed / USD TVL of Safety Module)?

---

### II.F/ Expanded Insurance Ecosystem

On top of the native insurance system of the money market, depositors and borrowers can **cover their positions through a third party insurance service** like Nexus Mutual or Unslashed.

The <span style="text-decoration:underline;">most widely covered risk is the one of a technical failure of smart contracts</span>. You will find covers for pretty much any widely used contract there is. Yet, **smart contract failures are not the only event that can lead to a loss of funds on a money market**.

Because of this, Robert Leshner the CEO of Compound can factually state the following[^5] while the protocol recently suffered 90M of abusive liquidations because of faulty oracles:

>Compound has been operating for close to 2 years with ZERO smart contract bugs.

It creates a false sense of security many are falling for, just like the period of operation of the protocol. Notice how I left it out of these 8 criteria? It's because it has close to zero relevance despite services like DeFiScore giving it an absurdly important weight.

{{< notice note >}}
I'm careful when I talk about "90M of abusive liquidations because of faulty oracles" but to be explicit - it affected negatively potentially any DAI borrower back then that might have gotten liquidated wrongly - losing a part of their deposit with **no recourse and no compensation** since Compound operated as intended (smart-contract wise).
{{< /notice >}}

On top of risks of smart contract failures, please consider the following list of non-exhaustive other risks that can result in a loss of fund: 

1. Failure or manipulation of an oracle, 
2. An issue with the smart contract of a token used collateral (such as infinite mint), 
3. A stablecoin used as collateral or borrowing asset on the market lose its peg 
4. The device or wallet of the admin of a not-so-decentralized service is compromised
5. Issues or delays with liquidations, meaning the money market can potentially no longer meet its collateralization requirements
6. etc.

Most insurance services are unhelpful with all these risks but for the risks of smart contract failures. The market for other types of risk is barely getting started thanks to Unslashed Finance now providing **coverage for the risk of stablecoins losing their peg** or custodian risk.

![Defiprime insurance](/img/2021/money-market-risks/defiprime-insurance.png "The different approaches to DeFi insurance --- FROM 2019 & but still somewhat instructive.")

To learn more about the different approaches for DeFi insurance, check [this piece from DeFi Rate](https://defiprime.com/comparing-insurance-like-solutions-in-defi). However please keep in mind the **massive bias here**: it was written more than two years ago by Hugh Karp, founder of Nexus Mutual. However, it's still factual enough and insightful to understand the different models.

#### Understanding insurances and the risk they truly cover

- __🎯Object__: Smart Contract Failure + stablecoin loss of peg.
- __💰Utility__: Provides compensation if a failure is observed.
- __✅Already happened?__: Nexus Mutual, one of the oldest insurance options already paid out on several situations.[^nexusmutual] 

So for the topic of extended insurances, you will want to look at services such as [Unslashed Finance](https://www.unslashed.finance/), [Nexus Mutual](https://nexusmutual.io/), or [Cover Protocol](https://www.coverprotocol.com/) and the plans they offer.

*   What are the options available through the ecosystem to cover a position on the money market?
*   What are their pricing and reliability (paid out already?)?

---

### II.G/ Native Token Risk Management

We discussed quite a bit about the various tokens used as collateral, but there is one you need to watch extra carefully: the **native token of the money market**. So that's the COMP token on Compound, AAVE on Aave, and CREAM on Cream.

{{< notice info >}}
The maximum Loan to Value (max LTV) dictates the borrowing power of collaterals. A 50% max LTV means one can borrow up to half to the dollar value of the collateral deposited.
{{< /notice >}}

The very first layer is of course to make sure that there is no fool play: **the money market must be neutral and not favor its own token**. It seems obvious, but it's not a given. Cream allows an excessive 75% max LTV on CREAM, one of the highest of the whole protocol - as high as some stablecoins. Compound itself gives COMP a permissive 60% max LTV while Aave is more conservative at 50%.

{{< notice tip >}}
If the money market is healthy and the token well designed - people should be bullish on it, meaning some of them use it as collateral to long it - aka depositing AAVE on Aave to long AAVE.

Unsurprisingly, despite the permissive LTV, COMP's and CREAM's longs are rarer than AAVE's.
{{< /notice >}}

#### Assessing how a money market manage its native token risks

- __🔮Likelihood of failure__: It's an all or nothing event: the money market can play with fire on its native token for months with no consequences before the situation eventually blow up and the token + the money market crumble together.
- __🔥Loss of funds risk if failure__: The loss can potentially be system-wide (whole money market affected).
- __❌Already happened?__ Not yet. But Cream is already way beyond any reasonable max LTV figure on the CREAM token.

And here are some considerations worth exploring:

*   Look at the health of the native token of the platform: token contract, liquidity, integrations, etc.
*   Look at the native token usage on the protocol & assess the health of its market
*   Ownership, distribution, and Gini coefficient of the governance token

So far, we've focused on the money market themselves. Yet, they are community-driven & governed projects, so their community & integration within the ecosystem are an essential part of the assessment.

---

### II.H/ Community & Ecosystem

In DeFi, communities are essential. It's not a "nice-to-have" to make the protocol more attractive, it's a **core feature** and I assess it as such.

On such a topic, again, no metrics will help you just by themselves. The gist is to get a sense of how dynamic the community is. It usually translates into its core components: the DAO, the Discord, and the overall presence in the space.

Another consequence of a healthy community is **widespread support and usage across the ecosystem**, with many services and products built "on top of" the protocol examined. Here despite Compound's lead being the first mover, Aave is also now a prime choice for any new protocol building a new financial primitive.

Indeed, teams can purposely foster such an environment simply by having members accessible and involved in the space. Besides, Aave has an **ecosystem grants**[^aavegrants] initiative helping to fund projects built on top of Aave such as [APWine offering fixed yields](https://tokenbrice.xyz/content/posts/2021/firp-apwine.md). Other community-related initiatives are a healthy tell, such as hackathons, AMAs, livestreams, etc.

Again here - make sure to **assess the quality, not the quantity**. It's easy to rush out all the initiatives listed above. But doing it right, in a way that makes sense for the community and pushes it forward is much harder.

I don't want to make this a case against Compound, but here again, it's so obvious. While Compound community fundings are quite limited the grants program just launched[^6], its founder Robert Leshner is an active venture capital investor, with the Robot Ventures funds[^7].

![Robovc](/img/2021/money-market-risks/robovc.png "RoboVC & its main investments.")

#### Assessing the community & DAO of a money market

- __🔮Likelihood of failure__: The community is the most important feature of all for the long-term success of the money market.
- __🔥Loss of funds risk if failure__: Long-term risk. If a money market loses the community favors, it's not gonna be a dramatic event but more of slow and painful threading into irrelevance for the given market.
- __✅Already happened?__ Yes, with Compound - they lost their top of mind position and preference for several reasons, such as their lack of support for the ecosystem, the DAI Market Oracle issue & the team reaction to it.

So here are some questions and clues to help you assess this last yet essential part:

**At the DAO-level:**

- How does it work to submit a proposal? 
- How are they reviewed and improved? 
- What's the delay between the vote and the execution? 
- Any proposal that was ignored or not implemented for a long time?

**Core team members:**

- Are they legit? Involved in the space? Giving back? Advising?
- Background-check: any involvement with a scam? What were they doing before?
- Present-check: on top of their involvement with the money market, what are they doing? Any potential conflict of interest?

**Ecosystem**

- Documentation & support: how hard is it to build on top of this money market?
- What are the services built on top of the money market? Are they widely used?
- Are they communicating clearly on risk parameters? Do they have non-technical/non-dev risk-focused documentation?

---

## III/ A note on DeFi Tribalism

Exploring such a topic was insanely insightful for me, at so many levels. I remain quite surprised by the tribalism of the space: apart from Aave, gathering the information presented in this article was not a trivial task.

Because of the question I asked and the observations I shared, I've been the target of personal attacks from founders of some of the teams mentioned in this article. Others were quite misleading and selective in their answers. I received no answers from both Cream & Compound official accounts or teams.

Such attitudes gave me even more will to push this article forward. **Beyond the technicalities of each protocol, I think the attitude of the founding team is essential too**. On this front, there is a protocol that stands an order of magnitude above any other: surprise surprise, it also happens to be the most technically sound, secure, integrated, and exciting, and interesting. 👻

---

### III.A/ Limitations of this risk assessment approach

I anticipate strong reactions already, so let me add a few more topics not addressed here:
1. While we went quite deep, we did not discuss the tokenization process: the process used by the protocol to represent the assets deposited. On this front, **both Compound and Cream are using an archaic approach** that was topped on all fronts by Aave with the first release of the aTokens in early 2020.[^aTokenMasterRace] Aave V2 further improved the tokenization process.
2. Cream by itself is a small market, but **through the Iron Bank other protocols can borrow from Cream**. Assessing the risk on such a market is even harder - and it was excluded from this analysis. To learn more about the real risk already posed and manifested by such an approach, you can check the [latest Rekt on Alpha Homora](https://www.rekt.news/alpha-finance-rekt/).
3. While MakerDAO provides a service functionally equivalent to lending, the process is significantly different since each borrower is minting DAI. So for the sake of simplicity, I've mostly excluded MakerDAO from this analysis, but for a few meaningful examples.
4. I have no affiliation whatsoever with the Aave, Compound, Cream, or any other money market. However, I do own AAVE tokens (that I purchased myself on the markets) and stake them in the Safety Module. All the content hosted on my blog is made accessible for free - I am the sole editor.

I hope this article helped you get a better grasp of the scope of risks in money markets. I want to stress again that it's non-exhaustive, nor absolute truth but I do firmly believe provides clear and useful contributions to make sure risks in DeFi are broadly understood, better than what currently exists.

If you do not agree with this statement, feel free to challenge me. **I'm eager for facts disproving my observations: it would mean DeFi is safer than I thought.**

---

Reminder: this blog is **[one of the few websites of the space not pillaging your data](https://tokenbrice.xyz/content/posts/2020/hello-world.md)** through the usage of Google Analytics and the likes.

## IV. Notes & References

You can find additional information on each fact, event or figure mentioned in the article through the footnotes:

[^1]: I pinged them on Twitter and [suggested many obvious improvements](https://twitter.com/TokenBrice/status/1360296967939772423?s=20) anyone with some DeFi experience could have provided.
[^2]: Feel free to reach out to him if you want to claim the 500 USDC bounty! [Here is the tweet](https://twitter.com/jack_clancy93/status/1360305374033682436?s=20)
[^3]: To learn more about this attack or any other in the DeFi space, **[check the Rekt](https://www.rekt.news/nxm-hugh-speaks-out/)**
[^4]: Find **[more info about the 89M DAI oracle abitrage on Compound here](https://decrypt.co/49657/oracle-exploit-sees-100-million-liquidated-on-compound)**
[^5]: Yes he's factual since the contract never failed so far. However for less technically-savy people, it can read like Compound never suffered any loss, which is not the case. **[Robert Leshner Tweet](https://twitter.com/rleshner/status/1358566161361821696?s=20)**
[^6]: The proposal for Compound Ecopsystem Grants was [executed two months ago](https://compound.finance/governance/proposals/30).
[^7]: [RoboVC](https://robvc.com/): It funded several services harnessing Compound (like InstaDapp or Multis) & Compound itself.
[^8]: Jack, one of their engineer recognized that [the case of Compound DAI score > Aave is not defensible.](https://twitter.com/jack_clancy93/status/1360304560846364672?s=20)
[^9]: [Developper documentation on cTokens reserves](https://compound.finance/docs/ctokens#total-reserves)
[^10]: There are around $450K worth of tokens collected in the reserve as of now: [Aave's reserve factor documentation](https://docs.aave.com/risk/asset-risk/risk-parameters#reserve-factor)
[^defiscore]: From the get go, the formula used was abitrary, suffered dozens of obvious flaws and was rigged in favor of Compound through the ridiculous importance given to the time of operations. In my humble opinion, the [DeFiScore](https://defiscore.io/)'s main goal was Consensys' promotion. If at least, they had done the work...
[^makerCBT]: The MakerDAO team published a [write-up](https://blog.makerdao.com/the-market-collapse-of-march-12-2020-how-it-impacted-makerdao/) after the events explaining what happened.
[^aavegrants]: The first round of [Aave Ecosystem grants started about a year ago](https://medium.com/aave/aave-ecosystem-grants-88260ede1485)
[^nexusmutual]: You can follow the [claims and payouts on Nexus Mutual here](https://app.nexusmutual.io/claim-assessment).
[^compoundreserve]: Each cToken stores reserves (insurance), there's $9.4m (and growing by over $100k/day) [Robert Leshner Tweet](https://twitter.com/rleshner/status/1358566161361821696)
[^compoundCOMPstosk]: Compound is also sitting on a 4 million COMP (roughly $1.8b) chest that could be allocated for insurance [Robert Leshner Tweet](https://twitter.com/rleshner/status/1358569634618867714?s=20)
[^covershitcoin]: Cover is an insurance protocol unable to secure their own token contract and liquidity mining program. They got attaked three times already. Here are [some info on the last one](https://coingape.com/cover-becomes-latest-defi-protocol-to-get-exploited-price-crashes-by-77-within-an-hour/).
[^compoundoracle]: Despite the attack occuring several weeks ago because of their reliance on Coinbase centralized oracles, it seems like [the situation has not been fixed yet](https://twitter.com/ChainLinkGod/status/1362132404484198401?s=20).
[^aTokenMasterRace]: The case for aTokens' technical superiority could be the topic on an article by itself but here is the gist of it:
	
	1. **Simpler**: aTokens maintain a 1:1 ratio against the base asset while cTokens have an increasing exchange rate against their base assets.
	2. **Easier accounting & integrations**: aTokens 1:1 correspondence makes them much easier to interact with - there is no need to fetch any additional data. With Compound, any service interacting with cTokens needs to fetch the corresponding the cToken/BaseToken exchange rate.
	3. **Dynamic and understandable interest**: both a & c tokens accrue interest dynamically. However, here again, because of aTokens' more elegant and straightforward design, the experience is more fluid with aTokens (deposit, reassured by 1:1 correspondence, number go up) 
	4. **More potent integrations**: aToken allows for novel use cases, especially if you take into account the other features of Aave. For instance, there is a Yearn vault harnessing aLINK to borrow USDC from users' deposits to farm with them and settle the income for more aLINK. 

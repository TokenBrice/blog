---
title: "🎲 PoolTogether: The story of the no-loss lottery where everyone wins"
description: "Gambling, all rotten? Once again, decentralized finance allows us to consider new ways of doing things - in this case a less predatory and more fun lottery: PoolTogether. This article explains how it works."
date: '2021-12-20T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Understanding]
tags: [DeFi, Ethereum, POOL, PoolTogether, Lottery, Sports betting, money games, betting games, gambling]
toc: true
tocNum: false
url: pool-together
---

DeFi has enabled the emergence of an alternative financial system built on fundamentally different foundations: transparency, open-source, composability and resistance to censorship. Many use cases have emerged and it is now possible to buy and exchange tokens without a centralized intermediary, but also to lend or borrow and much more!

The topic of the day, PoolTogether, goes one step further: it uses and assembles different DeFi services to offer a new kind of "money game", which is more fun, but also more instructive and much less dangerous and harmful than its classic counterpart.

I offer you to explore this protocol in detail: we start with its context, before analyzing how it works and the different issues it involves. Let's get started!

![tokenbrice-pooltogether-cover](/img/2021/pool-together/cover-EN.png)

---

## The context: limits and dangers of the classic lottery

This chapter is almost hard for me to write because it is seems so obvious, yet it is still very poorly perceived by the majority of people. Concretely from a societal point of view, the lottery is probably as deleterious as smoking. Consider:

1. By its design (possible and promoted jackpot), the **lottery targets the most vulnerable populations**.
2. Despite this, the **expectation of winning is negative**: players lose money while playing for most of them.
3. There are also **serious consequences for the winners**, it's a complex experience and [many end up broke after a few years](https://www.businessinsider.com/lottery-winners-lost-everything-2017-8?IR=T). Regular gamblers also suffer from addiction problems.
4. The lottery was wildly taxed and owned by the state... until now. **Privatization means giving the profits from an activity that is clearly harmful to society to private companies** - the comparison with smoking makes even more sense!
5. Finally, and this is not specific to the lottery but **equally miserable, denounceable and pitiful**: gambling often targets the most vulnerable populations for their advertising and [and particularly on young people](https://www.theguardian.com/society/2020/mar/27/children-more-likely-to-become-gamblers-due-to-high-volume-of-betting-ads).

![winamax-pub](/img/2021/pool-together/winamax-pub.jpg "Example of advertising in France: 'Tout pour la daronne', which means 'Everything for your mama'")

You can have a look on the full film advertisement created by TBWA, France for Winamax [here](https://www.adsoftheworld.com/media/film/winamax_the_mama)...

### Addictions, dependencies: consequences

What follows is logical, mechanical and despairing: in the long term trend, bets are exploding despite a declining number of players:

![stats-fdj](/img/2021/pool-together/evolution-2007-2017.png)

The subject is complex and, like smoking, often documented and researched by the gambling service providers themselves. The numbers speak for themselves, however: about 17% of gamblers are potentially at risk of addiction or dependency.

![addictions](/img/2021/pool-together/addictions.png)

"_In 2017, Internet gambling (lottery games, horse or sports betting and poker) accounted for 11.2% of total spending, a share that has been steadily increasing since its authorization in 2010_" according to the French Observatory of Drugs and Addictions.

Other statistics are simply hopeless but ultimately understandable: **the more social and economic misery increases, the more the promise of the lottery jackpot attracts the gullible**, thus increasing the privatized winnings of the FDJ (the operator of France's national lottery games) and others, and destroying the social fabric ever more.

We'll stop here, but you'll have understood: when you get out of the studies financed by the FDJ or associated, you quickly realize the extent of the social break that the lottery causes. The 22.7% returned to the communities is clearly not enough to compensate the real costs of this "game" (ruined lives, addictions, suicides, broken families, etc.).

#### Promotion of a deleterious social novel?

Finally, to finish this picture that sets the context, I propose a last more subjective point: what about the impact of the lottery on the **social novel**? The social novel is like the American dream: a fable that constitutes one of the foundations of the construction of the national identity (in this case: everyone can succeed in the US if they work hard enough).

It is a real collective delusion, but it contributes to **defining the imaginary associated with success in a given society.**

So let me ask the question: what impact does the lottery have on our social novel? Again it is rather negative I think, because it feeds the fable that to be successful you have to be born into a good family, or "lucky" -> become a celebrity / play high level sports or lottery. **The classic lottery thus feeds the emptiness of our contemporary aspirations:** one more factor contributing to the ambient mediocrity.

But now we are done with that. Let's get to the heart of the matter and see how PoolTogether reshuffles the deck.

## The basics to understand the concept

The principle of PoolTogether is basically quite simple, but there are also many details and subtleties that need to be figured out to really understand what the protocol aims to do.

In DeFi, there are different sources of return, for example a USDC owner, a stablecoin, can lend it to others to generate a return via a service like Aave or Compound. **Basically, PoolTogether is a playful abstraction layer built on top of such a source of returns.** At a high level, it looks like something like this:


1. Players deposit USDC into the USDC pool on PoolTogether - and receive a corresponding token to recognize their deposit (PTaUSDC)
2. The pool (set of smart contracts) deploys the assets in different strategies to produce a return. The return is collected and used to fund the winners' prize.
3. Each USDC deposited in the pool (⇒ PTaUSDC) corresponds to a potential winning lottery ticket. Every day, an auditable random draw (ChainLink VRF) is held to determine the many winners, with 3 initial prize ranges: 10 PTaUSDC, 100 PTaUSDC or 2500 PTaUSDC jackpot.

It's this infrastructure that produces a return - and puts only the return into play that qualifies Pool Together as a **no-loss** lottery. At any time, **the player can stop playing: he will get back at least his initial committed capital**, if he has never won the lottery, or more.

If we want to be very precise, the only cost of Pool Together is the "opportunity cost of capital": the potential lost opportunity on the mobilized capital, which could theoretically produce a better return otherwise.

---

## PoolTogether v3: the POOL token, sponsors and community pools

Two versions of PoolTogether are online: v3 and v4. The concept remains the same but the infrastructure has greatly evolved. So before we look at what v4 has brought, let's start with the still relevant v3 and [accessible here](https://app.pooltogether.com/).

This update was released [in October 2020](https://defirate.com/pooltogether-v3/) shortly before [the POOL token](https://medium.com/pooltogether/introducing-pool-23b09f36db48), in February 2021. It brings many improvements to the PoolTogether infrastructure.


### Sponsoring Pools and Reserve Factor

While the schematic explanation of earlier is useful, two initial subtleties must be added: sponsorship pools and the governance-controlled reserve factor.

1. Let's start with **sponsoring**. The idea is to allow "non-player capital" to increase player earnings: this capital contributes to the output produced, but has no chance of winning. At first this was envisaged from a rather voluntary perspective, but with the launch of the token sponsors are now eligible for POOL rewards.
2. The **Reserve** system is even simpler: each pool has a _Reserve Factor_ which corresponds to a % of the return captured by the pool directly. These funds are used to guarantee the sustainability of the protocol.

With v3, we also saw the arrival of _Community Pools_, pools created by the community directly on the tokens of their choice, as long as they have a source of return, as well as many other additions that were more or less successful.


### 3,3T, Lootboxes & PoolTogether on Polygon


For example, Olympus DAO offers a _3,3 Together_, where players stake their OHM rebase: every three days the rebase of all players is distributed to the three winners.

They also had other innovative ideas in v3 but they didn't catch on, mainly because of the gas costs of the mainnet. For example, each pool has its _Lootbox_ which allows anyone to add an arbitrary token as a prize or even an NFT! Just send it to the lootbox address and when the next prize is distributed the NFT/token is automatically sent to the winner.

The v3 also marked the arrival of the POOL token a few months later and its airdrop which we will talk about below.

Finally, v3 also marked the arrival of PoolTogether on other channels like Polygon or BSC. Nevertheless this logic has its limits because it also leads to a fragmentation of liquidity.

---

## PoolTogether v4: Tsunami with innovative cross-chain approach

The v4 is a very important iteration on the base proposed in v3. Here, the experience has been simplified and reworked to make it as accessible and fun as possible: and it works! Let's see how.

### Cross-chain egalitarian approach

We will detail this point because it is crucial, PoolTogether was a pioneer in this field and it is a dimension that we find on all projects: **the cross-chain strategy**. It aims to offer the same service, whatever the channel used by the user. I'm coming to that, but before I do, let's take the time to understand the classic cross-chain replication approach and its consequences.

#### The basic approach: replication
Most projects simply **replicate their service on all channels**: this is the case of Sushi for example, which is present on more than ten channels, but also Pool Together v3 as described above. 

This approach has the merit of simplicity and allows access to the service on all covered channels - but it results in **fragmentation of liquidity** which can make this service less qualitative on "small channels". Thus PT v3 Polygon USDC players, now few in number, play for a weekly fee of $69. On the other hand PT v4 USDC players share a daily price of over $100,000.


#### Tsunami

With PoolTogether v4 comes the so-called Tsunami model where all chains are equal. To do this, PoolTogether introduces an abstraction layer between all chains to redistribute prices if necessary.

This allows **mutualizing depositors' funds across all chains** to offer one big attractive prize rather than multiplying pools and dividing prizes. One consequence is that players on Polygon (where the gas cost of depositing is marginal) can play with the same odds and payout expectation as mainnet players.

So of course this requires more development and implementation work and there are consequences for players as well, the most notable being **a one day delay between initial deposit and eligibility for the first draw**. But this is not too much of a trade-off considering the fact that PoolTogether is intended to be a game that promotes long-term savings.

### Adjustment of the pricing model


Where v3 opted for flexibility, with pools having daily or weekly draws, the unique v4 pool can afford a **daily draw** given its size. In addition, the prize structure has been revised to allocate more small prizes to make the experience a little less random in the long run.

![prize-breakdown-old](/img/2021/pool-together/prize-breakdown-old.png "First PTv4 prize distribution logic")

The jackpot logic is preserved with the first and only winner pocketing $2500 anyway, but there are also nearly 720 other potential winners with the $100 and $10 prizes.

![tokenbrice-pooltogether-winning](/img/2021/pool-together/winning.png "Approximately 2 weeks worth of 5000 PTaUSDC draws")

In reality, the number of winning players is lower because it is possible to win several prizes at once. However, this approach also smoothes out the income for large depositors, who frequently win $10 or $100 rewards, potentially even every day if the deposit is large enough.

This distribution allows for frequent rewards for players who use PoolTogether for savings purposes while maintaining the spirit of the game:

1. A decent chance (depending on the size of the deposit) to have small winnings ($10 and $100 prizes) 
2. A small chance of a massive payout: the $2500 jackpot.

Beyond the prize model, the whole experience around prize allocation has been reviewed with v4. The governance has continued to iterate and recently voted on an overhaul of the prize structure: [PTIP-47: Prize Adjustments](https://gov.pooltogether.com/t/ptip-47-prize-adjustments/1752).

![prize-breakdown](/img/2021/pool-together/prize-breakdown.png "The new prize distribution")

### A more satisfying experience.

Many settings and details have been adjusted to make the winning experience more fun and enjoyable. The complete list is on [the PoolTogether documentation](https://docs.pooltogether.com/faq/v3-to-v4-differences), so we'll just mention the essentials.

First of all, the winnings go into a **claim logic**, where before they went directly into the wallet. This makes it easier for players to understand and quantify winnings. In addition, they are now paid out in PTaUSDC, the PoolTogether v4 lottery ticket, and are therefore **automatically compounded**: winning increases your chances of winning, with a simple claim!

![comparison-pt-vs-savings](/img/2021/pool-together/comparaison.png "Pooltogether vs savings")

**Players have 60 days to claim their reward**, which guarantees a form of follow-up and commitment, but also allows an almost totally passive interaction with the protocol for those who wish to do so: deposit > every 59 days: claim > withdrawal when desired.

---

The POOL token has been mentioned several times without digging into it: this was deliberate. Now that the system is clear to you, I propose to finish by analyzing its value proposition.


## The POOL token

We will talk about airdrop of course, but also liquidity and of course governance: let's go!

### Airdrop: everybody won!

To launch the most fun token of the DeFi, there couldn't be anything else than an airdrop obviously. This is one of the retroactive airdrops that followed in the wake of Uniswap, but still came early enough that it wasn't overly abused by the infamous airdrop hunters.

**14% of POOL's total supply** was distributed to players who participated before January 14, 2021, with weighting based on deposit amount and duration. This was a nice surprise for early adopters, even with small amounts.


### POOL incentives and LP (v3)


Who says token also means most often incentives: PoolTogether is no exception to the rule.

With the token came POOL incentives for all players; as well as adjustments to the sponsorship model described above. There is also a liquidity issue on the POOL token now.

After starting with a classic incentive model for LPs, governance decided to explore a model that allows the protocol to [control its own liquidity (PTIP-40](https://gov.pooltogether.com/t/ptip-40-olympus-lp-incentives-pool-pool-distribution/1638) through bonding (Ohm-like).


### Define the "FunTogether"!


The POOL is used to take part in the protocol decisions and help to refine the model. Furthermore, the implementation of the governance itself is also fun. In order to vote, you have to deposit your POOL tokens in the POOL pool on PoolTogether: while having a basic return + chances to win prizes, players can thus vote on governance decisions.

I sometimes call PoolTogether "the most fun protocol in the whole of DeFi", a true statement but one that can be taken even further.

PoolTogether governance, with its decisions, works to define what is "optimal fun", with very concrete questions, like the number of prizes or their distribution. With the launch of v4, the number of prizes has greatly increased, allowing more players to win: more than half of the unique wallets playing PTv4 have won at least once:


<div align = "center">
{{< tweet 1463642952778014726 >}}
</div>
    
It's a good start, but there's probably room to refine the model even further to delight more players by positively promoting long-term savings. 

---


If you've read me this far, would you like some more alpha? 

**PoolTogether's lossless logic is exported beyond the lottery / savings**. Many social mechanisms and games around money can be involved: sports betting, prediction markets, insurance, etc. The lossless family will be large, and PoolTogether already knows a first cousin that tackles predictions markets: [EntropyFi](https://docs.entropyfi.com/user-guide/game-explained).

Place your bets, 
- 🎲 no more bets ! [archaic logic]
- (🎲,🎲) and have fun :) [web3]

_🙏Thanks to Th. for helping translate this article into English._
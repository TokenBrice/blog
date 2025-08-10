---
title: "Volume begets fees: how are the main decentralized exchanges capturing value?"
description: "A look at Uniswap's, Sushiswap's and Curve's value capture mechanism to better understand how value accrues for token holders."
date: '2021-01-23T01:13:50.191Z'
categories: [DeFi, Discovery]
tags: [DeFi, Ethereum, Decentralized finance, DEX, Decentralized Exchange, Uniswap, Sushiswap, Curve, Curve Finance, Balancer, Bancor, CRV, UNI, SUSHI]
toc: true
tocNum: false
url: decentralized-exchange-value-capture
image: /img/2021/dex-value-capture/cover-fr.png
---

I've shared my perspective on many DeFi protocols on this blog, but recently I realized I've never gone back to the basics: the DEXs. That's precisely what we will do today, tackling the topic mostly by looking at value capture mechanisms.

AMM-based DEXs like Uniswap, Curve or SushiSwap all grew tremendously both in available liquidity and volume this year, and so did the fees they collected. To put it simply: **these DEXs now are the main fee-collectors there are in crypto, right after the Bitcoin and Ethereum network themselves**:

![crypto-fees](/img/2021/dex-value-capture/fees.png)

It's quite an impressive achievement! So today we'll look at this yummy cake and understand how it's split. What's the different approaches? What is their token used for / how do they establish their incentive model? And then how will the arrival of layer 2 impact all of that?

---

## The rise of Automated Market Maker (AMMs)

With all the discussions around automated market makers (AMMs) lately, I wanted, as usual, to take a step back and consider the current state of the market, the position of the main players and what's coming next.

We'll discuss AMMs but I'll leave the technical details of the bonding curves to others. Instead, we will address the topic from a value capture and tokenomics perspective. 

**The rise and development of AMMs fundamentally changed the market**. Before their dominion, order-book based approaches were still widely used. One of the main merits of AMMs is to change the logic of the service, as it becomes **peer to contract**: there is no need for a matching order on the other side, thanks to the bonding curve, there's always one (within pool liquidity & slippage limits).

I think it's one of the key factors that enabled them to grow as they streamlined everything related to token exchanges: from the act of swapping itself, but also liquidity providing and even things like fetching a price for assets.

So we have our beautiful DEX-commissions-cake, now let's dive into the main services' value capture mechanism to better understand their main differences.

{{< notice note >}}
For the sake of the simplicity of this article, we won't address Balancer and Bancor models. It might be a good follow-up piece.
{{< /notice >}}

---

## Value capture mechanisms in discovery mode

Through the different iterations and releases of the main DEXs, their value capture mechanisms evolved. Initially, there was not necessarily a token and a share of the exchange collected fee captured by it.

### Uniswap: The need for liquidity

Indeed, in the first days of the AMM, the main concern was liquidity - still very scarce back then: Uniswap had no token and no need for it to pioneer the AMM-front. The initial and still current fee distribution infrastructure matches this requirement: a **30 bps fee (0.3%) is taken on every trade and distributed to the liquidity providers**. 

It was a perfect fit to start as you have a liquidity chicken and egg problem to begin with: sufficient liquidity will enable swaps without too much slippage, driving volume (if there's need for the given token/market) and therefore revenues for LP.

There is currently no fee or value capture at the token-level but it's **ready to be implemented** if the DAO was to decide it - the V2 of the protocol shipped last year includes a `Protocol fee` feature.[^1]

### SushiSwap: Value capture to the token

Since the early days, one of the core changes of SushiSwap was a slight reduction of this fee to 25 bps to **redirect the 5 bps left to SUSHI stakers.** This enables SUSHI stakers to get a share of the fees collected on all pairs, instead of liquidity-pair based distribution only.

Since the initial distribution phase, there were several adjustments made but the mechanism is roughly the same. Onsen introduced a rotational reward system onboard relevant new pools. More importantly for the tokenomics, ⅔ of the SUSHI rewards earned through liquidity mining are now vested over a 6 months period.

![sushiswap-onsen](/img/2021/dex-value-capture/sushi-onsen.png)

This vesting reduces the incentives for "mercenary liquidity", especially for liquidity managed by a vault for instance & helps to **make sure that large liquidity providers are also SUSHI holders at all time** (even up to 6 months after they're done farming), better aligning interests.

To achieve this split, SushiSwap distributes a 0.25% fee for each swap to LP, just like Uniswap's 0.30%. On top of this fee, another 0.05% fee is collected on each swap in form of LP tokens, and settled for SUSHI distributed to the stakers.

The improvements brought by Sushi are relevant, yet in my eyes the real game-changer is the Curve model, so let's have a look at it.

---

## A peek at the endgame? Curve Finance & CRV

Curve's model is slightly more complex than the previous but results in an ever better alignment of incentives between the platform users and the token holders. Let's see how.

Since the launch of the CRV token, liquidity providers on Curve have been earning CRV tokens on top of their usual commissions (if they stake). And just like SushiSwap, Curve's introduced a form of value capture at the CRV-token level. 

![Curve pools](/img/2021/dex-value-capture/curve-pools.png "Overview of the main pools pools on Curve")

Yet the model is more intricate so let's discuss each part and see how they interact with one another.

### 1/ Tutorial : The Timelock

To make use of CRV tokens within Curve, the first choice one has to make is the length of its commitment. The base unit is veCRV, a time-weighted locked CRV enabled for governance. To be explicit: **to be eligible for the fees collected and other features discussed below, you need to lock your CRV token for at least 1 year.**

The mechanism is quite straightforward, you can lock for 1 to 4 years. 4 years will give you 1 veCRV per CRV, decreasing linearly to 0.25 veCRV per CRV for a one year period. As said before, veCRV is the base unit of the system - so it will determine how much fees as well as boosting and governance power you have access to.

### 2/ Level-up Zone : Your share of the fees

Staking and locking CRV tokens in the DAO is enough to be eligible for a share of the fees collected on Curve, yet it's only the first step of the journey. The commissions are collected frequently and settled for 3pool LP tokens. The mechanism recently kicked off and started distributing rewards.

Please note that the effective return fluctuates as it's tied to Curve's exchange volume and the CRV token acquisition price. At the time of writing, it's around **$0.29 yearly for 1 vecRV.**

{{< notice note >}}
To describe the next layer of the Curve's onion, I love to use a metaphor inspired from online role-playing games. Indeed, there are three types of realms fitting to describe the next three steps for Curve:

1. **PvE (Player vs Environment)**: where you face only AI-controlled monsters (mobs)
2. **PvP (vs Players)**: where you fight against other players in a set environment (arena/battlefield)
3. **RvR (Realm vs Realm)**: where you fight against other players potentially everywhere (faction-based)

We'll use this frame of reference to analyze the next three layers of the Curve's onion.
{{< /notice >}}

### 3/ Curve's PvE - Boosting CRV rewards

As mentioned earlier, liquidity providers can stake their LP tokens to earn CRV on top of their usual commissions. But they can also **use their veCRV tokens to boost** one or several of their pools, increasing the CRV earned up to 2.5 times.

To do so, one needs an amount of veCRV proportionate to the $value of the liquidity providing position boosted. The effective cost (in veCRV) to have the maximum boost is not the same for each pool - creating a first layer of incentives/arbitrages games.

![Curve CRV boosting](/img/2021/dex-value-capture/crv-boost.png "It takes a different amount of veCRV per $ deposited into a given pool to achieve the maximum boost.")

It's an interesting mechanism enabling a better alignment of incentive: **large and efficient CRV earners are also significant veCRV holders** (-> locked for 1-4 years) so they have a fair amount of skin in the game. Yet it's just the first & friendliest layer of Curve's meta game. Let's go deeper into the onion.

### 4/ Curve's PvP - The Gauge Weight's Game

>If pool-boosting is PvE, the gauge-weights are Curve's PvP arena.

The gauge-weights are a bit similar to boosting, but **at the platform-level**. veCRV holders can vote to **decide the share of newly minted CRV allocated to each pool**. Additional restrictions apply here to prevent the manipulation of the votes:

*   The VeCRV needs to be locked with at least 7 days left.
*   The gauge weight voting can only be changed by users every 10 days.

It enables the incentivization of new pools, theoretically without impulse needed from the Curve team.

### 5/ Curve's RvR - Governance & inter-protocol gov

The last layer of the onion lies with Curve's governance: veCRV holders can vote on the DAO proposal and with at least 2 500 veCRV, you can submit a proposal to the DAO. So, to recap, once you hold veCRV, you:

1. Earn a share of the fees collected by the exchange
2. Can boost your own CRV streams
3. Through gauges, influence future CRV emission on curve pools.
4. And finally with the governance, you have a say in the key parameters of the system.

While 1&2 is what is of interest to most-end users, **items 3&4 can be incredibly valuable for other dApps, DeFi projects and protocol politicians**[^2].

From here, the possibilities are virtually endless:
1. For instance, imagine a project introducing a new stablecoin. Wouldn't it be neat for them to have governance power within Curve to eventually include it in a boosted Curve pool?
2. Even deeper into the onion, already **successful DeFi projects with treasury can allocate a part of it to the CRV token to harness the benefits from all 4 items** - 1&2 to boost their treasury income streams and 3&4 to make their platform or service more attractive.
3. Another layer deeper: **[Yearn's yveCRV vault](https://crv.ape.tax)**. It offers better returns on CRV than staking yourself (~1.3x), but depositors renounce boosting and voting capacity in favor of Yearn - which can then use this extra boosting/voting capacity to enhance the yield of its vaults.
4. Final level of depth: imagine a crypto/DeFi PR-like service a couple years from now. I expect them to be able to **supply other projects with proposition power** on the main DAOs like Curve or Aave.

### 6/ Next Steps for Curve

Finally, we have to consider one last dimension on Curve, as it's not just any DEX. Indeed, from the get-go Curve specialized into the **swaps of pegged-assets** and optimized for it. It started with stablecoins only, but we now also have BTC and ETH representations too. 

Thanks to the growing available liquidity, the team is now harnessing DeFi synergies (with Synthetix) to offer swaps between the different pegged assets listed on Curve, such as DAI -> wBTC or USDT -> EURS.

It provides incredible value as it covers markets that are currently not broadly available elsewhere (EURS) and enables a minimization of slippage for large trades.

To stay concise, Uniswap and Sushiswap's bonding curves are well suited to **support many small or average swaps, especially on large pools** with a low slippage. However, they are less optimal for large orders as slippage increases in proportion to the share of liquidity of the pool required by the trade. 

{{< notice tip >}}
A service like **[ParaSwap](https://paraswap.io)** helps you streamline this process & optimize your swap further.
{{< /notice >}}

---

## Future outlook: L2 & its incentives

To wrap up this article, let's not forget about the upcoming tectonic shift for the Ethereum space: the increasing availability of layer 2.

Last year, we saw the value transacted on AMM explode to the detriment of order-book based approaches. They streamlined the whole experience and made tons of sense for layer 1 so we can reasonably expect them to pave the way for L2 decentralized trading. 

**Loopring is already delivering live in production an AMM on L2:** a zk-Sync based L2 DEX with various incentives for liquidity providers. Curve has been working with Zk-Sync too, so we can reasonnably expect them to ship a live L2 product this year considering the latest developments with Zk-Sync.

![Loopring V2 Stats](/img/2021/dex-value-capture/loopring.png "Overview of the main pools on Loopring V2")

On the other hand, Synthetix recently rolled their Optimism L2 mainnet and the force seems strong around a Uniswap x Optimism rollout. Jokingly the other day I was saying: 
> Synthetix Optimism L2 is Uniswap's testnet. 

It wouldn't be surprising to see Uniswap's L2 implementation rolling out within weeks or months.

While we're at it, what about tokoenomics x L2? I expect to see **LP incentives too migrating to L2**, as it's already the case with Loopring. Synthetic too quickstarted its current limited L2 (minting/burning only) with SNX incentives.

Services that do not already have a token might have an edge here as they can incentive the L2 directly. On the other hand, the protocols that heavily incentivized their L1 already might lack firepower to match the incentives offered by projects with "L2-native" tokens.

It's going to be fascinating to watch the releases of the different layer 2 and how they impact the protocols usage and tokenomics.

{{< notice note >}}
![defi-france-live-16](/img/2021/dex-value-capture/defi-france-live-16.png)
🇫🇷 If you understand spoken French:

We're thrilled to meet 0xMaki to discuss the topic **in French** this Monday on [DeFi France's YouTube](https://www.youtube.com/watch?v=JT8N7-gqTjA)
{{< /notice >}}

## Notes & References

[^1]: Find more info in the [Uniswap V2 Documentation](https://uniswap.org/docs/v2/advanced-topics/fees/).
[^2]: A concept [first theorized in the Bankless newsletter]([https://newsletter.banklesshq.com/p/the-life-of-a-protocol-politician)referring to a person or entity specializing in gaining influence over diverse decentralized protocols & then offering on-the-tap access to this influence as a service.

_🙏 Huge thanks to HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony for proofreading the French version of this article and translating it integrally into English._
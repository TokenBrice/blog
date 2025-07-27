---
title: "📖 How to make DeFinancial products work for you"
description: "A balanced overview of decentralised finance services you can use to make your ETH work for you - 6 base strategies, their variants, & what to watch for while implementing them."
date: '2020-05-20T10:53:50.191Z'
categories: [🌌 DeFi, ⚙ Understanding]
tags: [DeFi, Ethereum, Lending, Liquidity Providing, Synthetic Assets, Liquidation, Gas, Impermanent Lossses, guide]
toc: true
tocNum: false
image: /img/2020/definancial-services-guide/cover.jpeg
---

Welcome to the new economic paradigm!

If you landed here, you probably already have heard about Ethereum and even decentralised finance (DeFi). That's great - today we take it to the next step: how to use DeFi to better your personal finance.

This article walks you through 6 base strategies and their variants that harness the most relevant DeFinancial services. We start with the "set and forget" strategies and progressively move down the stack towards the more complex but also lucrative ones.

Before we dive into the strategies, I URGE you to read attentively the primer on gas below & as well as the disclaimers. 

**This article is not investment advice. I am not an accredited investor or asset manager. I am just a 27 year old dude using DeFinancial services abundantly and highly active in the space.**

**YOU ARE THE ONLY ONE RESPONSIBLE FOR YOUR INVESTMENT DECISIONS.**


## A primer on gas

_ℹ If you know what gas is, feel free to ignore, else - please read this:_

 
All strategies described here are enabled thanks to decentralised finance services and executed on the Ethereum network. **To interact with DeFi services, you'll have to pay for the commons of the Ethereum network - and that's what gas costs are.** 


Gas costs are paid in gwei, a subunit of ETH (1 gwei =  0.000000001 ETH). Most Ethereum wallets will suggest a default gas price. That's usually enough to get started. 

However, as you dive deeper into the arcane of DeFi, you'll find yourself coming back to gas to understand it better and optimise your transaction costs. Indeed, depending on the gas cost you pick (vs network observed one), your transaction will clear quickly, slowly, or not at all. 

![eth-gas-station](/img/2020/definancial-services-guide/gas-station.png)

You can [check recommended gas prices on ⛽ EthGasStation](https://ethgasstation.info/),

Or read [📑 EthHub Docs on Ethereum Transactions](https://docs.ethhub.io/using-ethereum/transactions/) to learn more about gas.

Note: Some strategies listed below (1, 3 & 4) are applicable without having to worry about gas, using [Argent](https://argent.xyz/).

---

We're almost ready to go in! I just have some necessary disclaimers to share with you to make sure we're on the same level & you understand the content presented below for what it is: 

### Necessary reminders - PLEASE READ

1. **All returns discussed in the articles are yearly APR (Annual Percentage Rate)** - to realise these APR (assuming the estimation is accurate), you need to hold your position for a year.
2. **There are no objective measurements of complexity or risk** - the parameters I present you with while introducing a strategy are here for understanding only.
3. What does "**risk**" represent? A chance of losing your assets due to market events or your own shortcomings (usually stemming from a lack of understanding)  \
The "**complexity**" score gives you an idea of how technical and hard the risk is to understand and estimate. 
<br> *Please note: the risk of a failure at the Ethereum network-level is not equal to 0. I do not mention this risk again below - it's implied as a base-level of risk.*
4. There are no free lunches: be sensible with your decisions, here's a **quick rule of  thumb "the higher the APR, the higher the risk"**.
5. When markets go wild (either way), some products are affected more than others. While a sudden ETH price variation doesn't impact RealT's APR (2) - it can translate into significant losses for users of TokenSets or liquidity providers.
6. Finally, keep in mind that most of the APR mentioned below change quite often. Don't take them as such, especially if you read this piece weeks after its release: double check by yourself.

If you're considering committing capital to a given project, **I URGE YOU** to check the following ressources to learn more on their risk model [DeFiScore](https://app.defiscore.io/) & [DeFiWatch](https://defiwatch.net/).

![defi-score](/img/2020/definancial-services-guide/defiscore.png)

## PASSIVE DEFINANCIAL SERVICES

_Products 1-4 are "set and forget" (please monitor your positions still). What's meant is that entry is usually done through a simple purchase/swap - and so is the exit._

_Meanwhile, in between the two, you have nothing to do to earn your yield - it's paid to you without requiring any intervention (claim or other)._


### With Stable Assets

Some passive investment products involve only stablecoins - these are tokens tracking the price of a stable currency, usually the dollar. Considering the minimal amount of work required to use them, and the lower overall risk (mostly technical failure) these products are the best to get you started with decentralised finance.


#### 1/ Stablecoins Yield

>You own an Ethereum-based asset tracking the price of the dollar (ex: DAI). You find a way for this asset to earn interest: lending (ex: aDAI) or liquidity providing.

(1 = lowest, 5 = highest)

![1-stablecoin-yield](/img/2020/definancial-services-guide/subh/1-stablecoin-yield.jpeg)

Yield-bearing stablecoins are the gateway drug. 

They can provide decent returns (up to 8-9% APR), are convenient to use and also not too complex so they are a good start to understand some fundamentals about DeFi.

Getting in and out is as easy as swapping a token. So, if while considering this approach, you only have three things to keep in mind:

1. Risk: base stablecoin risk (on DAI) + any service on top of it (ex: Aave for aDAI)
2. Return: there are some neat ressources to keep track with the yields, check [LoanScan](https://loanscan.io) for instance.
3. Gas costs to get in & out (especially **if you invest small amounts, or while the network is busy**).

To implement this first strategy, you have several options: [Compound](https://compound.finance/), [Aave](https://aave.com/), etc. You can acquire their corresponding tokens (cDAI, aDAI, iDAI) using a service like [ParaSwap](https://paraswap.io). In terms of APR, historically, aDAI has been consistently topping the charts.

If you want to expand on top of the base concept, you have several options offering better returns (meaning more risk):


##### 1-A/ Implementing a basic stablecoin-yield based strategy

**RECAP: You own an Ethereum-based asset dynamically rebalancing between several stablecoins providing yields to optimise your return.**

As said above, there are several services offering stablecoins providing returns thanks to lending pools. You can manually chase the best rate yourself, but will require you to monitor the rates and do the rebalances yourself.

So instead, why not use an Ethereum native service to do that for you in full transparency? [Idle Finance](https://idle.finance/) is the leading solution:

![idle-dai](/img/2020/definancial-services-guide/idle-dai.png)

##### 1-B/ Stablecoins Liquidity Providing: Curve Pools

> You own several Ethereum-based stablecoins and help facilitate trades on Curve (= liquidity provider). You earn a commission on each trade corresponding to the prorata of your share of the pool.

We will have a dedicated section about liquidity pools below but I had to mention the Curve Pools here. In a gist, [Curve](https://curve.fi) is a service made to optimize stablecoin swaps. Providing liquidity on Curve can be quite attractive since the base assets are all stablecoins & the returns provided by the commissions collected on the swaps (& lending) are decent.

##### 1-C / No loss lottery: Pool Together

>You lock a stablecoin (DAI or USDC) for a week or a month. They are pooled with other users' to generate interest (->Compound). At the end of the week/month, the winner gets all the interests.

I love this one because it's both surprising to see it here and amazing. So first, let me clear the air: [PoolTogether](https://www.pooltogether.com/) is not a financial product per-se - their vision is more pedagogic: PoolTogether is a money game.

The concept is quite simple, as described in the recap. Since all the profits of the winner are generated on the interests of all players, nobody loses any money with PoolTogether.

However please rest assured, the addition of PoolTogether in this list is not ideological: **average returns are superior to Compound. **The reason why is quite simple: PoolTogether uses Compound to generate its return (= same APR) + each pool has some "sponsored" ticket - tickets contributing to the interest accrual, but without winning chances.**

![pool-together-sponsored-balances](/img/2020/definancial-services-guide/pt-sponsored.png)

Finally, with the average APR is higher, please bear in mind that PoolTogether is much less regular - most of the time you'll get nothing, but if you win you get the equivalent of years of interest on your capital. 

PoolTogether essentially provides a new flavor of interest distribution on top of Compound's return: PT's returns are much more random but also potentially massive (if lucky).

Last month, [PoolTogether released the pods](https://medium.com/pooltogether/winning-more-prizes-185bad7f6d63) - a new option for users to play as a group. Users can now share their odds and their gains - which makes the wins less significant but much more frequent.

[You can play the PoolTogether lottery directly from their website.](https://www.pooltogether.com/) You'll need some DAI or USDC.


#### 2/ Tokenized Real Estate - RealT

> You own shares of tokenized properties (securities). You earn your share of the rent daily (currently in USDC) + extra earning opportunities (liquidity providing, incentive programs).

![2-realt-tokenised-real-estate](/img/2020/definancial-services-guide/subh/2-tokenised-real-estate.jpeg)

**[RealT](https://realt.co) is a totally different beast from anything else in that list, at several levels**. Since RealT tokens represents real estate in the real world, the risk profile is also totally different (~~>  less Ethereum risk, more real-word risk).

Before we dive into what makes RealT tokens so interesting, let's make sure we are clear. **RealT tokens are securities - you have to go through a KYC process to be able to purchase them** (whitelist + lease agreement).

![RealT-tokenised-real-estate](/img/2020/definancial-services-guide/realt.png)

It's a bit more work than for interest-bearing stablecoins, but you have several benefits to gain here compared to strategy 1:

*   **Returns**: depending on the property, APR ranges from 8% to 12.5%.
*   **Daily payment of returns**: once you have some RealT tokens in your wallet, you will receive your corresponding** share of the rent, daily, in USDC**.
*   **Hedging**: you have a yield based on real estate - AKA less correlated to the rest of the crypto markets
*   **Additional opportunities**: you can add more to this strategy to increase the return. To do so, consider providing liquidity on Uniswap - generating some returns. [Providing liquidity on RealT tokens is currently incentivised](https://medium.com/realtplatform/announcing-the-uniswap-incentive-program-f82f721cf63a) - landing even more returns.


### With Volatile Assets


#### 3/ Automated Trading Strategies - TokenSets

> You own a "set" representing a stake in an automated trading strategy based on a technical indicator or another trader (social sets) a.k.a. "Holding on autopilot".

![3-tokensets-automated-strategies](/img/2020/definancial-services-guide/subh/3-tokensets.jpeg)

**[TokenSets](https://www.tokensets.com/) are the holders' best friend**. While the service is definitely not the easiest to understand or the less risky, it currently provides significant utility. Indeed, if you are a long term holder of ETH for instance, TokenSets is one of your best options to grow your ETH stash (against ETH).

Sets are automated trading strategies represented by a token. Each set trades a given pair (ex: ETH/cUSDC) following a pre-set of rebalancing rules triggered by the cross with the set technical indicator.

![Tokensets performance visualised with TokenViz](/img/2020/definancial-services-guide/tokenviz.png)
Wondering which set to pick? [TokenViz](https://tokenviz.io) provides a neat dashboard to help you chose.

So as a user who is not willing to look at charts all day, TokenSets is an excellent option. Indeed, most people trying to trade tend to lose money. **With the sets, the emotions are out & machines rule.**

On top of the regular sets following a technical indicator (such as ETH 20 Days Moving Average), there are now social sets. It's the same mechanism, but your set will follow another's trader strategy instead of simple technical indicators: aka "copy-trader" feature.


#### 4/ Simple yields to chase on ERC20 tokens

>This is essentially the ERC-20 version of strategy 1: you own an ERC-20 (non-stable) token producing some form of returns, usually through lending or liquidity providing.

![4-erc20-yields](/img/2020/definancial-services-guide/subh/4-erc20-yields.jpeg)

Before we explore the more active approaches, allow me to introduce one more passive approach, this time based on ERC20 tokens (not stablecoins.)

Since Aave offers aTokens on up to 15 different ERC-20 tokens, it might be worth for you to keep an eye on them - with a tool like [AaveWatch](https://aavewatch.now.sh/):

![AaveWatch - overview of lending opportunities offered on Aave](/img/2020/definancial-services-guide/aavewatch.png)

Among them, I think the following are the most interesting:

1. aSNX: base rate around 7%, can spike quite high for a bit - keep a very close eye to this one on Wednesdays, especially if prices of ETH/SNX crashed during the week: we observe SNX borrowing surges during certain claim periods.
2. asUSD: can spikes quite hard too, especially lately (~12% APR over the last month)
3. aZRX: rates can spike, read more about ZRX to know when
4. aMANA: same here - decentish rate (1-2%)

---

## ACTIVE DEFINANCIAL SERVICES

**Doing nothing is amazing - and when it comes to investing it’s a strategy that can be surprisingly effective**. Being able to stand still and do nothing, even in the middle of a marketstorm is truly an art you would gain to master. However, and it shouldn't come as a surprise for you: the best yield will require effort.

![Doing nothing - the best strategy of them all?](/img/2020/definancial-services-guide/nothing.jpg)

Notice how I didn't say work? Sometimes, the "efforts" can simply be that you accept to stomach a risk others wouldn't, and get paid nicely for it --- **the investor equivalent of a stunt double.**

The next strategies will require a more precise understanding of what you are doing. Indeed, at their core, all strategies would benefit immensely from your market acumen. So before we explore such strategies, allow me some reminders:

*   **Information is power.** More specifically for DeFi investing: the information you have & understand is the main thing driving the alpha (returns) you're extracting from the markets.
*   **Take it slow, be safe, it's not a race**. Despite writing this article (with many people advising), I have yet to use strategy 6 with serious amounts of capital for instance. It's wise to double-check your understanding of a given platform every time you increase your stake.
*   **Want to quickstart the process? Go in with $50.** Small amounts are amazing to help you understand a protocol and be involved without taking too many risks and stressing about it.


### Some pointers on passive vs active styles

It’s impossible to give an accurate representation of the potential earning spread between an average DeFi passive investor and an active one. However, a combination of services reproduces a similar situation: 

*   Synthetix: SNX staking model to collateralise synthetic assets.
*   Aave + Synthetix = aSNX Passive (type 4) investment asset

<table align = "center">
  <tr>
   <td>
   </td>
   <td>
<div align = "center"> <b>Actions Required</b></div>
   </td>
   <td><div align = "center"> <b>Expected Yearly Return </b></div>
   </td>
  </tr>
  <tr>
   <td><div align = "center"> <b>Passive Style (aSNX)</b></div>
   </td>
   <td><div align = "center">None (once you own aSNX)</div>
   </td>
   <td><div align = "center">~10%</div>
   </td>
  </tr>
  <tr>
   <td><div align = "center"> <b>Active Style (SNX stake managed through mintr)</b></div>
   </td>
   <td><div align = "center">Weekly claim of reward (1y escrowed) + sUSD + synths management strategy (trading, liquidity+staking)</div>
   </td>
   <td><div align = "center">~80% & more (up to you)</div>
   </td>
  </tr>
</table>

#### 5/ Synthetix

> You start with a stake of SNX (Synthetix token). You stake (lock) them which already generates a neat SNX return but vested for a year (+weekly sUSD non-vested). Thanks to your stake, you can then mint synthetic tokens - that expose yourself for up to 1/8 of the initial SNX value & offer additional earning opportunities.

![5-synthetix](/img/2020/definancial-services-guide/subh/5-synthetix.jpeg)

Before anything else: what I say below is NOT ENOUGH to understand Synthetix+SNX if you are just discovering it. **Do not rush it!** Synthetix is definitely a next step in terms of complexity, here's an overview of all the new things you will have to do:

1.   Have a secured wallet - **will you be able to access your wallet in a year?**  \
SNX rewards are escrowed a year: you claim them today, but you can only move them out of Mintr (Synthetix platform) a year after the claim date.
2.   **Claim reward weekly** (SNX vested for a year + sUSD) 
3.   **Monitor** your collateralization ratio and adjust when need to be able to claim
4.   **Decide** which Synth you're exposing yourself to and when

Since Synthetix is really flexible, allow me to stick to a strategy I've successfully implemented. Other approaches are possible, and my choice is suggestive. However, I think this strategy does a good job at highlighting the different synergies available with Synthetix.

##### 5-A/ The Synthetix/Curve YieldStack (a.k.a. "the 4-steaks yieldburger")

> You use Synthetix (+SNX) to mint sUSD, a stablecoin, and supply this stablecoin to an incentivised liquidity pool for extra returns. 

Let's not beat around the bush: this is much harder, much more work than 1-4, but the returns are an order of magnitude higher if done right. Your position is also more complex to monitor since you are exposed to several types of assets, getting returns in several kinds of assets too, and the timeline of the returns are not the same either.

![The Synthetix-Yieldbuger-TokenBrice](/img/2020/definancial-services-guide/yieldburger.png)
*Stake? Steak? Does it matter as long as there is meat on the bone?*

Let's have a look at the base of the yield stack:

1. **Staking SNX + SNX reward** ~ 50% APR, in SNX, paid weekly (claim required) & vested for a year
2. **sUSD Staking reward** - variable sUSD reward (based on exchanges volume), paid weekly, claim required, no vesting period.
3. **Liquidity Provider Curve sUSD pool** - 3 to 5% APR, earned while exiting the pool.
4. **Incentive Program** for that pool (accessed by staking the pool token)-  25% APR, in SNX, paid weekly (claim required), no vesting period

_Note: The Curve sUSD pool ran into some issues, and the current live version is not the most optimised one for returns. A new version of the sUSD pool is coming up, harnessing Aave to optimize it even farther. This strategy might get even more compelling as soon as this ships!_

Curious ? Here is a [comprehensive overview to get started with Synthetix](https://synthetix.community/docs/intro).

#### 6/ Liquidity Provider (not on stablecoins)

> You use a capital equally split into to tokens (ex 50% ETH 50% DAI) to supply a liquidity pool, which generates commissions on the trade you help facilitate.

![6-liquidity-provider](/img/2020/definancial-services-guide/subh/6-liquidity-provider.jpeg)

This is essentially a riskier variant of the strategy 1-B. In this scenario, you are still providing liquidity but this time you move to another kind of pair - the ETH based ones. 

**While you provide liquidity on a decentralised exchange, the main risk you face (on top of the usual) is what we call "impermanent losses**". (confusing name, they are very permanent)

I can't explain the full concept here, but here's a quick recap: **impermanent losses usually stem from a sudden variation between the relative prices of the two assets you're providing liquidity to**. 

**So if the two assets are tracking the same price (ex ETH/sETH), the impermanent loss risk is minimized**. So, from the lower level of risk, to greater, you have:

1. Providing liquidity on stablecoins: both assets prices are relatively stable, and they track the same price => the impermanent losses risk is minimized.
2. Providing liquidity on assets that are not stable but tracking the same price, such as ETH/sETH. 
3. Providing liquidity on an ETH/stable pair.
4. Providing liquidity on a ETH/ERC20 (both non stable & not tracking the same price) - this is where the risk is greater, since both assets can move - if both assets price were to suddenly move in opposite directions you can suffer significant impermanent losses.

If you are considering providing liquidity on AMMs, please read more on the topic: [Risk/Reward of liquidity provision in AMMs](https://blog.bancor.network/beginners-guide-to-getting-rekt-by-impermanent-loss-7c9510cb2f22).

*Edit (07/16)* - If you are curious about liquidity providing, here is another guide covering the main incentivised opportunities: **[💦 The Yield Farmer Tier List](https://tokenbrice.xyz/content/posts/2020/yield-farmer-tier-list.md)**.

## Conclusion

I think this is a good place to call it a run and keep this guide digestible. 

If you're ready to jump-in, here are some solutions that will make it easier for you:
1. [Argent Wallet](https://argent.xyz/) Secure wallet offering one tap access to Aave tokens, PoolTogether & TokenSets presented in this article.
2. [Monolith Visa Debit Card](https://monolith.xyz) You've made some profits in DeFi you'd like to cash out in the real world? This is the only no-compromise solution allowing you to do so.

And if you're wondering what could be your next steps, here is are some of your potential ones:

*   Opening vaults on [Maker](http://makerdao.com/) or using [Aave](https://aave.com/) to get leverage (⚠ liquidation risk).
*   Using options like [Opyn](https://opyn.co/) or insurance service such as [Nexus Mutual](https://nexusmutual.io/)
*   [Aave's](https://aave.com/) Flash loans 

I hope this was an insightful read and you've figured a few ways to make DeFinancial services work for you. If you have any questions, feel free to reach out to the [DeFi community on Telegram](https://t.me/de_fi), or their variants in your native language.

---

This article was made possible thanks to a tremendous amount of support from people in the community who shared their suggestions, insights and proofread it.

Thanks to these amazing people:

*   [Jimmy Ragosa - follow him on Twitter](https://twitter.com/jimmyragosa), his meme game is woke 👌
*   [Marc Zeller](https://twitter.com/lemiscate) - dev advocate @Aave, do I need to say anything more?
*   Marouane - he's coming after your risks, [watch out!](https://twitter.com/UnslashedF)
*   [Viktor](mailto:victor@function.media) who worked on the graphics of this article and indulged my terrifying napkin diagrams. 

As well as people who did not contribute directly to this specific article but were key in helping me understand DeFinancial services better - allowing me to be in a position to write this guide:

*   [Pascal Tallarida](https://twitter.com/pscltllrd): founder of Jarvis Netowrk, proeminent onboarder and vulgariser in the French community. He's the one who helped me (and MANY others) grasp their heard around synthetic assets.
*   [Mounir](https://twitter.com/mounibec): founder of Paraswap.io, the OG-est of DEX aggregator and still the only one that can fetch a price <1-2s without melting your laptop. Mounir is a one-man-army and an incredibly helpful actor in the French & international communities.
*   [Abel](https://twitter.com/AbelsAbstracts): this guy keeps up with everything and he's my go-to person to discuss new releases and see through the marketing. Check [his amazing podcast](https://open.spotify.com/show/6NO8M2R4u9YSgAdz5TA4ZA) - we do a DeFi catchup every week together.

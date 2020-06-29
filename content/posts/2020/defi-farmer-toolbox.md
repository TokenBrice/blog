---
title: "The DeFinancial Farming Toolbox"
description: "A hitchhiker's guide to liquidity mining curating tips & tools to help you make the most of DeFi's agrarian revolution 🌻"
date: '2020-06-29T01:13:50.191Z'
categories: [🌌 DeFi, 💸 Practical DeFi]
tags: [DeFi, Ethereum, Lending, Liquidity Providing, Synthetic Assets]
toc: true
tocNum: false
---

![cover-DeFi-Farmer-Toolbox](/img/2020/defi-farmer-toolbox/cover.jpeg)

Howdy farmer,

If you made it here, we will assume a shared basic understanding of [what yield farming is](https://ethereumprice.org/guides/article/yield-farming/). 

You might even have tried it by yourself, or heard the [tales from a yield farmer](https://defiweekly.substack.com/p/tales-from-a-yield-farmer): amazing! Today, it’s my turn to share key concepts & a curated list of tools to help you make the most out of it.

If by any chance you landed here without any idea of what [Ethereum](https://ethhub.io/) or **[DeFi](https://tokenbrice.xyz/posts/2020/definancial-services-guide/)** is, please click these links. This is not a guide, I keep it short & sweet with pointers only - Let’s get started! 


## Organic DeFarming

Farming used to be simple: you planted some seeds and hopefully collected yields. Nowadays, we have some **super crops**, landing extra yields on top of usual commissions on the swaps facilitated or fees collected on lending.

How? Essentially because **some DeFi platforms like Compound or Balancer are now incentivising users to perform actions critical to the service;** such as supplying liquidity and borrowing for Compound. Their users are rewarded with their native governance token (COMP in this case). Pricing such token is a hard task the markets are currently crunching on. Price stability of these token may take time as they are currently in price discovery mode

So before we go any further, it’s time to hear a tale from Stani, an organic farmer:

> What is needed is sustainable farming. In essence, farmers should farm quality crops by bringing quality liquidity for long term and keeping the seeds of these crops to expand their farms to new lands.
> - Stani Kulechov, Aave's CEO [on Twitter](https://twitter.com/StaniKulechov/status/1276093091624226816?s=20)

We’ll dive deeper into this later, but the overall **high average gas prices are incentivising you to pick solid crops and stick with them** instead of foraging all around. For more context on liquidity mining, I’d also recommend reading this piece about the SAFG framework:

> Fundamentally the SAFG shifts us from a world of “buying to own” to one of “participating to govern,” which can ultimately result in more successful protocols and healthier communities.
>- [Intro - SAFG Framework](https://medium.com/ideo-colab/meet-the-safg-defis-emergent-framework-for-participatory-investing-and-protocol-development-62286a576fb5)


### Liquidity Mining Sources

Here are the main liquidity mining sources, ordered by the share of tokens available through liquidity mining: 

*   Balancer Labs - [BAL](https://medium.com/balancer-protocol/proposing-balancer-liquidity-mining-cab4503972fa) - 100M total supply, 75M distributed through liquidity mining (75%), since June 1 - includes some externally incentivized pools.
*   Curve Finance - CRV ??? - there is currently little to no public information available.
*   Compound Finance - [COMP](https://medium.com/compound-finance/expanding-compound-governance-ce13fcd4fe36) - 10M total supply, ~4.2M through liquidity mining (42%), since June 15
*   Universal Market Access - [UMA](https://defirate.com/safg/) ~ 35% of the supply through mining (details TBD)
*   Synthetix & other incentives program (like JRT)
*   Jarvis x Aave [Onramp Sponsoring Program](https://sponsoring.jarvis.network/): redirect interest earned form your stablecoins on Aave to earn JRT tokens.

![synthetix liquidity mining programs](/img/2020/defi-farmer-toolbox/synthetix-liquidity-mining.png)

### Adapting the strategy to your budget

Before we see how to get in and out of such positions, it's time for a quick discussion on gas prices. They have been pretty high lately in a 25-35 gwei/fast range. Here's roughly what it means for common operations:


*   Deposit @Compound ($2-3 gas)
*   Deposit @Liquidity Pools @Zapper, an all-in-one tool to handle your liquidity providing positions, more on this below ($3-5 + swap fees)
*   Deposit @Liquidity Pools "manually" ($0.3 (approve) + $2-3 as many times as tokens as in the pool)
*   Exiting also has a cost, as well as any token swap required (like selling your COMP while exiting your position) $1-3


#### A cold hard look at gas cost impact on medium capitals ($ 2000)

**Let's look at the returns over time of a 2 000 USDT Deposit @Compound**

To keep this simple, we assume the current parameters will stay as such for the next year. **This is obviously unrealistic - take this as a thought experiment.** Here were the parameters at the time of writing:


*   4% APY on USDT on Compound = $80 for a year on the capital
*   0.66 COMP/year =~$150 produced by our capital

In the table below, the "Actual Profits" column corresponds to a total exit of the position (back to USDT), which means effectively 3 transactions overall for the operation:

1. Supplying on Compound
2. Withdrawing on Compound
3. Selling the COMP tokens

So if we look at this position with these assumptions over several time frames, here is what we get:

| Timeframe | Total Return ($) | Actual Profits ($) | Effective % return over the timeframe |
|:-----------:|:------------------:|:--------------------:|:---------------------------------------:|
| 1 day     | $0.63            | -$8.37             | -0.42%                                |
| 1 week    | $4.42            | -$4.58             | -0.23%                                |
| 1 month   | $23.00           | $14.00             | 0.70%                                 |
| 3 months  | $57.50           | $48.50             | 2.43%                                 |
| 6 months  | $115.00          | $106.00            | 5.30%                                 |
| A year    | $230.00          | $221.00            | 11.05%                                |


*Please note: This simplistic scenario ignores the opportunity cost on ETH price. $5 of gas (=ETH) paid today might be worth $10 a year from now.*

The learning here I wanted to share is that **for such capitals, considering the current gas costs, it will probably be better to stick to a position for months instead of trying to chase the best currently available yield**. Decent profits (~0.81 % /month) starts around the 3-months timeframe. 

So, remember Stani the farmer? You need to pick your crops wisely. 


#### Whale's Playground (> $ 10 000)

Now if you have more skin in the game and are willing to take more exposure, gas costs become less prohibitive and there are more options available to you. I won't expand on these, some pointers will be enough:

For instance, you can leverage your Compound exposure to maximize your effective COMP mining (through supply/borrow). It obviously comes with a risk of liquidation. [InstaDapp](https://dsa.instadapp.io/compound) helps you maximize COMP returns by folding your position up to 4x.

In a previous article, I've detailed a strategy built on the Synthetix platform which included another form of small leverage. It observed impressive returns (~200% effectively) since [introduced 5 weeks ago](https://tokenbrice.xyz/posts/2020/definancial-services-guide/#5-a-the-synthetixcurve-yieldstack-aka-the-4-steaks-yieldburger) - mostly due to a significant appreciation of the price of SNX, the largest exposure in this strategy and the very high level of activity on the Curve sUSD pool.



![The Synthetix-Yieldbuger-TokenBrice](/img/2020/definancial-services-guide/yieldburger.png)


Alright, enough prep - you are now an advised farmer - congrats! Let's look at the tools used to plant your seed, secure your crops and harvest your yields.


### Getting in and out of positions

You can get into liquidity pools “manually”, that is directly on each platform. It will require several transactions and a proportionate amount of a least two tokens, to begin with. If not, you will also have to swap accordingly beforehand, using a service like **[ParaSwap](https://paraswap.io)**. ParaSwap also helps you get into tokens like cDAI (interest-bearing DAI from Compound) from any other ERC20 with gas and price-efficient paths.

*Note: Balancer just add the option to enter a liquidity pool from [just one token](https://twitter.com/jbrukh/status/1276958110024896514?s=20) (-> getting up to 8 tokens from 1, watch for slippage!).* 🔥

If you’re not the most familiar with Ethereum yet, the easiest way for you to partake in this feast would be to use tools:

![Zapper.Fi-zap-in-liquidity-pools](/img/2020/defi-farmer-toolbox/zapper-fi.png)

**Getting in and out of pools**: [Zapper.fi](https://zapper.fi): in the Invest tab, Zapper lets you conveniently get into/out of pools on Balancer, Curve, and Uniswap, from ETH, DAI and a few other tokens.

**Buying ETH & using DeFi services** like Aave (gas free on Aave for now!) - [Argent](https://argent.xyz)

**Spending ETH & stablecoins** - [Monolith](https://monolith.xyz). Now with ParaSwap built-in for swaps and soon an on-ramp to buy ETH/ERC-20 from your bank account!

![monolith](/img/2020/defi-farmer-toolbox/monolith.jpeg)

While we’re at it, here’s a quick tip because I see this way too much. 
**You should never claim on Compound.** It's costly and your COMP tokens are automatically claimed every time you adjust your position by depositing or withdrawing assets (minimal amount of COMP claimable required).


## The DeFinancial Farmer's Essential Toolbox

Now that we’ve explained  the basics dear organic farmers, it’s time to finally have a look at that promised toolbox. You'll find below tools that help you track your positions and the markets & analyse the potential returns of strategies you think about applying.

On top of helping you zap in/out of pools, **[Zapper.fi](https://zapper.fi)** is an amazing all-in-one DeFi position tracker. Here's [the Zapper of the wallet](https://www.zapper.fi/synthetix?address=0x4E60bE84870FE6AE350B563A121042396Abe1eaF) of the legendary farmer [DegenSpartan](https://twitter.com/DegenSpartan) - seems like he took a bite into that juicy yieldburger:

![Zapper.fi - DegenSpartan](/img/2020/defi-farmer-toolbox/degen.png)

If you need to look at a wallet from a historical perspective, **[Zerion](https://zerion.co)** is king.

For a more holistic market view, you can check:

- **[DeFiMarketCap](http://defimarketcap.io/)** to see the main DeFi tokens and the prices
- **[DefiPulse](http://defipulse.com/)** to see the main platforms ranked by total assets locked
- **[Token Terminal](https://www.tokenterminal.xyz/)** for an overview of the earnings and P/E ratio of DeFi protocols
- [This **Dune Analytics** dashboard](https://explore.duneanalytics.com/public/dashboards/c87JEtVi2GlyIZHQOR02NsfyJV48eaKEQSiKplJ7) giving you an overview of the volume on DEXes:

![DEX volumes overview](/img/2020/defi-farmer-toolbox/DEX.png)

⛽ You can also use [HAL](https://twitter.com/HAL_team) to create notifications on different situations, like **[when gas prices are below a certain threshold](https://medium.com/@mattiascaricato/get-notified-when-gas-price-is-cheap-%EF%B8%8F-2a157a3d18b9)**.

### Platform-specific resources

**Compound**

You'll find an **[overview of the COMP tokens mining & claims](https://explore.duneanalytics.com/public/dashboards/JMB9bYfVUtMAPHM5moj7aIjLaDwos2k9JjJTtk64)** here. Use this tool to **[calculate the expected COMP returns](http://www.predictions.exchange/compound/None)** obtained by supplying or borrowing tokens on Compound.

**Balancer**

Just like Compound, you can estimate your BAL mining: **[BAL Distribution Calculator](http://www.predictions.exchange/balancer/%5B%5D)**. If you intend to use Balancer, I'd also recommend brushing up on the **[BAL token distribution early shenanigans](https://thedailygwei.substack.com/p/striking-a-balancer-the-daily-gwei)**.

**RealT**

Liquidity mining returns are quite variable, so on the side you might want to consider tokenised real estate for more predictable returns with [RealT](https://realt.co). Here are two main helpful resources: **[see owners & earnings](https://realt-dashboard.co/portfolio/0x51a7ead10340af963c3124b026b86dd2807c2b1c)** + **[Amazing Google Sheets to help you track your profits](https://realt.sigri44.com/)** - both are made by the community so feel free to thank their creators.

**Various**

You can **[follow Aave's market using AaveWatch](https://aavewatch.now.sh/)**. If you are a TokenSet user, **[TokenViz](http://tokenviz.io/)** will help you make sense of the sets' performance.


### Keeping track with the DeFi news

To learn more on DeFi, here are a few resources I'd recommend:

- The **[Bankless Newsletter](https://bankless.substack.com/)**, Podcast, Livestream, discussions: all of it!
- **[The Daily Gwei](https://thedailygwei.substack.com/)** - a short and sweet daily read on a key event/release
-& you can find me discussing DeFi every week with my friend Abel here: **[Abel Abstracts](https://abelsabstracts.substack.com/)**

## Parting Words

Finally, it's Gitcoin grant season so please indulge this closure:

You've been in the space for a bit, hopefully even making some profits? How about sharing a small share back, let's say 2 %, to critical infrastructure projects and to support your favourite DeFi services or content producers?

Your contributions are immensely appreciated and can have a great impact, even for just 1 DAI thanks to the CLR matching. So if you liked this piece or my contributions to the DeFi space overall, feel free to have a look at **[my Gitcoin grant](https://gitcoin.co/grants/811/tokenbrice-shining-light-on-ethereums-defi-en-fr)**. 

It will help me fund more initiatives for the French community & help to go on with content production efforts like this one. Every contribution makes a difference, even 1 DAI (currently matched +5).

Now that you are on Gitcoin with a grant in your basket, why not add more? Feel free to look around and support critical initiatives, from vulgarisation efforts to core research. Remember the gas struggles? You can **donate to the [EIP 1559 Community Fund](https://gitcoin.co/grants/946/project-title-eip-1559-community-fund)** to help on that front too!

Thank you for reading & happy farming!


### Thanks

- To [Jimmy](https://twitter.com/jimmyragosa) who helped make sure this article is as clear as it can be.
- To [Jon](https://twitter.com/OtherBright) for his help proofreading this article.
- & To [Antoine](https://twitter.com/AntoineMouran?s=09) for his various suggestions to improve this content.
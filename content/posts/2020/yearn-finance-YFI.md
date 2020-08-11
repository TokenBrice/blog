---
title: "YearnFinance - DeFi on autopilot?"
description: "Yearn Finance V2 is just a few weeks old, yet it is already one of the most influential releases of the year for DeFi - let’s unpack what happened, and why it matters."
date: '2020-08-11T01:13:50.191Z'
categories: [🌌 DeFi, 🔮 Discovery]
tags: [DeFi, Ethereum, Lending, Aave, Compound, BzX, Curve, yVault, Lending, Leveraging, YFI, Yearn, Yearn Finance]
---

A few weeks ago, Yearn v2 release and the launch of the YFI token (pronounced "Waifu") shook decentralised finance. Indeed, the whole recipe was there: Yearn is like a robo advisor, it helps you save and grow a capital - obviously one of the most thought after use cases. 

More than the product itself, core to defining what Yearn became was its founder Andre Cronje, **his choice of fully opening the governance**, and the amazing community that soon federated around the project.

With this piece today, I want to share some pointers to understand why Yearn came to be, how it works, and why it matters.

![The YFI Family](/img/2020/yearn-finance-YFI/wifeys.jpg "The YFI Family")

## What is Yearn?

The first version of Yearn started with a simple promise: it **helped you get the best lending rate available at any time on a given stablecoin**. Indeed as there were more and more options to lend stablecoins (Compound, Aave, dYdX, etc.), yield optimization quickly became essential.

Yearn v2 already brought a new product to the market, the yVaults: they go beyond yield optimization (rebalancing stablecoins between several lending platforms) to provide more returns. Let’s see how this work: 

### End-User Perspective: Deposit, Wait, Money go Up

Before we go in the specifics, here it's how it works for an end-user:

1. You own a token supported in the yVaults, such as LINK
2. You can deposit your LINK in the yVault to start earning. Entry and exit to the vaults are gas optimised (usually ~$2-3).
3. When you're done, you exit the pool. 0.5% of the **total** value is taken by the system to cover all the fees.

Given **enough time spent in the vault to make up for the exit cost**, investors walk out with a profit paid in the token they entered (ex: more LINK).


{{< notice info >}}
_Note: yVaults are still highly experimental. Make sure you know what you are getting into. Andre has quite an interesting approach, stated in his twitter bio ["I test in prod](https://twitter.com/AndreCronjeTech/status/1291252150635560960?s=20)"._
{{< /notice >}}

****

### What's happening under the hood?

yVaults are amazing because **they abstract an immense amount of complexity for the users,** and do it better than most of us. Going back to our yLINK vault, here's what happens to provide the yields:

1. LINK are deposited on Aave (Credit Delegation) and used as collateral to open positions. The positions are maintained within a safe range using an safety mechanism (funded on the returns).
2. Stablecoins are borrowed and put to work to provide a return. The latest strategy farms the mUSD/USDC MTA Balancer Pool.
3. Any actual returns of the farming portion of the position (stablecoins earned above the debt) are sold for LINK, increasing the effective returns of the whole position.

The gist of yVaults is that **they harness DeFi synergies to provide yields on autopilot.** They are designed to be flexible with their capital allocation - so that it can easily be re-allocated to follow a different strategy with better yields.

Each vault has a different strategy. Here's a neat explainer graphics made to explain the yCRV vault strategy:

![Yearn Finance yCRV vault strategy explained](/img/2020/yearn-finance-YFI/yCRV-vault.png "Yearn Finance yCRV vault strategy explained")

Explaining this one would be another article by itself, so I'll let you dig the graph and join the [Yearn Discord](https://discord.gg/HFK5uea) if interested.


## Why Yearn is unlike anything else before

Yearn is DeFi on steroids, and made possible by developments that occurred over the last year. Yearn is harnessing synergies between several "DeFi legos". Without going too deep in, here are the key ones:

1. **Aave recently launched the Credit Delegation feature**, enabling a contract to open a position on your behalf. This feature was necessary for the yVaults to function as they do now, as they enable the first part of most strategies - getting leverage.[^2] 
2. DEX & Automated Market Makers - especially **Curve.fi**, an obvious dependency for the yCRV Vault.
3. The overall **dynamism of the stablecoins markets**, thanks to new entrants such as mStable or the COMP token release. 

Yearn is the perfect example of DeFi composability![^3]


### Building as little as possible & assembling legos

Why am I focusing on this? Because as someone working in the DeFi space for two years, I can tell you that the biggest operational mistake I see ALL THE TIME - is simple: **teams re-building the wheel - reinventing what already exists and working**.  

I think DeFi projects (like most startups) would gain immensely from actively trying to reduce the scope of work they undertake - here are two amazing questions that should be asked more often:

1. "What is the unique value delivered by our product?" & 
2. "What do we need to deliver it? Can we harness existing solutions to achieve this?"

Yearn's structural design demonstrates a keen eye to identify high-potential DeFi projects and harness their synergies. In short, by **assembling several DeFi legos together in an unprecedented way**, Andre efficiently delivered a brand new use case if not a new subset of the whole industry.


## The first DeFi 100% community-driven project

This headline is not at attention grab, I stand by it as there is meat on the bone!

So first, let us restress than **Yearn has been a working product handling significant volumes for a while before the YFI token**. Now, you can add to it:

1. 100% of the tokens distributed to the community
2. Using a novel liquidity mining approach, pertinent to the product (yCRV pool).
4. The community was quick to step up and is booming with well-articulated ideas.
5. Andre relinquished control of the main contracts governing the service, in favour of a multisig with reputable actors of the space.[^4]

{{< notice note >}}
While I regard and value an open governance process as a net positive, at least in the long-run, this is also a risk - and **this is usually how people in the industry reads it**. An open governance can be hijacked in a direction that does not match the best interest of the project.
{{< /notice >}}

### DeFi/Web3 -> Communities Hegemonize Brands

You might not be on board yet, but for me, building and growing communities - that’s essentially my life. In the years I've been doing it, I found no secret sauce yet I **uncovered an obvious truth: communities >>> brands**. 

In the case of DeFi, I can't wait to see the **clash of brands** we're about to witness: 

*   On the one hand, VC-funded brand-companies tend to lack personality and have a harder time bolstering dynamic organic communities.
*   On the other hand, a community-driven project is **a story writing itself every day.** And when it comes to Yearn's brand, we see it growing fast: the swag is already there! 

![Yearn Finance Swag](/img/2020/yearn-finance-YFI/yearn-swag.png "Yearn swag was quick to arrive")


## Feeling the Yearn

Yearn is so much more than yVaults! I focused this explainer on them for clarity, but there are several other Yearn products being developed. Without diving too much in, here some promising ones:

*   **[yBorrow](https://yborrow.finance/)** - a generalised credit delegation interface using Aave. What makes it amazing is the synergy with the vaults, it will enable anyone to access vaults like yCRV from an ERC-20 token they like. 
*   ySwap: a novel automated market maker
*   A mysterious leveraged stablecoin-farming solution


### The Yearn ToolBox

Here are some tools and resources developed by the community that proves super helpful if you are exploring or using Yearn:

*   **[LearnYearn](https://www.learnyearn.finance/)**: A comprehensive Yearn wiki frequently updated!
*   **[FeelTheYearn](https://feel-the-yearn.vercel.app/)**: A simple page to get the current status of the vaults: assets locked in, assets deployed and the strategy used for each vault.
*   **[YCosystem](https://ycosystem.info/)**: A community aggregator to find all the useful links, from docs/YIP to where to purchase Yearn swag!

Whether or not you are interested in Yearn, I URGE YOU to give the [governance forum](https://gov.yearn.finance/) a read - you are forever invited to read and partake in the discussions shaping Yearn. This time, there is no VC, no BS - just a DAO and a one-man-army named [Andre Cronje](https://twitter.com/AndreCronjeTech).


### The Wifeys Family

Finally, it would be dishonest to cover Yearn/YFI & without mentioning that YFI sparked a whole movement - there are now dozens of forks, more or less credible. While the first few ones where just "miners fork", adjusting a few parameters, we're now seeing more creative approaches. Indeed, Yearn is open source so easily forkable, and Andre even invited the community to get creative with it[^5]!

Some communities are forking YFI to create their own pooled earning system, with a longer-term vision. It's just the beginning but I think we will see fascinating development in that space. I think we will see communities reappropriating themselves parts if not the whole YFI system - remember the Wifeys family earlier?

It's already starting! I'm following closely [YFLink](https://medium.com/yflink/the-idea-of-yflink-is-born-aa520921a4a3), a YFI fork adjusted for the needs of the LINK community. Right now, it looks like a farming cooperative, but the end game might be a community staking node - the perfect match!

I can't wait to the Yearn and its family grow!

{{< notice warning >}}
Yearn vaults are novel DeFi products integrating many others meaning the failure risks are compounded. I am not a financial advisor - you make your own decision. 

**I am responsible for <u>YOUR INVESTMENT DECISIONS</u>**, may they bring you Lambos or bankruptcy.
{{< /notice >}}

[^2]: [Here's Stani (Aave's CEO) giving you a rundown of why this is big!](https://twitter.com/StaniKulechov/status/1280500969986498561?s=20)
[^3]: Andre himself is [the first to acknowledge](https://twitter.com/AndreCronjeTech/status/1290845154430025731?s=20) what made Yearn possible and the importance of composability. 
[^4]: The protocol governance now lies in the hands of YFI holder. The access to the main contracts are held by a multi-sig, [Andre doesn't have a key](https://twitter.com/AndreCronjeTech/status/1285427748761198594?s=20). 
[^5]: ["If you do clone /and you are welcome to/, please change a few things so we get new data from the experiment. Repeating the same experiment isn't fun."](https://twitter.com/AndreCronjeTech/status/1289959986190147585?s=20)
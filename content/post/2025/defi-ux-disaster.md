---
title: "DeFi’s UX Disaster: Curation Could Save Innovation"
description: "Shining a light on DeFi’s dirty secret: the curation layer crisis - and what can we do to address it."
date: '2025-03-08T01:13:50.191Z'
categories: [Thesis]
tags: [DeFi, Ethereum, Decentralized Finance, DeFi, Public Good, DeFiScan, BlueChip, L2Beat]
url: defi-ux-disaster
image: /img/2025/defi-ux-disaster/defi-ux-disaster-cover.png
difficulty: "beginner"
---

Everyone worries about the infrastructure and app layers, and that’s cute, but what about the curation layer? Without it, the two others are nearly useless, as the complexity of the space is already far too great for most of the population to handle. So today, I want to plead to address the most significant lack in DeFi, informed by my experience with over six years spent educating people about it, onboarding pretty much anyone willing in my surroundings and online, and following up with them.

## Defining the infrastructure, application, and curation layers

Before we move forward, we need to align on the key terms – those three layers. An image is worth a thousand words, so let’s study an interesting example taken from the wild that features bits of each of the three layers:


![jumper-exchange](img/2025/defi-ux-disaster/jumper.png)


This is a pretty dense flow involving:



* Ethereum mainnet (infrastructure)
* wBTC (application)
* Mayan bridge (infrastructure)
* Aave on Optimism (application)
* USDC (application)
* Jumper (application + curation), powered by Li.FI (infrastructure).

Doing this “manually” would represent a hefty sequence of operations: 



1. Approve wBTC on exchange
2. Swap wBTC to USDC on mainnet 
3. Approve USDC on bridge
4. Bridge USDC from mainnet to optimism
5. Approve USDC on Aave/Optimism
6. Deposit USDC on Aave/Optimism

Hurray! Here’s for the application layer working its magic! But I’d like to focus on another even more critical dimension here - the curation dimension of Jumper: 

Jumper auto-detected the tokens I had in my wallet as soon as I connected, allowing me to find my wBTC quickly. It found two potential bridges and “recommended” one by placing it first (because it has the best returns). It found the respective token contracts and protocol I needed. It also provided me with an interface to execute all this without worrying if I was about to send my tokens to a scammer — that might not seem much to you or me, but to a normie, that is close to everything.

So from that example, let’s take a minute to settle the definitions:



1. **Infrastructure layer: the base layer**, which can include blockchains (Ethereum), but also pieces of infrastructure that are built upon at the next layer (Li.Fi>Jumper scenario).
2. **>> Application layer: the end-user layer**, where they actually interact with DeFi – these include all the protocols, frontends, and toolings (DeBank, DeFiSaver, Jumper, etc.) you are aware of.
3. **>>>> Curation layer: the “guidance” layer**, helping users navigate the options available at the application layer. While it exists independently, its insights can and should be integrated into the application layer.

This perspective is essentially a simplified version of [Schär's DeFi Stack](https://www.researchgate.net/figure/The-Decentralized-Finance-DeFi-Stack_fig4_340061422) where his Settlement and Asset layers are merged into my Infrastructure layer, his Protocol+Application layer into my Application layer, and his Aggregation layer is broadened and rebranded into my Curation Layer:


![Schar-defi-stack](img/2025/defi-ux-disaster/defi-stack.png)


The Curation layer champions, others than widely used tools with a curation/directory element such as [CoinGecko](https://coingecko.com/) (helping users to validate token contract & protocols front end URLs), [Jumper](https://jumper.exchange/) or [Debank](https://debank.com/) currently are websites/frameworks providing essential and verifiable insights on key verticals such as [L2Beat](https://l2beat.com/) (L2s decentralization evaluation), [DeFillama](https://defillama.com/) (DeFi data + directory), [Bluechip](https://bluechip.org/) (stablecoin economic ratings), [DeFiSafety](https://www.defisafety.com/) (development practices evaluation) or [DeFiScan](https://defiscan.info/) (protocol decentralization evaluation).

Curation can include various endeavours:



* **Validation**: Helping users verify the validity of information, such as CoinGecko acting as a source of truth for contract addresses or DeFillama for protocol frontend URLs, or Rabby various warnings helping users to realize if they are interacting with a spoofed version of a given protocol.
* **Aggregation**: Curation is provided on top of the aggregation (“here is the best route”). This includes all DEXes and bridge aggregators (ParaSwap, CowSwap, Bungee, Jumper, etc).
* **Verifiable Insights**: Information service providers like L2Beat, DeFiScan, or Bluechip enable users to access contextualized and verifiable information (onchain and against their respective framework) in their given vertical.


## The Curation Layer: DeFi’s Achilles’ Heel

If you are unconvinced about the urgent need for a better curation layer, I beg you to onboard your mom to DeFi, explain the basics of a wallet, send her some ETH, and watch her scratch her head. 

Wanna swap? Sure, we have 200 DEXes, 20 aggregators, aggregators of aggregators, and also those new bridge aggregators that now handle swap, ah and let’s not forget the intent-based protocols; by the way, do you know you can also indirectly swap by supplying a UNIv3 pool? So which one is it gonna be? Oh, you heard of Uniswap? Right, let’s try this. No, Mom, don’t click that first link on the search results; it’s not the real Uniswap. “But it’s written Uniswap”...


### Curation is the missing piece to mass onboarding

**What was the biggest helper when onboarding people? It’s not Aave, Eigen, or the latest shiny chains like Bera or Abstract. It was simple, straightforward, and easy to use tools such as DeBank or Jumper.** On top of the utility, both also act as a mini curation layer: DeBank helps users know their positions and provides them with a safe and verified link to the protocol frontends. 

Jumper essentially made bridging something a normie can handle. Before Jumper, they needed to know about the various bridges available for a given route, safely find their website and not a phising copy of it sitting at the top of the associated query thanks to Google Ads; and if their token was just a little bit “exotic”, they also needed to be familiar with the contract address find, copy and paste flow. All of this was abstracted in a simple and safe-to-use UI, making DeFi newcomers immensely more comfortable with the multichain world. I’ve witnessed it firsthand with my trainees; there was a before and an after Jumper in how much they could accomplish independently without worrying.

While both DeBank and Jumper have curating components, it’s not their primary focus. If we want to broaden the base that can harness DeFi, **we need to double down on curation**, with dedicated apps and services well integrated with the main gateways users already harness (wallets, portfolio trackers, aggregators, etc).


## How did we get there?

For the lazy readers, I’ll give it straight: **the DeFi staples failed us** – that is, the top protocols, institutions, and other well-funded actors of the space.

**Think about those prominent protocols like Aave, Uniswap, or Maker and their associated DAOs: have you ever seen them fund something remotely close to a DeFi public good?** Think about the big layer 2 or layer 1 foundations; do you see them entertaining such endeavours? The closest we got was maybe with Uniswap and the DeFi Education Fund, but it has limitations; its scope is mainly lobbying for regulations, and there remain [unaddressed concerns about its funding and transparency](https://gov.uniswap.org/t/demand-for-transparency-from-defi-education-fund/13299). 

The only exception here would be that DeFiLlama was initially funded by ex-Curve team members. However, it was done at a personal level, not in the name of Curve Finance: still, **it is worthy of praise, as it shows genuine concern for the overall good of the space**, and not just Curve’s success — an endeavour usually direly lacking in DeFi, and the main driver behind our current predicament.

To illustrate this better, let me tell you a story. When the [DeFi Collective](https://deficollective.org/) was still an idea, we contacted various teams that we thought were value-aligned to offer them to donate to the Collective. Our core idea and pitch were that:



1. DeFi Collective will help genuine DeFi thrive
2. If you are a top protocol, you benefit from having a strong ecosystem
3. Thus, even if you do not directly benefit from the existence and success of the Collective, you will benefit indirectly over a longer timeframe, and you might consider donating nonetheless.

A few resonated with the project, and we can’t thank them enough (they are listed on [the homepage](https://deficollective.org)). But for most, the conversations went essentially like this:



* Me: “Hello, TokenBrice here, /insert_pitch/”
* Them: “Nice idea! So our protocol, where would it stand on the framework?”
* Me, being honest: “Well, it depends; it could be stage 1 or 2, but even if that is, we will most likely not allocate funds to it at least early on, as we have to demonstrate the positive impact the Collective can have with smaller projects first.”
* Them: “So there’s nothing in it for us?”
* Me: “Not directly, but you will benefit from having the DeFi ecosystem thriving: that means more resilient protocols and tokens for your protocol to integrate.”
* Them: “Not interested.”

You might think it is just us, but it is not! Let’s look at the situation with the other curation-layer projects mentioned before. We have two oddities, DeFillama and L2beat, which, although they struggled initially, are now well-funded and often receive donations. Apart from that, it’s pretty much a nightmare:



* Bluechip initially explored a non-profit structure funded by donations but could not get sufficient funding, so it had to evolve into a for-profit venture.
* DeFiSafety is carried by only one chad, Rex, and had to introduce [payments](https://www.defisafety.com/pricing). Despite delivering high-quality and actionable reviews harnessed by many for years, it still barely stays afloat.


### New curation layer projects struggle to emerge

As you can see above, the core issue is not so much about the funding of already successful and well-known curation layer projects but **about smaller and newer projects not being able to source the funding they need to grow in the first place**.

Once a project reaches an L2Beat / DeFillama size and awareness, supporting it can be seen as a “marketing cost” for adjacent projects. For instance, several L2s allocated a share of their token supply to L2Beat: it made economic sense for them, as it raised awareness of their L2. It achieved support for a public good simultaneously – a win-win! Thanks to their awareness and reach, these two curation layer projects also usually perform well on donation platforms such as Gitcoin.


### The cost of free-to-access information

The thing is that these **curation-layer services have serious costs**, costs they cannot recoup with their readers if they want to keep the information they produce maximally available – that is, free and open to all.

I can give you insights on DeFiScan. Discounting:



* The months we spent researching and iterating on the framework.
* All DeFiCollective members who are seriously underpaid ($1500-2500/month for a half time) for their expertise and commitment (a.k.a. proper value-aligned Chads, I can’t thank them enough), are also supporting DeFiScan.
* Many contributors, myself included, work closer to full-time for DeFiCollective/DeFiScan (for a half-time pay).
* DeFiCollective covers all infrastructure and service costs incurred by DeFiScan.

We **estimate** the effective cost of a review in the $3000 (small immutable protocol) to $10 000 range (large codebase, mutable protocol), and potentially even more (hello Aave and your infinite codebase). Mind that each review is not only written by the initial submitter (who can be one of us or someone tied to the reviewed protocol) but also carefully discussed and reviewed by other team members. With 14 reviews already published, that’s essentially **a “burn” of $91k already in about five months** of existence. **If we account for the review in progress (total including the live ones = 35), this cost jumps to $227,500, or a ~$45,500 monthly burn.**

Please remember that the above is an estimation, as no one is paying for DeFiScan – not you, the readers/users, or the projects reviewed. For some perspective, let’s look at Bluechip since Ben agreed to share their pricing – what projects pay to get reviewed: $15k for a holistic evaluation and a $5k annual maintenance fee, starting after a year.

I’m not writing this to beg for your money – we are figuring it out on our own, thanks to the unique situation of the DeFiCollective, and exploring all other relevant options. This is a reminder that information (curation, in our case) has a cost.


### What can you, dear reader, do about this?

Again, I’d like to stress that the goal of this article, the message it carries, is not “donate to your curation layer services”. However, you are welcome to, and at our level, you already have. When we offered our community the opportunity to donate for the first anniversary of the DeFi Collective, you [jumped at the occasion](https://deficollective.org/blog/first-anniversary-nft/). You contributed the maximum possible (10 ETH) in not even three days.

Instead, the message I would love to spread is more about **1) the critical importance of the curation layer, 2) realizing the costs of the valuable information they provide, and 3) the need for you, me, and essentially everyone to be much more proactive in advocating for its funding.** It’s pretty clear that big DAOs and other well-funded institutions are not too eager to fund this, so it is up to us to help them see the light.

Again, thanks to the unique situation at the DeFi Collective, we’re not worried about our short/mid-term survival; however, I think it’s a necessity for the long-term survival of DeFi to see DeFiSafety, Bluechip, and other projects yet to emerge and thrive. We are, of course, all three chatting to one another already and contemplating a “DeFi Information Service Provider Alliance” (name is a work in progress), in which we would love to see more significant projects like DeFiLlama and L2Beat as well.

If you read my plea and heard my call, the next step is simple: **go to the DAOs you are active on and ask them what they are doing to support the space beyond their immediate benefits.** The current situation, with its seriously undersized curation layer, has severe consequences that should be obvious to all: **newcomers are getting butchered**, rugged, scammed, etc. As a result, our whole industry looks like a circus from the outside. **DeFi can only go mainstream once the average new user is reasonably safe**; that is currently not the case. Moreover, curation tools are also a big ask from institutional clients actively seeking such resources: **an enhanced curation layer means we will be better at attracting and retaining both individuals and institutions**.

So go nudge public and well-known whales and other well-funded institutions to do more. Protocols of the size of Aave, Maker, Uniswap, Eigen, and more have a responsibility to support the broader ecosystem. Since they are currently barely/not doing it, **it’s our job to remind them and advocate in that direction**, as that’s the beauty of DeFi: if they fail to do it because they see no immediate benefits for them, I’m convinced that they will suffer long-term and face real costs because of it.

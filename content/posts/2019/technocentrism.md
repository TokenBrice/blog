---
title: Why is technocentrism killing blockchains?
description: >-
  Blockchains are the future, let’s make sure they live by its standards: the
  people of tomorrow are diverse and inclusive, so why can’t we?
date: '2019-05-07T11:39:41.016Z'
categories: [🧔 Opinions]
tags: [Diversity, Proof of Stake, Lightning Network]
---

![Photo by [Agnieszka Kowalczyk](https://unsplash.com/photos/c0VRNWVEjOA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)](/img/2019/technocentrism/cover.jpeg)
Photo by [Agnieszka Kowalczyk](https://unsplash.com/photos/c0VRNWVEjOA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

From its very early days, the blockchain industry was a world for geeks. It really made sense at first: I think it was a conjunction of two main factors. First, technical profiles were already deeply involved in promoting the values (autonomy, privacy, trustless cooperation) that blockchains can deliver. Moreover, at the humble beginnings, the roadblocks were technical ones involving “hard science” fields: mathematics, cryptography, game theory, etc.

However, as the blockchains developed (Bitcoin is 10 years old!), the people involved did not get any more diverse. **Right now everybody is so focused on the tech that the whole industry has a tunnel vision.** Go to meet-up and see it for yourself: it’s only tech talk. Every time you go to one, you’re left scratching your head wondering if we even need such a complex solution to a problem you’re not even sure exists.

I think **that just like any major government institutions, “the blockchain industry” (if that’s even a thing) is already suffering from groupthink and lack of diversity.** The `15-35 years old, tech-focused, guy` description matches 95% of the profiles.

From a high-level design perspective, we know it's simply inefficient at best, if not profoundly detrimental: think about the decisions our `45-75 years old, male with elite education, rich, white` politicians come up with. Diversity is not just a shiny cool thing to add to show you're progressive: it's actually the **biggest success driver of success for any given group, even before education or expertise.** (_see reference 1_)

We’re direly missing outsiders, people who will look at the systems being designed and ask the “naive” yet hard and insightful questions. I intend to demonstrate that to you with two very simple examples — I’ll explain the concepts I’m referring so you won’t need to be a tech lad or a blockchain-expert to follow my though process.

#### Proof of Stake — the “humans are rational beings” assumption

_ℹ️ Blockchains need mechanisms for their different participants to reach a consensus. The most famous one is called Proof of Work and involve mining: people dedicating computational power to solve a mathematical challenge in order to verify transactions, and being rewarded for doing so. Proof of Stake (PoS) is another take to solve this problem: instead of the computing power, this time people lock “stakes” (coins of the given currency) in order to validate a transaction._

Essentially, **we’re making with Proof of Stake the very same mistake economics — as an academic field — has been making from day one: assuming that we are all rational beings who behave logically, always trying to maximize our own best interest.**

More specifically, in the case of proof of stake, the whole system holds onto the premise that people don’t want to lose money: so if they start to misbehave (trying to game the system), they will have their “stake” slashed, potentially all of it.

The elephant in the room that is rarely accounted for, as you probably understand already, is that **people are sometimes willing to lose money because they act on other motives**: love, hate, rage… I can picture dozens of scenarios where a group of people would be willing to burn millions if not billions of dollars just to destroy a chain, but one will be enough:

*   Let’s say a PoS protocol becomes increasingly popular, to the point where major banks are worried. Three of them realize that by banding together, and with a little disinformation/scare campaign, they can crash the price 30–40%, and then expand barely a fraction of their annual income to progressively take control of the chain. The coins they buy to destroy the chain are accounted as a cost. They’re not motivated by profit: they are motivated by fear, which is potentially the strongest human driver (_see reference 2_).

_ℹ️ There are ways to protect a chain against such an attack, my point is more about the issue of making the assumption that humans are rational while designing this consensus mechanism._

#### Layer 2 — Getting lost in the tech, losing sight of real usage

Maybe you’ve heard about what we call layer-2 solutions? They are essentially networks built on top of the base network (Bitcoin or Ethereum) to allow faster and fee-less transactions. The most prominent developments include Lightning network, Plasma, Casper and or other state chains. We’ll focus on Bitcoin’s Lightning network as its mains flaws are shared by most others.

The problem is simple: **some layer 2 solutions somehow managed to provide a worse user experience than the base layer**. Here are the restrictions of the Lightning Network, that will never be lifted because they are due to protocol-level decisions:

1.  A channel must be open to receive/send money (aka you must be “online” to send/receive).  
     — You don’t have to, on the base layer.
2.  A channel must be provided with some currency to be opened. **It cannot allow the transit of more currency than what’s in it**. Say you open a channel with 1 BTC, someone sends you 10 BTC — doesn’t matter, you won’t be able to get more than 1 BTC out of it.   
    — The base layer knows no limitations to the amounts you can send (as long as you can face the transaction cost) and receive.
3.  Most of the transactions are settled off-chain (except the state update — the settlement when you close a channel), which means they are low-fee and fast, but you also lose the security and accountability provided by on-chain settlements.

So from a very high level perspective, the layer 2 tradoff is as follows: you loose most (if not all) benefits provided by blockchains + you have to face additional significant limitations but your transactions are faster and cost less. Why such a need for speed? An Ethereum transaction currently takes [~20 second](https://etherscan.io/chart/blocktime)s.

Now, this is where it gets funny: this whole thing has been in development for more than 3 years. So far, there are no real usages or use cases provided by layer-2 solutions that you can’t do better with the appropriate base layer solution. There will never be. Yet we have hundreds of technical papers discussing its potential implementation and crowds getting hyped at the idea of the Lightning Network making small, incremental progress.

If you go a meetup talking layer-2 you’ll meet a crowd of semi-enthusiastic nerds discussing the highly technical details of the different implementations. You can ask them my very question: how do you expect this thing to ever be used if the UX is worse than layer 1? They’ll answer you 100% on the technical side, and miss the whole point completely — **breaking through the tunnel vision requires diversity, from within and at an early stage of the development.**

### Don’t leave blockchains to the geeks!

Blockchains are more than just cool technology. **They are protocols to implement societal-wide change.** Mass adoption will disrupt the organization of the whole world, so we need people from all backgrounds and perspectives to make it happen.

1.  We need **psychologists** to understand, at the individual level, the current worries people have with blockchains.
2.  We need **sociologists** to help us figure out how, at the macro-level, we can answer and articulate these concerns to initiate of change of habits.
3.  We need **literary profiles** to help us craft a narrative of change and tell an inclusive and compelling story.
4.  We need **magicians** to figure out how we can captivate audiences with that story.
5.  We need **artists** to give a body to the story of the Etherial world — one people can identify and resonate with.
6.  We need **philosophers** to consider the fundamental consequences of these changes and anticipate their impacts on how we see the world.
7.  We need **waiters, taxi drivers, and stewards** to keep a direct channel with every layer of our society, reminding us of its beautiful diversity.
8.  We need **social workers** to help us design systems adapted to the realities of everyone.
9.  We need **teachers** to sensitize students as to why privacy, autonomy and decentralization are necessary to be self-sovereign and truly exercise our free will.
10.  Hell, we even need **public servants** to understand how to jump from the protocol to the actual real-life implementation, with all its frustrations and the nitty-gritty.

Blockchain is the world of tomorrow, let’s make sure it lives by its standards: **the people of tomorrow are diverse and inclusive, so why can’t we be?**

Do you want to give involved in blockchains while not having a technical background? [Feel free to reach out](https://twitter.com/TokenBrice), I’ll do everything I can to help you find your spot because you are a NECESSARY addition. Don’t leave the design of the base protocols of tomorrow to the nerds — they’ll do an awful job at it solely by themselves.

_⚠️ My opinions are solely my own — I’m expressing myself outside any professional quality or relationship. And yes, I mostly fit the blockchain mono-profile of a 15–35yo privileged white dude, except for my education not being science-focused, which is yet another proof of my whole point: we need diversity._

#### References/Further Reading

1.  [Effects of Diversity in Teams and Workgroups: A Qualitative Systematic Review ](http://www.ijbhtnet.com/journals/Vol_7_No_2_June_2017/2.pdf)— Seyhan Güver&Renate Motschni for the _International Journal of Business, Humanities and Technology,_ June 2017_._
2.  [Appealing to Fear: A Meta-Analysis of Fear Appeal Effectiveness and Theories](https://www.apa.org/pubs/journals/releases/bul-a0039729.pdf) —Melanie B. Tannenbaum, Rick S. Zimmerman, Justin Helper, Lindsey Saul and Samantha Jacobs for the _American Psychology Association_, 2015.
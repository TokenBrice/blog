---
title: "Farewell to the GHO Liquidity Committee and reflections on the rise of DeFi newspeak"
description: "I've resigned from the GHO Liquidity Committee - this post explains why and reflect on the core challenges observed in DeFi's governance and committees"
date: '2024-02-08T01:13:50.191Z'
categories: [🌌 DeFi]
tags: [DeFi, Ethereum, Decentralized Finance, Stablecoins, Liquidity, GHO, GHO Liquidity Committee]
url: farewell-glc
---

I’ve resigned from the GHO Liquidity Committee and would like, in this blog post, to share more context on its adventures and the learning we can draw from it. 

* [Onchain message from tokenbrice.eth](https://etherscan.io/verifySig/35543)
* [Signer removal transaction](https://etherscan.io/tx/0x39760c8cd33beba102cbcb6a3c50489a24b1a50d8290de7c42c09845cf814dba)

For those whose first reaction will be “ain’t ready all of that,” here is a recap of the main shortcoming I see in the committee that led to my decision:

1. The committee's operating model is inefficient and prevents a coherent vision from emerging and being delivered.
2. The committee's scope of responsibilities is unclear, leading to a passive attitude (towards governance mishaps) assumed by most members.
3. The committee mainly comprises governance professionals who lack any serious expertise in the topic at play – liquidity management. It results in inefficient operations, conflicts of interest because of their numerous other commitments, and subpar use of the Committee’s resources.

Governance is always a challenge. Indeed, it can seem insane to give power to random people on the internet, and it often is. There is a built-in democratic assumption in governance operations – although most governances are purely plutocratic – that severely hinders any serious structuration that would enable delivering upon commonly agreed goals. The GHO Liquidity Committee was appointed by the Aave governance precisely because it recognized – in a flash of lucidity – its incompetence and ineptitude in directional liquidity management.

Yet, after years of experience, I’ll tell you what’s even more crazy: giving power to people that the crowds perceive as “experts” on a topic. It’s all a show: the most recognized and mediatic expert of a given field is never the one actually the most informed on the topic. I, for one, would know quite a bit on the matter, with my own field of expertise — liquidity management, shaping, and incentivization — a topic prone to public perception manipulation more than any other because of the financial stakes inherently associated with it.


## The case of the CRV Wars

Let’s illustrate: regarding liquidity, the word on the street is that Curve is the best model, and all pros and experts use Curve, right? **It’s so good that over the last round (62), projects are spending $1 to receive $0.7 of incentives to their pools**: an instant donation of 30% of the amount they spend on bribes to veCRV/vlCVX holders. It means that if projects which bribed would have allocated the same amount to direct liquidity mining instead, they would have delivered 30% more $ to their LPs and thus attracted more liquidity for the same cost, all of which without assuming the price risk associated with CRV fluctuations for a week.

![curve-bribes](/img/2024/farewell-glc/votium-round-62.png)

So what’s happening there? Quite a few things, and it’s not the main course on today’s menu, just the appetizer, so I’ll go over this quickly:

1. **Most projects have no one internally competent with liquidity**, so they often do random wastes like these. Many prominent DeFi projects recognized for the liquidity games are big spenders but not exactly savvy.
2. **The Curve Wars have been a meme for a while**: there have been no genuine new entrants in these wars for ages – simply because it’s not worth it financially for most players, especially those without ties to the Curve ecosystem. Moreover, the liquidity structures available on Curve (stableswap and V2) are suboptimal compared to Uniswap or Maverick for many very common types of DeFi tokens – LSDs, LRTs, loosely pegged stablecoins, and liquid wrappers. You can confidently mark any protocol outputting a token of this type building liquidity primarily on Curve as inapt in liquidity management.
3. What you are left with are **“insider protocols,”** teams building on top of the Curve ecosystem who usually own sizeable veCRV/vlCVX positions, allowing them to recoup a large share of their bribes (1. Own veCRV/vlCVX ⇒ 2. Post a bribe ⇒ 3. Vote on the pool you just bribed ⇒ 4. Collect and repeat next round). This tactic manipulates public perception into thinking that real money is being spent on these Curve wars. Some of these now insiders are originally external protocols, such as Inverse or Alchemix, which decided to kiss the llama ring for the better and the worse.

Don’t take my word for it; simply look at the top spenders: Frax, Convex, Alchemix, CLever (Aladin), Prisma, Conic, Inverse, etc. **To make it easy to visualize, here are the top spenders of the last round, ranked by amount spent, with the insider protocols highlighted in red**:


![curve-bribes](/img/2024/farewell-glc/top-bribers.png "Top bribes in Votium CRV epoch 62")


Enough with Curve, llamas already hate me; I just wanted to highlight the example of Curve, “the king of liquidity,” being a poorly efficient venue to build and sustain liquidity. Curve, “maker or breaker of stablecoins,” as the DEX with arguably subpar liquidity structures for most stablecoin pools: **Newspeak arrived in DeFi, and public perception/words used are often entirely at odds with the onchain observable reality**. Sadly, a similar pattern has been observed with the GHO Liquidity Committee, today's topic, so let’s get to it.


## The case of the GHO Liquidity Committee

**The GHO Liquidity Committee is a prime example of expertise misplacement**, as it was composed of an unhealthy mix of professionals “DeFi politicians” (more on this below), people with low expertise and vested interest in a given DEX, and people close to the Aave’s DAO / ex Aave team but devoid of any expertise on the topic of liquidity.

It led to a waste of resources, baseless struggles, and heavily misinformed decisions. At the end of the day, the **GLC is like a big bag of cash everyone was trying to pull from to direct to protocol they have an interest in**.

So let’s dive in: what were its limitations, and what anyone interested in governance, whether committee-based or not, can learn from it?


### Operating model of the GLC

In its first months, the GLC operated erratically, sometimes leading several initiatives that were at odds with each other and needed a more coherent vision. It was simply a bunch of degens with a large amount of GHO in a multisig **spraying and praying**. The pinnacle was reached when bribes were allocated to a pool whose liquidity shape was detrimental to the repegging efforts, which, luckily for the Committee, ended out of range before the emissions began, enabling its prompt termination: a net burn of GHO.

I was eventually elected head of the committee and [assumed a temporary and objective-based dictatorship](https://x.com/TokenBrice/status/1719328410479059227?s=20). It enabled the committee to stop allocating resources on liquidity support that were doing a disservice to the cause of repegging GHO and **focus the energy, resources, and efforts where it actually mattered.**

Yet the story also raised eyebrows and attracted media attention ([CoinDesk](https://www.coindesk.com/business/2023/11/28/aaves-gho-stablecoin-nears-elusive-dollar-peg/), [DeFiant](https://thedefiant.io/benevolent-dictator-succeeds-in-bringing-aave-s-stablecoin-gho-near-parity-with-usd), etc.) as it highlighted the failure of governance by itself – at least from the perspective of said media. **During my two mandates, two targets were set: the first was missed by a few basis points (after an increase of ~200 bps), and the second was missed by a few days**. My targets were ambitious, especially considering that they relied as much on deliverables external to the liquidity committee (interest rate management, single-sided staking for GHO, etc.). After two terms, I let go of the leading role early in January.

⇒ When governance elects a committee to handle a specific task, it acknowledges its inefficiency on the matter. **Such committees should not shy away from appointing a leadership, as ownership and responsibility can be very healthy,** especially in “decentralized” governances where the eminences are often gray, and thus ownership and responsibility often lacking.


### Scope of the GLC

The GLC inherited several “governance debts”: decisions made by the governance that prove absolutely indefensible in the current state of affairs and operations. It failed even to find the will to challenge them and instead decided to enforce them despite the warning of a couple of committee members.

Example: Mobilizing the CRV of the committee as sdCRV, a subpar option at the technical level, as it requires weekly voting of the committee (no vote carry-over), has low liquidity, and strips the committee of its due CRV gauge voting power unless it owns veSDT / benefits from a veSDT boost delegation, all of that in a lovely ethical mess, as it strengthens ties with a protocol/team that operates with many questionable practices and several committee members are veSDT holders and in proximity with the said team.

{{< notice note >}}
⇒ The scope of any appointed committee must be clearly defined – and the committee should be able and willing to challenge decisions previously enacted by governance on its matter of expertise.
{{< /notice >}}

### What “professionalism” means in DeFi newspeak 

Participants in groups such as the GHO Liquidity Committee are expected to be “professionals” — you, dear readers, and I would understand by that: master of their topic, accurate, always trying to serve the committee's purpose, and available for their mission.

But we’re misplaced, as in DeFi newspeak, “professionalism” has an entirely different meaning; it’s actually the opposite, as DeFi “professional” profiles tend to:


* Make no waves, and avoid anything perceived as “political”, even if that means associating with scammers: you cannot put business partners in a tough spot.
* Silence truths that are hard to swallow but would be of public interest to enable the community to learn from previous mistakes. For instance, **the failure of the developers of GHO to anticipate the depeg is never discussed**. However, it had been expected by many – myself included — up to one year before GHO’s launch. The interest rate model and the absence of a GHO single staking option at the launch were both apparent lacks that any competent stablecoin developer should have anticipated and resolved **before launch**.
* Harness structures such as the GLC to promote the protocol they have vested interests in by all means possible, even if that means arriving at situations that, if described honestly, would qualify as conflicts of interest.
* Demonstrate, by their onchain initiatives and the communication they share in private groups, an approximate, if not missing, understanding of the topic of their expertise.

{{< notice note >}}
⇒ Participants in governance should learn how to place their trust better. Thanks to their existing platforms, the most publicly visible figures are usually selected when committees are elected. 
{{< /notice >}}

My presence in this committee was an oddity that emerged out of necessity, as governance knew that a deep understanding of liquidity shaping, especially Maverick, was needed to give the GLC the best chances of success. Many actual experts hanging around governance forums and Discords remain powerless despite their knowledge and good intentions simply because they are not well-known figures in DeFi.


### The rise of DeFi politicians and its consequences

Governance is a theater. Anyone involved in DeFi knows that, but even myself was surprised to realize the extent of the scenarization of governance interactions. Just like IRL politics, where we have professional politicians devoid of expertise about the topics they are handling, we’re observing the same phenomenon in DeFi, where a caste of politicians is assuming an increasing responsibility over various DAOs.

**Such profiles specialize in governance-related operations and operate exactly like the IRL PR specialists: their primary care is about public perception and how to manipulate it to achieve their purpose** (usually obtaining the allocation of a sizeable budget from the DAO to their governance structure). Governance discussion is not happening publicly on the forum — the forum is just a stage. The actual discussions are happening backstage: in calls, IRL meetings, and DMs. Discussions on the forum are avoided as much as possible, especially if they are anticipated to be controversial. The forum is simply here to record previously and privately discussed matters: look at the conversations on most proposals: they look so fake that, at this point, one could suspect bots are talking to one another, which once again reminds me of IRL politics. It happened to me several times that such a profile contacted me as I was typing an answer to their governance post, trying to avoid any form of public discourse:

![typing](/img/2024/farewell-glc/gov-typing.png)

{{< notice note >}}
⇒ Confirmed DeFi politicians (= those who earn their money mostly/only through governance-related activities) should simply be banned from participating in any structure having even a remote power – as they are the bane of decentralization, the devil in Prada of DeFi. The professionalization of governance is synonymous with its capture and thus centralization.
{{< /notice >}}


## Parting Words

As [Hayden puts it](https://x.com/haydenzadams/status/1710510768469237827?s=20), **governance stands at the bottom of the tier list in terms of decentralization and thus should be a solution of last resort.** Not only is it inefficient, but it’s also simply too prone to be manipulated, and the probability of it happening increases with the power and resources the governance manages. **Once a given governance has grown enough, its corruption is simply unavoidable**, at least under the current dominant plutocratic governance model: 1 token = 1 vote, hello stone age of governance we’ve been seemingly stuck at for five years.

To wrap this up, allow me one last analogy with IRL politics since we’ve established that similar actors participate in DeFi’s governance. Governance professionals love to dismiss ideas because they deem them “too political.” It enables them to appear as reasonable, non-aligned figures. Yet, **non-alignment does not exist: every decision is political**. Those who say otherwise usually tend to be positioned at the “extreme-center” end of the spectrum: a brutal profit maximalist alignment wrapped in a costume of gentle neutrality, aka the DeFi equivalent of an Emmanuel Macron.

When it comes to committees appointed by governance, I am unlikely to participate in any other after this one – unless its scope is clearly defined and it's given the means to challenge governance's suboptimal decisions.

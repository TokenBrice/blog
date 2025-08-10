---
title: 'The Hitchhiker''s Guide to Crypto Bullshit: How to spot a shitcoin?'
description: >-
  An overview of the main things to watch for in a cryptocurrency project and
  some tricks to spot the red flags before it's too late.
date: '2018-07-05T10:36:25.787Z'
categories: [Tutorial]
tags: [ICO, scam, Ethereum, Decentralisation, EcoCrypto]
---

![](/img/2018/hitchhikerguide/cover.jpeg)

Looking to invest in an ICO, or get your hands on some already traded coins? Awesome, welcome aboard! Before you jump in, let me give you some clues to spot shaky projects with examples taken from actual ones. These tips come from my experience (and failures) as well the discussion I had both with friends and the cryptocurrency community.

### The Whitepaper is ALWAYS the most insightful resource

Whitepapers (WP for the rest of this article) can be scary. While some manage to keep it short (~10 pages), others can reach the hundreds yet it’s the best place to gauge the seriousness of a project. **It’s still the first thing I check once I’m seriously considering a coin**. So what should you be watching closely in a WP?

#### The English Language

Surprising? Not so much if you put it this way: **how to trust an organization unable to put out a flawless WP with a decentralized cryptocurrency project?** It might seem small or even petty, but if you find a low-quality English or repeated typos in the WP, you better start running.

#### Big Promises with technical vagueness

This is probably the most common, as most people won’t read the technical parts of the whitepaper. Even if you don’t fully get the technical details, the difference between a WP trying to cover its lies and a transparent one are quite apparent. [SFIcoin is the perfect example of this — DONT INVEST: SCAM](http://www.sficoin.co/white-paper/white-paper.pdf), the full recipe is here:

*   **Big promises that don’t mean anything**: “The Next Global Paying System”.
*   **Unbacked claims**: their WP that details the vision, the roadmap, the use cases but doesn’t address AT all the tech.

> Last but not the least, the SFICOIN is just going to be the first leading peer to peer cryptocurrency to manage the high-value instant payments.

*   **“We will be the first to X”**: massive red flag. There are no certainties in cryptocurrencies.
*   **A WP made by marketers for marketers** lot of visuals, a lot of work on design but overall it’s empty of real meaning.

It’s ok for a WP to get quite technical (here is Stellar’s — XLM), but it’s not OK to cover an absence of technical solution with jargon.

![stellar-wp](/img/2018/hitchhikerguide/stellar-wp.png)

#### The Darwin Awards of Whitepapers

Wanna see how does a terrible WP looks like? [Check Narbonne’s](https://narbonne.io/Narbonne.pdf), it’s been 7 months and I can’t find any worse. Out of the 22 pages, ~18 are spitting copy pasta about the future. Most of the paper is very generic, and so many things in it are so off. I had to pick one so here we go, the comparison between Narbonne, Ether**i**um and Wa**w**es. Yes, you read it right, they can’t even spell Ethereum and Waves properly.


![narbonne-wp](/img/2018/hitchhikerguide/narbonne-wp.png)

So many things need to be debunked in this table, it’s actually a good exercise. Here are a few you do the rest:

*   “Bookkeeping at the [blockchain](https://hackernoon.com/tagged/blockchain)”: I’m not even sure what it means, but I think a project like [Request (REQ)](https://request.network/#/) covers this for Ethereum.
*   “Mobile Banking”: Hello [OmiseGo](https://omisego.network/)!
*   “AI, chatbot, voice control”: strictly no use for the project (an infrastructure for banks) but buzzwords so they had to be here!

#### How does a proper WP look like?

A WP is a **technical document** usually presenting at least:

1.  The vision for the project / what problem the team is trying to crack,
2.  An overview of the technical solutions proposed to the problem and why they were chosen,
3.  The details of the technical implementation of the chosen solutions,
4.  A credible roadmap for the delivery,
5.  Technical information about the token: token type, total amount, token mechanisms…
6.  Specifications for the ICO, if any.

To hone your skills, there is nothing better than the OG! I invite you to read the [original Bitcoin’s whitepaper](https://bitcoin.org/bitcoin.pdf) written by Satoshi. You can also check:

*   [Ethereum’s WP](https://github.com/ethereum/wiki/wiki/White-Paper) to remind you that **the design doesn’t have to be fancy** (it’s a GitHub wiki) if the fundamentals are sound.
*   Cardano’s WPs: split between a “[philosophical WP](https://www.cardano.org/en/philosophy/)” and [academic papers](https://www.cardano.org/en/academic-papers/), I think the team does an outstanding job to make their project intelligible to those interested.


### The Transactions per second myth

Now that we’ve got the whitepapers covered, let me address another big chunk of today’s article: the myth of the transactions per second (TPS).

#### Transaction per second: A convenient lie

**TPS doesn’t mean anything at all.** So why is it so popular? Well, it’s a bit like the GHz for processors: it used to be the only thing advertised. It makes sense in a way, **it gives the impression** that you have a standard allowing you to compare different processors that are actually not comparable: higher is always better right?

Well, no. You can have a 32 bit 1 core processor operating at 3.5 GHz and a 64 bits 8 cores processor operating at 2 GHz. Guess which one delivers the most computing power? It’s the second one without a doubt.

It’s exactly the same for the tokens, except it’s not only the power that matters here. Let me pull [a quick reminder from my previous article if you missed it](https://medium.com/coinmonks/why-decentralization-matters-a-12-min-overview-for-the-layman-6ec572d35af6):

> The choice to make a system more decentralized isn’t made for performance; it’s made for the advantages provided by decentralization. It allows creating new kind of services offering guarantees that weren’t possible before.

Even if the TPS is meaningless, it’s almost expected now. Newcomer investors will put significant trust in this very misleading indicator, and most projects advertise a given TPS. Good! It gives you a good sign of how honest they are:

#### Using TPS to cut through the crap

Consider coin A, advertising 1M TPS and coin B advertising 10 TPS. What about the features they support? What about decentralization? What about the team vision? Community support? Simply by looking at the number, I know now that Coin A is bullshit and coin B could be OK.

![nano](/img/2018/hitchhikerguide/nano.gif)

**The current state of the art of tech allows for a maximum of ~10 000 TPS (already huge) without excessive centralization.** Any coin promising something higher than this is either:

*   **Making compromise on decentralization.** [The prime example of this EOS](https://medium.com/@CryptoPeterG/eos-centralization-problem-bd7a392eeed2) and its 21 block producers that have tremendous power over the network.
*   **The lab scenario**: you can see some coins advertising crazy TPS, some will even show a test network supporting their claim. The thing to look for is the setup of the test network: usually, it’s just a few nodes. It’s easy to reach a high TPS on a three nodes [network](https://hackernoon.com/tagged/network), but it gets harder and harder as the nodes multiply.
*   **Banking on novel and previously untested technological solutions.** [NANO](https://nano.org/en) uses a new kind of ledger called block-lattice and supports up to 7 000 TPS in ideal conditions. [IOTA](https://www.iota.org/) which uses another radically new solution (the Tangle) currently supports ~800 TPS, but it will scale with user adoption. Those two are the most radical “ledger innovations” there are and the most promising. They are the current state of the art: to me any project advertising TPS over this without an equally radically new technical solution is instantly suspicious.
*   Including **off-chain scaling** solutions in their computation of TPS, which leads back to point one: excessive centralization.
*   **Including new mechanisms such as sharding** in their computation. Ethereum which has arguably one of the most robust dev community there is, is still 1 to 2 years away from a live implementation of sharding. How could a bunch of newcomers pull this in 6 months?
*   Pulling this number out of their hat.

_Note: A cryptocurrency development project often starts quite centralized. What matters is that the team have a plan to open up the network progressively. For instance, NEO is quite centralized for now, but now that the infrastructure is sound_ [_the team is making moves towards decentralizing more_](https://neo.org/blog/details/4089)_._

Before we conclude, let us dive into the crazy world of ICOs, it’s such a wild west that it deserves another section by itself.

### ICOs red flags to look for

#### Huge discounts for early birds

If you see an ICO offering huge discounts (>30%) on the first phases of the sale that’s usually a recipe for disaster. Indeed, it means:

*   Since the early birds get such a large discount, they have a **strong incentive to dump at ICO price or even a little below** once the token hit the market: it’s guaranteed free money if they sell fast enough.
*   Why should the team need such a strong incentive to drive the sale? I see this pattern a lot for **tokens with close to no utility**.
*   Even the two situations above don’t unfold, one is guaranteed: huge discounts push towards a concentration of the tokens in the hand of a few: it attracts whales. Massive discounts are a recipe for **political centralization and governance problems**.

#### No product, demo or code

The big risk with ICOs is that you’re essentially investing on a promise or a vision. Yet some ask for money once they already have a working alpha while some others run straight to the ICO as soon as the WP is ready. The latter is much riskier. If there is an alpha or a demo version available, please do check it out!

Even if you’re not a dev, **it’s always insightful to check the GitHub repository of the project.** GitHub makes it easy to see how active the repository is, even without looking at the code. This method is far from perfect are there are ways to make it look like a repo is active even if it’s not.

#### The team doesn’t match

If you are seriously considering investing in an ICO, I urge you to google the most prominent team members. Look at their LinkedIn, their Twitter, their previous companies, etc. If you find inactive profiles, it’s usually a pretty bad sign. You might also find skeletons in the closest, such as one team member who participated in another crypto project that turned out to be a failure or a scam.

![Screenshot for [Banano, a NANO fork](https://banano.co.in/) that doesn’t take itself too seriously](/img/2018/hitchhikerguide/team.png))
Screenshot for [Banano, a NANO fork](https://banano.co.in/) that doesn’t take itself too seriously

A low quality or frequency social media presence is also a bright orange flag. These guys will have to market their project, acquire users and partners. If they can’t market themselves, it’s already a shaky start.

**It’s also very common for ICO scams to advertise a prestigious advisor… that has nothing to do with the project**. Double check any high profile figure to make sure they are actually involved in the project. If you see Satoshi as advisor, RUN!

#### Inappropriate token distribution

The token distribution chart is usually present in every WP. If it’s not, it’s essentially like “give us your money, and we won’t tell you what we’ll do with it”… RUN!

It usually looks like a pie chart. The most transparent projects have two: one for the distribution of the tokens, and one covering how the funds will be spent by team.

![Storm token distribution is pretty good ([source](https://blog.stormtoken.com/token-structure-and-ceo-update-bd055860251e))](/img/2018/hitchhikerguide/distribution.png)
Storm token distribution is pretty good ([source](https://blog.stormtoken.com/token-structure-and-ceo-update-bd055860251e))

It’s ok, even good that the team reserves a share of the token for the development of the project. You have to watch the share allocated to the team: it can range from 10% to 30% for the reasonable projects.

On the other extreme of the spectrum, you have coins like Ripple (XRP) for which the team owns ~60% of the total supply. It is a significant risk for token holders: first, it’s an enormous vector of centralization. Besides, it means that **the team can heavily manipulate the price of its coin**.

_Note: A few months ago, facing a backlash against this very centralized distribution, the team put an escrow system in place using a smart contract._ [_55 billions tokens are now placed in escrow_](https://ripple.com/dev-blog/explanation-ripples-xrp-escrow/) _and released at the pace of 1 billion per month. It doesn’t change anything to the underlying centralization issue and makes me wonder which kind of team would need $500 million (current price of XRP ~ $0.5) each month for its development/partnership/other. Besides,_ **_since these tokens are now locked they are not counted in the circulating supply (~39B)_**_, which might reassure investors but is purely misleading. The actual supply is 100B tokens. Personal view: the whole move feels like a marketing stunt._

### Conclusion

I wrote this article to provide you with some clues to help you spot unreliable crypto projects. Overall, I hope that you understand by now that **the more you read before investing, the lower the risk will be**. I advise you NOT TO INVEST IMPULSIVELY. Even if it’s the best project in the world, you can sleep on it, read some more and decide a couple of days later with a fresh outlook if you want in or not.

To finish, let me give you more tricks I use to get a quick idea of the seriousness of the project:

*   Google search `site:reddit.com "token name (+scam/shitcoin/issues...)"`: this method allows you to search Reddit for a specific token. If there is a massive red flag on the project, it's usually documented somewhere on Reddit. _Additional note: Reddit is getting quite tribal now. The best place to find reliable information on a given token is certainly not the token subreddit. Don't go to /r/Ripple/ if you want an objective perspective on XRP._
*   **Don’t trust one single source, always cross them!** Greedy people are promoting shaky projects all around the internet, never blindly trust just one guy even if he seems to be honest.
*   Several services exist to organize the community due diligence on ICOs. [ICOCheck](https://icocheck.io/) is a pretty reliable one, but do your own due diligence.

Last but not least: **I strongly recommend you to not invest in ICOs for at least the first year you’ve been invested in cryptos**. A lot of them fail dramatically. You are much better off limiting yourself to the top 25/100/200 tokens depending on the risk you’re willing to take. Even among those, there are many doubtful projects: beware and happy investing!

PS: You have some tricks to spot an unreliable project you haven’t seen in this piece? Feel free to share them below.

Let me know if you liked this article and [check out my wiki for more content like this.](https://github.com/Ahirice/BCC/wiki) **Don’t forget to clap it** **to help it spread:** you can keep pressing  👏up to 50 claps.

This article is the translation of an original (French) [EcoCrypto.fr](https://ecocrypto.fr) story.
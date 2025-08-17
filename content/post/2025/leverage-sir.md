---
title: "Leverage Like a Sir: Polynomial Gains, No Liquidation Pains"
description: "Exploring a novel protocol offering no funding fee no liquidation leverage with convex returns, and announcing my involvment."
date: '2025-03-12T01:13:50.191Z'
categories: [DeFi, Projects]
tags: [DeFi, Ethereum, Decentralized Finance, DeFi, Leverage, Immutable Protocol, Lending, Polynomial]
image: img/2025/leverage-sir/leverage-sir-cover.jpg
url: leverage-sir
difficulty: "advanced"
---


A few weeks ago, Sir Trading, a fascinating novel DeFi primitive was shipped, and I quickly fell in love with it. I’ve also decided to get involved, so welcome to this article introducing Sir Trading, explaining what I found interesting in the model, and announcing my involvement as an advisor.


## Sir.Trading explained like a business

To understand Sir Trading (and it works well with most protocols), we can use a business metaphor: Who are the customers, intermediaries, and stakeholders?

![sir-diagram](img/2025/leverage-sir/sir-diagram.png)

So let’s start from the bottom up: our “customers” are the APEs who open leverage positions and pay fees. Everything else is a "means" to that end.

Our second population is the “intermediaries”, the liquidity providers on the Sir Protocol, called TEA holders, also called “gentlemen”. They are necessary because the more TEA liquidity exists, the greater APE’s capacity to lever up, and thus, the more likely users are to ape at scale. Maximizing this population is essential, as it helps to address one of the main weaknesses of the Sir model: the **absence of leverage decay can only be guaranteed if the liquidity provided is sufficient compared to the leveraged position opened.**

Thus, it makes sense to incentivize liquidity providers with SIR emissions to attract liquidity proportional to APE demand. Additionally, continuous SIR rewards provide LPers with stable income, complementing the volatile minting/closing fees they also earn—a critical advantage, as LPers usually prioritize predictability (cf. Aerodrome vs. Uniswap).

Finally, the SIR holders act as stakeholders. They can stake their tokens to receive ETH dividends from fees collected on positions opening and closing and, in the future, could be involved in a mini-governance centered around decisions about resource allocation (⇒ which vaults to incentivize with SIR emissions?).

With our three core populations defined, we can essentially assemble them into the “business model” of Sir:


![sir-business-model](img/2025/leverage-sir/sir-business-model.png)


SIR Protocol aims to maximize its customer base (APE holders), which drives revenue shared with stakeholders (SIR holders). Stakeholders approve SIR emissions to fund intermediaries (TEA LPers) that provide the liquidity necessary to the purpose and allocate it to the vaults most relevant to drive usage.


## Zooming in on the APE’s side

As mentioned above, the protocol's core is the APE—the ability to leverage any asset traded on UniswapV3. But what makes this leverage so interesting, especially compared to the myriad of other options now available?

The table below should answer the most important questions for anyone already familiar with other protocols offering leverage, such as f(x) or Squeeth:


<table>
  <tr>
   <td>Type of Returns
   </td>
   <td>polynomial (=/ multiplicative)
   </td>
  </tr>
  <tr>
   <td>Max leverage
   </td>
   <td>Up to ^5 with no leverage decay given sufficient liquidity, realistically ~ ^2
   </td>
  </tr>
  <tr>
   <td>Liquidation
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>Rebalancing
   </td>
   <td>None
   </td>
  </tr>
  <tr>
   <td>Fees
   </td>
   <td>No funding fees, only set fees paid when opening or closing position
   </td>
  </tr>
  <tr>
   <td>Assets Supported
   </td>
   <td>Potentially any traded on UNIv3 + permissionless vault deployment
   </td>
  </tr>
  <tr>
   <td>Security Considerations
   </td>
   <td>Protocol to be eventually fully immutable once out of Beta Mode, oracle used is trustless (UNIv3)
   </td>
  </tr>
</table>



As you can see above, I think the offer is quite compelling even when compared to existing options, although it is a bit “weird” if you are used to other more classical leverage products as you have to wrap your head around a few new concepts.


### Polynomial returns?!


First, let’s tackle **the question of linear (most common) vs polynomial leverage (Sir’s case)**. If you are not a math buff, I think the first thing to understand about polynomials is that their impact is increasingly more palpable as the price moves farther from the starting price. It is better to be careful, as it works both ways. Let’s illustrate with a hypothetical simplified position started when ETH = $2000 (fees are ignored for simplicity; we’ll come back to them later):


<table>
  <tr>
   <td>
   </td>
   <td>$2500 (+25%)
   </td>
   <td>$3000 (+50%)
   </td>
   <td>4000 (+100%)
   </td>
   <td>10000 (+400%)
   </td>
  </tr>
  <tr>
   <td>Linear - ETH x2
   </td>
   <td>3 000
   </td>
   <td>4 000
   </td>
   <td>6 000
   </td>
   <td>18 000
   </td>
  </tr>
  <tr>
   <td>Polynomial - ETH ^2
   </td>
   <td>3 125
   </td>
   <td>4 500
   </td>
   <td>8 000
   </td>
   <td>50 000
   </td>
  </tr>
  <tr>
   <td>Linear - ETH x5
   </td>
   <td>4 500
   </td>
   <td>7 000
   </td>
   <td>12 000
   </td>
   <td>42 000
   </td>
  </tr>
  <tr>
   <td>Polynomial - ETH ^5
   </td>
   <td>6 103.52
   </td>
   <td>15 187.5
   </td>
   <td>64 000
   </td>
   <td>6 250 000
   </td>
  </tr>
</table>


You see that last row/column scenario, with our ETH^5 ape reaching a >$6M Valhalla on a mere 1 ETH base position (with a +400% price appreciation)? That’s the power of polynomial returns. What we looked at above is enticing, although it abstracts many factors, including the fees, and assumes no leverage decay for both positions. Picture it as an example of understanding the power of polynomial vs linear in a financial context more than anything else.

Polynomial returns (convex payouts) have historically been overpromised and underdelivered. Delivering them consistently is usually challenging, but they are generally implemented with **corrective factors** of different natures and names: time decay, volatility decay, leverage decay, etc. The usual model for such a product revolves around **managing loans between traders and lenders** to keep the leverage as constant as possible. This leads to models where leveragers constantly stream varying fees to lenders and still see their positions often rebalanced. With Sir, this correcting factor is clear and explicit upfront – that is that steep fee, so let’s dive right into it.


### Fee Structure

Next is the fee model, which is also quite different from the usual. Sir fees are fixed, dependant on your leverage, and charged ½ at position opening (APE minting) and ½ at position closing (APE redemption). At first glance, they might seem quite steep:


<table>
  <tr>
   <td>Leverage
   </td>
   <td>Total Fees
   </td>
  </tr>
  <tr>
   <td>^1.5
   </td>
   <td>17.35% of principal
   </td>
  </tr>
  <tr>
   <td>^5
   </td>
   <td>69.13% of principal
   </td>
  </tr>
</table>


Let’s zoom in on an ETH/USDC^1.5 position to understand better the impact of the polynomial leverage and the Sir’s fees, with a hypothetical position opened at ETH = $2000.

![sir-calculator](img/2025/leverage-sir/sir-calculator.png)

With ETH = $4000 (+100%), such position is up ~17% in ETH terms or ~134% in USD terms. Of course, by this point, you are a polynomial leverage expert, and thus you understand that **the gap between the ETH/USDC^1.5 and raw ETH holding increases the further the price appreciates**. At ETH = $6000 (+200%), the position is now up ~43% vs ETH or ~330% vs USD. At ETH = $8000, we are now at ~65% gains vs ETH and ~562% vs USD. Again, this works the same way in reverse; please remember.

I think this explicits well the “goal of the game” with Sir:



1. Ideally, you want to seize a nice dip + reversal to open your position on a favorable price and quickly earn enough returns to cover the fees.
2. Your goal is then to seize the maximal spread between your opening and closing price, knowing that each % you can grab provides exponentially more returns.

The product's design is well-suited for such plays since you do not have to worry about funding fees or time decay. You’re essentially looking to buy low and sell high; welcome to crypto: except this time, you have a tool amplifying your returns the more you manage to do so.

Because of its fee structure, **Sir is geared toward leveragers with a long-term perspective**, which matches its other key features (no liquidation, no leverage decay). Overall, the fees paid are similar to those that would be incurred maintaining a margin position for a year, striking a balance between potential returns, protocol stability, and upfront costs. When opening a leveraged position, one of the main concerns is getting the timing wrong and chopped by range-bound price action, where the fees accumulate and take away any potential profits; this concern is non-existent in Sir’s model.

Finally, I’d like to remind you one more time of the main limitation of Sir: the absence of liquidity decay can only be ensured if there is sufficient liquidity to stomach your trade. While it’s pretty **reasonable to assume so for incentivized ^1.25, ^1.5, or even ^2 vaults**, it becomes much less certain for ^5 vaults, even with strong incentives, because of the maths I shared above.

If you’d like more data to understand the impact of polynomial leverage in the context of Sir (=fees included), check [the new calculator on the Sir website](https://app.sir.trading/leverage-calculator). 

Note: APE tokens are ERC-20; thus, further composability could be envisioned. It could get interesting as the protocol grows!


## What about the TEA drinkers?

Now that you have a decent understanding of the demand side, the APE/leveragers, let’s jump to the other side, the liquidity providers/TEA holders.

Let’s start with the basics: TEA drinkers are essentially ~counter-trading APEs, as they provide the liquidity APE redeem against if they manage to earn and secure (redeem) sizable gains. When I say “counter-trading” here, I mean it similarly as a UNIv2_ETH/USDC LP is counter-trading the market: when the market is mostly buying ETH (⇒ price goes up), the liquidity providing positions are rebalancing to USDC, and vice versa.

So, even more simply, **TEA holders are shorter against the underlying asset than if they were just holding it**. Understanding this is all you need to be able to project the impact of price variants on your principal. You also have to **keep in mind the liquidity utilization,** as if you are supplying to a vault where there is little/no aping, you are counter-trading little to no one, and your principal exposure becomes similar to a naked raw holding of the underlying.

While TEA holders are “shorter” compared to a naked raw holding of the underlying asset, they remain exposed to its price appreciation.  You can **think of TEA holders as ETH/USD^0-1**.

Now, with the principal cleared out, let’s address the earnings as a TEA holder. It’s pretty straightforward: by default, **TEA holders of a given vault collectively earn all the fees incurred by the APE minters**. Fees are earned in such (same token as the supplied token) and autocompounded. TEA holders can redeem them when burning their position to recover their principal + all the fees accrued.

In addition to the fees earned based on aping activity, **some vaults are also incentivized with** **streams of SIR emissions.** These currently include the most utilized: ETH/USDC1.5, wBTC/USDT1.5, SIR/ETH1.5, and SIR/ETH5. When vaults are incentivized with SIR emissions, ~10% of the fees incurred by the APE are redirected to SIR stakers.

Note: TEA tokens are ERC-1155, limiting further composability, which is a good thing here, as you want to avoid restaking-type situations on those tokens, which are critical to the protocol's proper functioning.


## Noteworthy features

With the above, you should already have a decent understanding of the protocol, so rather than boring you with expansive explanations of each subtleties, I’ll instead zoom in on a few features of Sir I found worthy of commentary:


### Trustlessness maximization

My blog readers will not be surprised to find a section addressing this, as maximal decentralization and trustlessness are my mantras. In that regard, Sir Trading fares quite well, and the design demonstrates the priority given to those two topics by its founders.

Let’s start with the most important – the potential immutability of the protocol. Considering its novel approach and the risks associated with it, making the protocol immediately fully immutable could be inconsequential. Instead, the approach developed here is a progressive path to eventual immutability with four modes:


![sir-beta-mode](img/2025/leverage-sir/sir-beta-mode.png)


Sir is currently in Training Wheels mode, in which some parameters, such as the fees can still be adjusted. From the Training Wheels mode, it can switch to Emergency in response to a bug or exploit and from here to a Shutdown (⇒ Redeploy) if needed. On the other hand, if all goes well, the training wheels can be removed, and the protocol can be switched to Unstoppable mode, where it becomes immutable. I find this approach balanced and interesting, [definitely worthy of studying](https://docs.sir.trading/protocol-overview/beta-period) for other builders.

Now, let’s look at the oracle solution chosen, a critical element for any lending or leverage-based protocol. Here, **the solution is simple and fully trustless: Uniswap v3.** It, of course, has limits, most notably the liquidity available on Uniswap to ensure the price is not easily manipulated. However, considering the top vaults are majors like ETH or wBTC, it’s not a big concern. It could be more of an issue for SIR-related vaults, but here again, the liquidity is reasonably sufficient compared to the token market cap (TVL in pools > 35% FDV). Further mitigation is implemented on the UNIv3 oracle (30 min TWAP) to resist price manipulation better.

Another interesting feature in terms of trustlessness and resilience is the **harnessing of [token auctions](https://docs.sir.trading/protocol-overview/token-auctions) to streamline fee distribution to stakers**. Sir is far from the only one doing this, as, for instance, [Euler Finance harnesses a similar logic](https://docs.euler.finance/developers/periphery/fee-flow/). Such auctions enable the conversion of many assets into one (in this case, wETH) without adding unnecessary compromises to the protocol. I expect to see even more of these.

Note: Xatarrer (founder) has self-submitted a DeFiScan review for Sir Trading, which is currently under review. Please check [DeFiScan](https://defiscan.info/) once the review is published for more details regarding Sir's decentralization.


### Protocol Owned Liquidity

Liquidity is Sir's lifeblood, and the protocol design acknowledges this with **a keen focus on growing permanent liquidity (TEA) reserves**. Every liquidity provider deposit includes a fee (~8.99% of their principal) retained as permanent protocol-owned liquidity. Thus, incentivizing LPers with SIR isn’t just "renting" liquidity—it’s also an immediate partial "buyout" of their deposit.

Thanks to this, as the protocol grows and can attract more liquidity providers, it builds permanent liquidity reserves, enabling an ever-increasing “minimal guaranteed liquidity for APEs”. It’s essentially a virtuous loop progressively solving one of the main drawbacks of the model: elegant!


### Continuous Token Emission Model

SIR works under a **constant emission model at the rate of 2015M SIR per year**, with the lion’s share always going to incentivize liquidity providers. There is, however, a switch in the distribution logic, made to give the protocol the means for its early growth in the first three years:



* For the first 3 years, 68.13 % directed to liquidity providers, 13.65 % to pre-mainnet contributors, 10 % reserved in a treasury, and 8.22 % to investors.
* After that: 100% to liquidity providers.

This model is efficient, as no vesting is needed for the team/investors/treasury, since the logic is wholly shifted here: you have to think in terms of streams of tokens (X SIR/day) instead of total balance and associated vesting.


## Putting your understanding in practice

To wrap things up, we can now articulate our shared understanding of the protocol by studying three different market hypotheses articulated into strategies:


### “I am bullish ETH or BTC over a mid/long time frame”

This one is the most straightforward; it's as simple as minting the ETH/USDC^1.5 APE token. The absence of liquidation and funding fees will allow you to set this position and forget about it. **Your primary metric to watch for here is the opening+closing fee at 17.35%: you need to seize a ~26% price appreciation on ETH to enter profit territory**, with your gains increasing in a polynomial fashion from thereon.

Variants:



* I am bullish BTC: all the same, except using the wBTC/USDT^1.5 APE (main vault: good amount of liquidity available).
* I am bullish ETH against BTC and looking for adrenaline: all the same, except using the wETH/wBTC^5 vault (careful, low liquidity right now)
* I am bullish SIR against ETH: you have several tiers of leverage available to express that conviction onchain (SIR/ETH^1.5 and SIR/ETH^5 being the most liquid).


### “I am bearing ETH over a mid/long time frame”

Really?! No judgment; there is also a vault for that, in the name of USDC/wETH^1.5! Because this vault is USDC based, against ETH, opening an APE position there means going short ETH with polynomial leverage.

Inversely, supplying that vault as a liquidity provider (TEA) means counter-trading the (potential) shorters ⇒ being long ETH (if there is utilization), but from a USDC base this time. However, this vault is not incentivized with SIR emissions currently, so your earnings will stem only from APEs opening positions.


### “I am bullish SIR, but not really a leverage-hungry APE”

That’s understandable; not everyone is a thrill-maxxer. Here, you could consider **harnessing the constant emissions to liquidity providers to build your SIR stash over time and only at capital opportunity cost**. Considering the LP supply fee, you are “forced” to sustain the position for a few weeks/months to reduce the fee's impact. If you are worried about principal depreciation in the case of a significant market reversal upward, you could consider splitting your deposits over several incentivized vaults to hedge for it.

Assuming you initially farm with an ETH or wBTC deposit, you have a compounding option with your freshly farmed SIR: supplying the SIR vaults. Also, consider staking your SIR to maximize a mid/long-term SIR position.


## Discussing My Involvement

Before you, I’d like to give you more context on my involvement with Sir: I am advising the Sir team to help them with my core topics: growth, tokenomics optimization, and BD. I am compensated for this endeavour, and I am also an APE and TEA holder and, therefore, a SIR farmer – **I am long SIR in all possible ways**.

I discovered Sir somewhat recently (the protocol is still just a few weeks old), but the timing was excellent. As those following me on Twitter probably already know, I have been profoundly disappointed with f(x), where I suffered from an abusive liquidation stemming from infrastructure shortcomings on their end (RPCs). 

I was, since then, on the hunt for an alternative solution to f(x) and stumbled upon Sir, which delivers some similar features (“real” no liquidation, no funding fees) but also brings welcome additions to the mix, such as the polynomial leverage vs linear: both the protocol and the timing were perfect, so going the extra mile to help it succeed happened very spontaneously.

I do not approach advisory as a collectible to add to my wallet, show in 2 monthly calls, collect the payout, and call it a day. I am on the opposite side, equally maximally committed, involved, and selective with them. 

With Sir, considering the recency of the protocol, my current contributions revolve around raising awareness for the protocol, helping it get well integrated into the ecosystem, and expliciting its benefits to as many people as possible, as done with this article. I harness my extensive DeFi experience, network, and presence to support the team in all relevant ways.


### My “Valhalla or hell, nothing in-between” position

[I opened a ^5 SIR position on my public wallet tokenbrice.eth](https://etherscan.io/tx/0x5f9038d9004b53501bdf05b3f30d8fc8fd2d8da6a89299a624276c7605bf4ea7) – feel free to track it: 500K SIR levered ^5 ⇒ redeemable for ~155K SIR at inception (~69% fees), opened on Mar-04-2025 08:34:47 PM UTC. If all goes well, I hope to eventually redeem this for ~8M SIR (⇒ SIR at 2x my starting price, assuming sufficient liquidity) and do something fun with it. **I want to remind you that such leverage is the closest you can get to onchain insanity; this position is now known in the community as “Valhalla or hell, no in-between”**.

Note: As a protocol built for resilience, [Sir is also supported by the DeFi Collective](https://x.com/DeFiCollective_/status/1897575989032497390), which received a SIR donation, matched it with ETH, initiated and supplied the UNIv2 LP, and locked the LP token for one year to secure a liquidity baseline on the token.

Disclaimer: This article and the above strategy are not investment advice but practical illustrations of what the protocol can do. You make your own decisions, and you are responsible for them. In case that wasn’t clear enough with the previous warnings: I am exposed to SIR as a token and protocol and stand to benefit from its growth; in other words, I am maximally aligned.

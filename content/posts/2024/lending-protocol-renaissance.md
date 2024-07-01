---
title: "Is this a Lending Protocol Renaissance?"
description: "New models are being explored both for CDP protocols and money markets, and some protocols are even merging the two into one: is this a lending protocol renaissance?"
date: '2024-07-01T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Understanding]
tags: [DeFi, Ethereum, Decentralized Finance, Stablecoins, Stable Assets, Money Markets, Liquity, Tapioca, Dyad, TAP, USDO, BOLD, LUSD, LQTY, Aave, Morpho, Interest Rate, veCRV, veVELO, twTAP]
url: lending-protocol-renaissance
---

![0-lending-protocol-renaissance-cover](/img/2024/lending-protocol-renaissance/0-lending-protocol-renaissance-cover.png)

In the last few months, we’ve seen a flurry of novel and exciting lending protocols come to market, such as Morpho, DYAD, Fluid, or Tapioca; even more are expected in the coming months, such as Liquity V2 (Bold) or Euler V2. All are innovative, in the arena, trying things to the point that I wonder if we’re not experiencing a lending protocol renaissance after a few years of rehashing the same concepts.

Thus, in this article, I’d like to give you a tour of the interesting ideas I’ve seen being explored — we’ll go through some of the protocols mentioned above and, for each, focus on understanding their main innovation.


## Collateralized Debt Position (CDP) protocols vs Money Market

Let’s dive in, starting with a primer on the differences between CDP protocols (e.g., Maker or Liquity) and money markets (e.g., Aave or Morpho). It will come in handy as we will discuss both in this article and even finish with a project merging the two models into one protocol. 


<table>
  <tr>
   <td>
   </td>
   <td><strong><em>CDP (ex: Liquity)</em></strong>
   </td>
   <td><strong><em>Money Market (ex: Aave)</em></strong>
   </td>
  </tr>
  <tr>
   <td><em>Borrower Interest Rate</em>
   </td>
   <td><em>Predictable, can even be fixed or initiation fee only</em>
   </td>
   <td><em>Volatile, entirely dependent on pool usage</em>
   </td>
  </tr>
  <tr>
   <td><em>Collateral accepted</em>
   </td>
   <td><em>Usually limited options, cannot mix collateral</em>
   </td>
   <td><em>Various collateral: a given position can mix several collaterals at once</em>
   </td>
  </tr>
  <tr>
   <td><em>Assets that can be borrowed</em>
   </td>
   <td><em>Only the protocol stablecoin (DAI on Marker, LUSD on Liquity)</em>
   </td>
   <td><em>Diverse – any asset enabled as a borrowable asset</em>
   </td>
  </tr>
  <tr>
   <td><em>Collateral re-hypothecation</em>
   </td>
   <td><em>None</em>
   </td>
   <td><em>Collateral are deposited in a pool and thus potentially re-lent to other users</em>
   </td>
  </tr>
  <tr>
   <td><em>Protocol core challenge</em>
   </td>
   <td><em>Stabilizing the stablecoin outputted & securing enough liquidity on it</em>
   </td>
   <td><em>Attracting sufficient borrowable assets (USDC, ETH) to fulfill borrowing demand</em>
   </td>
  </tr>
  <tr>
   <td><em>Protocol main risk</em>
   </td>
   <td><em>Oracle failure ⇒ collateral value not accurately evaluated ⇒ some users can borrow more than their collateral worth ⇒ stablecoin death spiral</em>
   </td>
   <td><em>Oracle failure ⇒ collateral value not accurately evaluated ⇒ some users can borrow more than their collateral worth ⇒ all borrowable assets are drained</em>
   </td>
  </tr>
</table>


CDP protocols stand out for their ability to facilitate cheaper borrowing costs, thereby stimulating more borrowing-side demand, a challenging feat to achieve. This is due to the unique feature of CDPs, where the user directly contracts debt against the protocol, eliminating the need to source and pay an external stablecoin depositor demanding a competitive interest rate, as is the case with a money market like Aave. The primary challenge with CDPs lies in the stability and liquidity of the stablecoin that is produced.

On the other hand, money markets tend to be more flexible. Thanks to their structure, they allow users to mix and match collateral and can quickly onboard new ones. Yet, they tend to require more maintenance, as collateral parameters must be constantly adjusted to reflect the realities of the market. This creates quite the load for governance, as seen on Aave, where [over a thousand proposals](https://boardroom.io/aave/overview) were already processed in four and a half years: approximately 22 per month. It works, but it seems overengineered; surely there must be a better way.


## DYAD: Flirting with the endogenous collateral taboo

Dyad is a CDP protocol that implements several novel ideas, such as delivering free borrowing to its users, who must own an NFT to partake (Note). It also serves as the protocol's base coordination layer. I invite you to [read the documentation](https://dyad.gitbook.io/dyad-docs-v2/) to become more familiar with it. Let’s zoom in on Dyad’s novel approach when it comes to handling a key topic for CDP protocols: overcollateralization.

{{< notice info >}} For stablecoins, we talk about endogenous vs exogenous collateral. To quickly tell, ask yourself this question: if the stablecoin fails, does the collateral also fail? If yes, your collateral is endogenous (ex: my beloved & defunct [seigniorage-based stablecoins](https://tokenbrice.xyz/posts/2021/seigniorage-basis-vs-esd/)); if not, it’s exogenous (ex: ETH for Liquity). {{< /notice >}}

Stablecoins harnessing endogenous or no collateral can scale quickly, as seen with ESD, Basis Cash, or Terra/UST. However, they can and usually do explode even faster. For this reason, harnessing endogenous collateral is considered a very risky practice – worthy of an instant Red Flag / F on the stablecoin rating agency [Bluechip](https://bluechip.org/).


![1-endogenous-collateral-bluechip](/img/2024/lending-protocol-renaissance/1-endogenous-collateral-bluechip.png "Red Flags on Bluechip")


What I want to focus on today regarding Dyad is its utility token, KEROSENE, which acts as a mechanism for allocating the right to mint against existing surplus collateral in the system. By default, the system's minimal collateralization ratio is 150%. However, KEROSENE holders can deposit it into their Notes to reduce their exogenous collateral ratio to 100%.

Thus, KEROSENE is not technically an endogenous collateral but a mechanism to price and enable users to harness the protocol's exogenous over-collateralization. KEROSENE’s utility gives it a “deterministic value” corresponding to its utility while deposited into a Note. Since KEROSENE is mostly farmed by supplying liquidity on DYAD, it could entertain an interesting flywheel.

![2-dyad-defillama](/img/2024/lending-protocol-renaissance/2-dyad-defillama.png "Dyad TVL on Defillama")

Launched at the end of the year, the protocol has seen gentle and steady growth although still limited. The rollout is progressive: the base functionalities are live (Note, DYAD minting, LP incentives, KEROSENE utility), yet much more is coming: sDYAD, momentum (a mechanism to better align protocol participants), a lending market, etc. It’s worth following for any stablecoin enjoyer such as myself.


## Liquity v2 – The base rate of DeFi

Liquity’s LUSD remains one of the most successful genuinely decentralized stablecoins on the mainnet, so when v2 was announced, it gathered a lot of attention. After researching a novel approach harnessing a reserve model, the team pivoted back to a CDP protocol, growing from learning the first iteration. V2 is expected to be released by the end of the year.

Today, I want to focus on one, in particular, on interest rate management.

Interest-rate management is crucial for all lending protocols, even CDP protocols. The rate can be easily defined based on the market utilization rate in money markets. For CDP protocols, replicating a similar approach is impossible, and other venues must be explored; several were:



* Governance-defined (ex: Maker / DAI): while this approach provides flexibility, it generates uncertainty for borrowers and challenges in governance.
* Algorithmic (ex: Liquity / LUSD): no governance is always better, when possible; however, it doesn’t come without shortcomings either. In the case of Liquity, the set initiation fee proved inflexible, which led to the protocol adjusting to a higher interest rate environment with redemptions and, thus, through a lowering of the overall LUSD supply.

With v2, the protocol switches to an interest rate model (no more initiation fee), which should already provide more agility. What’s more interesting is [how this interest rate is decided: directly by the users](https://www.liquity.org/blog/liquity-v2-why-user-set-interest-rates). The team introduces another protocol-level game with straightforward parameters: redemptions will be processed based on the interest rate paid by the user, from lowest to highest.

Thus, users who choose a very low interest will put themselves first in line for redemptions, while those who pick the highest interest will be maximally protected. To make it easy for any user to partake, interest rate delegation will be possible, with various delegates delivering different mandates expected at launch.

This will allow the protocol to rapidly adjust to all kinds of market environments, from low interest rates to high, avoiding the long redemption phases as seen in v1 while remaining immutable and delivering greater predictability to borrowers.

![3-bold-stability](/img/2024/lending-protocol-renaissance/3-bold-stability.png)

As the protocol gains adoption, the average interest rate observed could even inform beyond Liquity v2 itself, as it will correspond to a base rate borrowers are willing to pay on a risk-minimized and immutable protocol. Riskier protocols will have to offer a lower interest rate to attract borrowers. The v2 packs many more interesting innovations. To get up to speed, I recommend checking out [Bojan’s thread of threads](https://x.com/bjnpck/status/1772227278606389496).


## Tapioca – CDP x Money Market Convergence

Tapioca was launched just a few weeks ago and is still being progressively released, as some protocol components still need to be made live. In today’s highlight, I’d like to focus on two main items:



1. Convergence of the CDP and Money Market model with Tapioca
2. The innovative token lock model harnessed

Let’s dive right in. For more context about Tapioca, as often, [the official documentation](https://docs.tapioca.xyz/tapioca) is a great source.


### Convergence of CDP and Money Market

CDP protocols face a challenge: they must deliver competitive yield on the stablecoin they output to drive demand. Liquity v2 will redirect most of the fees collected, thanks to the interest rate, to BOLD stakers, Maker has the DSR / sDAI, etc.

Yet, another way to ensure stablecoin minters can access competitive yields is to build a money market on top of the stablecoin: that’s precisely what Tapioca is doing. Indeed, Tapioca is essentially a double protocol.

First, there is the CDP—branded “Big Bang,” where users can mint USDO against selected collateral: gas tokens and LSDs. The collateral selection is purposely restrictive, as tokens accepted here directly affect USDO backing. Borrowers pay an interest rate and, depending on USDO’s peg situation, potentially an initiation fee of up to 1% (if underpeg). It enables users to loop-leverage their ETH / LSD exposure or simply harness their ETH / LSD as collateral to borrow some USDO.

Then, there is the money market — branded “Singularity,” which provides isolated markets where users can supply various types of collateral to borrow USDO, supplied by borrowers on the CDP side. This creates a native yield for USDO holders that is decorrelated from the CDP side, as well as offering an elegant approach to handle all types of collateral:



* Censorship resistant majors ⇒ CDP collateral =backing USDO
* Derivatives / more risky tokens ⇒ Singularity = yield to USDO holders without compromising USDO’s backing.

This dual structure allows Tapioca to host various collateral, with appropriate risk-mitigation measures for each. Since singularity harnesses isolated markets, the risk for each collateral onboarded there is isolated, and it can be further managed with its parametrization (LTV, interest rate, and liquidation bonus) and limits.


### twAML: an innovative token-locking model

After following and commenting on the DEX evolutions, starting with veCRV and followed by the improvements we observed with Velodrome (veNFT), I was anticipating seeing token lock models harnessed on lending protocols too. It has been, but only in a primitive manner, with gauge-based emissions & governance token locking to allocate them, such as seen on Prisma.

Tapioca finally delivers with an exciting approach harnessing a new type of token locking (twAML), both for their governance token TAP and for the suppliers of the money market, to secure the supply side and thus drive more borrowing demand. Hence, after Velodrome improved the veCRV model and delivered the first credible improvement over veCRV, we might see its third iteration come to fruition. Here are the highlights:


<table>
  <tr>
   <td colspan="4" ><strong><em>Main Locking Model Overview</em></strong>
   </td>
  </tr>
  <tr>
   <td><em>Name</em>
   </td>
   <td><em>veCRV</em>
   </td>
   <td><em>veNFT (ex: veVELO)</em>
   </td>
   <td><em>twAML (ex: twTAP)</em>
   </td>
  </tr>
  <tr>
   <td><em>Meaning</em>
   </td>
   <td><em>Vote Escrowed</em>
   </td>
   <td><em>Vote Escrowed NFT</em>
   </td>
   <td><em>Time Weighted Average Magnitude Lock</em>
   </td>
  </tr>
  <tr>
   <td><em>Locked Position Represented by</em>
   </td>
   <td><em>None</em>
   </td>
   <td><em>NFT</em>
   </td>
   <td><em>NFT</em>
   </td>
  </tr>
  <tr>
   <td><em>Locked Position Transferable</em>
   </td>
   <td><em>No</em>
   </td>
   <td><em>Yes</em>
   </td>
   <td><em>Yes</em>
   </td>
  </tr>
  <tr>
   <td><em>TKN &lt;> veTKN ratio</em>
   </td>
   <td><em>Solely dependent on time duration, one veTKN per TKN if 4-year lock</em>
   </td>
   <td><em>same as veCRV</em>
   </td>
   <td><em>Depends on twAML – the average lock duration of other lockers: if equal/above, then one veTKN per TKN</em>
   </td>
  </tr>
  <tr>
   <td><em>veTKN &lt;> TKN Decay</em>
   </td>
   <td><em>Yes, linear over time (ex, after 2 years of lock, only 0.5 veTKN per TKN)</em>
   </td>
   <td><em>same as veCRV</em>
   </td>
   <td><em>No Decay</em>
   </td>
  </tr>
  <tr>
   <td><em>Revenues for lockers</em>
   </td>
   <td>
<ol>

<li><em>Pro-rata share of the fees collected on Curve</em>

<li><em>Potential bribes</em>

<li><em>LP boost revenue</em>
</li>
</ol>
   </td>
   <td>
<ol>

<li><em>Weekly rebase added to veNFT</em>

<li><em>Fees from pool voted on</em>

<li><em>Potential bribes</em>
</li>
</ol>
   </td>
   <td>
<ol>

<li><em>USDO Interest Accrued </em>

<li><em>Liquidation Profit Shares</em>

<li><em>USDO Creation Fees</em>

<li><em>Flash Mint Fee</em>
</li>
</ol>
   </td>
  </tr>
</table>




The main innovation lies in the flexibility and additional game theory layer this model implements. Instead of a linear veTKN to TKN correspondence, depending on the time locked and maxing at four years, like with veCRV and veAERO, twAML looks at other lockers' average lock time (magnitude weighted). In practice, achieving a 1:1 TKN&lt;->veTKN correspondence no longer requires a four-year lock but simply to lock for as much / longer than the existing locks. Thus, the lock time will rapidly increase during the first epoch, ramping up from the 4-week maximum initially set up until it finds an equilibrium point and potentially starts to decay.

![4-twTAP](/img/2024/lending-protocol-renaissance/4-twTAP.png "twTAP overview")

Released for the first time with dynamic adjusting, the twAML was met with excessive degeneracy and quickly ramped up over four years. Thus, the team has returned to work and switched the adjustment to epoch-based. The new iteration is expected in the coming weeks, another development worth monitoring for stablecoin and lock tokens enjoyers.

Tapioca is quite the beefy protocol, two years in the work. I’ve barely scratched the surface there, as there are many other components worthy of commentary:



* It’s natively omnichain harnessing Stargate omnichain fungible token standard
* Tapioca, like Liquity, will be one of the few CDP protocols redirecting fees generated from stablecoin minting to its token holders through the twTAP model.
* Rewards for USDO lockers are distributed in oTAP, an option token connected to the twAML logic.
* The protocol is keen on accruing Protocol-Owned Liquidity, both for TAP and USDO, which will enable it to lower its liquidity maintenance costs and potentially turn it into a profitable endeavor.

I wanted to cover more protocols, but this article is already beefy, so I’ll keep it there for today. There are many exciting developments for lending protocols worth discussing, such as the growth of isolated markets with protocols like Morpho or Silo. All of this and more leads me to believe that after years of Aave & Maker dominating the lending protocol landscape, we might see some challengers rising to a similar size, if not overtaking them in the coming years.

I’ll be watching, and so should you.

_Thanks to Gray for the cover image._


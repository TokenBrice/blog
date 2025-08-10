---
title: "BadgerDAO's story: an intro through DIGG"
description: "Badger sits at the forefront of two highly trendy themes: DeFi & BTC on Ethereum. Let's digg in to better understand what the end game plan looks like."
date: '2021-01-30T01:13:50.191Z'
categories: [DeFi, Discovery]
tags: [DeFi, Ethereum, Decentralized finance, Badger, BadgerDAO, DIGG, Elastic Currencies, wBTC, renBTC, Curve BTC pools, gitcoin, Meme, vault, farming, liquidity providing, setts, LP, BTC, BTC on Ethereun, Platformization of DeFi]
toc: true
tocNum: true
url: badger-digg
image: /img/2021/badger-digg/cover.png/
---

Despite launching barely a few weeks ago, BadgerDAO quickly grew into a DeFi powerhouse now **hosting > $1.2B of assets farming**. While I've quickly touched on Badger in previous articles or shows, I think it's about time for a dedicated piece focusing on DIGG but not forgetting about its context.

## A quick intro to Badger DAO

BadgetDAO is a community-driven project with a clear value proposition: to help **build the infrastructure needed to relay BTC into DeFi**. This core vision manifests through all their products, all centered around representations of Bitcoin on Ethereum like wBTC or sBTC and the native tokens - BADGER and now DIGG. 

### Clear value proposition: BTC on Ethereum optimizer

The first layer of this onion is pretty straightforward: Badger offers a Yearn-like service for BTCs on Ethereum: users can deposit tokens representing a position in a Curve BTC pool to earn BADGER & DIGG on top of the native APY.

![badger-sett-overview](/img/2021/badger-digg/badger-stats.png/ "Overview of Badger's key metrics with Sett.Vision")

There are also vaults (called "setts") available for BADGER and DIGG themselves, as well as their respective LP tokens on both Uniswap and SushiSwap.

{{< notice tip >}}
Setts function like the Yearn vaults, inspired by the aTokens design on Aave: initially when the vault is launched, the correspondence between the base asset and the vault token is 1:1. As the vault accrues additional tokens through its harvests, the vault token increasingly represents more and more of the underlying asset.
{{< /notice >}}

This value proposition by itself is nothing new and could have been delivered by Yearn directly. What makes Badger special is **how the team approaches building the product and the whole underlying vision behind it.** 

### Community-focus

Since the start, the community has been put at the center with Badger. It's clearly visible simply by looking at the token distributions[^1]:

![badger-distribution-overview](/img/2021/badger-digg/badger-breakdown.png/ "Overview of the BADGER token initial distribution")

![digg-distribution-overview](/img/2021/badger-digg/digg-breakdown.png/ "Overview of the DIGG token initial distribution")

Indeed, the two largest shares of the supply of both tokens were allocated to the liquidity mining program - rewarding active users of the protocol as well as the DAO's treasury tasked with structuring the long-term operations of the protocol and its growth.

The airdrops, along with the vaults created a very attractive loop for the receivers: unlike the UNI airdrop where most people choice was to sell or hold, with BADGER & DIGG, people **optimistic about the protocol from the get-go had the chance to compound their airdrop with the vaults**.

The initial BADGER airdrop recognized key actions tied to Bitcoin on Ethereum, as well as gitcoin donors. The second airdrop (DIGG) rewarded interactions with the Badger ecosystem itself.

On top of the momentum created by the launch and initial distribution, the community was able to sustain it thanks to a blossoming spirit of meming: a distribution of NFT was organized on Meme[^2], available to the depositors in the bBADGER sett or wBTC/BADGER Uniswap sett.

A total of 6 different NFTs were available and the fist one to collect them was able to claim a neat BADGER bounty. Being a holder or farmer of these NFTs was acknowledged in the initial DIGG distribution & their inclusion to Badger as yield multiplier is being discussed.

![badger-meme-satoshi-nft](/img/2021/badger-digg/badger-nft-satoshi.gif/ "One of the 6 Badger x Meme NFTs - Satoshi")

{{< notice tip >}}
If you are very bullish on a token price short-term wise, it's usually a bad idea to enter a 50/50 liquidity providing position on it. You'll be much better off simply holding your stack and selling it. If you are worried about this scenario unfolding with Badger or DIGG, you can deposit to the BADGER or DIGG only vaults (no risk of impermanent loss).
{{< /notice >}}

---

## Are you DIGGing it yet?

DIGG is the second major step of Badger's DAO project: a new type of representation of BTC living on the Ethereum blockchain. Unlike wBTC or renBTC, DIGG is not backed by a fixed supply of BTCs. Instead, it uses the rebase mechanism initiated by Ampleforth to attempt to eventually deliver an asset keeping track of BTC's price.

Before we dive into how DIGG works, let's quickly discuss the pre and post-launch. 

### Wen DIGG?

DIGG's launch was a highly anticipated event. While from the outside it looks like it took longer than what was expected, what happened internally was fascinating: the **initial community gathered around Badger was actively involved in the key decisions surrounding DIGG.**

After discussion within the community, it was decided to go with a relatively low starting supply (4000) allowing for a **stress test from the start of the rebase mechanism**. The rebases also started from the very beginning - 24h after the launch of the token.

![wen-digg](/img/2021/badger-digg/wen-digg.jpeg/ "Wen DIGG meme contest")

Badger being Badger, the hype machine was of course on point with a "Wen DIGG?" meme contest to make sure everyone was aware. 

So without further ado, let's dive into the meat of it: the rebases.

### Rebases

DIGG is what is called an "elastic currency", as initiated by Ampleforth. What it means is that the total supply of DIGG is not set, but fluctuates daily based on the time-weighted average price of DIGG against its peg - BTC.

The more DIGG is "off from his peg", meaning its price is superior to the price of BTC, the more the DIGG supply is diluted, with the additional DIGG produced distributed proportionately to all the holders. The mechanism works exactly the same the other way around.

Just like with AMPL, with DIGG all holders (liquidity pool tokens included) are impacted by the rebase, be it positive or negative. However with DIGG, just like with the seigniorage tokens, there is a mechanism to abstract it to allow for a better composability within DeFi: that's bDIGG, we'll discuss it right after.

Rebases happen at a set time, for DIGG it's 3pm EST, that's 9 pm for my dear French readers.

{{< notice tip >}}
Rebase tokens harness mechanisms similar to the ones involved in algorithmic stablecoins / seigniorage tokens, so feel free to read my **[previous post on the topic](https://tokenbrice.xyz/content/posts/2021/seigniorage-basis-vs-esd.md)** for more information.
{{< /notice >}}

For instance, after the first day, the genesis rebase was positive and triggered a production and redistribution of about 12% of the initial supply. Several positive rebases followed and DIGG is still trading above peg.

Right now the rebase mechanism is quite straightforward but it might be better aligned with the setts incentives in the future to help DIGG maintain its peg.

### Next step for the setts

With DIGG launched, the next big step for Badger as the protocol is to start increasing its capital efficiency: to put it in simple words - to allow its users to borrow from their setts positions.

To make it clearer (while extrapolating quite a bit): picture the current Badger, with an additional function allowing you to mint DAI from your setts like you do with your vaults on Maker. Wouldn't you do it?

Indeed, setts would make for quite desirable collateral, considering they accrue in value against the base asset. So BTC setts for instance could be potentially as safe as their underlying assets, accounting for the additional layers of risks involved by the fact that the underlying asset is a Curve LP token.

However, before we see a native lending market on Badger, I expect to see different **Badger-related tokens and setts accepted as collateral** on other lending platforms.

On this front, I'd like to draw your attention to bDIGG in particular. While it represents a position made a 100% of DIGG which rebases, **bDIGG itself does not rebase**. It's like a layer of abstraction built on top of DIGG, a rebase-buffer amongst other things. It makes it easier to integrate it into other protocols, and I expect to eventually see a wide range of support for bDIGG.

---

## The endgame for BadgerDAO & DeFi in general

The endgame for Badger would be like what I described before along with a full ecosystem around the CLAW or whatever his name is.[^3] It would increasingly turn Badger into a more of a Synthetix-like service where holders are given different options of more or less active involvement in the ecosystem, with the appropriate rewards.

As services like Badger integrate money-market components such as borrowing, they **increase the capital efficiency for their users**. What used to be a representation of BTC producing 20% APY is now the same + you can borrow a share of its value in stablecoin to further increase the yield, if that suits your risk appetite.

This logic is bigger than Badger, as it's observed elsewhere too, we could call it the **"platformization of Defi**". Yearn is implementing a similar approach with the Iron Bank where some services will be able to borrow under-collateralized, generating a capital-efficiency moat for the eligible lucky ones.

Moreover, to go back to Badger, moving towards a model like this could mean native & sustained revenue feeds to potentially tie back to Badger. Considering that most of the yields currently come from liquidity mining incentives, that would be quite synergistic to grow out of it.

Considering the **[success of the Curve & CRV model](https://tokenbrice.xyz/content/posts/2021/dex-value-capture.md)**, it makes sense to see more and more protocol adopting elements of it: the gist being giving your holders the options to commit their tokens to participate in governance, tap into the platform revenue streams & boost their own returns obtained by the usage of the service.

[^1]: The graphs are coming from [Badger's DAO liquidity mining launch announcement](https://badgerdao.medium.com/badger-dao-liquidity-mining-launch-b2415301bd31#:~:text=Tokens%20distributed%3A%20%24BADGER%20and%20%24,2nd%20product%20of%20the%20DAO.).
[^2]: **[Meme](https://dontbuymeme.com/collections/badger)** is a distribution mechanism for NFT where users stake a given token (bBADGER in our case) to earn points - pineapples. They can them redeem the pineapples for the NFT of their choice.
[^3]: This is not purerly speculative as BadgerDAO is already exploring how it could [harness synergies with UMA and SushiSwap](https://twitter.com/spadaboom1/status/1354826775801561091?s=20) to achieve a similar end.

_🙏 Huge thanks to HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony for proofreading the French version of this article and translating it integrally into English._
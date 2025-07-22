---
title: "Yearn Finance's Forks: The State of the Waifus Family"
description: "On top of being one of the most succesful DeFi protocols, Yearn is also forked alot. Today, we have a look at the top YFI forks and what made them stick!"
date: '2020-09-18T01:13:50.191Z'
categories: [🌌 DeFi, 🔮 Discovery]
tags: [DeFi, Ethereum, Curve, yVault, Lending, YFI, Yearn, Yearn Finance, YFV, YFII, YFL, FARM, Harvest Finance]
---

Every day a new Yearn fork is popping up: how to keep track with them? There is no simple answer to this dilemma, however, I believe I can **provide you with some clues to help you spot YFI fork with high potential.** To do so, I’ll cover three (+1) YFI forks and try to pinpoint the changes to the secret sauce that made them stick.

![Yearn's Fork Waifus](/img/2020/yearn-waifus/cover.jpg) 

Yearn is more than Yearn.Finance product itself: it became a template to kickstart a project, sometimes called "fair launch". Yearn pioneered the method which stands on three key elements:

1. **Liquidity Mining Fair Launch**: the initial distribution of the token of the platform (ex: YFI) happens through liquidity mining. Supporters can stake tokens like yCRV to earn the governance token.
2. **Community-Driven Development**: the decisions regarding the development of the project are taken by the community of token holders, through informal and formal (on-chain) votes.
3. **Pooled Investment Strategies (Vaults)**: the Yearn-inspired projects usually also try to replicate this core feature of Yearn: they offer tokenised investment strategies. The vaults are essential for the long-term success of the project past the initial liquidity mining phase. 

{{< notice tip >}}
The term "Vault" is used to cover two vastly different reality:
1. **The "Basic Vault"**, where tokens are collected and stake to produce a yield. The yield produced is frequently settled for stablecoins (no leverage).
2. **"Delegated Vault"**, where once tokens are deposited, they are used as collateral (thanks to credit delegation) to borrow stablecoins then used to produce a return.

Delegated Vaults are much more complex to develop and implement, while basic vaults can be sprung quickly.
{{< /notice >}}

### YFI? Wifey? Wai-fu?

In the early days of Yearn, people were unclear on how to pronounce "YFI". [A discussion on the governance forum](https://gov.yearn.finance/t/make-yfi-pronounced-waifu/552) settled for "Wai-fu" (/waɪfu/). From this point onward, there was only one wai-fu but plenty of wifeys: the YFI forks.

Indeed, despite being barely a few months old, **Yearn has already been forked, a lot**. There is now a whole family of wifeys built upon similar premises, each project adjusting different parameters to attempt to better fit their envisioned use case. Many of these forks were unnecessary, however, **several managed to bring something new and exciting to the table** —  the ones we will consider today.

{{< notice note >}}
This content assumes an understanding of Yearn, to brush up on the topic I'd recommend [**my previous article on Yearn**](https://tokenbrice.xyz/content/posts/2020/yearn-finance-YFI.md).
{{< /notice >}}

### [DFI.Money (YFII)](http://dfi.money/)

One of the earliest discussion in Yearn's community was around the **emission schedule**: while it was initially planned for a week, there were discussions about extending it - most notably [YIP 8](https://yips.yearn.finance/YIPS/yip-8) which proposed a longer emission schedule halving weekly. **Despite support from the Yearn Community, the proposal did not meet the quorum and was not implemented**, which lead to the YFII fork** - a fork of YFI implementing it.

So **instead of having a week-only distribution, YFII opted for a longer schedule, still ongoing.** It started July 27 and will end on October 5. The farming pools proposed are very similar to Yearn's: staking the yCRV token or staking the Balancer pool token (98%DAI / 2 % YFII).

On top of this base differentiation, YFII develops an interesting angle with a **strong presence in Asia**: the DFI.Money website was quickly translated into Chinese and soon other languages. There is also a strong **focus on UX** to make the experience as easy as possible to onboard.

![Overview of the DFI.Money Vaults](/img/2020/yearn-waifus/dfi-money.png)

[You can view the stats here](https://stats.dfi.money/).

On September 14, [DFI.Money launched the v2 of their vaults](https://twitter.com/DfiMoney/status/1305339433638531072?s=20), supporting ETH, USDC, USDT, DAI, TUSD, BUSD, HBTC, & yCRV. As this piece was written, there was a total of $70M deposited into DFI's vaults. 

{{< notice info >}}
This article is not an exhaustive overview of YFI forks. There were other forks of Yearn with minimal changes that are not covered, such as YFFI.
{{< /notice >}}

### [YFLink (YFL)](http://yflink.io/)

YFL is another one of the early forks of YFI. Here, the twist is simple:** LINK was used as the base token of the system** - the one to deposit for the initial liquidity mining phase. The farming pools structure was similar to YFI/YFII, but with LINK/aLINK.

The initial vision was to create a farming collaborative for LINK holders. YFL was developed by 5 anonymous teams working together and initially released on August 7 2020. 

![YFL LinkSwap](/img/2020/yearn-waifus/Linkswap.png)

The growth was quick and the plan soon refined! YFLink is [now working on LINKSwap](https://medium.com/@linkswapco/yf-link-ecosystem-linkswap-development-update-44f8413721c9), a community-governed Automated Market Maker (AMM), focusing on safety and value capture for LINK holders. LINKSwap explores novel ideas to increase investors' safety - for instance, the RugLock feature, designed to avoid rug pulls - when the token’s creators drain the liquidity pools, leaving holders with a sizeable bag of worthless coins.

### [YFValue (YFV)](http://yfv.finance/)

YFValue adds several more twists, with a similar goal of providing a service facilitating yieldfarming and making it more accessible.

Here, the farming pools were mostly 98% ERC20-token / 2% YFV Balancer pools and the emission schedule is much longer (5 to 20 weeks) - it's still ongoing while [YFV launched mid-August.](https://medium.com/@yfv.finance/yfv-bringing-true-value-to-yield-farming-bddc4edf889a) There is also a "seed pool" accepting stablecoins.

YFV was one of the first project to provide credible earning opportunities on tokens such as BAL, YFI, BAT, REN, KNC, BTC, WETH, or LINK: it really helped to attract liquidity — there are around $470 M deposited on YFV as I write this.

![YFV Staking Interface](/img/2020/yearn-waifus/yfv.png)

YFV's core product, the Governance Vault was just [launched on September 15](https://medium.com/@yfv.finance/roadmap-update-value-contract-governance-vault-e226ad2f909e). YFV Holders can stake their token for several benefits:

1. Voting power in the governance
2. A return paid in vUSD and vETH
3. YFV token from the emission schedule
4. YFV tokens earned from the strategy implemented with the Governance vaults funds.
5. YFV tokens earned from buying back YFV with 6.8% of the profits made with the vaults.

YFV is a highly ambitious project. The vaults (wETH, wBTC, renBTC) are expected shortly. On top of the existing farms and governance structure, the team is working on transitioning to an AMM/farming collaborative called Value Liquid. 

{{< notice note >}}
YFValue is in the process of transitioning to VALUE (token) and Value Liquid (name of the exchange/service). You’ll find [more information on this rebranding and transition here](https://medium.com/@yfv.finance/faq-yfv-and-value-migration-af3a5a5c2190).
{{< /notice >}}

### YFInspired - [Harvest.Finance (FARM)](https://harvest.finance/)

While Harvest.Finance is technically not a fork of Yearn, one could say it's a **"fork in spirit".** Indeed, Harvest ambitions to streamline yieldfarming to make it more accessible & it's quite a success: Harvest is now home to more than $200 M (+200 M) of diverse assets farming with no stress.

The experience on Harvest is quite straightforward, just like with the Yearn's vault. **Users deposit tokens into the strategy of their choice to put them to work**. For instance, they deposit their DAI to get fDAI, DAI currently farming on Swerve.fi.

![Harvest Finance](/img/2020/yearn-waifus/harvest-finance.png)

**Once they own fDAI (or other fTokens), users can stake them to earn FARM - the native token of the platform.** They can also provide liquidity to the fDAI/DAI pair on Uniswap which facilitates the entry and exit of smaller capitals. 

Harvest.Finance launched on September 15 a new vault accepting for wETH. The community is highly active and committed, and it shows in the reactivity of the team: to better the yield, the stablecoin farms (DAI, USDC, USDT) switched from the Curve strategy to Swerve barely 16 hours after [Swerve's](https://swerve.fi/) launch.


### The YFI-Fork Secret Sauce?

I hope these quick introductions will help to better understand the recipe for a successful YFI fork. Considering the sample size (3+1), it’s hard to draw some conclusions but allow me to try.

Here’s how I see a YFI-Fork scoring some resilience points:

1. It **focuses on a clearly identified community** (ex: LINK holders for YFLINK).
2. The protocol parameters (pools, tokens, etc.) are adjusted to match the target community wants and needs
3. **A one-week emission schedule was a luxury only affordable by the first Waifu,** mother of all others (YFI). Successful YFI-forks tend to need a longer schedule (5-20 weeks) to gather and structure their community.
4. A farm by itself is not enough, there is a real need for **a convincing vision for the project in the long-run**, such as an AMM (YFL/YFV), or going above and beyond on the farming front (Harvest), and more than anything a driven and dedicated community to support it.

PS: Thanks to Ashitaka#4868 from the [Yearn Finance Discord](https://discord.gg/RheJ78p) for the amazing cover image.

### NECESSARY DISCLAIMER

{{< notice warning >}}
This is **NOT investment advice** or a recommendation to purchase any of the token mentioned above.

**I am not a financial advisor. I have no formal financial advising training, certification, nor experience.**
{{< /notice >}}

I am a DeFi native sharing my insights, do with it as you may, but please think twice and avoid impulsive decisions at all cost: they are usually the worst.

🚜 Merry Farming!
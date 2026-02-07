---
title: "Turning Locks into Leverage: How Autopilot, 40Acres & haiVELO Evolve veNFTs"
description: "The development of the veNFT infrastructure layer with Autopilot, 40Acres, and haiVELO: automation, collateral, and yield enhancement."
date: '2025-08-14T16:06:21.672Z'
categories: [Lending, Yield, DEX]
tags: [DeFi, Ethereum, Decentralized Finance, Curve Finance, veCRV, Velodrome, veVELO, Aerodrome, veAERO, 40Acres, Autopilot, haiVELO]
toc: true
url: veNFT-infrastructure
image: /img/2025/veNFT-infrastructure/cover.png
difficulty: "expert"
---

The landscape of veNFTs is rapidly evolving, ushering in a new era of decentralized finance where governance power and yield generation are tokenized. As the adoption of the veNFT model grew, **the infrastructure supporting it matured**, harnessing veNFT’s native yield to deliver novel services and automations. 

In this article I want to spotlight a few of these:  **[Autopilot](https://theautopilot.xyz/), [40Acres](https://www.40acres.finance/) & [haiVELO](https://www.letsgethai.com/)**. You can refer to my previous articles if you are not already familiar with the veNFT model:

* [ve(3,3), the logical next step after veCRV?](https://tokenbrice.xyz/solidly-velodrome-fork/)
* [Subtles nuances with great consequences: a cross analysis of Curve and Velodrome](https://tokenbrice.xyz/crv-vs-velo/)

## veNFTs took over the locks

veNFTs allow users to lock up tokens for a set period to gain voting power and boosted yields. This mechanism incentivizes long-term participation and alignment with protocol goals. The critical innovation of veNFTs is that, unlike previous lock models such as veCRV, the **locker obtains a token representing their lock: the veNFT**.

But just like with Curve/Convex locks, managing Velodrome and Aerodrome positions can prove time-consuming and complex without the appropriate tools. Users now have **tons of options**, such as using their veNFT as collateral or completely automating their management. Let’s dive in.

### Autopilot: Autonomous veAERO Position Management

Autopilot offers an autonomous solution for managing veAERO positions, enabling fully passive yet optimized veAERO holding. Users delegate their veAERO to Autopilot, which does not have any custody. It’s more like allowing a helper on your veNFTs to perform the following every week:

1. Optimized voting
2. Rebase and fees+bribes claim
3. Selling fees+bribes to USDC

![Autopilot](/img/2025/veNFT-infrastructure/autopilot.png)

Once a user deposits his veNFT, he can essentially do nothing and let the USDC accrue, to claim at his convenience. This type of service significantly **lowers the barrier to entry** for users who want to benefit from veNFTs but lack the time or expertise for active management.

The website is clear, and the UI provides a rewards and rebase breakdown for every epoch, facilitating accounting for projects or DAOs looking to harness Autopilot as well. 

### 40Acres: Self-Repaying Loans with veNFT Collateral

Beyond autonomous management, innovative financial instruments are being developed around veNFTs. [40Acres](https://www.40acres.finance/) provides a service offering** self-repaying loans collateralized by veAERO/veVELO**. This mechanism allows users to unlock liquidity from their locked veNFTs without having to sell their positions.

![40Acres](/img/2025/veNFT-infrastructure/40acres.png)

40acres has a built-in “Autopilot” as well, which manages the voting and collection of rewards on behalf of users. They can also **customize how to use their rewards**, with various percentages allocated to repayment or position growth (buying and locking more AERO). The LTV is adjusted to match a ~ 52 epoch repayment: a year to fully self-repay.

This service transforms veNFTs into more liquid assets, enabling users to **access instant capital while smartly harnessing future yield potential**.

### haiVELO: Enhancing VELO earnings

![haiVELO](/img/2025/veNFT-infrastructure/haiVELO.jpeg)

Some projects are **smartly harnessing the Drome by providing a service to veNFT holders** or liquidity providers. One of these is [HAI](http://letsgethai.com/earn), with haiVELO. For users, haiVELO provides a liquid derivative of veVELO with additional yield amplification, since it can be collateral for minting HAI. It optimizes the voting for yield, paid out in HAI.

### Relayers: OG strategies

Beyond additional infrastructure and integrations, Velodrome and Aerodrome offer, at the base level, the relays, providing **one-click access to shared voting and compounding strategies**. Most of them are centered around a given project looking to develop their liquidity, but some can also be cause-driven, like the DeFiCollective’s relays.

![Velo/Aerodrome Relays](/img/2025/veNFT-infrastructure/relay.png)

Projects can build on top of their relays, for instance, by allocating rewards to sustained depositors, but we haven’t seen much of this yet.

## Projects x Infrastructure

To illustrate how this additional infrastructure layer impacts projects involved in the ecosystem, let me discuss the Luchadores and particularly their veAERO strategy. **Two sets of veAERO** are managed to provide a balance of yield, utility, and growth. **The first, deposited into Autopilot**, provides a constant stream of stablecoins for the payment of expenses. A **second veAERO deposited into El Volador Luchador relay** supports the yields on LUCHA pools on Aerodrome, which the treasury also seeds with approximately $200k. The strategy is **fully automated** thanks to Autopilot and only requires defining the relayer voting strategy.


![Luchadores AERO Strategy](/img/2025/veNFT-infrastructure/luchadores-strategy.png)

On top of **covering two core members' salaries (~$2000/month)**, the effective management of the position provides **sustained growth levers to the project**, which enabled it to build a ~$13k reserve in ETH and stablecoins, **while sustaining $400k worth of liquidity for its token**. The project now controls a total of ~223k veAERO, at face value worth almost as much as LUCHA’s whole market cap.

The integration of veNFT into more advanced products is fascinating to witness. As they come built-in with a solid 25-30% yield while properly optimized, they offer a lot of options ranging from self-repaying loans to a fully automated stablecoin yield source. Such innovations deliver increased accessibility and capital efficiency, while fostering the growth of an ecosystem. 40Acres now has over $40M of deposits, while Autopilot manages 5.8M veAERO, approximately $8M.

## PS: Let’s not forget accounting

Before we wrap up, I'd like to share one last set of **tips and tools that could prove useful to veAERO/veVELO** **holders** regarding accounting.

It’s not the most exciting topic, but it remains essential for a sound management of positions, as my experience with the [DeFi Collective](https://deficollective.org/), where this is a key topic, taught me. The most notable tool for you to harness is a custom Dune dashboard that could easily be adjusted to your position, enabling weekly tracking and reporting on:

1. Trading fees earned (voting)
2. Bribes earned (voting)
3. AERO/VELO claimed (LP)

Find the [Velodrome/OP version here](https://dune.com/spicypiz/defi-collective-pools), and the [Aerodrome/Base version](https://dune.com/spicypiz/defi-collective-pools-base) here.

For those looking to leave no expenses behind, [0Khmer’s Gas Spent Check Dune Dashboard](https://dune.com/0xkhmer/gas-spent-checker) will also prove very handy. I’m excited to see the veNFT growing, and the new possibilities it enables for both projects and individual holders: I hope this article helped you make the most of your veNFTs.
---
title: "Chicken Bonds: an NFT-powered hatching factory to beat DeFi’s liquidity chicken and egg problem"
description: "How can a new experiment pioneering dynamic NFTs evolving based on the user's interactions help Liquity grow LUSD's liquidity and reduce the stablecoin premium?"
date: '2022-10-17T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Understanding]
tags: [DeFi, Ethereum, Decentralized Finance, Stablecoins, Stable Assets, Money Markets, Liquity, LUSD, Chicken Bonds, NFT, NFTfi]
toc: true
tocNum: true
url: lusd-chicken-bonds
image: /img/2022/lusd-chicken-bonds/lusd-chicken-bonds-cover-tokenbrice.png
---

Liquity recently released the LUSD Chicken Bonds, a **game-theory experiment merging DeFi and NFT elements to grow LUSD’s liquidity and reduce its price premium**. 

Although Chicken Bonds are building on top of existing protocols, such as Yearn, b.protocol, or Curve, it also instigates novel mechanisms, the two leading ones being:

1. **No maturity principal-protected bonding**: Chicken Bonds use a new type of bonding offering strong guarantees to the depositor, including the possibility to recoup the entire initially supplied capital at no cost (Chicken Out).
2. **Participate to Earn dynamic NFT**: While interacting with the LUSD Chicken Bonds protocol, users obtain a **dynamic NFT** that evolves depending on their choices and previous onchain interactions.

Chicken Bonds tackle one of the core challenges of DeFi, the sustainable growth of liquidity pools, first for the LUSD token only. Still, eventually, the model will be made available in a generalizable permissionless version for any protocol in need of liquidity to use.

This post explores how [LUSD Chicken Bonds](https://chickenbonds.org) work and what they achieve. However, before answering these questions, additional context is needed on LUSD: let’s get started!

## The context: LUSD price premium

One of the most misunderstood dimensions of Liquity’s model is **LUSD pegging mechanisms**. Indeed, while LUSD has strong guarantees (hard peg) than LUSD>$1.00 (redemption) and &lt;$1.10 (110% minimal collateralization ratio), in between the equilibrium is more based on a **game of incentives (soft peg)**.

In the wake of [OFAC’s crackdown on Tornado Cash](https://blog.chainalysis.com/reports/tornado-cash-sanctions-challenges/) back in August, there has been an **increased demand** for censorship-resistant stablecoins. Yet, the **appetite for leverage is low** because of the deteriorated market conditions. Thus, will the demand for LUSD is high, a significant share of its adopters purchase it at a premium on the markets instead of minting it by leveraging their ETH. 

Both factors have converged over the last few months, leading to a **sustained price premium** for LUSD, often trading in the $1.02 to $1.04 range. I won’t expand too deeply into this topic here, as it has already been covered on Liquity’s blog: **[The Premium of Resiliency](https://www.liquity.org/blog/the-premium-of-resiliency)**. However, let’s discuss **the impact of the premium on Liquity users** since it has real consequences.

![lusd-peg-incentives](/img/2022/lusd-chicken-bonds/lusd-peg-incentives.png)

### Impact of the LUSD premium

The impact of a price premium on borrowers **can be positive or negative**, depending on their timing and actions. Borrowers worried about LUSD price volatility can use Chicken Bonds, or b.protocol to preserve a pure LUSD exposure while earning yields.

{{< notice note >}}
It is worth noting that borrowers who preserve a 100% LUSD exposure do not suffer any consequence from its price fluctuations since they do not need to buy it back when repaying their debt.
{{< /notice >}}

However, having LUSD fluctuates can also benefit informed users that can arbitrage the discrepancies: 

1. **Profit margin** | The more LUSD goes over $1, the more profitable it is to take an arbitrage trade on its peg: at $1.01, shorting the peg returns $0.01 per LUSD if successful. At $1.09, the profits jump to $0.09 per LUSD.
2. **Likelihood of profits being realized** | The farther away LUSD strands from $1.00, and the closer it gets to $1.10, the more likely it is for peg arbitrageurs to outweigh LUSD buyers and thus push the price downward.

Thus arbitraging LUSD is a game of balance between maximizing profits (1) and their odds of realizing (2). To put it simply: past a certain price point, the arbitrage trade becomes **too profitable and too likely to realize for arbitrageurs to ignore**. It has helped to ensure that LUSD stayed in the lower bond of its soft peg, the $1.00-$1.05 range, even during phases of peak demand.

For users who do not monitor the situation continuously, though, it can translate into a loss of capital — for instance, if one borrows LUSD while the price is at $1.02, invest it into something else, and then weeks later try to buy back LUSD to repay its debt, only to find the price at $1.04.

Thus, LUSD’s fluctuations in the $1.00-1.10 range add **an additional layer of uncertainty for borrowers**. Growing the liquidity of LUSD and stabilizing its peg will help restore the borrowers’ confidence and streamline interactions with the protocol.

## Enter LUSD Chicken Bonds

![lusd-chicken-bonds](/img/2022/lusd-chicken-bonds/chicken-bonds.png)

To solve LUSD’s liquidity challenge, the Liquity team worked on a **brand new protocol**, first tried out with LUSD: Chicken Bonds. If successful, the model will be generalized with an LQTY instance. As a final step, the generalized model could be made ready to be harnessed by any DAO with the Chicken Bond Factory.

Last Tuesday, [the LUSD Chicken Bonds were released](https://www.chickenbonds.org/blog-posts/chicken-bonds-is-live), offering **a novel proposition merging DeFi and NFTs' elements providing optimized yield-producing opportunities to LUSD holders**. It will also fuel the growth of LUSD’s liquidity on the LUSD/3CRV Curve pool. 

There are two protagonists interacting with Chicken Bonds: 

1. **The depositors (users)** enjoy a gamified experience delivering **amplified and auto-compounded yields on LUSD**. 
2. **The deployer (protocol)** sets up an **engine enabling the sustained growth and capture of liquidity on its token** while actively engaging its holders.[^deployer]  

### So, what exactly are Chicken Bonds?

As a consequence, Chicken Bonds fulfill the function of different types of products depending on the perspective. **For users, Chicken Bonds act like an NFT-enhanced yield optimizer**. Bonding enables them to maximize their returns on LUSD by optimizing the compounding frequency and amplifying the existing yields. From their perspective, they could compare the utility of Chicken Bonds to the one already delivered by a protocol like Yearn, lacking the NFT element. It maximizes and streamlines yield-producing activities on LUSD.

From the deployer (protocol) perspective, Chicken Bonds are a **cost-effective solution to develop the available liquidity on their token**. Alternative solutions to achieve a similar goal would include liquidity mining, POL-capture solution like Olympus Pro, acquiring liquidity-driver tokens (CRV, BAL, VELO, etc.)[^liquidity-driver-tokens], or bribing liquidity-driver token owner votes. 

![chicken-egg](/img/2022/lusd-chicken-bonds/chicken-egg.png)

While each existing solution has its own tradeoffs, they all share a similar profile: they **require recurring expenses to grow and sustain liquidity**. Only the acquisition of liquidity-driver tokens can provide continuous incentives to support liquidity, but it’s also the most costly approach as it requires significant investments from projects.

On the other hand, Chicken Bonds have no cost as they harness existing yield sources: **all it needs to capture and grow liquidity is time**. They harness a novel form of **no-maturity principal-protected bonding**, offering amplified yields and strong protections for the depositors.

To explain the model of LUSD Chicken Bonds, let’s jump to the depositor perspective by looking at the lifecycle of a bond and its impact on the associated NFT.

### The story of a bond through its NFT

![3chickens](/img/2022/lusd-chicken-bonds/3chickens-static.gif "An 🥚 Egg NFT, a 🐔 Chicken In NFT and a 🐣 Chicken Out NFT")

**To create a bond, a user deposits LUSD. In exchange, he receives an 🥚 Egg NFT representing his deposit**. The NFT contains the claim on the underlying bonded LUSD and can be sold or transferred. From thereon, the user has two mutually exclusive options that will transform his NFT too: 
- 🐔 Chicken In 
- or 🐣 Chicken Out.

The Egg NFTs have four attributes: a card, egg, and background colors rolled randomly, and an egg-size scaling with the deposited LUSD amount.

When an egg is created, it starts progressively accruing bLUSD. As the bond matures, it becomes profitable for the users to claim it, forgoing their LUSD to obtain the bLUSD accumulated — It’s the “**Chicken In**” option and makes the visual of the NFT evolve accordingly: the Egg turns into a 🐔 **Proud Chicken**.

A user can recover the full invested amount at any time during the process. Still, he will renounce the bLUSD accumulated so far — it’s the “**Chicken Out**” option and also leads to an evolution of the NFT from the Egg to a 🐣 **Scared Chick**.

![3chickens](/img/2022/lusd-chicken-bonds/3chickens.gif "Preview of the possible variations")

#### Going deeper into the Chicken Bonds NFT

While Chickening In, the NFT gains additional attributes rolled at random (comb, tail, beak, and wings) and special attributes depending on the wallet onchain activities. Wallets engaged in the following activities are eligible for special attributes or boosted chances at rolling rarer ones:

1. Owning a Liquity Trove with ongoing debt,
2. Owning LQTY, or staking it either directly or with Pickle,
3. Voting for the LUSD/3CRV gauge (veCRV holders).[^ve-CRV-NFT-attribute-bribe]

The NFT collection also harnesses interesting mechanisms, such as the **affinity** to generate the coolest chickens possible; read the dedicated article on Liquity’s blog for more information on the topic:

![egg-variants-overview](/img/2022/lusd-chicken-bonds/egg-variants-overview.png "Overview of existing eggs on x2y2")

All NFTs are part of the same collection and can be traded on the usual venues, such as [LooksRare](https://looksrare.org/collections/0xa8384862219188a8f03c144953Cf21fc124029Ee/) or [X2Y2](https://x2y2.io/collection/lusd-chicken-bonds-nfts/items). Chicken Bonds is a generative NFT collection as much as a DeFi protocol: both are intrinsically tied together. The art and initial generation script were made by the NFT artist [Luchador](https://luchadores.io), creator of the eponym game. 

{{< notice info >}}
For an explainer of all the attributes and modifiers taken into account, read the article dedicated to the NFTs on the Chicken Bonds blog:<br>
**[NFT x DeFi: Deep dive into LUSD Chicken Bonds' Dynamic NFT](https://www.chickenbonds.org/blog-posts/nft-x-defi-deep-dive-into-lusd-chicken-bonds-dynamic-nft)**
{{< /notice >}}

### boostedLUSD (bLUSD): a yield-enhanced auto-compounded LUSD

By bonding and eventually Chickening In, depositors can accumulate bLUSD, but you might wonder at this point why this token can be desirable: let’s dive into the beefy DeFi side of Chicken Bonds!

![blusd](/img/2022/lusd-chicken-bonds/blusd.png)

The short story is that **owning bLUSD provides access to auto-compounded and amplified yields on LUSD**. bLUSD is a standard ERC-20 token backed by LUSD thanks to the redemption mechanism, with a rising price floor thanks to the yield amplification.

![user-flow-overview](/img/2022/lusd-chicken-bonds/user-flow-overview.png)

#### Base yield source

As a protocol, Chicken Bonds collect LUSD and deploy them into two potential yield sources:

1. **Liquity Stability Pool**, where LUSD can be deposited to earn LQTY as well as variable ETH liquidation premiums.
2. **The Curve LUSD/3CRV**, where LUSD can be supplied against USDC/USDT/DAI to earn trading fees as well as CRV tokens.

{{< notice info >}}
If you are not familiar with how Liquity works yet, you can get up to date with this dedicated article: <br>
**[⚖️ Liquity: an unstoppable, efficient and innovative borrowing service](https://tokenbrice.xyz/content/posts/2021/liquity-protocol.md)**
{{< /notice >}}

#### Auto compounded

Instead of plugging into the yield sources directly, middleware solutions are used to provide various benefits.

1. Deposits into the Liquity Stability Pool are managed using the **[B.Protocol vault](https://bprotocol.org/)**, which handles the frequent harvesting and compounding of ETH and LQTY obtained into LUSD. 
2. For the Curve Pool, the **[Yearn vault](https://yearn.finance/#/vault/0x5fA5B62c8AF877CB37031e0a3B2f34A78e3C56A6)** is used to optimize the yields obtained by harnessing Convex.

So far, so good: streamlined solutions to simple problems. Yet, the yield amplification, one of the biggest feats of the Chicken Bonds, is a bit trickier.

#### Yield Amplification

To understand how it can achieve this, we must start peeling the onion that is the internal accounting tool of the protocol: the Buckets.

There are three buckets enabling the Chicken bonds to guarantee the three core features of the protocol: the option to Chicken Out (Pending), the yield amplification (Reserve), and the growth of liquidity (Permanent).

![3buckets](/img/2022/lusd-chicken-bonds/3buckets.png "Yield source and redistribution between each bucket")

The **Pending Bucket** has a simple job: it must be able to repay investors fully if they were to Chicken Out. To ensure it’s always possible, the Pending Bucket harnesses a yield source free of impermanent loss: the Stability Pool.

When users Chicken In a bond, the corresponding LUSD balances are split between the Reserve and Permanent Bucket.

**The Reserve Bucket backs bLUSD**. With redemptions, bLUSD holders can burn their tokens to obtain a pro-rata share of the LUSD contained in the Reserve Bucket —  securing a price floor for bLUSD. Funds in reserve are also producing a yield harnessing the Stability Pool.

**Finally, the Permanent Bucket grows the liquidity of LUSD**. Thanks to its shifting function, triggerable by anyone when LUSD is overpeg, the Permanent Bucket can pull its liquidity out of the b.protocol vault to single supply the Curve LUSD/3CRV pool instead. It helps reduce the LUSD price and secures a favorable entry point in the pool since the deposit rebalances it.

The **yield produced by the Pending and Permanent buckets is redirected to the Reserve Bucket**, which creates the yield amplification and rising price floor of bLUSD.

![lusd-cb-user-timeline](/img/2022/lusd-chicken-bonds/lusd-cb-user-timeline.png "Bonder-centric timeline of LUSD Chicken Bonds")

### Bootstrap period & next steps 

LUSD Chicken Bonds have been live since Tuesday, October 4, 2022. During the first two weeks of the system, until Oct 19, it’s still in the **bootstrap period**: Chicken Ins are not possible, which means the supply of bLUSD is still 0. It means that all the LUSD are in the Pending Bucket, except the yield already produced that is being redirected to the Reserve Bucket.

Once the bootstrap period is over, the Chicken In option will be available, enabling depositors to start accessing bLUSD. To facilitate getting in and out of bLUSD, a **bLUSD liquidity pool will be incentivized on Curve Finance, using a 3% fee paid while Chickening In**. It will enable the liquidity to develop progressively as the first batch of bonds reaches their break-even point (~Oct 19) and optimal rebond time (~Nov 4).

The next section will discuss the chosen liquidity structure and its impact.

## Chicken Bonds’ impact on LUSD’s price and liquidity

If you read me up to this point, you are now in the know regarding LUSD’s price premium and the model introduced by the Chicken Bonds. Let’s connect the dots then and consider how the LUSD Chicken Bonds will **contribute to LUSD’s overall liquidity and help to contain its premium**.

Chicken Bonds have two impacts on LUSD liquidity:

1. With the growth of the Permanent Bucket, the liquidity supplied to the LUSD/3CRV will grow as long as the LUSD price still has a premium.
2. The liquidity pool structure was chosen for bLUSD to help further grow liquidity on the LUSD/3CRV.

{{< notice note >}}
In a short time frame, the release of LUSD Chicken Bonds lead to more demand for LUSD and an increase in its price. However, LUSD deposited into the Chicken Bonds proves beneficial to LUSD’s liquidity in the long run, as we highlight in this section.
{{< /notice >}}

### An engine to capture liquity over time

As deposits into the LUSD Chicken Bonds accrue, the potential impact on the LUSD peg grows. Indeed, when a user Chickens In, the underlying LUSD are distributed between the Reserve and the Permanent Bucket.

By default, all three buckets produce yield by deploying the LUSD into the b.protocol vault. However, the Permanent Bucket also features a **shifting function** triggerable by anyone as long as LUSD trades at a premium. It shifts the LUSD of the Permanent Bucket to **provide liquidity on Curve** (single asset supply), helping to progressively rebalance the pool while also growing its liquidity.

The share of the total amount of LUSD deposited into Chicken Bonds allocated to the Permanent Bucket is hard to predict, as it depends on users' behaviors. Here are some napkin maths using a conservative estimate of 10% of the total assets in the Permanent Bucket, with the 5M LUSD currently available in the LUSD/3CRV to estimate the Chicken Bonds impact:

Chicken Bonds TVL|Directly Added Liquity|Added Liquity (%)
:--|:--|:--
7M (Current)|700K LUSD|14.00%
10M|1M LUSD|20.00%
20M|2M LUSD|40.00%
50M|5M LUSD|100.00%

The added liquidity percentage could be a good proxy indicator of how much of the price premium can be reduced. Keep in mind that it remains approximative, as it only considers the LUSD/3CRV main pool.

Nonetheless, with $10M TVL into the Chicken Bonds by the end of the first cycle, the impact could already be palpable with an increase of \~20% of the LUSD amount available in the Curve pool.

{{< notice note >}}
The shifting function is disabled for the first 45 days of the system, i.e. until November 19. After this date, anyone will be able to move the Permanent Bucket liquidity from Curve <-> B.Protocol if **[conditions](https://liquity.gitbook.io/chicken-bonds/faq/lusd-peg-stability#_vowf7444yzdt)** are met.
{{< /notice >}}

### Growing bLUSD liquidity hands in hand with LUSD

There is another indirect beneficial effect of the Chicken Bonds, stemming from the chosen structure for bLUSD liquidity, incentivized by the protocol.

Indeed, a **3% Chicken In fee is collected and redirected to incentivize liquidity providers of the bLUSD/LUSD-3CRV pool**. This pool is a meta pool made of bLUSD paired with the LP token of the existing LUSD/3CRV. At perfect equilibrium, the asset exposure would be: 50% bLUSD / 25% LUSD + 25% 3pool (8.33% USDC / 8.33% USDT / 8.33% DAI).[^blusd-lusd3pool]

This liquidity structure ensures that **50% of the deposits made into the bLUSD LP pool directly contribute to growing the liquidity of the main LUSD/3CRV**. Moreover, because this pool has its own incentive budget (Chicken In fee), it will provide an attractive LUSD yield to stakers on top of the base yield generated by swaps.

As the Chicken Bonds mature, the bLUSD/LUSD-3CRV pool could get its own gauge, securing additional CRV (and potentially CVX) rewards on top of the existing ones.

This model was chosen over a bLUSD/LUSD pool which would have required a sizeable amount of LUSD without contributing to LUSD’s liquidity against other stablecoins. The main downside of the chosen model is that it makes the deposit and withdrawal interactions more complex for liquidity providers. However, this concern will be lifted with **zaps enabling the supply and withdrawal from LUSD and bLUSD directly**.

Depending on the bLUSD/LUSD-3CRV pool equilibrium, supplying it single-sided with either LUSD or bLUSD can result in a premium:
- If there is too much LUSD-3CRV in the pool, providing bLUSD rebalances the pool and results in a premium.
- If there is too much bLUSD in the pool, then supplying it with LUSD will result in a **double premium** as both the bLUSD/LUSD-3CRV and LUSD/3CRV pools are rebalanced in the process.

Learn more about the bLUSD/LUSD-3CRV in the dedicated article on the Chicken Bonds blog [**Game of Chickens!** The end of the bootstrap period and what it means for bLUSD](https://www.chickenbonds.org/blog-posts/game-of-chickens-the-end-of-the-bootstrap-period-and-what-it-means-for-blusd) 

## Additional solutions to grow LUSD’s liquidity

Chicken Bonds are the main ongoing initiatives attempting to grow LUSD’s liquidity, yet, other projects and solutions are being explored too. Here’s an overview.

### veCRV position and bribes

The Liquity treasury entered the Curve Wars months ago, acquiring and locking CRV tokens to support the bLUSD/LUSD-3CRV gauge. To maximize the impact of the LUSD Chicken Bonds, **a bribing campaign** is also synchronized with the release to increase the CRV APY of LUSD/3CRV pool depositors.

Using Warden Quest, LQTY tokens are awarded to veCRV and vlCVX voters on the LUSD/3CRV CRV gauge. The bribing campaign secured **5M veCRV votes (\~1% of total votes)**, which led to a sharp increase in the APY, bringing it to parity with a basic Stability Pool deposit. 

{{< notice info >}}
Are you out of the loop with the Curve Wars? Start here: <br>
**[⚔ CRV wars: the race to accumulate the ability to influence the Curve Finance protocol](https://tokenbrice.xyz/content/posts/2021/crv-wars.md)**
{{< /notice >}}

### PowerPool’s LUCY: interest-bearing LUSD LP position

The PowerPool team has been working on an interesting **novel type of Balancer pool** suited for LUSD, and it’s now close to being released: the LUSD-a-bb-USD pool, also known under the sweet name of **LUCY**.

Like the Chicken Bonds, this pool **harnesses b.protocol to provide an auto-compounded earning opportunity on LUSD**. Indeed, the main innovation of this pool is to involve interest-bearing assets and constantly **rebalances between yield-bearing and liquidity-providing activities**. The pool is made of two wrapper tokens:

#### 1/ Balancer Boosted Aave USD

This pool is essentially the **Balancer’s equivalent of Curve’s 3 pool**, the main stablecoin pool of the decentralized exchange. The key difference here is that the pool involves **interest-bearing wrappers** of each stablecoin. Depending on the pool’s liquidity needs, each stablecoin rebalances between liquidity-providing or yield-bearing through Aave:

![bbaUSD-pool-composition](/img/2022/lusd-chicken-bonds/bbaUSD-pool-composition.png)

#### 2/ LUSD + b.protocol

The bb-a-USD tokens are paired against LUSD, which also **rebalances yield-bearing (Stability Pool with b.protocol) and liquidity-providing** depending on the needs.

Thus, the LUCY pool should be interesting to grow LUSD’s available liquidity, as it could provide an interest yield-stacking option for liquity providers, earning:

1. The **swap fees APR**, collected on exchanges involving the pool’s tokens.
2. The **base yield** on each pool token (Aave’s yield for USDC/USDT/DAI, Stability Pool’s yields for LUSD)
3. [If a BAL gauge is obtained] the **LP token BAL staking APY**, which can be further increased with gauge votes and bribing campaigns. 

This novel pool will mark the arrival of LUSD on Balancer, diversifying its liquidity source further, as the main venues to trade LUSD are currently Curve, Uniswap, and Velodrome on Optimism.

### LUSD integrations into other lending protocols

Over the last few months, LUSD has been increasingly integrated across various DeFi protocols, providing **additional options to LUSD holders and arbitrageurs**.

The [addition of LUSD as a borrowable asset on Aave](https://app.aave.com/reserve-overview/?underlyingAsset=0x5f98805a4e8be255a32880fdec7f6728c6568ba0&marketName=proto_mainnet) marked the first time the stablecoin could be borrowed using collateral other than ETH to secure the position. As the liquidity available on the market grows, it opens LUSD arbitrage to non-ETH holders.

![lusd-aave-market](/img/2022/lusd-chicken-bonds/lusd-aave-market.png)

Meanwhile, **LUSD was also added as collateral on two €-based lending protocols**: [Angle Money](https://angle.money/) and [Mimo](https://mimo.capital/). Both enable LUSD holders to enter a short position on €, using their LUSD as collateral.

Finally, [GearBox](https://gearbox.fi/) is gearing up to release its V2 shortly, enabling users to get leverage according to a pre-determined and smart-contract-enforced set of rules. Amongst the options available at release, **liquidity providers of the LUSD/3CRV will be able to leverage their position**.

Growing the lending market of LUSD beyond Liquity grows the stablecoin utility while enabling more various types of users to arbitrage its price fluctuations. Paired with the ongoing efforts to grow LUSD’s liquidity on DEX, it will help stabilize its price.

### LUSD on Optimism: Velodrome and Stargate

LUSD also **has a strong presence on Optimism**, thanks to Liquity being one of the protocols involved in the Velodrome races. With a respectable veVELO position, Liquity has been able to grow several LUSD-related pools to sizeable TVL. Moreover, pools on Velodrome tend to be more balanced than the mainnet pools:

![lusd-velodrome](/img/2022/lusd-chicken-bonds/lusd-velodrome.png)

However, bridging LUSD to Optimism is currently a bit of a one-way trip. Bridging LUSD to Optimism is easy and only takes 5-10 min using the official bridge. However bridging back to the mainnet takes 7 days with the official bridge, and no alternative options with decent liquidity are available yet.

The situation is about to change, enabling LUSD’s strong liquidity on Optimism to positively impact the mainnet situation: Stargate, the omnichain liquidity transport protocol, recently voted to **add support for LUSD** ([SIP#16](https://snapshot.org/#/stgdao.eth/proposal/0xe6fef4aa9c8e9d162f694ab764b11c06918b9f199aafe43e0d85b12d8271011c)), which will enable its fast bridging from and to Optimism once implemented. If Stargate can provide a reliable solution to fast bridge LUSD from Optimism to mainnet, it could positively impact mainnet’s LUSD liquidity pools balance.

## Learn more about Chicken Bonds

I hope this article piqued your curiosity about Chicken Bonds and LUSD. If that’s the case, many resources are available for you to explore the model further; here are some recommendations:

1. The [Chicken Bonds website](https://www.chickenbonds.org/) is a great starting point — you’ll find [the list of the front ends](https://www.chickenbonds.org/lusd-bonds#front-ends) you can use to interact with LUSD Chicken Bonds.
2. To go deeper, feel free to [check the blog](https://www.chickenbonds.org/blog) available on the website: it features several articles deep diving into critical dimensions of the Chicken Bonds.
3. Finally, the most comprehensive resource about Chicken Bonds is [the user documentation](https://liquity.gitbook.io/chicken-bonds/faq/table-of-content), so feel free to check it if some of your questions are left unanswered.

To keep track of what is happening with the Chicken Bonds, you'll find stats in the UI of the front-end you use. Else, a community member has made a neat [Chicken Bonds Dune Analytics](https://dune.com/nemoventures/chicken-bonds) that will be helpful. For further discussion, you can [join the Liquity Discord](https://discord.gg/WQMEcgHBpc), where a brand new section is dedicated to Chicken Bonds.

[^deployer]: Right now, Liquity is the only "deployer." This concept will gain relevance with the Generalized version of the Chicken Bonds, where other protocols can harness the model to benefit their tokens.
[^liquidity-driver-tokens]: Liquidity driver tokens enable direct incentives to selected liquidity or lending pairs, usually through a locking system. They allow projects which lock them to direct emissions to pools of their choosing to attract liquidity. 
[^ve-CRV-NFT-attribute-bribe]: As far as I know, this is the first time this kind of bribery has been attempted on Curve voters (or any other DeFi token holders): NFT-attribute-based bribes; here we come!
[^blusd-lusd3pool]: The pool is [already live](https://curve.fi/factory-crypto/134) but cannot be supplied before the end of the bootstrap period.
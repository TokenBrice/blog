---
title: "🤖 Vaults: DeFi Investing Streamlined?"
description: "Vaults enable easy DeFi investments with a streamlined management of the position for the end-users. What are the options and their tradeoffs?"
date: '2020-09-30T01:13:50.191Z'
categories: [🌌 DeFi, 💸 Practical DeFi]
tags: [DeFi, Ethereum, Curve, yVault, Yearn, Yearn Finance, YFV, Uniswap, UNI, YFII, FARM, Harvest Finance]
---

As the ecosystem of decentralized financial services on Ethereum grows and matures, the service offering is becoming more dense and sometimes hard to understand. While the most technically savvy users can chase the latest releases and hedge their risk appropriately, less-seasoned investors might feel left out.

Luckily, there are DeFi services made to match the diverse set of investors exploring the space. Yearn Finance was the first platform to pioneer a passive-type of investment products: vaults. 

The base idea is simple as 1, 2, 3:

1. Vaults are **tokenized investment strategies**: your deposit is represented by a token (for instance, yCRV in Yearn’s Vault -> yyCRV/yUSD)
2. **The vault frequently harvest and re-invest the profits** (here CRV) to purchase more of the base asset supplied, compounding the returns.
3. **Fees are streamlined**: the depositors do not pay for the gas costs of the vaults operation (such as harvesting). Fees are usually charged while exiting the vault.

So if you'd like to **avoid the headaches** of chasing the latest farm, managing the claim of the profits you earn, when and how to reinvest them, without forgetting, of course, to account for the gas costs of all these operations in the calculation of your profits, vaults are a credible alternative.

<div align=""center>

![Harvest Finance GIF](/img/2020/vaults/harvest.gif)
_Harvest Finance offers several vaults to simplify farming [(gif source)](https://twitter.com/risk22_/status/1307304283415560193?s=20)_

</div>


Vaults are made to **abstract the complexity for the end-users**. You deposit some tokens and wait while they are farming a set strategy for you. So let's see what options are available.

{{< notice note >}}
This article is straight to the point and highlights the different vaults available. To learn more about Yearn Finance debuts, [**read this piece**]({{< relref path="/content/posts/2020/yearn-finance-YFI.md" >}}). For more context on Yearn’s forks, [**check this one**]({{< relref path="/content/posts/2020/yearn-waifus.md" >}}).
{{< /notice >}}

## Simplest: Basic Vaults

Vaults use the token you deposit (DAI for instance) to farm a given strategy, produce a return and re-invest it automatically.

The pioneer is of course Yearn with the yCRV vault, but several options are now available or progressively rolling out. This article provides a structured overview of the main earning opportunities enabled by vaults. 

Here, you deposit a given token to earn more of it over time, and potentially additional reward. The tokens you are supplying are not used to provide liquidity on decentralized exchanges, **so there is no exposure to impermanent losses**.

However, **as more and more vault-types products are being released, you want to take the time to understand what's happening with the one you choose**.

Below you will find tables summarizing the main vaults that I know of, with the tokens they accept, the service they farm, and how the return is denominated.

The mention "returns normalized to the base" means that the strategy generates a return frequently settled for the base token supplied - this operation is sometimes referred to as “harvesting”. 

{{< notice tip >}}
The frequency of the harvest is important as it will influence the compounding factor of the overall position, as well as level of risk taken on the price of the farmed token.
{{< /notice >}}

### Stablecoins & BTC Vaults

When it comes to Vaults, the most common tokens accepted as deposits are stablecoins. Such vaults will deploy your capital on Curve Finance pool to earn CRV tokens, usually the Y pool, . More recent projects, such as Pickle Finance also enables farming from the Curve sUSD pool.

<div align="center">

![pickle-finance-pjar0](/img/2020/vaults/pickle-pjar0.png)

_Pickle Finance pJar 0 explainer infographics [source](https://medium.com/@picklefinance/introducing-picklejars-70a311ab65c5)_
</div>

Finally, some services like Harvest or YFV have an incentive model on top of their vault: depositors earn the governance token of the platform (FARM or YFV) on top of the base return.

|  **TOKENS** | **SERVICE** | **FARMS ON** | **REWARDS** |
| :---: | :---: | :---: | :---: |
|  DAI, USDC, USDT, TUSD | Harvest.Finance | Curve | Curve returns normalized to the base + FARM |
|  USDC, USDT, DAI, TUSD, BUSD | DFI.Money | Curve | Curve returns normalized to the base |
|  DAI, USDC, USDT, TUSD | YFV (Seed Pool) | Value | YFV/VALUE staking reward |
|  yCRV, DAI, USDC, USDT, TUSD | Yearn Finance | Curve | Curve returns normalized to the base |
|  pJar 0 + psCRV pool (Curve sUSD) | Pickle Finance | Curve/Pickle | Curve returns normalized to sCRV + PICKLE |

Since Curve also supports tokenized BTC pools, there are now vaults for them too:

|  **TOKEN** | **SERVICE** | **FARMS ON** | **REWARDS** |
| :---: | :---: | :---: | :---: |
|  wBTC, renBTC & CRVRENWBTC | Harvest.Finance | Curve | Curve returns normalized to the base + FARM |
|  hBTC | DFI.Money | Curve? | Rewards normalized to the base |

{{< notice note >}}
With Harvest.Finance, you can deposit wBTC or renBTC directly, or the CRVRENWBTC token, which represents a deposit in Curve's Pool 5 (RenBTC & wBTC pool).
{{< /notice >}}

### ETH-Based Vaults

BTC & Stablecoins positions are interesting, but maybe you'd like to keep an exposure to the price ETH? 

You can achieve such a result by yourself by leveraging your ETH. You'll use them as collateral to mint or borrow stablecoins/wBTC that are then deployed to produce a return superior to your borrowing cost: here's an article I wrote providing tips and tools to leverage ETH efficiently - [**🎚 ETH exposure or DeFi yields: why choose?**]({{< relref path="/content/posts/2020/leveraging-ETH.md" >}})


However, with such a position, you can be exposed to liquidations if the price of ETH was to drop.


Once again, Yearn was the pioneer here with the release of the wETH vault that automated this whole process. However, the volume of deposit was massive and the service ran into some technical issues currently being worked on.

So instead of waiting for the re-release of Yearn's wETH vault, why not consider the **existing available options**? They are not as intricate as Yearn's wETH, since they do not leverage your ETH; the ETH is simply deposited somewhere to produce a return.

|  **SERVICE** | **FARMS ON** | **REWARDS** |
| :---: | :---: | :---: |
|  Yearn Finance | Maker + Curve | Normalized to ETH |
|  Harvest.Finance | Cream Deposit | Cream returns normalized to wETH + FARM return (fwETH staking) |
|  YFV | Soda | Soda returns normalized to wETH + VALUE |
|  DFI.Money | ? | Returns normalized to wETH |

So far, we've stuck to "simple" vaults where you deposit a given token, let it sit for a while, and hopefully walk out of there with more of it (+potentially some governance extra tokens). Yet, the release of Uniswap's UNI token, another kind of riskier vault is available.


## Riskier: Uniswap UNI-farming Vaults


### UNI farming basics

Along with the release of the UNI token came a distribution program instauring UNI incentives on specific pools:

1. ETH/USDC
2. ETH/USDT
3. ETH/DAI
4. ETH/wBTC

If you provide liquidity on any of the pools listed above, you can stake your liquidity pool token for an additional UNI income directly on Uniswap's website. You'll be earning UNI continuously. However, you'll have to manage the position yourself, which means claiming the UNI (and pay the associated gas costs), as well as selling and reinvesting them.

These strategies are riskier than ETH/BTC/Stablecoins vaults. Indeed, while farming UNI tokens you are providing liquidity on Uniswap, which comes with a risk of impermanent losses.

But why face the hassle of "manual farming" when you can **let a vault do the hard work for you**.


### UNI farming using a Vault

Indeed, quickly after the launch of Uniswap, several services started offering vault-type products to streamline the farming of UNI. Here's an overview:

|  **SERVICE** | **TOKENS** | **REWARDS** |
| :---: | :---: | :---: |
|  Harvest | ETH/USDC, ETH/DAI, ETH/USDT, ETH/wBTC | UNI returns normalized to the base + FARM |
|  Pickle Finance | ETH/DAI, ETH/USDC, ETH/USDT | UNI returns normalized to the base + PICKLE |
|  YFV | ETH/USDC, ETH/wBTC | UNI returns normalized to the base + VALUE |

{{< notice note >}}
This list is not exhaustive. Only vaults are included - services which automatically re-invest the profits for you. 
{{< /notice >}}


Other opportunities exist to farm UNI, but they require more intervention from your end. For instance, with [Sake Swap](http://sakeswap.finance/) you can stake your ETH-Stable Uni-V2 LP tokens to earn both UNI & SAKE tokens. However, you'll have to claim and manage the SAKE & UNI tokens earned yourself.

To learn more about a given vault and how they operate, feel free to check their resources. Yearn and Harvest Finance have great documentation with infographics explaining their vaults:

*   [**Learn Yearn**](https://www.learnyearn.finance/)
*   [**Farm Wiki**](https://farm.chainwiki.dev/en/home)

{{< notice warning >}}
This is not investment advice, stay sharp and do your own research.
{{< /notice >}}

Services mentioned:
- [**Yearn Finance**](https://yearn.finance/)
- [**Harvest Finance**](https://harvest.finance/)
- [**Pickle Finance**](https://pickle.finance/)
- [**DFI.Money**](https://dfi.money/)
- [**YFV**](https://yfv.finance/)

Merry Farming! 🚜
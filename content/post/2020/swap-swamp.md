---
title: "🐊 Navigating the swap swamps"
description: "Practical tips and considerations to understand what's happening under the hood while swapping tokens and how to do it efficiently."
date: '2020-11-30T01:13:50.191Z'
categories: [DeFi, Practical]
tags: [DeFi, Ethereum, Swaps, DEX, ParaSwap, Uniswap, Balancer, Curve, SushiSwap, Aave, Compound]
image: /img/2020/swap-swamps/paraswap-aave-idle.png
difficulty: "beginner"
---

Is swapping tokens easy as A, B, C? Don't let yourself be fooled by the apparent simplicity: yes, there are easy to use interfaces where you pick an input, an amount, and press a button to trade. Yet, without a basic understanding of DeFi, you might find yourself falling for avoidable mistakes.  As DeFi is increasingly made more broadly accessible, knowing **what's happening under the hood is essential to make the most of it**. 

So with this piece, I want to quickly discuss token swaps, focusing on a few tips and considerations to help you reduce the overall impact of gas costs on your trading. 

### Reading the fine print before hitting the "Swap" button!

When it comes to swapping tokens, **beware of the fine prints**! While most carefully watch the exchange rate, many other parameters also influence the output of the trade - such as the gas costs or the service used.

{{< notice note >}}
Is the pre-trade estimate reliable?
{{< /notice >}}

It's a true jungle! Some services display the worst-case scenario, while others are more optimistic. Meaning that on some services, you can sometimes beat the rate displayed, while others won't allow it. Uniswap opted for an interesting approach, with a base rate paired with a "minimum received". 

ParaSwap currently works with a worst-case scenario assumption: rate fluctuations and various optimizations can result in a pleasant surprise.

{{< notice note >}}
What about the gas cost?
{{< /notice >}}

The **gas efficiency** of the aggregator you use can significantly vary depending on the situation. There are two main types of interactions aggregators perform swaps (potentially bundled) and interactions with smart contracts, such as with Aave's to deposit USDC for aUSDC. 

The latter can have the greatest impact on gas costs if they are not correctly optimized. Properly harnessing **aggregators’ ability to wrap several interactions in one transaction** can help you reduce the impact of gas prices on their strategies.

Moreover, gas costs can be computed differently by different services. Some services can further reduce them by implementing the Gas Token. Depending on the service, the extra ETH saved can be returned to the user, or taken as a service fee.

![Debank Swap Comparator](/img/2020/swap-swamps/debank.png "Debank Swap Rate Comparator")

{{< notice note >}}
What's your plan?
{{< /notice >}}

Considering the whole situation is essential while computing gas costs. Comparing the gas costs of two transactions one to one makes little sense if one of the transactions is actually a series of operations while the other is not. 

![Paraswap-Aave-IdleFinance](/img/2020/swap-swamps/paraswap-aave-idle.png "ParaSwap can wrap a withdrawal from Idle Finance, a swap, and a deposit on Aave in a single transaction")

With that in mind, try to **think about the full context before performing a swap**, such as if you want to use the bought tokens with a DeFi service afterward.

You want to sell a token you're currently using as collateral on Aave or Compound? An aggregator can do that in one transaction. Cashing-out some profits earned on an ERC-20 token to an interest-bearing stablecoin? Still one tx.

### Going beyond the curtain

Increasing gas efficiency goes beyond the tools and services master race. It requires you to level up your understanding of them. In that spirit, I've been documenting the magic behind ParaSwap on **[ Learn2Swap, its user handbook](https://learn2swap.com/l2s/)**.

With technical developments and new DEXes frequently launching, the swapping situation evolves pretty much daily. So to help you keep track, we **[maintain a changelog](https://learn2swap.com/l2s/links-and-resources/changelog-2020)** giving you a comprehensive summary of the additions and improvements to the service. Each update can have a significant impact:

![paraswap-october2020-changelog](/img/2020/swap-swamps/paraswap-october2020-changelog.png "October was a busy month for ParaSwap!")

For instance, [one of the latest updates](https://twitter.com/paraswap/status/1321417337703223304?s=20) improved the computation of gas costs while routing the trades through several decentralized exchanges. It prevents ParaSwap from "over-optimizing" smaller trades, without requiring the user to choose between achieving the best rate or optimizing for gas efficiency.

So here are three **key takeaways for efficient swaps**:

{{< notice tip >}}
1. Compare the rates using a tool like **[Debank](https://debank.com/swap)**, but don't trust it blindly - feel free to double-check.
2. Keep in mind your whole situation: what you intend to do with the tokens before and after.
3. Make sure you're in the know regarding the revenue model of the services you're using. You can read **[the details on ParaSwap's situation here.](https://app.gitbook.com/@paraswap-network/s/l2s/understanding-paraswap/fees)**
{{< /notice >}}

So next time you swap, consider your options! You can access **[ParaSwap](https://paraswap.io/)** directly through the website, with your phone through your Argent or Monolith wallets, and now even with MetaMask and Ledger Live which aggregates ParaSwap amongst other sources.
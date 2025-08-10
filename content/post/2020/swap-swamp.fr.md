---
title: "🐊 Immersion dans la mare aux swaps"
description: "Des conseils et astuces pour comprendre ce qu'il se passe sous le capot avec les aggrégateurs d'échanges décentralisés et comment les utiliser au mieux."
date: '2020-11-30T01:13:50.191Z'
categories: [DeFi, Pratique]
tags: [DeFi, Ethereum, Swaps, Token Exchange, Swapping Tokens, ParaSwap, Uniswap, Balancer, Curve, SushiSwap, Aave, Compound]
image: /img/2020/swap-swamps/paraswap-aave-idle.png
---

L'échange de tokens est-il aussi facile que ça ? Ne vous laissez pas tromper par l'apparente simplicité : oui, il existe des interfaces accessibles où vous choisissez un token, un montant, et appuyez sur un bouton pour échanger. Mais sans une compréhension de base de la DeFi, vous risquez de faire des erreurs évitables.  Il devient de plus en plus critique de savoir **ce qui se passe sous le capot pour en tirer parti**. 

C'est pourquoi, dans cet article, je souhaite discuter rapidement des échanges de tokens, en mettant l'accent sur quelques conseils et considérations qui vous aideront à réduire l'impact global des coûts du gaz sur vos échanges. 

### Le diable est dans les détails

Lorsqu'il s'agit d'échanger des tokens, **vérifiez les détails** ! Si la plupart des gens surveillent attentivement le taux de change, de nombreux autres paramètres influencent également le rendement de l'échange - comme les coûts du gaz ou le service utilisé.

{{< notice note >}}
L'estimation est-elle fiable ?
{{< /notice >}}

C'est une véritable jungle ! Certains services assument le pire scénario, tandis que d'autres sont plus optimistes. Cela signifie que sur certains services, vous pouvez parfois battre le taux affiché, alors que d'autres ne le permettent pas. Uniswap a opté pour une approche intéressante, avec un tarif de base couplé à un "minimum reçu". 

ParaSwap fonctionne actuellement sur la base d'une hypothèse du pire scénario : les fluctuations de taux et les diverses optimisations peuvent entraîner une agréable surprise.

{{< notice note >}}
Qu'en est-il du coût en gaz ?
{{< /notice >}}

Le **rendement du gaz** de l'agrégateur que vous utilisez peut varier considérablement selon la situation. Il y a deux principaux types d'interactions : les agrégateurs effectuent des échanges (potentiellement groupés) et les interactions avec des contrats intelligents, comme avec Aave pour déposer des USDC pour aUSDC. 

Ces dernières peuvent avoir un impact maximal sur les coûts du gaz si elles ne sont pas correctement optimisées. Exploiter correctement la capacité des **agrégateurs à regrouper plusieurs interactions en une seule transaction** peut vous aider à réduire l'impact des prix du gaz sur leurs stratégies.

De plus, les coûts du gaz peuvent être calculés différemment selon les services. Certains services peuvent les réduire davantage en mettant en œuvre le Gas Token. Selon le service, le surplus d'ETH économisé peut être restitué à l'utilisateur, ou pris comme frais de service.

![Comparateur de taux de swap Debank](/img/2020/swap-swamps/debank.png "Comparateur de taux de swap Debank")

{{< notice note >}}
Quel est votre plan ?
{{< /notice >}}

Il est essentiel de considérer l'ensemble de la situation tout en calculant les coûts du gaz. Comparer les coûts du gaz de deux transactions une à une n'a guère de sens si l'une des transactions est en fait une série d'opérations alors que l'autre ne l'est pas. 

![Paraswap-Aave-IdleFinance](/img/2020/swap-swamps/paraswap-aave-idle.png "ParaSwap peut regrouper un retrait de Idle Finance, un swap et un dépôt sur Aave en une seule transaction")

En gardant cela à l'esprit, essayez de **réfléchir à l'ensemble du contexte avant d'effectuer un échange**, par exemple si vous voulez utiliser les jetons achetés avec un service DeFi par la suite.

Vous voulez vendre un token que vous utilisez actuellement comme collatéral sur Aave ou Compound ? Un agrégateur peut le faire en une seule transaction. Vous voulez encaisser les bénéfices réalisés sur un jeton ERC-20 dans un stablecoin produisant un retour ? Encore une seule transaction.

### Aller de l'autre côté du rideau

L'amélioration de l'efficacité du gaz va au-delà de la course aux outils et aux services. Il vous faut également les comprendre. Dans cet esprit, j'ai documenté la magie de ParaSwap sur **[Learn2Swap, son manuel d'utilisation](https://learn2swap.com/l2s/)**.

Avec les développements techniques et le lancement fréquent de nouveaux DEX, la situation de l'échange évolue presque quotidiennement. Pour vous aider à suivre l'évolution de la situation, nous **[maintenons un journal des modifications](https://learn2swap.com/l2s/links-and-resources/changelog-2020)** qui vous donne un résumé complet des ajouts et des améliorations apportés au service. Chaque mise à jour peut avoir un impact important :

![paraswap-october2020-changelog](/img/2020/swap-swamps/paraswap-october2020-changelog.png "Octobre a été un mois chargé pour ParaSwap !")

Par exemple, [une des dernières mises à jour](https://twitter.com/paraswap/status/1321417337703223304?s=20) a amélioré le calcul des coûts en gaz lorsque l'éxchange est acheminé sur plusieurs DEX. Cela permet à ParaSwap d'éviter  de "sur-optimiser" les petits échanges, sans que l'utilisateur ait activement à choisir entre obtenir le meilleur tarif ou optimiser l'efficacité du gaz.

Voici donc trois **principaux points à retenir pour des échanges efficaces** :

{{< notice tip  >}}
1. Comparez les taux en utilisant un outil comme **[Debank](https://debank.com/swap)**, mais ne vous y fiez pas aveuglément - n'hésitez pas à revérifier.
2. Gardez à l'esprit l'ensemble de votre situation : ce que vous comptez faire avec les jetons avant et après.
3. Assurez-vous que vous êtes au courant du modèle de revenus des services que vous utilisez. Vous pouvez lire **[les détails sur la situation de ParaSwap ici](https://app.gitbook.com/@paraswap-network/s/l2s/understanding-paraswap/fees)**
{{< /notice >}}

Alors la prochaine fois que vous échangez, réfléchissez à vos options ! Vous pouvez accéder à **[ParaSwap](https://paraswap.io/)** directement par le site web, avec votre téléphone par le biais de vos portefeuilles Argent ou Monolith, et maintenant même avec MetaMask et Ledger Live qui agrége ParaSwap parmi d'autres sources.

{{< notice info  >}}
Pour approfondir votre compréhension, n'hésitez pas également à lire la **[Tactique du Mardi récemment publiée sur BanklessFR](https://banklessfr.substack.com/p/-la-pratique-du-mardi-comment-changer)**, qui détaille quelques situations tirant profit des optimisations offertes par ParaSwap.
{{< /notice >}}
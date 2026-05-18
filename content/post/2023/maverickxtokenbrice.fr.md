---
title: "Annonce : TokenBrice 🤝 Maverick"
description: "Je supporte l'équipe Maverick en conseillant la stratégie de croissance, la tokénomique"
date: '2023-04-21T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Projects, DEX]
tags: [DeFi, Ethereum, Maverick, DEX, Liquidity Management, Liquidity Shaping, Concentrated Liquidity]
toc: false
tocNum: false
url: maverick-x-tokenbrice
image: img/2023/maverickxtokenbrice/maverick-x-tokenbrice-cover.png
difficulty: "intermediate"
---

Ce billet est plus une annonce personnelle : je voulais vous faire savoir ce que je fais et ce qui se passe avec Maverick. Alors ne tournons pas autour du pot : je suis ravi d'annoncer que **je soutiens l'équipe de Maverick en tant que conseiller, en aidant à la stratégie de croissance, à la tokenomics, et au développement des affaires**.

### Storytime

Tout comme moi, vous devez être saturé de DEX. Si vous suivez DeFi de près, vous avez vu plusieurs de ces lancements par jour. Pourtant, la plupart d'entre eux adoptent toujours les structures de liquidité fondamentales : x\*y=k pour les paires volatiles et le stableswap, et se concentrent plutôt sur l'innovation en matière de tokenomics : les désormais célèbres DEX ve(3,3).

**Cela faisait un moment que je cherchais un DEX qui innoverait à un niveau plus profond**, alors en mai de l'année dernière, lorsque Bob m'a contacté pour me parler de Maverick, j'étais tout ouïe. J'ai rapidement réalisé que Maverick pouvait redéfinir la façon dont nous envisageons la liquidité dans DeFi et contribuer à améliorer son efficacité. Je suis donc heureux d'annoncer ma participation aujourd'hui : Maverick est déjà en ligne, se développe rapidement et est prêt à connaître une croissance encore plus exponentielle.

Mais avant de nous plonger dans ce qui rend Maverick si intéressant, nous devons prendre un peu de recul et considérer le contexte plus large de la liquidité dans DeFi :


### La structuration de la liquidité en profondeur

**Au début, il y avait Uniswap**, et sa facilité d'utilisation pour les fournisseurs de liquidité a conduit les gens à penser qu'il s'agissait d'une activité triviale. Pourtant, toute activité d'apport de liquidité sur un DEX implique deux décisions :

1. Choisir une paire (ou plus) de jetons (ex : ETH/USDC)
2. **<span style="text-decoration:underline;">Formuler des hypothèses de prix concernant l'un ou les deux jetons (🐂, 🐻, ou 🦀).</span>**

La deuxième décision est **souvent implicite**, comme avec UniswapV2, où vous n'avez pas d'option mais un seul choix : 50/50, ce qui signifie que votre scénario optimal est que les deux tokens évoluent latéralement en termes de prix avec un volume d'échange important.

Lorsque l'Uniswap V3 est apparu, la deuxième hypothèse est devenue soudainement plus explicite pour les utilisateurs de DeFi grâce à la concentration de la liquidité. Cependant, la V3 a ajouté de la complexité à l'expérience des fournisseurs de liquidité et à la gestion active. Elle **s'adresse principalement aux utilisateurs puissants qui peuvent se permettre des rééquilibrages fréquents**, ou **qui ont besoin d'outils externes** pour être exploités efficacement par les LPs, le gestionnaire de liquidité - Arrakis, Bunni, etc.


### Qu'est-ce que Maverick a d'unique ?

En termes simples, Maverick est le descendant spirituel d'UniV3 et de CurveV2. Il offre une flexibilité infinie dans la conception de la position d'apport de liquidité, similaire à Uniswap V3, mais avec une exécution rationalisée et autonome, tout comme sur Curve. En effet, les LPs sur Maverick peuvent décider de redistribuer leurs liquidités pour suivre le prix dans une ou deux directions. **Si nécessaire, le rééquilibrage est effectué au niveau du DEX, ce qui garantit l'efficacité du gaz.** Maverick prend également en charge les "pools statiques" (range).

**Cette caractéristique fait de Maverick un outil fantastique pour les actifs ancrés, en particulier ceux qui ne sont pas continuellement négociés précisément à l'ancrage** et qui sont donc mal desservis par les structures de liquidité habituelles, telles que la paire LUSD/USDC :

* Curve stableswap, qui optimise la liquidité pour un prix de 1:1, n'est pas idéal lorsque le LUSD est au dessus du peg.
* Uniswap v3, où les LPs finissent généralement par être super concentrés autour du prix actuel du marché, ce qui est efficace, mais les met rapidement hors de portée lorsque le prix évolue.

![mav-mode-both](img/2023/maverickxtokenbrice/mav-both.gif "Maverick mode both, où la liquidité suit le prix à gauche et à droite")

Sur Maverick, une telle paire peut être exploitée de manière optimale par chaque LP, en fonction de son objectif réel. **Cela permet à chaque investisseur de créer une position qui s'ajuste automatiquement et qui met en œuvre une stratégie correspondant à ses hypothèses et à ses besoins**. Voici quelques exemples d'objectifs &lt;-> d'appariement de la structure de liquidité :

* 🎚️ | Vous recherchez un rendement sûr avec un risque minimal ? Un LP statique peut être préférable, car les résultats sont prévisibles.
* 🐂/🐻 | Penser que le LUSD est actuellement sur/sous-évalué : vous pouvez fournir de la liquidité directionnelle et gagner un supplément si votre hypothèse se vérifie.
* 🦀 | Vous voulez parier sur le volume avec des prix qui vont de côté ? Vous pouvez simplement concentrer votre liquidité sur quelques bacs autour du prix et activer le **mode gauche-droite** pour rééquilibrer constamment le prix actuel, maximisant ainsi la liquidité disponible et les frais perçus, mais aussi la perte potentielle impermanente.

Jusqu'à présent, Maverick a trouvé **une adéquation produit/marché exceptionnelle sur des pools telles que wstETH/ETH**, avec un taux d'utilisation quotidien moyen de plus de 100 %. Voici par exemple ce qui s'est passé aujourd'hui (20/4) :

* Curve : TVL = $1.5B, Volume =$34M, Utilisation = 2,26%
* Maverick : TVL = $10.6M, Volume =$10.45M, **Utilisation = 98,5%**

![Maverick Top Pools](img/2023/maverickxtokenbrice/mav-pools.png "Top pools sur Maverick aujourd'hui (4/20/23)")

### Que se passe-t-il ensuite ?

Lancé il y a seulement quelques semaines sur le mainnet Ethereum, Maverick enregistre déjà un volume impressionnant et un taux d'utilisation de la liquidité sans précédent, en particulier sur les paires d'actifs ancrés.

Maverick a également été lancé sur zkSync, son premier L2, il y a quelques jours. Au fur et à mesure que d'autres projets DeFi OG y déploieront leurs services, Maverick aura de nombreuses occasions de démontrer l'efficacité supérieure que ses modèles de liquidité peuvent offrir aux LPs.

Je suis très enthousiaste à l'idée des prochaines étapes : en tant que stratège DeFi chez Liquity, la sortie de Maverick m'a fait l'effet d'un Noël anticipé ; je pense que ce n'est qu'un début !

Je contribuerai à Maverick en tant que conseiller, ce qui signifie que mon objectif principal reste mon engagement envers les protocoles immuables, en particulier Liquity, en les aidant à se développer par le biais de diverses activités onchain et offchain. Je suis convaincu que Maverick s'avérera rapidement un outil décisif pour atteindre cet objectif.

Vous entendez parler de Maverick pour la première fois et voulez en savoir d'avantage ? **[Consultez-le site](https://mav.xyz/)** ou rejoignez [le serveur Discord](https://discord.gg/mavprotocol).

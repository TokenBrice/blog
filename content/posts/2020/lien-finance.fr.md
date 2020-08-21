---
title: "Lien Finance & la quête d'un stablecoin 'trustless'"
description: "Lien Finance est un système innovant qui dans un premier temps propose un stablecoin crédiblement sans intermédiaire de confiance. Le système est élégant et évite les deux pièges classiques : la sur-collatéralisation et l'excès de gouvernance (avec l'inertie que ça implique). **On ne parlera pas de l'équipe, elle est anonyme.**"
date: '2020-08-21T01:13:50.191Z'
categories: [🌌 DeFi, 🔮 Découverte]
tags: [DeFi, Ethereum, Prêts, Stablecoins, USDC, USDT, DAI, LIEN, iDOL]
---

![Lien Finance](/img/2020/lien-finance/cover.png)

Les stablecoins sont la monnaie de base de la DeFi - on pourrait même dire qu'ils ont été essentiels au démarrage de la scène - en effet, la volatilité rend la plupart des scénarios de prêt/emprunt intimidants, voire impossibles.

Heureusement pour nous, **l'offre de "stablecoin" s'est considérablement développée ces dernières années**. En plus des habituels DAI et USDT, nous avons vu l'USDC et le sUSD être de plus en plus adoptés dans la DeFi. L'USDC a de nombreux atouts - notamment un ancrage (peg) bien maintenu et une excellente liquidité. 

Toutefois, **comme pour l'USDT, un solde d'USDC peut être saisi ou gelé à tout moment** - à la seule discrétion du Circle (émetteur). Comme l'USDC est de plus en plus utilisé comme collatéral dans la DeFi, ce point soulève des inquiétudes sérieuses. 

Par exemple, via Maker il est désormais possible de déposer vos USDC en contrepartie (collatéral) pour générer des DAI. Bien. Mais que se passe t-il si les USDCs sont saisis parce qu'ils ont été impliqués dans un piratage par exemple ? Pour l'instant, c'est un territoire inexploré.


## Pourquoi les stablecoins 'trustless' sont nécessaires ?

**Les stablecoins sont des objets bidimensionnels : ils évoluent dans une dimension économique mais également relationnelle (confiance).**

Sur le plan économique, vous avez des questions telles que :

1. Est-ce que le stablecoion maintient vraiment son peg (1 stablecoin = 1 dollar autant que possible) ?
2. La liquidité du système est-elle suffisante même pour couvrir des besoins importants ?

**La dimension économique est généralement suffisante pour la plupart des utilisateurs, car ils ne détiendront pas les stablecoins à long terme ou ne les utiliseront pas comme collatéral**. Néanmoins, pour une utilisation fiable dans la finance décentralisée, un projet de stablecoin doit également comprendre la dimension de confiance :


* Le système peut-il être arrêté par une autorité centrale ou une tierce partie ?
* Qui le contrôle ?
* Le solde des stablecoins peut-il être gelé/saisi ?
* Il y a t-il d'autres paramètres du système qui pourraient être modifiés entraînant ainsi une perte pour les investisseurs?

Si le **USDT et l'USDC sont un succès économique évident, leur modèle les exclut instantanément de la prétention à être 'trustless'**. Donc, si nous excluons les stablecoins qui peuvent être saisis ou gelés, il nous reste essentiellement le DAI ou le sUSD.

Pour mieux comprendre les différents modèles de confiance et comprendre pourquoi la dimension trustless est critique, je vous invite à lire l'article BanklessFR qui propose une **[taxonomie pour la bande passante économique](https://banklessfr.substack.com/p/une-exprience-de-pense-qui-amne-leth)**.

### Choisissez en un : la confiance ou la viabilité économique ?

**Actuellement, nous n'avons pas de stablecoins qui fassent les deux.** Le DAI était auparavant raisonnablement trustless, mais fonctionnant à un faible volume. Plusieurs décisions ont été prises pour massifier le volume au détriment de la confiance : Maker accepte maintenant des garanties qui peuvent être saisies, comme le wBTC, l'USDC, et bientôt des actifs du monde réel.

Ce que nous avons tendance à observer, c'est que l'absence de confiance entrave généralement l'efficacité économique, laissez-moi vous expliquer. Prenez le premier modèle Maker, par exemple, qui vous permet de battre le DAI depuis l'ETH. En raison de la conception du système, vous pouvez à un grand maximum battre ⅔ de la valeur de l'ETH en DAI. 

La réalité observée est beaucoup plus faible, car le fait de battre ⅔ vous expose à des risques de liquidation. Nous appelons ce modèle "sur-collatéralisation", car il y a - à tout moment - plus de garanties (en valeur) que de dettes générées. **Alors que la sur-collatéralisation a permis à Maker de proposer un stablecoin qui peut être battu directement de l'ETH, c'est maintenant l'un des principaux facteurs qui entravent la mise à l'échelle de la plate-forme.**

Heureusement, depuis le lancement de Maker, l'industrie a évolué de manière spectaculaire. Et depuis le début de l'année, nous voyons à nouveau des projets qui tentent de fournir le stablecoin dont nous avons cruellement besoin : à la fois sans confiance et économiquement viable. Je connais deux projets qui explorent cette voie de manière crédible :



1. [Reflexer](https://medium.com/reflexer-labs/stability-without-pegs-8c6a1cbc7fbd) - techniquement, ce n'est pas un stablecoin mais il fournira une proposition de valeur similaire en utilisant des liens réflexes.
2. [Lien.Finance](http://lien.finance/), notre thème central pour le reste de cet article. Comme Reflexer, Lien utilise un niveau d'abstraction au-dessus de l'ETH qui est divisé en deux actifs synthétiques distincts lorsqu'il est déposé, comme nous le verrons plus loin.

J'ai exploré Reflexer, mais je ne le connais pas encore assez bien. Cliquez sur le lien ci-dessus pour en savoir plus ; le reste de cet article portera sur Lien.Finance car j'en sais plus à ce sujet.


## Lien : Le chaînon manquant entre la confiance et la viabilité économique ?

Compte tenu de notre sujet aujourd'hui, n'attendez pas un système simple et direct. En effet, l'objectif étant de fournir des stablecoins raisonnablement sans confiance et sans sur-collatéralisation, les voies simples et directes ne fonctionnent plus.

{{< notice info >}}
Lien Finance propose une solution complète pour créer des contrats d'actifs dérivés. Pour garder cet article le plus clair possible, la suite se concentre sur iDOL, un stablecoin décentralisé construit sur le protocole Lien.
{{< /notice >}}

Une autre dimensions clé de Lien est qualifiée sous le parapluie de **"gouvernance minimisée "**. Bien qu'elle soit exacte, ce n'est pas la plus explicite. Ce que l'on entend par là, c'est qu'iDOL (le stablecoin produit par le système Lien) est **effectivement émis et géré par un contrat intelligent s'ajustant aux conditions du marché** : ou pour le dire en termes plus simples, "la banque centrale de Lien" est un contrat intelligent.

Cela signifie que les paramètres clés régissant le système ne sont pas décidés par des humains ou par un DAO comme c'est le cas sur Maker (comme le frais de stabilité) - il s'agit d'un ajustement en fonction des conditions du marché.

Comment Lien.Finance s'y prend-il ? Nous allons faire un tour d'horizon :


### Lien Finance : Aperçu de l'infrastructure

Le graphique ci-dessous est assez complet, c'est donc un bon point de départ. Pas de stress si vous n'avez pas encore tout compris à qu'il se passe, nous allons suivre pas à pas cette illustration :


![Flux d'Ether, SBT, et LBT dans le système iDOL/Lien](/img/2020/lien-finance/eth-flow.png "Flux d'Ether, SBT, et LBT dans le système iDOL/Lien")


Avant de me lancer, permettez-moi de vous rappeler une chose : **Vous n'avez pas besoin d'interagir avec l'ensemble du système décrit ci-dessous si vous voulez juste interagir avec iDOL, le stablecoin**.  Tout comme DAI et d'autres, vous pourrez les obtenir par d'autres moyens également.


### Diviser l'ETH : SBT+LBT

L'une des principales promesses de Lien est de fournir un stablecoin qui ne repose pas sur une sur-collatéralisation. **De ce fait, l'ETH elle-même ne convient pas comme garantie** - en effet, la volatilité des prix est trop élevée pour atteindre les résultats escomptés.

Pourtant, il n'y a pas d'actif plus "monétaire" que l'ETH sur Ethereum, alors comment le Lien s'en sort-il ? La clé réside dans les actifs dérivés. Au lieu d'utiliser l'ETH lui-même comme unité de base du système, comme le fait Maker, **Lien ajoute une autre couche d'abstraction en divisant l'ETH entrant dans le système en 2 actifs dérivés : LBT & SBT**.

Commençons par le point commun : ces deux tokens sont des obligations (bonds) - ils sont très différents de vos tokens ERC-20 habituels car ils ont une **date d'échéance**. Ces nouveaux types d'actifs ont conduit Lien à développer également [FairSwap](https://lien.finance/White_paper.html#white_2), un DEX optimisé pour l'échange de tokens obligataires.

![The decomposition of ETH into SBT and LBT](/img/2020/lien-finance/eth-sbt-lbt.png "Décomposition de l'ETH en LBT et SBT")

Pour ce qui est des différences, c'est essentiellement la lumière et le jour :


* **🧱 Le roc qui est difficile à déplacer : le SBT**. Le Solid Bond Token ressemble plus à une obligation ordinaire. Le SBT est stable par rapport à l'USD et verse une valeur fixe à son détenteur à l'échéance, avec une très forte probabilité.
* **🎈 La plume portée par le vent : LBT**. Le Liquid Bond Token est un dérivé qui réunit en un seul produit la volatilité de ~2ETH. C'est un moyen très efficace de parier sur le prix de l'ETH, mais c'est aussi un jeu difficile, car vous êtes surexposé à la baisse du marché.

Ne vous laissez pas effrayer par cette division, le système est en fait assez élégant et facile à suivre une fois que vous l'avez compris.

Ainsi, lorsque les ETH entrent dans le système, il est divisé entre un dérivé très volatil (LBT) et un autre plus stable (SBT). Vous pouvez vous représenter le LBT comme une manière "d'externaliser la volatalité". **Nous allons nous concentrer sur les SBT pour l'instant, puisqu'ils sont les dérivés qui soutiennent l'iDOL des stablecoins.** 

### De SBT à iDOL

Le SBT en lui-même est déjà à peu près stable, le principal joker étant la date d'échéance : plus la date d'expériation du SBT est proche, plus il est sûr. À partir de là, les investisseurs avertis à la recherche d'actifs stables pourraient déjà composer leur propre panier de SBT avec différentes dates d'échéance pour couvrir leurs risques.

Mais pourquoi les laisser faire le travail, alors qu'un contrat intelligent pourrait le faire mieux et de manière plus sûre ? C'est là qu'entrent en jeu les contrats iDOL représentés dans le coin supérieur droit du graphique précédent. Le contrat **iDOL est essentiellement un panier roulant de SBT avec diverses dates d'échéance.**

En fonction des conditions du marché - et notamment de la volatilité observée de l'ETH, le contrat iDOL ajuste ses préférences en matière de risque :

* Si la volatilité des prix est faible, le contrat iDOL pourra accepter un plus grand nombre de SBT plus éloignés de leur date d'échéance.
* En période de volatilité croissante, le contrat iDOL recentrera l'exposition sur les SBT approchant leur date d'échéance (-> moins de risque).

Et c'est précisément ce qui m'a convaincu - l'ensemble du système est agile et s'adapte au marché - et pas seulement au prix de l'ETH lui-même. **Le principal moteur de la décision sur les paramètres de risque dans le système de Lien est la volatilité de l'ETH.**

Pour moi, cela a tellement de sens !  En effet, considérer la volatilité aussi bien que le prix, c'est comme observer l'accélération d'une voiture au lieu de se contenter de sa simple vitesse :



* La vitesse vous donne un absolu instantané : la voiture roule à X Mph.
* L'accélération peint une tendance : Toutes choses gardées comme telles, la voiture ira à X dans un temps Y.

Il y a encore beaucoup de choses à dire sur le Lien, mais il s'agit d'un article d'introduction, alors soyons bref. Avant de vous laisser partir, explicitons une dernière dimension du Lien : l'aspect "gouvernance minimisée". Comme nous l'avons vu plus haut, les ajustements quotidiens des paramètres avec Lien se font de manière programmatique, en s'adaptant aux marchés. 

C'est une innovation sensée en soi si vous considérez par exemple le système Maker où même les paramètres de base comme la commission de stabilité (frais payés pour emprunter) sont décidés par le système de vote. 


## Pour en savoir plus sur Lien Finance

Ai-je éveillé votre curiosité sur Lien.Finance ? Vous pouvez en apprendre davantage sur le projet en regardant cette discussion (en Anglais) sur les stablecoins à laquelle j'ai participé **[#mDeFi 5 - La prochaine génération de stablecoins](https://www.youtube.com/watch?v=jPrwinPvwv4)**. Il s'agit d'un panel de 2h où je présente Lien Finance, aux côtés de James ([mStable](http://mstable.org/)), Michael Egorov ([Curve.Fi](https://www.curve.fi/)) & modéré par mon ami Abel ([AbelAbstracts](https://abelsabstracts.substack.com/)).

Enfin, **[pour suivre l'aventure Lien Finance en première ligne vous pouvez rejoindre le serveur 🎮 Discord communautaire.](https://discord.gg/stCABfA)**
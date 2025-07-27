---
title: "Tokens directeurs de liquidité au-delà de Curve : analyse des Balancer Wars"
description: "Nous examinons les particularités de l'échange décentralisé Balancer ainsi que de son écosystème pour mieux comprendre la dynamique de la course aux BAL."
date: '2022-11-24T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Comprendre]
tags: [DeFi, Ethereum, Finance Décentralisée, Balancer Finance, BAL, Polygon, Aura Finance, AURA, PowerPool, CVP, veBAL, vlAURA, Hidden Hand, Warden, Vote Bribing, Liquidity Driver Tokens]
toc: true
tocNum: false
url: balancer-wars
image: /img/2022/balancer-wars/balancer-wars-cover.png
---

Les tokens directeurs de liquidité, comme je les appelle, sont une construction émergente et fascinante. En termes simples, ces tokens vous permettent de diriger des incitations (CRV, BAL, etc.) vers la pool de liquidité de votre choix. Pour ce faire, vous devez généralement posséder et verrouiller le token correspondant (veCRV, veBAL, etc.) au sein de leur contrat de gouvernance, ce qui garantit un engagement continu des projets participants.

Ainsi, les tokens directeurs de liquidité sont rapidement devenus très recherchés par les DAO dont les besoins en liquidité sont constants et généralement croissants. Cela a conduit à ce que nous appelons des « courses » ou « guerres »: un terme qui fait référence aux diverses stratégies que les projets exploitent pour augmenter constamment leur réserve de veTokens, idéalement plus rapidement que les autres participants, afin de développer un avantage concurrentiel.


J'ai largement couvert la tokenomique CRV, le pionnier du modèle ve, et leurs conséquences dans ce blog :

1. [⚔ CRV wars : comprendre la course à l'accumulation de pouvoir pour influencer le protocole Curve Finance](https://tokenbrice.xyz/content/posts/2021/crv-wars.fr.md)
2. [⚔ Guerres CRV avancées : analyse des protocoles construits au dessus de Curve et Convex](https://tokenbrice.xyz/content/posts/2022/crv-wars-l2.fr.md)

## Les veTokenomiques, au-delà de l'écosystème Curve

Si Curve est fascinant à étudier, c'est qu'il s'agit du pionnier du modèle ve et de l'implémentation la plus mature et la plus dense de la tokenomique ve à ce jour, il existe désormais de nombreuses autres instances de course avec leurs variantes qui méritent d'être étudiées.

En effet, la tokenomique veCRV a plus de deux ans, et de nombreux autres projets ont lancé ou remanié leur tokenomique depuis, en s'inspirant du modèle de Curve. Sans être exhaustif, voici les autres "courses" que je suis de plus près :

1. Solidly a été le pionnier du modèle "ve(3,3)", une amélioration du modèle ve, sur Fantom en février 2022, attirant rapidement des milliards de TVL avant [d'échouer dramatiquement en raison d'une très mauvaise exécution](https://hackmd.io/@c30/BJ2PNCwgs).
2. [Velodrome](https://app.velodrome.finance/), un fork de Solidly corrigeant ses problèmes critiques, a rapidement trouvé sa place sur Optimism après son lancement en juin 2022.
3. [Balancer](https://balancer.finance/) - une alternative historique à Curve et Uniswap, un DEX contenant des innovations intéressantes, [est récemment passé à un modèle ve en mars 2022](https://medium.com/balancer-protocol/vebal-is-live-aeda1ae13e20).
4. [SolidlyETH](https://twitter.com/SolidlyETH), encore. En effet, alors que le premier projet a échoué, la communauté s'est rassemblée pour prendre la relève et est sur le point de relancer Solidly, cette fois sur le mainnet, ce qui le rend beaucoup plus intéressant.

À mon échelle personnelle, je suis également addict aux tokens directeurs de liquidité, commme je le partageais récemment sur Twitter :


Tous les projets ont des besoins constants en matière de liquidités ; y répondre de manière durable a une grande valeur. En effet, la valeur des tokens directeurs de liquidité dépasse ce que les DAO/projets peuvent en tirer : 1 $ de bribe peut déplacer > 1 $ d'incitations. Les participants individuels peuvent également gagner beaucoup en étant capables de se positionner tôt dans une course pertinente.

Une fois le décor planté, plongeons dans le sujet du jour : Balancer, la course au BAL, et l'infrastructure "BAL-Layer-2" qui a émergé par-dessus, tout comme cela s'est produit avec Curve.

## Cartographie de la trinité de Balancer

![balancer-trinity](/img/2022/balancer-wars/balancer-trinity.png)
    
Nous avons regardé ensemble l'écosystème se développer à travers l'exemple de Curve. Pour la première fois, nous allons étudier [Balancer](https://balancer.finance/) et on observe déjà un écosystème mature ! Balancer a déjà "son Convex", appelée [Aura Finance](https://aura.finance/) qui contrôle plus de 25% du veBAL (contre >50% du veCRV pour Convex). 

Cependant, l'infrastructure de base de Balancer nécessite un troisième composant : un réseau d'automatisation nécessaire pour permettre le type de pools le plus avancé. À ce stade, on ne sait toujours pas qui mène cette course, c'est pourquoi j'ai utilisé l'un de leurs participants les plus importants - [PowerPool](https://powerpool.finance/) et son réseau de PowerAgents - pour jouer le rôle.

Pour ceux qui sont familiers avec l'approvisionnement en liquidités d'UniswapV3, on pourrait dire que les PowerAgents jouent un rôle similaire à celui de [Gelato](https://www.gelato.network/) : ils gèrent l'automatisation des opérations nécessaires pour permettre des cas d'utilisation spécifiques, tels que la récolte de récompenses et la composition automatique.

## En quoi Balancer est-il différent ?

Avec Uniswap et Curve, Balancer est l'un des DEX les plus anciens et les plus populaires aujourd'hui. En effet, si on considère le marché DEX d'un point de vue global, Balancer se classe à la cinquième place avec environ 3 % du volume total traité :

![defillama-dex-overview](/img/2022/balancer-wars/dex-overview.png)

_Vue d'ensemble du volume d'échange observé sur les principaux échanges décentralisés de [DeFiLlama](https://defillama.com/dexs)_

{{< notice note >}}
Balancer n'est lancé que sur mainnet, Polygon et Arbitrum - ce qui signifie moins de chaînes que la plupart des autres DEX du top 5, un élément à garder à l'esprit dans une comparaison au niveau global.
{{< /notice >}}

La première version de Balancer a été lancée en mars 2020, et de nombreuses itérations ont été expédiées depuis lors, améliorant le modèle de token BAL et la structure de liquidité. Cependant, Balancer avait des **particularités depuis la V1** qui sont probablement utiles pour expliquer pourquoi il est toujours debout aujourd'hui. Je vais me concentrer sur les plus emblématiques :

### Pool supportant deux à huit actifs

Balancer est encore, à ce jour, l'un des seuls DEX à offrir un tel éventail de structures de pool. En effet, une pool Balancer peut être composé de **n'importe quel nombre d'actifs allant de deux à huit**, alors que la plupart des autres DEX ne supportent que les paires, donc deux actifs à la fois.

Il permet de nouveaux types de pools, tels que : 

* Des pools de trois actifs, comme le pool wBTC/USDC/wETH similaire au pool TriCrypto de Curve, ou pour diversifier les paires d'un token donné, comme la pool OHM/ETH/DAI.
* Ou même pools avec six-huit actifs qui commencent à agir comme des indices de token autant que des pools de liquidité, comme le pool YFI/wBTC/COMP/wETH/UNI/CHZ/LINK.

### Pondération arbitraire des pools

En plus du support flexible en termes de nombre de tokens, **la pondération des pools n'a pas besoin d'être égale entre les tokens** et peut largement être personnalisée.

Cela permet des structures de pool déséquilibrées qui sont très utiles dans certaines situations :

* Par exemple, la pool OHM/DAI/ETH mentionné ci-dessus est **50%OHM, 25%DAI, et 25%wETH** - permettant de maximiser la liquidité OHM disponible contre DAI et ETH en même temps.
* Une autre distribution fréquemment utilisée est la **98/2**, particulièrement adaptée pour commencer à construire la liquidité d'un token nouvellement sorti avec un risque minimal de IL (puisque 98% du pool est composé d'un actif sûr, comme un stablecoin ou ETH).
* Enfin, la répartition de la liquidité **80 % token / 20 % actif apparié**, comme 80 % BAL / 20 % wETH, est également très recherchée, car elle permet aux détenteurs de tokens de participer à des activités de fourniture de liquidité avec des risques d'IL minimisés si le token devait s'apprécier.

### Pondération dynamique des pools

Enfin, Balancer peut ajuster la répartition de la pondération des pools selon les besoins grâce à un type spécifique de pool appelé [Liquidity Boostraping Pool (LBP)](https://docs.balancer.fi/products/balancer-pools/liquidity-bootstrapping-pools-lbps). Ces pools sont particulièrement adaptées au lancement de tokens et au développement de leur liquidité en même temps, car ils permettent de rationaliser le flux de tokens de la mise sur le marché. Par exemple :

1. Un projet donné veut lancer rapidement la liquidité de ses tokens - la DAO associée contrôle une quantité importante de tokens, mais généralement aucun des actifs de contrepartie potentiels (généralement ETH ou stablecoin).
2. Ils commencent donc avec un pool de 98%USDC/2%Token, ce qui leur permet de fournir des liquidités avec des exigences minimales en matière de token d'appariement.
3. Le pool agit comme un événement d'initiation de token et un mécanisme de découverte de prix en même temps. Le token démarre à un prix donné, qui diminue au fil du temps si personne n'achète le token.

![balancer-trinity](/img/2022/balancer-wars/LBP.png "Evolution du prix d'un token pendant un LBP s'il n'y a pas d'achat")

Les LBP sont conçus pour permettre aux utilisateurs intéressés par le projet d'acheter des tokens de manière équitable sur une période donnée, en les protégeant contre les attaques habituelles observées lors de lancements de tokens plus classiques (tels que les bots MEV snipant l'approvisionnement initial).

Grace aux LBPs, les projets sont en mesure de diversifier progressivement leur Token vers l'actif d'appareillage (ETH ou USDC généralement). En ce faisant, la LBP agit également comme un mécanisme de découverte de prix. Les projets qui l'utilisent sont ainsi dans une situation idéale pour ensuite apporter de la liquidité sur leur token qui sera possédée par le protocole, garantissant ainsi une liquidité minimale aux utilisateurs.

### Spécificités du modèle ve de Balancer

Balancer a également mis en œuvre son propre mécanisme de verrouillage inspiré de celui de Curve. Ici, au lieu de verrouiller le token directement (CRV ⇒ veCRV), les participants à la gouvernance doivent **verrouiller un token LP** correspondant au pool Balancer **80 % BAL / 20 % wETH**.

Comme nous l'avons dit plus haut, cette répartition des liquidités limite les risques d'IL pour les déposants suite à une hausse de BAL. Grâce à ce twist, Balancer peut capter d'importantes réserves de liquidités à travers les opérations normales de son mécanisme de participation à la gouvernance.

Enfin, depuis peu, il semble que Balancer se concentre sur les tokens productifs et développe de nouveaux cas d'utilisation pour y répondre. Par exemple, [BIP#19](https://medium.com/balancer-protocol/vebal-pt-2-bribing-and-bip19s-free-bribes-b2f8334eba14) introduit des "bribes gratuits" pour les pools impliquant des actifs productifs : le rendement produit par l'actif de la pool est recyclé comme pot-de-vin pour soutenir sa liquidité.

## Les guerres de Balancer : un état des lieux

Comme Curve, Balancer a un joueur dominant de sa course qui a développé un protocole maximisant sa synergie : Aura. Aura est l'un des nombreux services disponibles dans l'écosystème Balancer-fonctionnel-L2, mais un service largement dominant avec ~25% de tous les veBAL sous son contrôle.

Aura offre un farming efficace aux détenteurs de tokens LP de Balancer, avec des récompenses BAL augmentées grâce à l'importante réserve veBAL du protocole et aux incitations supplémentaires AURA. À cet égard, c'est la même chose que Convex avec Curve.

![defiwars-balancer](/img/2022/balancer-wars/defiwars-balancer.png)

_Vue d'ensemble des liquid wrappers veBAL - [merci defiwars.xyz](https://www.defiwars.xyz/wars/balancer)_

### Protocoles avec positions veBAL/vlAURA

En plus des protocoles travaillant sur des liquid wrappers pour veBAL comme Aura, d'autres DAO et projets ont construit des positions veBAL/vlAURA importantes pour augmenter et maintenir leur liquidité, comme Frax le fait sur Curve.

### Marchés de bribes Balancer

De nombreux marchés de bribes permettent l'achat de votes veBAL ou vlAURA ; voici les principaux :

1. [Hidden Hand - Aura](https://hiddenhand.finance/aura) et [Hidden Hand - Balancer](https://hiddenhand.finance/balancer).
2. [Paladin Warden Quest](https://app.warden.vote/quest/)
3. [Et StakeDAO BAL Votemarket](https://votemarket.stakedao.org/), une sorte d'agrégateur de marchés de bribes.

Pour suivre la guerre des BAL, assurez-vous d'exploiter les données offertes par la Llama Airforce :

![llama-airforce-aura](/img/2022/balancer-wars/llama-airforce-aura.png)

Comme on peut le voir sur le graphique, le marché des bribes a rapidement décollé avant de trouver un équilibre à environ **0,06$ par vote AURA, ce qui se traduit par une efficacité des bribes de 1,50x** : Un dollar dépensé pour influence le vote permet d'ajouter 1,50 dollar d'émissions de BAL à la pool ciblée au cours de l'époque.

Ce chiffre est plus faible pour Curve, environ 1,25x pour les bakchichs sur le vlCVX de Convex. C'est logique puisque les courses Curve sont beaucoup plus anciennes. 

## Quelles sont les prochaines étapes pour Balancer ?

Pour compléter la traction obtenue grâce à la refonte de la tokénomique et au passage au veBAL, plusieurs développements techniques ont été livrés/arrivent et devraient contribuer à renforcer sa position.

### Pools boostées

Les premières sont les pools boostées, qui sont déjà opérationnelles. Le but est d'augmenter le rendement natif pour les apporteurs de liquidité. Pour se faire, les Boosted Pools exploitent une source de rendement additionnel non sujette à l'IL comme par exemple Aave. Les boosted pools réallouent leurs distribution entre apport de liquidité et production de rendement en permanence, en fonction des besoins en liquidité de la pool.

Le bb-a-USD, l'équivalent du 3pool de Curve, est actuellement la plus grande Boosted Pool, mais d'autres sont à venir, dont une basée sur le LUSD : LUCY.

[Introduction au pool LUCY de PowerPool et ce qu'il apporte au $LUSD (en Anglais)](https://www.liquity.org/blog/introduction-to-powerpool-lucy-pool-and-what-it-brings-to-lusd)

### Aave x Balancer

Aave et Balancer ont des liens historiques, le module de sécurité d'Aave s'appuyant sur la V1 de Balancer, et Aave ayant même proposé un marché V2 il y a quelques années pour emprunter avec les tokens LP de Balancer en collatéral.

D'autres collaborations sont attendues, car [Aave a récemment acquis des tokens BAL](https://app.aave.com/governance/proposal/87/) et devra faire face à des besoins de liquidité considérablement accrus avec la sortie du GHO.


### Balancer : le foyer des LSDs ?

Enfin, si l'on considère la pool actuelle la plus importante en termes de TVL sur Balancer, une tendance claire se dessine : les liquid staking derivatives, tels que le rETH de Rocket Pool ou le stETH de Lido. Les deux ont des pools importants correctement incités sur le réseau principal de Balancer. 

Si vous n'avez jamais entendu parlé des Liquid Staking Derivatives, je vous renvoie vers un meetup DeFi France : **[DFF Lyon #1 - Perspectives sur les Liquid Staking Derivatives](https://www.youtube.com/watch?v=_eXm9VQh5HY)**

{{< youtube _eXm9VQh5HY >}}


La pool wstETH/wETH de Lido a même dépassé la pool 80BAL/20wETH et est devenue la première pool du DEX avec $200M TVL. De même, stMATIC/wMATIC est la première pool de Balancer/Polygon, suivi de MATICX/wMATIC, un autre dérivé liquide de MATIC staké. Sur Arbitrum, la troisième et dernière chaîne où Balancer est actif, là encore, la pool wstETH/wETH est en tête du classement. 

## Conclusion

Si vous souhaitez prendre part aux guerres de Balancer, assurez-vous d'exploiter toutes les excellentes ressources disponibles :

1. [Llama Airforce](https://llama.airforce/#/bribes/overview/hh/aura-bal)
2. [DeFiwars - Balancer](https://www.defiwars.xyz/wars/balancer)
3. [Dune Analytics](https://dune.com/balancerlabs/balancer-pools)

J'espère que cet article vous a fourni des informations utiles sur les tokens directeurs de liquidité, mais je voulais ajouter une dernière dimension : il semble qu'une **sous-catégorie** de tokens directeurs de liquidité soit en train d'émerger - **les tokens directeurs de liquidité d'emprunt**. 

Leur fonctionnement est très similaire, mais au lieu de permettre à leurs détenteurs de diriger les incitations vers des pools de liquidité, ils leur permettent de **diriger des incitatations vers des marchés de prêt choisis**. Ainsi, au final, ils atteignent un objectif différent par un moyen similaire : le contrôle d'un grand nombre de ces tokens directeurs de liquidité d'emprunt, comme le EUL d'[Euler Finance](https://euler.finance/), permet de maintenir une liquidité importante sur les marchés monétaires.

Cela vaut probablement la peine de s'y intéresser ; cela fait un moment que j'anticipe l'arrivée de la tokenomique basée sur ve et ve(3,3) sur les marchés monétaires.

🙏 Un grand merci à [Disiaque](https://twitter.com/disiaque_eth) pour sa relecture attentive et constructive.
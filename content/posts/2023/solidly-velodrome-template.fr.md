---
title: "ve(3,3) : l'étape logique après le modèle veCRV?"
description: "On creuse les modèles de Solidly et Velodrome pour comprendre en quoi les DEX ve(3,3) augmentent le modèle veCRV."
date: '2023-04-28T01:13:50.191Z'
categories: [DeFi, Comprendre]
tags: [DeFi, Ethereum, Decentralized Finance, Curve Finance, CRV, Convex, CVX, vlCVX, veCRV, Solidly, Velodrome, ve(3,3), DEX, Échanges]
toc: false
tocNum: false
url: solidly-velodrome-fork
---


Les forks Solidly/Velodrome ont poussé comme des champignons, en particulier sur les layers 2 populaires comme Arbitrum ou zkSync. Solidly est maintenant le troisième protocole le plus forké en DeFi et l'un des rares cas où les forks (comme Velodrome) sont les leaders du marché. À première vue, on pourrait croire qu'il s'agit d'un nouveau train de hype, comme lorsque nous avons eu la saison des forks Uni/Sushi, la saison des forks Olympus, etc.

En effet, c'est exagéré : une quantité absurde de DEX sont lancés chaque semaine, et 95% d'entre eux ne seront plus d'actualité dans six mois. Cependant, comme dans la plupart des cas de hype similaire, il existe une innovation fondamentale dans la conception des échanges décentralisés qui vaut la peine d'être étudiée.

Cet article se penchera donc sur les modèles Solidly et Velodrome afin de comprendre pourquoi ils sont devenus un modèle de fork standard. Cela étant dit, nous serons dans une excellente position pour réfléchir aux prochaines étapes pour ces DEX et à ce à quoi ce marché pourrait ressembler dans quelques mois.

C'est parti !

![cover-image](/img/2023/solidly-velodrome-template/cover.png)

{{< notice note >}}
Cet article suppose une compréhension minimale de la finance décentralisée et une compréhension approfondie du modèle veCRV. Si vous avez besoin d'une remise à niveau, consultez : [⚔ CRV Wars : comprendre la course à l'accumulation de CRV pour influencer le protocole Curve Finance](https://tokenbrice.xyz"/content/posts/2021/crv-wars.fr.md).
{{< /notice >}}

## Introduction aux DEX ve(3,3)

Avant de nous plonger dans la manière dont Solidly s'est appuyé sur le modèle veCRV et a tenté de l'améliorer, prenons un peu de recul.


### Structure de l'AMM VS couche d'incitation

Pour comprendre l'histoire des DEX ve(3,3), nous devons faire la distinction entre deux niveaux qui sont tout aussi importants pour un échange décentralisé :



1. **La structure de la liquidité** : les différents modèles d'AMM utilisés pour maintenir la liquidité, tels que x\*y=k d'UNIv2 ou le stableswap de Curve.
2. **Le modèle d'incitation** : les frais + toutes les autres incitations destinées au fournisseur de liquidités, y compris les émissions de jetons (comme dans le modèle CRV).

Si, en fin de compte, la première couche - la structure de la liquidité - est le cœur du jeu, la deuxième couche - les incitations - est cruciale pour attirer et maintenir une liquidité suffisante.

Curve a innové dans les deux domaines, mais les modèles dont nous allons parler aujourd'hui sont construits sur cette base et **se concentrent entièrement sur l'amélioration de la couche d'incitation**. En effet, au stade actuel, la plupart des DEX ve(3,3) exploitant le modèle Solidly ou Velodrome n'offrent que deux types de structure de liquidité bien connus : x\*y=k & stableswap.

{{< notice info >}}
Selon les DEX, ces deux modèles de liquidité sont appelés corrélé/volatile ou stable/volatile.
{{< /notice >}}

Parlons donc de ce qui était si intéressant dans le Solidly original d'Andre Cronje et des enseignements que nous pouvons tirer de son échec.


## Les innovations apportées par Solidly

Solidly a été présenté au début de 2022 sur [le medium de Andre Cronje](https://andrecronje.medium.com/ve-3-3-44466eaa088b) ; la partie cruciale de la vision de Solidly était une amélioration significative de l'utilité pour ceux qui vérouillent des tokens - les lockers. Sur Curve, les lockers sont engagés pour quatre ans, sans aucun transfert possible. Bien que cela soit excellent pour l'alignement des incitations à long terme de tous les participants de l'écosystème Curve, cela crée également une barrière importante à l'entrée.

C'est ainsi qu'est né ve(3,3), avec en son cœur **le veNFT**. Alors que les veCRV sont illiquides, les positions veSOLID sont représentées par le veNFT qui est lui liquide, ce qui permet leur transfert ou leur vente/achat de gré à gré. Cela permet de rendre le verrouillage moins effrayant. Pour l'encourager davantage, Cronje a introduit les "**rebases anti-dilutives**", un concept tiré d'Ampleforth/Olympus.

L'idée est simple : étant donné que le modèle Curve/Solidly DEX émet des jetons chaque semaine aux fournisseurs de liquidités, les détenteurs de jetons sont constamment dilués. Ils doivent constamment augmenter leur position afin de maintenir leur part de vote actuelle. Pour compenser cela, les détenteurs de veSOLID reçoivent un rebasement hebdomadaire proportionnel aux émissions. Cela leur permet de conserver leur part de vote même si aucun nouveau jeton n'est bloqué.

Hormis ces changements, Solidly a hérité de la plupart des éléments du modèle Curve, y compris **la fonction LP boost**, qui permet aux détenteurs de vetokens d'obtenir des rendements accrus sur leur position de liquidité. Cette fonctionnalité a des conséquences réelles puisqu'elle "appelle pratiquement un Convex". En effet, la conclusion logique d'une telle fonctionnalité est qu'un ou quelques acteurs s'emparent de quantités significatives de vetokens et fournissent leur LP boost aux déposants moyennant une commission.

La présence ou l'absence de cette caractéristique constitue la différence essentielle entre les modèles de Solidly et de Velodrome, et nous y reviendrons plus tard.

Enfin, il y a une dernière particularité essentielle sur le modèle d'incitation des votants. Sur Curve, les LP reçoivent la moitié des frais d'échange collectés + les émissions de CRV, alors que les votants ne sont pas exposés aux frais de la pool sur laquelle ils votent. Cela peut conduire à une situation où les veCRV holders votent pour des pools uniquement pour les incitations de vote, même si la pool ne fournit aucun volume à l'échange.

Sur Solidly, les LP ne sont récompensés que par l'émission SOLID, et les frais collectés sur la paire sont redirigés vers les votants de la pool. Ainsi, en tant que détenteur de veSOLID, pour optimiser vos gains, vous êtes incité à prendre en compte le volume de la pool sur lequel vous votez, et pas seulement les pots-de-vin. Cela abouti à un meilleur alignement des incitations des principaux participants du protocole (swapper, apporteur de liquidité, veHolder).

Solidly a aussi innové sur la stratégie de lancement, avec **un airdrop ciblé sur les protocoles**, en fonction de leur activité onchain sur Fantom, où Solidly se trouvait. Ensemble, toutes ces innovations et le battage médiatique ont permis d'attirer rapidement une quantité massive de liquidités sur l'échange.

Mais la mise en œuvre initiale de Solidly présentait quelques faiblesses majeures, notamment une baisse agressive des émissions et une création de jauges entièrement sans permission qui permettait à n'importe quel pool de recevoir des récompenses SOLID. Il était possible de jouer, alors on a joué. Rapidement, des jetons ont été créés dans le seul but de farmer SOLID : le prix du SOLID s'est écroulé et la spirale de la mort s'est enclanchée.

![cover-image](/img/2023/solidly-velodrome-template/solidly-tvl.png)

La TVL a disparu aussi rapidement qu'elle est apparue, et Solidly est entré dans l'histoire pour la plupart des gens. Mais ceux qui ont suivi les événements de près savaient que l'échec de Solidly ne provenait pas d'une faiblesse du modèle ve(3,3) mais plutôt d'un **détail négligé de son implémentation**, ce qui signifie que même si Solidly n'existait plus, ve(3,3) referait probablement surface. Et c'est ce qui s'est passé, quelques mois plus tard, sur une autre chaîne, et conçu par une autre équipe : Velodrome.

## Les améliorations apportées par Velodrome au modèle Solidly

[Velodrome](https://www.defiscan.info/protocols/velodrome-v2/optimism) a exploité le modèle de Solidly et a résolu le problème des émissions en mettant en place une **validation pour les jauges**, ce qui permet d'éviter la situation où les récompenses sont attribuées à des jetons inventés, comme c'est le cas sur Solidly. 

Velodrome est allé bien au-delà d'un simple fork et a mis en œuvre d'autres améliorations, notamment un modèle d'émissions plus durable et la **suppression de la fonction LP boost**, ce qui signifie qu'il n'y a pas de traitement préférentiel pour les détenteurs de veVELO en termes de rendement. Cela simplifie également l'expérience pour les nouveaux LP qui pourraient être déconcertés par la gamme de rendement que l'on voit sur les DEX avec la fonction LP boost.

Au-delà des caractéristiques techniques, une grande partie du succès de Velodrome est due à **l'exécution et au soin apporté par l'équipe aux stratégies de développement commercial**, une partie essentielle du modèle ve(3,3). Construit sur Optimism, Velodrome a trouvé son PMF comme la source de liquidité de la chaîne. Grâce à son modèle, le maintien de la liquidité sur Velodrome est beaucoup plus rentable pour les projets que, par exemple, sur Uniswap.

Comme Solidly, **Velodrome a airdrop plusieurs protocoles avec un NFT veVELO,** sans conditions, ce qui a énormément aidé à attirer l'activité initiale de vote et d'incitation. Le protocole a trouvé une bonne place, principalement auprès d'autres protocoles émettant des stablecoins ou des dérivés d'enjeux liquides ETH :

![defiwars-velodrome](/img/2023/solidly-velodrome-template/defiwars-velodrome.png "DeFiwars.xyz - veVELO ownership overview")


Cela fait presque un an, et l'activité s'est maintenue, grâce à des ajustements prudents et progressifs des **incitations OP attribuées sur le protocole**, connu sous le nom de [Tour de OP](https://medium.com/@VelodromeFi/tour-de-op-updates-631268181baa). La plupart d'entre eux sont utilisés pour encourager deux comportements essentiels pour soutenir la vélocité de la flywheel :

1. Les incitations au vote (bribes), qui sont encouragées grâce à un matching en OP.
2. Verrouillage de veVELO, encouragé par des OP bonus attribués aux lockers de VELO.

Le matching des bribes est encore augmentée pour les projets qui verrouillent veVELO ou déploient des quantités importantes de liquidité (Protocol Owned Liquidity), ce qui contribue à amplifier l'effet de renforcement : ceux qui veulent construire des liquidités soutenues à long terme sur Velodrome ont de bonnes raisons d'acheter veVELO, de verrouiller et de voter, de soumettre des incitations de vote et de fournir de la POL, **idéalement tout cela en même temps**.

Cela permet à Velodrome d'être en tête du classement des protocoles TVL sur Optimism et de traiter environ 30% du volume total de la chaîne, contre 50% pour Uniswap, qui a environ ¼ de la TVL de Velodrome.

![optimism-DEX-volume](/img/2023/solidly-velodrome-template/optimism-volume.png "Volume on DEXes on Optimism, from DeFiLlama")

Alors, pourquoi un tel écart entre les deux ? C'est simple : Le ratio Volume/TVL d'Uniswap est ~9x supérieur à celui de Velodrome car la liquidité sur Uniswap est beaucoup plus concentrée et donc plus efficace. Mais cela est sur le point de changer car Velodrome V2 arrive bientôt.



### Présentation de Velodrome V2

Bien qu'Uniswap ait eu une longueur d'avance avec la liquidité concentrée, cela va changer rapidement. La licence v3 [a expiré le 1er avril 2023](https://docs.uniswap.org/contracts/v3/guides/governance/liscense-modifications), ce qui signifie que le modèle est maintenant beaucoup plus facile à réimplémenter. De nombreux DEX, y compris les forks Solidly/Velodrome, ont l'intention d'exploiter cette possibilité. Cependant, pour garder cet article concentré, nous ne couvrirons que ce qui est annoncé pour Velodrome V2, attendu dans les semaines/mois à venir.

En effet, Velodrome V2 ne marquera pas seulement **l'introduction du style UNI-v3 de LP sur le DEX** mais aussi des améliorations significatives de l'UX/UI, un relayeur pour faciliter la gestion des veNFT, des illustrations pour les veNFT, et bien d'autres choses encore. Consultez l'[article d'annonce de la V2](https://medium.com/@VelodromeFi/velodrome-the-road-ah-43488531bb0e) pour plus de détails.

## Conclusion

J'espère que cet article vous a aidé à comprendre les avantages des modèles Solidly et Velodrome. Bien que je mentionne la myriade de forks dans l'introduction, j'ai gardé le cap dans cet article. Je pense que cela appelle une suite où je passe au peigne fin les principaux forks et les modifications qu'elles apportent au modèle : bientôt !

## Principaux enseignements

* **L'importance des capacités humaines/commerciales de l'équipe** | ve(3,3), tout comme Curve, sont des protocoles pour des protocoles. Le professionnalisme de l'équipe et sa capacité à établir des priorités et à mettre en œuvre le développement commercial sont des facteurs de réussite importants pour le DEX à long terme.
* **L'importance des bons partenaires**| Même si le BD est bien fait, un DEX ve(3,3) donné n'est bon que dans la mesure où ses meilleurs coureurs le sont. Oui, vous voulez qu'ils postent des incitations de vote, qu'ils apportent de la liquidité, qu'ils votent et qu'ils fassent connaître le marché, mais pas seulement. La qualité des liquidités acheminées vers le DEX est également importante (rapport volume/TVL & nature de la liquidité).
* **LP Boost et conséquences** | Si un ve(3,3) implémente le LP boost, il appelle des protocoles de type Convex. Le succès du ve(3,3) dépendra de l'ampleur et de la qualité des résultats obtenus par les protocoles Convex-like construits dessus. Pour suivre les statistiques clés des différents wrappers et des principaux détenteurs de jetons ve, consultez - [DeFiWars](https://www.defiwars.xyz/wars).
* **Impact de l'arrivée des liquidités concentrées** | Bien que ve(3,3) soit une innovation significative pour la couche d'incitation du DEX, il exploite actuellement des structures de liquidité basique. Une bonne adéquation entre le modèle d'incitation ve(3,3) et une structure de liquidité efficace de type UNIv3 permettra d'améliorer encore l'efficacité de la flywheel. 

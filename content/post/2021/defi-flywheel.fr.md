---
title: "🎡 Flywheel DeFi : synergies de protocoles à protocoles, par tokens interposés
"
description: "Analyse de Convex, CRV et des flywheels DeFi pour comprendre comment tokenomics et protocoles peuvent se renforcer mutuellement."
date: '2021-06-08T01:13:50.191Z'
reviewed: 2026-05-19
categories: [DEX, Yield]
tags: [DeFi, Ethereum, Money Markets, Liquity, Curve, CRV, Polygon, Convex, CVX, Yearn]
toc: true
tocNum: true
url: defi-flywheel
aliases:
  - p/defi-flywheel
image: /img/2021/defi-flywheel/defi-flywheel-cover.png
difficulty: "beginner"
---

En trois semaines, le protocole Convex a attiré plus de $ 3 milliards de dépôts, tout en devenant la plus grande 🐳 baleine de CRV, aujourd'hui et à priori pour toujours. La chance n'est jamais un facteur négligeable, mais avec une entrée aussi fracassante dans les sommets de la DeFi il faut chercher bien plus loin. En effet, la clef de compréhension de l'ascension fulgurante de Convex c'est la tokenomics, et c'est donc notre sujet du jour !

En DeFi, outre les caractéristiques techniques il faut aussi être fin sociologue, ou plutôt "game theorist" comme on dit par ici : savoir anticiper les réactions des foules à un jeu de règles données.

L'émergence des programmes d'incitations de liquidité (liquidity mining) l'année dernière a démontré qu'un jeu de règles approprié peut mettre des quantités colossales de capital en mouvement. La question est désormais de savoir le faire à bon escient, c'est-à-dire en étant conscient des enjeux **sur le long terme.**

En effet, le liquidity mining par lui-même n'attire à priori que des **dépôts mercenaires et opportunistes**. En soit, le liquidity mining est davantage un outil qui sert à faire connaître un projet qu'à sa pérennisation.

Durer en DeFi, c'est une affaire de tokenomics : c'est-à-dire les mécaniques des tokens natifs des protocoles. **La tokenomics, c'est en quelque sorte le gameplay d'un protocole DeFi**.

Vous le savez sans doute, je suis un grand admirateur du modèle CRV. Ça tombe à pic, puisque le jeu autour du token CRV n'a jamais été aussi vif que ces dernières semaines. Certains parlent même de #lockening pour décrire **la course à l'accumulation de VeCRV** à laquelle se livrent Convex, Yearn et StakeDAO.

On va rentrer dans le détail pour bien comprendre le concept de flywheel avec l'exemple de Convex / Curve. Je finirai par l'analyse de protocoles qui pourraient se prêter à un scénario similaire.


## L'émergence de la première 🎡 flywheel DeFi

Avec le lancement de Convex, on a commencé à utiliser un nouveau terme pour décrire son fonctionnement et sa tokenomics : 🎡 flywheel.

Il n'a pas vraiment de définition précise encore mais je me mouille : cela décrit un protocole qui réussit un triptyque gagnant :

1. Une tokenomics qui offre des opportunités intéressantes aux possesseurs du token optimistes sur le futur du modèle.
2. Un protocole qui est lui-même pertinent et répond à un vrai besoin, idéalement en synergie directe avec un autre protocole.
3. Un programme de liquidity mining (+airdrop) pour lancer la boucle et attirer les premiers possesseurs du token.

J'ai généralisé le modèle de Convex, mais il a une particularité supplémentaire : Convex est en quelque sorte un "meta-protocole" : il est **construit entièrement sur Curve Finance et en synergie avec celui-ci.**

Ainsi, l'ancêtre de la flywheel serait sans doute à chercher parmi les protocoles construits en synergie avec d'autres. Par exemple, bien qu'il soit construit sur BSC et [ait subi une attaque conséquente récemment](https://rekt.news/pancakebunny-rekt/), le protocole Bunny a bien aidé le DEX PancakeSwap à se développer.

En effet, Bunny propose de gérer les positions d'apport de liquidité Pancake, tout en émettant son propre token en fonction des rendements générés. Cela permet de simplifier la gestion des positions des apporteurs de liquidité sur Pancake tout en générant une source de rendement supplémentaire (token BUNNY).

Alors pour bien comprendre le concept de 🎡 flywheel, on va analyser la meilleure qu'on ait eu l'occasion de voir à ce jour : Convex. Elle s'avère un peu plus compliquée car elle s'appuie sur Curve, il faut donc déjà avoir saisi les enjeux à ce niveau là.


## CRV : Une tokenomics qui appelle les 🎡 flywheels ?

La tokenomics de Curve Finance a bientôt un an et pourtant elle est encore souvent mal comprise.

La grande élégance de la tokenomics CRV, c'est qu'elle **aligne les intérêts de plusieurs acteurs mieux que tout autre connue à ce jour** : les apporteurs de liquidité sur Curve, les holdeurs de CRV et le protocole Curve lui-même.

En effet, le modèle tend avec le temps à confondre les deux populations (CRV holdeurs et LP) grâce à deux mécaniques :



1. Les apporteurs de liquidité sont rémunérés en CRV.
2. Les stakers de CRV (holdeurs VeCRV) peuvent "booster" le rendement en CRV de leur position d'apport de liquidité sur Curve.

Le modèle crée ainsi un chemin intéressant pour les utilisateurs du protocole, qui sont **fortement incités à s'engager dans la durée**. En effet, verrouiller des CRV en VeCRV devient de plus en plus efficace plus l'engagement est long - le maximum étant 4 ans.

Pour aller plus loin tout en français, je vous invite à suivre le [direct-marathon Curve Finance avec Charlie.](https://www.youtube.com/watch?v=G5PbqGtjSDQ) Sinon, [cet article en anglais est aussi utile.](https://stakecapital.substack.com/p/curve-tokenomics-and-first-mover)

![crv-tokenomics](/img/2021/defi-flywheel/crv-tokenomics.png "Les bases de la tokenomics CRV")

Néanmoins, le modèle CRV connait aussi ses limites, la plus évidente étant l'impact des frais de transaction Ethereum : des sommes importantes peuvent être requises pour que le jeu commence à faire du sens.

Le truc, c'est que depuis longtemps, les plus grands apporteurs de liquidité sur Curve ne sont plus des utilisateurs mais **d'autres protocoles**. Mutualiser les fonds permet ainsi de réduire l'impact des frais en gaz tout en développant potentiellement une stratégie d'accumulation de VeCRV.

C'est ainsi que différentes solutions sont apparues pour **gérer les positions d'apport de liquidité sur Curve**, la plus connue étant Yearn, mais il y a aussi Harvest et StakeDAO. Bien qu'elles puissent être utiles pour les déposants, elles souffrent de deux grandes limites : les frais de gestions élevés ainsi que leur approche proche de celle d'un parasite. Yearn, Harvest ou StakeDAO vendent immédiatement tout token farmé. Cela résulte en une pression vendeuse grandissante sur le token natif des protocoles utilisés pour produire le rendement.


## Le modèle de Convex, première flywheel 🎡

Fonctionnellement, Convex propose un service similaire à Yearn aux apporteurs de liquidité sur Curve : la **gestion automatisée de leur position afin d'en optimiser le rendement**. Tout comme Yearn, Convex a une stratégie d'accumulation de VeCRV afin de maximiser le rendement des déposants en CRV grâce au mécanisme de boost.

Néanmoins, l'approche sous-jacente est totalement différente de Yearn et s'inscrit dans une synergie vertueuse avec Curve :



1. **Pas de vente systématique** : contrairement à Yearn, Convex ne vend pas les tokens farmés. Les apporteurs de liquidité sont ainsi rémunérés en CRV mais aussi en CVX, le token natif de Convex.
2. Les **frais collectés par Convex sont dédiés à 100% au protocole**, tandis que Yearn par exemple paie des "strategists" - de toute évidence assez redondants sur une stratégie simple comme celle-ci.
3. Grâce à la distribution des frais collectés, Convex crée deux **opportunités de staking intéressantes** pour composer ses rendements, détaillées plus bas.
4. Enfin, **la liquidité** sur le token qui représente un CRV dans Convex (CvxCRV) est **plus** **optimale** que l'équivalent Yearn : CvxCRV s'échange dans une pool directement contre le CRV, avec un programme d'incitation en CVX.


### Les frais : le nerf de la guerre

Bien comprendre la structure des frais est essentiel pour arriver à saisir ce qu'il s'est passé avec Convex. Le protocole contrôle désormais plus de 32M de VeCRV, soit **presque deux fois le total de Yearn, et ce à peine après trois semaines d'existence**.

![convex-curve-stats](/img/2021/defi-flywheel/convex-curve-stats.png "Rendements générés par Convex sur Curve Finance")

Convex prélève un frais total de 16% sur l'ensemble des CRV farmés sur le protocole (contre 20/2 sur tous les tokens pour Yearn, ou 30% pour Harvest par exemple). Sur les 16%, 1% sert à couvrir les frais opérationnels comme le coût en gas des collectes.

![convex-synergies-CRV](/img/2021/defi-flywheel/convex-synergies-CRV.png "Synergies et capture de valeur Convex / Curve")

Le plus intéressant s'opère au niveau de la redistribution des 15% restants, soit 15% de tous les CRV farmés par Convex (**plus de 400 000 CRV par jour** au rythme actuel). Vous pouvez consulter la [position Curve de Convex via CurveMarketCap par ici.](https://curve.fi/pools?see=0x989aeb4d175e16225e39e87d0d97a3360524ad80) Deux populations de stakers sont éligibles à ce juteux gâteau :

1. **10% sont reversés aux stakers de CvxCRV**, sous forme de CRV, en plus de leur rendement en token 3pool et CVX (+airdrops VeCRV holder). Posséder du CvxCRV devient ainsi bien plus attractif que du VeCRV pour un simple déposant.
2. **5% sont reversés aux stakers de CVX**, sous forme de CvxCRV. Cela signifie donc que 5% de tous les CRV farmés par Convex sont capturés et verrouillés au sein du protocole. Cela permet d'augmenter mécaniquement la réserve de VeCRV même si aucun dépôt de CRV par un tiers n'a lieu.

La situation est encore en plein développement et on observe encore des écarts surprenants : par exemple à l'heure où j'écris ces lignes (07 juin) la capitalisation totale du token CVX ne représente même pas la moitié de la valeur des CRV que possède le protocole ($30M vs $80M). Je pense que la situation va s'harmoniser sur le long terme.


## Anticiper les prochaines flywheels ?

Avec quelques notions sur Curve et une analyse de la flywheel 🎡 Convex, on a désormais les cartes en mains pour se risquer au jeu de la prospective. Avant cela néanmoins je vous propose plutôt d'aller regarder dans le passé pour analyser une presque flywheel ratée : Pickle Finance.


### Pickle Finance : une flywheel arrivée trop tôt

Sur le papier, Pickle a tout d'une flywheel : c'est un système pour augmenter les rendements des dépôts Yearn grâce à l'émission additionnelle de token PICKLE. PICKLE reprend des éléments du système VeCRV, avec un mécanisme de verrouillage (DILL) qui permet de stimuler les rendements en PICKLE des dépôts sur Pickle Finance.

Sauf que… Pickle n'apporte techniquement strictement rien en plus de Yearn, en dehors de l'émission de PICKLE. En outre, Pickle ne se spécialise pas : des fermes sont proposées sur les vault Yearn mais aussi certaines paires Sushi. À l'inverse de Convex, Pickle n'est donc pas en mesure de développer un avantage unique (moat) sur les services farmés.

En DeFi rien n'est définitif. La situation de Pickle pourrait évoluer, si les tokenomics des protocoles sous-jacents (YFI et SUSHI) évoluent. Les deux protocoles semblent s'orienter vers une réappropriation du modèle VeCRV donc c'est tout à fait possible. Un modèle qui mèle la logique de burn Adamant/Ellipsis et le boosting Curve a même été proposé pour Sushi : **[oSUSHI](https://forum.sushi.com/t/sushinomics-introducing-osushi/4055)**.

![veYFI](/img/2021/defi-flywheel/veYFI.png "Exemple d'interface pour le mécanisme de verrouillage/boost YFI (veYFI)")


### Adamant Finance : 🎡 flywheel sur les LP Polygon ?

Adamant est un protocole encore récent qui existe sur la sidechain Polygon. Il permet la gestion facilitée des positions d'apport de liquidité sur les principaux services d'échanges : QuickSwap, Cometh, SushiSwap, etc.

Outre la composition automatique des rendements, Adamant offre aussi des récompenses supplémentaires en ADDY (en fonction des profits générés). Tous les ADDY obtenus sont vested (verrouillés) pendant 3 mois et peuvent être retirés plus tôt avec une pénalité de 50%. Celle-ci est redistribué à ceux qui acceptent de staker + locker leur ADDY pendant 3 mois.

En outre, tous les stakers de ADDY (même ceux vested) bénéficient d'une part des frais collectés par la plateforme, distribués en wMATIC. Le protocole dispose donc d'une tokenomics déjà assez élaborée avec différents mécanismes de rétention, mais il lui reste encore quelques améliorations à trouver pour devenir une flywheel.

La première consisterait à introduire une plus grande incitation à verrouiller ses ADDY grâce à un système de boost similaire à Curve. Les déposants possédant des ADDY en stake+lock disposeront ainsi d'un meilleur rendement en ADDY sur leur position LP. C'est déjà en discussion voir même en développement.

Reste à Adamant à développer une synergie avec les protocoles farmés aussi solide que Convex avec Curve. C'est pour l'instant difficile voir impossible car aucun d'entre eux ne dispose d'une tokenomics aussi subtile que CRV.


### Un service X sur Liquity : 🎡 flywheel sur un marché monétaire ?

Jusqu'à présent, on a discuté de flywheels construits sur des services d'échange décentralisés, cela semble le plus évident. Néanmoins on peut envisager des modèles similaires sur d'autres types de service, comme les marchés monétaires.

Je vous propose donc de finir avec une flywheel théorique maison. À ma connaissance un tel protocole n'existe pas encore : c'est à vous de jouer !

L'équation de base est simple :

1. Il y a une forte demande pour des **produits "passifs ETH"** - des produits qui développent des stratégies sur ETH en vue d'accumuler des ETH.
2. Pour se faire, une des options est d'emprunter des Stablecoins en utilisant les ETH comme collatéral. Les Stablecoins peuvent ainsi produire un rendement supplémentaire.
3. Pour cette stratégie, Liquity serait **la plateforme de prédilection sans contestation possible**. En effet, le coût d'emprunt y est le plus bas du marché (presque 12x moins cher que Maker sur une année) et les opportunités de rendement sur le stablecoin LUSD ne manquent pas.

![protocole-x-liquity](/img/2021/defi-flywheel/protocole-x-liquity.png "Exemple d'un protocole flywheel construit sur Liquity (fictif pour l'instant)")

L'enjeu sur une telle stratégie mutualisée c'est de **gérer le ratio de collatéralisation** et d'être en mesure de l'équilibrer rapidement si le marché venait à bouger. Là encore, Liquity s'y prête bien puisque la stability pool offre un rendement attractif sur le LUSD tout en permettant de  **mobiliser rapidement les LUSD pour rembourser la dette si besoin**.

Le protocole X en question proposerait ainsi **un produit passif de rendement sur l'ETH** pour les utilisateurs finaux qui n'auraient pas à gérer la position eux-même. On peut également envisager que le protocole X ait son propre token avec une tokenomics qui vient adresser un des principaux dangers de la stratégie : le manque de prédictibilité. Ainsi le token natif de protocole X pourrait servir à inciter les dépôts longs et d'une durée prévisible (les utilisateurs verrouillent leur ETH sur 3/6/9/12 mois par ex).

Des engagements longue durée permettent également de **développer une stratégie sur les LQTY farmés par les LUSD.** Ainsi en engageant des ETH pendant un an dans le protocole par exemple, l'utilisateur accumulera un droit sur une portion des LQTY farmés par l'ensemble du protocole, et donc un droit, à vie, aux LUSD et ETH qu'ils génèrent. La synergie du protocole avec Liquity ainsi que les rendements long-terme sont maximisés si le protocole X ne vend aucun LQTY, comme c'est le cas dans le concept proposé ci-dessus.

J'espère que cet article vous aidera à mieux comprendre ce qu'il s'est joué avec Convex, Yearn et Curve ces dernières semaines et utiliser les leçons tirées de cet épisode pour identifier les prochaines opportunités similaires.

Ce qui est chouette avec les différents mécanismes d'incitation, c'est qu'ils précèdent l'action. En game theory, il n'y a pas de certitudes, mais certains comportements sont quasiment mécaniques - pour qui comprend réellement les incitations et leurs enjeux. C'est à vous de jouer !

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

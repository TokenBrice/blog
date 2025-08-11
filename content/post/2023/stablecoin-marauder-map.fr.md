---
title: "La carte du Maraudeur des stablecoins"
description: "Chaque semaine de nouveaux stablecoins émergent : suivre les innovations est devenu une exercice difficile. AMO ? PSM ? DSR ? pegKeeper ? Cet article passe en revue les différents mécanismes qui sous-tendent les stablecoins afin d’en apprécier leur pertinence."
date: '2023-09-15T01:13:50.191Z'
categories: [DeFi, Comprendre]
tags: [DeFi, Ethereum, Decentralized Finance, Stablecoins, Stable Assets, Money Markets, Aave, GHO, crvUSD, LUSD, fETH, xETH, Interest Rate]
url: stablecoin-marauder-map
image: img/2023/stablecoin-marauder-map/stablecoin-marauder-map-cover.png
---

De nouveaux stablecoins plus ou moins décentralisés émergent chaque jour, et avec la multiplication des modèles dont ils s’inspirent, des blockchains et des couches (layers 2), la tendance n'est pas prête de s'arrêter. **Naviguer dans le paysage des stablecoins devient une compétence essentielle en DeFi**.

Les modèles de stablecoins centralisés sont les plus faciles à évaluer au contraire des stablecoins décentralisés qui exploitent divers mécanismes complexes, plus difficiles à comparer. Pourtant, des dizaines de stablecoins décentralisés pertinents apparaissent chaque année, et je ne m'attends pas à ce que cette tendance s'arrête de sitôt.

Cet article a donc pour but de fournir une carte du maraudeur pour naviguer sur la mer des stablecoins décentralisées. Avant de passer au peigne fin les innovations dans ce domaine, permettez-moi de revenir une minute sur le contexte : pourquoi nous intéressons-nous tant aux monnaies stables (décentralisées) ?


## Une question de valeur - la taille compte

En d'autres termes, **les stablecoins sont de très loin les produits les mieux adaptés aux marchés cryptos**. La DeFi, c'est cool, non ? C’est l’objet passion de ce blog. Pourtant il y a environ 3 fois plus de valeur bloquée dans les stablecoins que dans les protocoles DeFi.

Actuellement, la TVL totale de la DeFi est d'environ 38 milliards de dollars pour 124 milliards de dollars de stablecoins en circulation, principalement centralisés : l'USDT en représente 66 % et l'USDC 20 %.

{{< notice note >}}

N'oubliez pas que ces deux mesures sont redondantes, car les stablecoins sont largement utilisés en DeFi, de sorte que l'écart effectif est encore plus élevé.

{{< /notice >}}

Et maintenant, le vif du sujet ! Au fur et à mesure que nous examinerons les modèles de stablecoins décentralisés utilisés, j'illustrerai leurs mécanismes avec des exemples issus de projets réels : imaginez cet article à la croisée d’un livre de recettes et d’une carte de maraudeur, mais sur le thème des stablecoins décentralisés.


## COMMENT CONSTRUIRE UN STABLECOIN DÉCENTRALISÉ

Il existe une gamme quasi infinie de modèles pour produire des monnaies stables décentralisées ; cependant, tous reposent sur deux éléments fondamentaux :



1. **La stabilisation du prix** | Trouver un moyen efficace de stabiliser le prix sans trop de compromis.
2. **La liquidité** | Gérer activement la liquidité du stablecoin afin d'en optimiser l'efficacité.

Si ces deux thèmes répondent à la même nécessité, c’est à dire garantir que le stablecoin peut être échangé à sa valeur de référence en toutes circonstances, ils fonctionnent toutefois sur des périodes de temps différentes. Les mécanismes de stabilisation sont construits de manière à ce que les stablecoins tendent vers leur parité sur des périodes moyennes à longues. Les stratégies de liquidité sont là pour garantir que même des quantités importantes de stablecoins peuvent être achetées et vendues au plus près de leur valeur de référence.

Il s'agit là de deux conditions préalables pour qu'un concept de stablecoin soit pertinent et ait une chance de s'imposer. Une faille dans l’une de ces deux dimensions met en péril l'ensemble de la conception. Examinons donc les principaux mécanismes de stabilisation des prix et leurs conséquences.


### MÉCANISMES DE STABILISATION DES PRIX

Face à une demande importante, les stablecoins décentralisés peuvent se déprécier, c'est-à-dire s'écarter de leur prix d’ancrage, généralement 1 dollar, soit vers le haut (overpeg), soit vers le bas (depeg). Bien que similaires, ces deux mouvements résultent de problèmes de conception très différents. Commençons par le plus courant, le depeg : lorsqu'un stable vaut moins que sa valeur d'ancrage.


#### Depeg illustré par le GHO

Cela se produit généralement lorsque le stablecoin est principalement utilisé pour l'effet de levier et manque d'autres cas d'utilisation significatifs - **un excellent exemple actuel est le GHO d'Aave, qui se négocie autour de 0,97 $**. GHO est l'un des stablecoins les moins chers à emprunter (1,5% APY max), ce qui a créé une forte demande initiale. Cependant, GHO n’offre pas beaucoup d’options d’utilisation directe, à part fournir de la liquidité. Ainsi, de nombreux emprunteurs échangent leur GHO contre, par exemple, du DAI, afin d'exploiter le rendement de 5% du DSR.

En outre, la DAO d’Aave a tardé à prendre des mesures pour soutenir GHO. Bien que le stablecoin soit en ligne depuis mi-juillet, il y a encore très peu d'incitations visant à augmenter sa liquidité ; par ailleurs, les incitations présentes sont mal réparties car elles se concentrent principalement sur les pools de stableswaps où GHO est surpondéré en raison de son prix. Comme ces pools sont composés à 80 % de GHO, ils fournissent peu de liquidité adéquate au prix actuel :

![gho-balancer-pool](img/2023/stablecoin-marauder-map/gho-balancer-pool.png "Un des principaux pools GHO sur Balancer")

A l'heure actuelle, la seule pression pour le repeg du GHO vient de ses emprunteurs qui, s'ils pouvaient emprunter et échanger GHO autour de 1$, rembourseraient leur dette avec une décote de ~3%.

GHO aura besoin d’options de rentabilité attrayantes directement au sein du protocole pour s'approcher à nouveau de la parité, comme par exemple de nouvelles options d'apport de liquidité. Néanmoins, un module de staking basé sur GHO, avec partage des revenus, conviendrait parfaitement. Globalement, nous avons besoin de plus de réserve de GHO, c'est-à-dire de mécanismes permettant de frapper des GHO et de les conserver en tant que tels pendant de longues périodes. Pour l’instant, la gouvernance semble s’orienter vers un soutien accru à la liquidité de GHO et un potentiel PSM (Peg Stability Module) : vous trouverez plus d'informations ci-dessous, dans les paragraphes relatifs à  Maker/DAI.

Les défis actuels que GHO rencontre sont relatifs à son jeune âge et, côté DAO, à un manque de préparation du lancement. La DAO s'améliore à cet égard, et de nombreuses propositions ont été avancées pour remédier à la situation, notamment l'établissement d'un [comité de liquidité pour GHO](https://governance.aave.com/t/arfc-treasury-management-gho-liquidity-strategy-update/14801). Je devrais y contribuer.


#### Overpeg illustré par le LUSD

[Liquity](https://www.defiscan.info/protocols/liquity/ethereum) utilise un mécanisme unique de *Redemption* pour maintenir la stabilité de son prix. Dans Liquity, les utilisateurs déposent des ETH comme garantie pour emprunter et frapper des stablecoins (LUSD). La principale innovation réside dans le mécanisme de *Redemption*, qui permet aux utilisateurs d’échanger leurs LUSD contre la garantie sous-jacente (ETH) à taux fixe, même si le prix du marché de l'ETH chute de manière significative.

Ce mécanisme incite les utilisateurs à stabiliser le prix du LUSD en le rachetant lorsque le prix de l’ETH est bas, ce qui réduit ainsi l’offre en circulation en maintenant son cours au plus près de celui de l'USD.  **Les  détenteurs de LUSD ont ainsi un accès immédiat et immuable au collatéral du LUSD** sans devoir accéder à de la liquidité sur un échange décentralisé.

Les rachats offrent un niveau de garantie supplémentaire aux détenteurs de LUSD mais ajoutent de la complexité du côté de l'emprunt, poussant les emprunteurs à surveiller et à ajuster leur TVL par rapport à d'autres utilisateurs du protocole et aux conditions du marché.

{{< notice note >}}

Les *Redemptions* offrent l'accès le plus direct à la garantie sous-jacente d'un stablecoin. Les stablecoins centralisés comme l’USDC ou l’USDT utilisent un mécanisme similaire, bien que soumis à autorisation, pour permettre la *Redemption* en USD.

{{< /notice >}}

Le LUSD s'est négocié à un prix élevé pendant la majeure partie de son existence, même si la situation s'est récemment améliorée. En effet, plusieurs facteurs ont contribué à accroître la liquidité et la pression sur les prix : le succès des [Chicken Bonds](https://chickenbonds.net/), les stratégies de liquidité avancées sur les nouveaux DEX comme [Maverick](https://mav.xyz/), ou l'accumulation de LUSD par les DAO et les trésoreries.

La raison de ce prix élevé reste à déterminer avec précision. L'un des principaux facteurs probables est que **LUSD dessert une niche unique**, le stablecoin à la résilience optimale, où il y a généralement plus de demande (personnes souhaitant détenir LUSD) que d'offre (détenteurs d'ETH empruntant LUSD et le vendant). [Ce sujet a été traité en profondeur l'année dernière sur le blog de Liquity](https://www.liquity.org/blog/the-premium-of-resiliency#:~:text=LUSD%20est%20un%20stablecoin%20mais%20vient%20avec%20des%20défis%20de%20scalabilité.).

Si le depeg est globalement plus préoccupant, l’overpeg peut aussi avoir un impact non négligeable en rendant les coûts d'emprunt effectifs moins prévisibles pour les utilisateurs.

L'overpeg du LUSD est principalement le fait de mécanismes psychologiques : un long pic de dépassement a été observé lors de mouvements de panique sur le marché lorsqu’un certain stablecoin centralisé de premier plan a été perçu comme en danger. 

En effet, grâce à sa résilience, le LUSD est considéré comme **un stablecoin sûr**. Une performance remarquable mais qui a un prix : les foules se ruent sur le LUSD lorsque d'autres stablecoins sont en panne, comme lorsque l'USDC a perdu 10 % de sa valeur à la suite du bank run de la Silicon Valley Bank. Le LUSD a connu un volume d'échange incroyable ce jour-là, avec des achats importants au-dessus de 1,03 $, 1,04 $ et 1,05 $ alors que le marché perdait pied. Dans un tel contexte de panique certains utilisateurs sont prêts à payer le prix fort pour se mettre à l'abri.

    
#### Le DAI et le PSM : résoudre le problème de l’overpeg, non sans coût

À ses débuts, avant la mise à jour du Mutli Collateral Dai, le DAI était confronté aux mêmes problèmes que le LUSD : il avait tendance à overpeg. Avec la mise à jour, Maker a introduit le Peg Stability Module (PSM) pour stabiliser le prix de son stablecoin DAI. Le PSM agit comme un tampon entre le marché et l'écosystème DAI. Il permet aux utilisateurs d'échanger des actifs stables comme l'USDC contre des DAI à un taux de change fixe.

En ajustant le taux de change en fonction des dynamiques du marché, MakerDAO peut influencer l'offre de DAI et maintenir son prix proche de la parité avec l'USD. Ce qui a permis à  Maker de résoudre le problème d’ancrage du DAI. Cependant, cela a eu un coût : l’accumulation d'USDC et d'autres stablecoins centralisés comme garanties du DAI.

![maker-psm](img/2023/stablecoin-marauder-map/maker-psm.png "Le PSM a accumulé ~$1B de stablecoins centralisés en collateral pour DAI")

#### AMO (Algorithmic Market Operations) de FRAX : scaler la liquidité et le risque à l'infini

FRAX est un stablecoin décentralisé qui utilise un algorithme pour ajuster son ratio de collatéralisation en fonction des conditions du marché, et maintient donc son prix. Lorsque le prix du FRAX se négocie au-dessus de sa parité, le système frappe de nouveaux FRAX et les injecte dans des paires de liquidité.

Inversement, lorsque le prix du FRAX tombe en dessous de la parité, l’AMO réduit le ratio de collatéralisation afin d'encourager les utilisateurs à frapper du FRAX et à rétablir la parité. Les AMOs s'accompagnent de risques supplémentaires, liés à l'utilisation d’actifs frappés sans garantie : plus cette exposition est élevée, plus le risque est important.

Les principaux risques d'une telle conception se manifestent lorsqu'un problème survient avec l'un des services connexes (généralement les marchés monétaires ou DEX). Supposons que 10 millions de FRAX soient frappés par l'AMO et déposés sur un marché monétaire pour être empruntés par les utilisateurs. Or, le marché monétaire souffre d'un problème avec l'une de ses garanties et se vide : il y a maintenant 10 millions de FRAX de plus en circulation avec 0 garantie.

Pour y remédier, une gestion très active des AMOs est nécessaire - par des humains et via un multisig. Ce n'est pas idéal en terme de sécurité, car les AMOs peuvent frapper du FRAX à volonté, sans aucune contrepartie / garantie.


#### crvUSD pegKeeper : un meilleur PSM ?

Pour assurer la stabilité du crvUSD, Curve a exploré une voie similaire à celle du PSM, mais légèrement améliorée. En effet, ici, la contribution des utilisateurs n'est plus nécessaire :

Avec Maker PSM, c’est toujours l'utilisateur qui décide : en cas de dépassement, les utilisateurs fournissent des USDC comme garantie à Maker PSM et frappent des DAI, ce qui contribue à faire baisser son prix. Si le prix du DAI devait baisser, les utilisateurs pourraient de la même manière acheter du DAI (à moins de 1 $) pour le racheter contre 1 USDC, ce qui contribuerait à ramener son prix à son niveau de référence.

crvUSD fonctionne de manière similaire(si crvUSD>1$ => frapper, si crvusd&lt;$1 => brûler) mais ne nécessite aucune action : le système se stabilise de lui-même grâce à ses contrats pegKeepers. Ces contrats spéciaux peuvent créer des crvUSD non collatéralisés sous certaines conditions et pour des cas d'utilisation spécifiques uniquement.

Il y a 4 pegKeepers, chacun connecté à une pool différente de crvUSD et stablecoins centralisés redeemables (USDC, USDT, USDP et TUSD). Lorsque le crvUSD est surcoté, ils peuvent frapper du crvUSD pour l'échanger dans le pool associé, contribuant ainsi à ramener le prix du crvUSD à 1$. Lorsque le crvUSD est sous-coté, le pegKeeper peut racheter du crvUSD sur son pool associé (en utilisant les soldes stables centralisés accumulés pendant la surcote) et le brûler pour ramener le prix du crvUSD à sa valeur de référence.

Ainsi, les PegKeepers accumulent une dette en crvUSD envers le protocole lorsque le stablecoin est surcompensé, pour être idéalement résorbée une fois que le crvUSD est sous-compensé. La clé réside ici dans l'équilibre, en veillant à ce que l'écart entre l'offre de crvUSD (y compris la dette Pegkeeper) et l'offre empruntée ne devienne pas trop important.

![pegkeeper](img/2023/stablecoin-marauder-map/pegkeeper.png "Data from Curve Monitor")

Bien que les pegKeepers représentent toujours un risque pour le protocole, tout comme l'AMO de FRAX ou le PSM de Maker, il semble plus atténué ici. Mais le crvUSD est encore jeune, et seul le temps permettra d'évaluer avec précision la résilience effective du système.


### GESTION DES LIQUIDITÉS

La gestion de la liquidité en matière de stablecoin pourrait faire l’objet d’une thèse. C'est l'un des sujets les plus mal compris dans l'espace. Il m’importe que vous, chers lecteurs, soyez conscient de son aspect crucial.


#### La gestion des liquidités en tant que non-sujet

Si vous lisez ce blog, vous avez probablement déjà compris que **les stratégies de liquidité sont au cœur des guerres entre stablecoins.** Pourtant, de nombreuses équipes n'ont pas encore pris conscience de cette réalité. Elles les considèrent comme un élément peu critique, que la DAO  traitera plus tard… ce qui est incroyablement dangereux.

En effet, les DAOs ne sont pas les meilleures structures pour gérer la liquidité car elles ont tendance à utiliser des solutions non optimisées, à surpayer, et ont simplement besoin d'être plus rapides pour s'adapter au rythme soutenu des fluctuations de liquidité. Ce n'est pas une surprise, nous avons déjà établi depuis longtemps que les **DAOs/gouvernances sont adaptées aux orientations stratégiques (long terme) mais inaptes à la gestion à moyen/court terme (tactique),** grâce à l'exemple de MakerDAO (où, malgré l'absurdité de la chose, les détenteurs de MKR votent encore le taux d'intérêt de chaque vault, un paramètre purement opérationnel).

La solution évidente serait que la DAO **désigne un comité de liquidité** - une petite équipe de spécialistes disposant d'un budget à mobiliser en toute autonomie. Le comité pourrait être engagé pour une durée déterminée, et la DAO conserverait le droit de ne pas renouveler ou révoquer ce comité, comme cela se pratique avec n'importe quel prestataire de services.

Je vous invite à regarder les principaux projets de stablecoins gérés par des DAO et à identifier ceux qui ont déjà un comité. A ma connaissance, [seul Aave l'envisage enfin pour GHO](https://governance.aave.com/t/temp-check-treasury-management-create-and-fund-gho-liquidity-committee/14800). Le comité permet agilité et facilité opérationnelle pour la gestion de la liquidité tout en ettayant la réflexion et la prévoyance de la DAO dans son approche de la liquidité. Cela lui permet d'explorer des partenariats et des collaborations avec des acteurs finement sélectionnés, tels que le soutien d'un DEX innovant dès le premier jour de son lancement, contre de nombreux mois nécessaires pour expliquer la pertinence de l'innovation aux parties prenantes de la DAO, le vote d’un budget et sa mise en œuvre...


#### Les compétences sont rares

La dure réalité de la gestion des liquidités est que les compétences sont extrêmement rares. Cela souligne la raison pour laquelle le sujet doit être mieux compris alors qu'il n'est que rarement priorisé lors de la conception du projet et même dans les discussions ultérieures de la gouvernance. Un bon gestionnaire de liquidités doit avoir une compréhension précise des éléments suivants :



* Modèle de structure de liquidité de base, x\*y=k
* Structures de liquidité personnalisées telles que le stableswap
* Liquidité concentrée de base, style UNIv3
* Couche de gestion des liquidités Uniswap (Bunni, Merkl, etc.)
* Modèle de gestionnaire de liquidité CL (Gamma, Arrakis, etc.)
* veCRV tokenomics & ecosystem // veBAL
* Les marchés de vote et la culture des bribes
* Liquidité concentrée avancée, style Maverick
* Modèle d'incitation Maverick (Boosted Pool)
* Maverick tokenomics (veMAV)
* Panorama des agrégateurs de DEX et logique de pathing (optimisation des routes de swap)

**L'étendue des outils, services et protocoles utilisés pour la gestion des liquidités augmente de façon exponentielle, et très peu d'acteurs suivent de près**. Il est fréquent d'observer des écarts absurdes entre les dépenses de liquidité de deux projets similaires, avec parfois des écarts à plusieurs ordres de grandeur en terme de $ investis / résultats.


## Comment attirer des ETH&LSD ?

Jusqu'à présent, nous nous sommes concentrés sur les stablecoins à modèle de CDP (Collateralized Debt Position), comme Maker, Liquity ou Reflexer, où les utilisateurs doivent déposer une garantie pour contracter une dette vis à vis du protocole (chaque emprunteur sur un protocole CDP crée sa "propre" dette). Il s'agit d'une conception élégante qui permet au protocole de mettre en œuvre divers dispositifs pour absorber la volatilité du collatéral, maximisant ainsi l'inertie du prix du stablecoin.


### Les limites d'un stablecoin adossé à un CDP

**Il est toutefois difficile, voire impossible, d'atténuer la volatilité d'un collatéral tel que l'ETH sans marge d'erreur**. Par exemple, sur Liquity, le ratio de collatéralisation minimum toléré est de 110%, or le ratio moyen observé sur le protocole est de 226,3%.

La surcollatéralisation, limite principale du modèle CDP, est difficile à surmonter. En effet, l'abaissement de l'exigence de collatéralisation pourrait attirer davantage d'emprunteurs, mais augmenterait également le risque sur le stablecoin produit. Ainsi, la mise à l'échelle d'un stablecoin basé sur un CDP est une tâche difficile. Il existe d'autres idées pertinentes pour attirer davantage d'emprunteurs, comme la diversification de l'offre de garanties, comme indiqué ci-dessous. Mais là encore, cela s'accompagne de risques accrus pour le stablecoin, comme pour le DAI, qui a observé une dégradation importante des garanties au cours de ces dernières années.

Néanmoins, de nombreux projets explorent des approches qui pourraient aboutir à un stablecoin avec moins de compromis que le DAI, tout en atteignant une échelle similaire. Examinons quelques directions actuellement explorées pour faire évoluer le stablecoin décentralisé.


#### Élargir l'offre de garanties et de chaînes : les forks de Liquity

2023 est l'année des forks Liquity : de nombreux protocoles ont été lancés cette année, exploitant un modèle plus ou moins similaire à celui de Liquity, avec quelques modifications. Il s'agit notamment de Gravita, Prisma, Lybra, etc.

##### Gravita Protocol

Commençons par [Gravita](https://www.gravitaprotocol.com/), probablement le plus proche du modèle de base de Liquity. Ici, l'accent est mis sur l'amélioration de l'attractivité du protocole pour les emprunteurs, avec plusieurs ajouts bienvenus, notamment la possibilité d'emprunter en utilisant des ETH liquides comme stETH ou rETH en tant que garantie ou la mise à disposition du protocole sur L2 comme Arbitrum. Bien sûr, il s'agit ici d'un jeu d'équilibre, car la règle spécifiée ci-dessus s'applique toujours.

{{< notice note >}}

**Les conditions imposées aux emprunteurs définissent les garanties fournies aux détenteurs de stablecoins**.

{{< /notice >}}

##### Prisma Finance

[Prisma Finance](https://prismafinance.com/) explore également une approche similaire, il s'agit d'un autre fork Liquity permettant l'utilisation d'ETH-LSD comme collatéral, construit par une équipe proche de l'écosystème Curve/Llama. Des composants de veTokenomics sont également envisagés sur le jeton de partage des frais/gouvernance PRISMA, mais ils doivent encore être mis en place.

##### Lybra Finance

Une autre équipe, [Lybra](https://lybra.finance/), a expérimenté un modèle de verrouillage/escrow sur son jeton de gouvernance LBR. Bien que cela semble avoir bien fonctionné au départ pour attirer une quantité importante de capitaux, le défi avec de telles tactiques est de les maintenir dans le temps...

##### DYAD

Enfin, parlons de [DYAD](https://dyadstable.xyz/). Techniquement, il ne s'agit pas d'un fork de Liquity à proprement parler, mais plutôt d'un protocole inspiré de Liquity, en particulier en ce qui concerne le mécanisme de stabilisation du prix de leur stablecoin.

Le principal problème qu'ils tentent de résoudre est l'intégration de nouvelles garanties dans un protocole CDP actif sans étendre la portée du risque du protocole de base plus qu'il n'est nécessaire. Pour ce faire, DYAD introduit une "couche de licence sociale", essentiellement la couche de gouvernance.

Pourtant, elle ne ressemble en rien à la gouvernance à laquelle nous sommes habitués : ici, il n'y a pas de jeton de gouvernance, de sorte qu'il ne s'agit pas de la ploutocratie habituelle. Au lieu de cela, le pouvoir de gouvernance se trouve directement au sein du dNFT nécessaire pour utiliser le protocole : chaque dNFT contrôle un seul "interrupteur" pour chaque type de garantie proposé. 

Les possesseurs de dNFT peuvent changer la position de cet interrupteur à tout moment, aussi souvent qu'ils le souhaitent. Une garantie donnée peut faire partie du panier de garanties de DYAD si elle conserve une supermajorité de 2/3 de commutateurs "activés". Le seul moyen d'accroître son pouvoir de gouvernance est de contrôler davantage de dNFT.

DYAD obtient également des points bonus pour avoir préservé l'immutabilité autant que possible. Si le protocole peut être modifié puisqu'il peut intégrer de nouvelles garanties, l'ensemble de la couche de gouvernance est immuable. DYAD n'est pas encore live (seulement les dNFTs), mais arrive très prochainement.

Je m’en tiens ici aux principaux acteurs : LSDfi a fait fureur il y a quelques mois, et nous avons vu de nombreux protocoles offrir des options ETH-LSD se lancer récemment. Bien que ce sous-marché soit probablement déjà encombré, il y a de la place pour un modèle basé sur la CDP fournissant un stablecoin légèrement moins résilient que le LUSD mais avec des caractéristiques supplémentaires. La question est de savoir lequel.


#### Soyez doux avec vos emprunteurs : LLAMA/crvUSD

Une autre façon pour attirer beaucoup de ETH / LSD : rendre les conditions plus attrayantes pour les emprunteurs / adoucir les pénalités de liquidation. En effet, l'une des principales innovations de crvUSD réside dans le modèle de liquidation qui diffère grandement des autres services à effet de levier.

Le LLAMA (Lending Liquidating AMM Algorithm) remplace les liquidations habituelles par des "liquidations douces", où les emprunteurs sous-évalués sont rééquilibrés à travers des "bandes", chacune représentant un segment de prix différent.

Elle offre une protection importante contre les liquidations liés aux mouvements de marché brutaux. Au lieu des liquidations soudaines que nous connaissons, les liquidations douces du LLAMA sont plus graduelles, car la garantie est progressivement ajustée en proportion de son prix de marché.


#### Arrosez-les : DSR (DAI Saving Rate) & variantes

Pourquoi se donner la peine d'améliorer la conception d'un stablecoin alors qu'il existe des voies plus directes pour aller de l'avant ? MakerDAO a été le premier à proposer un rendement "sans risque" aux détenteurs de stablecoins pour stimuler la demande : le taux d'épargne du DAI, actuellement de 5 %.

Le maintenir s'avère très coûteux pour la DAO, qui s'oriente vers des garanties lucratives mais plus risquées pour se maintenir à flot. Une part importante des garanties sont désormais des actifs du monde réel (RWA) gérés par des dépositaires, dont certains sont lents, voire ne respectent pas leurs obligations de rendement ou de reporting, ou sont tout simplement sous-optimaux (MakerDAO gagne actuellement 3 % sur son USDC, tandis que [les particuliers peuvent obtenir 5 % avec Circle](https://cryptoslate.com/coinbase-raises-usdc-interest-rate-to-5/)).

Néanmoins, surprise, surprise : les incitations fonctionnent, du moins au début. Ainsi, cette conception brutale, peu contraignante et peu efficace à long terme se répand aujourd'hui :



* [Raft a lancé un concept similaire à 6 %](https://mirror.xyz/0xa486d3a7679D56D545dd5d357469Dd5ed4259340/1qSAAQtVdNCW_xn9cObEjwrQzFpwEshNrm0sjX0nkG8)
* Frax travaille également sur [sFRAX / Frax Saving Rate targeting 5%](https://gov.frax.finance/t/fip-2xx-sfrax-governance-proposal/2585).

![maker-dsr-impact](img/2023/stablecoin-marauder-map/maker-dsr-impact.png "Les incitations fonctionnent...")

L'avenir nous informera sur l'impact d'une telle conception sur le long terme. De mon point de vue, ces protocoles **épuisent la plupart de leurs revenus pour l'acquisition d'utilisateurs sur une base continue** - ils perdront la plupart des utilisateurs acquis avec le DSR à la minute où ils s'arrêteront. Ils auront brûlé une énorme quantité d'argent pour maintenir le cap, de l'argent qui aurait pu, par exemple, être dépensé sur des actifs stratégiques qui fournissent des incitations à vie aux fournisseurs de liquidité. **Cette conception est une excellente tactique, mais c'est l'une des stratégies les plus inconséquentes que je n’aie jamais vues**.


## Vers un stablecoin garanti par des réserves ?

Un changement se prépare ! Alors que les modèles basés sur le CDP, tels que Maker, Liquity ou Reflexer, sont en plein essor, les **monnaies stables garanties par des réserves** sont également de plus en plus considérées.

En effet, comme nous l'avons souligné plus haut, il existe une tension inhérente aux stablecoins purement basés sur l'emprunt / CDP. Pour le dire simplement :



* La mise à l'échelle d'un stablecoin décentralisé basé sur le prêt nécessite d'attirer et de recycler une quantité importante d'ETH / ETH-LSD.
* Mais plus le protocole est permissif à l'égard des emprunteurs, moins le stablecoin qu'il produit est désirable.

L'état d'un stablecoin basé sur un CDP dépend entièrement des actions de ses usagers.
Dans le cadre du modèle de réserve, le protocole gère et frappe directement sa réserve de stablecoins en lieu et place des utilisateurs. Ainsi, les modèles basés sur une réserve offrent une réponse crédible aux lacunes des CDP, et permettent à l'offre de stablecoins d'augmenter potentiellement, grâce à la réserve native qui permet une plus grande inertie du prix.

Résumons cet article en examinant deux excellents exemples de mise en œuvre d'un modèle de stablecoin garanti par des réserves. Je serai bref et fluide, et j'ajouterai des ressources pour aller plus loin.


### f(x) : pas de levier de financement & ETH à volatilité amortie de 90%

F(x) est un protocole fascinant fraîchement sorti ! C’est un produit double, qui permet aux déposants de stETH de s'exposer à deux types d'actifs dans les proportions qu'ils souhaitent :

1. xETH : un "ETH à effet de levier à haute volatilité".
2. fETH : un "stablecoin flottant à faible volatilité".

Comme dans un protocole avec CDP, les utilisateurs déposent de l'ETH (ou du stETH) pour frapper du fETH ou du xETH. Cependant, contrairement à Liquity/Maker/Other CDP, l'utilisateur ne gère pas sa position (un Trove). Au lieu de cela, le protocole gère directement la réserve de stETH. Une fonction de rachat permet aux détenteurs de fETH ou de xETH de récupérer le stETH sous-jacent. Cependant, le montant du rachat dépend de l'état du système, notamment de sa valeur nette d'inventaire : la valeur globale des stETH en réserve.

![protocolfx](img/2023/stablecoin-marauder-map/protocolfx.png)

Lancé il y a quelques semaines, le protocole en est encore à ses débuts avec environ 1300 ETH de TVL, et la liquidité sur fETH est encore en cours d'élaboration. Un troisième jeton, FXN, le jeton de gouvernance du protocole, est également prévu. 

La proposition de valeur de xETH et fETH est pertinente à mes yeux et devrait répondre à la demande une fois que le protocole sera plus mature. À mon avis, avec le crvUSD, c'est l'une des nouveautés les plus excitantes que nous ayons eues cette année dans le domaine des stablecoins : j'attends juste le bon moment pour expérimenter xETH.


### Liquity v2 : levier efficace et protégé

"Liquity v2" (nom de code) n'est pas encore opérationnel mais a été [présenté par Robert Lauko lors du dernier Stable Summit en juin](https://www.youtube.com/watch?v=Zps__IMxtTs).

Comme fETH, v2 offrira un effet de levier non liquidable sur les LSDs d'ETH sans frais de financement et ajoutera même une protection à la baisse. Ce nouveau stablecoin sera adossé à une réserve facilitant son développement et sa croissance. Ses besoins en liquidités sont également minimisés puisque le protocole agit comme un AMM primaire pour le stablecoin : les utilisateurs peuvent frapper et échanger le stablecoin pour 1 $ d'ETH.

La V2 est construite en public : si vous souhaitez en savoir plus ou même vous impliquer, n'hésitez pas à venir sur le [canal Discord de Liquity dédié à la v2](https://discord.gg/RCRp2CJR2S).


### En savoir plus sur AladinDAO's F(x) & Liquity V2

J'ai fait court sur les stablecoins garantis par des réserves, car je publierai probablement plusieurs articles sur ce sujet dans les mois à venir. En attendant, n'hésitez pas à obtenir votre alpha directement de la bouche des créateurs - voici une sélection d'articles et d'interviews pour en savoir plus sur les deux protocoles :



* [Un appel récent de la communauté, lorsque Robert et moi avons rejoint l'équipe AladinDAO/Protocol F(x) pour discuter plus largement des stablecoins décentralisés [60min]](https://twitter.com/aladdindao/status/1684141750900736000?s=20)
* [Community Call - Deep Dive into f(x) [30min]]](https://www.youtube.com/watch?v=_xA6AFufGoQ&t=3871s)
* [Protocole f(x) avec Kmets et Crouger de AladinDAO(Leviathan News) [28min]](https://www.youtube.com/watch?v=Nzy7xO09SFw)
* [Présentation de Liquity v2 - Liquity Blog](https://www.liquity.org/blog/introducing-liquity-v2)
* [Liquity v2 avec Colin Platt (Leviathan News)](https://www.youtube.com/watch?v=KOnGCPE5gaU)


## LES PRINCIPAUX ENSEIGNEMENTS

La gestion de la liquidité est le nerf de la guerre des stablecoins : observez et analysez les stratégies déployées par les projets que vous suivez - leur efficacité est l'un des principaux moteurs du succès du protocole sous-jacent.

**👉️ TODO:** Suivez l'événement entourant la gestion des liquidités de GHO sur [Aave Governance Forum](https://governance.aave.com/) et essayez de structurer votre thèse. Si vous pouvez anticiper le repeg avec précision, vous obtenez 3% de profit gratuit qui vous attend (GHO ~$0.97 à $1.00).

**👉️ BONUS-TODO:** GRAI, un autre stablecoin (Liquity fork), se négocie actuellement à ~$0.985 avec son plafond de rachat augmentant au cours des prochaines semaines ; un jeu similaire peut être envisagé ici.

LSD-FI (protocoles pour tirer parti de LSD) a été surchargé au cours des derniers mois. La plupart des protocoles de cette catégorie sont en perte de vitesse.

**👉️ TODO:** Examinez la structure d'incitation de protocoles tels que Gravita, Raft ou Lybra, et confrontez-la à leurs mesures de croissance - essayez d'évaluer la structure d'incitation qui semble persistante par rapport à celle qui est en perte de vitesse.

Après 4 ans de repli sur le modèle basé sur les CDP, il semble que les équipes les plus avisées aient commencé à chercher une autre voie.

**👉️ TODO:** Préparez l'avenir ! Grâce aux ressources partagées ci-dessus, approfondissez les modèles de stablecoins basés sur les réserves en vous familiarisant avec des protocoles tels que f(x) ou v2.

{{< notice info >}}

Un grand merci à Arem qui s'est chargé de la traduction de cet article. Arem contribue activement à la communauté DeFi France et est impliquée dans de nombreuses initiatives : faites comme Arem, **[suivez Arem](https://twitter.com/aremd_)**, et dites-le lui si cette traduction vous a été utile !

{{< /notice >}}

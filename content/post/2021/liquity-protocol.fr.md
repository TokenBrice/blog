---
title: "⚖️ Liquity : un service d'emprunt inarrêtable, efficace et innovant"
description: "Liquity est le premier service d'emprunt qui opère sans avoir besoin de gouvernance, tout en étant peu coûteux et très efficace. J'explique le protocol pour comprendre comment il innove et ce qu'il apporte à la DeFi."
date: '2021-11-30T01:13:50.191Z'
categories: [DeFi, Comprendre]
tags: [DeFi, Ethereum, Finance décentralisée, Stablecoins, Actifs stables, Marchés Monétaires, Liquity, LUSD, LQTY]
toc: true
tocNum: false
url: liquity-protocol
image: /img/2021/liquity-protocol/cover-en.png

---

[Liquity](https://www.defiscan.info/protocols/liquity/ethereum) est un protocole encore unique en son genre : il permet l'emprunt sur ETH et le mint d'un stablecoin (LUSD) sans pour autant nécessiter de gouvernance ce qui le rend "inarrêtable".

Le terme n’est pas toujours bien compris, alors explicitons : les contrats nécessaires à l'existence de Liquity et du LUSD ont été déployés et comme ils n’ont pas de fonctions administratives, **rien ne peut les arrêter tant que le réseau Ethereum se synchronise**.

Si cela ne suffit pas à exciter votre curiosité, la bonne nouvelle c'est que pour arriver à un tel résultat, Liquity met en œuvre plusieurs nouvelles idées vraiment pertinentes. En effet, outre sa résilience, Liquity est aussi **le protocole le moins coûteux** pour des emprunts long termes sur ETH et également **le plus permissif en levier**, hors “recovery mode”.

Le but de cet article est donc de présenter Liquity tout en explicitant plusieurs dimensions critiques pour tout service de prêt / marché monétaire en DeFi.


---

## FONCTIONNEMENT DU PROTOCOLE

Je vous propose un tour exhaustif du protocole pour en comprendre les enjeux et contributions apportées à la DeFi. Idéalement, il s'agirait de comprendre toute la dynamique. Je réalise cependant que mes explications peuvent être parfois denses, je vous les propose donc par niveau de complexité :


### 🏗 Les fondamentaux de Liquity

À un haut niveau, Liquity fonctionne dans une logique similaire à Maker: les utilisateurs créent des "Troves" où ils peuvent déposer des ETH afin d'emprunter des stablecoins, les LUSD, directement au protocole.


#### Marché monétaire ou service d'emprunt ?

Liquity tout comme Maker sont des services d'emprunt mais pas des marchés monétaires. La différence ? Qui est-ce qui vous prête ? 
1. Soit le protocole directement (service d’emprunt), 
2. Ou alors d'autres utilisateurs via un modèle de pooling comme Aave ou Compound (marché monétaire).

La différence est extrêmement importante au niveau de la compétitivité du protocole : **il est quasiment impossible, même théoriquement, d'envisager un marché monétaire proposant des coûts d'emprunts sur les stablecoins bas (&lt;3 % annuel) de manière durable**.

En effet, les marchés monétaires doivent offrir un rendement attractif à leurs déposants en stablecoins, qui disposent de très nombreuses alternatives pour produire du rendement. Ainsi, **si l'efficacité est un objectif essentiel, le modèle du service d'emprunt qui ne nécessite pas de dépôts d’autres utilisateurs est foncièrement plus efficace** - l'utilisateur emprunte directement au protocole à un coût plus faible.

Enfin pour conclure, éprouvons la théorie à la dure absurdité de la pratique : ces considérations sont valables pour analyser le design d'un marché monétaire / service d'emprunt. Il existe **des services d'emprunts (à priori donc très efficaces) qui arrivent malgré tout à être coûteux pour les emprunteurs, comme MakerDAO**. Les raisons sont diverses, mais le fait que la DAO décide encore les frais du protocole (de manière potentiellement totalement arbitraire) me semble l'une des principales.


#### Emprunter avec Liquity

Du point de vue d'un utilisateur potentiel, Liquity fonctionne donc comme une alternative à Maker ou autre : l'utilisateur arrive avec des ETH qu'il dépose dans son trove pour frapper le montant de LUSD désiré.

Néanmoins, le parallèle s'arrête ici car bien qu'à haut niveau le processus soit similaire, la logique sous-jacente est totalement différente.


##### Gestion des frais

Tout d'abord, le nerf de la guerre : les frais d'emprunt. À ce sujet et outre des coûts absolus d'emprunt très bas, Liquity a le mérite d'apporter de **la prédictibilité et de la clarté.** En effet, là où Maker, Aave et Compound par exemple pratiquent un taux annuel variable (via gouvernance pour Maker, conditions du marché pour Aave/Compound), **chez Liquity le taux est fixé et annoncé clairement à l'emprunt**.

En outre, chez Liquity les frais se paient en une fois, lors de la mise en place de l'emprunt : ce sont les “**initiation fees”, par défaut à 0.5%. Ce sont les seul frais que l'emprunteur paie, même s'il garde son trove pendant des années.**

![liquity-trove](/img/2021/liquity-protocol/trove.png "Ouverture d'un trove sur Liquity")


C'est pourquoi Liquity est **idéal pour les positions à long terme**, de tels coûts d'emprunt sont effectivement 5-10x inférieur à ce qu’on peut trouver sur les principales alternatives.


#### Stability pool : réserve de liquidité pour liquidations (backstop)

Si le modèle de Liquity apporte déjà des bénéfices pertinents dans la perspective d'un utilisateur, sa conception explore également des solutions pertinentes. 

L'un des principaux enjeux pour les services d'emprunts c'est bien sûr que le protocole reste solvable : il y a donc, si nécessaire, des liquidations pour rétablir l'équilibre. Liquider des positions nécessite des fonds propres à disposition et une certaine infrastructure lorsque ce sont les utilisateurs qui le font directement, comme sur Marker ou Aave. Pour optimiser le processus, l'idée d'un "**backstop**" de liquidité a émergé.

Il s'agit d'avoir **une réserve de fonds, généralement des stablecoins que le protocole utilise si nécessaire pour gérer les liquidations** : c'est la Stability Pool sur Liquity. Les utilisateurs qui le souhaitent peuvent déposer leur LUSD dans cette pool : ils sont rémunérés en LQTY (qu'on détaille juste après). 

Les fonds de la Stability Pool sont utilisés lorsque cela est nécessaire pour les liquidations. Le système étant désormais assez mature, les liquidations ont surtout tendance à arriver en cas de forte baisse rapide du prix de l'ETH. Une position dans la stability pool permet donc de profiter de ces juteuses liquidations sans avoir les compétences ou l'infrastructure nécessaire pour les exécuter.

 

La Stability Pool offre ainsi une option de rendement native sur le LUSD plutôt légère du point de vue du gas et assez attractive. Avec un ratio de collatéralisation prudent, cela peut même convenir pour une position presque entièrement passive.

Bien que le concept de backstop ne soit pas implémenté nativement sur les autres principaux marchés monétaires, [le projet B.Protocol](https://www.bprotocol.org/) agit comme une couche d'abstraction proposant l'équivalent de ce service à Maker, Aave et Compound (sans les bénéfices à l'avoir en interne).


#### Token LQTY & staking

Je vous le disais plus haut : Liquity n'a pas de gouvernance. Le système s'ajuste automatiquement en fonction de différents paramètres observés sur les marchés comme on le verra plus bas. Mais alors, à quoi sert LQTY ?

Dans sa forme la plus basique, c'est un mécanisme comptable qui permet d'allouer les revenus générés par le protocole. LQTY peut être staké pour obtenir des LUSD correspondant à sa part des frais d'initiation et des ETH en provenance des frais de redemption :


![lqty-staking-returns](/img/2021/liquity-protocol/lqty-staking-returns.png "Revenus pour les stakers LQTY")

Voilà pour les points essentiels sur Liquity et ses principales différences avec les solutions existantes. Néanmoins comme toujours le diable est dans les détails, donc maintenant que les bases sont établies je vous propose d'explorer les arcanes du protocole.

---

### 🧙 Compréhension aboutie et utilisation avancée

Jusqu'à présent, on est resté autant que possible dans la perspective d'un utilisateur potentiel. Pour cette section, il va falloir élargir nos horizons pour cerner toute la subtilité de la conception de Liquity. C'est parti !


#### Limites et risques du modèle

Maintenant que j'ai votre attention, parlons des risques : ça fait aussi partie des subtilités à connaître pour comprendre et tirer profit de Liquity.


##### 🔮 Dépendance à l'oracle

Si vous me lisez depuis un bout de temps, cette phrase vous dira sans doute quelque chose : "**la vérité sur les marchés monétaires, c'est ce que l'oracle dit**". L'oracle est le dispositif qui permet d'obtenir des données nécessaires on-chain, pour être utilisé par des smart contracts. La donnée critique en question ici c'est le prix d'ETH en USD, qui permet de déterminer si une position donnée est solvable ou doit être liquidée.

En l'occurrence, le choix est classique : le flux principal utilisé est [ETH/USD ChainLink](https://data.chain.link/ethereum/mainnet/crypto-usd/eth-usd), avec un fallback sur Tellor ([plus d'infos](https://docs.liquity.org/faq/stability-pool-and-liquidations#what-oracle-are-you-using-to-determine-the-price-of-eth)). ChainLink est très répandu et robuste, mais il faut être conscient du fait qu'un problème avec le flux ETH/USD ChainLink peut rapidement entraîner des conséquences graves sur Liquity (et à peu prêt toute la DeFi).


##### ⚖ Le LUSD contre son peg de $1 

LUSD est un stablecoin, c'est super de le minter directement pour pousser le plus possible vers le bas les coûts d'emprunt. Mais quid de la stabilité du LUSD ?


Le pegging de stablecoin, c'est une science assez dense, on ne va pas forcément faire le détail, juste les grandes lignes. Le LUSD a différentes caractéristiques qui lui permettent a priori d'établir un plancher ainsi qu'un plafond via les arbitrages :

* Plancher : le mécanisme de rédemption : un LUSD peut être racheté contre de l'ETH via un mécanisme qu'on explore juste après
* Plafond : le protocole garantit en toutes conditions une collatéralisation absolument minimale du LUSD par de l'ETH à 110%

Ainsi, bien que le LUSD tient relativement bien son peg à $1, on observe des fluctuations d'amplitude plus conséquentes que sur un stablecoin centralisé.

![lusd-price](/img/2021/liquity-protocol/lusd-price.png "Valeur du LUSD sur 90 jours")


Différentes situations extrêmes au niveau du marché (et donc du protocole) peuvent également amener à envisager un LUSD qui s'écarte plus ou moins durablement du peg. Dans l'ensemble, les mécanismes de stabilisation sont là pour ramener l'équilibre sur le long-terme.


#### Un jeu "protocol-level"

Liquity nous amène à une notion très intéressante que j'appelle "protocol-level", faute de mieux. Il s'agit des interactions possibles avec le protocole dont les conséquences dépendent des actions des autres joueurs.

En quelque sorte et pour reprendre ma métaphore favorite des MMORPGs :



1. **PvE = le joueur se bat contre des monstres (IA)**, en DeFi : farming simple & conséquences des autres joueurs seulement secondaires (ex dilution du yield quand une 🐳 arrive)
2. **PvP = les joueurs se castagnent directement entre eux** et ça, ça ne manque pas même en DeFi !
3. Mais le plus intéressant aujourd'hui c'est surtout **le RvR (Royaume contre Royaume)**. Là encore il y a bien castagne entre joueurs, mais c'est **une lutte structurée par faction**, avec des objectifs à atteindre. L'équivalent DeFi ici c'est bien sûr le jeu des gauges CRV sur Curve !

On observe ainsi sur Liquity des mécaniques "protocol-level" qui pourraient s'apparenter à du RvR dans cette métaphore, voyons donc comment elles fonctionnent :


##### Taux d'initiation/redemption dynamique

Tout d'abord, le plus basique : les frais. Je vous parlais plus haut d'un frais d'initiation à 0.5% : c'est vrai, mais légèrement simplifié. En réalité ce taux peut évoluer entre 0.5% et 5% : c'est le `baseRate` qui gouverne le frais payé à la fois sur les emprunts et les redemptions.

Lors d'une forte utilisation de Liquity, le `baseRate` augmente. C'est également un mécanisme défensif pour le protocole, qui sans ça, pourrait se faire "vider ses ETH" par des arbitrageurs (redemption massive LUSD->ETH). Le taux "decay" lorsque l'utilisation se calme pour revenir gentiment à 0.5% et je vous laisse aller voir [les maths derrière tout ça](https://docs.liquity.org/faq/lusd-redemptions#how-is-the-baserate-calculated) sur la doc pour les curieux. 

{{< notice note >}}
Comme le déposant paie ses frais au moment de l'emprunt sur Liquity, l'évolution du taux par la suite n'a pas de conséquence pour lui.
{{< /notice >}}

##### "Recovery Mode" : aussi terrifiant qu'efficace ?

En utilisation normale, **Liquity est le protocole le plus permissif pour leverager sur ETH, tolérant un ratio de collatéralisation aussi bas que 110%** (~90% de la valeur nette du collatéral est empruntée). C'est sans commune mesure avec ce qu'on trouve ailleurs en DeFi, quelques références sur ETH :


* Maker propose des ratios de collatéralisation allant de 58,8% pour ETH-C à 76,9% pour ETH-B (min collateral ratio de 130% à 170%)
* Aave est à 82.5% sur ETH 
* Compound à 75%


Si le protocole peut être aussi permissif, ce n'est pas parce qu'il prend plus de risques, mais plutôt parce que plusieurs solutions sont implémentées pour pousser les utilisateurs à re-collatéraliser lorsque cela est nécessaire : le recovery mode et les redemptions.

![recovery-mode](/img/2021/liquity-protocol/recovery-mode.png)


Le recovery mode est un jeu protocol-level sur Liquity : son déclenchement dépend du "Total Collateral Ratio" du protocole : le ratio entre l'ensemble des collatéraux et les LUSD dûs. 

Lorsque celui-ci passe **sous la barre des 150%, le Recovery Mode s'enclenche pour rétablir l'équilibre** : le seuil minimal de collatéralisation pour un trove passe à 150%. Les utilisateurs à risques sont ainsi invités à re-collatéraliser ou rembourser de la dette - et/ou seront liquidés si nécessaire lors de la mise en route du recovery.

La mise en route du recovery mode ne se fait néanmoins pas par surprise, puisqu'elle dépend d'un paramètre que tout le monde peut suivre aisément. Un tel système permet de maximiser l'efficacité du protocole la plupart du temps, tout en revenant rapidement vers des paramètres plus conservateurs si cela est nécessaire.


##### Le jeu des redemptions

Enfin, il reste une dernière mécanique à détailler : les rédemptions, un mécanisme d'arbitrage pour échanger des LUSD contre des ETH.

Là encore, il s'agit d'un jeu protocol-level : les rédemptions se font en utilisant la liquidité disponible dans les troves des utilisateurs. **Lorsqu'il y a redemption, le protocole commence par utiliser la liquidité du trove le moins collatéralisé sur Liquity** et remonte autant que nécessaire.

Ainsi, être **le** trove le moins collatéralisé de Liquity n'est pas une position très envieuse, puisque votre collatéral est à risque de servir pour les rédemptions. Si c'est le cas, l'utilisateur perdra des ETH, mais il verra aussi sa dette diminuer (proportionnellement aux LUSD échangés).

Ce mécanisme pousse les joueurs à rester raisonnable, même lorsque le recovery mode n'est pas activé : pour éviter les rédemptions, il ne faut pas être le plus agressif. C'est en quelque sorte **un mécanisme de régulation dont le seuil exact dépend de l'appétit moyen pour le levier des autres joueurs** : autrement dit une conception des plus élégantes.


##### Décentralisation des front-ends

Enfin, c'est peut-être un détail pour vous mais pour moi ça veut dire beaucoup : **l'équipe de Liquity n'opère pas le site de l'application**. À la place, elle a mis à disposition un [SDK Frontend](https://docs.liquity.org/documentation/sdk) pour aider d'autres développeurs à opérer eux-même une instance d'un front-end Liquity. Il y a également un mécanisme de kickback pour inciter ces intégrateurs.

Cette approche permet à Liquity d'**aller encore plus loin que les autres protocoles en termes de décentralisation** et d'offrir de solides garanties qu'au moins un des front-ends restera disponible quoiqu'il arrive.

**Cette spécificité de Liquity est à l'image du reste du protocole : une approche innovante, différente, et réellement pertinente que vous ne pouvez tout simplement pas ignorer.**

---

## Liquity et LUSD dans l'écosystème DeFi

J'ai écrit cet article car je considère Liquity comme une primitive DeFi essentielle et j'aimerais vous aider à comprendre pourquoi. Je ne suis pas le seul à saisir ce qu'il se joue ici, de nombreux protocoles s'intéressent à Liquity et au LUSD d'une façon ou d'autre autre. Voyons ça.


### Intégrations DeFi Liquity

Il y a tout d’abord les différents protocoles qui intègrent une ou plusieurs parties de Liquity et offrent ainsi de nouvelles opportunités aux possesseurs de LQTY ou LUSD.


#### Liquidité LUSD/LQTY et farming

[Harvest Finance](https://harvest.finance/) propose ainsi un vault LQTY qui s’appuie sur le staking : les LUSD et ETH obtenus sont fréquemment composés pour plus de LQTY.

[Pickle Finance](https://app.pickle.finance/farms) propose un produit similaire (pJar 0.98l) ainsi qu’un vault particulier en partenariat avec B.Protocol pour maximiser les LQTY obtenus :


![pickle-lusd](/img/2021/liquity-protocol/pickle-lusd.png "Vault LUSD B.Protocol sur Pickle Finance")


La source principale de liquidité pour LUSD c’est [la pool Curve](https://curve.fi/lusd), disponible  également avec Convex.

Côté liquidité sur le token LQTY, la situation est plus tendue mais s’améliore depuis le lancement du vault Uniswap V3 géré par [Visor](https://www.visor.finance/) qui offre également une nouvelle option pour farmer avec LQTY.


![visor-uni-lqty](/img/2021/liquity-protocol/visor-uni-lqty.png)


Liquity est également supporté sur [DeFiSaver](https://defisaver.com/), pour gérer plus aisément le levier et protéger les troves.

Voilà pour le tour d’horizon rapide des principales intégrations. Les DAOs s'intéressent également au LUSD car c’est le seul stablecoin inarrêtable.

---

### LUSD : un snack pour trésorerie de DAO ?

Les propriétés inhérentes du LUSD lui ont déjà valu de l’attention en DeFi. Par exemple, après avoir accumulé beaucoup de liquidité sur DAI et FRAX, Olympus s’est tourné vers LUSD avec l’accumulation de LUSD et LP Sushi LUSD/OHM via le mécanisme de bonds. LUSD est désormais un des principaux actifs possédés par OlympusDAO ([stats](https://dune.xyz/shadow/Olympus-(OHM))).


![olympus-lusd](/img/2021/liquity-protocol/olympus-lusd.png)


Les ohmies ne vont pas s’arrêter là : ils adorent les actifs productifs, et Liquity n’en manque pas : [le plan](https://forum.olympusdao.finance/d/177-tap-5-whitelist-liquity-lusd-stability-pool-and-lqty-staking) est donc que le protocole déploie ses LUSD dans la Stability Pool pour accumuler des LQTY qui seront également stakés.

Il y avait même du liquidity mining classique sur la paire LUSD/OHM, mais revisité. Avec le [Crucible ](https://crucible.alchemist.wtf/)d’Alchemist, un smart contract wallet NFT pour gérer facilement ses positions LP, un [programme de 35 jours ](https://www.liquity.org/blog/how-to-earn-rewards-on-the-lusd-ohm-pool-using-alchemists-crucible)était proposé, avec des récompenses en OHM, LUSD et MIST.

 \
D’autres protocoles en quête de résilience, diversification et stabilité pour leur trésorerie ont également franchi le pas :



* Fei, un protocole proposant un autre type de stablecoin, a diversifié son collatéral vers LUSD et compte désormais plus de 50 M LUSD : [Analytics Fei Money](https://app.fei.money/analytics)
* L’équipe de Synthetix s’intéresse également à amener le LUSD sur Optimism, qui pourrait aider pour stabiliser sUSD avec [le wrapper LUSD/sUSD](https://gist.github.com/kaleb-keny/33fd792ac52a70fdf4de00b8830569a4).

[Le top holder LUSD ](https://etherscan.io/token/0x5f98805A4E8be255a32880FDeC7F6728C6568bA0#balances)compte ainsi déjà plusieurs DAOs et **tout comme pour RAI** je pense que la tendance peut s’accentuer :

![lusd-holders](/img/2021/liquity-protocol/lusd-holders.png "Les 15 plus gros holders LUSD sur EtherScan")


D’autres intégrations sont encore envisageables, comme par exemple l’intégration directe de la stability pool sur une pool fuse pour permettre une utilisation plus optimale des actifs de la stability pool.

J’espère que cet article aura su éveiller votre curiosité DeFi : Liquity est disponible depuis Avril dernier et pourtant bien peu encore réalisent l'élégance et le minimalisme de ce protocole qui propose des solutions crédibles à de véritables enjeux.

Pour aller plus loin, y’a pas de secrets :

* [La documentation](https://docs.liquity.org/)
* [Le discord](https://discord.gg/j7hHaR4G6S)
* Et pour creuser, je vous propose ce live récent où je discute d’emprunts en DeFi : 

Have fun !

{{< youtube LXDSxRCMsDE >}}

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

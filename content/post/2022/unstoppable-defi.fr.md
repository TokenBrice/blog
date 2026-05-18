---
title: "Dans les coulisses du théâtre de la décentralisation : étude de l’inaltérabilité des protocoles DeFi"
description: "De la centralisation totale aux protocoles inarrêtables : définition et analyse du spectre des différents niveaux de résilience des protocoles DeFi"
date: '2022-05-18T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Analysis]
tags: [DeFi, Ethereum, Stablecoins, Stable Assets, Money Markets, Liquity, LUSD, LQTY, Curve, Uniswap, PoolTogether, Chainlink, Oracles]
toc: true
tocNum: true
url: unstoppable-defi
image: /img/2022/unstoppable-defi/unstoppable-defi-tokenbrice-cover.png
difficulty: "expert"
---

La finance décentralisée a permis l’émergence de protocoles autonomes dont les fonctionnalités sont assurées par des smart contracts parfois immuables, permettant à des individus du monde entier d’utiliser des services financiers tout à la fois souverains, accessibles mais aussi plus efficaces et résilients que ceux disponibles en finance classique. Voilà la belle histoire qu’on raconte aux nouveaux arrivants pour les endormir : la réalité est bien plus nuancée.

Effectivement, il y a bien **une poignée de protocoles qui correspondent à cette réalité,** mais la plupart sont loin d’être à la hauteur. Quand les taureaux sont de sortie, l’intérêt pour la résilience des protocoles est généralement très faible : la seule chose qui importe ce sont les appréciations de prix. Mais les ours ont fait leur grand retour, et avec vient heureusement un regain d’intérêt pour ces sujets.

L’implosion récente de l’écosystème Luna et de son stablecoin associé, UST, aura, je l’espère, servi de piqûre de rappel pour certains. C’était hélas une catastrophe **parfaitement évitable**. Le modèle utilisé pour ce stablecoin et ses défauts étaient déjà connus, avec de nombreuses précédentes instances couvertes à l’époque sur ce blog : BAC, MIC, ESD, DSD, etc. (au niveau applicatif sur Ethereum plutôt que protocolaire, mais avec les mêmes problèmes de fond). Tous ont connu la même fin : une spirale interminable qui les amène toujours plus proche du 0 absolu.


Face à cet événement, de nombreux investisseurs ont pris conscience que tous les Stablecoins ne se valaient pas et cherchent à se renseigner davantage sur la résilience des nombreux Stablecoins disponibles sur le marché ainsi que la robustesse de différents protocoles DeFi en général. Je saisis donc ce moment exceptionnel pour discuter de ce sujet essentiel pour la pérennité de la DeFi qui me passionne depuis longtemps.

En effet, l’année dernière je vous proposais déjà une analyse exhaustive des risques encourus sur les services d’emprunts en DeFi et comment les évaluer. **[Cet article](https://tokenbrice.xyz/fr/marche-monetaire-risque/)** est toujours d’actualité et sa lecture est fortement recommandée pour tout investisseur avisé.

Trêve d’introduction, venons au fait, en commençant par définir le terme "inarrêtable" et ce qu’il implique concrètement au niveau d’un protocole.


## Qu’est-ce qu’un protocole DeFi inarrêtable ?

Au niveau le plus basique, on peut qualifier **un protocole DeFi d’inarrêtable[^précisions-d’inarrêtable] lorsque ses fonctions essentielles sont assurées par des smart contracts qui ne sont pas modifiables et qu’il ne requiert pas d’intervention externe pour subsister.**

À cette définition plutôt simple et directe, je dois néanmoins ajouter de nombreuses notes et précisions pour couvrir la diversité des protocoles DeFi et des cas d’utilisation qu’ils desservent.


### ⚠️ Dépendances tierces des protocoles

En DeFi, il est extrêmement rare qu’un protocole fasse tout par lui-même. Le plus souvent, un protocole donné s’appuie sur différents protocoles tiers. Le cas le plus courant et le plus connu est bien sûr celui de l’oracle – la source de prix pour les actifs – un élément essentiel pour les services d’emprunts notamment.


#### Dépendance aux oracles comme ChainLink

En la matière, l’oracle le plus utilisé est [ChainLink](https://www.defiscan.info/protocols/chainlink-oracles/ethereum). Bien que techniquement robuste, l’industrie a eu récemment droit à un rappel grâce à Chris Blec et quelques autres acteurs soucieux de la résilience du service : les oracles de ChainLink sont susceptibles d’être manipulés ou censurés. Le vecteur d’attaque le plus risqué semble être **la multisig 3/20** qui permet de changer immédiatement la source de prix pour un actif donné.

Concrètement, cela signifie que si 3 personnes se synchronisent parmi ces 20, ils pourraient changer l’oracle ETH/USD par exemple pour un oracle maison qui retourne un prix de $1 et quasiment tous les prêts DeFi seraient liquidés dans la foulée. Il semble assez peu probable néanmoins que des gens membres de l’équipe ChainLink ou proches de celle-ci réalisent une telle attaque.

Le plus gros risque semble donc être au niveau d’une attaque perpétrée par un acteur externe qui voudrait nuire à l’ensemble de la DeFi. En effet, avec une multisig aussi permissif, il “suffirait” d’identifier 3 membres ou plus de ce multisig, les kidnapper et les menacer pour changer une source de prix de ChainLink. C’est la fameuse “🔧 wrench attack” : qu’importe la sécurité des smart contracts, s’ils sont administrés par une multisig, ils sont vulnérables à ce type d’attaque qui passe par les personnes derrière les protocoles plutôt que le code directement.

L’essentiel du problème ici ce n’est pas l’existence de ce multisig, nécessaire pour mettre à jour et améliorer les services que ChainLink apporte, mais son paramétrage :

1. 3/20 c’est extrêmement permissif et plus risqué d’un point de vue 🔧 wrench attack que 3/6 par exemple (qui aurait moins de cibles potentielles pour réaliser l’attaque). Un nombre plus raisonnable et aligné avec ce qu’il se fait habituellement pour 20 signataires au total serait quelque chose entre 8 et 12 requis.
2. Absence de timelock : les changements sont donc immédiats.

**⚠️ Mise à jour - 27 Mai** : Le 23 Mai (5 jours après la publication de cet article), la paramétrage de la Multisig a évolué pour devenir 4/9, offrant une meilleure protection contre les 🔧 wrench attack, mais il n'y a toujours pas de timelock.[^chainlink-multisig].

#### Dépendance à d’autres protocoles moins résilients que le protocole de base

Un des éléments les plus fascinants en DeFi, c’est la composabilité : les protocoles s’intègrent et s’utilisent les uns et les autres. Si cela permet l’émergence de synergies et de cas d’utilisation innovants, cela vient également avec des risques additionnels.

Sans trop le détailler, puisqu’on y reviendra ensuite, on va prendre en exemple ici PoolTogether, un des protocoles les plus résilients de la DeFi et quasi–inarrêtable. Le quasi, il le doit à ses dépendances externes et plus précisément les sources de rendement utilisées : Compound ou Aave.

En effet, les smart contracts de PoolTogether sont totalement immuables sauf pour la partie qui gère l’allocation des prix (v4), mais les fonds sont déployés dans des protocoles qui sont eux alimentés par des smart contracts pouvant  être modifiés (nécessaire, par exemple, pour l'ajout d'un nouveau collatéral mais c'est aussi un vecteur d'attaque potentiel et un risque réel, cf xSUSHI sur Aave[^aave-xSUSHI])

**La règle générale, c’est qu’un protocole est aussi résilient que le maillon le plus fragile de sa chaîne de composabilité**. Cette règle n’est pas absolue, car il reste possible de mitiger ou de contenir l’exposition prise avec une intégration, en implémentant par exemple de la redondance, comme on le verra plus bas lors des analyses détaillées.


### ⚠️ Accès aux protocoles : la question des sites webs (front-end)

Sur ce sujet, deux questions essentielles se posent :

1. Le point d’accès au protocole (= le site web / front-end) est-il résilient / peut-il être censuré, par exemple par un acteur étatique ?
2. Le site est-il sécurisé ? Peut-il être attaqué par un acteur malveillant ?

#### Risque de censure des front-end

Ici, il faut commencer par rappeler un point absolument fondamental : un service DeFi existe grâce à un jeu de smart contracts. Il est **tout à fait possible d’interagir avec n’importe quel service DeFi en passant directement par les contrats** – et donc, même si leur site venait à être inaccessible. Bien sûr, tous les utilisateurs de la DeFi n’ont pas la compétence technique pour interagir avec des smart contracts directement, et c’est pourquoi **la question des front-end reste importante**.

Ainsi, les protocoles qui tiennent à maximiser leur résilience se doivent de réfléchir à cette question. Il y a ici deux approches principales qui peuvent être cumulées.

Tout d’abord, un protocole peut avoir **plusieurs points d’accès** qui permettent l’accès à son service : si l’un d’eux venait à être inaccessible, d’autres resteront en ligne, n’entraînant ainsi qu’un désagrément mineur pour les utilisateurs du service. Par exemple, [Aave](https://www.defiscan.info/protocols/aave/ethereum) peut être utilisé via le site principal app.aave.com, mais également grâce à des outils comme [DeFiSaver](https://defisaver.com/), [InstaDapp](https://instadapp.io/) et de nombreux autres.

Néanmoins, la plupart de ces sites restent hébergés par des **services centralisés** qui pourraient tous être censurés en même temps : c’est plus de travail, mais c’est techniquement possible. Pour remédier à cette limite, il reste une autre option : avoir un ou plusieurs **sites hébergés via une solution décentralisée comme [IPFS](https://ipfs.io/)**.

Pour finir, en matière de résilience du front-end, la palme de l’approche la plus originale, élégante et efficace déployée à ce jour reste sans doute celle du protocole [Liquity](https://www.defiscan.info/protocols/liquity/ethereum). En effet, Liquity n’a pas de site officiel pour son application déployé et géré directement par l’équipe. À la place, l’équipe fournit **un kit pour déployer un front-end** de Liquity, utilisable par tous. Cela permet au projet d’avoir [une myriade de sites différents permettant d’utiliser son service](https://www.liquity.org/frontend), dont certains sont hébergés sur IPFS :

![some-liquity-frontends](/img/2022/unstoppable-defi/liquity-frontend.png "Aperçu des différents front-end pour utiliser Liquity (parmi >20)")


#### Risques de sécurité des front-end

Enfin, il ne faut pas oublier qu’aussi résilient que les smart contracts puissent être, un front-end reste un site web qui même s’il n’est pas censuré **peut être susceptible de subir des attaques** plus ou moins conséquentes : les sites des échanges décentralisés SpiritSwap ou bien encore QuickSwap ont par exemple récemment [fait les frais d’un tel scénario](https://twitter.com/QuickswapDEX/status/1525306033400188928?s=20&t=UKpcM2Gu6nZ9Kgl65kmp3w).

En l’occurrence, le vecteur d’attaque est lié au gestionnaire de nom de domaine (GoDaddy) utilisé par le service. D’autres types d’attaques sont envisageables : par exemple, les injections de code par le biais d’un service tiers que le site intègre, comme on a également pu le voir très récemment sur EtherScan et de nombreux autres sites à la suite de la compromission du tracker publicitaire utilisé (CoinZilla).


### ℹ️ Limites des protocoles inarrêtables

Tous les cas d’utilisation ne peuvent pas être couverts par des protocoles inarrêtables. En effet, en fonction de la complexité d’un protocole, il est parfois impossible d’éviter toute dépendance à un autre protocole lui-même censorable au moins en partie.

Enfin, il faut également garder en tête la contrepartie qui vient avec l’immutabilité des smart contracts des protocoles inarrêtables : **une mise à jour de ceux-ci est techniquement impossible**.

Ainsi, lorsqu’un protocole inarrêtable doit évoluer, il n’y a qu’un seul chemin possible : déployer une nouvelle version du protocole (avec son nouveau jeu de contrats immuables) et encourager la **migration** de ses utilisateurs vers celle-ci. C’est par exemple ce qu’a fait Uniswap à deux reprises, avec la migration vers la version 2 en Mai 2020[^UNIv2] puis un nouvelle fois un an plus tard avec la sortie de Uniswap v3 en Mai 2021[^UNIv3].

![UNIv2-migration-tool](/img/2022/unstoppable-defi/UNIv2-migration-tool.png "Outil de migration v1⇒v2 en un clic proposé par Uniswap")

En fonction des différences entre les versions, le protocole peut également proposer un outil pour faciliter la migration comme ce fut le cas pour UNIv1⇒UNIv2, mais impossible pour UNIv2⇒UNIv3 principalement à cause de l’introduction de la concentration de la liquidité.

{{< notice note >}}
Pour être exhaustif sur l’analyse coût/bénéfice des contrats immuables, rappelons qu’ils rendent les 🔧 wrench attack impossibles et peuvent également présenter un intérêt du point de vue réglémentaire.
{{< /notice >}}

## Le spectre de la résilience

Maintenant que la définition d'inarrêtable avec tout ce qu’elle implique a été détaillée, je vous propose d’en venir directement à l’analyse. Avant de creuser les protocoles pertinents, je vous propose un spectre qui met en lumière différents niveaux de résilience :

![defi-spectre-resilience-tokenbrice](/img/2022/unstoppable-defi/resilience-spectrum-fr.png)

Détailler des protocoles centralisés ou  “DINO” (Decentralized in Name Only), qui n’ont de décentralisé que le nom, n'est ni très excitant ni intéressant, je vous laisse donc creuser par vous-même. Analysons plutôt des protocoles qui se situent sur la partie la plus palpitante du spectre : à la droite de MakerDAO.

## Analyse des DEX les plus résilients

Avant d’en venir à la résilience d’Uniswap et de Curve, il faut rappeler quelques éléments importants sur les échanges décentralisés. Concrètement, ils ont deux types d’utilisateurs qui assument des niveaux de risques bien différents :


1. Les utilisateurs qui échangent des tokens grâce aux DEX. Ceux-ci supportent les risques liés aux smart contracts des DEX pour le temps du swap seulement (ainsi que ceux lié aux “approve” illimité si le contrat du DEX venait à être compromis et que celui-ci est modulable)
2. Les apporteurs de liquidité, qui sont exposés tant que leur position est maintenue.

Sur Uniswap comme sur Curve, **les contrats relatifs aux deux situations sont immuables** : il est par exemple techniquement impossible d’envisager un “rug” des apporteurs de liquidité, ce qui n’est pas le cas pour tous les DEX : une telle attaque était possible sur SushiSwap par exemple à une époque à cause de leur fonction de migration.[^migrator]


Il faut noter également que les DEX s’appuyant sur un Automated Market Maker comme Uniswap ou Curve n’ont **pas besoin d’oracle pour fonctionner**, ce qui réduit grandement leur dépendance à des services tiers potentiellement censorables.

Enfin, et ce sera le dernier point de contexte pour les DEX : même si les contrats sont immuables, le risque n’est pas nul pour les apporteurs de liquidité qui assument tous les risques liés aux tokens impliqués dans la paire. La règle générale ici est similaire à celle de la chaîne de composabilité : **une position LP donnée est aussi risquée que son token le plus dangereux**.

{{< notice note >}}
La question du front-end pour les DEX est un peu moins critique puisque de nombreux points d’accès existent. Les utilisateurs les plus malins passent même par un agrégateur d’échanges décentralisés, comme [ParaSwap](https://paraswap.io).
{{< /notice >}}

### Uniswap

Sur [Uniswap](https://uniswap.org/) v1, v2 et v3, les fonctions essentielles sont assurées par des contrats immuables. Depuis [Uniswap V2](https://www.defiscan.info/protocols/uniswap-v2/ethereum), la gouvernance peut voter néanmoins l’introduction d’un frais administratif[^UNI-fee-switch] (= pas pour les LP mais pour le protocole), comme c’est déjà le cas sur Curve.

Ici, le cas est donc très simple. S’il y a certes une gouvernance, la bonne nouvelle (moins pour les possesseurs d’UNI), est que ce qu’elle peut faire est très limité. **Aucune saisie ou migration des fonds n’est possible**. Outre le frais, elle gère des sujets tels que le déploiement d’Uniswap sur une nouvelle chaîne, l’ajout de nouveaux tiers de frais (1bps pour les Stablecoins), ou encore l’utilisation de la trésorerie du protocole[^UNI-treasury], par exemple pour financer des campagnes de liquidity mining ou encore pour distribuer des UNI à des gens sympathiques qui le demandent, sans aucune forme de limite ou comptabilité[^UNI5].

### Curve Finance

[Curve Finance](https://curve.fi/) est un autre exemple de DEX des plus résilient avec une approche tout aussi intéressante. Ici encore, les fonctions de base sont assurées par des contrats immuables. Néanmoins, Curve a aussi une “Emergency DAO” dont les membres sont élus par la gouvernance. Cette Emergency DAO peut “tuer” une pool (seulement celles qui ont moins de deux mois et ne sont pas des factory pools) : toutes les fonctions sauf le retrait sont désactivées. Cela permet d’éviter des pertes de fonds additionnels si un problème venait à émerger avec les contrats de Curve. L'Emergency DAO peut également "tuer" une jauge - le contrat qui gère les récompenses en CRV (et autres tokens potentiels) pour les apporteurs de liquidité. Les jauge "tuées" peuvent être ressucitées par la suite par la DAO principale.

Tout comme Uniswap, Curve a une gouvernance essentiellement centrée autour de la gestion des émissions du token CRV. Le modèle est néanmoins bien plus raffiné ici, je vous invite à lire mes précédents articles sur le sujet pour mieux le comprendre :

- [⚔ Guerre du CRV : comprendre la course à l'accumulation de la capacité à influencer le protocole Curve Finance](https://tokenbrice.xyz/fr/crv-wars/)
- [⚔ Guerre du CRV avancée : analyse des protocoles construits sur Curve et Convex ](https://tokenbrice.xyz/fr/crv-wars-l2/)

Contrairement à Uniswap, la participation à la gouvernance de Curve requiert le verrouillage des tokens CRV ( ⇒veCRV) jusqu’à quatre ans pour ceux qui veulent maximiser leur influence. Cela permet ainsi de protéger la gouvernance de différents types d’attaques.

Enfin, la gouvernance gère également une liste blanche des smart contracts autorisés à interagir avec le contrat veCRV [^veCRV-whitelist]: des décisions lourdes de conséquences pour les apporteurs de liquidité sur Curve et possesseurs de CRV sur le long terme.

{{< notice note >}}
La gouvernance de Curve est une des plus fascinantes à suivre en DeFi. Pour l’aider à prendre des décisions plus éclairées, [une newsletter proposant des analyses de risques des différents protocoles qui demandent une jauge](https://substack.com/profile/66151946-crypto-risk-assessments) s’est mise en place. Je vous en recommande chaudement la lecture, c’est une excellente source pour parfaire sa compréhension des risques en DeFi.
{{< /notice >}}

## Analyse approfondie des autres protocoles notables

Outre les échanges décentralisés, il y a d’autres types de protocoles qui s’approchent autant que possible de l’extrémité la plus résiliente du spectre. Néanmoins, les cas d’utilisations des protocoles que nous allons détailler maintenant sont plus complexes et ne peuvent pas être desservis, à ma connaissance, sans dépendances à d’autres services plus ou moins censorables.


### Liquity

[Liquity](https://www.liquity.org/) est un projet opiniâtre qui vise à créer le système d’emprunt, ainsi que le stablecoin, le plus résilient tout en maintenant un système efficace économiquement pour les emprunteurs. Je ne vais pas trop m’étendre sur ce protocole ici, je vous invite à **[lire l’article dédié](https://tokenbrice.xyz/fr/liquity-protocol/)**.

Concentrons-nous donc sur les points pertinents pour notre sujet du jour :

1. Le code de Liquity est entièrement immuable.
2. Liquity n’a pas de gouvernance.
3. Néanmoins, comme tout service d’emprunt, Liquity dépend d’un oracle (prix de ETH en USD). Ici, c’est ChainLink qui est utilisé mais un système de secours est également mis en place. Des calculs permettent de déterminer si la donnée apportée par ChainLink est jugée fiable. Si ça n’est pas le cas, alors le système passe automatiquement sur une source de prix secondaire tant que cela est nécessaire : l’oracle Tellor.[^liquity-oracle-fallback]
4. Enfin, comme je le mentionnais plus haut, Liquity a également une approche intéressante pour maximiser la décentralisation des front-end.[^liquity-front-end]

Grâce à cette approche, Liquity est le protocole d’emprunt le plus résilient disponible sur Ethereum ce qui permet également à LUSD de rafler le titre de stablecoin le plus solide et décentralisé.[^liquity-disclaimer]

### PoolTogether

[PoolTogether](https://pooltogether.com/) est un protocole fascinant qui explore un concept nouveau : le “sans-perte”. Concrètement, [PoolTogether](https://www.defiscan.info/protocols/pool-together-v5/ethereum) est une loterie où le joueur ne prend aucun risque financier sur son apport principal : le jeu s’appuie entièrement sur le rendement que le principal produit, et le redistribue au différents joueurs en fonction de leur chance au tirage.

![pooltogether](/img/2022/unstoppable-defi/pooltogether.png "Présentation de la lotterie sans perte PoolTogether")

Pour en apprendre plus sur ce protocole, je vous invite une fois de plus à **[lire l’article dédié](https://tokenbrice.xyz/fr/pool-together/)**.

Analysons donc la résilience du protocole. Ici, le principal enjeu est **la source de rendement initiale, qui est externe** :  elle provient de services comme Aave ou Compound, qui ne sont pas totalement inarrêtables. Ainsi, un joueur de PoolTogether assume ce risque sur l’ensemble de son dépôt : le principal ainsi que le rendement généré (avant qu’il soit collecté et redirigé).

Malgré cette dépendance tierce, le protocole PoolTogetger est particulièrement résilient. En effet, côté PoolTogether, **les contrats sont aussi immuables que possible**. Concrètement, ils le sont tous (une pool donnée ne peut donc pas changer de source de rendement), sauf pour la partie relative à la distribution des prix, qui n’affecte que le rendement généré. En effet, le modèle de distribution des prix peut évoluer suite à un vote de gouvernance (mainnet) ou à une opération du multisig (Avalanche/Polygon), nécessaire car la gouvernance cross-chain n’est pas encore disponible.

Je trouve ce point fascinant et assez unique en DeFi : PoolTogether est une loterie sans perte, et ce principe de design (financier) se manifeste également au niveau des smart contracts : en excluant un problème avec Aave/Compound ou bug critique dans les contrats de PoolTogether, un joueur ne peut pas perdre son principal – c’est garanti par le code lui-même ; seul le rendement est potentiellement à risque. Et ce, même si l’équipe entière de PoolTogether subit une 🔧 wrench attack, ou que la gouvernance de PoolTogether est totalement capturée. Ainsi **la promesse du no-loss est reflétée au niveau des contrats eux-mêmes**.

En matière de risques, il y a également des nuances et différences entre la V3 et V4 du protocole, le mieux reste encore de lire attentivement [la documentation](https://docs.pooltogether.com/security/risks) plutôt claire sur le sujet.


### TrustlessFi 🏗️

[Trustless](https://trustless.fi) est un protocole qui me fascine dernièrement. Il n’est pas encore live, mais je pense que l’approche a beaucoup de mérites. Pour le décrire très simplement, **TrustlessFi c’est un peu comme si Liquity et Reflexer faisaient un enfant ensemble, sur zkSync**.

Ainsi, le but est, comme pour Liquity, de créer un protocole qui sera éventuellement aussi inarrêtable que possible, et le stablecoin associé (HUE) héritera de cette propriété. On retrouve d’autres mécanismes proches de Liquity, comme ETH comme seul collatéral, des liquidations immédiates ou encore la décentralisation des front-end (avec un mécanisme de validation communautaire cette fois-ci).

Côté gouvernance, on a ici une approche similaire au plan de dégouvernance de Reflexer/RAI mais plus engageante : 4 phases sont envisagées, et à chaque étape le contrôle de la Foundation et de la communauté décroît, rendant le protocole de plus en plus immuable. Ces **phases seront implémentées au niveau du code des contrats eux-mêmes** : il est possible de retarder la transition vers une nouvelle phase de 45 jours jusqu'à trois fois si nécessaire, mais c’est impossible d’annuler totalement cette transition.

Il y a également un mécanisme similaire au Dai Saving Rate de Maker-MCD qui permet de participer au système sans avoir forcément besoin de générer de la dette. Les possesseurs de HUE pourront ainsi le staker pour obtenir un rendement provenant des taux d’intérêt payés par les emprunteurs.

Finalement, il y a également de véritables nouveautés fascinantes, comme par exemple le fait que les Troves/CDP seront tokenisés sous forme de NFT, permettant ainsi leur transfert. Ou bien encore, le déploiement de la liquidité en HUE sur Uniswap v3 avec une gestion assurée par le protocole lui-même (HUE/ETH). Au niveau de l’oracle également, on aurait ici enfin une source de prix inarrêtable avec l’utilisation d’Uniswap v3, mais cela vient sans doute avec des risques de manipulation accrus.[^^UNIv3-oracle]

Dans l’ensemble, l’approche part clairement dans la bonne direction, mais il y a de nombreux nouveaux concepts dans ce protocole, il n’est donc pas aisé de se projeter pour envisager le résultat une fois disponible en production pour l’instant.[^trustlessfi-doc]


## Conclusion et dernières précisions

J’espère que cet article conséquent pourra servir de référence à tous ceux qui se posent des questions essentielles quant à la résilience des protocoles DeFi. Comme à mon habitude, plutôt que de vous livrer des analyses telles quelles, j’ai essayé de détailler autant que possible la méthodologie et le raisonnement afin de vous permettre d’étudier par vous-même la résilience de tout protocole non mentionné dans cet article.

Pour approfondir, je vous invite chaudement à lire un article que j’ai publié l’année dernière qui est le parfait complément de celui-ci : il se concentre sur les marchés monétaires et services d’emprunts et vous propose là aussi une méthode d’analyse pour évaluer les différents risques potentiels qu’ils impliquent :

**[De l'évaluation du risque sur les marchés monétaires en finance décentralisée](https://tokenbrice.xyz/fr/marche-monetaire-risque/)**

J’imagine qu’une analyse aussi limpide d’un sujet si critique pourrait susciter des émotions plus ou moins positives. Sachez que, comme toujours, mon intention est uniquement **d’informer le plus grand nombre possible de DeFians sur des sujets que j’estime essentiels pour la DeFi en général.**

Toutes mes actions éducatives et pédagogiques en DeFi n’ont pas d’autre objet que de maximiser la résilience et la pertinence de la finance décentralisée sur le long terme. J’espère que les développeurs ou promoteurs de protocoles situés à la gauche de mon spectre d’inaltérabilité suggéré sauront également comprendre et reconnaître ce mandat.

_🙏 Un immense merci à tous les relecteurs et contributeurs qui ont particié à l'élaboration de cet article:_

- _Relecture et clarté de l'expression : [Charles](https://twitter.com/C53300) et [Disiaque](https://twitter.com/disiaque_eth)_
- _Relecture technique et factuelle: [Taz](https://www.radjaidjah.org/) de DeFi France, [MTorgin](https://twitter.com/MTorgin)_

---

## Notes de bas de page

[^précisions-d’inarrêtable]: J’évoque tout au long de cet article l'inarrêtabilité de certains protocoles DeFi : on parle ici de l’immuabilité du code des smart contracts. L’ordre des transactions sur Ethereum peut malgré tout être manipulé (⇒ MEV) et les mineurs gardent un rôle important (jusqu’à la transition vers PoS). L'inarrêtabilité contractuelle évoquée dans cet article connaît donc des limites infrastructurelles.
[^aave-xSUSHI]: [Analyse de l'incident](https://governance.aave.com/t/analysis-of-xsushis-incident/6335) sur le forum de gouvernance Aave.
[^UNIv2]: [Annonce du lancement d’Uniswap V2](https://uniswap.org/blog/launch-uniswap-v2)
[^UNIv3]: [Annonce du lancement d’Uniswap V3](https://uniswap.org/blog/uniswap-v3)
[^UNI-fee-switch]: Vous pouvez suivre [les dernières discussions en la matière](https://gov.uniswap.org/t/i-think-it-is-necessary-for-uniswap-concurrently-to-turn-on-the-fee-switch-and-liquidity-mining-incentive/15645) sur le forum de gouvernance d’Uniswap.
[^migrator]: Plus d’information sur cette fonction tant redoutée dans [cet article dédié de Rugdoc](https://rugdoc.io/education/migrator/).
[^UNI-treasury]: Entièrement en token UNI, cette trésorerie est assez volatile. Néanmoins, il y a quand même plus de 227M UNI disponibles aujourd’hui, soit environ $1.1B. [OpenOrgs](https://openorgs.info/)
[^UNI5]: C’est le tristement célèbre vote 005 “DeFi Education Fund”, lisez [le sujet associé sur le forum de gouvernance](https://gov.uniswap.org/t/governance-proposal-005-defi-education-fund/12963) pour plus de contexte.
[^veCRV-whitelist]: Il y en a trois à l’heure actuelle : Yearn Finance (yveCRV), Convex (cvxCRV) et StakeDAO (sdCRV).
[^liquity-oracle-fallback]: Cet article propose [une introduction claire au système de gestion d’oracles sur Liquity](https://www.liquity.org/blog/price-oracles-in-liquity).
[^liquity-front-end]: Plus d’informations [sur le modèle technique et d’incitation pour les opérateurs de front-end Liquity](https://www.liquity.org/blog/liquity-runs-on-decentralized-frontends).
[^liquity-disclaimer]: Comme vous l’avez sans doute déjà vu, je suis ravi d’avoir [rejoint l’equipe de Liquity très récemment](https://tokenbrice.xyz/fr/joining-liquity/). Je mentionne Liquity dans cet article car c’est un exemple pertinent et instructif de protocole résilient, indépendamment de mes engagements professionnels.
[^UNIv3-oracle]: Pour vous faire une idée plus précise, Euler Finance propose [un outil permettant de simuler les attaques d'oracle potentielles lorsqu'un TWAP Uniswap V3 est utilisé](https://oracle.euler.finance/).
[^trustlessfi-doc]: Comme toujours, l'alpha est pour ceux qui creusent et lisent attentivement les footnotes ainsi que [les documentations](https://trustlessfi.notion.site/Trustless-4be753d947b040a89a46998eca90b2c9).
[^chainlink-multisig]: ChainLink a partagé plus d'information sur ce multisig [dans leur documentation](https://docs.chain.link/docs/using-chainlink-reference-contracts/#updates-to-proxy-and-aggregator-contracts) et vous pouvez vérifier le contrat **[directement sur EtherScan ici](https://etherscan.io/address/0x21f73d42eb58ba49ddb685dc29d3bf5c0f0373ca#readProxyContract)** ![chainlink-multisig-updated](/img/2022/unstoppable-defi/chainlink-multisig-updated.png)

---
title: "Le cycle de l'agrégation tourne, avec le prêt"
description: "Dans le prêt, le véritable avantage n'est pas de trouver le taux ; c'est de posséder les rails qui les connectent tous."
date: '2025-08-10T01:13:50.191Z'
categories: [DeFi]
tags: [DeFi, Ethereum, Decentralized Finance, Lending, Aggregator, Fluid, Euler]
url: lending-aggregation
image: img/2025/lending-aggregation/lending-aggregation-cover.png
---

Quelque chose de grand se passe dans le prêt onchain. Sous la surface, un changement discret est en train de remodeler la façon dont la liquidité se déplace, dont les marchés se connectent et dont les utilisateurs accèdent au rendement. Une vague de nouveaux modèles, d'intégrations et d'étoiles montantes comme Euler et Fluid ont réécrit les règles avec une efficacité et une flexibilité sans précédent. Une nouvelle couche de coordination émerge et pourrait redéfinir le prêt lui-même : aujourd'hui, nous levons le voile sur l'agrégation de prêts.

## Le Cycle de l'Agrégation

J'ai vu un scénario similaire se dérouler du côté des DEX, avec l'essor d'Uniswap, suivi par la concurrence de Sushi, les agrégateurs et l'arrivée d'UNIv3. Les concepts de base nécessaires pour analyser les deux transitions sont similaires, et je les expliquerai dans cet article.

La première chose à noter est qu'il s'agit d'un modèle, dans lequel je vois quatre moments :

1. **Inception Verticale** : D'abord, une nouvelle verticale est découverte.
2. **Prolifération des Produits** : À mesure que plus d'équipes entrent dans la verticale, le nombre d'options disponibles pour les utilisateurs augmente, menant à une situation de saturation de l'offre.
3. **Agrégation** : Les agrégateurs émergent car ils apportent une valeur tangible aux utilisateurs (meilleur prix, plus rapide, plus sûr, etc.) par rapport à l'expérience site par site sous-jacente.
4. **Personnalisation du Côté de l'Offre** : Avec les agrégateurs maintenant courants, le marché est mûr pour une plus grande personnalisabilité du côté de l'offre, que les agrégateurs peuvent maintenant traiter et distribuer aux utilisateurs.

Ce scénario représente le niveau de base, généralement complété par un autre flux observé à la fois pour les échanges et les prêts : **l'augmentation de la personnalisabilité du côté de l'offre**, résultant d'un passage d'un modèle de pool à des offres plus à la demande et personnalisées (OTC). À mesure que cela se produit, les agrégateurs deviennent encore plus cruciaux car ils livrent maintenant à l'utilisateur ce qu'il ne découvrirait pas nécessairement par lui-même. Pour le dire autrement : tandis que **les agrégateurs trouvent leur PMF en exploitant les pools sous-jacents** (ex, UNIv2, Curve), **leur utilité brille vraiment une fois que la couche d'offre plus personnalisée est développée**.

Notez que bien que nous discuterons d'instances de ce modèle pour les prêts et les échanges décentralisés, la situation est similaire pour le bridging, avec la couche d'agrégation qui se renforce (Jumper, Bungee, Infinex Swidge, etc.).

## Le « Problème » : Densification des Offres de Prêts

L'agrégation de prêts a émergé pour résoudre un problème tangible, manifesté par la démultiplication des chaînes, des protocoles de prêts et de leurs modèles, permettant ensemble **un nombre exponentiellement croissant de façons de collatéraliser onchain**.

D'abord, vous avez les **marchés monétaires généralistes larges** comme Aave ou Compound. Ils ont une couverture de collatéral et des offres similaires. Tous deux supportent de nombreuses variantes d'ETH staké, de stables portant du rendement et de BTC tokenisé comme collatéral.

Les protocoles CDP **fournissent des outils plus adaptés aux cas d'utilisation avancés, tels que le looping ou l'emprunt à haut LTV. Ici encore, les options se multiplient : c'est **[la saison des forks de BOLD](https://www.liquity.org/blog/forkonomics-collaboration-not-competition)** !

Vous devez également prendre en compte le problème des chaînes : les protocoles mentionnés ci-dessus existent souvent sur **plusieurs chaînes avec des marchés segregués**, ce qui ajoute une toute autre couche d'opportunités. Vous avez aussi des tendances plus petites mais impactantes, telles que le relending, où des stables émis par un autre protocole et déjà mobilisés sont utilisés comme collatéral, avec [Level](https://www.level.money/), [Resupply](https://resupply.fi/), ou [Asymmetry](http://asymmetry.finance/).

Et enfin, il y a la **tendance à l'échelle de l'industrie vers une plus grande personnalisabilité du côté de l'offre**, lancée par Euler et Morpho, et bientôt suivie par Aave avec la sortie de la V4. L'objectif principal ici est d'accueillir les acteurs institutionnels (KYC, accès restreint, etc.).

Sur ce front, un autre OG值得 mention est [GearBox](https://gearbox.fi/), car il le fait depuis presque une demi-décennie déjà, bien que leur angle soit moins axé sur les institutions : Gearbox encapsule l'activité d'emprunt des utilisateurs dans un smart contract, lui permettant d'implémenter une logique relative à l'utilisation des fonds, telle que permettre aux utilisateurs d'emprunter, mais seulement pour acquérir des expositions spécifiques.

**La personnalisabilité de l'expérience de prêt peut être cartographiée sur un spectre borné par Aave et ETHLend :**

* ETHLend étant le plus personnalisable avec chaque situation spécifique à son emprunteur
* Tandis qu'Aave v1/2 est le plus standardisé, puisque tous les emprunteurs sont sous les mêmes termes

![lending-customizaility-spectrum](/img/2025/lending-aggregation/lending-customizability-spectrum.png)

## Agrégation Sous Tous les Angles

Donc, avec la multiplication des offres et leur diversité croissante, la seule réponse logique est l'agrégation :

### Agrégation d'Informations

Le premier problème est d'identifier les diverses options disponibles pour une paire collatéral/actif emprunté spécifique sur une chaîne donnée. C'est précisément ce que fait [DeFillama Borrow Aggregator](https://defillama.com/borrow) :

![defillama-borrow-aggregator](/img/2025/lending-aggregation/defillama-borrow-aggregator.png)

Cela facilite la **découverte des options** que les utilisateurs pourraient exploiter, mais ils doivent encore rechercher les venues qu'ils ne connaissent pas et procéder à l'exécution eux-mêmes. Certains projets vont donc un peu plus loin, en intégrant l'exécution et la gestion également : entre [DeFiSaver](https://defisaver.com/).

### Agrégation d'Interface

La promesse de [DeFiSaver](https://defisaver.com) est simple mais salvatrice : **une interface unique pour gérer vos positions de prêt sur tous les protocoles, plus quelques automatisations astucieuses, outils de migration ou de suivi en plus**. C'est particulièrement pratique pour les utilisateurs exploitant plusieurs protocoles à la fois, ou cherchant à utiliser l'automatisation pour auto-leverager ou deleverager leurs positions lorsque certaines conditions sont remplies.

![defisaver-discover](/img/2025/lending-aggregation/defisaver-discover.png)

Ainsi, bien que DeFiSaver ne soit pas un protocole en soi, il offre plus d'options que les emprunteurs peuvent exploiter pour créer et gérer des positions, et mérite d'être mentionné. En plus de la gestion, il facilite le processus de découverte via des analyses et l'outil [Discover](https://app.defisaver.com/discover), permettant aux utilisateurs de trouver les meilleurs venues pour leurs positions, similaire à DeFiLlama.

### Agrégation de Protocoles

L'étape suivante et dernière est, bien sûr, d'agréger plusieurs protocoles eux-mêmes. Bien que cette idée soit courante pour le rendement avec Yearn et ses vaults, elle est plus rare dans les prêts. Ici, un exemple principal est [Altitude](https://app.altitude.fi/?referrer=tokenbrice) :

C'est essentiellement un gestionnaire de positions d'emprunt faisant deux choses :

1. Refinance entre protocoles pour optimiser les coûts d'emprunt (Aave ou Morpho)
2. Déploie le capital surcollatéralisé pour générer du rendement utilisé pour auto-rembourser la dette (sur Curve, Pendle, ou Morpho)

C'est pour moi **un exemple sauvage d'agrégation de prêts efficace** : Je dépose mon collatéral sur Altitude et j'emprunte ; en arrière-plan, j'ai peut-être utilisé Aave ou Morpho, ou peut-être switché plusieurs fois entre les deux si j'ai tenu la position assez longtemps ; je n'ai même pas besoin de le savoir, je sais juste que j'ai obtenu le meilleur taux.

### Qu'en est-il des Curateurs ?

L'étincelle récente de personnalisabilité des prêts que nous vivons découle de l'émergence d'un modèle exploité par beaucoup pour **défier la position dominante d'Aave sur les marchés de prêts bluechip**, car à ce stade, il est impossible de défier Aave sur la taille disponible ou la sécurité perçue. Euler ou Morpho sont des constructeurs d'infrastructure autant que des opérateurs de protocoles. Ils fournissent des blocs de construction, exploités par les Curateurs, pour délivrer des expériences de prêts personnalisées et optimisées à des communautés spécifiques.

Pourtant, ils rendent la solution encore plus complexe à déballer, car en plus d'[évaluer le protocole (DeFiScan peut aider)](https://www.defiscan.info/), vous devez maintenant aussi **évaluer les curateurs**, ce qui est une logique totalement différente (historique, AUM, etc.). D'un autre côté, du côté d'Aave, jusqu'à présent, il n'y avait pas de curateur, ou seulement un omnipotent : la DAO Aave, l'entité gérant la gestion des risques et les paramétrisations via ses divers fournisseurs (AGI, LLamaRisk, etc.).

Les curateurs et les agrégateurs travaillent main dans la main. Les curateurs exploitent des pièces d'infrastructure pour délivrer de nouveaux marchés de prêts, tandis que les agrégateurs connectent toutes les offres déjà existantes pour faciliter l'expérience utilisateur.

L'agrégation de prêts devient le tissu conjonctif d'un marché du crédit de plus en plus fragmenté. À mesure que les protocoles se divisent à travers les chaînes, les modèles et les personnalisations, le rôle des agrégateurs passe de « outil utile » à « infrastructure de marché ». Tout comme les agrégateurs DEX sont devenus indispensables une fois la liquidité fragmentée, les agrégateurs de prêts définiront comment le capital circule, qui capture l'écart, et quelles stratégies restent compétitives. Le prochain cycle de prêts DeFi ne consistera pas à découvrir le meilleur venue—il s'agira de router, composer et automatiser à travers tous. Et dans cette course, les gagnants ne prêteront pas seulement plus intelligemment ; ils agrégeront mieux.
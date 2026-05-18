---
title: "De l'évaluation du risque sur les marchés monétaires en finance décentralisée"
description: "Cadre pratique pour evaluer les risques des marches monetaires DeFi, avec des lecons applicables aux protocoles plus largement."
date: '2021-02-18T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Analysis, Lending]
tags: [DeFi, Ethereum, DEX, Money Markets, Aave, Compound, Risk Scoring, Risk assessment, money market risk, aave risk, compound risk, cream risk, DeFiScore, CREAM, COMP, Oracles, Liquidation, Insurance, Safety Module]
series: money-markets
series_order: 1
toc: true
tocNum: false
url: marche-monetaire-risque
image: /img/2021/risk-tranching/cover.gif
difficulty: "expert"
---

Les marchés monétaires sont au cœur de DeFi. D'un point de vue de haut niveau, oui, ils permettent simplement d'emprunter et de prêter divers actifs. Pourtant **ces fonctions sont comme les deux verbes primitifs de DeFi** à la base de presque tous les cas d'utilisation.

Il y a actuellement trois grands marchés monétaires dans DeFi : Aave, Compound & Cream. Pourtant, tous les services suivants les utilisent, d'une manière ou d'une autre : Yearn Finance, Curve Finance, Alpha Finance, Harvest Finance, DeFiSaver, Saffron, 88mph, Idle Finance, etc. Pour dire les choses simplement - **les marchés monétaires sont l'un des niveaux de base du DeFi**.

Les marchés monétaires sont étonnants - à la fois simples et très complexes. Dans cet article, j'essaie de fournir un cadre et quelques indices pour évaluer le risque à différents niveaux.

Pour en savoir plus sur la couche de services qui est en train de se construire sur les marchés monétaires, n'hésitez pas à lire mes articles précédents :

1.   Une introduction au tranching via Saffron Finance :

**[🗡 Du risque ? Oui, mais juste un doigt](https://tokenbrice.xyz/fr/tranching-risque-defi/)**

2.   Une présentation des protocoles de taux d'intérêt fixes à travers le prisme d'APWine :

**[🍷 En oenologie comme en DeFi, la patience paie](https://tokenbrice.xyz/fr/fixed-interest-rate-protocol-firp-apwine/)**

---

## I/ L'évaluation du risque est cassée

Avant de nous plonger dans le cadre de l'analyse des risques, examinons rapidement la principale solution actuellement utilisée pour évaluer les risques dans le cadre de la DeFi : Consensys CodeFi DeFiScore [^defiscore].

**DeFiScore est incontestablement compromis puisqu'il donne toujours un score sur DAI plus élevé sur [Compound](https://www.defiscan.info/protocols/compound-v3/ethereum) que sur [Aave](https://www.defiscan.info/protocols/aave/ethereum)** même avec l'échec de l'oracle du côté du Compound et l'arrivée du module de sécurité du côté d'Aave :

L'équipe de Consensys CodeFi a été avertie il y a quelques jours [^1], a reconnu le problème [^8] mais a pourtant **refusé toute mise à jour immédiate du site web, même avec un simple avis ou une clause de non-responsabilité**. À la place, un de leurs membres a proposé une prime de 500 USDC ouverte à toute personne souhaitant mettre à jour la formule [^2]. Cette prime n'a pas encore été réclamée.

Il n'est pas surprenant que les approches quantitatives aient échoué jusqu'à présent. Elles doivent atteindre à la fois la durabilité (si la formule reste cohérente, elle permet des comparaisons historiques) et l'adaptabilité (pourtant les paramètres de risque sont toujours en évolution) : ce n'est pas une mince affaire.

Je ne m'étendrai pas sur la notation des risques, car un article consacré à la présentation d'un système de notation des risques digne de la DeFi sera bientôt publié sur ce blog (indice : il n'existe pas encore).

---

## II/ Apprécier la sécurité d'un marché monétaire

Je sais que c'est douloureux à entendre, mais comme l'analyse quantitative n'est pas utile, il faut recourir à une approche qualitative pour chaque projet. La bonne nouvelle, c'est qu'il n'y a pas beaucoup de marchés monétaires dans DeFi qui méritent d'être étudiés :

1. Aave
2. Compound
3. Cream

Pour chacun d'entre eux, il faut les considérer de manière globale. Je propose une approche qui est **purement la mienne**, utilisant **8 dimensions différentes toutes critiques pour la sécurité des actifs** engagés sur le marché monétaire analysé :

1. Accès au protocole et autorisations
2. Oracles
3. Mécanismes de liquidation
4. Analyse de risque des tokens acceptés en collatéral
5. Module de sécurité
6. Écosystème d'assurance élargi
7. Gestion des risques du token natif
8. Communauté et écosystème

Ce que nous avons aujourd'hui est donc essentiellement un cadre complet que vous pouvez utiliser pour évaluer la sécurité d'un marché monétaire donné. N'hésitez pas à me mettre au défi sur n'importe quel point. Plongeons dans le vif du sujet.

{{< notice warning >}}
**Avertissement nécessaire : Ceci n'est pas un conseil d'investissement.**

Presque personne n'est qualifié pour évaluer les risques dans le cadre de la DeFi : même les "institutions" qui le font comme le DeFiscore sont loin de le faire décemment.

Ce contenu est destiné à vous aider à mieux comprendre et apprécier le risque **<span style="text-decoration:underline ;">par vous-même</span>**, le moyen le plus fiable de le faire.
{{< /notice >}}

---

### II.A/ Accès au protocole et autorisations

Au niveau le plus élémentaire, vous voulez savoir qui peut mettre à jour les paramètres fondamentaux du protocole (-> les contrats), et les différentes limites qui y sont associées.

Par exemple, il y a généralement un **timelock**, ce qui signifie que toute modification importante ne s'applique qu'après une durée déterminée. Pour les fonctions administratives du protocole, vous devez vous assurer qu'elles **appartiennent à la communauté**, donc idéalement dans les mains des holders du token via la DAO ou une multisignature de membres de la communauté.

Cette section comprend également tout ce qui concerne *l'opsec* des portefeuilles/personnes** régissant le multisig. "Opsec" est l'abréviation de "operations security" - il s'agit de la sécurité de tout ce qui concerne les interfaces numériques liées aux détenteurs de ces clés. Peuvent-elles être piratées ? Usurpées ? Etc.

Une telle question est **<span style="text-decoration:underline ;">CRITIQUE</span>**, comme nous l'avons vu récemment avec le PDG de Nexus Mutual : son ordinateur portable a été compromis, permettant au pirate de soumettre une transaction frauduleuse en plus d'une transaction réelle qu'il a signée.[^3]

Nous n'avons pas encore vu d'attaques importantes basées sur l'ingénierie sociale au sein de la DeFi, mais nous nous y attendons.

La transparence sur les décisions du protocole est également essentielle : nous en parlons ci-dessous dans la section Communauté & écosystème.

Cet article se concentre sur les marchés monétaires matures comme Aave ou Compound. Les projets plus récents peuvent être moins décentralisés, et cela peut être une bonne chose - vous pourriez vouloir certaines options de contrôle et de récupération pour un projet plus récent.

#### Évaluation des accès au protocole et de la décentralisation

- __🔮Probabilité__ : À évaluer sur la base d'un protocole ou d'une équipe
- __🔥Potentielle perte de fonds__ : Tous les fonds déposés sur le marché
- __❌C'est déjà arrivé ?__ Pas encore 🤞

{{< notice tip >}}
Lorsqu'il s'agit d'évaluer l'opsec et le plan de décentralisation, [Chris Blec](https://twitter.com/ChrisBlec) est votre homme. Il est intransigeant sur l'opsec et a produit de nombreuses contributions utiles en la matière.

Vous pouvez trouver un **[aperçu résumé de la situation pour les principaux projets de DeFi ici](https://docs.google.com/spreadsheets/d/13S7NRk1girTdQMajnVdU5JRlVO5BG_uJKhTO2Ef10b0/edit?usp=sharing)**
{{< /notice >}}

Pour conclure cette première dimension, voici quelques bonnes questions à poser pour évaluer la sécurité d'un marché monétaire au niveau du protocole et des autorisations :

* Qui peut mettre à jour les contrats ?
* Sont-ils prudents du point de vue opsec ?
* Y a-t-il une fonction de vidange dans les contrats ?
* Que font les fonctions administratives ?
* Dans quelle mesure le processus de création d'un nouveau marché des prêts est-il décentralisé ?

---

### II.B/ Oracles

En termes simples, les oracles sont la source de "vérités extérieures". **Les blockchains ne sont conscientes que d'elles-mêmes**, donc pour Ethereum, le prix de l'ETH en dollars (ou tout autre token) est techniquement une "vérité extérieure" qu'il faut faire entrer dans la chaîne **d'une manière sûre et vérifiable** : c'est précisément ce que font les oracles !

C'est essentiel, car le **prix perçu** délivré par l'oracle est la **source de vérité pour les décisions de liquidation du protocole**. Si l'oracle dit que le DAI vaut 1,30, alors vous êtes liquidé même si votre position d'emprunt DAI était sûre avec un DAI de 1 $ et que le DAI vaut toujours en réalité 1 $ sur les marchés. C'est déjà arrivé avec Compound, donc ce n'est pas une préoccupation théorique [^4].

La bonne nouvelle ici est que la réponse est assez simple : [ChainLink](https://www.defiscan.info/protocols/chainlink-oracles/ethereum) est largement reconnu comme la solution décentralisée la plus crédible pour les oracles, donc tout marché monétaire qui n'utilise pas au moins en partie ses flux de prix joue avec l'argent de ses utilisateurs, comme l'a fait Compound avec de lourdes pertes. Il semble que la situation ne se soit pas améliorée - malgré le problème, Compound utilise toujours le même oracle centralisé (Coinbase)[^compoundoracle].

#### Évaluer les oracles

- __🔮Probabilité__  : Significative (c'est le facteur de risque le plus important à ce jour).
- __🔥Potentielle perte de fonds__ : des marchés entiers peuvent être drainés/affectés.
- __✅C'est déjà arrivé ?__ Oui, sur Compound. [^4]

Vous pouvez évaluer les oracles pour un marché monétaire avec la question suivante :

* Quelle est la source de vérité des prix ?
* Quelle est la fiabilité de cette source ?
* Y a-t-il des antécédents de liquidation abusive (découlant des problèmes des oracles) ?


---

### II.C/ Mécanismes de liquidation

Les mécanismes de liquidation sont également essentiels, mais ils n'interviennent qu'une fois qu'une liquidation peut être déclenchée - ce qui dépend du prix que l'oracle rapporte. Le **mécanisme de liquidation ne peut donc pas compenser un oracle défectueux**. Il est essentiel de le comprendre d'abord.

Ensuite, les différents marchés monétaires traitent les liquidations différemment. Ils ont des délais, des frais et des restrictions différents en ce qui concerne leurs liquidations. Par exemple, l'oracle de Maker (système interne) a un délai d'une heure pour éviter les liquidations instantanées en cas de crashs éclairs ponctuels.

De plus, la liquidation n'est pas un événement soudain ni un tout ou rien. Il y a plusieurs tampons à vos positions, par exemple sur Aave, chaque token a un **capacité d'emprunt donnée** (LTV) et un **seuil de liquidation** au moins légèrement plus élevé.

Ainsi, avec l'USDC en collatéral, par exemple, il y a un écart de 5 % entre les deux - la LTV maximale est de 80 % (*maximum de 8 000 $ empruntés sur un collatéral de 10 000 USDC*), tandis que le seuil de liquidation est de 85 % (*= liquidation si valeur du collateral &lt; 8 500 $*)

![Aave USDC collateral parameters](/img/2021/money-market-risks/aave-usdc.png "Les principaux paramètres pour USDC comme colléral sur Aave")

Il donne aux emprunteurs utilisant l'USDC comme collatéral une marge supplémentaire de 5 %, de sorte que même si l'oracle fait état de 0,97 $, aucune liquidation n'aura lieu. La situation est similaire sur les autres marchés monétaires.

#### Évaluer les mécanismes de liquidation

- __🔮Probabilité__ :  Cela dépend surtout de l'action sur les prix des collatéraux - un krach éclair pourrait déclencher une chaîne de liquidations
- __🔥Potentielle perte de fonds__ : Important (le marché monétaire pourrait être sous-collatéralisé)
- __✅C'est déjà arrivé ?__ Oui, sur Maker où il y a eu des problèmes et des retards dans les liquidations. [^makerCBT]

Voici donc quelques questions à se poser pour évaluer les mécanismes de liquidation :

* Quand les liquidations sont-elles déclenchées ? quel est le flux ?
* Est-ce qu'il y a un délai additionnel avant de liquider ?
* Quels sont les frais de liquidation ?

{{< notice info >}}
Il y a un autre sous-thème important ici : les **liquidations n'arrivent pas par magie** - elles sont déclenchées par d'autres utilisateurs. Il faut donc que les incitations soient là aussi au rendez-vous pour que les liquidations se fassent au moment voulu et rapidement. Ce sujet est encore plus complexe aujourd'hui, à l'ère des coûts élevés du gaz (bénéfices de liquidation vs coûts du gaz de la tx). On passe pour garder cet article digeste.
{{< /notice >}}


---

### II.D/ Analyse de risque des tokens acceptés en collatéral

D'accord, maintenant que nous avons un marché monétaire qui obtient des prix fiables et qui liquide quand c'est nécessaire, nous pouvons commencer à examiner les tokens acceptés comme collatéral et la procédure à suivre.

L'évaluation de la santé et de la sécurité globale d'un token est **l'une des tâches les plus complexes de nos jours au sein de DeFi** car il peut être difficile de comprendre l'ensemble de l'écosystème autour d'un token.

Prenons le token SNX, par exemple, un token ERC-20 important. Il est utilisable comme collatéral sur Aave, mais avec un ratio prêt/valeur maximum assez faible (à relever bientôt ?) à 15 %. D'autres tokens ERC-20 comme LINK sont dans la fourchette de 60-75%.

Sans trop entrer dans les détails, cela concerne ce que vous pouvez faire avec chaque token et l'utilisation de **SNX comme collatéral sur la plateforme Synthetix**.

Les paramètres de risque d'Aave sont suffisamment conservateurs pour que Synthetix soit essentiellement "en première ligne" dans la chaîne des liquidations si un événement "cygne noir" devait se produire sur Synthetix. Cela semble sage : un marché monétaire ne devrait pas vouloir s'exposer davantage sur un token donné que sur la plateforme native elle-même.

Une autre façon de voir les choses est l'inverse : évaluer la "santé" globale des derniers tokens ajoutés en garantie sur la plateforme : sont-ils liquides ? Sont-ils décentralisés de manière crédible ? Etc.

Vous pouvez également examiner la répartition des garanties afin d'évaluer l'exposition de la plateforme. Par exemple, on peut noter que sur Cream, près d'un tiers des dépôts sont des tokens FTT (échange FTX).

![Cream](/img/2021/money-market-risks/cream.png "Environ 1/3 des dépôts sur Cream sont constitués d'un seul token, et ce n'est pas celui que vous voudriez ou que vous vous attendriez à trouver ici").

#### Évaluation de la stratégie de gestion des risques sur les collatéraux

- __🔮Probabilité__ : Dépend de la stratégie de cotation des garanties et de l'appétit pour le risque
- __🔥Potentielle perte de fonds__ : Si un token dangereux est accepté en garantie, le marché monétaire peut se retrouver sous-collatéralisé, voire drainé. Cream, par exemple, accepte le COVER comme garantie. Le token a déjà été frappé trois fois à l'infini, exposant Cream à un risque supplémentaire.[^covershitcoin]
- __❌C'est déjà arrivé ?__ certains tokens ont subit une émission infinie, comme COVER. Mais ils n'était pas utilisés comme collatéraux sur un marché monétaire à l'époque.

Je ne m'étendrai pas davantage sur ce sujet, car la documentation d'Aave sur les risques est très bien faite - consultez [la section sur les paramètres de risque](https://docs.aave.com/risk/asset-risk/risk-parameters) pour plus d'informations.

* Comment sont prises les décisions relatives à la liste des garanties ?
* Quel est le cadre de risque utilisé pour les garanties ?
* Comment le marché monétaire s'adapte-t-il à l'évolution de la situation des tokens qu'il répertorie ?

---

### II.E/ Module de sécurité

Même si le risque est connu à tous les niveaux, **l'assurance n'est jamais une option et n'est jamais de trop**. La première couche de défense est bien sûr le niveau de la plate-forme s'il existe un module de compensation.

La bonne nouvelle, c'est qu'il y en a un ! Aave a été le pionnier dans ce domaine et même Compound a une petite réserve. La deuxième bonne nouvelle est que pour évaluer l'utilité de ce module, c'est très simple : il s'agit d'un simple rapport entre la valeur totale en $ des emprunts effectués sur le marché monétaire et le total des $ pouvant être mobilisés par le module de sécurité.

Aave dispose d'environ 2B dans le module de sécurité, dont jusqu'à 30% peuvent être saisis si nécessaire = 600M. Il couvre à la fois les V1 et V2 du protocole. Si les 30% sur la coupure du module de sécurité ne sont pas suffisants, le module de sécurité peut frapper des tokens AAVE supplémentaires. Un tel scénario n'est pris en compte ni par Compound ni par la Cream.

![Aave's Safety Module](/img/2021/money-market-risks/aave-safety-module.jpeg "Aperçu du Safety Module Aave")

En plus de l'assurance, les marchés monétaires peuvent aussi avoir des réserves. Compound est ici le pionnier, avec environ 10 millions de dollars de réserves [^compoundreserve]. Aave a également un système de réserve qui a été récemment lancé, mais je l'ai exclu de l'analyse compte tenu du solde limité [^10].

Alors, en regardant les chiffres disponibles, voici nos calculs rapides :

`Ratio de sécurité = Valeur de l'assurance en USD / Total des emprunts sur le marché monétaire`

1. **🛡 Aave = 53%** | 1,765 (30% mobilisable) milliard de dollars dans le module de sécurité pour 1,1 milliard de dollars empruntés à travers V1+V2 (572 millions de dollars V1, 437 millions de dollars V2)
2. **🕯 Compound = 0,24%** | 4,3 milliards de dollars empruntés sur un capital de sécurité de 10 millions de dollars.
3. **💀 Cream = 0 %** | Pour autant que je sache, Cream n'a pas de module d'assurance native ou en a un très limité (faibles montants).

ℹ Note : Bien que Compound n'ait actuellement aucun module de sécurité, l'équipe/DAO est actuellement assise sur une importante réserve de COMP qui pourrait être utilisée à cette fin [^compoundCOMPstosk]. Les calculs ont été effectués le 17 Février 2021.

#### Évaluation du module d'assurance natif

- __🔮Probabilité__ : Non-nul, mais moins pertinent ici. Le SM est là pour fournir des compensations en cas d'échec.
- __🔥Potentielle perte de fonds__ : Les déposants savent qu'ils peuvent se faire couper les vivres si nécessaire.
- __✅C'est déjà arrivé ?__ Aave est un pionnier dans ce domaine. Le slashing est activé depuis quelques semaines. Jusqu'à présent, aucun événement n'a obligé Aave à exploiter le module de sécurité, mais c'est bien de savoir qu'il est là !

Pour avoir une idée de la protection des modules de sécurité et d'assurance natifs, voici quelques questions décentes à poser :

* Y a-t-il un module d'assurance natif qui couvre la plate-forme ?
* Comment fonctionne-t-elle ?
* Quels sont les délais de retrait et les garanties ?
* Quel est le ratio de couverture (USD TVL exposé / USD TVL du module de sécurité) ?


---

### II.F/ Ecosystème d'assurance élargi

En plus du système d'assurance natif du marché monétaire, les déposants et les emprunteurs peuvent **couvrir leurs positions grâce à un service d'assurance de tiers** comme Nexus Mutual ou Unslashed.

Le <span style="text-decoration:underline ;">risque le plus largement couvert est celui d'une défaillance technique des contrats intelligents</span>. Vous trouverez des couvertures pour à peu près tous les contrats largement utilisés qui existent. Cependant, **les défaillances des contrats intelligents ne sont pas le seul événement qui peut entraîner une perte de fonds sur un marché monétaire**.

C'est pourquoi Robert Leshner, le PDG de Compound, peut déclarer ce qui suit [^5] alors que le protocole a récemment subi 90M de liquidations abusives en raison d'oracles défectueux :

>Compound fonctionne depuis près de 2 ans avec ZERO problèmes de smart contracts.

Cela crée un faux sentiment de sécurité auquel beaucoup se laissent prendre, tout comme la période de fonctionnement du protocole. Remarquez comment je n'ai pas inclus le "temps d'opération" dans ces 8 critères ? C'est parce qu'il a une pertinence proche de zéro malgré le fait que des services comme DeFiScore lui donnent un poids absurdement important.

{{< notice note >}}
Je suis prudent lorsque je parle de "90 millions de liquidations abusives à cause d'oracles défectueux" mais pour être explicite - cela a potentiellement affecté négativement tout emprunteur DAI à l'époque qui aurait pu être liquidé de manière incorrecte - perdant une partie de son dépôt sans **aucun recours et aucune compensation** puisque Compound a fonctionné comme prévu (du point de vue des contrats).
{{< /notice >}}

En plus des risques d'échec des smart contracts, veuillez considérer la liste suivante d'autres risques non exhaustifs qui peuvent entraîner une perte de fonds :

1. Échec ou manipulation d'un oracle,
2. Un problème avec le contrat intelligent d'un token utilisé en collatéral (par exemple token frappé à l'infini),
3. Un stablecoin utilisé comme collatéral ou actif d'emprunt sur le marché perd son ancrage
4. Le dispositif ou le portefeuille de l'administration d'un service pas si décentralisé est compromis
5. Des problèmes ou des retards dans les liquidations, ce qui signifie que le marché monétaire ne peut potentiellement plus répondre à ses exigences en matière de collatéral
6. etc.

La plupart des services d'assurance ne sont pas utiles pour tous ces risques, sauf pour les risques de défaut d'un smart contract. Le marché des autres types de risques commence à peine à se développer grâce à Unslashed Finance qui offre désormais une **couverture du risque de perte de l'ancrage des Stablecoins** ou du risque de dépositaire.

![Defiprime insurance](/img/2021/money-market-risks/defiprime-insurance.png "Les différentes approches de l'assurance DeFi --- publié 2019 & biaisé mais encore un peu instructif")


Pour en savoir plus sur les différentes approches de l'assurance DeFi, consultez [cet article de DeFi Rate](https://defiprime.com/comparing-insurance-like-solutions-in-defi). Veuillez garder à l'esprit le **biais massif ici** : il a été écrit il y a plus de deux ans par Hugh Karp, fondateur de Nexus Mutual. Cependant, il est encore suffisamment factuel et perspicace pour vous aider à comprendre les différents modèles.

#### Comprendre les assurances et le risque qu'elles couvrent réellement

- __🎯Objet__ : Échec de contrats intelligents + perte de peg de Stablecoins.
- __💰Utilité__ : Fournit une compensation si une défaillance est constatée.
- __✅C'est déjà arrivé ?__ Nexus Mutual, l'une des plus anciennes options d'assurance a déjà payé dans plusieurs situations de défaut de smart contracts. [^nexusmutual]

Pour ce qui est des assurances étendues, vous voudrez donc examiner des services tels que [Unslashed Finance](https://www.unslashed.finance/), [Nexus Mutual](https://nexusmutual.io/) ou [Cover Protocol](https://www.coverprotocol.com/) et les plans qu'ils proposent.

* Quelles sont les options disponibles à travers l'écosystème pour couvrir une position sur le marché monétaire ?
* Quels sont leurs prix et leur fiabilité (déjà payés ?)?

---

### II.G/ Gestion du risque du token natif

Nous avons beaucoup discuté des différents tokens utilisés comme collatéraux, mais il y en a un que vous devez surveiller de très près : le **token natif du marché monétaire**. Il s'agit donc du token COMP sur Compound, AAVE sur Aave, et CREAM sur Cream.

{{< notice info >}}
Le ratio prêt/valeur maximum (LTV maximum) détermine le pouvoir d'emprunt des collatéraux. Un prêt à valeur maximale de 50 % signifie que l'on peut emprunter jusqu'à la moitié de la valeur en dollars des collatéraux déposés.
{{< /notice >}}

La toute première couche est bien sûr de s'assurer qu'il n'y a pas de jeu de dupes : **le marché monétaire doit être neutre et ne pas favoriser son propre token**.

Cela semble évident, mais on est en droit de se poser la question, notamment au vu des ratios prêt/valeur accordés aux tokens de plateforme. Par exemple, Cream autorise une max LTV excessive de 75%  sur CREAM, l'une des plus élevées de tout le protocole. Compound lui-même donne au COMP une LTV max permissive de 60% alors que Aave est plus conservateur à 50%.

{{< notice tip >}}
Si le marché monétaire est sain et le token bien conçu - les gens devraient être optimistes, ce qui signifie que certains d'entre eux l'utilisent comme collatéral pour acheter à long terme - c'est-à-dire déposer AAVE sur Aave pour acheter à long terme AAVE.

Il n'est pas surprenant que, malgré la permissivité de la LTV, les positions longues de COMP et de CREAM soient plus rares que celles de AAVE.
{{< /notice >}}

#### Évaluer la manière dont un marché monétaire gère les risques liés aux tokens

- __🔮Probabilité__ : C'est un événement "tout ou rien" : le marché monétaire peut jouer avec le feu sur son token natif pendant des mois sans conséquences avant que la situation n'explose et que le token + le marché monétaire ne s'effondrent ensemble.
- __🔥Potentielle perte de fonds__ : La perte peut potentiellement s'étendre à l'ensemble du système (tout le marché monétaire est touché).
- __❌C'est déjà arrivé ?__ Pas encore. Mais Cream est déjà bien au-delà de tout chiffre raisonnable de max LTV  sur le token CREAM.

Et voici quelques considérations qui méritent d'être explorées :

* Regardez la santé du token natif de la plateforme : contrat de token, liquidité, intégrations, etc.
* Examiner l'utilisation du token natif sur le protocole et évaluer la santé de son marché
* Propriété, distribution et coefficient de Gini du token de gouvernance

Jusqu'à présent, nous nous sommes concentrés sur le marché monétaire lui-même. Pourtant, il s'agit de projets dirigés et régis par la communauté, de sorte que leur communauté et leur intégration dans l'écosystème constituent une partie essentielle de l'évaluation.

---

### II.H/ Communauté & Ecosystème

Dans le DeFi, les communautés sont essentielles. Il ne s'agit pas d'une option pour rendre le protocole plus attrayant, c'est une **caractéristique essentielle** et je l'évalue comme telle.

Sur un tel sujet, encore une fois, aucune mesure ne vous aidera à elle seule. L'essentiel est d'avoir une idée du dynamisme de la communauté. Cela se traduit généralement par ses composantes de base : le DAO, le Discord et la présence globale dans l'espace.

Une autre conséquence d'une communauté saine est **l'appui et l'utilisation généralisés dans tout l'écosystème**, avec de nombreux services et produits construits sur le protocole examiné. Ici, malgré le fait que Compound ait été le premier, Aave est aussi maintenant un choix de premier ordre pour tout nouveau protocole construisant une nouvelle primitive financière.

En effet, les équipes peuvent délibérément favoriser un tel environnement simplement en ayant des membres accessibles et impliqués dans l'espace. En outre, Aave a une initiative de **subventions d'écosystème** [^aavegrants] qui aide à financer des projets construits sur Aave tels qu'[APWine](https://tokenbrice.xyz/fr/fixed-interest-rate-protocol-firp-apwine/). D'autres initiatives liées à la communauté sont un bon exemple, comme les hackathons, les AMA, les livestreams, etc.

Ici encore, assurez-vous d'évaluer la qualité et non la quantité. Il est facile de se précipiter sur toutes les initiatives énumérées ci-dessus. Mais il est beaucoup plus difficile de le faire correctement, d'une manière qui ait un sens pour la communauté et qui la fasse avancer.

Je ne veux pas en faire un cas de figure contre Compound, mais là encore, c'est tellement évident. Alors que les financements communautaires de Compound sont assez limités, le programme de subventions vient d'être lancé [^6], son fondateur Robert Leshner est un investisseur en capital-risque actif, avec les fonds Robot Ventures [^7].

![Robovc](/img/2021/money-market-risks/robovc.png "RoboVC & ses principaux investissements")

#### Évaluation de la communauté & DAO d'un marché monétaire

- __🔮Probabilité__ : La communauté est la caractéristique la plus importante de toutes pour le succès à long terme du marché monétaire.
- __🔥Potentielle perte de fonds__ : Risque à long terme. Si un marché monétaire perd les faveurs de la communauté, ce ne sera pas un événement dramatique, mais plutôt un lent et douloureux enchaînement d'événements le plongeant dans l'inutilité.
- __✅C'est déjà arrivé ?__ Oui, avec Compound - ils ont perdu leur position de tête et leur préférence pour plusieurs raisons, telles que leur manque de soutien à l'écosystème, le problème sur l'oracle DAI et la réaction de l'équipe à ce sujet.

Voici donc quelques questions et indices pour vous aider à évaluer cette dernière partie, pourtant essentielle :

**Au niveau de la DAO :**

- Comment fonctionne la soumission d'une proposition ?
- Comment sont-elles examinées et améliorées ?
- Quel est le délai entre le vote et l'exécution ?
- Une proposition qui a été ignorée ou qui n'a pas été mise en œuvre pendant longtemps ?

**Membres de l'équipe principale :**

- Sont-ils légitimes ? Impliqués dans l'espace ? Redonnant ? Conseillant ?
- Vérification des antécédents : sont-ils impliqués dans une escroquerie ? Que faisaient-ils avant ?
- Vérification du présent : en plus de leur implication dans le marché monétaire, que font-ils ? Un conflit d'intérêts potentiel ?

**Écosystème :**

- Documentation et soutien : à quel point est-il difficile de s'appuyer sur ce marché monétaire ?
- Quels sont les services construits sur le marché monétaire ? Sont-ils largement utilisés ?
- Communiquent-ils clairement sur les paramètres de risque ? Disposent-ils d'une documentation non technique sur les risques ?

---

## III/ Une note sur le tribalisme dans la DeFi

L'exploration d'un tel sujet a été pour moi incroyablement instructive, à tant de niveaux. Je reste assez surpris par le tribalisme de l'espace : à part Aave, la collecte des informations présentées dans cet article n'était pas une tâche triviale.

En raison de la question que j'ai posée et des observations que j'ai partagées, j'ai été la cible d'attaques personnelles de la part des fondateurs de certaines des équipes mentionnées dans cet article. D'autres ont été assez trompeurs et sélectifs dans leurs réponses. Je n'ai reçu aucune réponse des comptes officiels ou des équipes de Cream & Compound.

De telles attitudes m'ont donné encore plus envie de faire avancer cet article. **Au-delà des aspects techniques de chaque protocole, je pense que l'attitude de l'équipe fondatrice est également essentielle**. Sur ce plan, il y a un protocole qui se situe un ordre de grandeur au-dessus de tout autre : surprise surprise, il se trouve aussi être le plus techniquement solide, sécurisé, intégré, et excitant, et intéressant. 👻

---

### III.A/ Limites de cette approche d'évaluation des risques

Je m'attends déjà à de fortes réactions, alors permettez-moi d'ajouter quelques sujets supplémentaires qui ne sont pas abordés ici :
1. Bien que nous soyons allés assez loin, nous n'avons pas discuté du processus de tokenisation : le processus utilisé par le protocole pour représenter les avoirs déposés. Sur ce front, **Compound et Cream utilisent tous deux une approche archaïque** qui a été dépassée sur tous les fronts par Aave avec la première version des aTokens au début de 2020 [^aTokenMasterRace] Aave V2 a encore amélioré le processus de tokenisation.
2. Cream en soi est un petit marché, mais **par le biais de l'IronBank, d'autres protocoles peuvent emprunter à Cream**. Il est encore plus difficile d'évaluer le risque sur un tel marché - et il a été exclu de cette analyse. Pour en savoir plus sur le risque réel déjà posé et manifesté par une telle approche, vous pouvez consulter le [dernier Rekt on Alpha Homora](https://www.rekt.news/alpha-finance-rekt/).
3. Bien que MakerDAO fournisse un service fonctionnellement équivalent au prêt, le processus est sensiblement différent puisque chaque emprunteur frappe le DAI. Par souci de simplicité, j'ai donc exclu MakerDAO de cette analyse, à part pour pour quelques exemples instructifs.
4. Je n'ai aucune affiliation avec Aave, Compound, Cream ou tout autre marché monétaire. Je possède cependant des tokens AAVE (achetés à mes frais bien sûr) stakés dans le Safety Module. Tout le contenu hébergé sur mon blog est rendu accessible gratuitement - je suis le seul éditeur.

J'espère que cet article vous a aidé à mieux comprendre l'ampleur des risques sur les marchés monétaires. Je tiens à souligner une fois de plus qu'il n'est ni exhaustif, ni d'une vérité absolue, mais je suis fermement convaincu qu'il apporte des contributions claires et utiles pour faire en sorte que les risques sur DeFi soient largement compris, mieux que ce qui existe actuellement.

Si vous n'êtes pas d'accord avec cette déclaration, **n'hésitez pas à me contester. Je suis avide de faits aptes à réfuter mes observations : cela signifierait que DeFi est plus sûre que je ne le pensais**.

---

Rappel : ce blog est **[l'un des rares sites web de l'espace à ne pas piller vos données](https://tokenbrice.xyz/fr/hello-world/)** : je n'utilise pas Google Analytics & autres trackers intrusifs.

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/c/DeFiFrance)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}

Un grand merci à Phil H pour sa relecture attentive de la version française de cet article et ses très nombreuses suggestions et corrections.

## IV. Notes et références

Vous pouvez trouver des informations complémentaires sur les fait, événements ou chiffres essentiels mentionné dans l'article en consultant les notes de bas de page :

[^1]: Je les ai notifié sur Twitter et [j'ai suggéré de nombreuses améliorations évidentes](https://twitter.com/TokenBrice/status/1360296967939772423?s=20) que toute personne ayant une certaine expérience de la DeFi aurait pu fournir.
[^2]: N'hésitez pas à le contacter si vous voulez réclamer la prime de 500 USDC ! [Voici le tweet](https://twitter.com/jack_clancy93/status/1360305374033682436?s=20)
[^3]: Pour en savoir plus sur cette attaque ou toute autre dans l'espace DeFi, **[check the Rekt](https://www.rekt.news/nxm-hugh-speaks-out/)**
[^4]: Trouvez **[plus d'informations sur l'abitrage de l'oracle 89M DAI sur Compound ici](https://decrypt.co/49657/oracle-exploit-sees-100-million-liquidated-on-compound)**
[^5]: Oui, il est factuel puisque le contrat n'a jamais échoué jusqu'à présent. Cependant, pour les personnes moins avancées techniquement, il peut se lire comme si Compound n'avait jamais subi de perte, ce qui n'est pas le cas. **[Robert Leshner Tweet](https://twitter.com/rleshner/status/1358566161361821696?s=20)**
[^6]: La proposition pour les subventions communautaire Compound a été [exécutée il y a deux mois](https://compound.finance/governance/proposals/30).
[^7]: [RoboVC](https://robvc.com/) : Il a financé plusieurs services exploitant Compound (comme InstaDapp ou Multis) et Compound lui-même.
[^8]: Jack, un de leurs ingénieurs a reconnu que [le cas du Compound DAI score > Aave n'est pas défendable.](https://twitter.com/jack_clancy93/status/1360304560846364672?s=20)
[^9]: [Documentation des développeurs sur les réserves de jetons](https://compound.finance/docs/ctokens#total-reserves)
[^10]: Il y a environ 450 000 dollars de tokens collectés dans la réserve à l'heure actuelle : [Documentation sur le facteur de réserve d'Aave](https://docs.aave.com/risk/asset-risk/risk-parameters#reserve-factor)
[^defiscore]: Dès le départ, la formule était faible, arbitraire et totalement en faveur de Compound à cause de l'importance donnée au temps d'opération. À mon humble avis, le principal but du [DeFiScore](https://defiscore.io/) était la promotion de Consensys : ils n'ont même pas assuré le minimum.
[^makerCBT]: L'équipe MakerDAO a publié un [compte rendu](https://blog.makerdao.com/the-market-collapse-of-march-12-2020-how-it-impacted-makerdao/) après les événements pour expliquer ce qui s'est passé.
[^aavegrants]: La première série de [subventions pour l'écosystème d'Aave a commencé il y a environ un an](https://medium.com/aave/aave-ecosystem-grants-88260ede1485)
[^nexusmutual]: Vous pouvez suivre les [réclamations et paiements sur Nexus Mutual ici](https://app.nexusmutual.io/claim-assessment).
[^compoundreserve]: Chaque cToken a une réserve (assurance) s'élèvant à 9,4 millions de dollars au total (et qui augmente de plus de 100 000 dollars par jour) [Robert Leshner Tweet](https://twitter.com/rleshner/status/1358566161361821696)
[^compoundCOMPstosk]: Compound est également assis sur un coffre de 4 millions de COMP (environ 1,8 milliard de dollars) qui pourrait être alloué à l'assurance [Robert Leshner Tweet](https://twitter.com/rleshner/status/1358569634618867714?s=20)
[^covershitcoin]: Cover est un protocole d'assurance incapable de garantir son propre token contract et son programme d'extraction de liquidités. Ils ont déjà été attaqués trois fois. Voici [quelques informations sur la dernière](https://coingape.com/cover-becomes-latest-defi-protocol-to-get-exploited-price-crashes-by-77-within-an-hour/).
[^compoundoracle]: Malgré l'attaque qui a eu lieu il y a plusieurs semaines en raison de leur dépendance aux oracles centralisés de Coinbase, il semble que [la situation n'a pas encore été corrigée](https://twitter.com/ChainLinkGod/status/1362132404484198401?s=20).
[^aTokenMasterRace]:Le cas de la supériorité technique des aTokens pourrait être le sujet d'un article à lui seul, mais en voici l'essentiel :

	1. **Simplification** : les aTokens maintiennent un ratio de 1:1 par rapport à l'actif de base tandis que les cTokens ont un taux de change croissant par rapport à leur actif de base.
	2. **Comptabilité et intégrations plus faciles** : la correspondance 1:1 des aTokens facilite grandement leur intégration - il n'est pas nécessaire d'aller chercher des données supplémentaires. Avec Compound, tout service interagissant avec des cTokens doit rechercher le taux de change cToken / jeton de base correspondant.
	3. **Intérêts dynamiques et compréhensibles** : les tokens a et c produisent des intérêts de manière dynamique. Cependant, là encore, en raison du design plus élégant et plus simple des aTokens, l'expérience est plus fluide avec les aTokens (dépôt, rassuré par la correspondance 1:1, le nombre augmente)
	4. **Intégrations plus puissantes** : aToken permet de nouveaux cas d'utilisation, surtout si vous prenez en compte les autres caractéristiques d'Aave. Par exemple, il existe un vault de Yearn qui utilise aLINK pour emprunter de l'USDC sur les dépôts des utilisateurs afin de farmer avec eux et de régler les revenus pour plus d'aLINK.

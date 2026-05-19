---
title: "Pharos : renseignement stablecoin gratuit, ouvert et de niveau recherche"
description: "Plus de 150 stablecoins suivis, monitoring du peg, scores d'alerte, notes de sécurité et liquidité : un bien public pour l'intelligence stablecoin."
date: '2026-03-12T01:13:50.191Z'
categories: [Projects]
tags: [DeFi, Stablecoins, Analytics, Public Good, Open Source]
url: pharos
aliases:
  - p/pharos
image: /img/2026/pharos/pharos-cover.png
toc: true
draft: false
type: post
difficulty: "intermediate"
---

Les stablecoins sont l'épine dorsale de la crypto. Selon toutes les métriques qui comptent, volume, utilisateurs, utilité réelle, ils sont ce que la DeFi a produit de plus réussi. Plus de 300 milliards de dollars de supply en circulation. Des centaines de milliards de dollars réglés chaque jour. Le pont entre la finance onchain et le reste du monde. Et pourtant, l'infrastructure d'information qui les entoure est embarrassante de pauvreté.

Vous voulez savoir si un stablecoin est sûr ? Bonne chance. Vous pouvez vérifier son prix sur CoinGecko, peut-être trouver une courbe de supply sur DeFiLlama. Pour les plus populaires, [Bluechip](https://bluechip.org/) fournit d'excellentes notes économiques. Mais à peu près rien de plus. **Il n'existe aucune façon systématique de suivre la stabilité du peg, d'évaluer la profondeur de liquidité, de détecter les signaux d'alerte, de suivre les événements de gel ou d'évaluer le risque sur les nombreux stablecoins maintenant en circulation.** La couche d'information est restée bloquée en 2021 alors que le marché est devenu dix fois plus complexe.

C'est important. Quand Terra s'est effondré, les gens n'ont compris que leur stablecoin était en danger que lorsqu'il était trop tard. Quand USDC a dépeggé pendant la crise SVB, la panique s'est propagée parce que personne n'avait une vision claire de l'exposition réelle. Chaque depeg suit le même schéma : l'asymétrie d'information bénéficie aux insiders et punit tous les autres.

J'ai donc construit [Pharos](https://pharos.watch).

![Page d'accueil du dashboard Pharos : Stability Index à 92,7 (BEDROCK), 329 milliards de dollars de supply stablecoin totale, 128 coins sur 148 au peg, titre du digest quotidien et table complète des stablecoins](/img/2026/pharos/pharos-homepage.png)

## Ce qu'est Pharos

Pharos est un dashboard d'analyse des stablecoins qui suit **156 stablecoins** à travers 18 devises de peg, plusieurs types de collatéral et différents modèles de gouvernance. Il surveille les pegs en temps réel, calcule des scores de risque composites, note la sécurité sur plusieurs dimensions, suit la liquidité DEX, détecte les signaux d'alerte précoce et publie un digest quotidien de marché généré par IA.

Le projet est entièrement [open source](https://github.com/TokenBrice/stablecoin-dashboard). Pas de compte. Pas de connexion wallet. Pas de monétisation, maintenant ou plus tard. **Pharos est un bien public** : gratuit, ouvert, et conçu pour donner à tout le monde le niveau d'intelligence stablecoin qui nécessitait jusqu'ici de construire sa propre infrastructure.

Si vous avez lu mon [article précédent sur la crise de la couche de curation de la DeFi](/defi-ux-disaster/), vous connaissez déjà la thèse : l'espace a désespérément besoin de meilleurs services d'information. Pharos est ma façon de mettre mon argent là où est ma bouche, littéralement. Le projet est entièrement autofinancé, construit en solo, et restera librement accessible.

## Penser les stablecoins correctement

Avant de surveiller intelligemment les stablecoins, il faut une taxonomie correcte. La plupart des dashboards traitent les stablecoins comme une liste plate : nom, ticker, supply, prix. Cela ne dit presque rien du profil de risque réel.

Pharos classe chaque stablecoin selon trois axes :

- **Modèle de gouvernance** : CeFi, CeFi-Dependent ou DeFi, selon la dépendance réelle à l'infrastructure centralisée, pas selon le narratif marketing. USDC est CeFi, évidemment. Mais DAI/USDS ? CeFi-Dependent : il a une gouvernance onchain, mais son backing est massivement lié à des actifs centralisés. Cette distinction est essentielle pour évaluer le risque.
- **Type de backing** : adossé à des RWA, adossé à des actifs crypto, ou algorithmique : ce qui soutient réellement le peg.
- **Devise de peg** : pas seulement l'USD. Pharos suit EUR, GBP, CHF, BRL, JPY, or, argent, tokens indexés CPI et de nombreuses autres monnaies. Toutes les supplies non USD sont ajustées FX pour que les totaux multi-devises soient significatifs, pas de simples sommes naïves en valeur faciale.

Cette taxonomie est fondatrice. Toutes les fonctionnalités de Pharos s'appuient dessus, parce que **vous ne pouvez pas évaluer le risque si vous ne comprenez pas d'abord ce que vous regardez**.

## Surveiller le peg

Le monitoring du peg semble simple : vérifier le prix et voir s'il est à 1 dollar. En pratique, c'est un cauchemar.

Les prix des stablecoins sont bruyants. Un seul CEX avec un carnet d'ordres peu profond peut produire un faux signal de depeg. Un gros swap sur Curve peut temporairement éloigner un prix du peg avant que l'arbitrage ne corrige. CoinGecko et d'autres agrégateurs rapportent parfois des données périmées. Si vous alertez naïvement sur chaque déviation de prix, vous vous noierez dans les faux positifs.

Pharos utilise un **pipeline de détection de depeg en deux étapes** :

1. **L'étape 1** tourne toutes les 15 minutes. Elle détecte les déviations de prix mais les valide contre les prix DEX pour supprimer les fausses alertes causées par une faible liquidité ou des données périmées.
2. **L'étape 2** s'active pour les stablecoins de grande taille (>1 milliard de dollars de supply). Elle exige une confirmation multi-source avant de déclarer un événement de depeg. Crier au loup sur USDT coûte de la crédibilité.

En plus de la détection, chaque stablecoin reçoit un **Composite Peg Score (0-100)** qui mesure sa stabilité dans le temps : depuis combien de temps il est au peg, combien de depegs il a connus, et quelle était leur sévérité. Cela transforme la question "est-il à 1 dollar maintenant ?" en une question bien plus utile : "à quel point reste-t-il fiable à 1 dollar ?"

![Pharos Depeg Tracker montrant la visualisation orbitale DEWS avec des stablecoins positionnés selon leur niveau de risque, 10 depegs actifs sur 148 suivis, et le Peg Leaderboard classant les coins par composite peg score](/img/2026/pharos/pharos-peg-tracker.png)

## Risque systémique : le Stability Index

Le monitoring individuel des pegs est utile, mais il manque la forêt derrière les arbres. Les moments vraiment dangereux en crypto ne sont pas ceux où un coin depeg ; ce sont ceux où la contagion se propage.

Le **Pharos Stability Index (PSI)** est un score composite de santé de l'écosystème (0-100) calculé toutes les 15 minutes. Il répond à une question simple : **à quel point l'écosystème stablecoin est-il sain maintenant ?**

Le PSI intègre :

- **Sévérité** : l'impact des depegs actuels, pondéré par la capitalisation. Un stablecoin de 50 milliards qui depeg de 2 % compte davantage qu'un stablecoin de 10 millions qui depeg de 20 %.
- **Largeur** : combien de stablecoins depeggent simultanément. C'est la contagion qui tue.
- **Largeur du stress** : combien de coins montrent des signaux de stress élevés via DEWS, décrit plus bas, même s'ils n'ont pas encore depeggé.
- **Tendance** : momentum de la capitalisation totale sur 7 jours. Les sorties de capital sont un indicateur avancé.

L'indice se mappe sur six régimes, de **BEDROCK** (tout va bien) à **MELTDOWN** (crise systémique). Pensez-y comme l'équivalent DeFi d'un rapport de stabilité financière, sauf qu'il se met à jour toutes les 15 minutes au lieu de chaque trimestre.

![Pharos Stability Index à 92,8 (BEDROCK), avec un graphique historique coloré du vert (BEDROCK) au rouge (MELTDOWN), et une timeline d'événements notables incluant Terra, USDC/SVB et FTX](/img/2026/pharos/pharos-stability-index.png)

Une décision de design mérite d'être notée : **les coins chroniquement dépeggés s'estompent progressivement de l'indice.** Un stablecoin hors peg depuis plus de 120 jours ne devrait pas dominer le score de sévérité pour toujours ; c'est une condition connue, pas une crise active. Ce "facteur de dépréciation" empêche les depegs zombies de masquer une instabilité fraîche.

Si vous êtes là depuis un moment, regardez l'historique du PSI : vous y verrez tous vos anciens traumatismes stablecoins reflétés par de grosses chutes de l'indice.

## Alerte précoce : DEWS

Le PSI vous donne l'état actuel. Mais qu'en est-il de ce qui arrive ? C'est le rôle du **Depeg Early Warning Score (DEWS)**.

DEWS est un score de stress prospectif (0-100) qui estime la probabilité de depeg en combinant huit sous-signaux :

- **Supply Velocity** : y a-t-il un schéma de bank run ? La fuite rapide du capital est le signal de danger le plus clair.
- **Pool Balance Drift** : les pools DEX deviennent-elles déséquilibrées ? Cela indique une pression de vente concentrée.
- **Liquidity Erosion** : les LP retirent-ils leur liquidité ? Quand les participants sophistiqués sortent, il faut prêter attention.
- **Price Confidence** : les sources de prix sont-elles fiables ou les données sont-elles dégradées ?
- **Cross-Source Divergence** : les différentes plateformes s'accordent-elles sur le prix ? Une fragmentation du pricing est inquiétante.
- **Blacklist Activity** : l'émetteur gèle-t-il des adresses en urgence ? Ce n'est jamais anodin.
- **Mint/Burn Flow** : y a-t-il une vague de redemptions ?
- **Yield Anomaly** : les schémas de rendement signalent-ils quelque chose d'anormal ?

Chaque signal est pondéré, supply velocity et pool drift ayant le plus de poids car ce sont les plus prédictifs, et le score composite se mappe sur cinq niveaux de menace, de **CALM** à **DANGER**.

Ce qui rend DEWS réellement utile, c'est son **amplificateur systémique**. Quand le PSI est sous 75, donc quand l'écosystème est déjà stressé, les scores DEWS sont augmentés jusqu'à 30 %. Cela capture une dynamique réelle : les vulnérabilités individuelles deviennent plus dangereuses quand tout le système est sous pression. Un stablecoin qui serait "WATCH" en conditions calmes peut devenir "ALERT" pendant une vente de marché généralisée, et c'est correct.

## Notes de sécurité

Les scores et indices sont utiles pour le monitoring, mais parfois il faut une réponse directe : **ce stablecoin est-il sûr ?** Pharos fournit des notes de sécurité multidimensionnelles, de A+ à F, sur cinq dimensions :

- **Stabilité du peg** : événements de depeg historiques, sévérité, streak actuel.
- **Liquidité** : disponibilité et profondeur DEX à travers les chaînes.
- **Résilience** : capacités de blacklist/freeze et vulnérabilité aux actions administratives.
- **Décentralisation** : modèle de gouvernance, risque de custody.
- **Risque de dépendance** : collatéral amont et dépendances de wrappers. Si votre stablecoin est adossé à un autre stablecoin, vous héritez de son risque.

Le résultat est un **bulletin** qui donne l'image complète, pas une simple note unique. Un coin peut avoir A en stabilité du peg mais D en décentralisation, bonjour USDC. Les dimensions sont visualisées sous forme de radar chart pour comparer les profils de risque en un coup d'oeil.

Pour les 17 stablecoins couverts par [Bluechip](https://bluechip.org/), Pharos affiche aussi leurs ratings SMIDGE indépendants aux côtés des siens : rien ne remplace une analyse manuelle comme celle de Bluechip, tandis que l'avantage du safety score de Pharos se trouve dans l'intégration en temps réel des données onchain et dans sa large couverture.

![Page Safety Scores montrant une barre de distribution des notes et une grille de cartes stablecoin, chacune avec un radar chart évaluant stabilité du peg, liquidité, résilience, décentralisation et risque de dépendance](/img/2026/pharos/pharos-safety-scores.png)

## Liquidité, rendements, gels et flux

Au-delà du framework de risque central, Pharos suit quatre dimensions supplémentaires importantes pour quiconque interagit sérieusement avec les stablecoins.

### Scoring de liquidité DEX

Le prix d'un stablecoin ne vaut rien si vous ne pouvez pas réellement le trader. Pharos calcule un **score de liquidité composite (0-100)** par stablecoin en agrégeant les données de pools de Curve, Uniswap V3, Aerodrome, DexScreener et plus encore. Il intègre la TVL, le volume, la composition des pools, la couverture cross-chain et le risque de concentration via HHI, le même indice que les régulateurs utilisent pour mesurer les monopoles de marché. **Un stablecoin avec 1 milliard de dollars de supply mais toute sa liquidité concentrée dans une seule pool sur une seule chaîne est fragile**, et le score le reflète.

### Intelligence de rendement

Pharos suit les **rendements ajustés du risque** pour plus de 40 stablecoins portant rendement et opportunités de lending. Le **Pharos Yield Score (PYS)** combine le niveau de rendement avec la note de sécurité, la constance et la soutenabilité. Un rendement élevé avec une mauvaise note de sécurité est pénalisé, parce que 20 % APY ne signifie rien si le protocole depeg ou se fait geler. Les sources de rendement sont résolues depuis plusieurs niveaux : exchange rates onchain, pools DeFiLlama, appréciation de NAV dérivée du prix et proxies de T-Bills. Chaque coin reçoit aussi des signaux d'avertissement, spikes de rendement, sorties TVL, données périmées, pour repérer les problèmes avant d'engager du capital.

### Tracker freeze & blacklist

USDC, USDT, EURC, PAXG et XAUT ont tous des capacités de gel ou de blacklist. Pharos suit ces événements sur 8 chaînes (Ethereum, Arbitrum, Base, Optimism, Polygon, Avalanche, BSC, Tron), avec une synchronisation toutes les 20 minutes. Vous pouvez voir quand des adresses sont gelées, combien a été affecté et si des actifs ont été saisis. C'est l'un des aspects les moins surveillés des stablecoins : **le pouvoir de geler est le pouvoir de confisquer**, et la plupart des utilisateurs n'ont aucune visibilité sur sa fréquence d'utilisation. Vous pouvez maintenant monitorer la censure quasiment en temps réel.

### Tracker mint/burn

Les changements de supply racontent une histoire. Pharos ingère les événements de mint et burn pour 81 stablecoins sur Ethereum, regroupés en flux horaires. Il calcule une métrique **Pressure Shift** (l'activité de burn actuelle comparée à la baseline 30 jours), un **Bank Run Gauge** (stress composite pondéré par market cap) et un détecteur **Flight-to-Quality** (quand le capital quitte les stablecoins risqués pour les refuges). S'il y a un bank run silencieux en cours, Pharos le fera remonter.

## Outils d'analyse

Les données ne sont utiles que si vous pouvez agir dessus. Pharos fournit trois outils d'analyse qui vont au-delà du monitoring passif.

### Outil de comparaison

Sélectionnez jusqu'à 5 stablecoins et comparez-les côte à côte sur toutes les dimensions : supply, prix, stabilité du peg, notes de sécurité, liquidité, DEWS, flux mint/burn. La comparaison inclut un graphique multi-séries, supply ou prix dans le temps, et un overlay radar pour les profils de sécurité. Vous pouvez exporter la comparaison en image pour la partager.

![Outil de comparaison montrant 5 stablecoins adossés à l'or (PAXG, Tether Gold, Kinesis Gold, Matrixdock Gold, DGLD) côte à côte avec leurs métriques clés, un historique de market cap et un radar chart superposé pour comparer les safety scores](/img/2026/pharos/pharos-compare.png)

### Dependency Map & analyse de contagion

C'est peut-être la fonctionnalité la plus unique de Pharos. La **dependency map** visualise les relations de collatéral entre stablecoins sous forme de graphe force-directed. Beaucoup de stablecoins sont adossés à d'autres stablecoins, ou à leurs versions wrappées, créant des chaînes de dépendance invisibles si elles ne sont pas cartographiées. Le **mode stress test** permet de simuler un échec : sélectionnez n'importe quel coin et voyez lesquels seraient affectés, et à quel point. Si USDC échoue, quels coins tombent avec lui ? Maintenant, vous pouvez le voir.

![Dependency map force-directed montrant les relations de collatéral entre stablecoins sur fond sombre, avec USDT et USDC comme noeuds centraux dominants et des dizaines de coins plus petits connectés autour d'eux](/img/2026/pharos/pharos-dependency-map.png)

### Le cimetière

80 stablecoins sont déjà morts. Pharos les documente tous : nom, cause de décès, peak market cap, nécrologie avec sources. C'est un cimetière qui sert à la fois d'archive historique et de rappel : **les stablecoins échouent plus souvent que la plupart des gens ne le pensent**, et comprendre comment ils ont échoué est un contexte essentiel pour évaluer ceux qui sont encore debout.

## Le digest quotidien

Chaque matin à 08:00 UTC, Pharos publie un digest de marché généré par IA qui synthétise les données de la nuit en un récit concis. Il s'appuie sur 12 sources de données : changements de market cap, depegs actifs, mouvements du PSI, activité de blacklist, signaux de supply velocity, transitions de safety grade, flux mint-burn, distribution du stress DEWS et plus encore.

Le digest s'adapte au régime courant : pendant les périodes calmes, il met en avant les changements subtils ; pendant les crises, il commence par les développements les plus urgents. Il est distribué via [Twitter/X](https://x.com/PharosWatch), le [canal Telegram](https://t.me/pharoswatch), et archivé sur le site. Pour des alertes plus granulaires (changements DEWS, événements de depeg, changements de safety grade), le [bot Telegram](https://t.me/PharosWatchBot) permet de s'abonner à des coins spécifiques et de régler ses propres seuils.

## Open source, bien public, gratuit pour toujours

Je veux être explicite là-dessus parce que c'est essentiel.

**Pharos n'a pas de monétisation, pas de token, et aucun plan pour l'un ou l'autre.** Tout le code est open source. Il n'y a pas de tiers premium, pas de fonctionnalités verrouillées, pas de "contactez-nous pour l'offre enterprise". Chaque métrique, score et dataset calculé par Pharos est librement disponible pour tout le monde. Une API est disponible pour tous.

C'est un choix délibéré. J'ai passé des années à défendre l'idée que la DeFi a besoin d'une meilleure infrastructure d'information, que la [couche de curation est sous-financée et sous-estimée](/defi-ux-disaster/). Pharos est ma réponse à ma propre critique. L'écosystème stablecoin est trop important et trop complexe pour que l'intelligence de risque soit enfermée derrière des paywalls.

Le projet est construit en solo et autofinancé. La stack technique (frontend Next.js, backend Cloudflare Workers + D1) est conçue pour garder des coûts d'exploitation minimaux tout en gérant l'échelle des données : plus de 20 cron jobs, plus de 15 sources de données, 68 migrations de base de données. L'architecture vise la soutenabilité comme bien public, pas la maximisation du revenu.

## Commencer avec Pharos

Si vous interagissez avec les stablecoins d'une façon ou d'une autre, trading, lending, fourniture de liquidité, construction de produits, Pharos vous donne la couche d'information qui vous manquait.

**Explorer :** [pharos.watch](https://pharos.watch) — nouveau ici ? Le [guide d'onboarding](https://pharos.watch/start/) vous fait découvrir chaque fonctionnalité.

**Source :** [GitHub](https://github.com/TokenBrice/stablecoin-dashboard)

**Rester informé :** suivez le digest quotidien sur [Twitter/X](https://x.com/PharosWatch) et [Telegram](https://t.me/pharoswatch), ou abonnez-vous à des alertes personnalisées via le [bot Telegram](https://t.me/PharosWatchBot)

Pharos continuera d'étendre sa couverture et d'affiner ses modèles. Si vous voulez contribuer, le repo est ouvert. Si vous voyez des problèmes ou avez du feedback, un formulaire est disponible sur le site.

Les stablecoins ont gagné la course à l'adoption. Il est temps que l'infrastructure d'information rattrape son retard.

PS : un concours d'une semaine de production de contenu (à partir des données Pharos) et de soumission de feedback est en cours, avec 3000 BOLD à gagner au total. [Participez](https://x.com/PharosWatch/status/2032107485629202921)

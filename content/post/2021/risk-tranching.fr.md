---
title: "🗡 Du risque ? Oui, mais juste un doigt"
description: "Introduction au tranching du risque, a son role dans les marches monetaires DeFi et a son importance pour Aave et Compound."
date: '2021-01-12T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Yield]
tags: [DeFi, Ethereum, Risk Management, Risk Tranching, Money Markets, DAI, aDAI, Saffron Finance, 88mph, Aave, Compound, Yearn, APWineFi]
toc: true
url: tranching-risque-defi
image: /img/2021/risk-tranching/cover.gif
difficulty: "intermediate"
---

La DeFi s'est considérablement développée au cours de l'année dernière, en partie grâce à l'apparition de produits d'investissement plus accessibles tels que **[les vaults](https://tokenbrice.xyz/fr/vaults/)** de Yearn ou de Harvest. Grâce à leur architecture, ils facilitent la mutualisation des capitaux, ce qui permet des investissements plus petits mais rentables sur les marchés monétaires et d'autres services DeFi comme Curve ou SushiSwap.

C'était une couche nécessaire et très appréciée, et plusieurs améliorations sont encore à apporter pour rationaliser encore plus les choses et augmenter l'efficacité en gaz. Toutefois, je pense que l'essentiel de l'innovation de cette année viendra d'un autre front : la gestion des risques sur les produits de type vault et les marchés monétaires en général.

En effet, plusieurs primitives financières ont été développées pour offrir davantage d'options de ségrégation et de couverture des risques. Il existe désormais des options d'assurance crédibles pour la DeFi, ainsi qu'une nouvelle approche pour mieux répartir le risque entre des acteurs consentants et informés : le tranching.

{{< notice info >}}
En français on parle aussi parfois de "sérialisation" mais ce n'est pas le plus explicite, je continue donc avec "tranching" pour le reste de l'article.
{{< /notice >}}

Nous allons nous y plonger, mais juste avant cela, je pense qu'il convient également d'examiner la terminologie.

---

## De protocoles de prêt aux marchés monétaires

Si vous me lisez depuis un certain temps, vous avez peut-être vu le terme "protocole de prêt" (_lending protocol_) utilisé. S'il convenait pour décrire leur premier objectif, je crois que le concept a maintenant dépassé le mot, je les appellerai donc désormais marché monétaire (_money market_). En effet, le terme "protocole de prêt" ne parvient pas à saisir toutes les subtilités qu'offrent aujourd'hui des services comme Aave - je suis en fait un peu en retard sur ce coup là.

Dans un sens, le changement de nomenclature reflète les différentes étapes de l'évolution de ces marchés monétaires. Dans leurs premiers mois d'existence, il y avait **un impératif de liquidité** : il s'agit essentiellement d'une lutte pour atteindre une taille importante, suffisamment grande pour justifier l'intérêt d'autres projets d'intégration au marché monétaire alimentant ainsi une boucle de croissance positive comme nous l'avons vu sur Aave.

![Aave TVL Growth - Debank](/img/2021/risk-tranching/aave-debank.png "Aperçu historique de la valeur totale bloquée sur Aave V1 - Debank")

Une fois que la masse critique est atteinte, **le centre d'intérêt peut et doit évoluer**. Pour continuer à se développer, le marché monétaire doit élargir sa gamme de caractéristiques - encore une fois, comme nous avons vu Aave le faire avec les flash loans et les emprunts à APR stables.

Il me semble clair à présent que **la deuxième phase de croissance des marchés monétaires sera axée sur les fonctionnalités**. En effet, les fonctionnalités de base disponibles sur le marché monétaire sont essentielles, car ces marchés sont davantage intégrés aux autres protocoles DeFi. Les marchés monétaires les plus flexibles au niveau de la couche de base pourront traiter des cas d'utilisation plus complexes, tels que la délégation de crédit.

Mais aujourd'hui, je souhaite axer cet article sur un concept de gestion des risques qui n'a pas encore trouvé sa voie vers un marché monétaire classique : le **tranching**. Voyons ce que cela apporte !

---

## Tranching : reprendriez-vous une autre tranche de risque ?

Commençons par **la "modification du risque" la plus simple qui soit : le tranching**. L'idée ici est assez simple : les différentes couches de risque prises par le déposant d'un marché monétaire donné sont réparties en tranches, c'est-à-dire séparées les unes des autres.

Chaque déposant peut choisir l'exposition qu'il préfère. Il permet, par exemple, à un dégénéré confiant de **supporter tous les niveaux de risque disponibles pour maximiser son rendement** tandis qu'une baleine plus conservatrice pourrait **réduire son périmètre de risque** en s'exposant au seul risque technique.

C'est l'idée de base, mais n'oublions pas que nous parlons ici de finance décentralisée, donc la **composabilité est la clé**. Ce qui rend le tranching si passionnant, c'est son avenir en tant que **primitive financière** - un élément de base que d'autres applications et projets peuvent utiliser pour fournir de nouveaux services.

Nous explorerons plus en profondeur ce que le tranching en tant que primitive financière implique juste après avoir examiné comment il fonctionne actuellement dans la pratique, et nous examinerons également le contexte plus large de la couverture des risques et de la fixation du taux d'APY.

{{< notice note >}}
Si vous êtes nouveau dans la DeFi ou même dans la finance en général, vous vous demandez peut-être pourquoi se soucier autant de la découpe du risque ? Pour dire les choses simplement, ces différents mécanismes de ségrégation de risques sont utiles pour fournir des produits adaptés à l'utilisateur final, quelle que soit sa propension personnelle au risque.

Je reviens plus explicitement sur l'utilité du tranching en fin d'article.
{{< /notice >}}

### La tranching de risque en pratique

Tout cet article a en fait été inspiré par un tweet que j'ai publié et dans lequel je partageais ce à quoi pouvait ressembler un aDAI tranché :

À ce jour, il y a principalement un produit qui fournit des tranches sur le mainnet que je regarde : [Saffron Finance](https://saffron.finance/). Il s'agit d'une couche d'abstraction de tranching construite sur le marché DAI de Compound. La séparation des risques est simple avec deux tranches principales + une :

1. La tranche **AA**, **couverte en cas de défaillance de la plateforme**.
2. La tranche **A**, qui fournit la couverture de la tranche AA (et subit donc des pertes en cas de défaillance), mais rapporte un **rendement beaucoup plus favorable**.
3. Il existe une troisième tranche - la **tranche S**. Cependant, elle rééquilibre simplement les deux autres en fonction des besoins.

![Les différentes tranches disponibles sur Saffron Finance](/img/2021/risk-tranching/saffron.png "Les différentes tranches disponibles sur Saffron Finance pour le marché  Compound/DAI")

Le découpage en tranches se fait sur une base d'_epoch_, actuellement fixée à deux semaines. Ainsi, si vous fournissez la tranche A, par exemple, vous supportez le risque de défaillance de la plate-forme pour la tranche AA pendant une période de deux semaines.

Grâce à l'enthousiasme qui a suivi le lancement, Saffron s'est développé pour atteindre près de 60 millions de dollars d'actifs déposés. Depuis lors, il y a eu un minimum de 15 millions de dollar d'actif déposé à tout moment sur le service.

![Saffron Finance TVL - Debank](/img/2021/risk-tranching/saffron-debank.png "Aperçu historique de la valeur totale bloquée sur Saffron Finance - Debank")

{{< notice note >}}
Sur le graphique, on peut voir des retraits importants : ils sont dus à la logique par _epoch_ de Saffron. À la fin de chaque _epoch_, les déposants doivent retirer leur liquidité et la déposer dans les tranches de la nouvelle _epoch_ pour continuer à générer un rendement.
{{< /notice >}}

Saffron cherche à s'étendre à d'autres marchés monétaires, en particulier à Aave et à étendre sa couverture en tokens (actuellement seulement DAI). D'autres projets explorent l'idée du tranching, notamment [BarnBridge](https://barnbridge.com/), mais leurs réalisations actuelles sont moins intéressantes à mes yeux.

*Edit de dernière minute : Le token de BarnBridge - [BOND vient d'être listé sur Coinbase](https://twitter.com/CoinbaseCustody/status/1348739247277268997).*

Maintenant que nous avons une compréhension plus pratique du tranching et de son fonctionnement, prenons un peu de recul pour comprendre ce qu'il apporte dans le contexte plus large de la gestion des risques dans la finance décentralisée.

---

## Le contexte plus large de la gestion du risque pour la DeFi

Jusqu'à présent, nous nous sommes concentrés sur le seul risque lié au produit financier lui-même : principalement les risques liés aux smart contracts, oracles et les attaques économiques. Nous avons laissé au moins deux niveaux de risque intacts :

1. **Variation du taux de rendement (APY)** : Le taux de rendement du service utilisé est généralement variable, il y a donc une couche d'exposition supplémentaire.
2. **Fluctuation des prix du token** : Parfois, les rendements sont payés en token différent de ceux déposés. Si le token de paiement n'est pas un stablecoin, son prix peut varier - ce qui signifie qu'il y a encore une couche d'exposition supplémentaire à prendre en compte ici si nous voulons être exhaustifs.

Par ailleurs, pour bien comprendre le contexte général, n'oublions pas qu'il existe plusieurs "approches temporelles" distinctes du risque :

* En utilisant une approche telle que le tranching, vous pouvez être **proactif**, en répartissant le risque **a priori** entre les participants qui comprennent leur exposition.
* Cela peut également aller de pair avec des approches plus **réactives**, comme l'assurance - un système prévoyant un paiement **a posteriori** en cas de défaillance.

Les marchés de l'assurance sont un autre sujet fascinant en soi, aussi nous nous en tiendrons à cette simple mention pour l'instant et revenons à nos rendements.

{{< notice note >}}
Pendant que nous parlons d'assurance, un projet fascinant vient d'être lancé : Unslashed Finance. Il est porté par un français que j'admire, donc je suis un peu partial, mais n'hésitez pas **[à lire le manifeste](https://medium.com/unslashed/manifesto-for-a-decentralised-crypto-insurance-unslashed-finance-873078fd0ddd)** à en savoir plus sur leur vision.
{{< /notice >}}

---

## La gestion des risques lié aux rendements : la fixation d'APY

Comme on le disait, les rendements des différents produits disponibles dans la finance décentralisée fluctuent constamment. Cela rend les revenus moins prévisibles et empêche l'entrée d'investisseurs qui ne sont pas prêts à supporter plusieurs niveaux de risque.

Pour résoudre ce problème, une autre couche de services méta-financiers est en train d'émerger - la proposition de valeur de base en tant qu'investisseur est assez simple : ils offrent un **un rendement stable sur les investissements des déposants**. Il s'agit essentiellement d'une autre saveur d'"assurance" : vous obtiendrez globalement un rendement un peu plus faible, mais il est prévisible. C'est très similaire à un prêt à intérêt stable sur Aave (par opposition à un taux variable).

Le côté acheteur de ces services est très intéressant : imaginez-le **comme un marché de prédiction, pour le rendement des vaults ou des marchés monétaires**. Les acheteurs déposent des actifs et parient sur le rendement moyen attendu : plus leur prédiction est proche, meilleur est leur rendement.

Je ne pense pas que le côté acheteur se généralisera de sitôt, mais il constitue **l'épine dorsale d'une primitive financière utile** pour fournir des services mieux adaptés à tout type d'investisseur.

### La fixation de rendement en pratique

Jusqu'à présent, deux projets visent à fournir un rendement fixe sur des produits d'investissement décentralisés populaires tels que les vaults de Yearn Finance : [APWine](https://apwine.fi/) & [88mph](https://88mph.app/).

Tout comme Saffron, 88mph est une autre couche d'abstraction construite sur les dépôts de Compound, Aave et Harvest. Elle fournit un **rendement fixe pour les déposants**, alors que de l'autre côté du marché, les acheteurs d'obligations à taux variable supportent le risque des fluctuations de rendement du produit d'investissement sous-jacent.

![88mph main interface](/img/2021/risk-tranching/88mph.png "Différentes opportunités à rendement stable sur 88mph")

---

## Prospection : quel avenir pour le tranching ?

Finissons avec une petite expérience de pensée. Nous allons maintenant quitter le présent et ce qui est actuellement en production sur le réseau principal d'Ethereum pour extrapoler un peu et examiner ce que le tranching et d'autres approches de gestion des risques peuvent permettre dans la DeFi d'ici quelques mois ou quelques années.

En supposant :

1. Un produit d'investissement construit, par exemple, sur le marché monétaire Aave :
2. Avec un produit de type Saffron intégré
3. Également avec un service de type 88 mph intégré
4. Enfin, une assurance telle que Unslashed également intégrée pour le peg ($1.00) du DAI.

On pourrait alors envisager **le premier investissement "sans risque" en DeFi**, qui serait un dépôt de DAI sur Aave, accompagné d'une répartition en tranches pour ne supporter que le risque de prix et protégé contre celui-ci par une couverture contre la perte du peg de DAI sur Unslashed.

Il est insensé d'envisager les différentes étapes de l'évolution du DAI dont nous avons été témoins ou dont nous sommes sur le point d'être témoins en à peine deux ans :

1. DAI
2. Un DAI **qui gagne des intérêts**
3. Un DAI qui gagne des intérêts **fixes et prévisibles**
3. Un DAI qui gagne des intérêts fixes et prévisibles, **non exposé au risque technique**
3. Un DAI qui gagne des intérêts fixes et prévisibles, non exposé au risque technique, et **couvert contre une perte de peg sur DAI**.

aFIXEDAPYDAI_PEGINSURED : notre nouveau maître de la monnaie ? Le vrai nom sera bien plus accrocheur, soyez-en sûrs !

Êtes-vous prêt à assister **à l'avenir de l'argent qui se déroule méthodiquement sous vos yeux alors que vos avoirs reçoivent des mises à jour logicielles** ?

Pour ma part, je ne peux pas attendre : je me prépare depuis trois ans.

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/c/DeFiFrance)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}

---

_Merci à Waël qui a réalisé l'image de couverture qui illustre cet article (et l'emblème TokenBrice)._

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

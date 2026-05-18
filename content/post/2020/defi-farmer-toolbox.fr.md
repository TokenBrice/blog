---
title: "🧰 Trousse à outils du cultivateur DeFi"
description: "Une liste d'outils et de conseils sélectionnés avec attention pour que vous puissiez tirer parti de la révolution agraire de la DeFi 🌻"
date: '2020-06-28T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Practical, Yield]
tags: [DeFi, Ethereum, Lending, Synthetic Assets, Liquidity Mining]
toc: true
tocNum: false
image: /img/2020/defi-farmer-toolbox/cover-fr.jpeg
difficulty: "intermediate"
url: defi-farmer-toolbox
---

Amis agriculteurs,

Si vous êtes ici, c'est que nous partageons une compréhension basique de [ce qu'est le yield farming](https://ethereumprice.org/guides/article/yield-farming/).

Vous avez peut-être même essayé par vous-même, ou entendu les [récits d'un producteur](https://defiweekly.substack.com/p/tales-from-a-yield-farmer) : incroyable ! Aujourd'hui, c'est à mon tour de partager les concepts clés et une liste d'outils pour vous aider à tirer parti de la révolution agraire sur Ethereum.

Si par hasard vous avez atterri ici sans avoir la moindre idée de ce qu'est [Ethereum](https://ethhub.io/) ou **[DeFi]({{< relref "definancial-services-guide.fr.md" >}})**, je vous invite à cliquer sur ces liens. Ceci n'est pas un guide, mais plutôt une sélection d'outils et de conseils. - Commençons !

## L'agriculture biologique DeFi

Autrefois, l'agriculture était simple : on plantait quelques graines et on espérait obtenir des rendements. Aujourd'hui, nous avons des **super graines**, ce qui nous permet d'obtenir des rendements supplémentaires en plus des commissions habituelles sur l'apport de liquidité ou de frais perçus sur les prêts.

De quelle facon ? Essentiellement parce que **certaines plateformes de la DeFi comme Compound ou Balancer incitent maintenant les utilisateurs à effectuer des actions essentielles au protocole**, comme fournir de la liquidité et emprunter sur Compound. Leurs utilisateurs sont récompensés par leur jeton natif de gouvernance (COMP dans le cas présent). La valorisation de ce jeton est une tâche difficile à laquelle les marchés s'attellent actuellement. Il faudra encore du temps pour que ces jetons trouvent leur prix.

Avant d'aller plus loin, il est donc temps d'écouter l'histoire de Stani, un agriculteur biologique et vendeur de tracteur/terres :

> Ce qu'il faut, c'est une agriculture durable. En substance, les agriculteurs devraient pratiquer des cultures de qualité en apportant des liquidités  à long terme et en conservant les semences de ces cultures pour étendre leurs exploitations à de nouvelles terres.
> - Stani Kulechov, PDG d'Aave [sur Twitter](https://twitter.com/StaniKulechov/status/1276093091624226816?s=20)

Nous y reviendrons plus tard, mais **le prix moyen élevé du gaz vous incite à choisir des cultures solides et à vous y tenir** au lieu de fouiller partout. Pour en savoir plus sur l'exploitation des liquidités, je vous recommande également de lire cet article sur le cadre du SAFG :

> Fondamentalement, le SAFG nous fait passer d'un monde où l'on "achète pour posséder" à un monde où l'on "participe pour gouverner", ce qui peut en fin de compte déboucher sur des protocoles plus efficaces et des communautés plus saines.
>- [Intro - Cadre du SAFG](https://medium.com/ideo-colab/meet-the-safg-defis-emergent-framework-for-participatory-investing-and-protocol-development-62286a576fb5)


### Sources de "Liquidity Mining"

Voici les principales sources de liquidity mining (apport de liquidité avec incitations supplémentaires), classées selon les jetons disponibles :

* Balancer Labs - [BAL](https://medium.com/balancer-protocol/proposing-balancer-liquidity-mining-cab4503972fa) - 100 millions de jetons au total, dont 75 millions distribués par le liquidity mining (75 %), depuis le 1er juin.
* Curve Finance - CRV ??? - il n'y a actuellement que peu ou pas d'informations publiques disponibles.
* Compound Finance - [COMP](https://medium.com/compound-finance/expanding-compound-governance-ce13fcd4fe36) - 10 millions de jetons au total, dont environ 4,2 millions disponibles via le liquidity mining (42%), depuis le 15 juin
* Universal Market Access - [UMA](https://defirate.com/safg/) ~ 35% de l'approvisionnement par l'exploitation minière (détails à déterminer)
* Programme d'incitation Synthetix & autres (comme JRT)
* Jarvis x Aave [Onramp Sponsoring Program](https://sponsoring.jarvis.network/) : redirigez les intérêts gagnés sur vos Stablecoins sur Aave pour gagner des jetons JRT. Jarvis a de nombreux autres programmes d'incitations, c'est un bon point de départ.

![Synthetix liquidity mining programs](/img/2020/defi-farmer-toolbox/synthetix-liquidity-mining.png)

### Adapter la stratégie à votre budget

Avant de voir comment entrer et sortir de telles positions, il est temps de discuter rapidement des prix du gaz. Ils ont été assez élevés ces derniers temps dans une fourchette de 25 à 35 gwei pour une transaction rapide. Voici en gros ce que cela signifie pour les opérations courantes :

* Dépôt @Compound (2 à 3 $ le gaz)
* Dépôt @Liquidity Pools @Zapper, un outil tout-en-un pour gérer vos positions d'apport de liquidités, plus d'informations à ce sujet ci-dessous (3-5 $ + frais de swap)
* Déposer @Liquidity Pools "manuellement" (0,3 $ (approuver) + 2-3 $ autant de fois que de jetons que dans le pool)
* La sortie a également un coût, ainsi que tout échange de jetons requis (comme la vente de votre COMP) : $1 à 3

#### L'impact des coûts du gaz sur les capitaux moyens ($ 2000)

**Examinons les rendements dans le temps d'un dépôt de 2 000 USDT @Compound**

Pour simplifier les choses, supposons que les paramètres actuels resteront tels quels l'année suivante. **C'est évidemment irréaliste - prenez cela comme une expérience de pensée.** Voici les paramètres au moment de la rédaction du document :

* 4% APY sur l'USDT sur Compound = 80 $ pour un an sur le capital
* 0,66 COMP/an =~150 $ produits par notre capital

Dans le tableau ci-dessous, la colonne "Profits réels" correspond à une sortie totale de la position (retour à l'USDT), ce qui signifie en fait 3 transactions au total pour l'opération :

1. Apport de liquidité sur Compound
2. Retrait
3. Vente des jetons COMP

Donc, si nous examinons cette position avec ces hypothèses sur plusieurs périodes, voici ce que nous obtenons :

| Période | Rendement Total ($) | Bénéfices Réels ($) | Retour effectif en % sur la période |
|:-----------:|:------------------:|:--------------------:|:---------------------------------------:|
| 1 jour | 0,63 $ | -8,37 $ | -0,42 % |
| 1 semaine | 4,42 $ | -4,58 $ | -0,23 % |
| 1 mois | 23,00 $ | 14,00 $ | 0,70% |
| 3 mois | 57,50 $ | 48,50 $ | 2,43 % |
| 6 mois | 115,00 $ | 106,00 $ | 5,30 % |
| Un an | 230,00 $ | 221,00 $ | 11,05 % |


*Remarque : ce scénario simpliste ne tient pas compte du coût d'opportunité sur le prix de l'ETH. 5 $ de gaz (=ETH) payés aujourd'hui pourraient valoir 10 $ d'ici un an.*

L'enseignement que je voulais partager ici est que **pour de tels capitaux, compte tenu des coûts actuels du gaz, il sera probablement préférable de s'en tenir à une position pendant des mois plutôt que d'essayer de courir après le meilleur rendement disponible**. Des bénéfices décents (~0,81 % /mois) commencent à se faire sentir dans un délai de trois mois.

Alors, vous vous souvenez de Stani l'agriculteur ? Vous devez choisir vos cultures avec sagesse.


#### Le terrain de jeu de la baleine (> 10 000 $)

Maintenant, si vous avez plus de capital investi et êtes prêt à vous exposer davantage, le coût du gaz devient moins prohibitif et vous avez plus d'options. Je ne m'étendrai pas sur ces points, quelques conseils suffiront :

Par exemple, vous pouvez tirer parti de l'effet de levier pour maximiser votre retour en COMP effectif (par des cycles d'emprunts / dépôts). Cela s'accompagne évidemment d'un risque de liquidation. Ce risque peut être plus restreint si vous utilisez la même cryptomonnaie pour votre collatéral que pour votre emprunt.
[InstaDapp](https://dsa.instadapp.io/compound) vous aide à maximiser les rendements du COMP en repliant votre position jusqu'à 4x voire plus mais ça reste difficile avec le prix du gaz actuel.

Dans un article précédent, j'ai détaillé une stratégie s'appuyant sur la plateforme Synthetix qui comprenait une autre forme de levier. Elle a permis d'observer des rendements impressionnants (~200% en réalité) depuis [son introduction il y a 5 semaines](https://tokenbrice.xyz/fr/definancial-guide/#5-a-le-synthetixcurve-kebb-alias-the-4-steaks-yieldburger) - principalement en raison d'une appréciation significative du prix du SNX (le prix a doublé), de la plus grande exposition de cette stratégie et du niveau très élevé d'activité sur le pool Curve sUSD.

![The Synthetix-Yieldbuger-TokenBrice](/img/2020/definancial-services-guide/yieldkebab.png)


Bon, assez de préparation - vous êtes maintenant un agriculteur averti - félicitations ! Examinons les outils utilisés pour planter vos semences, sécuriser vos cultures et récolter vos rendements.


### Entrer et sortir des positions

Vous pouvez entrer dans les pools de liquidité "manuellement", c'est-à-dire directement sur chaque plateforme. Il faut pour cela plusieurs transactions et un montant proportionnel d'au moins deux jetons, pour commencer. Sinon, vous devrez également au préalable procéder à des échanges en conséquence, en utilisant un service comme **[ParaSwap](https://paraswap.io)**. L'agrégateur ParaSwap vous permet de faire des échanges au meilleur prix mais également d'obtenir des jetons comme le cDAI (DAI stocké/gagnant des intérêts sur Compound) à partir de tout autre ERC20 ayant des trajectoires de gaz et de prix avantageux.

*Note : Balancer vient d'ajouter une fonctionnalité vous permettant d'apporter de la liquidité avec un seul token.*

Si vous n'êtes pas encore le plus familier avec Ethereum, la façon la plus simple de participer à ce festin serait d'utiliser des outils :

![Zapper.Fi-zap-in-liquidity-pools](/img/2020/defi-farmer-toolbox/zapper-fi.png)

**Entrer et sortir des pools de liquidité** : [Zapper.fi](https://zapper.fi) : dans l'onglet Invest, Zapper vous permet d'entrer et de sortir facilement des pools sur Balancer, Curve et Uniswap, de l'ETH, DAI et quelques autres jetons.

**Acheter de l'ETH & utiliser les services DeFi** comme Argent (gaz gratuit sur Argent pour certains protocols de la Defi pour l'instant !) - [Argent](https://argent.xyz)

**Spending ETH & Stablecoins** - [Monolith](https://monolith.xyz). Maintenant avec ParaSwap intégré pour les swaps et bientôt la possibilité d'acheter de l'ETH/ERC-20 à directement dans l'application !

![monolith](/img/2020/defi-farmer-toolbox/monolith.jpeg)

Pendant que nous y sommes, voici un petit conseil pour la route :
**Ça ne sert à rien de "Claim" sur Compound** C'est coûteux et vos jetons COMP sont automatiquement réclamés chaque fois que vous ajustez votre position en déposant ou en retirant des actifs (montant minimal de COMP réclamable requis).


## La boîte à outils essentielle de l'agriculteur DeFinancier

Maintenant que nous avons expliqué les bases, chers agriculteurs biologiques, il est enfin temps de jeter un coup d'œil à cette boîte à outils promise. Vous trouverez ci-dessous des outils qui vous aideront à suivre vos positions et les marchés et à analyser le rendement potentiel des stratégies que vous envisagez d'appliquer.

En plus de vous aider à entrer et sortir des pools, [Zapper.fi](https://zapper.fi) est un incroyable système tout-en-un de suivi de position DeFi. Voici [le Zapper du portefeuille](https://www.zapper.fi/synthetix?address=0x4E60bE84870FE6AE350B563A121042396Abe1eaF) du légendaire fermier [DegenSpartan](https://twitter.com/DegenSpartan) - on dirait qu'il a croqué dans le juteux burger :

![Zapper.fi - DegenSpartan](/img/2020/defi-farmer-toolbox/degen.png)

Si vous souhaitez obtenir un historique de votre wallet rendez vous sur **[Zerion](https://zerion.io/)**.

Pour une vue plus globale du marché, vous pouvez regarder :

- **[DeFiMarketCap](http://defimarketcap.io/)** pour voir les principaux jetons DeFi et leur prix.
- **[DefiPulse](http://defipulse.com/)** pour voir les principaux protocoles DeFi classé par la valeur totale des actifs verrouillés sur la plateforme.
- **[Token Terminal](https://www.tokenterminal.xyz/)** pour un aperçu des gains et du ratio P/E des protocoles DeFi
- [Ce tableau de bord **Dune Analytics**](https://explore.duneanalytics.com/public/dashboards/c87JEtVi2GlyIZHQOR02NsfyJV48eaKEQSiKplJ7) vous donne un aperçu du volume sur les DEXes :

![Aperçu des volumes sur les DEX](/img/2020/defi-farmer-toolbox/DEX.png)

⛽ Vous pouvez également utiliser [HAL](https://twitter.com/HAL_team) pour recevoir des notifications dans certaines situations, comme **[quand les prix du gaz passent sous un certain seuil](https://medium.com/@mattiascaricato/get-notified-when-gas-price-is-cheap-%EF%B8%8F-2a157a3d18b9)**.


### Ressources spécifiques à chaque plate-forme

**Synthetix / Yearn**

Il y a tellement d'oppurtinités qu'il peut être dur de les suivre ! Heureusement, les outils se développent rapidement aussi : **[yieldfarming.info](https://yieldfarming.info/) est très pratique** pour suivre les pools Synthetix/Yearn.

**Compound**

Vous trouverez un [aperçu des jetons COMP gagnés et réclamés (claim)](https://explore.duneanalytics.com/public/dashboards/JMB9bYfVUtMAPHM5moj7aIjLaDwos2k9JjJTtk64) ici. Utilisez cet outil pour [calculer les rendements attendus du COMP](http://www.predictions.exchange/compound/None) obtenus en fournissant ou en empruntant des jetons sur le protocole Compound.

**Balancer Labs**

Tout comme pour le COMP, vous pouvez estimer votre exploitation minière de BAL : **[Calculateur de la distribution de la BAL](http://www.predictions.exchange/balancer/%5B%5D)**. Si vous avez l'intention d'utiliser le Balancer, je vous recommande également de vous familiariser avec les **[BAL token distribution early shenanigans](https://thedailygwei.substack.com/p/striking-a-balancer-the-daily-gwei)**.

**RealT**

Les rendements de l'extraction de liquidités sont très variables, aussi, pour des rendements plus prévisibles, vous pouvez envisager d'utiliser des biens immobiliers tokénisés avec [RealT](https://realt.co). Voici deux principales ressources utiles : **[voir propriétaires et revenus](https://realt-dashboard.co/portfolio/0x51a7ead10340af963c3124b026b86dd2807c2b1c)** + **[Google Sheets pour suivre vos retours](https://realt.sigri44.com/)** - ces deux ressources sont réalisées par la communauté, alors n'hésitez pas à remercier leurs créateurs.

**Divers**

Vous pouvez **[suivre les marchés d'Aave en utilisant AaveWatch](https://aavewatch.now.sh/)**. Si vous êtes un utilisateur de TokenSet, **[TokenViz](http://tokenviz.io/)** vous aidera à comprendre leurs performance.


### Suivre l'actualité DeFi

Pour en savoir plus sur la DeFi, voici quelques ressources que je vous recommande :

- La **[Newsletter BanklessFR](https://banklessfr.substack.com//)**
- La **[chaine Youtube DeFi France](https://www.youtube.com/c/defifrance)**
- La discussion continue sur le **[groupe Telegram DeFi France](https://t.me/defifrance)**

## Le mot de la fin

Enfin, c'est la saison des subventions Gitcoin, alors permettez moi cette mention.

Vous suivez le développement d'Ethereum avec passion et attention ? Que diriez-vous de partager une petite part de vos retours, disons 2 %, pour soutenir des projets d'infrastructures essentielles & vos services DeFi ou vos producteurs de contenu préférés ?

Vos contributions sont grandement appréciées et peuvent avoir un réel impact, même 1 DAI grâce à la contrepartie du CLR. Donc si vous avez aimé cet article ou mes contributions à l'espace DeFi en général, n'hésitez pas à jeter un coup d'œil à **[mon grant Gitcoin](https://gitcoin.co/grants/811/tokenbrice-shining-light-on-ethereums-defi-en-fr)**.

Il m'aidera à financer davantage d'initiatives pour la communauté française et à poursuivre des efforts de production de contenu comme celui-ci. Chaque contribution fait la différence, même 1 DAI (actuellement égal à +5).

Maintenant que vous êtes sur Gitcoin avec une subvention dans votre panier, pourquoi ne pas en ajouter d'autres ? N'hésitez pas à regarder autour de vous et à soutenir des initiatives cruciales, des efforts de vulgarisation à la recherche fondamentale. Vous vous souvenez des luttes pour le gaz ? Vous pouvez **donner au [Fonds communautaire EIP 1559](https://gitcoin.co/grants/946/project-title-eip-1559-community-fund)** pour aider sur ce front aussi !
Et si vous souhaitez participer plus globalement vous pouvez donner au fond Gitcoin n°7, le suivant👍

Merci de votre lecture et bonnes récoltes !


### Remerciements

- Merci à [Jimmy](https://twitter.com/jimmyragosa) qui a contribué à ce que cet article soit aussi clair que possible.
- Merci à [Jon](https://twitter.com/OtherBright) pour son aide à la relecture de cet article.
- & Merci à [Antoine](https://twitter.com/AntoineMouran?s=09) pour sa relecture attentive de la version française et ses suggestions avisées.

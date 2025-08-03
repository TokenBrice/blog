---
title: "Effet de Levier pour gentilhomme : gains polynomiaux sans liquidations"
description: "Exploration d'un nouveau protocole offrant un effet de levier sans frais de financement ni liquidation avec des rendements convexes, et annonce de mon implication."
date: '2025-03-12T01:13:50.191Z'
categories: [DeFi, Projects]
tags: [DeFi, Ethereum, Finance Décentralisée, DeFi, Effet de Levier, Protocole Immuable, Prêt, Polynomial]
url: leverage-sir
image: img/2025/leverage-sir/leverage-sir-cover.jpg
---

Il y a quelques semaines, Sir Trading, une nouveau protocole DeFi fascinant et innovant, a été lancée, et je suis rapidement tombé amoureux. J'ai également décidé de m'impliquer, alors bienvenue dans cet article qui présente Sir Trading, explique ce que j'ai trouvé intéressant dans le modèle et annonce mon implication en tant que conseiller.

## Sir.Trading expliqué comme une entreprise

Pour comprendre Sir Trading (et cela fonctionne bien avec la plupart des protocoles), nous pouvons utiliser une métaphore d'entreprise : Qui sont les clients, les intermédiaires et les parties prenantes ?

![sir-diagram](img/2025/leverage-sir/sir-diagram.png)

Commençons donc par le bas : nos « clients » sont les APEs qui ouvrent des positions à effet de levier et paient des frais. Tout le reste est un « moyen » pour atteindre cet objectif.

Notre deuxième population est celle des « intermédiaires », les fournisseurs de liquidité sur le protocole Sir, appelés détenteurs de TEA, également appelés « gentlemen ». Ils sont nécessaires car plus il y a de liquidité TEA, plus la capacité des APE à utiliser l'effet de levier est grande, et donc plus les utilisateurs sont susceptibles d'ape à grande échelle. Maximiser cette population est essentiel, car cela aide à résoudre l'une des principales faiblesses du modèle Sir : **l'absence de dégradation de l'effet de levier ne peut être garantie que si la liquidité fournie est suffisante par rapport à la position à effet de levier ouverte.**

Il est donc logique d'inciter les fournisseurs de liquidité avec des émissions de SIR pour attirer une liquidité proportionnelle à la demande des APE. De plus, les récompenses continues en SIR offrent aux LPers un revenu stable, complétant les frais de minting/closing volatils qu'ils gagnent également — un avantage critique, car les LPers privilégient généralement la prévisibilité (cf. Aerodrome vs. Uniswap).

Enfin, les détenteurs de SIR agissent comme des parties prenantes. Ils peuvent staker leurs tokens pour recevoir des dividendes en ETH provenant des frais collectés lors de l'ouverture et de la fermeture des positions et, à l'avenir, pourraient être impliqués dans une mini-gouvernance centrée sur les décisions concernant l'allocation des ressources (⇒ quels vaults inciter avec les émissions de SIR ?).

Avec nos trois populations clés définies, nous pouvons essentiellement les assembler dans le « modèle d'entreprise » de Sir :

![sir-business-model](img/2025/leverage-sir/sir-business-model.png)

Le protocole SIR vise à maximiser sa base de clients (détenteurs d'APE), ce qui génère des revenus partagés avec les parties prenantes (détenteurs de SIR). Les parties prenantes approuvent les émissions de SIR pour financer les intermédiaires (LPers TEA) qui fournissent la liquidité nécessaire à cet objectif et l'allouent aux vaults les plus pertinents pour stimuler l'utilisation.

## Zoom sur le côté APE

Comme mentionné ci-dessus, le cœur du protocole est l'APE — la capacité d'utiliser l'effet de levier sur n'importe quel actif échangé sur UniswapV3. Mais qu'est-ce qui rend cet effet de levier si intéressant, surtout par rapport aux nombreuses autres options désormais disponibles ?

Le tableau ci-dessous devrait répondre aux questions les plus importantes pour quiconque est déjà familier avec d'autres protocoles offrant un effet de levier, tels que f(x) ou Squeeth :

<table>
  <tr>
   <td>Type de Rendements
   </td>
   <td>polynomial (=/ multiplicatif)
   </td>
  </tr>
  <tr>
   <td>Effet de Levier Max
   </td>
   <td>Jusqu'à ^5 sans dégradation de l'effet de levier avec une liquidité suffisante, réalistement ~ ^2
   </td>
  </tr>
  <tr>
   <td>Liquidation
   </td>
   <td>Aucune
   </td>
  </tr>
  <tr>
   <td>Rééquilibrage
   </td>
   <td>Aucun
   </td>
  </tr>
  <tr>
   <td>Frais
   </td>
   <td>Pas de frais de financement, seulement des frais fixes payés lors de l'ouverture ou de la fermeture de la position
   </td>
  </tr>
  <tr>
   <td>Actifs Supportés
   </td>
   <td>Potentiellement tout actif échangé sur UNIv3 + déploiement de vault permissionless
   </td>
  </tr>
  <tr>
   <td>Considérations de Sécurité
   </td>
   <td>Protocole devant être éventuellement entièrement immuable une fois sorti du mode Beta, oracle utilisé est sans confiance (UNIv3)
   </td>
  </tr>
</table>

Comme vous pouvez le voir ci-dessus, je pense que l'offre est assez convaincante même par rapport aux options existantes, bien qu'elle soit un peu « bizarre » si vous êtes habitué à d'autres produits d'effet de levier plus classiques, car vous devez vous familiariser avec quelques nouveaux concepts.

### Rendements polynomiaux ?!

Tout d'abord, abordons **la question de l'effet de levier linéaire (le plus courant) vs polynomial (cas de Sir)**. Si vous n'êtes pas un passionné de maths, je pense que la première chose à comprendre sur les polynômes est que leur impact est de plus en plus palpable à mesure que le prix s'éloigne du prix de départ. Il vaut mieux être prudent, car cela fonctionne dans les deux sens. Illustrons avec une position hypothétique simplifiée commencée lorsque ETH = 2000 $ (les frais sont ignorés pour simplifier ; nous y reviendrons plus tard) :

<table>
  <tr>
   <td>
   </td>
   <td>2500 $ (+25%)
   </td>
   <td>3000 $ (+50%)
   </td>
   <td>4000 $ (+100%)
   </td>
   <td>10000 $ (+400%)
   </td>
  </tr>
  <tr>
   <td>Linéaire - ETH x2
   </td>
   <td>3 000
   </td>
   <td>4 000
   </td>
   <td>6 000
   </td>
   <td>18 000
   </td>
  </tr>
  <tr>
   <td>Polynomial - ETH ^2
   </td>
   <td>3 125
   </td>
   <td>4 500
   </td>
   <td>8 000
   </td>
   <td>50 000
   </td>
  </tr>
  <tr>
   <td>Linéaire - ETH x5
   </td>
   <td>4 500
   </td>
   <td>7 000
   </td>
   <td>12 000
   </td>
   <td>42 000
   </td>
  </tr>
  <tr>
   <td>Polynomial - ETH ^5
   </td>
   <td>6 103,52
   </td>
   <td>15 187,5
   </td>
   <td>64 000
   </td>
   <td>6 250 000
   </td>
  </tr>
</table>

Vous voyez ce scénario de la dernière ligne/colonne, avec notre ape ETH^5 atteignant un Valhalla de plus de 6 millions de dollars sur une simple position de base de 1 ETH (avec une appréciation de prix de +400%) ? C'est le pouvoir des rendements polynomiaux. Ce que nous avons examiné ci-dessus est alléchant, bien qu'il abstrait de nombreux facteurs, y compris les frais, et suppose aucune dégradation de l'effet de levier pour les deux positions. Considérez cela comme un exemple pour comprendre la puissance du polynomial par rapport au linéaire dans un contexte financier plus que toute autre chose.

Les rendements polynomiaux (paiements convexes) ont historiquement été surpromis et sous-livrés. Les livrer de manière cohérente est généralement difficile, mais ils sont généralement mis en œuvre avec des **facteurs correctifs** de différentes natures et noms : dégradation temporelle, dégradation de la volatilité, dégradation de l'effet de levier, etc. Le modèle habituel pour un tel produit consiste à **gérer des prêts entre traders et prêteurs** pour maintenir l'effet de levier aussi constant que possible. Cela conduit à des modèles où les utilisateurs d'effet de levier diffusent constamment des frais variables aux prêteurs et voient encore leurs positions souvent rééquilibrées. Avec Sir, ce facteur correctif est clair et explicite dès le départ — c'est ce frais élevé, alors plongeons-y.

### Structure des Frais

Ensuite, le modèle de frais, qui est également assez différent de l'habituel. Les frais de Sir sont fixes, dépendent de votre effet de levier, et sont facturés à moitié lors de l'ouverture de la position (minting d'APE) et à moitié lors de la fermeture de la position (rédemption d'APE). À première vue, ils peuvent sembler assez élevés :

<table>
  <tr>
   <td>Effet de Levier
   </td>
   <td>Frais Totaux
   </td>
  </tr>
  <tr>
   <td>^1.5
   </td>
   <td>17,35% du principal
   </td>
  </tr>
  <tr>
   <td>^5
   </td>
   <td>69,13% du principal
   </td>
  </tr>
</table>

Zoomons sur une position ETH/USDC^1.5 pour mieux comprendre l'impact de l'effet de levier polynomial et des frais de Sir, avec une position hypothétique ouverte à ETH = 2000 $.

![sir-calculator](img/2025/leverage-sir/sir-calculator.png)

Avec ETH = 4000 $ (+100%), une telle position est en hausse d'environ 17% en termes d'ETH ou de 134% en termes d'USD. Bien sûr, à ce stade, vous êtes un expert en effet de levier polynomial, et donc vous comprenez que **l'écart entre l'ETH/USDC^1.5 et la détention brute d'ETH augmente plus le prix s'apprécie**. À ETH = 6000 $ (+200%), la position est maintenant en hausse d'environ 43% par rapport à ETH ou 330% par rapport à USD. À ETH = 8000 $, nous sommes maintenant à ~65% de gains par rapport à ETH et 562% par rapport à USD. Encore une fois, cela fonctionne de la même manière en sens inverse ; veuillez vous en souvenir.

Je pense que cela explicite bien le « but du jeu » avec Sir :

1. Idéalement, vous voulez saisir un bon creux + retournement pour ouvrir votre position à un prix favorable et gagner rapidement suffisamment de rendements pour couvrir les frais.
2. Votre objectif est ensuite de saisir l'écart maximal entre votre prix d'ouverture et de fermeture, sachant que chaque % que vous pouvez saisir fournit des rendements exponentiellement plus importants.

La conception du produit est bien adaptée à de telles opérations car vous n'avez pas à vous soucier des frais de financement ou de la dégradation temporelle. Vous cherchez essentiellement à acheter bas et vendre haut ; bienvenue dans la crypto : sauf que cette fois, vous avez un outil qui amplifie vos rendements plus vous parvenez à le faire.

En raison de sa structure de frais, **Sir est orienté vers les utilisateurs d'effet de levier ayant une perspective à long terme**, ce qui correspond à ses autres caractéristiques clés (pas de liquidation, pas de dégradation de l'effet de levier). Dans l'ensemble, les frais payés sont similaires à ceux qui seraient encourus en maintenant une position sur marge pendant un an, établissant un équilibre entre les rendements potentiels, la stabilité du protocole et les coûts initiaux. Lors de l'ouverture d'une position à effet de levier, l'une des principales préoccupations est de se tromper de timing et d'être haché par une action de prix en range, où les frais s'accumulent et emportent tout profit potentiel ; cette préoccupation est inexistante dans le modèle de Sir.

Enfin, je voudrais vous rappeler une fois de plus la principale limitation de Sir : l'absence de dégradation de la liquidité ne peut être assurée que s'il y a suffisamment de liquidité pour absorber votre trade. Bien qu'il soit **raisonnable de supposer cela pour les vaults incités ^1.25, ^1.5, ou même ^2**, cela devient beaucoup moins certain pour les vaults ^5, même avec de fortes incitations, en raison des maths que j'ai partagées ci-dessus.

Si vous souhaitez plus de données pour comprendre l'impact de l'effet de levier polynomial dans le contexte de Sir (=frais inclus), consultez [le nouveau calculateur sur le site de Sir](https://app.sir.trading/leverage-calculator).

Remarque : Les tokens APE sont des ERC-20 ; ainsi, une composabilité supplémentaire pourrait être envisagée. Cela pourrait devenir intéressant à mesure que le protocole se développe !

## Qu'en est-il des buveurs de TEA ?

Maintenant que vous avez une bonne compréhension du côté de la demande, les APE/utilisateurs d'effet de levier, passons de l'autre côté, les fournisseurs de liquidité/détenteurs de TEA.

Commençons par les bases : les buveurs de TEA font essentiellement du contre-trading par rapport aux APE, car ils fournissent la liquidité contre laquelle les APE rachètent s'ils parviennent à gagner et sécuriser (racheter) des gains importants. Quand je dis « contre-trading » ici, je veux dire de la même manière qu'un LP UNIv2_ETH/USDC contre-trade le marché : lorsque le marché achète principalement de l'ETH (⇒ le prix monte), les positions apportrices de liquidité se rééquilibrent vers l'USDC, et vice versa.

Donc, encore plus simplement, **les détenteurs de TEA sont plus courts par rapport à l'actif sous-jacent que s'ils le détenaient simplement**. Comprendre cela est tout ce dont vous avez besoin pour pouvoir projeter l'impact des variations de prix sur votre principal. Vous devez également **garder à l'esprit l'utilisation de la liquidité,** car si vous fournissez à un vault où il y a peu ou pas d'aping, vous contre-tradez peu ou personne, et votre exposition principale devient similaire à une détention brute de l'actif sous-jacent.

Bien que les détenteurs de TEA soient « plus courts » par rapport à une détention brute de l'actif sous-jacent, ils restent exposés à son appréciation de prix. Vous pouvez **penser aux détenteurs de TEA comme ETH/USD^0-1**.

Maintenant, avec le principal clarifié, abordons les gains en tant que détenteur de TEA. C'est assez simple : par défaut, **les détenteurs de TEA d'un vault donné gagnent collectivement tous les frais encourus par les minters d'APE**. Les frais sont gagnés en tant que tels (même token que le token fourni) et auto-composés. Les détenteurs de TEA peuvent les racheter en brûlant leur position pour récupérer leur principal + tous les frais accumulés.

En plus des frais gagnés en fonction de l'activité d'aping, **certains vaults sont également incités avec des flux d'émissions de SIR.** Ceux-ci incluent actuellement les plus utilisés : ETH/USDC1.5, wBTC/USDT1.5, SIR/ETH1.5 et SIR/ETH5. Lorsque les vaults sont incités avec des émissions de SIR, environ 10% des frais encourus par les APE sont redirigés vers les stakers de SIR.

Remarque : Les tokens TEA sont des ERC-1155, limitant la composabilité supplémentaire, ce qui est une bonne chose ici, car vous voulez éviter les situations de type restaking sur ces tokens, qui sont critiques pour le bon fonctionnement du protocole.

## Caractéristiques notables

Avec ce qui précède, vous devriez déjà avoir une bonne compréhension du protocole, donc plutôt que de vous ennuyer avec des explications expansives de chaque subtilité, je vais plutôt zoomer sur quelques fonctionnalités de Sir que j'ai trouvées dignes de commentaire :

### Maximisation de l'absence de confiance

Les lecteurs de mon blog ne seront pas surpris de trouver une section abordant cela, car la décentralisation maximale et l'absence de confiance sont mes mantras. À cet égard, Sir Trading s'en sort plutôt bien, et la conception démontre la priorité accordée à ces deux sujets par ses fondateurs.

Commençons par le plus important — le potentiel d'immuabilité du protocole. Compte tenu de son approche novatrice et des risques associés, rendre le protocole immédiatement entièrement immuable pourrait être inconséquent. Au lieu de cela, l'approche développée ici est un chemin progressif vers une immuabilité éventuelle avec quatre modes :

![sir-beta-mode](img/2025/leverage-sir/sir-beta-mode.png)

Sir est actuellement en mode Roues d'Entraînement, dans lequel certains paramètres, tels que les frais, peuvent encore être ajustés. À partir du mode Roues d'Entraînement, il peut passer en mode Urgence en réponse à un bug ou à une exploitation et de là à un Arrêt (⇒ Redéploiement) si nécessaire. D'un autre côté, si tout se passe bien, les roues d'entraînement peuvent être retirées, et le protocole peut être basculé en mode Imparable, où il devient immuable. Je trouve cette approche équilibrée et intéressante, [définitivement digne d'étude](https://docs.sir.trading/protocol-overview/beta-period) pour d'autres constructeurs.

Maintenant, regardons la solution d'oracle choisie, un élément critique pour tout protocole basé sur le prêt ou l'effet de levier. Ici, **la solution est simple et entièrement sans confiance : Uniswap v3.** Elle a bien sûr des limites, notamment la liquidité disponible sur Uniswap pour garantir que le prix ne soit pas facilement manipulable. Cependant, compte tenu que les principaux vaults sont des majors comme ETH ou wBTC, ce n'est pas une grande préoccupation. Cela pourrait être plus problématique pour les vaults liés à SIR, mais ici encore, la liquidité est raisonnablement suffisante par rapport à la capitalisation du token (TVL dans les pools > 35% FDV). Une atténuation supplémentaire est mise en œuvre sur l'oracle UNIv3 (TWAP de 30 min) pour mieux résister à la manipulation des prix.

Une autre fonctionnalité intéressante en termes d'absence de confiance et de résilience est l'**exploitation des [enchères de tokens](https://docs.sir.trading/protocol-overview/token-auctions) pour rationaliser la distribution des frais aux stakers**. Sir est loin d'être le seul à faire cela, car, par exemple, [Euler Finance exploite une logique similaire](https://docs.euler.finance/developers/periphery/fee-flow/). De telles enchères permettent la conversion de nombreux actifs en un seul (dans ce cas, wETH) sans ajouter de compromis inutiles au protocole. Je m'attends à en voir encore plus.

Remarque : Xatarrer (fondateur) a soumis lui-même une revue DeFiScan pour Sir Trading, qui est actuellement en cours d'examen. Veuillez consulter [DeFiScan](https://defiscan.info/) une fois la revue publiée pour plus de détails concernant la décentralisation de Sir.

### Liquidité Possédée par le Protocole

La liquidité est le sang vital de Sir, et la conception du protocole le reconnaît avec **un accent particulier sur la croissance des réserves de liquidité permanente (TEA)**. Chaque dépôt de fournisseur de liquidité comprend des frais (~8,99% de leur principal) retenus comme liquidité permanente possédée par le protocole. Ainsi, inciter les LPers avec SIR n'est pas seulement « louer » de la liquidité — c'est aussi un « rachat » partiel immédiat de leur dépôt.

Grâce à cela, à mesure que le protocole se développe et peut attirer plus de fournisseurs de liquidité, il construit des réserves de liquidité permanente, permettant une « liquidité minimale garantie pour les APE » toujours croissante. C'est essentiellement une boucle vertueuse résolvant progressivement l'un des principaux inconvénients du modèle : élégant !

### Modèle d'Émission de Token Continue

SIR fonctionne sous un **modèle d'émission constante au taux de 2015M SIR par an**, avec la part du lion allant toujours à l'incitation des fournisseurs de liquidité. Il y a cependant un changement dans la logique de distribution, fait pour donner au protocole les moyens de sa croissance initiale dans les trois premières années :

* Pour les 3 premières années, 68,13 % dirigés vers les fournisseurs de liquidité, 13,65 % vers les contributeurs pré-mainnet, 10 % réservés dans un trésor, et 8,22 % vers les investisseurs.
* Après cela : 100% vers les fournisseurs de liquidité.

Ce modèle est efficace, car aucun vesting n'est nécessaire pour l'équipe/les investisseurs/le trésor, puisque la logique est entièrement décalée ici : vous devez penser en termes de flux de tokens (X SIR/jour) plutôt qu'en solde total et vesting associé.

## Mettre votre compréhension en pratique

Pour conclure, nous pouvons maintenant articuler notre compréhension partagée du protocole en étudiant trois hypothèses de marché différentes articulées en stratégies :

### « Je suis haussier sur ETH ou BTC sur un horizon de temps moyen/long »

Celle-ci est la plus simple ; il suffit de minter le token APE ETH/USDC^1.5. L'absence de liquidation et de frais de financement vous permettra de définir cette position et de l'oublier. **Votre principale métrique à surveiller ici est le frais d'ouverture + fermeture à 17,35% : vous devez saisir une appréciation de prix d'environ 26% sur ETH pour entrer en territoire de profit**, avec vos gains augmentant de manière polynomiale à partir de là.

Variantes :

* Je suis haussier sur BTC : tout pareil, sauf en utilisant l'APE wBTC/USDT^1.5 (vault principal : bonne quantité de liquidité disponible).
* Je suis haussier sur ETH contre BTC et je cherche de l'adrénaline : tout pareil, sauf en utilisant le vault wETH/wBTC^5 (attention, faible liquidité actuellement)
* Je suis haussier sur SIR contre ETH : vous avez plusieurs niveaux d'effet de levier disponibles pour exprimer cette conviction onchain (SIR/ETH^1.5 et SIR/ETH^5 étant les plus liquides).

### « Je suis baissier sur ETH sur un horizon de temps moyen/long »

Vraiment ?! Pas de jugement ; il y a aussi un vault pour cela, au nom de USDC/wETH^1.5 ! Parce que ce vault est basé sur USDC, contre ETH, ouvrir une position APE là-bas signifie shorter ETH avec un effet de levier polynomial.

Inversement, fournir ce vault en tant que fournisseur de liquidité (TEA) signifie contre-trader les (potentiels) shorters ⇒ être long ETH (s'il y a utilisation), mais à partir d'une base USDC cette fois. Cependant, ce vault n'est pas actuellement incité avec des émissions de SIR, donc vos gains proviendront uniquement des positions ouvertes par les APE.

### « Je suis haussier sur SIR, mais pas vraiment un APE avide d'effet de levier »

C'est compréhensible ; tout le monde n'est pas un maximisateur de sensations fortes. Ici, vous pourriez envisager **d'exploiter les émissions constantes aux fournisseurs de liquidité pour construire votre réserve de SIR au fil du temps et seulement au coût d'opportunité du capital**. Compte tenu des frais de fourniture LP, vous êtes « forcé » de maintenir la position pendant quelques semaines/mois pour réduire l'impact des frais. Si vous êtes inquiet de la dépréciation du principal en cas d'un important retournement de marché à la hausse, vous pourriez envisager de répartir vos dépôts sur plusieurs vaults incités pour vous en prémunir.

En supposant que vous farmiez initialement avec un dépôt d'ETH ou de wBTC, vous avez une option de composition avec votre SIR fraîchement farmé : fournir les vaults SIR. Envisagez également de staker votre SIR pour maximiser une position SIR à moyen/long terme.

## Discussion de Mon Implication

Avant de vous quitter, j'aimerais vous donner plus de contexte sur mon implication avec Sir : Je conseille l'équipe de Sir pour les aider avec mes sujets principaux : croissance, optimisation de la tokenomie et développement commercial. Je suis rémunéré pour cet effort, et je suis également un détenteur d'APE et de TEA, et donc un farmer de SIR — **Je suis long SIR de toutes les manières possibles**.

J'ai découvert Sir assez récemment (le protocole n'a que quelques semaines), mais le timing était excellent. Comme ceux qui me suivent sur Twitter le savent probablement déjà, j'ai été profondément déçu par f(x), où j'ai subi une liquidation abusive découlant de lacunes infrastructurelles de leur côté (RPCs).

J'étais, depuis lors, à la recherche d'une solution alternative à f(x) et je suis tombé sur Sir, qui offre des fonctionnalités similaires (« vraie » absence de liquidation, pas de frais de financement) mais apporte également des ajouts bienvenus au mix, comme l'effet de levier polynomial vs linéaire : à la fois le protocole et le timing étaient parfaits, donc faire un effort supplémentaire pour aider à son succès s'est produit très spontanément.

Je n'aborde pas le conseil comme un objet de collection à ajouter à mon portefeuille, à montrer dans 2 appels mensuels, à collecter le paiement et à en rester là. Je suis à l'opposé, tout aussi engagé, impliqué et sélectif avec eux.

Avec Sir, compte tenu de la récente du protocole, mes contributions actuelles tournent autour de la sensibilisation au protocole, de son intégration dans l'écosystème et de l'explicitation de ses avantages au plus grand nombre possible, comme cela a été fait avec cet article. J'exploite mon expérience extensive en DeFi, mon réseau et ma présence pour soutenir l'équipe de toutes les manières pertinentes.

### Ma position « Valhalla ou enfer, rien entre les deux »

[J'ai ouvert une position SIR^5 sur mon portefeuille public tokenbrice.eth](https://etherscan.io/tx/0x5f9038d9004b53501bdf05b3f30d8fc8fd2d8da6a89299a624276c7605bf4ea7) — n'hésitez pas à la suivre : 500K SIR avec un effet de levier ^5 ⇒ rachetable pour ~155K SIR à l'initiation (~69% de frais), ouverte le 4 mars 2025 à 20:34:47 UTC. Si tout se passe bien, j'espère éventuellement racheter cela pour ~8M SIR (⇒ SIR à 2x mon prix de départ, en supposant une liquidité suffisante) et faire quelque chose d'amusant avec. **Je veux vous rappeler qu'un tel effet de levier est ce qui se rapproche le plus de la folie onchain ; cette position est maintenant connue dans la communauté comme « Valhalla ou enfer, rien entre les deux »**.

Remarque : En tant que protocole construit pour la résilience, [Sir est également soutenu par le DeFi Collective](https://x.com/DeFiCollective_/status/1897575989032497390), qui a reçu un don de SIR, l'a assorti d'ETH, a initié et fourni le LP UNIv2, et a verrouillé le token LP pour un an afin de sécuriser une base de liquidité pour le token.

Avertissement : Cet article et la stratégie ci-dessus ne sont pas des conseils en investissement mais des illustrations pratiques de ce que le protocole peut faire. Vous prenez vos propres décisions, et vous en êtes responsable. Au cas où cela n'était pas assez clair avec les avertissements précédents : Je suis exposé à SIR en tant que token et protocole et je bénéficie de sa croissance ; en d'autres termes, je suis aligné au maximum.

---
title: "Le cauchemard UX de la DeFi : comment la curation pourrait sauver l'innovation"
description: "Où je révèle le sombre secret de la DeFi : la crise de la couche de curation - et ce que nous pouvons faire pour y remédier."
date: '2025-03-08T01:13:50.191Z'
categories: [Thesis]
tags: [DeFi, Ethereum, Decentralized Finance, DeFi, Public Good, DeFiScan, BlueChip, L2Beat]
url: defi-ux-disaster
image: /img/2025/defi-ux-disaster/defi-ux-disaster-cover.png
difficulty: "beginner"
---

Tout le monde se soucie des couches d'applications et d'infrastructures, et c'est mignon, mais qu'en est-il de la couche de curation ? Sans elle, les deux autres sont presque inutiles, car la complexité de l'espace est déjà bien trop grande pour que la plupart des gens puissent la gérer. Aujourd'hui, je veux plaider pour combler la plus grande lacune de DeFi, éclairée par mon expérience de plus de six ans à éduquer les gens à ce sujet, à onboarder à peu près tous ceux qui le souhaitaient dans mon entourage et en ligne, et à faire un suivi avec eux.

## Définir les trois couches : infrastructure, application et curation

Avant d'aller plus loin, nous devons nous aligner sur les termes clés – ces trois couches. Une image vaut mille mots, alors étudions un exemple réel et intéressant qui présente des éléments de chacune des trois couches :

![jumper-exchange](img/2025/defi-ux-disaster/jumper.png)

Il s'agit d'un flux assez dense impliquant :

- Réseau principal Ethereum (infrastructure)
- wBTC (application)
- Bridge Mayan (infrastructure)
- Aave sur Optimism (application)
- USDC (application)
- Jumper (application + curation), utilisant Li.FI (infrastructure).

Faire cela « manuellement » représenterait une série d'opérations conséquentes :

1. Approuver wBTC sur l'échange
2. Échanger wBTC contre USDC sur mainnet
3. Approuver USDC sur le bridge
4. Bridge USDC du réseau principal vers Optimism
5. Approuver USDC sur Aave/Optimism
6. Déposer USDC sur Aave/Optimism

Hourra ! Voilà pour la couche applicative qui opère sa magie ! Mais j'aimerais me concentrer sur une autre dimension encore plus critique ici - la dimension curation de Jumper :

Jumper a automatiquement détecté les tokens que j'avais dans mon portefeuille dès que je me suis connecté, me permettant de trouver rapidement mes wBTC. Il a trouvé deux bridges potentiels et en a « recommandé » un en le plaçant en premier (parce qu'il a les meilleurs rendements). Il a trouvé les contrats des tokens respectifs et le protocole dont j'avais besoin. Il m'a également fourni une interface pour exécuter tout cela sans me soucier de savoir si j'étais sur le point d'envoyer mes tokens à un escroc — cela peut ne pas sembler grand-chose pour vous ou moi, mais pour un normie, c'est presque tout.

Donc, à partir de cet exemple, prenons une minute pour fixer les définitions :

1. **Couche d'infrastructure : la couche de base**, qui peut inclure les blockchains (Ethereum), mais aussi des éléments d'infrastructure sur lesquels on construit à la couche suivante (scénario Li.Fi>Jumper).
2. **\>> Couche applicative : la couche pour l'utilisateur final**, où ils interagissent réellement avec DeFi – cela inclut tous les protocoles, frontends et outils (DeBank, DeFiSaver, Jumper, etc.) que vous connaissez.
3. **\>>>> Couche de curation : la couche de « conseils »**, aidant les utilisateurs à naviguer parmi les options disponibles avec la couche applicative. Bien qu'elle existe indépendamment, ses informations et conseils peuvent et doivent être intégrés dans la couche applicative.

Cette perspective est essentiellement une version simplifiée du [DeFi Stack de Schär](https://www.researchgate.net/figure/The-Decentralized-Finance-DeFi-Stack_fig4_340061422) où ses couches "Settlement" et "Asset" sont fusionnées dans ma couche Infrastructure, ses couches "Protocol"+"Application" dans ma couche Application, et sa couche "Aggregation" est élargie et rebaptisée dans ma couche Curation :

![Schar-defi-stack](img/2025/defi-ux-disaster/defi-stack.png)

Les champions de la couche Curation, en plus des outils largement utilisés avec un élément de curation/répertoire tels que [CoinGecko](https://coingecko.com/) (aidant les utilisateurs à valider les contrats de tokens et les URLs des frontends des protocoles), [Jumper](https://jumper.exchange/) ou [Debank](https://debank.com/), sont actuellement des sites web/frameworks fournissant des informations essentielles et vérifiables sur des verticales clés telles que [L2Beat](https://l2beat.com/) (évaluation de la décentralisation des L2), [DeFillama](https://defillama.com/) (données DeFi + répertoire), [Bluechip](https://bluechip.org/) (évaluations économiques des stablecoins), [DeFiSafety](https://www.defisafety.com/) (évaluation des pratiques de développement) ou [DeFiScan](https://defiscan.info/) (évaluation de la décentralisation des protocoles).

La curation peut inclure diverses initiatives :

- **Validation** : Aider les utilisateurs à vérifier la validité des informations, comme CoinGecko agissant comme une source de vérité pour les adresses de contrats ou DeFillama pour les URLs des frontends des protocoles, ou les divers avertissements de Rabby aidant les utilisateurs à réaliser s'ils interagissent avec une version spoofée d'un protocole donné.
- **Agrégation** : La curation est fournie en plus de l'agrégation (« voici la meilleure route »). Cela inclut tous les DEX et agrégateurs de bridges (ParaSwap, CowSwap, Bungee, Jumper, etc.).
- **Informations vérifiables** : Les fournisseurs de services d'information comme L2Beat, DeFiScan ou Bluechip permettent aux utilisateurs d'accéder à des informations contextualisées et vérifiables (onchain et par rapport à leur framework respectif) dans leur verticale donnée.

## La couche de curation : le talon d'Achille de DeFi

Si vous n'êtes pas convaincu de l'urgence d'une meilleure couche de curation, je vous supplie d'onboarder votre maman à DeFi, de lui expliquer les bases d'un portefeuille, de lui envoyer quelques ETH, et de la regarder se gratter la tête.

Tu veux échanger ? Bien sûr, nous avons 200 DEX, 20 agrégateurs, des agrégateurs d'agrégateurs, et aussi ces nouveaux agrégateurs de bridges qui gèrent maintenant les échanges, ah et n'oublions pas les protocoles basés sur les intents ; au fait, tu savais que vous peux également échanger indirectement en fournissant une pool UNIv3 ? Alors, lequel allez-tu choisis ? Oh, tu as entendu parler d'Uniswap ? D'accord, essayons ça. Non, maman, ne clique pas sur ce premier lien dans les résultats de recherche ; ce n'est pas le vrai Uniswap. « Mais c'est écrit Uniswap »...

### La curation est la pièce manquante pour l'onboarding de masse

**Quel a été la plus grande aide lors de l'onboarding des gens ? Ce n'est pas Aave, Eigen, ou les dernières chaînes excitantes comme Bera ou Abstract. C'étaient des outils simples, directs et faciles à utiliser comme DeBank ou Jumper.** En plus de l'utilité, les deux agissent également comme une mini couche de curation : DeBank aide les utilisateurs à connaître leurs positions et leur fournit un lien sûr et vérifié vers les frontends des protocoles.

Jumper a essentiellement rendu le bridging accessible à un normie. Avant Jumper, ils devaient connaître les divers bridges disponibles pour un itinéraire donné, trouver en toute sécurité leur site web et non une copie de phishing assise en haut de la requête associée grâce à Google Ads ; et si leur token était un peu « exotique », ils devaient également être familiers avec le flux de recherche, copie et collage de l'adresse du contrat. Tout cela a été abstrait dans une interface simple et sûre à utiliser, rendant les novices en DeFi immensément plus à l'aise avec le monde multichain. J'en ai été témoin de première main avec mes apprentis ; il y avait un avant et un après Jumper dans ce qu'ils pouvaient accomplir de manière autonome sans s'inquiéter.

Bien que DeBank et Jumper aient des composants de curation, ce n'est pas leur principal objet. Si nous voulons élargir la base d'utilisateur qui peut exploiter DeFi, **nous devons accentuer l'effort sur la curation**, avec des applications et services dédiés bien intégrés avec les principales passerelles que les utilisateurs exploitent déjà (portefeuilles, trackers de portefeuille, agrégateurs, etc.).

## Comment en sommes-nous arrivés là ?

Pour les lecteurs paresseux, je vais le dire directement : **les piliers de DeFi nous ont laissé tomber** – c'est-à-dire les principaux protocoles, institutions et autres acteurs bien financés de l'espace.

**Pensez à ces protocoles éminents comme Aave, Uniswap ou Maker et leurs DAOs associées : les avez-vous déjà vus financer quelque chose qui ressemble de près ou de loin à un bien public DeFi ?** Pensez aux grandes fondations de layer 2 ou layer 1 ; les voyez-vous entretenir de telles initiatives ? Le plus proche que nous ayons eu était peut-être avec Uniswap et le DeFi Education Fund, mais il a des limitations ; son champ d'action est principalement le lobbying pour les réglementations, et il reste [des préoccupations non adressées concernant son financement et sa transparence](https://gov.uniswap.org/t/demand-for-transparency-from-defi-education-fund/13299).

La seule exception ici serait que DeFiLlama a été initialement financé par d'anciens membres de l'équipe Curve. Cependant, cela a été fait à titre personnel, pas au nom de Curve Finance : néanmoins, **cela mérite des éloges, car cela montre une préoccupation authentique pour le bien commun de la DeFi**, et pas seulement pour le succès de Curve — une initiative généralement cruellement absente dans DeFi, et la principale raison à l'origine de notre situation actuelle.

Pour mieux illustrer cela, laissez-moi vous raconter une histoire. Lorsque le [DeFi Collective](https://deficollective.org/) n'était encore qu'une idée, nous avons contacté diverses équipes que nous pensions alignées sur nos valeurs pour leur proposer de faire un don au Collective. Notre idée principale et notre pitch étaient que :

1. Le DeFi Collective aidera la véritable DeFi à prospérer
2. Si vous êtes un protocole de premier plan, vous bénéficiez d'avoir un écosystème fort
3. Ainsi, même si vous ne bénéficiez pas directement de l'existence et du succès du Collective, vous en bénéficierez indirectement sur un horizon plus long, et vous pourriez envisager de faire un don malgré tout.

Quelques-uns ont reconnu les mérites du projet, et nous ne pouvons pas les remercier assez (ils sont listés sur [la page d'accueil](https://deficollective.org)). Mais pour la plupart, les conversations se sont essentiellement déroulées ainsi :

- Moi : « Bonjour, TokenBrice ici, /insert_pitch/ »
- Eux : « Belle idée ! Donc notre protocole, où se situerait-il dans le framework ? »
- Moi, étant honnête : « Eh bien, cela dépend ; il pourrait être à l'étape 1 ou 2, mais même si c'est le cas, nous n'allouerons probablement pas de fonds à cela au moins au début, car nous devons démontrer l'impact positif que le Collective peut avoir avec des projets plus petits d'abord. »
- Eux : « Donc il n'y a rien pour nous ? »
- Moi : « Pas directement, mais vous bénéficierez d'avoir l'écosystème DeFi florissant : cela signifie des protocoles et des tokens plus résilients pour votre protocole à intégrer. »
- Eux : « Pas intéressé. »

Vous pourriez penser que c'est juste nous, mais ce n'est pas le cas ! Regardons la situation avec les autres projets de la couche curation mentionnés précédemment. Nous avons deux exceptions, DeFillama et L2beat, qui, bien qu'ils aient eu des difficultés initialement, sont maintenant bien financés et reçoivent souvent des dons. À part cela, c'est à peu près un cauchemar :

- Bluechip a initialement exploré une structure à but non lucratif financée par des dons mais n'a pas pu obtenir un financement suffisant, donc il a dû évoluer vers une entreprise à but lucratif.
- DeFiSafety est porté par un seul chad, Rex, et a dû introduire des [paiements](https://www.defisafety.com/pricing). Malgré la livraison de critiques de haute qualité et actionnables, exploitées par beaucoup pendant des années, il reste à peine à flot.

### Les nouveaux projets de la couche curation peinent à émerger

Comme vous pouvez le voir ci-dessus, le problème central n'est pas tant le financement des projets de la couche curation déjà établis et bien connus, mais **l'émergence des projets plus petits et plus récents qui ne parviennent pas à trouver le financement dont ils ont besoin pour croître en premier lieu**.

Une fois qu'un projet atteint une taille et une notoriété comme L2Beat / DeFillama, le soutenir peut être vu comme un « coût marketing » pour les projets adjacents. Par exemple, plusieurs L2 ont alloué une part de leur supply de tokens à L2Beat : cela avait un sens économique pour eux, car cela augmentait la notoriété de leur L2. Cela a permis de soutenir un bien public en même temps – un plan gagant-gagnant ! Grâce à leur notoriété et leur portée, ces deux projets de la couche curation sent sortent également bien sur les plateformes de dons comme Gitcoin.

### Le coût de l'information gratuite

Le fait est que ces **services de la couche curation ont des coûts sérieux**, des coûts qu'ils ne peuvent pas récupérer auprès de leurs lecteurs s'ils veulent garder l'information qu'ils produisent accessible au maximum – c'est-à-dire gratuite et ouverte à tous.

Je peux vous donner des perspectives sur DeFiScan. En ne tenant pas compte :

- Des mois que nous avons passés à rechercher et itérer sur le cadre.
- Tous les membres de DeFiCollective qui sont sérieusement sous-payés (1500-2500 $/mois pour un mi-temps) pour leur expertise et leur engagement (a.k.a. des Chads vraiment alignés sur les valeurs, je ne peux pas les remercier assez), qui soutiennent également DeFiScan.
- De nombreux contributeurs, moi y compris, travaillent plus près d'un temps plein pour DeFiCollective/DeFiScan (pour un salaire de mi-temps).
- DeFiCollective couvre tous les coûts d'infrastructure et de service encourus par DeFiScan.

Nous **estimons** le coût effectif d'une revue dans la fourchette de 3000 $ (petit protocole immuable) à 10 000 $ (grande base de code, protocole mutable), et potentiellement encore plus (bonjour Aave et votre base de code infinie). Notez que chaque revue n'est pas seulement écrite par celui à son initiative (qui peut être l'un de nous ou quelqu'un lié au protocole revu) mais aussi soigneusement discutée et analysée par d'autres membres de l'équipe. Avec 14 revues déjà publiées, c'est essentiellement **un coût de 91k$ en cinq mois d'existence**. Si nous comptabilisons les revues en cours (total incluant celles publiées = 35), **ce coût saute à 227 500 $, soit ~45 500 $ par mois**.

Veuillez noter que ce qui précède est une estimation, car personne ne paie pour DeFiScan – ni vous, les lecteurs/utilisateurs, ni les projets revus. Pour avoir une autre perspective, regardons Bluechip puisque Ben a accepté de partager leur tarification – ce que les projets paient pour être revus : 15k $ pour une évaluation holistique et des frais de maintenance annuels de 5k $, commençant après un an.

Je n'écris pas cela pour mendier votre argent – nous nous débrouillons seuls, grâce à la situation unique du DeFiCollective, et explorons toutes les autres options pertinentes. C'est un rappel que l'information (curation, dans notre cas) a un coût.

## Que pouvez-vous, cher lecteur, faire à ce sujet ?

Encore une fois, je tiens à souligner que le but de cet article, le message qu'il porte, n'est pas « faites un don à vos services de curation ». Cependant, vous êtes les bienvenus, et à notre niveau, vous l'avez déjà fait. Lorsque nous avons offert à notre communauté l'opportunité de faire un don pour le premier anniversaire du DeFi Collective, vous [avez sauté sur l'occasion](https://deficollective.org/blog/first-anniversary-nft/). Vous avez contribué au maximum possible (10 ETH) en moins de trois jours.

Au lieu de cela, le message que j'aimerais diffuser concerne davantage **1) l'importance critique de la couche curation, 2) la réalisation des coûts de l'information précieuse qu'ils fournissent, et 3) le besoin pour vous, moi, et essentiellement tout le monde d'être beaucoup plus proactif dans la préconisation de son financement**. Il est assez clair que les grandes DAOs et autres institutions bien financées ne sont pas trop enthousiastes à l'idée de financer cela, donc c'est à nous de les aider à voir la lumière.

Encore une fois, grâce à la situation unique au DeFi Collective, nous ne nous inquiétons pas pour notre survie à court/moyen terme ; cependant, je pense que c'est une nécessité pour la survie à long terme de la DeFi de voir DeFiSafety, Bluechip, et d'autres projets encore émerger et prospérer. Nous discutons bien sûr tous les trois déjà et envisageons une « Alliance des fournisseurs de services d'information DeFi » (nom temporaire), dans laquelle nous aimerions voir des projets plus importants comme DeFiLlama et L2Beat également.

Si vous avez lu mon plaidoyer et entendu mon appel, la prochaine étape est simple : **allez dans les DAOs sur lesquelles vous êtes actif et demandez-leur ce qu'ils font pour soutenir l'espace au-delà de leurs avantages immédiats**. La situation actuelle, avec sa couche curation sérieusement sous-dimensionnée, a des conséquences graves qui devraient être évidentes pour tous : **les débutants se font massacrer**, rugger, escroquer, etc. En conséquence, toute notre industrie ressemble à un cirque de l'extérieur. **La DeFi ne peut devenir mainstream que si l'utilisateur moyen est raisonnablement en sécurité** ; ce n'est actuellement pas le cas. En outre, les outils de curation sont également une demande importante de la part des clients institutionnels qui recherchent activement de telles ressources : **une couche de curation améliorée signifie donc que nous serons en mesure d'attirer et de retenir à la fois les particuliers et les institutions**.

Alors allez pousser les baleines publiques et bien connues et autres institutions bien financées à faire plus. Les protocoles de la taille d'Aave, Maker, Uniswap, Eigen, et plus ont la responsabilité de soutenir l'écosystème plus large. Puisqu'ils le font à peine/pas actuellement, c'est notre travail de leur rappeler et de plaider dans cette direction, car c'est la beauté de DeFi : s'ils échouent à le faire parce qu'ils ne voient pas d'avantages immédiats pour eux, je suis convaincu qu'ils souffriront à long terme et feront face à des coûts réels à cause de cela.

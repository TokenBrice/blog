---
title: "Vive la lutte libre (et vérifiable onchain)"
description: "Un article-thèse où je vous explique pourquoi les Luchadores me fascinent et ce que j'en attends"
date: '2021-10-04T01:13:50.191Z'
categories: [NFT]
tags: [Collectibles, NFT, Achat de NFT, Farming NFT, Chainlink VRF]
toc: true
tocNum: false
url: luchadores-nft
image: /img/2021/luchadores-nft/luchadores-cover.png
difficulty: "beginner"
---

Cet article va être plus personnel qu'à mon habitude, mais vu le sujet je ne peux pas faire autrement. On va s'intéresser à un projet NFT dans lequel je suis fortement impliqué : les Luchadores. Ce sont des lutteurs entièrement onchain, bientôt personnages dans un jeu à venir,  lui aussi onchain.

Plus que le projet lui-même, je vous expliquerai la thèse que je développe à son sujet. Je pense que cette démarche peut vous intéresser et vous aider à développer des convictions personnelles sur d'autres collections.

Dans cet article, je ne détaille pas les mécanismes des Luchadores ou du jeu associé à venir. N'hésitez pas à lire [le whitepaper désormais disponible en français](https://whitepaper.luchadores.io/v/francais/) pour plus d'infos à ce sujet.

---

## 📑 Ma thèse sur les Luchadores

Si vous n'êtes pas encore des plus informés sur les NFTs et mes activités dans le domaine, n'hésitez pas à aller lire la [page d'introduction](https://tokenbrice.xyz/fr/nft/).

Mon intérêt pour les Luchadores et la raison de mon enthousiasme pour cette collection tient à quatre raisons principales, allons donc droit au but :


### 🔮 Un processus de génération innovant et inclusif

La génération des Luchadores était un processus entièrement onchain grâce à l'utilisation de la VRF de Chainlink. Elle permet de **générer des nombres aléatoires de manière vérifiable**. Grâce à cet apport, le minting d'un Luchadores se faisait avec la garantie qu'il n'y avait pas de manipulations possibles, et la preuve du calcul reste disponible.

C'est cette dimension technique innovante qui m'a aidé à repérer le projet initialement. Limité à **10 000 Luchadores au total**, le mint est resté disponible environ **3 mois** (Mai->Août 2021), avec une certaine excitation dans les derniers jours.

La longue période de minting a permis à tous ceux qui le souhaitaient de pouvoir s'impliquer, avec tout le temps nécessaire pour atteindre des coûts de transaction plus opportuns si désirés.

La génération se faisait au prix de 2 LINK (frais nécessaire pour le mécanisme VRF), payé en ETH + les coûts en gas. En fonction du prix du LINK et des coûts de transaction sur le réseau, les minteurs ont payé entre 0.015 et 0.025 ETH par Luchadores.

La génération aléatoire vérifiable à donné lieu à quelques faits de "trivia" sur les Luchadores assez amusants :

![luchadores-distribution](/img/2021/luchadores-nft/luchadores-distribution.png "Table d'occurence par attributs des Luchadores")

La distribution de la rareté est une courbe normale : on compte plus de 8000 Luchadores (81,3%) dans le groupe des 3, 2 ou 4 attributs, les plus communs. Plus on s'approche des extrêmes, plus les Luchadores se font rares.

 |Commun (3*, 2*, 4*)|Rare (1*, 5*)|Epique (6*, 0*)|Légendaire (7*)
:--|:--|:--|:--|:--
**Nombre Générés**|8130|1654|205|11
**Pourcentage**|81.30%|16.54%|2.05%|0.11%

* Il y aurait pu avoir un Luchador avec 8 attributs, mais ça n'est pas arrivé. Il n'y en aurait très probablement eu qu'un seul : pas de dieu Lucha donc.
* Parfois, l'attribut "moustache" tombe sur un Luchador dont la couleur de peau est très proche de celle utilisée pour la moustache, créant ainsi une **[moustache cachée](https://luchadores.io/luchador/8085)**. Ces Luchadores font l'objet d'une attention particulière.

![luchadores-hidden_mustache_difference](/img/2021/luchadores-nft/hidden_mustache_difference.png "Une différence subtile mais signifiante")

### ⛓ L'approche onchain

Outre la génération faite entièrement onchain, le visuel du Luchadores est dans un format optimisé (svg) qui permet le **stockage directement sur la chaîne Ethereum**, apportant ainsi une résilience conséquente au média associé à chaque NFT.

Ça ne s'arrête pas là puisque le jeu à venir, dont on discute juste après, s'appuiera également sur des **mécanismes de génération aléatoire vérifiable**. Ainsi dans l'arène, les coups critiques ou les esquives seront le fruit d'un hasard vérifiable et très dur à manipuler.

![luchadores-art-for-all](/img/2021/luchadores-nft/AFA-score.png "ArtForAll permet d'analyser la résilience des NFTS")

Je ne suis pas le seul à remarquer cette approche très résiliente, qui a également plu aux Link marines. Les Luchadores sont également le seul projet à 100/100 avec les Avastars sur [ArtForAll, un service qui évalue la résilience de NFTs](https://artforall.io/score?search=).

Ainsi, on pourrait décrire le projet comme "on chain maximaliste" mais ça n'est pas le cas : des compromis, hélas nécessaires, sont envisagés au niveau où il est possible de se le permettre : les tirages aléatoires liés au jeu, seront réalisés sur une sidechain (Polygon) ou un rollup. Cela permettra de **garder le jeu accessible et peu coûteux**, tout en profitant de garanties maximales au niveau du NFT, lui toujours bien au chaud sur la chaîne Ethereum.


### 🎮 Le jeu Luchadores

Le jeu en lui-même résonne sans doute avec ma fibre nostalgique. En effet, la lutte se fera au **tour par tour**, avec un système d'attributs (stats), compétences passives et compétences à déclenchement.

![luchadores-stats](/img/2021/luchadores-nft/luchadores-stats.png "Les attributs seront déterminants dans l'arène")

Je vous laisse vous documenter sur l'impact des attributs et des compétences, mais en temps que fan de jeux tour par tour, de stratégies et RPG, je peux vous dire que je suis paré pour le theorycraft 🧙

![luchadores-arena](/img/2021/luchadores-nft/final-lucha-arena.png "Les batailles en équipe sont également envisagées")

**Un token associé** (LUCHA) sera gagnable en jeu. Il sera également distribué la première année aux possesseurs de NFT Luchadores. Le token aura plusieurs formes d'utilisations liées au jeu (respect, système de prodiges, rename ?) et peut également être **staké pour gagner des MASK**, un token non-transférable (↪ seulement in-game) utiles pour équiper ses Luchadores.


### 📜 La communauté et son histoire

Le jeu est développé par une seule personne, Luchador, qui a progressivement été rejoint par plusieurs profils nécessaires pour le développement:

* Dès le début, des membres de la communauté ont émergé comme Teh_Griz et LuchaBroy : ils sont devenus les premiers modérateurs du Discord.
* Je me suis progressivement impliqué, pour aider à faire connaître le projet, développer la communauté francophone et apporter mon aide là où c'est pertinent, plus d'info plus loin.
* Un game designer et deux pixel artists ([AbueloRetroWave](https://www.instagram.com/AbueloRetroWave/) & [m3r0j](https://www.artstation.com/m3r0j))

On ne parle ici que des implications "formelles". Il ne faut bien sûr pas oublier toutes les initiatives communautaires. Il est impossible de toutes les lister ici, mais je citerai quand même :

* Nicosz qui a créé un [outil en Python pour analyser les données liées aux Luchadores](https://github.com/sznicolas/luchadata).
* Un [dashboard pour suivre les principales métriques sur les Luchadores](https://dune.xyz/lokhidor/Luchadores), proposé par cnhkp.eth, grâce à Dune Analytics et l'aide de Nicosz.
* Ou encore OxMule qui a [traduit le whitepaper](https://whitepaper.luchadores.io/v/francais/) en quelques jours.
* Sans oublier les nombreux collectionneurs et "snipeurs" du Discord qui l'animent tous les jours, comme Chainlinkers, un des premiers membres de la communauté qui a gagné deux giveaways à la suite le jour de son anniversaire et est entré dans la légende.

---

## 🐒 Mon implication

J'ai découvert les Luchadores en Mai, j'en ai minté environ 80 et j'ai suivi le projet assez passivement au début. En juin, lorsque l'engouement a commencé à être plus palpable, je me suis impliqué plus activement, au début comme modérateur pour la communauté francophone puis administrateur du serveur Discord.

Je vois mon implication dans le projet comme une opportunité pour éduquer sur les dimensions techniques des NFTs. Je n'ai pas choisi ce projet au hasard : j'estime que l'approche SVG onchain utilisée par les Luchadores est parmi les plus crédibles, malgré le compromis graphique (-> style pixel).

Concrètement, j'anime la communauté avec différents giveaways et j'aide à faire connaître les Luchadores.


### 🃏 Mes Luchadores

J'ai été assez peu chanceux au minting de mes Luchadores, et j'ai donc compensé ma chance par mes acquisitions. Bien que la plupart correspondent à un nettoyage mécanique du prix plancher, surtout entre 0.025 et 0.035 ETH, j'ai aussi acquis quelques Luchadores plus rares dont trois 7 attributs.

Ma plus belle prise est le "Batman", un 7 attributs qui sera l'un de mes principaux combattants dans l'arène :

#### ⭐ Lucha 7 attributs #8956

![luchadores-8956](/img/2021/luchadores-nft/luchadores-8956.png "Un Luchador 7 attributs, à gagner dans l'arène")

Désormais en possession de 3 Luchadores 7 attributs, **je souhaite en remettre un en jeu**. Celui-ci ne partira pas au plus offrant, non.

**Le [Luchador #8956](https://luchadores.io/luchador/8956) se gagnera dans l'arène**, et ira donc au joueur le plus habile. Hâte de vous partager plus de détails sur le mécanisme d'allocation, lorsque le jeu sera disponible.


#### 🎁 Les dons

J' ai donc minté environ 80 Luchadores, et acheté plus de 150 sur OpenSea.

J'entends en utiliser une bonne partie comme "budget promotionnel" pour les Luchadores - et c'est déjà le cas. Plusieurs distributions ont eu lieu et une bonne cinquantaine a déjà été donnée, dont 25 aux top farmeurs de blé DeFi France.

Pour le reste, comme je suis fan du concept de skin-in-the-game (implication directe avec conséquences), et vu mon implication dans le projet je ne le voyais pas autrement. Je n'ai pas de Luchadores en ma possession sur d'autres wallets, je centralise tout sur [mon ENS par transparence.](https://opensea.io/tokenbrice?search[sortBy]=LISTING_DATE&search[query]=luchadores)

---

## 📈 La valeur d'un lutteur

{{< notice warning >}}

⚠ Cet article ne constitue pas un conseil en investissement. Choisir quand et quel jpeg/svg acquérir est un choix personnel.

{{< /notice >}}

Les Luchadores se sont d'abord échangé à proximité du coût de revient du minting, avant d'établir un premier plancher autour de 0.03 ETH. Depuis la fin du mois de septembre, avec l'arrivée du whitepaper, l'engouement est palpable et se reflète sur le floor (prix plancher) désormais aux alentours de 0.07 ETH.

Alors un lutteur oui, mais à quel prix ? Ne vous attendez pas à une réponse directe de ma part là-dessus. À ce jour et à ce stade de développement, cela reste encore un pari. Néanmoins l'approche est pertinente et je pense que les Luchadores ont de quoi entrer dans le canon des NFTs, en repoussant toujours plus la frontière de l'interactivité rendue possible avec ces objets numériques.

Acquérir un Luchadores aujourd'hui implique de payer environ trois fois minimum le prix observé il y a quelques semaines - et pourtant ce serait une bonne affaire si la tendance actuelle continue 🔮 : bienvenue dans le monde des NFTs, où le pricing est un mécanisme social et hautement réflexif.

Là-dessus, c'est faites vos jeux, rien ne va plus 🎲.

---

{{< notice note >}}

_Je n'en parle que maintenant sur le blog car je voulais prendre le temps d'articuler ma pensée. Ceux qui me suivent en live ou sur Twitter ont entendu parler du projet dès Mai et ont pu en minter directement, s'ils le désiraient._

{{< /notice >}}

J'espère que cet article vous a permis de comprendre ce qui peut bien me fasciner dans une collection de lutteurs, et plus généralement comment j'analyse une collection et qu'il vous aidera également à évaluer d'autres.

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._
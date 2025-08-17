---
title: "NFTfi : repousser les limites de NFTs grâce à la DeFi"
description: "La DeFi apporte aux projets NFTs des outils pour résoudre leurs principales limites (comme la liquidité) tandis que les NFTs permettent de rendre la DeFi plus fun et digeste : un mariage parfait ?"
date: '2022-03-29T01:13:50.191Z'
categories: [NFT]
tags: [DeFi, Ethereum, Decentralized Finance, NFT, Forgotten Wizard, Luchadores, NFTfi]
toc: true
tocNum: false
url: nftfi-defi-nft
image: /img/2022/nft-defi-infrastructure/nft-defi-infrastructure-tokenbrice.png
difficulty: "beginner"
---

La finance décentralisée a ouvert un monde de possibles : une myriade d’intermédiaires auparavant nécessaires sont désormais surnuméraires. Malgré tout, elle intimide par sa potentielle complexité et sa transdisciplinarité. Outre la dimension technique évidente, la DeFi invoque également des notions issues de disciplines diverses: économie, sciences sociales, “mémétique”, etc.

Ainsi, depuis des années déjà, les NFTs ont servi de porte d’entrée vers le monde décentralisé, démontrant les bénéfices de la tokénisation et de la désintermédiation à une population encore peu friande de DeFi. 

Je vous propose donc aujourd’hui de faire converger les deux thèmes principaux de ce blog en un sujet captivant : l’émergence de l’infrastructure DeFi pour les NFTs, ou encore l’arrivée des NFTs/gamification dans la DeFi - c’est une question de perspective.

## DeFi + NFT => NFTfi : un monde de possibles pour vos JPEGs

Les cas d'utilisation à la croisée de la DeFi et des NFTs sont nombreux et en plein développement. Plutôt qu'une liste exhaustive, je vous propose d'analyser quelques projets emblématiques pour comprendre comment ils assemblent des éléments des deux univers pour offrir un service pertinent.

Cette infographie est un bon point de départ pour approfondir votre analyse de la NFTfi si cet article éveille votre curiosité :

![nftfi-landscape](/img/2022/nft-defi-infrastructure/nftfi-landscape.jpeg "Carte des projets NFTfi (source UnUniFi Protocol)")

On commence par le plus intuitif pour ceux qui sont déjà un peu à jour avec la DeFi : l’arrivée d'une infrastructure financière pour échanger, mais aussi prêter, rendre productif ou encore fractionnaliser des NFTs. Pour attaquer ce vaste sujet, partons de la première couche : l’infrastructure utilisée pour acheter et vendre des NFTs.

### Les services d’achat et vente de NFTs

Jusqu’à peu, les NFTs vivaient une drôle de situation d’entre deux. Par essence, les NFTs permettent la désintermédiation et une interaction plus directe entre les cŕéateurs et leur audience. Cette désintermédiation s’accompagne d’une réduction massive des frais engagés pour mettre une œuvre sur le marché et de nouvelles possibilités, comme leur interactivité.

Seulement voilà, les NFTs restent échangés principalement sur un service qui n’est pas  à leur hauteur, j’ai nommé OpenSea - qui reste encore dominant bien que la situation évolue rapidement depuis l’arrivée de LooksRare.

Sans trop s’étendre, OpenSea connaît de nombreuses limites :



* Un frais proche de l’usure pour chaque échange - 2.5% - et qui est réservé exclusivement à l’équipe.
* Un manque de respect des plus basiques pour la communauté NFT : violation de leur vie privée, manipulation, etc.
* Un certain mépris pour les projets NFTs les plus communautaires : les mécanismes de vérification sur OpenSea sont assez peu transparents et ne dépendent pas réellement du volume. Des projets pitoyables, mais portés par des célébrités, se sont ainsi vu vérifiés rapidement tandis que les Luchadores, par exemple, attendent encore.
* Un manque d’investissement dans son propre développement : la plateforme est lente à évoluer et n’écoute pas ses utilisateurs.
* Une approche 100% business : [OpenSea a réalisé 9 levées de fonds](https://www.crunchbase.com/organization/opensea/company_financials) jusqu’à présent, et ce, malgré les profits gargantuesques qu’ils génèrent via le frais excessif prélevé : $100M de volume **sur 1 jour** ⇒ $2.5M dans les poches de la team (- frais opérationnels, mais quand même…)

On obtient ainsi une situation proche des fournisseurs d’accès internet américains : OpenSea est utilisé par tous dans le monde des NFTs, mais également **viscéralement détesté par une part non négligeable de ses utilisateurs**.

Commençons donc par regarder les données qui sont éloquentes :

![looksrare-vs-opensea](/img/2022/nft-defi-infrastructure/looksrare-vs-opensea.png "Volume observé sur LooksRare et OpenSea")


On regarde ici simplement le volume. En termes de nombre d’utilisateurs et de transactions OpenSea domine encore largement. Vous pouvez retrouver toute la donnée sur le super dashboard [d’Hildoby](https://twitter.com/hildobby_) : [LooksRare VS Opensea (Dune Analytics)](https://dune.xyz/hildobby/LooksRare-VS-OpenSea).

On était nombreux à attendre une alternative crédible, et heureusement elle est arrivée : LooksRare. Le cas vaut la peine d’être creusé, mais en résumé LooksRare c’est l’exact inverse d’OpenSea :



* Les frais de transaction sont réduits à 2% et **redistribués entièrement** aux stakers du token LOOKS.
* L’équipe LooksRare se montre très à l’écoute de la communauté et en deux mois d’existence, ils ont déjà implémenté de très nombreuses fonctionnalités demandées par leurs utilisateurs.
* Le token LOOKS a été airdrop aux utilisateurs d’OpenSea. Il s’obtient désormais en achetant ou vendant des NFT sur Looksrare : **une distribution directe** aux utilisateurs du service.
* Une stratégie de POL (Protocol Owned Liquidity) est mise en place par le protocole : une part non négligeable de la liquidité sur LOOKS est possédée directement par celui-ci.

Le protocole possède ainsi déjà près de $13M en ETH+LOOK déployé sur UniswapV3 pour soutenir la liquidité - voici [le wallet de LooksRare](https://debank.com/profile/0xc8c57e4c73c71f72ca0a7e043e5d2d144f98ef13) pour vérifier par vous même. Les frais collectés sur le LP sont utilisés pour… apporter toujours plus de liquidité !

![looksrare-pol](/img/2022/nft-defi-infrastructure/looksrare-pol.png)


Ce nouveau jeu de règles permet à LooksRare d’être extrêmement compétitif par rapport à Opensea, puisque le frais est 20% plus bas, et que chaque achat/vente est également rémunéré en LOOKS. Le résultat est sans appel : acheteur comme vendeur gagnent tous deux à préférer LooksRare à Opensea.

![looksrare-vs-opensea-cost](/img/2022/nft-defi-infrastructure/looksrare-vs-opensea-cost.jpeg "Comparaison des coûts LooksRare vs Opensea")

### La tokénisation expliquée avec la partialisation de NFTs

Échanger des NFTs, c’est top : encore faut-il comprendre ce qu’il y a dans la boîte ! On va donc détailler les enjeux de la tokénisation avec plusieurs exemples. En effet, les possibilités offertes par cette dernière sont immenses, alors illustrons les !

Prenons donc le temps de bien expliquer le concept. Tokéniser, c’est l’action de créer un token (token qui **représente** quelque chose). À première vue comme ça, l’intérêt peut être dur à concevoir. Néanmoins, tokéniser permet également une forme “d’alchimie” : une transmutation - un changement du type de token du fongible à non-fongible, et vice-versa.

Prenons un exemple qui illustre bien les bénéfices de la tokénisation - le cas de **la fractionalisation d’un NFT**.

1. On part donc d’un token non fongible spécifique, le CryptoPunk #666 par exemple.
2. On le verrouille dans un contrat qui émet 10 000 PUNK tokens, des tokens ERC-20. 
3. On a maintenant un token qui représente 1/10 000 du CryptoPunk #666 original. Ce token est un ERC-20 classique et donc échangeable facilement via Uniswap ou autre (⚠️ Liquidité)

⇒ La tokénisation permet ici **la possession collective d’un bien unique** (le NFT CryptoPunk #666).

Ce concept, tout en illustrant les bénéfices de la tokénisation correspond également à un cas d’usage réel. La réalité est bien sûr plus complexe, puisque nous avons décrit ici seulement le mécanisme de collectivisation (1 NFT ⇒ 10 000 ERC20). Le chemin inverse est aussi possible pour récupérer l’accès au NFT verrouillé : 10 000 PUNK ⇒ NFT CryptoPunk #666 : c’est la privatisation.

Ce modèle, c’est celui de [Spectre.xyz](https://spectre.xyz/litepaper), un service qui permet de gérer la collectivisation et privatisation de NFTs.

![spectre](/img/2022/nft-defi-infrastructure/spectre.png)


Outre la possession collective, une telle solution a aussi un intérêt en terme de liquidité : le token obtenu (PUNK) est un ERC20 classique, il est donc bien plus aisé de développer des solutions permettant son achat et sa vente immédiate qu’avec un NFT, qui nécessite la rencontre d’une demande et d’une offre simultanée.


### Tokénisation pour développer la liquidité : les vaults

Une fois la tokénisation bien comprise, le prochain chapitre - les vaults NFT - est presque une évidence. Un des enjeux sur les NFTs, c’est la liquidité des marchés. La non fongibilité c’est chouette pour faire des collections de 10 000 pièces toutes uniques bien que similaires - mais _quid_ de la valorisation et de l’échange de celles-ci?

Outre LooksRare et Opensea précédemment mentionné, il existe d’autres places de marché pour les NFTs qui s’appuient sur une logique différente : c’est **le modèle des vaults NFT** - qui a de nombreux intérêts, mais aussi des limites - la principale étant que cette approche n’est possible qu’avec des grosses collections (plusieurs centaines d’unités) et/ou assez populaires (forte demande).



1. [MINT] Un “vault” (smart contract) spécifique à une collection est créé ; les utilisateurs peuvent déposer leur NFTs dans celui-ci. 
2. Lorsqu’un utilisateur dépose un NFT dans le vault, sa contribution est reconnue par l’émission d’un token ERC20.
3. [REDEEM] À tout moment, le token ERC20 peut être échangé contre n’importe quel NFT du vault. Le token ERC20 est alors détruit.

{{< notice warning >}}
⚠️ Vous l’aurez compris, le vault assume que tous les NFTs sont équivalents : mieux vaut donc rentrer dans un vault avec un NFT parmi les moins rares de la collection donnée. 
{{< /notice >}}

Le leader en la matière, c’est probablement [NFTX](https://nftx.io/vault/0x87931e7ad81914e7898d07c68f145fc0a553d8fb/info/), mais il y a aussi [NFT20](https://nft20.io/). Cette méthode permet d’obtenir un token ERC20 - par exemple le WIZARD - qui correspond à un claim sur n’importe quel NFT du vault, en l'occurrence n’importe lequel des 215 Forgotten Wizard Cult (NFTs) contenu dans [le vault.](https://nftx.io/vault/0x87931e7ad81914e7898d07c68f145fc0a553d8fb/info/)

![nftx-wizard-list](/img/2022/nft-defi-infrastructure/nftx-wizard-list.png "Le vault des Forgotten Wizard Cult ur NFTX")


La liquidité sur le token WIZARD peut être développée contre ETH par exemple, permettant ainsi l’achat immédiat de n’importe quel wizard contenu dans le vault. L’inverse est également possible : tout possesseur d’un Forgotten Wizard Cult peut le déposer dans le vault afin d’obtenir 1 WIZARD qu’il pourra ensuite vendre pour de l’ETH.

Et enfin NFTX va même plus loin puisque le token natif de la plateforme ainsi que les frais collectés sont utilisés pour proposer des incitations à deṕoser dans le vault et développer la liquidité. **Les utilisateurs qui** **déposent des NFTs dans le vault sont ainsi éligibles à une rémunération de staking** - et des rendements plus élevés sont possible pour ceux qui déposent + LP : la financiarisation des NFTs est lancée !

![alt_text](/img/2022/nft-defi-infrastructure/nftx-wizard.png "Rendements staking (rouge) et LP (violet) sur le token WIZARD")


On se concentre ici sur la liquidité, mais il faut garder en tête que le passage d’un NFT à un ERC-20 vient avec de nombreux autres avantages :



1. Si la liquidité sur la paire est suffisante - alors elle devient également **une source de prix**.
2. Qui dit source de prix (oracle) + liquidité dit… collatéral évidemment ! Avec ces deux éléments, rien n’empêche d’envisager le WIZARD comme **collatéral pour emprunter** d’autres tokens comme des stablecoins. C’est faisable mais bien plus complexe en partant directement du NFT.
3. Enfin, gardez en tête qu’il n’y a pas de limite à la tokénisation, tant qu’il y a un intérêt. On est resté ici sur des cas de tokénisation unique, mais des **scénarios de tokénisations enchevêtrées** sont également envisageables.

Un token ERC-20 qui représente un claim sur un Wizard donné, c’est top. Maintenant imaginez que vous ayez la même chose pour les CryptoPunks, le BAYC et ainsi de suite - c’est le cas sur NFTX. Rien n’empêche d’envisager une étape de tokénisation supplémentaire pour créer un **index NFT** représenté par un token ERC20 mais qui serait lui meme** échangeable contre les tokens représentants les actifs sous-jacents:** :

On pourrait ainsi imaginer le NFT-Bluechip-Index, un token ERC-20 créé en verrouillant 1 WIZARD + 1 PUNK + 1 BAYC. Ce token serait facilement liquide, et permettrait ainsi de s’exposer facilement aux trois collections en une seule transaction. En outre, le token resterait entièrement collatéralisé à tout moment par 1 NFT de chaque collection. Un possesseur du NFT-Bluechip-Index pourrait tout à fait faire la marche inverse à tout moment, c’est à dire :



1. [Avec le contrat NFT-Bluechip] : burn de 1 NFT-Bluechip-Index pour récupérer 1 WIZARD + 1 PUNK + 1 BAYC
2. [En utilisant les contrats/vaults de NFTX] burn de 1 WIZARD + 1 PUNK + 1 BAYC pour récupérer un NFT (au choix parmi ceux qui sont dans le vault) de chaque collection sous-jacente. 


### Idol : des NTFs pour tokéniser un rendement DeFi

Pour continuer et finir sur la tokénisation, sachez  qu’elle permet également de faire le lien entre les deux mondes - les NFTs et la DeFi : l’exemple parfait ici c’est le projet [IdolsNFT](https://www.theidols.io/).

Les IdolsNFT ont été vendus initialement via une bonding curve pour un prix entre 0.25 et 0.5 ETH. Tous les ETH collectés durant la vente sont stakés via Lido (StETH). Posséder un Idol vous rend éligible à la part correspondante des rendements. Ici, c’est donc le rendement généré par les StETH qui est tokenisé.

![idols-nft](/img/2022/nft-defi-infrastructure/idol-nfts.png)


Et le projet va même plus loin ! En effet, il y a aussi un ERC-20 dans l’histoire, le VIRTUE, initialement distribué aux premiers acheteurs. Désormais pour obtenir du VIRTUE, il faut bond des stETH (-> ce qui augmente le capital productif du projet). 

Le VIRTUE correspond à une exposition par proxy sur les IdolsNFT : pour chaque vente d’un NFT Idol, un frais de 7.5% est prélevé et reversé aux stakers de VIRTUE.

![idolnfts-virtue-cycle](/img/2022/nft-defi-infrastructure/idol-cycle.png)

Ainsi, les Idols, “Gardiens d’Ethereum” utilisent les NFTs pour rendre le staking d’ETH plus fun et interactif. En outre, la capture des frais sur le token VIRTUE permet d’éviter une “capture externe” des frais générés par les échanges de IdolsNFT comme c’est le cas pour les NFTs échangés sur NFTX par exemple. 

Enfin, les gros possesseurs de la collection ont un chemin tout tracé pour composer leur rendement si leur conviction est forte :



1. Possession de plusieurs IdolsNFT ⇒ Yield en stETH
2. Composition des stETH farmés via bonding ⇒ VIRTUE
3. Stake des VIRTUE ⇒ Yield en ETH
4. Staking ETH avec Lido ⇒ StETH ⇒ Bonding pour des VIRTUE puis stake

Quoi qu'il arrive avec cette collection, je pense qu’elle a posé les bases de ce que peuvent être les collections NFTs augmentées par et synergétique avec la DeFi. Je m’attends à voir de nombreuses autres variations pertinentes sur ce modèle.


### Agrégation de diverses sources de liquidité

Dans cet article, on a déjà mentionné trois plateformes différentes pour acheter ou vendre des NFTs : OpenSea, LooksRare et NFTX. La réalité est encore plus dense, il existe une armada de places de marché pour les NFTs, plus ou moins réussies et plus ou moins spécialisées, en voici quelques autres : [Rarible](https://rarible.com/), [Superrare](https://superrare.com/), [Foundation](https://foundation.app/), [NFT20](https://nft20.io/), etc.

Face à cette myriade d’options, les acheteurs n’ont pas forcément le temps, l’envie, l’énergie ou bien encore la connaissance pour explorer toutes leurs options avant de conclure une transaction. La situation est très similaire à l’achat/vente d’un token ERC20 en DeFi : la liquidité est très fragmentée. Logiquement, la solution est donc similaire à celle déployée en DeFi : l'agrégation.

![gem.xyz](/img/2022/nft-defi-infrastructure/gem-xyz.png "Gem, l'aggrégateur NFT")


Il existe ainsi plusieurs services capables de diriger les “ordres” vers différentes places de marché, voire de ŕealiser un “swipe” sur plusieurs plateformes avec une seule transaction : il s’agit de [Genie](https://genie.xyz) et [Gem](https://gem.xyz). 

Là encore, c'est la réactivité de l’équipe et la composabilité du service qui feront la différence sur le long terme : Gem semble avoir pris de l’avance grâce à son intégration avancée de LooksRare (claim LOOKS possible pour les acheteurs via Gem).

---

## NFT + DeFi => Des jeux avec de vrais enjeux

Si la DeFi a découvert le marché énorme qu’est les NFTs récemment, la marche inverse s’observe aussi : **l’arrivée de composantes DeFi dans des projets NFTs** - on parle souvent de GameFi pour décrire cette tendance.

Cela fait plusieurs années déjà que les premières itérations de GameFi sont apparues, avec des jeux qui peuvent devenir une source de revenu crédible pour leurs joueurs : le plus célèbre est bien sûr [Axie Infinity](https://axieinfinity.com/), mais il en existe quantité d’autres : [AaveGotchi](https://www.aavegotchi.com/), [CryptoRaiders](https://cryptoraiders.xyz/), etc.

Hélas je ne suis moi-même pas très actif sur ces projets, je vous propose donc de détailler un qui m’est plus familier : les Luchadores. Ici encore, on retrouve des composantes DeFi qui se greffent sur le projet NFT :

* Posséder un Luchador (NFT) donne le droit à un rendement en LUCHA (token ERC20).
* Le protocole possède environ [60% de la liquidité sur les deux paires LUCHA](https://debank.com/profile/0x0cb11b92fa5c30eafe4ae84b7bb4df3034c38b9d), grâce aux fonds levés pendant la vente des premières pinatas.

{{< notice note >}}
Les 🪅 sont des tokens ERC-1155 qui contiennent 1 accessoire pour Luchadores, dont la rareté est déterminée par un aléatoire vérifiable ([Chainlink VRF](https://blog.chain.link/vrf-v2-mainnet-launch/)).
{{< /notice >}}


* Le protocole possède également une trentaine de Luchadores (⇒Yield en LUCHA) acheté avec une partie des profits de la première pinata : l’achat a été effectué en utilisant un agrégateur.
* Une place de marché est disponible pour les accessoires, avec paiement en LUCHA : une redistribution des frais collectés est également envisageable.

![luchadores](/img/2022/nft-defi-infrastructure/luchadores.png)

Le jeu n’est pas encore disponible (Alpha d’ici la fin Mars !), mais les interactions de ce type ne vont que se densifier au fur et à mesure de son développement. Avec l’arrivée du jeu, viendront de nouvelles fonctionnalités : staker ses tokens LUCHA permettra d’obtenir des MASK, un token non-transférable mais nécessaire pour acheter différents objets servant à augmenter la puissance de ses Luchadores.

Dès le lancement du jeu, les joueurs gagneront des LUCHA à chaque victoire. En fonction de leur classement, la quantité de LUCHA obtenus augmente : les meilleurs joueurs pourront ainsi dégager des retours intéressants, pour un coût initial très modéré (1 Luchador, potentiellement minté pour ~0.03 ETH). Soyez prêts !

Si vous découvrez les Luchadores avec cet article, n'hésitez pas à lire cette introduction : **[🤼 Vive la lutte libre (et vérifiable onchain)](https://tokenbrice.xyz/content/posts/2021/luchadores-nft.fr.md)**

---

## Et après ? 

Dans cet article, on est encore resté sur la partie visible de l’iceberg. À la croisée de la DeFi et des NFTs, il reste quantité de nouveaux cas d’utilisation possibles. Je vous propose d’en faire une liste accompagnée des principaux services qui explorent ces champs : 


### FloorDAO : NFT x DeFi x DAO

[FloorDAO](https://floor.xyz/) c’est en quelque sorte une couche supplémentaire construite sur NFTX. FloorDAO utilise le modèle OlympusDAO mais adapté pour les NFTs. L'objectif est d'assurer un rendement et soutenir la liquidité sur les collections concernées (Punk et Wizard pour l'instant). Comment ? Simple : pour les collections concernées, les possesseurs du token NFTX correspondant (ex WIZARD pour les Forgotten Wizards) ainsi que le LP (WIZARD/ETH) peuvent le bond pour obtenir des tokens FLOOR.

![floordao-bond](/img/2022/nft-defi-infrastructure/floordao-bond.png "La pertinence du bonding varie en fonction des besoins de la FloorDAO et de l'evolution du prix de FLOOR.")

Les tokens et LP collectés sont utilisés par FloorDAO pour produire un rendement (staking NFTX). La communauté (holders de gFLOOR) vote pour décider les prochains actifs à acquérir. Olympus utilise l'inflation de son token de gouvernance pour acquérir des actifs stratégiques commme DAI, LUSD, ou CRV ; FloorDAO fait la même chose mais avec pour cible des tokens NFTX et donc backés par un NFT.   

Là encore, le protocole possède une part de la liquidité sur FLOOR/ETH (sur Uniswap) et les frais générés par la position contribuent au rendement de la trésorerie.

### NFT pour collatéraliser des emprunts (sans passer par un ERC20/vault)

La principale limite à surmonter ici est bien sûr le fait que la vente de NFT se fait dans une logique bid/ask et n’est donc pas immédiate. Plusieurs projets s’attaquent malgré tout au problème :

* [DropsDAO](https://drops.co) : qui importe la logique des lending pools, pour des collections NFTs
* [Arcade.xyz](https://www.arcade.xyz/) : les OGs se souviennent d’ETHLend, l’ancêtre d’Aave. Arcade c’est la même logique mais pour des NFTs : un service d’emprunt sans pool, qui marche par offre/demande.
* [JPEGd'69](https://twitter.com/JPEGd_69) - qui devrait bientôt se lancer et permettre d'utiliser les CryptoPunks comme collatéral.
* Ou encore [NFTfi](https://www.nftfi.com/).


### Évaluation du prix de NFTs / oracle

Pour les emprunts, il faut une source de prix afin de déterminer si la position est solvable. Là encore plusieurs projets s’y collent :

* [Abacus](https://abacus.wtf/) - un service décentralisé pour évaluer le prix d’un NFT
* [Pilgrim](https://pilgrim.money/) - un AMM / méthode de valorisation pour les NFTs


### Location de NFT

La location permet par exemple d’emprunter un NFT pour jouer à un jeu sans avoir à le posséder. Elle crée aussi des opportunités pour les gros possesseurs de NFT d’une collection GameFi.

* [Rentable](https://beta.rentable.world/), un protocol généraliste pour la location.
* Prêt de vaisseau + partage de revenus générés avec sur [Cometh](https://www.cometh.io/)
* [Modèle scholarship Axie Infinity](https://axie.fr/tutoriel-scholarship-axie-quest-ce-quun-scholarship-et-comment-postuler/)

---

Enfin, pour aller plus loin dans votre exploration de l'infrastructure DeFinancière NFT / la NFTfi, n’hésitez pas à voir ou revoir le live réalisé avec CookingCrypto où on nous en discutons et revenons sur son expérience après plus d’un an dans les tranchées du minting/flipping de NFTs :

{{< youtube cdj-wXvIuwU >}}

_Merci à Charles, FrenchTony, Disiaque et Arthursw pour la relecture et correction de cet article._
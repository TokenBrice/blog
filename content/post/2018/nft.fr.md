---
title: Les tokens non fongibles expliqués par Tortank et Dracaufeu
description: >-
  Des concepts complexes rendus accessibles grâce aux carte Pokémon : le future de la tokénisation sur Ethereum, des tokens non fongibles aux ERCs
date: '2018-08-08T12:56:45.787Z'
categories: [NFT]
tags: [Ethereum, NFT, non fungible tokens, collectibles, ERC721, ERC1155, EcoCrypto]
image: /img/2018/nft/cover.png
difficulty: "beginner"
url: nft
aliases:
  - p/nft
---


«Non fongibles». Derrière ce nom énigmatique qui nous rappelle la garniture de nos omelettes, se cache un concept assez ancien qui trouve un second souffle aujourd'hui. Pour l'instant, cela se traduit surtout par des objets à collectionner et des jeux, mais le potentiel est énorme. En effet, **leur potentiel dépasse largement le simple cadre des jeux-vidéos**&nbsp;: documents officiels, titres de propriétés, traçabilité de l'art, etc


Posons les bases sur les tokens non fongibles (NFTs - Non Fungible Token en anglais) à l'aide de Pokémons avant d'en voir les usages potentiels et d'explorer le futur de la technologie.

### Tokens? Smart Contracts?

Avant de creuser les NFTs et de parler Pokémon, rappelons deux définitions utiles pour comprendre la suite de l'article :

*   **Les Smart Contracts** (contrats intelligents) sont des protocoles informatiques qui facilitent, vérifient et exécutent la négociation ou l'exécution d'un contrat.
*   **Les tokens** sont des smart contracts spécifiques codés afin de représenter un bien digital. Chaque token a des propriétés et des fonctions définies par rapport à son usage final.

### La fongibilité, kézako ?

Un bien fongible est un bien qui se caractérise par son appartenance à un genre& : chaque unité est interchangeable. Le terme est utilisé dans plusieurs disciplines, on se concentre ici sur la définition économique.

Passons tout de suite à des exemples concrets qui sont bien plus parlants que les définitions. Nos monnaies modernes telles que l'Euro ou le Dollar sont fongibles : un billet de 5€ en vaut un autre, et les deux sont parfaitement interchangeables. L'or est également un bien fongible : un kilogramme d'or pur est interchangeable avec un autre.

**Un bien fongible est donc standardisé : chaque unité de ce bien n'a rien d'unique, ce qui rend possible son échange avec ses pairs.**

### Et les biens non fongibles, ils ne sont pas comestibles alors ?


À l'inverse, il existe des biens non fongibles. Ce sont des biens qui **partagent des attributs communs mais qui ont leur propre identité**& : chaque bien possède un ensemble de valeurs unique pour chaque attribut qui est partagé avec l'ensemble du genre.


Le meilleur exemple que nous connaissons tous, ce sont bien sûr... Les cartes Pokémon ! Tant qu'à faire, prenons celle qui assurait le respect dans la cours de recré : Dracaufeu en personne.

![image](/img/2018/nft/charizard.jpeg)

Un carte Pokémon c'est :


1.  Un nom (+ niveau) : Dracaufeu Niv.76
2.  Des PV : 150
3.  Un type : feu
4.  Un talent : Dépense d'Énergie
5.  Une attaque et son coût : Danse Flamme (4 énergies feu)
6.  Des faiblesses et résistances : eau et résistance combat
7.  Un coût de retraite : 3

Chaque carte Pokémon est unique, mais toutes suivent cette typologie.


En effet, considérons la carte de Tortank : il a lui aussi les mêmes 7 attributs décrits plus haut, mais a des valeurs différentes pour chaque.

![image](/img/2018/nft/blastoise.jpeg)

C'est la combinaison de tous les attributs qui font l'unicité de la carte. Ainsi, toute carte de type feu à 150PV n'est pas un Dracaufeu, c'est simplement une carte qui partage 2 de ses 7 attributs (type et PV) avec Dracaufeu.


Ce petit détour par le monde des Pokémons nous explique l'essentiel du concept, le reste est son adaptation moderne. Ainsi, **les tokens non fongibles définissent une catégorie de biens qui partagent des attributs communs**. Néanmoins, chaque token a un unique jeu de valeurs pour ces attributs ce qui rend le token lui-même unique.


Pour ceux qui étaient trop jeunes ou vieux pour les cartes Pokémons, c'est le même concept qui sous-tend les cartes Magic, Yu-Gi-Oh !, World or Warcraft (le jeu de carte) et autres.

### La fongibilité version crypto

La plupart des cryptos que vous connaissez à l'heure actuelle sont considérées fongibles (⬇️ voir plus bas) : un Bitcoin en vaut un autre et les deux sont interchangeables. Idem pour Ethereum et tout ce que vous trouverez sur Coinmarketcap.


_Étant donné que l'historique des transactions de la plupart des cryptomonnaies est publique, celles qui ont été impliquées dans des activités illégales sont parfois repérées et bloquées sur les services d'échange. Ainsi, avoir un historique de transaction publique rend la fongibilité totale impossible. Les seules monnaies totalement fongibles sont celles se concentrent sur la protection de la vie privée, comme Monero où l'historique des transactions est secret._


Ce qui va nous intéresser aujourd'hui, ce sont les tokens non fongibles. Il y a eu plusieurs tentatives, dès 2013, pour créer des tokens non fongibles sans trop de succès. Ce qui a changé la donne, c'est un nouveau standard Ethereum, le ERC-721 qui permet la création de «  cryptocollectibles »  (barbarisme tout droit venu de l'anglais). Ce sont des biens uniques ayant leur propres propriétés tout en partagent un standard commun - essentiellement l'équivalent **des cartes Pokémon sur la Blockchain.**

**[📑 Cet article explore ce qui est fait avec les NFTs pour des fins communautaires ou artistiques.](https://tokenbrice.xyz/fr/nft-cas-d'utilisation/)**

### Les débuts avec le standard ERC-721

L'exemple le plus célèbre, ce sont les [CryptoKitties](https://www.cryptokitties.co/), des chats virtuels qui ont été les précurseurs du standard mentionné plus haut.

![image](/img/2018/nft/cryptokitties.png)

Lancé en Octobre, les CryptoKitties ont eu tellement de succès qu'ils ont provoqué une surcharge de l'ensemble du réseau Ethereum pendant plusieurs jours début Décembre, au summum de leur viralité.

Certains matous particulièrement désirables ont atteint des prix délirants, à 5 chiffres (en $) et changé de main plusieurs fois par semaine début Décembre. Face au succès, le standard est passé par toutes les étapes de validation pour être finalisé en juin 2018.

![image](/img/2018/nft/ck-price.png)


### Les tokens non fongibles dans le vrai monde

> When it comes to pushing and improving new technologies, you’ll often find porn and video games sharing the front line.

Pour l'instant et comme souvent, c'est le monde du jeux-vidéo qui porte l'innovation. En effet, quand il s'agit de pousser les limites des nouvelles technologies, ce sont souvent le porno ou les jeux-vidéos qui sont précurseurs.


Néanmoins les applications réelles des tokens non fongibles sont très nombreuses et beaucoup plus proches qu'on ne le croit. Les propriétés des NFTs font d'eux un support idéal pour «tokeniser » des biens réels. Tokeniser, c'est un autre import venu de l'Anglais : cela signifie **créer une token représentant un bien**. Le token en lui même n'a pas de valeur. **Il en acquiert une car le bien qu'il représente a une valeur bien réelle**.


### Tokenize everything!

Tokeniser permet de traiter le bien comme un token ce qui ouvre de nombreuses possibilités : échanges, transfert sans intermédiaires ou bien encore propriété fragmentaire (0.x). En outre, on peut envisager d'autre fonctionnalités adaptées à chaque type de bien : historique des propriétaires, historique de la valeur du bien, liste détaillée de ses caractéristiques, restrictions quant à qui peu le posséder...


Avec ça en tête, on se rend compte que **la tokenisation de biens réels pourrait permettre de se passer de nombreux intermédiaires aux tendances gloutonnes tout en gagnant grandement en fonctionalité.** Voici quelques exemples :

*   Tokenisation des biens immobiliers => plus besoin de notaire.
*   Tokenisation des œuvres d'art => de nombreux intermédiaires comme les
commissaires-priseurs verraient leur rôle remis en question.
*   Tokenisation des certificats (documents d'identité par exemple) => grand
ménage dans les institutions et acteurs nécessaires pour l'émettre
ainsi que dans celles qui chassent les fraudes.


Dans les trois cas cités plus haut, la vérification de l'authenticité des biens ainsi que de la réalité de la possession du bien par le propriétaire seraient grandement facilités.

#### Les bénéfices de la désintermédiation par tokenisation


La tokenisation peut aller au delà de la création d'un token représentant un bien réel. Revenons à la définition des tokens non fongibles décrite plus haut : «  des biens uniques ayant leur propres propriétés tout en partagent un standard commun ».


Cela s'applique tout aussi bien à des documents qui font offices de certificats. Ainsi, **les cartes d'identité, les passeports, les bulletins scolaires ou même encore les licences d'utilisation de logiciels pourraient se retrouver tokénisés**. Tout en facilitant leur émission et leur transmission, cela apporterait également une traçabilité sans commune mesure avec celle qui existe aujourd'hui pour ce genre de document (s'il y en a une). En outre, cela simplifiera grandement la détection et la lutte contre les fraudes.


En poussant la logique encore plus loin, et en revenant au monde digital, on peut envisager **des NFTs pour représenter notre identité digitale** - des profils sur les réseaux sociaux qui serait open-source par exemple, et ainsi facilement exportables d'un réseau à l'autre. Cela nous permettrait en outre d'avoir un contrôle total sur nos données ce qui empêcherait leur appropriation par des tiers malveillants.


Avant d'en arriver là, il faudra commencer par **dépasser les limites actuelles d'Ethereum et des tokens non fongibles** : comme on le disait plus haut, les CryptoKitties ont surchargé le réseau Ethereum pendant plusieurs jours. La technologie actuelle (celle de décembre pour le moins) n'est clairement pas utilisable à grande échelle.

### Les ERCs - Les nouveaux standards pour Ethereum

Concernant le réseau Ethereum, l'effort est en marche ! Différents projets travaillent depuis plusieurs années déjà à l'optimisation technique du réseau, comme OmiseGo/Plasma ou encore la prochaine mise à jour de d'Ethereum (Casper). Vous trouverez des articles dans les sources qui couvrent ces sujets ; ce qui nous intéresse aujourd'hui ce sont les NFTs, alors revenons y.


L'ERC-721 est un bon début, mais il pose **plusieurs problèmes à l'échelle**. Avant d'en venir là, faisons un petit point sur les ERC. Un ERC (Ethereum Request for Comments) est une proposition soumise par un développeur de la communauté Ethereum qui décrit des méthodes, comportements, innovations ou recherches applicables au fonctionnement du réseau. Une fois acceptée, un ERC devient un standard. Une fois encore, l'exemple rend ça plus palpable : le standard le plus connu pour ethereum est l'ERC-20, il décrit un token simple et fongible.


Le principal intérêt des ERCs est qu'ils permettent d'intégrer facilement les tokens suivants ce standard à l'écosystème : **pas besoin de connaître les spécificités d'un token pour le manipuler, puisqu'il répond à un jeu de méthode communs à d'autres** (définit par l'ERC qu'il suit). C'est la raison pour laquelle un portefeuille (wallet) compatible avec ERC-20 peut supporter n'importe quel token ERC-20 sans nécessiter de développement spécifique à chaque nouveau token.

#### L'ERC-1155, le futur des tokens non fongibles ?

L'ERC-1155 est un nouveau standard pour les NFTs proposés par Witek Radomski, le co-fondateur d'[EnjinCoin](https://enjincoin.io/) une plateforme faite pour faciliter le développement de jeux avec des biens tokénisés sur Ethereum.


**L'ERC-1155 résout plusieurs problèmes techniques posés par l'utilisation à grande échelle de tokens ERC-721 tout en apportant de nouvelles fonctionnalités**. Du point de vue de l'optimisation technique, et sans rentrer dans trop de détails, l'ERC-1155 permet l'utilisation d'un code commun à plusieurs tokens/collections de tokens non fongibles différents. Cela permettra de supporter un volume bien plus grand de transactions, le tout pour la même charge sur le réseau Ethereum (comparé au ERC-721).

![A transaction involving several fungible and non-fungible goods thanks to ERC-1155](/img/2018/nft/erc1155.png)
A transaction impliquant plusieurs tokens fongibles et non fongibles grâce au à l'ERC1155

On peut également noter notamment la possibilité d'échanger plusieurs objets en une seule transaction. Avec l'ERC-721, si Bob veut échanger CryptoKitty #1, #2, #3 et #4 contre le CryptoKitty #5 d'Alice, cela va nécessiter 5 transactions au total, alors qu'une seule serait suffisante avec l'ERC-1155.


**L'ERC-1155 supporte également les objets/tokens fongibles** qui sont très nombreux dans les jeux en lignes : pièces d'or, potions, flèches et autres consommables... L'utilisation du seul standard ERC-1155 (contre un mélange d'ERC-20 pour les fongibles et ERC-721 pour les non fongibles) simplifie grandement la donne pour les développeurs.


Finalement, une des dernières grande nouveauté est la gestion de la fongibilité par groupe : il sera ainsi possible de différencier les différentes itérations d'un même objet, et le premier possesseur de celui-ci pourra effectivement prouver qu'il l'est.

### Conclusion

Les biens non fongibles sont en plein essor, et Ethereum mène la charge. Le mieux pour comprendre les ramifications du concept de token non fongible reste encore d'aller voir les utilisations concrètes qui en sont faites. Faison donc un petit tour d'horizon loin d'être exhaustif pour finir. Il n'y a pas que les cryptokitties dans les NFTs :

![Gods Unchained](/img/2018/nft/godsunchained.png)
Gods Unchained

*   [Gods Unchained ](https://godsunchained.com/): On a utilisé les jeux de cartes pour introduire le concept de non fongibilité plus haut, on les retrouve logiquement ici. GodsUnchained est l'un des plus connus et s'appuie sur le standard ERC-721. Les bénéfices par rapport aux jeux de carte classiques (comme Hearthstone) sont nombreux : immutabilité des cartes après la phase de beta (fini les nerfs surprises), transparence quant à la rareté de chaque type de carte, traçabilité des possesseurs précédents de chaque carte... L'accent est mis sur l'eSport avec un premier championnat du monde début 2019.
*   [Decentraland ](https://decentraland.org/): Imaginez Minecraft, en réalité virtuelle, avec des mécanismes basés sur la Blockchain pour gérer les titres de propriété : bienvenue dans le futur ! Une fois possesseur d'une parcelle, libre aux utilisateurs d'y créer/développer l'expérience de leur choix (grâce au SDK) ; ils pourront ensuite en contrôler l'accès à leur guise, et donc le faire payer s'ils le souhaitent. Decentraland est une expérience humaine et sociale à l'échelle mondiale. Elle sera assurément pleine de surprises !

![A creature of Augmentors](/img/2018/nft/augmentors.png)
Une créature dans Augmentors

*   [Augmentors](https://www.augmentorsgame.com/) : On parlait de Pokémons en début d'article, mais quid de Pokémo GO ? Augmentors jeu combine réalité augmentée et Blockchain pour proposer un jeu où les NFTs permettent à chacun de posséder réellement ses créatures et de les échanger à sa guise.

Il pourrait être tentant de sous-estimer les NFTs, de les voir comme un truc pour gamins ou barbus collectionneur de cartes. Néanmoins c'est tout l'inverse : les CryptoKitties l'ont montré, les NFTs comptent parmi les meilleurs chevaux de Troie pour faire rentrer la décentralisation dans les mœurs de la population générale.


Comme souvent avec les nouvelles technologies, le développement technique n'est que l'échauffement.** La vraie bataille est au niveau de l'acception sociale et légale ; à ce niveau là, les cryptominous et autres collectibles sont des précurseurs.**

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/channel/UCefQC4Y-X9MBRuYBKc2waiQ)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}

#### Sources / Deep Dive

*   [_Mapping the Emerging Non-Fungible Token Landscape_](https://medium.com/point-nine-news/mapping-the-emerging-non-fungible-token-landscape-ee56f0d1079f) — Pawel Chudzinski on Medium, 06/15/2018.
*   [_ERC-721 Ethereum standard confirmed and finalized!_](https://medium.com/0xcert/erc-721-ethereum-standard-confirmed-and-finalized-73b78f7ea315) — 0xcert on Medium, 06/24/2018.
*   [_Porn Drives Tech Innovation Again, This Time In VR _](https://www.huffingtonpost.com/entry/porn-drives-technological-innovation-again-this_us_59f8085de4b094db8e76f834)— Jarone Ashkenazi on the HuffPost, 10/31/2017.
*   [_Explained: Ethereum Plasma_](https://medium.com/@argongroup/ethereum-plasma-explained-608720d3c60e)— Lukas Schor on Medium/ArgonGroup, 05/28/2018.
*   [_Ethereum Casper 101_](https://medium.com/@jonchoi/ethereum-casper-101-7a851a4f1eb0) — Jon Choi on Medium, le 10/22/2017.
*   [_A Proposal To Shake Up Ethereum — A New Standard On The Horizon? Mapping the Emerging Non-Fungible Token Landscape_](https://hackernoon.com/a-proposal-to-shake-up-ethereum-a-new-standard-on-the-horizon-d2dfa88507a6) — Ermos Kyriakides on HackerNoon, 06/27/2018.

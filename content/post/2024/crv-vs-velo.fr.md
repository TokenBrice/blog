---
title: "Nuances subtiles avec de grandes conséquences : une analyse croisée de Curve et Velodrome"
description: "Le modèle Velodrome, inspiré par veCRV, atteint un alignement supérieur entre les trois participants clés d'un DEX - les LPs, les détenteurs de tokens et les projets ayant besoin de liquidité. Pourtant, la plupart de l'espace DeFi ne comprend toujours pas pourquoi : mais pas vous anon - une fois que vous aurez lu cet article."
date: '2024-03-21T01:13:50.191Z'
categories: [DeFi]
tags: [DeFi, Ethereum, Decentralized Finance, Curve Finance, veCRV, Velodrome, veVELO, Aerodrome, veAERO]
url: crv-vs-velo
image: img/2024/crv-vs-velo/cover.png
difficulty: "expert"
---

Aujourd'hui, je veux aborder Velodrome/Aerodrome, une véritable success story en DeFi. J'ai couvert les DEX de manière extensive sur ce blog, en particulier Curve : cet article comparera les deux modèles et expliquera comment Velodrome a amélioré le modèle veCRV.

Tout d'abord, commençons par un avertissement : il y a deux composants principaux d'un DEX que tout le monde doit connaître pour comprendre ce qui suit :

1. Les structures de liquidité qu'il fournit (x\*y=k, stableswap, CL, stableswap-NG, curve V2, etc.)
2. Le modèle d'incitations, qui pour un DEX est synonyme de ses tokenomics.

Cet article se concentre sur ce dernier, le cœur de l'innovation de [Velodrome](https://www.defiscan.info/protocols/velodrome-v2/optimism). Cet article suppose une familiarité de base avec les tokenomics veCRV de Curve ; si ce n'est pas le cas, je vous encourage à [lire mon écrit précédent à ce sujet](https://tokenbrice.xyz/fr/crv-wars), posté il y a trois ans mais toujours utile pour comprendre le modèle.

## A/ veCRV/veVELO Collecte et Distribution des Frais

La collecte et la redistribution des frais sont les lignes de vie d'un échange décentralisé. Ici, la simplicité est généralement bonne, car le leader du segment DEX Uniswap opère toujours sous un modèle extrêmement simple mais brutalement efficace, où 100 % de l'argent collecté va aux fournisseurs de liquidité.

Avec le lancement de son token CRV en août 2020, Curve a exploré une voie alternative, où 50 % des frais collectés sur une paire donnée vont aux fournisseurs de liquidité et les 50 % restants à la « DAO » (frais admin), c'est-à-dire aux détenteurs de veCRV. Curve a introduit le concept de « gauges de liquidité », où les détenteurs de tokens verrouillés (veCRV) peuvent diriger les émissions à recevoir par les fournisseurs de liquidité, créant une base d'incitations indépendante du volume traité.

Velodrome a été lancé deux ans plus tard, à la fin de mai 2022, et a exploré une autre division, inspirée d'un projet précédent itérant sur le modèle Curve : Solidly. Ici, **les LPs n'ont aucune exposition aux frais collectés sur les paires pour lesquelles ils fournissent de la liquidité et sont entièrement incités par les émissions de tokens**.

La différence principale entre veCRV et veVELO réside dans la manière dont ils gèrent les frais collectés au niveau du DEX/DAO, où nous observons des différences dans le montant des frais collectés et leur modèle de distribution.

Plongeons dans les nuances de ce sujet : elles sont clés pour comprendre les avantages et inconvénients de chaque mode.

### A.1/ Montant des frais distribués : VELO = 2 x Curve

Curve et Velodrome opèrent sous la même logique de base : chaque semaine, un montant donné de tokens CRV/VELO est émis et distribué aux fournisseurs de liquidité. Chaque pool a une gauge associée pour laquelle les détenteurs de veCRV/veVELO peuvent voter, et l'allocation budgétaire hebdomadaire suit la proportion du « vote de gauge » : si une gauge reçoit 1 % du vote total veCRV/veVELO, 1 % de toutes les émissions produites cette semaine lui sera dirigé.

Ces émissions sont essentiellement le coût principal pour le DEX : le prix payé pour attirer et retenir la liquidité. Ce qui compte alors est ce qui se trouve de l'autre côté du bilan – les revenus : dans notre cas, ce sont les frais collectés.

Sur Curve, les revenus proviennent des « frais admin » de chaque pool, qui sont généralement fixés à 50 %. Cela signifie que les frais collectés sur une pool donnée sont divisés 50/50 entre le LP et la DAO/détenteurs de veCRV.

![curve-revenues](img/2024/crv-vs-velo/curve-revenues.png "Aperçu des Revenus de Curve : le bleu clair représente les frais admin, en jaune les frais payés au LP, et en bleu foncé les revenus provenant du stablecoin crvUSD - source: curvemonitor.com")

Sur Velodrome, c'est simple : les fournisseurs de liquidité n'ont aucune exposition aux frais collectés sur la pool qu'ils fournissent ; ils sont incités uniquement par les émissions $VELO, ce qui signifie que la DAO/détenteurs de veVELO obtiennent 100 % des frais générés sur le DEX.

Bien que cette différence principale ait déjà un impact massif, la suivante est encore plus significative car elle concerne la manière dont ces frais sont distribués aux détenteurs de veCRV/veVELO.

### A.2/ Modèle de distribution des frais : une approche plus juste et plus efficace

Curve utilise un modèle qui pourrait être décrit comme **un système de mutualisation des frais** : les frais que reçoivent les détenteurs de veCRV dépendent uniquement du montant de veCRV qu'ils contrôlent. Sans entrer dans les détails techniques, ces frais sont collectés dans les divers tokens impliqués dans la pool (comme USDC/USDT/DAI pour la 3pool), et chaque semaine, récoltés, échangés contre des tokens LP 3pool, puis rendus disponibles pour réclamation aux détenteurs de veCRV – comme vous pouvez le voir, cela nécessite une infrastructure pour fonctionner, dont le coût augmente avec le nombre de pools sur le DEX Curve.

D'un autre côté, Velodrome fournit un modèle supérieur sur toutes les dimensions, car il atteint un meilleur alignement DEX/LP/détenteur de token sans aucune infrastructure requise. Voyons comment.

Simplement dit, **Velodrome relie l'activité de vote de gauge à la distribution des frais**. Ici, le montant de veVELO que l'on contrôle compte, mais ce qui est encore plus important est la pool pour laquelle on vote puisque les **votants sont exposés uniquement aux frais collectés sur les paires pour lesquelles ils votent.** Ils collectent les frais en tant que tels (c'est-à-dire qu'un votant de la pool ETH/USDC obtient ETH et USDC), ce qui signifie que l'infrastructure requise est beaucoup plus gérable.

Velodrome lie la distribution des frais à l'activité de vote de gauge : les détenteurs de veVELO reçoivent les frais collectés sur la pool qu'ils votent SEULEMENT, payés en tant que tels chaque semaine. Cela permet un meilleur alignement des détenteurs de veVELO avec les meilleurs intérêts de Velodrome en tant que DEX par rapport à Curve.

Cette simple torsion crée un volant d'inertie de vote intéressant. Les paires à haut volume collectent beaucoup de frais, ce qui signifie des incitations élevées pour les votants. Cela conduit à de nombreux votes, qui dirigent des émissions sensées vers la paire, attirant plus de fournisseurs de liquidité, permettant plus de volume traité, etc., jusqu'à ce qu'un point d'équilibre soit atteint. Cela signifie que les paires à haut volume se maintiennent d'elles-mêmes sans pots-de-vin ou un baleinier votant bienveillant minimisant les profits, ce qui n'est pas le cas avec Curve.

![velodrome-revenues](img/2024/crv-vs-velo/velodrome-revenues.png)
Aperçu des Revenus de Velodrome - [source: tableau de bord 0xkhmer](https://dune.com/0xkhmer/velodrome)

![aerodrome-revenues](img/2024/crv-vs-velo/aerodrome-revenues.png)
Aperçu des Revenus d'Aerodrome - [source: tableau de bord 0xkhmer](https://dune.com/0xkhmer/aerodrome)

### A.3/ Ce que cela signifie en pratique

Assez avec les explications ; illustrons en considérant le cas d'un votant veCRV/veVELO, qui a décidé de voter pour une paire traitant un volume minimal (la situation est courante).

Sur Curve :

1. Un détenteur significatif de veCRV vote pour une pool traitant un montant marginal de volume par rapport à sa TVL, soit pour collecter un pot-de-vin, soit parce qu'il veut soutenir les tokens impliqués dans la pool.
2. Son activité de vote est préjudiciable à Curve en tant que DEX car il dirige les émissions là où elles sont inutiles.
3. Il reçoit la même quantité de 3CRV qu'un votant plus aligné sur Curve avec un sac veCRV équivalent essayant de diriger les incitations pour maximiser le volume.

Maintenant sur Velodrome :

1. Un détenteur significatif de veVELO vote pour une pool traitant un montant marginal de volume par rapport à sa TVL, soit pour collecter un pot-de-vin, soit parce qu'il veut soutenir les tokens impliqués dans la pool.
2. Son activité de vote est préjudiciable à Velodrome en tant que DEX car il dirige les émissions là où elles sont inutiles.
3. Il reçoit un montant marginal de frais puisque la pool pour laquelle il vote traite un volume marginal.

La situation est la même en sens inverse pour voter sur une pool à haut volume qui serait d'intérêt pour le DEX :

* Sur Curve, ce votant aligné sur le DEX recevra la même quantité de 3CRV que quiconque détenant le même sac.
* Sur Velodrome, ce votant aligné sur le DEX sera bien récompensé, car il sera un votant majoritaire sur une paire à haut volume : une situation idéale pour maximiser les frais gagnés.

Des deux côtés, des pots-de-vin sont payés aux votants et peuvent mener à des situations où les votes sont dirigés vers des pools qui ne sont pas optimaux en termes de volume traité. Cependant, sur Curve, il n'y a aucune pénalité pour le faire. Sur Velodrome, les corrupteurs de tels pools concurrencent les pools à haut volume offrant des APR attractifs aux votants, avec ou sans pots-de-vin.

La même chose, sous un autre angle : sur Curve, le coût des pots-de-vin dépend uniquement de la valeur des émissions CRV. Sur Velodrome, le prix de base qu'un projet doit payer pour rassembler des votes dépend des pots-de-vin totaux + des frais collectés sur les autres pools. Cela signifie que les pools à haut volume poussent le coût des pots-de-vin à la hausse, entretenant encore un autre volant d'inertie dans le volant d'inertie.

Comprendre ce qui précède signifie comprendre la différence principale entre les modèles Curve et Velodrome. Cependant, pour obtenir l'image complète, plus d'éléments doivent être considérés. Discutons maintenant du boost LP.

## B/ Boosts LP et son impact sur l'écosystème

Le boost LP, comme on l'appelle, est une fonctionnalité spécifique à Curve. De nombreux protocoles forçant les tokenomics veCRV, comme Balancer avec son veBAL, l'utilisent également. Il permet aux détenteurs de veCRV de gagner plus de récompenses CRV sur leur LP, en tenant compte de plusieurs éléments, y compris la taille de leur sac veCRV et la taille de leurs diverses LPs. Ainsi, avec une propriété veCRV appropriée, un LP peut obtenir un « Boost LP » jusqu'à 2,5x par rapport au taux d'émission de base.

### B.1/ Boost LP expliqué

Pour maximiser le boost obtenu, jusqu'à 2,5x maximal, il faut :

1. Posséder autant de veCRV que possible
2. Avoir des positions LP dans autant de pools que possible.
3. Avoir un montant proportionnel/équilibré de TVL dans ces diverses pools.

**Simplement dit, le Boost LP est un jeu truqué dès le départ**. Il n'est pas conçu pour bénéficier aux détenteurs individuels de veCRV sur leur LP mais pour attirer des méta-protocoles, comme Convex, qui peuvent atteindre 1+2+3 de manière consistente. **La croissance de Convex n'est pas une success story ; elle est par design (le design de Curve)**. Si ce n'était pas Convex, un autre protocole similaire posséderait la plupart de l'offre veCRV. Nous avons observé des patterns similaires avec d'autres protocoles qui ont adopté le Boost LP : Balancer a Aura. Convex et Aura contrôlent > 50 % de l'offre veCRV/veBAL.

Velodrome et Aerodrome évitent complètement la possibilité d'un nouveau protocole gobant l'offre en n'ayant aucun mécanisme de boost. Comme nous l'avons vu avec Curve, Convex a émergé et capturé la plupart de l'offre ; maintenant, tous les LPs gagnent avec un boost, et aucun ne bénéficie d'une quantité disproportionnée de CRV. Le système a convergé vers tout le monde gagnant à peu près le même boost effectif, ou dans le cas de Velodrome/Aerodrome, aucun boost puisque le résultat futur aurait été des LPs gagnant le même boost effectif. L'autre fait reste que puisque Convex a une majorité de CRV verrouillé, ils contrôlent la gouvernance future de CRV.

### B.2/ Conséquences du Boost LP

L'existence du Boost LP appelle une couche comme Convex au-dessus du DEX ; il n'y a pas moyen d'y échapper. À ce stade, certains pourraient penser : « Donc vous avez un protocole qui gobe la plupart de vos émissions et les verrouille pour toujours ; quel est le problème ? »

La réponse est simple : c'est simplement un design inefficace puisque ces méta-couches fournissent des fonctionnalités qui pourraient être délivrées de manière moins convolutée au niveau de base (par le DEX lui-même) et sans les frais.

Curve a besoin de Convex et du marché des pots-de-vin : Votium, Warden, et Hidden Hands. Mais aussi l'auto-compoundeur/gestionnaire de délégation de vote : Airforce Union, Concentrator, etc. Vous finissez avec des dizaines de protocoles prenant des frais ici et là pour délivrer quelque chose que Velodrome parvient à intégrer nativement. Cela rend l'expérience plus complexe pour les utilisateurs, qui doivent connaître ces dizaines de protocoles et leurs subtilités pour tirer le meilleur parti de Curve.

Rappelez-vous aussi comment, en discutant de la distribution des frais, nous avons mentionné que Curve nécessitait une infrastructure beaucoup plus dense pour fonctionner ? Eh bien, imaginez le chaos que veCRV + Boost LP est en backend. Il y a une raison pour laquelle à la fois Curve et Balancer prennent des âges pour déployer sur une nouvelle L2, et souvent avec des fonctionnalités partielles (comme pas de Boost LP, surprise surprise.).

## Expansion fluide au-delà de ce que Curve offre

Sur Velodrome, le marché des pots-de-vin est intégré : les projets peuvent poster leurs pots-de-vin directement sur le frontend de Velodrome, et les votants peuvent vérifier les pots-de-vin disponibles et voter au même endroit. De nouvelles fonctionnalités continuent d'être délivrées et ajoutées à la même interface utilisée par tous les participants : LPs, projets, et détenteurs de tokens.

### Relais Velodrome

Elles vont des améliorations de qualité de vie / économie de gaz, comme le « auto-max-lock », économisant aux verrouilleurs qui souhaitent rester max-verrouillés pour maximiser leur pouvoir de vote de gauge la peine de le faire manuellement, à des fonctionnalités beaucoup plus étendues, comme Relay, un système de gestion de positions veVELO.

![velodrome-relay](img/2024/crv-vs-velo/relay.png)

C'est un outil destiné aux projets utilisant Velodrome pour développer la liquidité sur leurs paires. Il leur permet de configurer leur stratégie de vote et de corruption et de l'implémenter automatiquement : plus besoin de soumettre des transactions hebdomadaires. Relay a un autre avantage, puisque actuellement, la stratégie disponible est une veVELO-maxi, composant tous les frais et pots-de-vin collectés en VELO et les reverrouillant pour maximiser le pouvoir de vote : cela crée un puits VELO considérable, directement indexé sur les frais distribués par l'échange. [Presque 1/5 de tous les veVELO y sont déjà](https://twitter.com/VelodromeFi/status/1762908204894445834).

Au fur et à mesure que la fonctionnalité Relay mûrit, plus de stratégies seront disponibles pour ses utilisateurs, y compris certaines qui composent tous les frais et pots-de-vin gagnés en veVELO mais, par exemple, les rendent réclamables en ETH ou USDC. Cela s'avérera très pratique pour les détenteurs de veVELO qui ne cherchent pas à soutenir un projet en particulier.

### veNFT : Positions verrouillées tokenisées

Velodrome a d'autres innovations astucieuses intégrées, comme le veNFT encore sous-apprécié : avec Curve, veCRV est non transférable, rendant leur gestion douloureuse. Velodrome peut atteindre le même alignement mais permet la transférabilité : les positions veVELO sont représentées par un veNFT qui peut être transféré. Il n'y a aucun moyen de racheter un veNFT donné pour les tokens VELO sous-jacents à part attendre l'expiration du verrou. Cependant, cela facilite la gestion d'une telle position en permettant son transfert. Il y a aussi [un marché OTC pour les veNFT veVELO](https://decode.market/), où les détenteurs peuvent vendre leur position à des acheteurs intéressés à un discount fluctuant par rapport à la valeur des tokens VELO sous-jacents.

### Une compréhension profonde de la nature du jeu

Des échanges comme Curve ou Velodrome sont un type de produit particulier dans le paysage DeFi. En termes d'affaires réguliers, **ils pourraient être décrits comme B2B2C : Business to Business to Consumer**. Ils sont B2B parce que leurs premiers clients sont d'autres projets – les divers protocoles cherchant de la liquidité. S'ils servent avec succès ce marché, les projets qu'ils intègrent à leur DEX feront le travail B2C pour eux, car leurs pools de liquidité présentent des opportunités à leurs détenteurs de tokens respectifs.

À cet égard, je pense que Curve a complètement échoué. Avec sa pyramide de solutions imbriquées les unes sur les autres, Curve est particulièrement peu convivial pour l'intégration des projets. Ils veulent corrompre ? D'accord, décidez entre veCRV ou vlCVX sur Bribe.crv, Votium, Warden, ou StakeDAO. Ils veulent gérer leur propre CRV ? Bien, choisissez juste entre veCRV, aCRV, cvxCRV, sdCRV, vlCVX, uCRV, etc. Bien que cette myriade d'options puisse ravir les enthousiastes de Curve, elle se transforme, à mon avis, en une qualité négative pour le côté B2B des choses.

En contraste, l'expérience avec Velodrome est fluide : un endroit où tout se passe, une option pour chacune – sans besoin de comparer entre une demi-douzaine d'alternatives cryptiques et parfois trompeuses. Couplé aux caractéristiques précédentes des jeux veCRV discutées avant, en particulier le Boost LP, cela rend [l'écosystème Curve particulièrement peu convivial pour les nouveaux entrants](https://tokenbrice.xyz/farewell-glc/#the-case-of-the-crv-wars) : **qui voudrait entrer dans une course truquée en faveur des premiers entrants trois ans après son début** ?

![tour-de-op](img/2024/crv-vs-velo/tour-de-op.png)

De plus, les efforts BD de Velodrome sont remarquables ; l'équipe est largement disponible pour aider à intégrer de nouveaux projets, et plusieurs programmes sont conçus pour rendre l'expérience aussi simple et convaincante pour les nouveaux entrants, regroupés sous l'umbrella « Tour de OP », qui inclut un programme de matching de pots-de-vin, des bonus de verrou et des boosts de vote.

## MOTS DE LA FIN

Comme vous avez pu le voir, à la fois Velodrome & Aerodrome ont attiré beaucoup d'attention dernièrement, grâce à leur token voyant un momentum positif : je pense que c'est bien mérité. La sortie de Slipstream, l'implémentation de Velodrome de la Liquidité Concentrée, augmentera le volume traité par unité de TVL, débloquant la prochaine phase de croissance du volant d'inertie. Aerodrome, le fork de Velodrome sur le réseau Base, a vu une croissance spectaculaire depuis son lancement il y a six mois, démontrant davantage la viabilité du modèle.

À plus long terme, l'équipe Velodrome commence à [se référer à Velo comme un « MetaDEX »](https://medium.com/@VelodromeFi/velodrome-the-metadex-48e4af1ef9a4), hintant à Velodrome devenant le hub de liquidité de base non seulement d'Optimism mais pour toute la Superchain : toutes les chaînes construites sur la stack OP.

Le temps dira, mais Velodrome est déjà un succès retentissant sur Optimism, donc gérer un DEX cross-chain correctement serait un game changer. C'est particulièrement vrai en considérant à quel point Curve & Balancer ont échoué là – non parce qu'ils n'ont pas essayé, mais simplement parce que leur infrastructure convolutée avec Boost LP rend le déploiement cross-chain douloureux (Bonjour AuraFinance distribuant AURA sur des chaînes où... il n'y a pas de liquidité pour $AURA).

PS : J'adresse ici la partie DEX de la suite de produits, qui est le produit complet pour Velodrome mais pas pour Curve, qui a maintenant crvUSD et Llamalend. Pourtant, même avec crvUSD inclus, Aerodrome collecte et redistribue maintenant plus de frais que Curve, tout cela en étant présent sur une seule chaîne vs 13 pour Curve. Alors que Curve-DEX a été sous-performant pendant un moment, l'équipe a prouvé à plusieurs reprises être innovante et capable de rebondir. Les revenus crvUSD ont déjà dépassé ceux de Curve-DEX, et qui sait ce que Llamalend pourrait accomplir.

Game on : attendons et voyons.
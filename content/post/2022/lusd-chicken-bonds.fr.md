---
title: "Chicken Bonds : synergie DeFi x NFT pour résoudre le problème de l'oeuf et de la poule de la ĺiquidité en finance décentralisée"
description: "Comment les Chicken Bonds de Liquity utilisent des NFT dynamiques pour soutenir la liquidite du LUSD et aligner les utilisateurs."
date: '2022-10-17T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Stablecoin, Yield]
tags: [DeFi, Ethereum, Stablecoins, Stable Assets, Money Markets, Liquity, LUSD, Chicken Bonds, NFT, NFTfi]
series: stablecoin-arc
series_order: 5
toc: true
tocNum: true
url: lusd-chicken-bonds
aliases:
  - p/lusd-chicken-bonds
image: /img/2022/lusd-chicken-bonds/lusd-chicken-bonds-cover-tokenbrice.png
difficulty: "beginner"
---

Liquity a récemment publié les LUSD Chicken Bonds, une **expérience de théorie des jeux fusionnant des éléments DeFi et NFT pour accroître la liquidité du LUSD et réduire sa prime de prix**.

Bien que les Chicken Bonds s'appuient sur des protocoles existants, tels que Yearn, b.protocol, ou Curve, ils mettent également en place de nouveaux mécanismes, dont les deux principaux sont les suivants :

1. **"No maturity principal-protected bonding"** : Les Chicken Bonds utilisent un nouveau type de bonds offrant de fortes garanties au déposant, y compris la possibilité de récupérer la totalité du capital initialement fourni sans frais (Chicken Out).
2. **Participer pour gagner des NFT dynamiques** : En interagissant avec le protocole LUSD Chicken Bonds, les utilisateurs obtiennent un **NFT dynamique** qui évolue en fonction de leurs choix et des interactions précédentes sur le réseau.

Les Chicken Bonds s'attaquent à l'un des principaux enjeux de la DeFi, la croissance durable des pools de liquidité, en commençant par LUSD. À terme, le modèle sera mis à disposition dans une version sans permission généralisable pour tout protocole ayant besoin de liquidité.

Ce billet détaille le fonctionnement et les résultats attendus des [LUSD Chicken Bonds](https://chickenbonds.org). Cependant, avant de répondre à ces questions, il est nécessaire d'avoir un contexte supplémentaire sur les LUSD : commençons !

## Le contexte : La prime de prix sur LUSD

L'une des dimensions les plus mal comprises du modèle de Liquity est le **mécanisme d'ancrage du LUSD**. En effet, alors que le LUSD présente de fortes garanties (hard peg) que le LUSD>1,00$ (rachat) et &lt;$1,10 (ratio de collatéralisation minimal de 110%), entre les deux, l'équilibre repose davantage sur un **jeu d'incitations (soft peg)**.

Dans le sillage de [la répression de l'OFAC sur Tornado Cash](https://blog.chainalysis.com/reports/tornado-cash-sanctions-challenges/) en août, il y a eu une **augmentation de la demande** de monnaies stables résistantes à la censure. Pourtant, l'appétit pour l'effet de levier est faible en raison de la détérioration des conditions du marché. Ainsi, si la demande de LUSD est élevée, une part importante de ses adeptes l'achète à un prix élevé sur les marchés au lieu de le frapper en utilisant leur ETH comme garantie.

Ces deux facteurs ont convergé au cours des derniers mois, conduisant à une **prime soutenue** pour le LUSD, qui se négocie souvent dans une fourchette de 1,02 à 1,04 dollar. Je ne m'étendrai pas trop sur ce sujet ici, car il a déjà été abordé sur le blog de Liquity : **[The Premium of Resiliency](https://www.liquity.org/blog/the-premium-of-resiliency)**. Cependant, discutons de **l'impact de la prime sur les utilisateurs de Liquity** car il a des conséquences réelles.

![lusd-peg-incentives](/img/2022/lusd-chicken-bonds/lusd-peg-incentives.png)

### Impact de la prime LUSD

L'impact d'une prime de prix sur les emprunteurs **peut être positif ou négatif**, en fonction de leur timing et de leurs actions. Les emprunteurs qui s'inquiètent de la volatilité du prix du LUSD peuvent utiliser les Chicken Bonds, ou b.protocol pour préserver une exposition pure au LUSD tout en obtenant des rendements.

{{< notice info >}}
Il convient de noter que les emprunteurs qui préservent une exposition à 100% au LUSD ne subissent aucune conséquence des fluctuations de son cours puisqu'ils n'ont pas besoin de le racheter lors du remboursement de leur dette.
{{< /notice >}}

Cependant, le fait que le LUSD fluctue peut également profiter aux utilisateurs avertis qui peuvent arbitrer les écarts :

1. **Marge bénéficiaire** | Plus le LUSD dépasse 1 $, plus il est rentable d'effectuer une opération d'arbitrage sur son peg : à 1,01 $, le short du peg rapporte 0,01 $ par LUSD en cas de succès. À 1,09 $, les profits passent à 0,09 $ par LUSD.
2. Plus le LUSD s'éloigne de 1,00 $ et plus il se rapproche de 1,10 $, plus il est **probable** que les arbitragistes du peg l'emportent sur les acheteurs de LUSD et poussent ainsi le prix à la baisse.

Ainsi, l'arbitrage des LUSD est un jeu d'équilibre entre la maximisation des profits (1) et leurs chances de réalisation (2). En d'autres termes, au-delà d'un certain niveau de prix, l'opération d'arbitrage devient **trop rentable et trop susceptible de se réaliser pour que les arbitragistes l'ignorent**. Cela a contribué à ce que la paire LUSD reste dans la partie inférieure de son ancrage souple, entre 1,00 et 1,05 dollar, même pendant les phases de pic de la demande.

Pour les utilisateurs qui ne surveillent pas la situation en permanence, cependant, cela peut se traduire par une perte de capital - par exemple, si l'on emprunte des LUSD alors que le prix est à 1,02 $, qu'on les investit dans autre chose, puis que quelques semaines plus tard, on essaie de racheter des LUSD pour rembourser sa dette, pour se retrouver avec un prix à 1,04 $.

Ainsi, les fluctuations du LUSD dans la fourchette 1,00-1,10 ajoutent **une couche supplémentaire d'incertitude pour les emprunteurs**. L'augmentation de la liquidité du LUSD et la stabilisation de sa parité contribueront à restaurer la confiance des emprunteurs et à rationaliser les interactions avec le protocole.

## Ca, c'était avant les Chicken Bonds

![lusd-chicken-bonds](/img/2022/lusd-chicken-bonds/chicken-bonds.png)

Pour résoudre le problème de liquidité du LUSD, l'équipe Liquity a travaillé sur un **nouveau protocole**, d'abord testé avec le LUSD : les Chicken Bonds. En cas de succès, le modèle sera étendu à une instance de LQTY. Dans une dernière étape, le modèle généralisé pourrait être rendu prêt à être exploité par n'importe quelle DAO avec la Chicken Bond Factory.

Mardi dernier, [les LUSD Chicken Bonds ont été mis en ligne](https://www.chickenbonds.org/blog-posts/chicken-bonds-is-live), offrant **une nouvelle proposition fusionnant les éléments de DeFi et NFTs fournissant des opportunités de rendement optimisées aux détenteurs de LUSD**. Elle alimentera également la croissance de la liquidité du LUSD sur le pool de la courbe LUSD/3CRV.

Il y a deux protagonistes qui interagissent avec les Chicken Bonds :

1. **Les déposants (utilisateurs)** bénéficient d'une expérience gamifiée offrant **des rendements amplifiés et auto-composés sur les LUSD**.
2. **Le déployeur (protocole)** met en place un **mécanisme permettant la croissance soutenue et la capture de la liquidité sur son token** tout en engageant activement ses détenteurs.[^deployer].

### Alors, que sont exactement les Chicken Bonds ?

En conséquence, les Chicken Bonds remplissent la fonction de différents types de produits selon la perspective. **Pour les utilisateurs, les Chicken Bonds agissent comme un optimiseur de rendement amélioré**. Les bonds leur permettent de maximiser leurs rendements sur les LUSD en optimisant la fréquence de composition et en amplifiant les rendements existants. De leur point de vue, ils pourraient comparer l'utilité des Chicken Bonds à celle déjà fournie par un protocole comme Yearn, sans l'élément NFT. Il maximise et rationalise les activités de production de rendement sur LUSD.

Du point de vue du déployeur (protocole), les Chicken Bonds sont une **solution rentable pour développer la liquidité disponible sur leur token**. Des solutions alternatives pour atteindre un objectif similaire incluraient l'extraction de liquidité, une solution de capture de POL comme Olympus Pro, l'acquisition de jetons de conducteur de liquidité(CRV, BAL, VELO, etc.), ou les bribes des votes des propriétaires de jetons conducteurs de liquidité[^liquidity-driver-tokens].

![chicken-egg](/img/2022/lusd-chicken-bonds/chicken-egg.png)

Si chaque solution existante présente ses propres inconvénients, elles ont toutes un profil similaire : elles **nécessitent des dépenses récurrentes pour accroître et maintenir la liquidité**. Seule l'acquisition de jetons de liquidité peut fournir des incitations continues pour soutenir la liquidité, mais c'est aussi l'approche la plus coûteuse car elle nécessite des investissements importants de la part des projets.

En revanche, les Chicken Bonds n'ont aucun coût car ils exploitent les sources de rendement existantes : **Tout ce qu'il faut pour capturer et accroître la liquidité, c'est du temps**. Ils exploitent une nouvelle forme d'obligations **sans échéance avec protection du capital**, offrant des rendements amplifiés et de fortes protections pour les déposants.

Pour expliquer le modèle des LUSD Chicken Bonds, passons au point de vue du déposant en examinant le cycle de vie d'une obligation et son impact sur le NFT associé.

### L'histoire d'un bond à travers son NFT

<video autoplay loop muted playsinline title="Un 🥚 Œuf NFT, un 🐔 Chicken In NFT et un 🐣 Chicken Out NFT">
  <source src="/img/2022/lusd-chicken-bonds/3chickens-static.mp4" type="video/mp4">
  Your browser does not support video. <a href="/img/2022/lusd-chicken-bonds/3chickens-static.mp4">View GIF</a>
</video>

**Pour créer un bond, un utilisateur dépose des LUSD. En échange, il reçoit un 🥚 Œuf NFT représentant son dépôt**. Le NFT contient la créance sur le LUSD cautionné sous-jacent et peut être vendu ou transféré. A partir de là, l'utilisateur dispose de deux options mutuellement exclusives qui transformeront également son NFT :
- 🐔 Chicken In
- ou 🐣 Chicken Out.

Les NFTs d'œuf ont quatre attributs : une carte, un œuf et un arrière-plan déterminés aléatoirement, ainsi qu'une taille d'œuf adaptée au montant de LUSD déposé.

Lorsqu'un bond est créé, il commence à accumuler progressivement des bLUSD. Au fur et à mesure qu'il arrive à maturité, il devient rentable pour les utilisateurs de le réclamer, en renonçant à leurs LUSD pour obtenir les bLUSD accumulés - C'est l'option " **Chicken In** " et fait évoluer le visuel du NFT en conséquence : l'Œuf se transforme en 🐔 **poulet fier**.

L'utilisateur peut récupérer l'intégralité du montant investi à tout moment du processus. Il renoncera néanmoins aux bLUSD accumulés jusqu'à présent - c'est l'option "**Chicken Out**" et elle conduit également à une évolution du NFT de l'Œuf vers un 🐣 **poulet effrayé**.

<video autoplay loop muted playsinline title="Aperçu des variations possibles">
  <source src="/img/2022/lusd-chicken-bonds/3chickens.mp4" type="video/mp4">
  Your browser does not support video. <a href="/img/2022/lusd-chicken-bonds/3chickens.mp4">View GIF</a>
</video>

#### Approfondir les liens les bonds et le NFT

Pendant le Chicken In, le NFT gagne des attributs supplémentaires obtenus au hasard (peigne, queue, bec et ailes) et des attributs spéciaux en fonction des activités du portefeuille. Les portefeuilles engagés dans les activités suivantes peuvent obtenir des attributs spéciaux ou des chances accrues d'obtenir des attributs plus rares :

1. Posséder un Trove Liquity avec une dette en cours,
2. Posséder LQTY, ou le jalonner soit directement, soit avec Pickle,
3. Voter pour la jauge LUSD/3CRV (détenteurs de veCRV). [^ve-CRV-NFT-attribut-bribe]

La collection NFT exploite également des mécanismes intéressants, comme l'**affinité** pour générer les poulets les plus cool possibles ; lisez l'article dédié sur le blog de Liquity pour plus d'informations sur le sujet :

![egg-variants-overview](/img/2022/lusd-chicken-bonds/egg-variants-overview.png "Aperçu des œufs existants sur x2y2")

Tous les NFTs font partie de la même collection et peuvent être échangés sur les sites habituels, tels que [LooksRare](https://looksrare.org/collections/0xa8384862219188a8f03c144953Cf21fc124029Ee/) ou [X2Y2](https://x2y2.io/collection/lusd-chicken-bonds-nfts/items). Chicken Bonds est une collection de NFT générative autant qu'un protocole DeFi : les deux sont intrinsèquement liés. L'art et le script de génération initial ont été réalisés par l'artiste NFT [Luchador](https://luchadores.io), créateur du jeu éponyme.

{{< notice info >}}
Pour une explication du prix de tous les attributs et modificateurs pris en compte, lisez l'article consacré aux NFT sur le blog de Chicken Bonds :<br>
**[NFT x DeFi: Deep dive into LUSD Chicken Bonds' Dynamic NFT](https://www.chickenbonds.org/blog-posts/nft-x-defi-deep-dive-into-lusd-chicken-bonds-dynamic-nft)**
{{< /notice >}}

### boostedLUSD (bLUSD) : un LUSD auto-composé à rendement amélioré.

En créant un bond et éventuellement Chicken In, les déposants peuvent accumuler des bLUSD, mais vous pouvez vous demander à ce stade pourquoi ce jeton peut être souhaitable : plongeons dans le côté DeFi des Chicken Bonds !

![blusd](/img/2022/lusd-chicken-bonds/blusd.png)

En résumé, **posséder bLUSD donne accès à des rendements auto-composés et amplifiés sur LUSD**. bLUSD est un token ERC-20 standard adossé à LUSD grâce au mécanisme de rédemption, avec un prix plancher croissant grâce à l'amplification du rendement.

![user-flow-overview](/img/2022/lusd-chicken-bonds/user-flow-overview.png)

#### Source de rendement primaire

En tant que protocole, les Chicken Bonds collectent les LUSD et les déploient dans deux sources de rendement potentielles :

1. **Liquity Stability Pool**, où les LUSD peuvent être déposés pour gagner des LQTY ainsi que des primes de liquidation ETH variables.
2. **La pool Curve LUSD/3CRV**, où les LUSD peuvent être fournis contre des USDC/USDT/DAI pour gagner des frais de transaction ainsi que des jetons CRV.

{{< notice info >}}
Si vous n'êtes pas encore familier avec le fonctionnement de Liquity, vous pouvez vous mettre à jour avec cet article dédié : <br>
**[⚖️ Liquity : un service d'emprunt imparable, efficace et innovant](https://tokenbrice.xyz/fr/liquity-protocol/)**.
{{< /notice >}}

#### Composition des rendements automatique

Au lieu de se brancher directement sur les sources de rendement, des solutions middleware sont utilisées pour offrir divers avantages.

1. Les dépôts dans le Liquity Stability Pool sont gérés à l'aide du **[B.Protocol vault](https://bprotocol.org/)**, qui gère la récolte et la composition fréquentes des ETH et LQTY obtenus en LUSD.
2. Pour la pool Curve, le **[vault Yearn](https://yearn.finance/#/vault/0x5fA5B62c8AF877CB37031e0a3B2f34A78e3C56A6)** est utilisé pour optimiser les rendements obtenus en exploitant Convex.

Jusqu'ici, tout va bien : des solutions directes à des problèmes simples. Pourtant, l'amplification du rendement, l'une des plus grandes prouesses des Chicken Bonds, est un peu plus délicate.

#### Amplification du rendement

Pour comprendre comment il peut y parvenir, nous devons commencer à éplucher l'oignon qui est l'outil de comptabilité interne du protocole : les Buckets ("seaux)".

Il y a trois buckets permettant aux Chicken bonds de garantir les trois caractéristiques principales du protocole : l'option de Chicken Out (Pending), l'amplification du rendement (Reserve), et la croissance de la liquidité (Permanent).

![3buckets](/img/2022/lusd-chicken-bonds/3buckets.png "Source de rendement et redistribution entre chaque bucket")

Le **Pending Bucket** a une tâche simple : il doit être en mesure de rembourser intégralement les investisseurs s'ils devaient se dégonfler (Chicken Out). Pour s'assurer que c'est toujours possible, le Pending Bucket exploite une source de rendement sans perte impermanente : le Stability Pool.

Lorsque les utilisateurs Chicken In un bond, les soldes LUSD correspondants sont répartis entre le Reserve Bucket et le Permanent Bucket.

**Le Reserve Bucket soutient le bLUSD**. Avec les rédemptions, les détenteurs de bLUSD peuvent brûler leurs jetons pour obtenir une part proportionnelle des LUSD contenus dans le Réserve Bucket - garantissant un prix plancher pour les bLUSD. Les fonds en réserve produisent également un rendement en exploitant le pool de stabilité.

**Enfin, le Permanent Bucket accroît la liquidité des LUSD**. Grâce à sa fonction de shifting ("déplacement"), qui peut être déclenchée par n'importe qui lorsque le LUSD est au dessus du peg, le Permanent Bucket peut retirer ses liquidités du vault b.protocol pour alimenter le pool Curve LUSD/3CRV à la place. Cela permet de réduire le prix du LUSD et de sécuriser un point d'entrée favorable dans le pool puisque le dépôt la rééquilibre.

Le **rendement produit par les buckets Pending et Permanent est redirigé vers le Reserve Bucket**, ce qui crée l'amplification du rendement et la hausse du prix plancher du bLUSD.

![lusd-cb-user-timeline](/img/2022/lusd-chicken-bonds/lusd-cb-user-timeline-fr.png "Chronologie centrée sur l'utilisateur des Chicken Bonds LUSD")

### Période d'amorçage et prochaines étapes

Les Chicken Bonds LUSD sont en ligne depuis le mardi 4 octobre 2022. Pendant les deux premières semaines du système, jusqu'au 19 octobre, il est toujours dans la **période d'amorçage** : Les Chicken Ins ne sont pas possibles, ce qui signifie que l'offre de bLUSD est toujours égale à 0. Cela signifie que tous les LUSD sont dans le Pending Bucket, sauf le rendement déjà produit qui est redirigé vers le Reserve Bucket.

Une fois la période d'amorçage terminée, l'option Chicken In sera disponible, permettant aux déposants de commencer à accéder aux bLUSD. Pour faciliter l'entrée et la sortie du bLUSD, une **pool bLUSD pool sera incitée sur Curve Finance, en utilisant une commission de 3% payée lors du Chicken In**. Cela permettra à la liquidité de se développer progressivement à mesure que le premier lot de bonds atteindra son seuil de rentabilité (~19 octobre) et le moment optimal de rebond (~4 novembre).

La section suivante discute de la structure de liquidité choisie et de son impact.

## Impact des Chicken Bonds sur le prix et la liquidité du LUSD

Si vous m'avez lu jusqu'à ce point, vous êtes maintenant au courant de la prime de prix du LUSD et du modèle introduit par les Chicken Bonds. Relions donc les points et examinons comment les Chicken Bonds du LUSD **contribueront à la liquidité globale du LUSD et aideront à contenir sa prime**.

Les Chicken Bonds ont deux impacts sur la liquidité du LUSD :

1. Avec la croissance du Permanent Bucket, la liquidité fournie au LUSD/3CRV augmentera tant que le prix du LUSD aura une prime.
2. La structure de la pool de liquidité a été choisie pour bLUSD afin d'aider à accroître davantage la liquidité sur le LUSD/3CRV.

{{< notice note >}}
Dans un court laps de temps, la libération des LUSD Chicken Bonds a entraîné une augmentation de la demande de LUSD et une hausse de son prix. Cependant, les LUSD déposés dans les Chicken Bonds s'avèrent bénéfiques pour la liquidité du LUSD à long terme, comme nous le soulignons dans cette section.
{{< /notice >}}

### Un moteur pour capturer la liquidité progressivement

Au fur et à mesure que les dépôts dans les Chicken Bonds du LUSD s'accumulent, l'impact potentiel sur le peg du LUSD augmente. En effet, lorsqu'un utilisateur fait un Chicken In, les LUSD sous-jacents sont répartis entre la Réserve et le Permanent Bucket.

Par défaut, les trois buckets produisent du rendement en déployant les LUSD dans le vault de b.protocol. Cependant, le Permanent Bucket dispose également d'une **fonction de déplacement** qui peut être déclenchée par n'importe qui tant que les LUSD s'échangent à un prix élevé. Elle déplace les LUSD du Permanent Bucket pour **fournir de la liquidité sur la Curve** (fourniture d'un seul actif), contribuant ainsi à rééquilibrer progressivement le pool tout en augmentant sa liquidité.

La part du montant total des LUSD déposés dans les Chicken Bonds allouée au Permanent Bucket est difficile à prévoir, car elle dépend du comportement des utilisateurs. Voici quelques calculs rapides en utilisant une estimation prudente de 10% des actifs totaux dans le Permanent Bucket, avec les 5M LUSD actuellement disponibles dans le LUSD/3CRV pour estimer l'impact des Chicken Bonds :

Chicken Bonds TVL|Liquidité directement ajoutée|Liquidité ajoutée (%)
:--|:--|:--
7M (actuel)|700K LUSD|14.00%
10M|1M LUSD|20.00%
20M|2M LUSD|40.00%
50M|5M LUSD|100.00%

Le pourcentage de liquidité ajoutée pourrait être un bon indicateur approximatif de l'ampleur de la réduction de la prime de prix. Gardez à l'esprit qu'il reste approximatif, car il ne prend en compte que la pool principale LUSD/3CRV.

Néanmoins, avec 10 millions de dollars de TVL dans les Chicken Bonds à la fin du premier cycle, l'impact pourrait déjà être palpable avec une augmentation de \~20% du montant LUSD disponible dans le pool Curve.

{{< notice note >}}
La fonction de shifting est désactivée pendant les 45 premiers jours du système, c'est à dire jusqu'au 19 Novembre. Passé cette date, n'importe qui pourra déplacer la liquidité du Permanent Bucket de Curve <-> B.Protocol si **[les conditions](https://liquity.gitbook.io/chicken-bonds/faq/lusd-peg-stability#_vowf7444yzdt)** sont remplies.
{{< /notice >}}

### Augmentation de la liquidité du bLUSD main dans la main avec le LUSD

Il existe un autre effet bénéfique indirect des Chicken Bonds, découlant de la structure choisie pour la liquidité bLUSD, encouragée par le protocole.

En effet, un **3% de frais de Chicken In est collecté et redirigé pour inciter les fournisseurs de liquidité de la pool bLUSD/LUSD-3CRV**. Cette pool est une méta pool composé de bLUSD appariés avec le jeton LP du LUSD/3CRV existant. A l'équilibre parfait, l'exposition des actifs serait : 50% bLUSD / 25% LUSD + 25% 3pool (8,33% USDC / 8,33% USDT / 8,33% DAI).[^blusd-lusd3pool]

Cette structure de liquidité garantit que **50% des dépôts effectués dans le pool LP bLUSD contribuent directement à accroître la liquidité du principal LUSD/3CRV**. En outre, parce que ce pool a son propre budget d'incitation (frais Chicken In), il fournira un rendement LUSD attractif aux stakers en plus du rendement de base généré par les swaps.

Au fur et à mesure que les Chicken Bonds arrivent à maturité, la pool bLUSD/LUSD-3CRV pourrait obtenir sa propre jauge, garantissant des récompenses CRV (et potentiellement CVX) supplémentaires en plus de celles existantes.

Ce modèle a été préféré à une pool bLUSD/LUSD qui aurait nécessité une quantité importante de LUSD sans contribuer à la liquidité du LUSD par rapport aux autres monnaies stables. Le principal inconvénient du modèle choisi est qu'il rend les interactions de dépôt et de retrait plus complexes pour les fournisseurs de liquidités. Cependant, cette préoccupation sera levée avec **zaps permettant l'approvisionnement et le retrait de LUSD et bLUSD directement**.

En fonction de l'équilibre du pool bLUSD/LUSD-3CRV, son approvisionnement unilatéral en LUSD ou bLUSD peut entraîner une prime :
- S'il y a trop de LUSD-3CRV dans le pool, fournir du bLUSD rééquilibre le pool et entraîne une prime.
- S'il y a trop de bLUSD dans le pool, l'apport de LUSD entraînera une **double prime** car les pools bLUSD/LUSD-3CRV et LUSD/3CRV sont rééquilibrées dans le processus.

Pour en savoir plus sur le bLUSD/LUSD-3CRV, consultez l'article dédié sur le blog Chicken Bonds [**Game of Chickens!** The end of the bootstrap period and what it means for bLUSD](https://www.chickenbonds.org/blog-posts/game-of-chickens-the-end-of-the-bootstrap-period-and-what-it-means-for-blusd).

## Solutions supplémentaires pour accroître la liquidité du LUSD

Les Chicken Bonds sont les principales initiatives en cours visant à accroître la liquidité du LUSD, mais d'autres projets et solutions sont également à l'étude. En voici un aperçu.


### Position des veCRV et bribes (pots-de-vin)

La trésorerie de Liquity est entrée dans la guerre du CRV il y a plusieurs mois, en acquérant et en verrouillant des jetons CRV pour soutenir la jauge bLUSD/LUSD-3CRV. Pour maximiser l'impact des LUSD Chicken Bonds, **une campagne de bribes** est également synchronisée avec la sortie pour augmenter l'APY CRV des déposants de la pool LUSD/3CRV.

En utilisant Warden Quest, des jetons LQTY sont attribués aux votants veCRV et vlCVX sur la jauge LUSD/3CRV. La campagne de bribe a permis d'obtenir **5M de votes veCRV (\~1% du total des votes)**, ce qui a conduit à une forte augmentation de l'APY, l'amenant à la parité avec un dépôt de base dans la Stability Pool.


{{< notice info >}}
À la trâine par rapport aux CRV Wars ? Rattrappez votre retard avec cet article : <br>
**[⚔ CRV wars : la course pour accumuler la capacité d'influencer le protocole Curve Finance](https://tokenbrice.xyz/fr/crv-wars/)**.
{{< /notice >}}

### Le LUCY de PowerPool : Stability Pool et apport de liquidité

L'équipe de PowerPool a travaillé sur un **nouveau type de pool Balancer** adaptée aux LUSD, et il est maintenant sur le point d'être publié : la pool LUSD-a-bb-USD, également connu sous le doux nom de **LUCY**.

Comme les Chicken Bonds, ce pool **exploite le b.protocol pour offrir une opportunité de gain auto-composé sur le LUSD**. En effet, la principale innovation de cette pool est d'impliquer des actifs porteurs d'intérêts et de constamment **rééquilibrer entre les activités de rendement et de fourniture de liquidités**. Le pool est composé de deux jetons wrappers :

#### 1/ Balancer Boosted Aave USD

Cette pool est essentiellement l'équivalent **de Balancer au 3pool de Curve**, la pool principale de stablecoin de l'échange décentralisé. La principale différence ici est que la pool implique des **wrapper productif** de chaque stablecoin. En fonction des besoins en liquidité de la pool, chaque stablecoin est rééquilibré entre l'apport de liquidité et le rendement grâce à Aave :

![bbaUSD-pool-composition](/img/2022/lusd-chicken-bonds/bbaUSD-pool-composition.png)

#### 2/ LUSD + b.protocol

Les jetons bb-a-USD sont appariés au LUSD, qui **rééquilibre également entre le rendement (Stability Pool avec b.protocol) et l'apport de liquidité** en fonction des besoins.

Ainsi, la pool LUCY devrait être intéressante pour accroître la liquidité disponible de LUSD, car elle pourrait fournir une option de cumul de rendements pour les fournisseurs de liquidité, gagnant :

1. Les **frais de swap**, perçus sur les échanges impliquant les jetons de la pool.
2. Le **rendement de base** de chaque jeton du pool (rendement d'Aave pour USDC/USDT/DAI, rendement de la Stability Pool pour LUSD).
3. [Si une jauge BAL est obtenue] le **un rendement additionnel en BAL**, qui peut être encore augmenté avec des votes de jauge et des campagnes de bribes.


Cette nouvelle pool marquera l'arrivée du LUSD sur Balancer, diversifiant davantage ses sources de liquidité, puisque les principaux lieux d'échange du LUSD sont actuellement Curve, Uniswap et Velodrome sur Optimism.

### Intégration du LUSD dans d'autres protocoles de prêt

Au cours des derniers mois, le LUSD a été de plus en plus intégré à divers protocoles DeFi, offrant **des options supplémentaires aux détenteurs de LUSD et aux arbitragistes**.

L'[ajout du LUSD comme actif empruntable sur Aave](https://app.aave.com/reserve-overview/?underlyingAsset=0x5f98805a4e8be255a32880fdec7f6728c6568ba0&marketName=proto_mainnet) a marqué la première fois que le stablecoin pouvait être emprunté en utilisant une garantie autre que l'ETH pour sécuriser la position. Au fur et à mesure que la liquidité disponible sur le marché augmente, elle ouvre l'arbitrage du LUSD aux détenteurs de non-ETH.

![lusd-aave-market](/img/2022/lusd-chicken-bonds/lusd-aave-market.png)

Pendant ce temps, **LUSD a également été ajouté comme garantie sur deux protocoles de prêt basés sur €** : [Angle Money](https://angle.money/) et [Mimo](https://mimo.capital/). Ces deux protocoles permettent aux détenteurs de LUSD de prendre une position courte sur l'euro, en utilisant leurs LUSD comme collatéral.

Enfin, [GearBox](https://gearbox.fi/) s'apprête à sortir sa V2 sous peu, permettant aux utilisateurs d'obtenir un effet de levier selon un ensemble de règles prédéterminées et appliquées par des smart contracts. Parmi les options disponibles lors de la sortie de la V2, **les fournisseurs de liquidités du LUSD/3CRV seront en mesure de bénéficier d'un effet de levier sur leur position**.

L'expansion du marché des prêts de LUSD au-delà de Liquity augmente l'utilité du stablecoin tout en permettant à davantage de types d'utilisateurs différents d'arbitrer les fluctuations de son prix. Associé aux efforts en cours pour accroître la liquidité du LUSD sur le DEX, cela contribuera à stabiliser son prix.

### LUSD sur Optimism : Velodrome et Stargate

LUSD a également **une forte présence sur Optimism**, grâce à Liquity qui est l'un des protocoles impliqués dans la course du DEX Velodrome. Avec une position respectable sur Velodrome, Liquity a été capable de faire croître plusieurs pools liés au LUSD jusqu'à des TVL importantes. De plus, les pools sur Velodrome ont tendance à être plus équilibrés que celles du réseau principal :

![lusd-velodrome](/img/2022/lusd-chicken-bonds/lusd-velodrome.png)

Cependant, faire le pont entre LUSD et Optimisme est actuellement un peu un voyage à sens unique. Le bridge entre LUSD et Optimism est facile et ne prend que 5-10 minutes en utilisant le bridge officiel. Cependant, le retour sur le réseau principal prend 7 jours avec le bridge officiel, et aucune option alternative avec une liquidité décente n'est encore disponible.

La situation est sur le point de changer, permettant à la forte liquidité de LUSD sur Optimism d'avoir un impact positif sur la situation du mainnet : Stargate, le protocole de transport de liquidité omnichain, a récemment voté pour **ajouter le support de LUSD** ([SIP#16](https://snapshot.org/#/stgdao.eth/proposal/0xe6fef4aa9c8e9d162f694ab764b11c06918b9f199aafe43e0d85b12d8271011c)), ce qui permettra un bridging rapide de et vers Optimism une fois implémenté. Si Stargate peut fournir une solution fiable pour le bridge rapide des LUSD d'Optimism vers le mainnet, cela pourrait avoir un impact positif sur l'équilibre des pools de liquidité LUSD du mainnet.

## En savoir plus sur les Chicken Bonds

J'espère que cet article a piqué votre curiosité sur les Chicken Bonds et la LUSD. Si c'est le cas, de nombreuses ressources sont disponibles pour vous permettre d'explorer davantage le modèle ; voici quelques recommandations :

1. Le [site Web des Chicken Bonds](https://www.chickenbonds.org/) est un excellent point de départ - vous y trouverez [la liste des front ends](https://www.chickenbonds.org/lusd-bonds#front-ends) que vous pouvez utiliser pour interagir avec les Chicken Bonds de LUSD.
2. Pour aller plus loin, n'hésitez pas à [consulter le blog](https://www.chickenbonds.org/blog) disponible sur le site Web : il contient plusieurs articles qui approfondissent les dimensions critiques des Chicken Bonds.
3. Enfin, la ressource la plus complète sur les Chicken Bonds est [la documentation utilisateur](https://liquity.gitbook.io/chicken-bonds/faq/table-of-content), alors n'hésitez pas à la consulter si certaines de vos questions restent sans réponse.

{{< notice note >}}
Pour approfondir avec un format vidéo plus interactif, n'hésitez pas à rattraper le meetup DeFi France consacré aux Chicken Bonds, disponible en replay : <br>
**[🎥 DFF Toulouse #1 - Les Chicken Bonds nouvelle brique DeFi/NFT avec TokenBrice](https://www.youtube.com/watch?v=TXtXpfyHbVU)**
{{< /notice >}}

Pour suivre ce qui se passe avec les Chicken Bonds, vous trouverez des statistiques dans l'interface utilisateur du front-end que vous utilisez. Par ailleurs, un membre de la communauté a créé un outil d'analyse [Chicken Bonds Dune Analytics](https://dune.com/nemoventures/chicken-bonds) qui vous sera utile. Pour de plus amples discussions, vous pouvez [rejoindre le Discord Liquity](https://discord.gg/WQMEcgHBpc), où une toute nouvelle section est consacrée aux Chicken Bonds.

[^deployer]: Pour l'instant, Liquity est le seul "déployeur". Ce concept gagnera en pertinence avec la version généralisée des Chicken Bonds, où d'autres protocoles peuvent exploiter le modèle au profit de leurs jetons.
[^liquidity-driver-tokens]: Les jetons conducteur de liquidité permettent des incitations directes à des paires de liquidité ou de prêt sélectionnés, généralement par le biais d'un système de verrouillage. Ils permettent aux projets qui les verrouillent de diriger des incitations vers les pools de leur choix pour attirer des apporteurs de liquidité.
[^ve-CRV-NFT-attribut-bribe]: Pour autant que je sache, c'est la première fois que ce type d'influence a été tenté sur les électeurs de Curve (ou tout autre détenteur de jetons DeFi) : Les bribes basés sur les attributs NFT ; nous voilà !
[^blusd-lusd3pool]: La pool est [déjà en ligne](https://curve.fi/factory-crypto/134) mais ne peut être alimentée avant la fin de la période d'amorçage.

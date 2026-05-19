---
title: "⚔ Guerre du CRV avancée : analyse des protocoles construits sur Curve et Convex "
description: "Tour d horizon de Votium, Warden, Concentrator, Conic et des nouvelles dynamiques autour des tokens CRV et CVX."
date: '2022-04-05T01:13:50.191Z'
reviewed: 2026-05-19
categories: [DEX]
tags: [DeFi, Ethereum, Curve, Convex, Votium, veCRV, bribe.crv, Conic Finance, Warden, Concentrator]
series: crv-wars
series_order: 2
toc: true
tocNum: false
url: crv-wars-l2
image: /img/2022/curve-wars-l2/curve-wars-l2-cover-tokenbrice.png
difficulty: "expert"
---

Le jeu et la lutte autour des tokens CRV et CVX ont changé d’ampleur depuis mon dernier article qui décrivait les Curve Wars des origines, désormais presque primitives. L’infrastructure autour de Curve s’est grandement densifiée avec l’arrivée de Convex bien sûr, mais aussi Votium, l’Union Llama Airforce, Concentrator, CCRV, Lendflare, Warden, et de nombreux autres protocoles encore en développement.

Pour assumer une position stratégique sur CRV ou CVX, il faut désormais pouvoir supporter un investissement de plusieurs dizaines de millions de dollars. Ainsi, la course à l’accumulation de CVX et CRV est devenue avant tout un jeu pour DAOs ou pour les whales. Plus spécifiquement, les DAOs semblent préférer CVX au CRV, qui représente un compromis plus favorable :

1. **Boosts LP Curve** : capacité de développer sa liquidité via les votes sur les jauges Curve
2. **Rendements** : 4-5% en cvxCRV + potentiel rendement des bribes si capacité non utilisée (ou que le protocole bribe également)
3. **Flexibilité** : CVX peut être utilisé au maximum de ses capacités en s’engageant 16 semaines + 3 jours (vlCVX) tandis que CRV requiert jusqu'à 4 ans d’engagement (1 CRV = veCRV).

Ainsi pour extraire l’utilité du CRV, CVX est une alternative crédible et plus flexible, c’est pourquoi la plupart des DAOs se concentrent sur ce token. Convex Finance est devenu un “L2 fonctionnel” de Curve : une seconde couche qui apporte des nouvelles fonctionnalités et un jeu de compromis différent.

Malgré tout, Convex n’est pas le seul projet qui a essayé de réaliser cette vision : il y avait aussi Yearn qui a désormais capitulé : les vaults Curve de Yearn passent essentiellement par Convex, désormais plus rentable. Depuis, de très nombreux projets tentent de proposer une brique synergétique avec le mastodonte Curve/Convex.


## CRV ou CVX ?

Je ne reviendrai pas sur les bases de la séparation entre les deux tokens ici, c’est l’affaire d’un article entier si vous découvrez le sujet : [⚔ Guerre du CRV : comprendre la course à l'accumulation de la capacité à influencer le protocole Curve Finance](2. [⚔ Guerres CRV avancées : analyse des protocoles construits au dessus de Curve et Convex](https://tokenbrice.xyz/fr/crv-wars-l2/)

Il ne faut pas oublier que malgré l’équivalence calculable entre CVX et CRV (1vl CVX contrôle environ 4.8 veCRV - [source](https://dune.xyz/Marcov/Convex-Finance)), les deux tokens ont des compromis différents comme décrit plus haut.

L’équilibre entre CRV et CVX a tendance à se maintenir, malgré des oscillations fréquentes : dernièrement, le pendule semble plus aller du côté de CVX. Néanmoins je pense qu’il reste de la place pour d’autres approches qui partent de la source (CRV) et elles commencent à émerger.

[Warden](https://app.warden.vote/) de Paladin propose ainsi un protocole qui aide les apporteurs de liquidité sur Curve à maximiser leurs rendements et peut être atteindre le désirable bonus 2.5x grâce à de l’emprunt de la capacité de boosts des tokens veCRV (apportés par d’autres) payés directement en CRV.

Mais il y a tellement d’autres subtilités et interactions à avoir en tête pour comprendre la pertinence des stratégies déployées par les différents projets, DAOs et protocoles pour gagner les Curve Wars.

C’est pourquoi cet article se propose de faire le point sur la guerre des CRV et CVX **en visualisant et détaillant l’ensemble de l'écosystème** qui s’est développé autour de ces deux protocoles.


## Layer 2 fonctionnels de Curve

{{< notice note >}}
Dans cet article, je vais parler de “L2 fonctionnel”, ou tout simplement L2 de Curve ou Convex. C’est une image pour décrire cette tendance à la démultiplication des supports pour interagir avec Curve/Convex.

Prenez garde à ne pas confondre le terme avec les “vrais L2” / L2 de scaling : le terme dans son sens originel pour décrire une nouvelle chaîne qui hérite de la sécurité de sa parente tout en permettant un débit de transactions plus important et des coûts plus modérés.
{{< /notice >}}

On commence donc par les **L2 “fonctionnels”** de Curve, puis ceux de Convex (lui-même L2 de Curve), ensuite les services d’emprunt permettant de saisir avec effet de levier les nombreuses sources de rendement offertes par l’ensemble de l'écosystème Curve et on finira avec les protocoles-whales de CRV/CVX.

C’est une aventure dense et haute en couleurs, mais comme souvent avec mes articles, je vous propose ici un condensé de mes recherches sur le sujet : bonne lecture !

Pour ne pas vous perdre en route, je vous propose cette carte qui résume les principaux acteurs de l’écosystème Curve/Convex :

![Curve/Convex L2 map](/img/2022/curve-wars-l2/curve-convex-l2-map-fr.png "Résumé des principaux protocoles L2 fonctionnels Curve/Convex")

### Convex Finance : Curve à la découpe

Convex est le premier L2 fonctionnel de Curve ; d’autres projets lui ont précédé (yveCRV et sdveCRV) mais ils n’étaient pas aussi synergétique avec Curve et n’ont donc connu qu’un succès marginal.

En résumé, Convex donne accès aux rendements du token CRV maximisés et liquides grâce à cvxCRV. La capacité de gouvernance ainsi que celle pour voter sur les jauges Curve correspondantes aux tokens veCRV sous-jacent est redirigée vers les possesseurs de vlCVX. Convex permettant ainsi un accès facilité à l'écosystème Curve (pour les possesseurs de CRV).

Bien que Convex contrôle une grande quantité de veCRV, la centralisation du pouvoir de vote sur les jauges est évitée en offrant cette capacité au plus offrant grâce à Votium (bribes).

Convex, c’est désormais basique, je ne le détaille donc pas plus ici. Mon précédent article sur la guerre du CRV approfondi sur le modèle et les apports de Convex : [⚔ Guerre du CRV : comprendre la course à l'accumulation de la capacité à influencer le protocole Curve Finance](https://tokenbrice.xyz/fr/crv-wars/)


### Warden de Paladin : Curve sous stéroides ?

[Warden](https://app.warden.vote/) est un autre chemin envisageable pour les LP Curve, qui propose un jeu de compromis différent à Convex. Warden ne contrôle pas directement de veCRV, mais propose à la place de louer la capacité de boost des LP Curve de veCRV possédés par d’autres.

La location se paie directement en CRV et à la semaine. Elle provient de possesseurs de veCRV qui la mettent à disposition, pour le prix et la durée de leur choix. L’affaire se conclut grâce à la délégation des veCRV correspondant.

![Location de boost LP Ve sur Warden](/img/2022/curve-wars-l2/warden-veboost.png "Location de boost LP Ve sur Warden")

Warden revient ainsi sur le jeu des boosts de LP Curve. Sur Convex, la plupart des pools sont boostées entre 1.5 et 1.7x via Convex. Avoir son propre stock de veCRV, augmenté par un emprunt Warden permet d’envisager d’atteindre 2x voir les 2.5x maximum sur certaines pools.

Depuis peu, Warden propose même un calculateur bien pratique pour visualiser la quantité de veCRV nécessaire pour atteindre un multiplicateur donné :

<video autoplay loop muted playsinline title="Un calculateur pour estimer l'impact d'une location de boost ve avec Warden">
  <source src="/img/2022/curve-wars-l2/warden-calc.mp4" type="video/mp4">
  Your browser does not support video. <a href="/img/2022/curve-wars-l2/warden-calc.mp4">View GIF</a>
</video>


Warden est donc une alternative crédible pour les protocoles, DAOs et gros porteurs qui voudraient optimiser leur LP Curve dans une perspective de maximisation des CRV obtenus.


## L2 Convex

Convex n’a pas encore un an (Mai 2021) mais face à la place prépondérante que le service occupe déjà, les abstractions construites dessus n’ont pas tardé à arriver.


### Votium : mise aux enchères des votes de Convex

Le protocole Convex concentre la plus grande quantité de veCRV possédée par une entité unique. Néanmoins, la capacité de vote correspondant aux veCRV possédés par Convex (obtenue grâce au cvxCRV) est distribuée entre tous les possesseurs du token CVX qui le “vote lock” (vlCVX) pour 16 semaines + 7 jours).

Via snapshot, ils peuvent mobiliser leur puissance de vote directement sur la jauge des pools Curve de leur choix. [Votium](https://votium.app/) est une couche supplémentaire construite sur ce dispositif : Votium permet à n’importe quel projet d’allouer un budget pour supporter une jauge curve donnée. À la fin du round, les possesseurs de vlCVX qui ont voté sur cette jauge se partagent les récompenses, à la hauteur de leur puissance de vote : ce sont les fameuses bribes.

![Votium bribes](/img/2022/curve-wars-l2/votium-bribes.png "Plus de $15M de bribes sont payées chaque deux semaine pour influencer le jeu des jauges Curve.")

Grâce à la quantité impressionnante de veCRV contrôlés par Convex, Votium a rapidement émergé comme **un outil essentiel pour établir et pérenniser une présence sur Curve** : un bribe conséquent sur Votium permet de rendre rapidement une pool Curve très attractive.

On détaille plus bas l’exemple de Frax Finance qui propose environ $5-7M de bribes à chaque round ; cela permet de maintenir des rendements attractifs sur la pool Frax/3CRV conséquente malgré la dilution massive (la pool contient presque $3B d’actifs), et ce sans émettre de leur propre token (FXS) pour du liquidity mining.


### Union Llama Airforce : gestion mutualisée des vlCVX

Les bribes proposées sur Votium sont très alléchantes : cela permet à vlCVX d’atteindre un rendement **d’environ 40% APR - dont l’essentiel (90%) provient des bribes**. Cependant, gérer soi-même sa position vlCVX a plusieurs contraintes :

1. **Les frais en gas**, pour verrouiller ses CVX, mais aussi pour récolter les bribes.
2. Bien qu’il soit possible de déléguer, cela entraîne une dispersion des récompenses (payées dans une dizaine de token différents -> frais en gas). Ainsi les petits et moyens porteurs de vlCVX préfèrent généralement concentrer leur vote sur un projet donné : plus pratique, mais ça implique de ne pas oublier de **voter à chaque round** !

L’Union de Llama Airforce propose ainsi de remédier à ces deux principales limites, pour le bonheur des petits porteurs ainsi que de ceux qui préfèrent une **gestion 100% passive de leur vlCVX**.

Le concept est simple : l’Union mutualise la gestion des vlCVX. La seule action requise de la part des utilisateurs, c’est la délégation de sa puissance de vote vlCVX vers le contrat de l’Union. Par la suite, l’Union se charge de tout :



* À chaque round, l’Union se charge de claim toutes les bribes obtenues, et les vend pour des cvxCRV (=mutualisation / réduction immense de l’impact des frais de transaction).
* Les cvxCRV obtenus sont ensuite déposés dans le Pounder (uCRV), qui les stake avec Convex et compose le rendement automatiquement.

L’Union offre ainsi une alternative pertinente pour les possesseurs de CVX qui comptent maintenir et composer leur position sur le long-terme. Comme toujours, n’oubliez pas de faire attention aux frais malgré tout :



* Les frais en gas sont répercutés et distribués sur tous les utilisateurs de l’Union.
* Un frais correspondant à 2% du total des bribes reçues est également prélevé à chaque round.

![Llama Air Force Union](/img/2022/curve-wars-l2/llama-airforce-union.png "Évolution de la TVL de la Union ⚠️")

{{< notice warning >}}
Cette TVL ne prend en compte que les rendements des bribes composés en cvxCRV par l'Union (uCRV). Les vlCVX ne sont pas pris en compte puisqu'ils sont simplement délégués à l'Union (environ 2.5M CVX).
{{< /notice >}}


L’Union a connu un succès rapide. Le projet provient de la [Llama Airforce](https://llama.airforce/#/convex/flyer), une source d’information déjà bien connue au sein de l'écosystème Curve/Convex, ce qui a sans doute contribué à son adoption.


### Concentrator (AladdinDAO)

En résumé, le [Concentrator](https://concentrator.aladdin.club/) c’est un peu le même esprit que l'Union, mais cette fois-ci pour les apporteurs de liquidité. Ainsi le Concentrator se propose de gérer des LP Curve pour ses déposants : les récompenses (CRV, CVX et potentiels autres tokens) sont automatiquement vendues pour du cvxCRV et composées automatiquement (staking sur Convex) via le wrapper aCRV.

La proposition est intéressante et plutôt synergétique avec Curve et Convex : c’est un peu dommage de voir que les CVX sont vendus pour l’instant, mais expliqué par l'absence de wrapper disponible pour vlCVX. Le service proposé par Concentrator est donc plutôt pertinent pour les **petits et moyens porteurs qui veulent utiliser leur LP Curve pour maximiser leur exposition au token CRV** de manière efficace.


### Congruent CCRV : Optimisation de la flywheel Curve/Convex


Une des limites actuelles de Convex (ou feature pour certains) c’est que malgré la liquidité assez dense dans la pool Curve cvxCRV/CRV, celle-ci est souvent déséquilibrée. CvxCRV est liquide contre CRV, mais rarement à 1:1.

[CCRV](https://ccrv.finance/) est donc conçu comme un mécanisme pour aider à rééquilibrer cette pool, en utilisant à la fois Curve et Convex. Le principe est assez simple si vous avez compris les mécanismes de Curve et Convex :

![CCRV.finance](/img/2022/curve-wars-l2/ccrv.png)

1. Création du token cCRV, backé par 1 cvxCRV. Le protocole stake tous les cvxCRV déposés pour backer des cCRV dans Convex, afin d’obtenir un rendement.
2. Création de la pool Curve 3CRV : CRV, cvxCRV et cCRV
3. Bribes sur la pool 3CRV pour l’aider à se développer.

Le mécanisme se lancera grâce à une allocation initiale de 1M CRV (fournie par Congruent DAO). Cela permettra d’airdrop 1M cCRV (via bribes) sur les premières semaines d’existence du token afin de l’aider à se lancer rapidement.

Si le plan de lancement semble assez solide, la pérennisation du mécanisme semble encore incertaine. L’ajout de frais pourrait permettre au protocole CCRV de posséder sa propre liquidité (et donc rendement en CRV, CVX et 3 pool) ce qui pourrait alimenter les bribes tout en réduisant leur coût effectif sur le long terme.

cCRV n’est pas encore lancé mais se veut être une **nouvelle optimisation de la flywheel Curve/Convex**. Point intéressant, cCRV est développé par [Congruent](https://congruent.fi/), une DAO qui développe des produits de “Governance as a Service” (GaaS).


### Bent : le Convex de Convex ?

[Bent](https://app.bentfinance.com/) est un véritable L2 Convex / L3 de Curve. La question principale qui se pose avec ce projet c’est surtout de savoir s’il y a quelque chose à gagner à descendre à ce niveau de profondeur.

Concrètement, Bent fonctionne comme Convex fonctionne pour Curve : Bent permet de staker les tokens LP Curve : ils sont ensuite stakés dans Convex (par Bent), et vous bénéficiez d’un rendement supplémentaire payé avec leur token natif - BENT, en échange de frais collectés par Bent :

![Bentfinance-fees](/img/2022/curve-wars-l2/bentfinance-fees.png "Structure des frais sur Bent, très similaire à Convex")


Vous le remarquerez sans doute, la structure des frais est quasiment identique à celle de Convex. Enfin, tout comme Convex a créé sa propre représentation de CRV (cvxCRV), Bent crée sa représentation du CVX, le bentCVX. Celui-ci peut également être verrouillé (weBENT) exactement comme CVX->vlCVX, pendant 8 semaines pour obtenir un rendement supplémentaire correspondant aux bribes.

Chaque deux semaines (round de jauges Curve), les possesseurs de weBENT votent sur Snapshot pour allouer leur capacité de vote sur les jauges de leur choix. Les votes des weBENT holders se répercutent via les CVX possédés par BentFinance, eux-même répercutés en vote CRV par Convex : deux niveaux de profondeur !

![bentCVX-lock.png](/img/2022/curve-wars-l2/bentCVX-lock.png "Vérouiller des BENT donne accès aux bribes collectés sur les tokens sous-jacents (vlCVX).")


#### Une abstraction pertinente ?

Comme je le disais en abordant le sujet de Bent, la question ici n’est pas de savoir si le modèle est pertinent puisque Convex en est la preuve vivante. Néanmoins, Convex n’est pas un jeu à somme nulle par rapport à Curve, puisque le protocole a apporté de nouvelles fonctionnalités qui n’existaient pas avec juste Curve :

1. Farm avec LP Curve optimisé, sans posséder de veCRV
2. “Locking liquide” (⚠️taux de change cvxCRV &lt;-> CRV) pour CRV
3. Et le troisième point qui est un peu la conséquence des deux autres : Convex est désormais le plus gros possesseurs de veCRV, et peut donc proposer le service de bribes (via Votium) avec le plus de potentiel tout en étant le plus pratique (délégation, pas besoin de claim chaque semaine, etc.)

Si je détaille les apports de Convex, c’est évidemment pour poser la question : qu’apporte **fonctionnellement** Bent par rapport à Convex ?

1. Option de farm avec LP Curve sans posséder de veCRV encore plus optimisée que Convex, mais toute la sur-performance vient de l’émission BENT.
2. Un locking de CVX moins contraignant que le locking direct via vlCVX (8 semaines chez Bent, 16 semaine + 7j chez Convex)

Il manque encore pour moi le troisième élément pour faire de Bent une option intéressante, un mécanisme qui créerait une vraie valeur ajoutée par rapport à Curve/Convex, outre l’optimisation du farm et une réduction des contraintes.

Enfin, je serai malhonnête si je n’ajoute pas un dernier point : la sécurité et la pérennité du protocole. En effet, Bent Finance a subi une attaque à priori par un insider en Décembre 2021 pendant plusieurs semaines. L’attaque a été rendue possible par le fait qu’à cette époque, les contrats de Bent n’étaient pas sécurisés par un multisig : [plus d’informations par ici](https://halborn.com/explained-the-bent-finance-hack-december-2021/).


### Conic Finance (CNC) 🚧 : gestion collective de liquidité sur Curve/Convex

{{< notice tip >}}
🚧 signale un protocole pas encore lancé
{{< /notice >}}

Similaire à Bent, [Conic](https://twitter.com/ConicFinance) propose une abstraction supplémentaire à partir de LP Curve stakés sur Convex. Cependant je pense que cette fois-ci, le modèle a de la pertinence.

Conic introduit le concept des “omnipools”, qui simplifierait la gestion pour les LP Curve en redescendant au niveau primitif : ici, ce sont directement les tokens qui sont déposés (ex: USDC ou DAI). Les omnipools de Conic se chargeront ensuite de distribuer les tokens sur différentes positions LP Curve stakés ensuite sur Convex.

Les déposants reçoivent ainsi leur token CRV, CVX ainsi que des CNC, le token de Conic. De manière similaire à CVX, le CNC peut être “vote locked” pour :



1. Participer aux votes de jauges toutes les deux semaines qui déterminent la distribution des pools Curve par actifs acceptés sur Conic.
2. Voter sur la whitelist et blacklist des pools Curve acceptés (et donc éligible pour les jauges)
3. Participer au vote pour décider les actifs supportés sur Conic
4. Et tout autre décision de gouvernance, dont l’activation potentielle de frais pour le service (initialement, il n'y en aura aucun).

L’approche de Conic semble donc pertinente et pourrait être décrite comme une gestion mutualisée d’actifs. C’est un modèle qui rappelle celui de [Tokemak](https://tokemak.xyz/) et va un pas plus loin que Curve/Convex qui reste au niveau de la détermination des incantations par la gouvernance. Ici, les votes de gouvernance résulteront en des mouvements de fonds effectifs entre différentes pools Curve. Si le protocole parvient à attirer une liquidité suffisante, il pourra devenir un acteur important des Curve Wars, avec potentiellement son propre système de bribes à terme.

![conic-finance-fr](/img/2022/curve-wars-l2/conic-finance-fr.png "Fonctionnement de Conic Finance, une solution collective de gestion de liquidité sur Curve")


Le projet vient d’être dévoilé et l’approche envisagée pour le lancement est également intéressante. Une partie du supply de CNC est airdrop aux possesseurs de vlCVX. Pour le reste, il sera distribué avec une levée de fonds communautaire, du liquidity mining sur CNC/ETH et aux déposants sur Conic. Pour en apprendre plus, il n’y a [qu’un seul article disponible pour l’instant](https://medium.com/@ConicFinance/conic-finance-pre-launch-announcement-7b9f485f59f2).


## Services d’emprunt avec tokens LP Curve/Convex en collatéral

Arrivé à ce stade, vous commencez peut-être à saturer rien qu’à l’évocation d’un nouveau wrapper potentiel sur CRV, CVX ou même cvxCRV : c’est sans doute normal. La plupart des protocoles impliqués dans les Curve Wars développent directement des synergies au niveau du token, qui reste le plus direct. Mais il ne faut pas oublier deux autres types d’acteurs important :

1. Les protocoles proposant un service synergétique avec le LP Curve/Convex, comme par exemple l’utilisation de celui-ci en collatéral.
2. Les protocoles / DAOs qui possèdent de larges quantités de CVX et CRV et peuvent les utiliser pour développer une position stratégique.

Avant d’aller voir du côté des whales et de leurs stratégies, je vous propose deux dernières analyses de protocoles qui permettent d’emprunter depuis une position LP Curve.


### Lendflare (LFT)

[Lendflare](https://lendflare.finance/) permet aux LPs Curve d’emprunter depuis leur position un actif qui suit le même peg, par exemple un emprunt de DAI avec le token LP 3pool (USDC/DAI/USDT) comme collatéral. Cette limitation permet d’éviter les liquidations dues aux variations de prix entre les actifs : avec Lendflare tant qu’un emprunteur rembourse sa dette à l’heure ou avant, il n’est pas liquidé.

Le point critique, comme avec tout marché monétaire, c’est de réussir à attirer assez de déposants pour rendre l’emprunt aussi peu coûteux que possible et donc compétitif. Lendflare reprend ici la logique des boosts de Curve : les utilisateurs qui apportent des liquidités (USDC, DAI, ETH ou wBTC) pour faciliter les emprunts sont rémunérés avec le token LFT.

Tout comme sur Curve, ils peuvent ici aussi bénéficier d’un multiplicateur allant jusqu’à 2.5x en verrouillant une quantité de LFT (veLFT) proportionnelle au dépôt. Il y a même un schéma très dense qui résume le tout et vous fera apprécier le soin tout particulier que je mets dans mes infographies maisons :

![LendFlare](/img/2022/curve-wars-l2/lendflare.jpeg)

Le protocole est encore en plein déploiement, bien que la fonctionnalité d’emprunt soit déjà disponible. Une vente initiale (IDO) du token LFT est en cours, et un airdrop est également discuté.


### Curvance (CVE) 🚧

Curvance s’attaque au même problème mais avec une approche différente. Ici le protocole ne s’intéresse pas aux LP Curve comme collatéral, mais plutôt aux “wrapped assets” en général comme cvxCRV, bveCVX (Badger) ou yvBOOST (Yearn). Pour permettre l’emprunt de Stablecoins avec ces actifs comme collatéral, ils envisagent d’isoler le risque en s’appuyant sur des pools Fuse.

Là encore, le token CVE sera distribué aux apporteurs de liquidité et un système de type veCVE est envisagé avec une nouvelle subtilité : encore un wrap, une version liquide du veCVE, le cveCVE qui donne accès au rendement du veCVE mais délègue les capacités de gouvernance à la DAO. Ici encore, des boosts, des jauges, et même potentiellement des bribes sont envisagés

Pour les curieux, [la documentation est ici](https://docs.curvance.com/cve/).


## DAOs whales en CVX

Enfin, pour finir ce panorama de l’écosystème Curve/Convex, il ne faut pas oublier de regarder  directement les tokens - et notamment les DAOs qui possèdent de grandes quantités de CRV ou CVX.

Pour CRV, il n’existe pas encore de tableau de bord clair résumant la situation à ma connaissance. Pour CVX par contre, il y a un site pour ca : [daocvx.com](Daocvx.com). Les protocoles que nous allons détailler désormais n’ont donc pas de synergie construite nativement avec Curve ou Convex, mais ils possèdent de grande quantité de CVX et les utilisent pour améliorer leur position compétitive dans la guerre des CRV.

![daocvx.png](/img/2022/curve-wars-l2/daocvx.png "Distribution des tokens CVX parmi les différentes DAOs (⚠️DAO uniquement)")

Je vous laisse creuser la liste par vous-même, on en détaillera simplement deux : Frax et Badger.


### Frax Finance : dominer le jeu des jauges Curve

Frax développe depuis longtemps une stratégie pertinente qui vise à dominer le jeu des jauges Curve pour aider à l’adoption de FRAX. Ca a été une des premières DAO à acquérir une position conséquente en CVX ; c’est désormais la DAO ayant **la plus grosse position avec plus de 2.1M CVX**.

Frax est connu pour être également le projet le plus agressif avec les bribes et c’est fréquemment Frax qui propose le plus gros bribe de Votium pour sa pool FRAX/3crv. Au dernier round (14), le bribe de Frax représentait environ **40% de la valeur totale de toutes les bribes** payées à ce round ($6.5M / $16.2).

Si Frax peut se permettre d’être aussi agressif, c’est que leur position vlCVX permet de réduire le coût effectif de ces bribes : grâce à ses propres votes, le protocole est en mesure de [récupérer](https://etherscan.io/tx/0x090777069299e6e292363c6131b5cc5b463d598a7f89d3c7207148c0497587f8) une partie non négligeable des FXS utilisés à chaque round.

Avec cette stratégie, la pool FRAX/3CRV est en mesure de **maintenir un taux d’émission de CRV presque cinq fois plus élevé que la 3pool, pour une liquidité totale similaire** (3pool : $3.3B, FRAX : $2.7B).


### Badger : un petit coin pour Bitcoin

Depuis le début, Badger se concentre sur l’optimisation du farming avec BTC sur Ethereum. Initialement, avant Convex, Badger travaillait de près avec Yearn, mais avec le lancement de Convex et sa domination rapide, la position de Badger a évolué.

Contrairement à Frax, Badger n’a pas acheté ses CVX. À la place, Badger développe plutôt un modèle similaire à celui de Convex pour accumuler du CRV sous contrôle ; le vault bveCVX. Il propose un retour similaire au verrouillage direct sur Convex, mais s’inclut dans l'écosystème Badger.

Les balances en bveCVX contribuent par exemple au système de boost interne à Badger effectif sur la plupart des vaults. En outre, à chaque round la BadgerDAO utilise la puissance de vote correspondante au bveCVX pour soutenir les pools Curve supportées dans Badger, c’est à dire essentiellement des pools qui impliquent une ou plusieurs variantes du wBTC.

![bvecvx.png](/img/2022/curve-wars-l2/bvecvx.png)


Plutôt que d’acquérir sa position en CVX, Badger est en mesure de l’obtenir au prix d’émission sur son token natif - c’est donc en quelque sorte une location de CVX. Il y a également une pool Curve bveCVX/CVX pour permettre la sortie anticipée du vault. Il y a désormais presque 1.7M CVX dans le vault, la stratégie a donc fait ses preuves.


### Les autres DAOs

Je me suis concentré sur deux projets qui développent deux stratégies bien distinctes pour accumuler des CVX et peser dans les Curve Wars. Comme vous pouvez le voir sur le graphique plus haut, il y en a de nombreuses autres.

Quand un protocole développe une position conséquente sur CVX (disons >300K CVX), il bénéficie d’avantages directs pour son/ses tokens, notamment au niveau de la liquidité. Néanmoins ça ne s’arrête pas là : les grands possesseurs de CVX sont dans une position stratégique et vont être également courtisés très prochainement pour différents partenariats.


On voit déjà la mécanique à l'œuvre, avec la discussion autour d’une potentielle 4pool (USDC/USDT/FRAX/UST), rendue possible grâce au cumul des influences de Frax, Luna, Redacted et Olympus. Les protocoles-whales CVX deviennent ainsi des interfaces pour les Curve Wars, reste à voir qui saura leur faire la meilleure offre.

_🙏 Un grand merci à [Charles](https://twitter.com/C53300) pour sa relecture attentive et ses nombreuses suggestions pertinentes._
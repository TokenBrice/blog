---
title: "Gestion automatisée et collatéral : comment Autopilot, 40Acres et haiVELO font évoluer les veNFT"
description: "Le développement de la couche d’infrastructure des veNFTs avec Autopilot, 40Acres et haiVELO: automatisation et collatéralisation."
date: '2025-08-14T16:06:21.672Z'
categories: [DeFi]
tags: [DeFi, Ethereum, Decentralized Finance, Curve Finance, veCRV, Velodrome, veVELO, Aerodrome, veAERO, 40Acres, Autopilot, haiVELO]
toc: true
url: veNFT-infrastructure
image: img/2025/veNFT-infrastructure/cover-fr.png
---

Le paysage des veNFT évolue rapidement, inaugurant une nouvelle ère de finance décentralisée où le pouvoir de gouvernance et la génération de rendement sont tokenisés. À mesure que l'adoption du modèle veNFT s'est développée, **l'infrastructure qui le soutient a mûri**, exploitant le rendement natif des veNFT pour offrir de nouveaux services et automatisations. 

Dans cet article, je souhaite mettre en avant quelques‑uns d'entre eux:  **[Autopilot](https://theautopilot.xyz/), [40Acres](https://www.40acres.finance/) & [haiVELO](https://www.letsgethai.com/)**. Vous pouvez vous référer à mes articles précédents si vous n'êtes pas déjà familier avec le modèle veNFT:

* [ve(3,3), l'étape logique suivante après veCRV?](https://tokenbrice.xyz/solidly-velodrome-fork/)
* [Des nuances subtiles aux grandes conséquences: une analyse croisée de Curve et Velodrome](https://tokenbrice.xyz/crv-vs-velo/)

## Les veNFT ont supplanté les verrous

Les veNFT permettent aux utilisateurs d'immobiliser des jetons pendant une période déterminée pour obtenir un pouvoir de vote et des rendements augmentés. Ce mécanisme incite à la participation à long terme et à l'alignement avec les objectifs du protocole. L'innovation fondamentale des veNFT est que, contrairement aux anciens modèles de verrouillage tels que veCRV, **le verrouilleur obtient un jeton représentant son verrou: le veNFT**.

Mais tout comme pour les verrous Curve/Convex, la gestion des positions Velodrome et Aerodrome peut s'avérer chronophage et complexe sans les outils appropriés. Les utilisateurs disposent désormais de **tout un éventail d'options**, comme l'utilisation de leur veNFT en tant que collatéral ou l'automatisation complète de leur gestion. Plongeons‑y.

### Autopilot: Gestion autonome des positions veAERO

Autopilot propose une solution autonome pour la gestion des positions veAERO, permettant de détenir des veAERO de manière entièrement passive mais optimisée. Les utilisateurs délèguent leurs veAERO à Autopilot, qui n'en a pas la garde. Il s'agit plutôt de permettre à un assistant d’effectuer chaque semaine les actions suivantes sur vos veNFT:

1. Vote optimisé
2. Réévaluation (rebase) et revendication des frais + des pots‑de‑vin
3. Vente des frais + des pots‑de‑vin en USDC

![Autopilot](/img/2025/veNFT-infrastructure/autopilot.png)

Une fois qu’un utilisateur dépose son veNFT, il peut en fait ne rien faire et laisser les USDC s’accumuler, pour les réclamer à sa convenance. Ce type de service **réduit considérablement la barrière à l'entrée** pour les utilisateurs qui souhaitent bénéficier des veNFT mais manquent de temps ou d'expertise pour une gestion active.

Le site est clair, et l'interface utilisateur fournit un détail des récompenses et de la réévaluation pour chaque époque, facilitant la comptabilité pour les projets ou les DAO qui souhaitent également utiliser Autopilot.

### 40Acres: des prêts auto‑remboursables avec un collatéral veNFT

Au‑delà de la gestion autonome, des instruments financiers innovants sont développés autour des veNFT. [40Acres](https://www.40acres.finance/) propose un service offrant **des prêts auto‑remboursables garantis par des veAERO/veVELO**. Ce mécanisme permet aux utilisateurs de débloquer de la liquidité à partir de leurs veNFT verrouillés sans avoir à vendre leurs positions.

![40Acres](/img/2025/veNFT-infrastructure/40acres.png)

40acres dispose également d'un «Autopilot» intégré, qui gère les votes et la collecte des récompenses au nom des utilisateurs. Ils peuvent aussi **personnaliser l’utilisation de leurs récompenses**, avec diverses répartitions en pourcentage entre le remboursement ou la croissance de la position (achat et verrouillage de plus de AERO). Le LTV est ajusté pour correspondre à un remboursement sur environ 52 époques: une année pour se rembourser entièrement.

Ce service transforme les veNFT en actifs plus liquides, permettant aux utilisateurs d’**accéder à un capital immédiat tout en exploitant intelligemment le potentiel de rendement futur**.

### haiVELO: amélioration de rendement sur veVELO

Certains projets **tirent intelligemment parti des Dromes en offrant un service aux détenteurs de veNFT** ou aux fournisseurs de liquidité. L’un d’eux est [HAI](http://letsgethai.com/earn), avec haiVELO. Pour les utilisateurs, haiVELO fournit un dérivé liquide de veVELO avec une amplification supplémentaire du rendement, puisqu’il peut servir de collatéral pour minter du HAI. Le vote est optimisé pour le rendement, et payé en HAI.

### Relayers: stratégies OG

Au‑delà des infrastructures supplémentaires et des intégrations, Velodrome et Aerodrome offrent, à la base, les relais, fournissant **un accès en un clic à des stratégies de vote partagé et de capitalisation**. La plupart sont centrés sur un projet donné cherchant à développer sa liquidité, mais certains peuvent aussi être motivés par une cause, comme les relais de la DeFiCollective.

![Velo/Aerodrome Relays](/img/2025/veNFT-infrastructure/relay.png)

Les projets peuvent construire sur leurs relais, par exemple en attribuant des récompenses aux déposants fidèles, mais nous n’en avons pas encore beaucoup vu.

## Projets x Infrastructure

Pour illustrer comment cette couche d’infrastructure supplémentaire impacte les projets impliqués dans l’écosystème, laissez‑moi discuter des Luchadores et en particulier de leur stratégie veAERO. **Deux ensembles de veAERO** sont gérés pour fournir un équilibre de rendement, d'utilité et de croissance. **Le premier, déposé dans Autopilot**, procure un flux constant de stablecoins pour le paiement des dépenses. Un **second veAERO déposé dans le relais El Volador Luchador** soutient les rendements des pools LUCHA sur Aerodrome, que le trésor alimente également à hauteur d’environ 200000$. La stratégie est **entièrement automatisée** grâce à Autopilot et ne nécessite que la définition de la stratégie de vote du relayer.

![Luchadores AERO Strategy](/img/2025/veNFT-infrastructure/luchadores-strategy-fr.png)

En plus de **couvrir les salaires de deux membres clés (~2000$ par mois)**, la gestion efficace de la position offre **des leviers de croissance soutenue pour le projet**, ce qui lui a permis de constituer une réserve d’environ 13000$ en ETH et en stablecoins, **tout en maintenant 400000$ de liquidité pour son jeton**. Le projet contrôle maintenant un total d’environ 223000 veAERO, dont la valeur nominale équivaut presque à l’ensemble de la capitalisation de marché de LUCHA.

L’intégration des veNFT dans des produits plus avancés est fascinante à observer. Comme ils incluent un rendement solide de 25–30% lorsqu’ils sont correctement optimisés, ils offrent de nombreuses options allant des prêts auto‑remboursables à une source de rendement en stablecoins entièrement automatisée. De telles innovations accroissent l’accessibilité et l’efficacité du capital, tout en favorisant la croissance d’un écosystème. 40Acres compte désormais plus de 40M$ de dépôts, tandis qu’Autopilot gère 5,8M de veAERO, soit environ 8M$.

## PS: N'oublions pas la comptabilité

Avant de conclure, je souhaite partager un dernier ensemble de **conseils et d’outils qui pourraient s’avérer utiles aux détenteurs de veAERO/veVELO** concernant la comptabilité.

Ce n'est pas le sujet le plus excitant, mais il reste essentiel pour une bonne gestion des positions, comme mon expérience avec la [DeFi Collective](https://deficollective.org/), où c'est un sujet clé, me l'a appris. L’outil le plus notable à exploiter est un tableau de bord Dune personnalisé qui peut facilement être adapté à votre position, permettant un suivi et un rapport hebdomadaires sur:

1. Les frais de trading gagnés (votes)
2. Les pots‑de‑vin gagnés (votes)
3. AERO/VELO revendiqués (LP)

Vous trouverez la [version Velodrome/OP ici](https://dune.com/spicypiz/defi-collective-pools), et la [version Aerodrome/Base](https://dune.com/spicypiz/defi-collective-pools-base) ici.

Pour ceux qui souhaitent ne laisser aucune dépense de côté, le [tableau de bord Dune de vérification des dépenses en gas de 0Khmer](https://dune.com/0xkhmer/gas-spent-checker) se révèlera également très utile. Je suis enthousiaste de voir les veNFT se développer et les nouvelles possibilités qu’ils offrent à la fois aux projets et aux détenteurs individuels: j’espère que cet article vous a aidé à tirer le meilleur parti de vos veNFT.

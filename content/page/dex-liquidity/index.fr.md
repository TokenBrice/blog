---
title: "DEX et Liquidité"
description: "Guide evergreen des exchanges décentralisés : AMM, pools de liquidité, swaps d'actifs pegged, vote-escrow, bribes, routing et liquidity shaping."
slug: dex-liquidity
date: 2026-05-18
lastmod: 2026-10-01
toc: true
readingTime: false
reading_path:
  - { path: "/pegged-assets-swap/", group: core, note: "Comparez les designs de liquidité pour actifs corrélés avant de choisir un DEX." }
  - { path: "/crv-vs-velo/", group: core, note: "Curve contre Velodrome : qui capte la valeur et qui finance la liquidité ?" }
  - { path: "/solidly-velodrome-fork/", group: core, note: "Le modèle Solidly/Velodrome, étudié dans sa version de 2023." }
  - { path: "/venft-infrastructure/", group: core, note: "Automatisation et collatéral autour des veNFT, avec leurs dépendances." }
  - { path: "/defi-flywheel/", group: core, note: "Suivez la boucle d'incitations plutôt que l'APY affiché." }
  - { path: "/maverick-liquidity-shaping/", group: historical, note: "Le design de liquidity shaping de Maverick en 2023." }
  - { path: "/balancer-wars/", group: historical, note: "La course au pouvoir de vote Balancer de 2022." }
  - { path: "/crv-wars-l2/", group: historical, note: "Les couches autour de Convex et les marchés de vote de 2022." }
  - { path: "/crv-wars/", group: historical, note: "L'explication originale des Curve Wars de 2021." }
  - { path: "/decentralized-exchange-value-capture/", group: historical, note: "La comparaison de la distribution des frais DEX de 2021." }
  - { path: "/swap-swamp/", group: historical, note: "Les bases du swap via les interfaces de 2020. Vérifiez le routing et les approvals actuels." }
---

Les DEX sont la couche d'exécution de la DeFi. Ils pricent les actifs, routent le volume, créent des flux de frais et transforment les incitations de gouvernance en liquidité. Le sujet n'est pas seulement le TVL, mais la forme de la liquidité, qui paie les incitations et si le design sert mieux des actifs volatils ou pegged.

## Parcours de lecture

{{< reading-path >}}

## Concepts clés

- [DEX](/fr/glossary/dex/), [AMM](/fr/glossary/amm/) et [pool de liquidité](/fr/glossary/liquidity-pool/) définissent le lieu.
- [Slippage](/fr/glossary/slippage/), [price impact](/fr/glossary/price-impact/) et [routing](/fr/glossary/routing/) expliquent la qualité d'exécution.
- [Vote escrow](/fr/glossary/vote-escrow/), [gauge](/fr/glossary/gauge/) et [bribes](/fr/glossary/bribes/) expliquent les marchés d'incitation.
- [Liquidity shaping](/fr/glossary/liquidity-shaping/) couvre les nouveaux designs.

## Hubs liés

- [Catégorie DEX](/fr/categories/dex/)
- [CRV Wars](/fr/series/crv-wars/)
- [Pegged Assets](/fr/series/pegged-assets/)
- [Yield](/fr/yield/)
- [Gouvernance](/fr/governance/)

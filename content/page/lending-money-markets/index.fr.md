---
title: "Prêt DeFi : collatéral, taux et risques"
description: "Prêt DeFi sans brouillard marketing : collatéral, liquidations, taux et agrégation. Un parcours dans les analyses et les grilles de risque."
slug: lending-money-markets
date: 2026-05-18
lastmod: 2026-10-01
toc: true
readingTime: false
reading_path:
  - { path: "/money-markets-risk/", group: core, note: "Le risque d'abord : une grille d'analyse, pas un classement des marchés actuels." }
  - { path: "/lending-aggregation/", group: core, note: "Ce que l'agrégation change, et ce qu'elle ne fait que masquer." }
  - { path: "/lending-protocol-renaissance/", group: core, note: "Les designs CDP et money markets de 2024, avec leurs compromis." }
  - { path: "/leverage-sir/", group: core, note: "Un autre mécanisme de levier et les risques qui l'accompagnent." }
  - { path: "/venft-infrastructure/", group: core, note: "Quand les positions de vote deviennent collatéral et rendement avec levier." }
  - { path: "/reflexer-rai/", group: historical, note: "Le design RAI de 2021 : collatéral ETH et prix de rachat flottant." }
  - { path: "/liquity-protocol/", group: historical, note: "Le design LUSD de Liquity V1 en 2021, pas Liquity V2 ou BOLD." }
  - { path: "/money-market-innovations/", group: historical, note: "La taxonomie de 2021, dont les prêts façon Alchemix." }
  - { path: "/money-market-recipes/", group: historical, note: "Les stratégies originales de 2021. Les paramètres ne sont pas des instructions actuelles." }
  - { path: "/leveraging-eth/", group: historical, note: "Une recette d'emprunt Maker de 2020, pas une recommandation de taux actuel." }
---

Les protocoles de lending sont une primitive racine de la DeFi. Ils permettent d'emprunter contre collatéral, fournir des actifs pour obtenir un rendement, construire des stratégies avec levier et émettre des actifs stables. L'interface paraît simple, mais le risque se loge dans les collatéraux listés, les oracles, les liquidations, la gouvernance, la liquidité et les modèles de taux.

## Parcours de lecture

{{< reading-path >}}

## Concepts clés

- [Money market](/fr/glossary/money-market/) et [lending](/fr/glossary/lending/) définissent la primitive.
- [Emprunt](/fr/glossary/borrowing/), [LTV](/fr/glossary/ltv/), [health factor](/fr/glossary/health-factor/) et [liquidation](/fr/glossary/liquidation/) couvrent le risque utilisateur.
- [Oracle de prix](/fr/glossary/price-oracle/) est une dépendance protocolaire centrale.
- [CDP](/fr/glossary/cdp/) relie lending et émission de stablecoins.

## Hubs liés

- [Catégorie Lending](/fr/categories/lending/)
- [Série Money Markets](/fr/series/money-markets/)
- [Stablecoins](/fr/stablecoins-guide/)
- [Risque DeFi](/fr/defi-risk/)
- [Yield](/fr/yield/)

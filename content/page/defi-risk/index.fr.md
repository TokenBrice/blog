---
title: "Risque DeFi"
description: "Guide evergreen du risque DeFi : smart contracts, gouvernance, oracles, collatéral, liquidité, liquidations, bridges, structure de marché et opérations utilisateur."
slug: defi-risk
date: 2026-05-18
lastmod: 2026-10-01
toc: true
readingTime: false
reading_path:
  - { path: "/money-markets-risk/", group: core, note: "Commencez par les dépendances et les chemins de défaillance, pas par un score." }
  - { path: "/unstoppable-defi/", group: core, note: "Demandez ce qui peut encore être arrêté, upgradé ou capturé." }
  - { path: "/defi-ux-disaster/", group: core, note: "La curation et le risque utilisateur font partie de l'analyse protocolaire." }
  - { path: "/defi-bullshit-detector/", group: core, note: "Une méthode d'enquête pour confronter les affirmations, pas un audit magique." }
  - { path: "/pharos/", group: core, note: "Le projet de suivi des stablecoins que je construis. Un signal n'est pas une garantie." }
  - { path: "/farewell-glc/", group: historical, note: "Mon départ du comité GHO en 2024 : incitations, conflits et langage de gouvernance." }
  - { path: "/risk-tranching-defi/", group: historical, note: "Le cas Saffron de 2021 : répartir le risque ne le supprime pas." }
  - { path: "/great-filter-defi/", group: historical, note: "Le filtre de 2020 pour séparer les mécanismes durables du bruit fragile." }
---

Le risque DeFi n'est pas une seule chose. C'est une pile de dépendances techniques, économiques, de gouvernance, de liquidité et opérationnelles. Le but n'est pas de trouver un protocole sans risque, mais de comprendre ce qui peut casser, comment les pertes se propagent et si la rémunération vaut l'exposition.

## Parcours de lecture

{{< reading-path >}}

## Checklist de risque

- Risque contractuel : audits, upgradeability, clés admin, bug bounties et contrats dépendants.
- Risque oracle : qualité des sources de prix, fréquence de mise à jour, résistance à la manipulation et fallback.
- Risque collatéral : liquidité, volatilité, permissions du token, exposition bridge et centralisation.
- Risque liquidation : profondeur de marché, concurrence des keepers, bad debt et cascades.
- Risque gouvernance : multisigs, timelocks, quorum, capture, délégation et pouvoirs d'urgence.
- Risque utilisateur : approvals, phishing, mauvais réseau, levier et suivi des positions.

## Concepts clés

- [Smart contract](/fr/glossary/smart-contract/), [audit](/fr/glossary/audit/) et [bug bounty](/fr/glossary/bug-bounty/) couvrent le risque code.
- [Oracle de prix](/fr/glossary/price-oracle/), [liquidation](/fr/glossary/liquidation/) et [liquidation cascade](/fr/glossary/liquidation-cascade/) couvrent la mécanique de marché.
- [Multisig](/fr/glossary/multisig/), [timelock](/fr/glossary/timelock/) et [attaque de gouvernance](/fr/glossary/governance-attack/) couvrent le risque de contrôle.
- [Bridge](/fr/glossary/bridge/), [exploit](/fr/glossary/exploit/) et [rug pull](/fr/glossary/rug-pull/) couvrent les chemins de défaillance fréquents.

## Hubs liés

- [Catégorie Analyses](/fr/categories/analysis/)
- [Money Markets](/fr/series/money-markets/)
- [Lending et Money Markets](/fr/lending-money-markets/)
- [Stablecoins](/fr/stablecoins-guide/)
- [Gouvernance](/fr/governance/)

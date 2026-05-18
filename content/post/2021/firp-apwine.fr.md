---
title: "🍷 En oenologie comme en DeFi, la patience paye : introduction aux FIRps avec APWine.FI"
description: "Une introduction aux protocoles de fixation de rendements (FIRP) au travers du prisme d'APWine pour mieux comprendre ce qu'ils permettent de faire et apportent à DeFi"
date: '2021-02-11T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Yield]
tags: [DeFi, Ethereum, DEX, Money Markets, Aave, Compound, APWineFi, 88mph, Fixed Interest Rate Protocol, FIRP]
toc: true
tocNum: true
url: fixed-interest-rate-protocol-firp-apwine
image: /img/2021/firp-apwine/pac-man.png
difficulty: "intermediate"
---


La production de rendements, c'est comme l’œnologie : le secret réside dans le processus. Alors que DeFi se développe plus rapidement que jamais, avec maintenant plus de 50 milliards de dollars de valeur totale bloquée sur tous les protocoles, **l'offre de rendement se diversifie**.

Notre sujet d'aujourd'hui frappe au cœur de cette tendance, avec une solution offrant un rendement potentiellement instantané pour les dépôts sur les protocoles DeFi comme Yearn ou Aave : APWine. Mais avant d'en arriver là, nous devons replacer dans leur contexte les marchés monétaires et les FIRP en général, car il s'agit encore de types de produits nouveaux pour la plupart des utilisateurs de DeFi.

---

## Marché monétaire = PacMan

Le tranching (sérialisation de risque), l'assurance et les FIRP agissent tous les trois comme des **couches d'abstraction construites sur un marché monétaire** pour fournir des fonctionnalités supplémentaires :
1. **🔪 Tranching** ➡ meilleure séparation des différents types de risques
2. **🛡 Assurance** ➡ couverture contre les défaillances techniques (& plus !)
3. **🔮 FIRPs** ➡ "couverture" contre les variations de l'APY

Bien qu'elles soient intéressantes en tant que telles, ce qui me fascine, c'est ce qui se passe **quand/si elles sont intégrées au niveau de base**. Cela permettrait à d'autres protocoles d'exploiter ces fonctionnalités. Par exemple, Harvest pourrait proposer un vault USDC "sans risque" et qui amène essentiellement l'ensemble de la DeFi à un autre niveau.

En effet, les valeurs nouvelles portées par la DeFi ne sont pas seulement un avantage pour la transparence et l'audibilité : elle rendent la DeFi **aussi au moins <ins>un ordre de grandeur</ins> plus efficace** que le patchwork de finance mourant qu'elle est destinée à remplacer.

---

## Protocoles de fixation de rendements (FIRP)

Avant de commencer, définissons ce que sont les protocoles de fixation de rendement et quel est leur rôle dans l'écosystème plus large de la finance décentralisée sur Ethereum.

Avec le DeFi, l'objectif pour la plupart est **de produire des rendements à partir d'un actif donné.** Habituellement, l'un des moyens les plus faciles d'y parvenir sera de le prêter, par exemple, pour un retour. Pour ce faire, il faut assumer plusieurs niveaux de risque contre lesquels on peut s'assurer (-> Unslashed) ou simplement éviter de prendre grâce au tranchage (-> Saffron).

Même si vous êtes super responsable et que vous essayez d'assurer et de protéger davantage vos dépôts, il vous reste un problème important : **le rendement de base produit par l'actif est généralement volatil**, ce qui rend la tarification de l'ensemble (dépôt prêté + assurance + tranching) difficile à comprendre.

![coingecko-crypto-2020-report](/img/2021/firp-apwine/coingecko-report.png "CoinGecko a mis en évidence les différentes approches du FIRP comme un sous-ensemble croissant de la DeFi dans leur dernier rapport")

Consultez le [rapport complet ici](https://assets.coingecko.com/reports/2020-Year-End-Report/CoinGecko-2020-Report.pdf).

C'est précisément là que les FIRP ont une chance de briller : **parce qu'ils rendent l'intérêt prévisible, les FIRP contribuent à promouvoir une attitude plus responsable** pour l'ensemble de l'espace - en facilitant l'utilisation de toutes les méta-structures désormais disponibles pour protéger les dépôts sur les marchés monétaires ou les gestionnaires d'actifs DeFi.

Cet article traite uniquement des protocoles de taux d'intérêt fixes. Pour une perspective plus large de la gestion des risques liés aux dépôts des DeFi, **[lire mon introduction sur l'assurance, le tranching et les FIRP](https://tokenbrice.xyz/fr/tranching-risque-defi/)**. Nous y avons abordé la manière dont l'assurance, la sérialisation et les taux d'intérêt fixes pourraient éventuellement être intégrés dans les marchés monétaires, ce qui permettrait de **[envisager des Stablecoins porteurs d'intérêts "sans risque"](https://tokenbrice.xyz/fr/tranching-risque-defi/)**.

Cet article suppose une compréhension minimale du sujet. Si quelque chose n'est toujours pas clair, veuillez vous référer à l'article précédent ☝

---

## APWine : Sauternes à rendement fixe 🍷

Alors, avec une introduction d'enfer et sans plus attendre, plongeons dans l'affaire d'aujourd'hui : **comprendre ce que sont les FIRP et ce qu'ils apportent à la table à travers le prisme d'APWine**.

🍷 Encore mieux, c'est sur le thème du vin et les Frenchies sont impliqués - comment ne pas aimer ?

### La différence entre APWine et 88mph

D'un point de vue de haut niveau, les deux projets pourraient être décrits comme des FIRP, mais ils atteignent ce résultat par des moyens différents :

* Avec 88mph, le rendement de vos dépôts est fixé grâce à un marché secondaire de prédiction construit pour lui.
* Avec APWine, vous pouvez bloquer vos actifs pendant un mois par exemple pour obtenir instantanément le rendement.

Pour être plus explicite, les deux moyens ne sont pas interchangeables et ne fonctionnent pas sur la même période : avec 88mph, le revenu devient **prévisible mais c'est toujours un processus itératif**. Avec APWine, le revenu devient **prévisible et instantanément livré**.

Cela signifie également différents compromis du côté de la gestion des risques. Avec 88mph, le rendement est calculé de manière algorithmique - il y a toujours un acheteur, ce qui est pratique, mais cela signifie aussi que le protocole peut accumuler des dettes en cas de non-concordance.

L'inverse est vrai pour APWine : puisqu'il est basé sur un marché, aucun décalage ne peut se produire (-> pas de dette protocolaire), mais cela signifie qu'il peut y avoir des problèmes de demande/offre (tels que de fortes remises sur les FYT).

![apwine-deposit-process](/img/2021/firp-apwine/apwine.png "Le processus de dépôt sur APWine (source : site officiel)")

### APWine : Jour de paie instantané ?

Avec APWine, la logique est assez simple. Tout commence par le dépôt d'un token rapportant un certain rendement, comme un stablecoin déposé sur Aave ou un token de vault Yearn.

Au début de chaque période, les utilisateurs reçoivent des FYT (Future Yield Tokens) représentant leurs rendements pour la période. **Les FYT sont des tokens ERC-20 standard** qui seront négociables peu après le lancement sur APWine.

Le dépôt est bloqué pour la période, mais les utilisateurs peuvent se retirer de manière anticipée moyennant des frais, en brûlant leurs tokens FYT. La slashing est désactivée pour la période bêta.

Comme le rendement est instantanément disponible et utilisable, APWine devrait offrir de nombreuses possibilités de couverture et d'arbitrage.

{{< notice note >}}
Après plusieurs semaines de testnet, APWine arrive sur le mainet ! La beta commencera dans quelques semaines, avec **la première période qui début le 1er Mars**. Le lancement du token APW et du liquidity mining associé devraient suivre.

**[Plus d'informations sur la bêta et le lancement d'APWine](https://apwine.medium.com/our-beta-is-live-on-the-ethereum-mainnet-3860491a365c)**.
{{< /notice >}}

## Les prochaines étapes pour APWine

À court terme, je suivrai de près le lancement de la plateforme la semaine prochaine. Plusieurs lancements à venir ont déjà été annoncés, comme l'arrivée de plus de services et de pools sur la plateforme et la sortie du token APW et de son plan de liquidity mining associé.

Comme toujours, ce qui m'excite vraiment, c'est le endgame !

### L'Endgame : un protocole de couverture de rendement

Avant d'envisager la fin du jeu ici, nous devons d'abord voir si l'idée fonctionne et **s'il y a une réelle adéquation**. Dans le cas d'APWine, **le succès sera mesuré en examinant la santé des marchés des tokens FYT**.

Je ne m'attends pas à ce qu'ils s'établissent à parité avec les rendements attendus, mais si les utilisateurs peuvent vraiment obtenir une **paiement instantané même avec une redevance de 20%**, je suis sûr qu'il y aura une demande.

Pour y parvenir, il faut avoir des marchés FYT vraiment liquides, ce qui est parfaitement faisable, surtout s'il existe un plan d'exploitation des liquidités dans le token APW pour les amorcer. En ce qui concerne le token APW lui-même, une plongée dans la FAQ vous donnera un peu plus d'informations sur ce que l'équipe envisage :

> A chaque expiration future, 10% du rendement généré est partagé entre tous les détenteurs de tokens APW (pourcentage susceptible de changer dans le futur en fonction de la demande du marché). Le token leur permettra également de participer aux mécanismes de gouvernance d'APWine.
>
> - Source : [APWineFi FAQ](https://apwine.fi/faq)

Donc, en plus du droit de gouvernance habituel du protocole, il semble qu'il y ait déjà une source de revenus envisagée pour le token APW, en plus de tout plan potentiel d'extraction de liquidités impliquant une paire basée sur APW.

---

Le français étant la langue de DeFi, il était temps d'impliquer de bons vignerons dans le processus de brassage des rendements ! Si vous êtes intéressé par le protocole, vous pouvez **[en savoir plus sur la version bêta ici](https://apwine.medium.com/our-beta-is-live-on-the-ethereum-mainnet-3860491a365c)**.

![apwine-deposit-process](/img/2021/firp-apwine/defi-france-live-19.png)

Je vous suivrai de près car je vais avoir **[un chat avec Antoine](https://www.youtube.com/watch?v=Zo0B64swtPI)**, une des personnes impliquées dans APWine la semaine prochaine (en français). Retrouvez-nous Lundi 15 à 17h sur le YouTube pour le direct, ou à tout moment après pour le replay.

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/c/DeFiFrance)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

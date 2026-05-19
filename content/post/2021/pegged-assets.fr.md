---
title: "Actifs à vocation stable sur Ethereum : quelles approches et quels enjeux ?"
description: "La quête de stabilité sur Ethereum : aperçu des différentes approches de stabilisation et indexation d'actifs pour en comprendre leurs enjeux."
date: '2021-03-23T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Stablecoin, Lending, Yield]
tags: [DeFi, Ethereum, Finance Décentralisée, DEX, Aave, Compound, Reflexer, Stablecoins, MakerDAO, Basis Cash, Empty Set Dollar, Dynamic Set Dollar]
series: pegged-assets
series_order: 1
toc: true
tocNum: true
url: actifs-stables-ethereum
image: /img/2021/pegged-assets/money-god-meme.png
difficulty: "intermediate"
---

Aujourd'hui, je veux traiter un sujet essentiel pour Ethereum et les autres blockchains et souvent mal compris : **les actifs "stables"**, qui suivent le prix d'un actif de référence. Avant d'étudier les différentes approches qui permettent de produire un tel actif, on va d'abord commencer par un niveau d'analyse plus élevé :

1. Pourquoi a-t-on besoin de tels actifs ?
2. Quels usages en sont faits ?
3. Pourquoi veut-on représenter des actifs non-natifs d'Ethereum sur cette chaîne ?

Une fois ces bases établies, on aura le nécessaire pour **étudier les différentes approches et comprendre leurs enjeux**. Je finirai avec une analyse plus détaillée d'un projet qui me semble très pertinent et innovant sur la question : le RAI de Reflexer Labs.

{{< notice note >}}
Dans cet article, faute de traduction satisfaisante je vais parler de "pegged-assets" c'est-à-dire des actifs indexés sur un autre, au sens large. Ils ne sont pas tous indexés sur le dollar, par exemple il y a aussi des pegged-assets BTC sur la chaîne Ethereum, comme wBTC ou RenBTC.
{{< /notice >}}

---

Si vous connaissez déjà bien les différents mécanismes de pegging, vous pouvez sauter [directement vers la section sur Reflexer](#zoom-sur-le-rai-de-reflexer).

## Représentation d'actifs sur la chaîne Ethereum

Le volume d'émission et d'utilisation des pegged-assets (actifs indexés) a explosé l'année dernière, mais avant de voir concrètement à quoi ils servent, comprenons pourquoi. Le cas d'usage le plus simple est celui qui vise à produire un actif stable, le plus souvent indexé sur le dollar.

Pour se faire, **l'approche utilisé à un haut niveau est la tokénisation** : on représente un actif qui vient d'une autre chaîne / d'un autre monde sur Ethereum, comme par exemple wBTC (correspondant à 1 BTC sur la chaîne Bitcoin) ou encore USDC (correspondant à 1 USD dans le compte en banque de Circle, en très bref).

Cela permet de **répondre à une des inquiétudes les plus communes pour le grand public : [les cryptos sont des actifs volatiles](https://tokenbrice.xyz/fr/Stablecoins/)**.

En outre, **l'essor des Stablecoins est allé de pair avec l'essor de la DeFi**, pourquoi ? Il y a pour moi de nombreuses raisons dont voici les principales :

1. Les emprunts
2. Les actifs stables peuvent être très productifs en DeFi

### Pourquoi les emprunts se font essentiellement en Stablecoins ?

[Les marchés monétaires](https://tokenbrice.xyz/fr/marche-monetaire-risque/) permettent à leur utilisateurs d'emprunter des actifs en utilisant d'autres actifs comme garanties (collatéral). Le cas d'usage le plus fréquent correspond au schéma suivant :

1. L'utilisateur dépose un actif volatile, comme ETH, wBTC ou encore LINK
2. Il l'utilise comme collatéral pour **emprunter un actif stable, comme USDC ou DAI**.

Pourquoi est-ce ainsi ? Pour le dire simplement, peu de gens sont friands des risques liés aux variations de prix. **Emprunter un actif, si vous le mobilisez ensuite revient à le shorter**. Pas de problème avec les Stablecoins — à priori donc, mais la réalité est tout autre avec un actif non stable : si le prix diminue, tant mieux pour vous : la dette n'en sera que moins chère à rembourser.

Néanmoins dans l'autre sens le scénario peut être effrayant puisque **vous pouvez vous retrouver avec une dette qui augmente**. Je m'explique : mettons que vous empruntez 1000 UNI quand il vaut $20. Vous les vendez pour un autre token, par exemple des Stablecoins. Vous voilà donc avec $20 000 DAI que vous mobilisez en DeFi par exemple.

Vous gardez votre dette plusieurs mois et vous souhaitez désormais la rembourser. Sauf que l'UNI vaut maintenant $30 et vous n'en avez plus : vous devez en racheter sur les marchés pour rembourser la dette et clôturer la position. **La dette se paie toujours dans l'actif emprunté** : vous devez donc 1000 UNI à $30 l'unité soit 30 000 DAI.

{{< notice warning >}}
J'ignore ici totalement les intérêts du prêt par simplicité. En réalité vous devriez rembourser légèrement plus d'UNI, en fonction du taux d'intérêt et de la durée d'exposition.
{{< /notice >}}

### Production de rendement avec des Stablecoins

Avec le premier point compris, le second coule de source : **de très nombreuses personnes empruntent des Stablecoins**, cela signifie donc que de l'autre côté du marché des gens les prêtent, pour des taux d'intérêt attractifs vu la demande. Par exemple sur Aave, un des principaux marchés monétaires, on constate **une crise de liquidité (_liquidity crunch_) sur les Stablecoins** quasiment depuis le lancement de la v2. Les déposants bénéficient d'un retour moyen annualisé de 10% environ.

La situation est assez similaire ailleurs avec des différences dues aux spécificités de chaque marché monétaire. Néanmoins, la crise de liquidité sur les Stablecoins dépasse largement Aave : elle s'étend potentiellement à toute la DeFi.

En effet, **les opportunités pour produire un retour avec des Stablecoins ne manquent pas**. Je vous parle ici de prêts, mais il est également possible d'apporter de la liquidité sur les paires de Stablecoins voire de cumuler les deux approches pour augmenter le rendement avec un produit comme Curve :

![curve-yield-pool](/img/2021/pegged-assets/curve-yield-pool.png "Curve propose de nombreuses pools acceptant des Stablecoins productifs")

### Explosion de l'utilisation des pegged-assets en 2020

On a ainsi observé une véritable explosion de l'émission et de l'utilisation des pegged-assets en 2020. D'un côté, de plus en plus de projets se lancent pour proposer de **nouveaux types d'actifs ou de nouvelles approches pour les représenter**. De l'autre, les scénarios d'utilisation de ces pegged-assets se multiplient grâce à la croissance des marchés monétaires de Curve, des vaults comme ceux proposés par Yearn ou Harvest et d'autres produits DeFi plus complexes encore.

Pour n'en citer qu'un, parlons un peu[ d'Alchemix](https://alchemix.fi/), un nouveau service d'actif synthétique qui permet **des emprunts sécurisés par votre futur rendement**. Je m'explique : avec Alchemix, tout débute avec un actif stable qui produit un rendement. Ils ont choisi le yDAI pour commencer (DAI productif grâce au vault Yearn).

L'utilisateur donc commencer par déposer des yDAI. Il peut ensuite **renoncer à son futur rendement** pour emprunter jusqu'à 50% de la valeur déposée. Son prêt est **remboursé automatiquement grâce aux intérêts produits par le yDAI**. En outre, comme il a accès à 50% de la valeur déposée immédiatement (emprunté en alUSD), il peut la mettre au travail pour augmenter le retour de l'ensemble de la stratégie.

Ce type de produits permet un arbitrage temporel intéressant et entraîne une demande encore plus conséquente pour les Stablecoins : lors du lancement d'Alchemix, les dépôts dans le vault yDAI ont décollé au point d'atteindre la capacité maximale pendant un moment.

Je vous ai parlé jusqu'à présent plutôt des Stablecoins, mais un scénario similaire s'est déroulé sur d'autres pegged-assets comme les BTC tokénisés sur Ethereum.

![stablecoin-growth-ethereum-messari](/img/2021/pegged-assets/stablecoin-growth.png "Perspective historique sur l'évolution du volume de Stablecoins émis sur le réseau Ethereum. Source: Messari.")

Face à la croissance impressionnante de la DeFi, on ne peut s'attendre qu'à une augmentation toujours plus rapide de la demande pour ce type d'actifs. Voyons donc les différentes approches utilisées pour les produire afin de comprendre leur compromis.

---

## Les différentes approches pour produire des pegged-assets

Jusqu'à présent, la très large majorité de cette demande pour des actifs stables est adressée avec des solutions s'appuyant sur une correspondance 1:1 nécessitant de la confiance. Ainsi, ce sont **essentiellement USDT ($38.5 B émis) et USDC ($9.4 B) qui mènent la danse**, bien devant DAI ($2.7 B). Idem côté Bitcoin, sans rentrer dans les détails, toutes les solutions les plus utilisées nécessitent de la confiance.

{{< notice note >}}
En anglais on parle de "pegged-assets" (actifs indéxés). Ce sont des actifs qui suivent le prix d'un autre via un mécanisme dit de "pegging". Le "peg" est donc la valeur que l'actif doit maintenir, par exemple $1 pour les Stablecoins qui suivent le dollar.
{{< /notice >}}

Une diversité d'approches grandissantes sont donc explorées pour produire un pegged-asset avec moins de compromis. On les regroupe généralement dans des grandes familles qui correspondent à la principale méthode utilisée pour maintenir le peg. Néanmoins au fur et à mesure du développement de ces approches, les limites entre elles se confondent vu que plusieurs projets explorent **des approches hybrides mêlant plusieurs éléments de chaque**. On commence du plus simple à comprendre pour aller progressivement vers le plus complexe.


### La correspondance 1:1 avec un intermédiaire de confiance

*   **👍 Avantages :** Le peg est maintenu facilement et plutôt stable. Le système est solvable à tout moment (-> 1 USD en banque pour 1 USDC émis par ex)
*   **👎 Inconvénients / Risques :** Le système nécessite un intermédiaire de confiance central — l'organisme émetteur. Ce même organisme repose sur un autre intermédiaire, la banque où les USD sont déposés. En outre, la présence d'un intermédiaire de confiance crée un risque : est-il fiable ? transparent ? Le risque va au-delà de l'image, il peut aussi être légal.

On a déjà assez détaillé cette approche, je passe donc directement aux méthodes plus complexes.

### Stablecoin produit par sur-collatéralisation : Maker DAI

*   **👍 Avantages :** Le système n'implique plus d'intermédiaire de confiance central (en tout cas initialement) & arrive malgré tout à plus ou moins maintenir le peg.
*   **👎 Inconvénients / Risques :** Il faudra **toujours plus de collatéral en $ que de $ (DAI) produit (sur-collatéralisation)**. Risques de gouvernance. Risques aux niveaux des liquidations, effectués par des tiers. Le système est aussi trustless que ses collatéraux les plus utilisés. Maker accepte désormais des collatéraux censurables (wBTC, USDC, etc.) ce qui réintroduit un risque de confiance dans le système.

Bien avant les Stablecoins algorithmiques, MakerDAO est un pionnier quand on réfléchit à comment **produire un actif stable avec moins de confiance nécessaire dans le système que les approches 1:1**. Maker est un service plus complexe car au-delà du DAI — le stablecoin émis par le système, il permet également à ses utilisateurs d'utiliser différents actifs pour emprunter (techniquement battre / _mint_) des DAI.

En outre, cela recrée des risques et dangers pour maintenir le peg du DAI. De nombreuses améliorations ont été proposées et implémentées depuis le début, ce qui permet à DAI d'être désormais beaucoup plus stable que dans ses premiers jours. Néanmoins, la mise à l'échelle du DAI s'est faite avec des compromis additionnels en termes de confiance.

---

### Les approches plus innovantes

Ici, les approches sont plus diversifiées — je les regroupe en deux familles : les approches algorithmiques déjà bien étudiées sur mon blog ainsi que les approches hybrides. Toutes deux s'appuient sur un concept essentiel à comprendre : la "banque centrale" de ces systèmes est un smart contract.


#### Un smart contract comme "banque centrale"

{{< notice note >}}
J'utilise le mot "banque centrale" car il évoque bien le concept essentiel ici : l'organisme émetteur de la monnaie et qui applique la politique monétaire du système est un smart contract. Cela permet d'avoir une grande transparence et visibilité sur les actions relatives à la politique monétaire.
{{< /notice >}}

Donc pour comprendre les systèmes présentés plus bas, il faut vraiment saisir ça : **les décisions de création ou de destruction de nouveaux Stablecoins sont "prises" par un smart contract** — lui seul à cette capacité d'émettre (et de détruire dans certains systèmes) des jetons.

Quand je dis que le smart contract prend des "décisions" il faut aussi expliciter : pour être plus précis, on pourrait dire qu'**il réagit à l'évolution de différents paramètres mesurables**. Les décisions du smart contract sont donc transparentes et prédictibles. Un changement des règles qui le régissent est possible mais uniquement via un vote de gouvernance.

Le plus souvent, le principal paramètre pris en compte est tout simplement **le prix du stablecoin**. Par exemple dans les premiers systèmes algorithmiques comme Basis (BAC est le stablecoin), les règles sont simples :

*   Si BAC > $1, alors le système émet et distribue de nouveaux BAC pour essayer de ramener le prix vers $1.
*   Lorsque BAC &lt; $1 le système détruit des BAC pour créer une pression haussière. La destruction n'est pas directe mais volontaire : les acteurs du système sont incités à brûler leur BAC pour un coupon (BAB) correspondant à 1 BAC + premium, qu'ils pourront collecter seulement lorsque BAC aura un cours soutenu au-dessus du dollar.

Pour plus de contexte sur cette idée de "smart contract banque centrale", vous pouvez lire mon premier article sur les Stablecoins algorithmiques :

**[L'état et le futur des Stablecoins algorithmiques](https://tokenbrice.xyz/fr/algorithmic-stablecoins/)**

#### Approches algorithmiques

*   **👍 Avantages :** Cela rend possible des systèmes sans intermédiaire central de confiance et donc ouvre la voie à des pegged-assets réellement trustless. Gouvernance communautaire possible.
*   **👎 Inconvénients / Risques :** Perte de peg soutenue ou difficulté à maintenir le peg. Possible attaque de gouvernance.

J'analyse les principales approches pour produire des Stablecoins algorithmiques dans un article dédié :

**[⚖ L'histoire de deux modèles de seigneuriage : Basis contre ESD](https://tokenbrice.xyz/fr/seigniorage-basis-esd/)**

Ainsi, des projets comme ESD, DSD, ou encore Basis Cash ont été les pionniers des Stablecoins algorithmiques. Néanmoins tous ces systèmes sont aujourd'hui un peu dans une abysse : cela fait **bien longtemps que leur "stablecoin" vaut largement moins d'un dollar**.

![bac-price-90d](/img/2021/pegged-assets/bac-90days.png "Évolution du prix de BAC sur les trois derniers mois. La situation est similaire sur ESD, DSD & MIC.")

Leurs utilisateurs sont plutôt dans l'expectative d'une V2 qui arriverait comme le messie à ramener le stablecoin au dollar.


#### Approches hybrides

*   **👍 Avantages :** Le meilleur des deux mondes ?
*   **👎 Inconvénients / Risques :** Un nouveau point potentiellement central et potentiellement intermédiaire de confiance apparaît dans le système. Vous connaissez la suite…

Face aux limites actuelles des Stablecoins algorithmiques de première génération, une autre approche a émergé avec succès : l'approche hybride. Il s'agit de systèmes algorithmiques par essence qui **incluent néanmoins une réserve en stablecoin** (différent de celui du système) utilisé pour maintenir le peg : [plus d'info ici (en anglais)](https://samkazemian.medium.com/frax-v2-algorithmic-market-operations-b84521ed7133).

Le pionnier en la matière, c'est Frax. Avec Frax, **lorsque le FRAX s'échange au-dessus du dollar le système lui-même en vend pour accumuler des USDC**. Cela permet de ramener le prix vers le bas tout en constituant une réserve en Stablecoins non exposés au système lui-même. Ainsi, si le FRAX s'échange **au-dessous du dollar, le système peut acheter des FRAX directement** sur le marché (grâce à son stock d'USDC) pour ramener le prix vers $1.

![frax-price-90d](/img/2021/pegged-assets/frax-price.png "Le stablecoin FRAX maintient son peg depuis plusieurs mois.")

Bien que cette approche a le **mérite de l'efficacité** (FRAX a très bien maintenu son peg depuis le lancement), elle réintroduit un intermédiaire de confiance dans le mécanisme. Certes, ce n'est pas une banque comme avec Tether, mais ça reste de la confiance nécessaire dans le système. Que se passe-t-il si la balance en USDC de Frax est saisie ou gelée : est-ce que le système pourrait y survivre ? Pour ceux qui ne le savent pas, oui c'est tout à fait possible techniquement parlant (et légalement).

{{< notice info >}}
Je reste très haut-niveau sur FRAX et décrit le système surtout tel qu'il était au début. De nombreuses intégrations ont été implémentées ou sont envisagées, comme la possibilité de battre le FRAX directement dans le FRAX-Tornado anonymity set (directement dans TornadoCash) pour proposer un stablecoin potentiellement plus confidentiel.
{{< /notice >}}

---

## Zoom sur le RAI de Reflexer

Pour finir cet article que j'espère instructif, je vous propose d'analyser un système novateur : Reflexer RAI. C'est une approche similaire à celle de Marker, dans le sens où l'actif à vocation stable est produit par sur-collatéralisation. Néanmoins, il apporte de nombreuses améliorations par rapport au modèle Maker :

1. **Collatéraux trustless**: Jusqu'à présent, RAI n'accepte que ETH en collatéral. Cela signifie donc que 100% des collatéraux du système ne sont pas censurables.
2. **Au-delà du dollar** : l'actif produit par le système ne suit pas le dollar (qui n'est lui-même pas vraiment stable). Le prix du RAI est déterminé par un consensus établi par le marché.
3. **Le Money God** : tout comme les Stablecoins algorithmiques, le système réagit à différents paramètres observés. Néanmoins tout comme Maker, ici ce sont les utilisateurs eux-mêmes qui frappent directement le RAI.
4. **Dégouvernance** : le token du système Reflexer (FLX), qui sera distribué aux utilisateurs a pour vocation de servir à décentraliser progressivement la gouvernance.

Pas de panique si vous n'avez pas immédiatement compris pourquoi ce système est innovant et significatif, on va explorer chacun de ces points plus en détail.


### Collatéral résistant à la censure

**Initialement, MakerDAO n'acceptait que l'Ether en collatéral**. Avec la première mise à jour significative du système — le [Multi Collateral DAI](https://makerdao.com/whitepaper/White%20Paper%20-The%20Maker%20Protocol_%20MakerDAO%E2%80%99s%20Multi-Collateral%20Dai%20(MCD)%20System-FINAL-%20021720.pdf) — de nouveaux tokens ont été acceptés. La communauté est restée perplexe face à cette décision, surtout à cause du choix des tokens acceptés. Ainsi, BAT a été l'un des premiers nouveaux collatéraux tandis que LINK, un token au volume et à la liquidité déjà largement supérieure à BAT à l'époque n'est arrivé que bien plus tard.

Au-delà de cette **priorisation difficilement compréhensible**, le nœud du problème c'est surtout que **de nombreux collatéraux désormais acceptés sont censurables**: wBTC, RenBTC, USDC, TUSD, etc. Cela réduit ainsi la trustlessness de MakerDAO puisque en fonction des moments, jusqu'à 50% de tous les DAI étaient frappés depuis des collatéraux censurables.

Le chiffre est désormais réduit, mais l'inquiétude persiste. En outre, l'addition d'un vault spécial USDC a été critiqué lors du Black Thursday pour aider le DAI à retrouver son peg — mais cela a également rendu MakerDAO encore plus dépendant de ce type de collatéraux.

Ainsi, Reflexer s'inscrit aussi comme **une réaction à cette "dérive" de MakerDAO** : pour l'instant, seulement ETH est accepté pour ouvrir un vault. Je serai surpris de voir l'équipe ou la DAO voter pour accepter des collatéraux censurables.


### Au-delà du dollar

En outre, Reflexer va bien plus loin que DAI dans sa quête de stabilité. En effet, le dollar en lui même n'a pas de valeur stable, à cause de la production continue de nouvelles unités qui entraîne une inflation : ainsi $10 000 de 1950 sont équivalent en pouvoir d'achat à presque $110 000 de 2021 (3.42% inflation par an en moyenne sur la période).

**Un actif qui a pour vocation d'être stable se doit donc de dépasser les limitations du dollar et c'est précisément ce que fait RAI** : il ne suit pas le prix du dollar. Le prix du RAI est déterminé par un pur consensus social : le système prend en compte le prix observé sur la paire ETH/RAI (market price) ainsi qu'un objectif de prix interne (redemption rate).

Il y a souvent des écarts entre les deux, ce qui crée une forme d'incitation à battre du RAI :

![reflexer-spread](/img/2021/pegged-assets/reflexer-spread.png "Ici on observe un écart d'environ 3 centimes USD")

**RAI n'est donc bien évidemment pas un stablecoin. Ce n'est pas non plus un pegged-asset.** Les mots manquent pour décrire fidèlement ce qu'est RAI mais permettez moi d'essayer. RAI c'est une abstraction sur l'ETH qui a vocation d'être plus stable que celui-ci, tout en maintenant sa trustlessness (à terme).


### All Hail the Money God

Le "Money God", c'est le terme utilisé pour faire référence à l'ensemble des règles qui régissent le système Reflexer. Le potentiel mémétique est également énorme. Pour rester assez synthétique, le Money God est clément envers ceux qui s'inscrivent dans une logique pérenne et long terme sur le protocole.

Par exemple, le mécanisme de distribution du token Reflexer, le FLX, a récemment été modifié pour mieux aligner les incitations ([plus d'info ici](https://medium.com/reflexer-labs/introducing-flx-20755214a465)). L'essentiel du changement est de mieux rémunérer ceux qui pérennisent le système, c'est à dire :

1. Déposent des ETH pour frapper du RAI
2. Déposent **tous** les RAI frappés + l’équivalent en ETH dans la pool de liquidité sur Uniswap.

Depuis le 8 Mars, 100% des FLX sont distribués à ceux qui suivent ce scénario.[ L'historique des stratégies de distribution rétroactive du FLX est ici.](https://gist.github.com/stefanionescu/e66204be990f4bc113a022341cb39186)


### Le plan de dégouvernance

Outre l'innovation technique importante sur Reflexer, à peine explorée ici, j'apprécie tout particulièrement **leur approche de la gouvernance et décentralisation du protocole**, comme décrit par Stefan l'un de ses architectes :

"Le principe de la "dégouvernance" vient de notre volonté de progressivement retirer les mécanismes de contrôle individuel (humain) du système RAI afin de lui permettre de se développer et le rendre évolutif via un consensus social."

L'équipe a établi **un plan avec des objectifs concrets et datés** pour arriver à cette fin. La première étape consiste à rendre "governance minimized" les mécanismes de liquidation et de taxation du système — seuls quelques paramètres resteront modifiables via la gouvernance (vote des FLX holders) à partir de ce moment. La date visée est le 17 Avril 2022 soit un peu plus d'un an après le lancement initial de RAI.

À chaque étape, le scénario est similaire : un mécanisme critique du système est "governance-minimized" avant qu'il soit remis entièrement sous contrôle des holders de FLX.

Vous pouvez retrouver[ le détail de ce plan ici](https://medium.com/reflexer-labs/introducing-flx-20755214a465).

Pour approfondir, n'hésitez pas à lire **[le whitepaper de RAI traduit en français traduit par PhilH et BenDuPeloux](https://github.com/reflexer-labs/whitepapers/blob/master/French/rai-french.pdf)**.

---

## Conclusion

Je suivais et attendais Reflexer depuis plus d'un an, je suis ravi d'enfin vous en parler et excusez-moi pour le délai : je voulais le mettre en contexte pour s'assurer que tout le monde saisisse l'innovation apportée par ce protocole.

{{< notice warning >}}
Cet article **ne constitue pas un conseil en investissement**. Je n'ai aucune accréditation en la matière : elles n'existent pas encore pour la DeFi.

Je discute des mécanismes de plusieurs protocoles et ce qu'ils permettent de faire ou d'envisager dans le futur. Même si je mentionne des tokens, idem : je discute de leur utilité ou tokenomics mais **jamais de leur pertinence en tant qu'investissement**. Sur ce sujet, c'est à vous de voir !
{{< /notice >}}

J'espère que cet article vous aidera à mieux comprendre l'essor des pegged-assets sur Ethereum — c'est essentiel. Il est également critique de comprendre les différents jeux de compromis associés à chaque approche : elles sont toutes potentiellement plus ou moins pertinentes, tout dépend de votre situation et de vos besoins !

Enfin, que vous soyez convaincu par Reflexer ou non, je vous invite grandement à creuser ce système, tout comme je vous invite régulièrement à explorer le fonctionnement d'Aave, de Curve ou d'Unslashed. Tous les quatre sont des systèmes très pertinents et innovants : les comprendre en profondeur vous permettra d'internaliser de nombreuses choses essentielles pour comprendre la finance décentralisée en général.

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

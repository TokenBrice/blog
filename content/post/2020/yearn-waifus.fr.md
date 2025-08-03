---
title: "Les forks de Yearn Finance : présentation de la famille des Waifus"
description: "Au-delà de son succès retentissant, Yearn Finance a inspiré de nombreux projets qui l'ont forké. Cet article le tour des forks de YFI les plus pertinents."
date: '2020-09-18T01:13:50.191Z'
categories: [DeFi, Discovery]
tags: [DeFi, Ethereum, Curve, yVault, Lending, YFI, Yearn, Yearn Finance, YFV, YFII, YFL, FARM, Harvest Finance]
image: img/2020/yearn-waifus/cover.jpg
---

À chaque jour son nouveau fork de Yearn Finance : comment les suivre ? Il n'y a pas de réponse simple, mais je pense pouvoir **vous fournir quelques éléments pour vous aider à repérer les fork de YFI à fort potentiel**. Pour ce faire, je vais couvrir trois (+1) fork YFI et essayer de mettre le doigt sur ce qui les rend intéressants.

Yearn est plus que le produit Yearn.Finance lui-même : il est devenu un modèle pour lancer un projet, parfois appelé "lancement équitable". Yearn a été le pionnier de cette méthode qui repose sur trois éléments clés :

1. **Distribution via liquidity mining** : la distribution initiale du token de la plateforme (ex : YFI) se fait par le biais de liquidity mining. Les supporters peuvent staker des tokens comme yCRV pour gagner le token de gouvernance de la nouvelle platforme.
2. **Développement communautaire** : les décisions concernant le développement du projet sont prises par la communauté des détenteurs de tokens, par le biais de votes informels et formels (on chain).
3. **Stratégies d'investissement tokénisées (Vaults)** : les projets inspirés par Yearn tentent généralement de reproduire cette caractéristique essentielle de Yearn - ils proposent des stratégies d'investissement tokenisées. Les vaults sont essentiels pour le succès à long terme du projet après la phase initiale d'extraction des liquidités. 

{{< notice tip >}}
Le terme "Vault" est utilisé pour couvrir deux réalités très différentes :
1. **"Les vault simples"**, où des tokens sont déposés pour produire un rendement. (Pas de levier)
2. **"Les Delegated Vaults "**, où une fois les tokens déposés, ils sont utilisés comme garantie (grâce à la délégation de crédit) pour emprunter des stablecoins qui sont ensuite utilisés pour produire un rendement.

Les vaults délégués sont beaucoup plus complexes à développer et à mettre en œuvre, tandis que les vaults basiques peuvent être développés plus rapidement.
{{< /notice >}}

### YFI ? Wifey ? Wai-fu ?

Dans les premiers temps de Yearn, les gens ne savaient pas très bien comment prononcer "YFI". Grâce à [une discussion sur le forum de gouvernance](https://gov.yearn.finance/t/make-yfi-pronounced-waifu/552) la communauté s'est mise d'accord sur "Wai-fu" (/waɪfu/). À partir de ce moment, il n'y a plus qu'une seule wai-fu, mais de nombreuses waifus/wifeys : les forks de YFI.

En effet, bien qu'il ait à peine quelques mois, **Yearn a déjà été forké, beaucoup**. Il y a maintenant toute une famille de wifeys construite sur une base similaire, chaque projet ajustant différents paramètres pour tenter de mieux s'adapter au cas d'utilisation envisagé. Beaucoup de ces forks étaient inutiles, mais **plusieurs ont réussi à apporter quelque chose de nouveau et d'excitant** - ceux dont nous parlerons aujourd'hui.

{{< notice note >}}
Ce contenu suppose une bonne compréhension de Yearn, afin d'approfondir le sujet, je recommande la lecture de [**mon précédent article sur Yearn**](https://tokenbrice.xyz/content/posts/2020/yearn-finance-YFI.fr.md).
{{< /notice >}}

### [DFI.Money (YFII)](http://dfi.money/)

L'une des premières discussions au sein de la communauté de Yearn a porté sur le **programme d'émission** : alors qu'il était initialement prévu pour une semaine, il a été question de le prolonger - notamment avec la [YIP 8](https://yips.yearn.finance/YIPS/yip-8) qui proposait un programme d'émissions plus long, avec une réduction de moitié chaque semaine. **Malgré le support de la communauté Yearn pour YIP-8, la proposition n'avait pas le quorum requis pour passer**, ce qui a conduit au fork YFII** - un fork de YFI la mettant en œuvre.

Ainsi **au lieu d'avoir une distribution sur une semaine, YFII a opté pour un calendrier plus long, toujours en cours**, qui a commencé le 27 juillet et se terminera le 5 octobre. Les pools proposées sont très similaires à celles de Yearn : stake du token yCRV ou stake du token Balancer pool (98 %DAI / 2 % YFII).

Au-delà de cette différenciation, YFII développe un angle intéressant avec une **forte présence en Asie** : le site DFI.Money a été rapidement traduit en chinois et bientôt dans d'autres langues. Il y a également un fort **focus sur l'interface** pour rendre l'expérience aussi facile que possible à bord.

![Vue d'ensemble des vaults de DFI.Money](img/2020/yearn-waifus/dfi-money.png)

[Vous pouvez consulter les statistiques ici](https://stats.dfi.money/).

Le 14 septembre, [DFI.Money a lancé la version 2 de ses vaults](https://twitter.com/DfiMoney/status/1305339433638531072?s=20), qui accepte l'ETH, l'USDC, l'USDT, le DAI, le TUSD, le BUSD, le HBTC et l'yCRV. Au moment de la rédaction de ce document, un total de 70 millions de dollars a été déposé dans les vaults de DFI. 

{{< notice info >}}
Cet article n'est pas un aperçu exhaustif des forks de YFI. Il existe d'autres forks de Yearn avec des changements minimes qui ne sont pas couverts dans cet article, comme le YFFI.
{{< /notice >}}

### [YFLink (YFL)](http://yflink.io/)

YFL est un autre des premiers forks de YFI. Ici, le changement est simple: **LINK a été utilisé comme le token de base du système** - celui à déposer pour la phase initiale d'extraction des liquidités. La structure des pools  était similaire à celle de YFI/YFII, mais avec LINK/aLINK.

L'objectif initial était de créer une coopérative d'investissement pour les détenteurs de LINK. YFL a été développé par 5 équipes anonymes travaillant ensemble et a été publié initialement le 7 août 2020. 

![YFL LinkSwap](img/2020/yearn-waifus/Linkswap.png)

La croissance a été rapide et le plan s'est rapidement affiné ! [YFLink travaille actuellement sur le LINKSwap](https://medium.com/@linkswapco/yf-link-ecosystem-linkswap-development-update-44f8413721c9), un créateur de marché automatisé (AMM) géré par la communauté, qui se concentre sur la sécurité et l'accumulation de valeur pour les détenteurs de LINK. 

LINKSwap explore de nouvelles idées pour accroître la sécurité des investisseurs - par exemple, la fonction RugLock, conçue pour éviter les "Rug Pull"" - lorsque les créateurs du token vident les réserves de liquidités, laissant les détenteurs avec des beaucoup des tokens qui ne valent plus rien.

### [YFValue (YFV)](http://yfv.finance/)

YFValue ajoute plusieurs autres éléments, dans le même but de fournir un service facilitant l'investissement dans la DeFi et le rendant plus accessible.

Ici, les pools étaient principalement composées à 98% ERC20-token / 2% de pools YFV Balancer et le calendrier des émissions est beaucoup plus long (5 à 20 semaines) - il est toujours en cours alors que [YFV a été lancé mi-août.](https://medium.com/@yfv.finance/yfv-bringing-true-value-to-yield-farming-bddc4edf889a) Il existe également une "seed pool" acceptant les stablecoins.

YFV a été l'un des premiers projets à offrir des possibilités de gains crédibles sur des tokens tels que BAL, YFI, BAT, REN, KNC, BTC, WETH ou LINK : cela a vraiment contribué à attirer des liquidités - il y a environ 470 millions de dollars déposés sur YFV au moment où j'écris ces lignes.

![YFV Staking Interface](img/2020/yearn-waifus/yfv.png)

Le produit principal de YFV, la Governance Vault, vient d'être [lancé le 15 septembre](https://medium.com/@yfv.finance/roadmap-update-value-contract-governance-vault-e226ad2f909e). Les détenteurs d'YFV peuvent staker leur token pour plusieurs avantages :

1. Voter dans la gouvernance de YFV
2. Un retour payé en vUSD et vETH
3. Des YFV tokens issus du programme d'émission
4. Les tokens YFV gagnés grâce à la stratégie mise en œuvre avec les fonds du Governance Vault.
5. Les tokens d'YFV ont été obtenus en rachetant YFV avec 6,8 % des bénéfices réalisés avec les autres vaults.

YFV est un projet très ambitieux. Les vaults (wETH, wBTC, renBTC) sont attendus sous peu. En plus des fermes et de la structure de gouvernance existantes, l'équipe travaille à la transition vers une collaboration AMM appelée Value Liquid. 

{{< notice note >}}
YFValue est en train de passer à VALUE (token) et Value Liquid (nom du service). Vous trouverez [plus d'informations sur ce changement de marque et cette transition ici](https://medium.com/@yfv.finance/faq-yfv-and-value-migration-af3a5a5c2190).
{{< /notice >}}

### Inspiré de YFI : [Harvest.Finance (FARM)](https://harvest.finance/)

Bien que Harvest.Finance ne soit pas techniquement un fork de Yearn, on pourrait dire que c'est un **"fork dans l'esprit".** En effet, Harvest a pour ambition de rationaliser la mise à l’œuvre de capitaux dans la DeFi & c'est un succès : Harvest abrite aujourd'hui plus de 200 millions de dollars (+200 millions) d'actifs divers qui produisent un retour stress.

L'expérience de Harvest est assez simple, tout comme pour les vaults de Yearn. **Les utilisateurs déposent des tokens dans la stratégie de leur choix pour les mettre au travail**. Par exemple, ils déposent leur DAI pour obtenir le fDAI, DAI qui exploite actuellement les retours apportés par Swerve.fi.

![Harvest Finance](img/2020/yearn-waifus/harvest-finance.png)

**Ils peuvent également fournir des liquidités sur la paire fDAI/DAI sur Uniswap, ce qui facilite l'entrée et la sortie des utilisateurs avec des capitaux plus modestes.**

Le 15 septembre, Harvest Finance a lancé un nouveau vault acceptant le wETH. La communauté est très active et engagée, et cela se voit dans la réactivité de l'équipe : pour améliorer le rendement, les exploitations de stablecoin (DAI, USDC, USDT) sont passées de la stratégie Curve à Swerve à peine 16 heures après le lancement de [Swerve](https://swerve.fi/).


### La recette pour un fork de YFI réussi ?

J'espère que ces introductions vous aideront à mieux comprendre la recette d'un fork YFI réussie. Compte tenu de la taille de l'échantillon (3+1), il est difficile de tirer des conclusions, mais permettez-moi d'essayer.

Voici comment je vois un fork YFI augmenter ses chances de survie :

1. Il **se concentre sur une communauté clairement identifiée** (ex : détenteurs de LINK pour YFLINK).
2. Les paramètres du protocole (pools, tokens, etc.) sont ajustés pour correspondre aux souhaits et aux besoins de la communauté cible.
3. **Le programme d'émission sur une semaine était un luxe que seul la première Waifu**, mère de tous les autres (YFI) pouvait se permettre. Les forks YFI réussis ont tendance à proposer un programme d'émission plus long (5-20 semaines) pour avoir le temps de fédérer et structurer leur communauté.
4. Une ferme à elle seule ne suffit pas, il y a un réel besoin **d'une vision convaincante du projet à long terme**, telle qu'un AMM (YFL/YFV), d'aller au-delà du basique pour permettre aux gens d'investir simplement (Harvest), et surtout d'une communauté motivée et dévouée pour soutenir le projet

PS : Merci à Ashitaka#4868 du [Discord Yearn Finance ](https://discord.gg/RheJ78p) pour l'image de couverture parfaitement adaptée.

### AVERTISSEMENT NÉCESSAIRE

{{< notice warning >}}
Cet article  **n'est pas du conseil en investissement** ni une recommandation d'achat d'un des tokens mentionnés ci-dessus.

**Je ne suis pas un conseiller financier. Je n'ai pas de formation formelle en matière de conseil financier, ni de certification, ou d'expérience**.
{{< /notice >}}

Je suis un natif de la DeFi et je partage mes idées, faites-en ce que vous voulez, mais réfléchissez à deux fois et évitez à tout prix les décisions impulsives : elles sont généralement les pires.

🚜 Bonnes récoltes !

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/channel/UCefQC4Y-X9MBRuYBKc2waiQ)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}
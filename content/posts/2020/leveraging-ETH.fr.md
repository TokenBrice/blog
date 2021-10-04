---
title: "🎚 Ether ou DeFi : Pourquoi choisir ?"
description: "Il est temps de mettre vos ETH au travail ! Voici des outils et conseils pratiques pour utiliser Maker afin de maintenir une exposition en ETH tout en investissant dans la DeFi."
date: '2020-08-03T01:13:50.191Z'
categories: [🌌 DeFi, 💸 Pratique]
tags: [DeFi, Ethereum, Lending, Maker, Lending, Leveraging, Minting DAI]
toc: true
tocNum: true
---

Alors qu'Ether le géant semble se réveiller, vous envisagez peut-être vos **options pour recentrer votre exposition sur l'ETH**. C'est précisément ce que j'ai examiné et exécuté ces derniers temps, et c'est le moment de partager mes retours et conseils ! 

En effet, la finance décentralisée s'emballe et les rendements sont attrayants. Cependant, **même les rendements de l'apport de liquidités (sur stablecoins) pourraient ne pas battre l'appréciation du prix de l'ETH une fois que son heure sera venue.** Donc, au lieu d'avoir à choisir, pourquoi ne pas avoir les deux ?

Avec ce seul objectif à l'esprit, la solution la plus évidente était [Maker](http://makerdao.com/). La position peut, bien sûr, être atteinte en utilisant d'autres services ; je les considère à la fin.

Voilà donc l'idée initiale : au lieu d'investir directement vers les ERC20s ou les stablecoins et de les déployer, vous maintenez une base d'ETH que vous utilisez pour générer des DAI, ensuite réinvestis par exemple dans des vaults. De cette façon, vous conservez une exposition saine à l'ETH - le compromis étant le risque supplémentaire, y compris la liquidation, qui est abordé ci-dessous.

![Maker-Leveraging-ETH-overview](/img/2020/leveraging-ETH/leveraging-ETH-fr.png "Un aperçu des principales stratégies que vous pouvez mettre en œuvre en utilisant le DAI extrait de vos positions ETH sur Maker")

## Réinvestir les DAI

Les possibilités de réinvestir votre DAI sont pratiquement infinies. Je me concentrerai donc sur celles qui sont les plus judicieuses, c'est-à-dire celles qui permettent le mieux de tirer parti de la prime actuelle sur DAI. N'hésitez pas à consulter mes précédentes publications sur les possibilités d'investissement dans les pools de liquidités avec programme d'incitations et les outils utiles pour les exploiter :
1. **[💦 Pools de Liquidité avec programmes d'incitation - La Tier List]({{< relref path="/content/posts/2020/yield-farmer-tier-list.fr.md" >}})** 
2. **[🧰 Trousse à outils du cultivateur DeFi]({{< relref path="/content/posts/2020/defi-farmer-toolbox.fr.md" >}})**.

Donc, essentiellement, pour réinvestir vos DAI ou autre stablecoins, vous avez plusieurs options, voici les grandes catégories :

* **RETOURS CLASSIQUES SUR STABLECOINS** - Rendez vos DAI productifs, avec un simple dépôt sur Compound ou Aave, ou en utilisant un optimiseur de rendement.
* **STRATEGIES STABLECOINS AVANCÉES** - Déployez vos DAI dans la Curve Ypool pour obtenir des rendements décents + des possibilités de gains supplémentaires sur vos tokens d'apport de liquidité.
* **EXPOSITION ERC20 (+LP)** - Achetez des jetons ERC20 et conservez ou achetez des jetons ERC20 et fournissez des liquidités.
* **ENCORE PLUS D'ETH** - Utilisez le DAI pour acheter plus d'ETH. Peut être potentiellement répété pour plus d'effet de levier (ATTENTION). Cette méthode est évidemment la plus intéressante lorsque vous attendez une action positive sur le prix de l'ETH.

Le DAI se négocie actuellement à une prime ($~1,03), certaines stratégies sont meilleures que d'autres pour exploiter l'impact de cet écart. Je les détaille dans la dernière section.

### Gestion des coffres-forts : Comment augmenter l'efficacité du gaz ?

Lorsqu'il s'agit de s'assurer que vous ne vous brûlez pas votre capital sur les coûts en gaz, j'ai déjà couvert plusieurs outils essentiels que nous ne détaillerons pas à nouveau, tels que [Zapper.Fi](http://zapper.fi/), ou [ParaSwap](http://paraswap.io/) pour certains échanges de jetons. Aujourd'hui, je veux parler des services qui sont utiles pour gérer les positions sur Maker.

1. En interagissant avec vos coffres, vous vous trouverez à effectuer des séries de transactions (déposer ETH -> mint DAI -> faire quelque chose avec le DAI). Pour réduire vos coûts de gaz, vous pouvez **utiliser [FuruCombo](https://furucombo.app/) pour construire votre série d'opérations et l'exécuter en une seule transaction.**
2. Vous pourriez avoir besoin d'un "capital flash" pour fermer une position quelque part et la rouvrir ailleurs. Si c'est le cas, un flash loan Aave vous sera utile. Et voici la meilleure: **les flash loans sont dispos sur FuruCombo!**

![Collateral swap using Furucombo](/img/2020/leveraging-ETH/furucombo.png "Échange de collateral sur Maker (ETH->USC) en utilisant FuruCombo + Flash Loan")

Gardez à l'esprit qu'en ces temps de prix élevé du gaz, chaque interaction est coûteuse. Pour réduire l'impact du gaz sur votre stratégie, essayez de minimiser la quantité d'opérations que vous effectuez - FuruCombo est tout simplement étonnant pour cela !

Si vous avez de nombreuses coffres à fermer/ouvrir, vous pouvez aussi attendre une période opportuniste pour le faire, où le coût du gaz est faible. Les soirées du week-end (heure d'Europe) sont généralement les meilleures.

## 🚨 LISEZ SVP : Comment ne pas se faire liquider ?

### Comprendre le mécanisme de liquidation de Maker

Lorsque vous êtes liquidé, (une partie de) votre capital est saisie pour couvrir votre dette. **L'existence de la liquidation sur Maker signifie que vous pourriez perdre potentiellement une grande partie de vos ETH utilisé comme collateral** si vous êtes négligent.

Voici mes conseils et recommandations pour éviter que cela ne vous arrive :

**Si vous commencez tout juste avec l'effet de levier, maintenez un ratio de collatéralisation très sain**. Je recommanderais > 300 % pour les nouveaux utilisateurs, simplement pour avoir l'esprit tranquille pendant votre phase de découverte.

**Ne mettez pas tous vos œufs dans le même panier** : sur Maker, vous pouvez ouvrir autant de coffres que vous le souhaitez. Si vous ne voulez pas ouvrir des centaines de coffres pour maîtriser les coûts du gaz, vous pouvez aussi envisager de diviser vos coffres pour ne pas faire courir le même risque à toutes vos ETH et pouvoir gérer les coffres plus progressivement au fur et à mesure de leur croissance.

**Gestion facile des coffres Maker** : si vous souhaitez une approche moins stressante, vous pouvez utiliser [DeFiSaver](https://defisaver.com/) pour vous assurer que votre position soit automatiquement maintenue à un certain ratio (Save).

![Automatisation de la gestion des coffres Maker avec DeFi Saver](/img/2020/leveraging-ETH/defisaver-automation.png "Automatisation de la gestion des coffres Maker avec DeFi Saver")

### Gestion avancée des coffres Maker

Si vous avez plusieurs coffres, vous pouvez utiliser un outil pour redistribuer le capital entre elles en une seule transaction, toujours avec FuruCombo :
```
Mint des DAI sur le Coffre-1 (actuellement en sécurité) 
> Brûler la dette DAI de le Coffre-2 pour réduire les risques
```

Grâce à un flashloan, vous pouvez même fermer complètement un coffre "dans" une autre chambre forte par exemple :
```
Flashloan DAI (= dette de le Coffre-1) 
> Brûler les DAI sur le Coffre-1, pour libérer vos ETH
>> Dépôt des ETH dans le Coffre-2 (celle que vous gardez) 
>>> Mint DAI sur le Coffre-2 
>>>> Rembourser le flashloan.
```

**Faites attention à ce que vous faites avec les DAI que vous créez : c'est une dette**. Si vous investissez dans quelque chose de stupide et vous faites massacrer en même temps que le prix de l'ETH se déprécie, vous pouvez mettre l'ensemble de la position en danger et perdre de nombreux ETH.

## Pourquoi Maker est le meilleur service pour tirer parti de l'ETH en ce moment

J'ai décidé de centrer cet article sur Maker uniquement, considérant que l'angle d'attaque est de tirer parti de l'ETH et que Maker est actuellement la meilleure plateforme pour y parvenir, ainsi que probablement la plus sûre (en tout cas la plus ancienne). Voici mes trois principales raisons :

1. **Ça marche** - Maker vous permet de conserver une exposition à l'ETH tout en générant un DAI supplémentaire à réinvestir - ça colle parfaitement au but initial.
2. **La coût de l'emprunt est actuellement de 0** (sur l'ETH) - il ne vous en coûte que du gaz pour ouvrir une position sur Maker. (Stability Fee /ETH = 0)[^1]
3. **Premium DAI -** Le DAI se négocie fréquemment à 1,02-1,03 $, ce qui signifie que la frappe du DAI peut entraîner un profit instantané de 2-3% sur les montants réinvestis (plus d'informations à ce sujet plus loin - section prime DAI).

Veuillez garder à l'esprit que **c'est la situation MAINTENANT**, dans plusieurs semaines il pourrait y avoir de meilleures options pour de telles positions, comme Aave met en place ses nouveaux tokenomics par exemple. Une position similaire pourrait déjà être atteinte aujourd'hui en utilisant Compound, mais il ne semble pas rentable de le faire maintenant (vs Maker).

## A qui s'adresse cette stratégie ?

Comme il s'agit d'une stratégie assez flexible, **elle peut être utilisée par pratiquement tous ceux qui possèdent des ETH et cherchent un moyen de la mettre en œuvre.** Permettez-moi toutefois de mettre en évidence quelques cas d'utilisation qui devraient vous donner des idées :

1. Vous êtes entré sur les marchés récemment (2019) et vous avez fait des bénéfices, mais pas vraiment sur l'ETH. Alors que vos investissements sur les ERC20s sont à la hausse, vous pourriez craindre de ne pas réaliser de bénéfices sur l'ETH. Pour augmenter votre exposition à l'ETH, vous pourriez solder certaines de vos positions pour de l'ETH, ouvrir une position Maker et rouvrir jusqu'à ⅔ des positions ERC-20 fermées.
2. Ces derniers temps, vous avez réalisé des gains intéressants sur les stablecoins, mais même les meilleurs rendements ne peuvent pas battre un géant qui se réveille. Vous pouvez envisager d'acheter ETH avec vos stablecoins, pour ensuite ouvrir un coffre-Maker et rouvrir une partie de votre position sur les stablecoins - vous conservez une partie de vos rendements tout en ajoutant une exposition au prix d'ETH.

### Exploiter la prime DAI

Pour conclure, examinons les meilleures options si votre objectif est de tirer le meilleur parti de la prime DAI actuelle - quel est son impact le plus important ?

Il est évident que c'est très bien pour les emprunts à long terme de l'ETH. En effet, si le DAI se négocie à 1,03 $, il est plus efficace d'acheter de l'ETH depuis du DAI.

Si vous envisagez d'investir dans le pool Curve y, je vous recommande de considérer de passer à 100 % par DAI. Vous économiserez ainsi massivement sur les swaps qui ne sont pas nécessaires (+ moins de transactions de dépôts et d'approval ). En plus de ces économies, le fait d'investir à 100 % dans le pool Curve y en DAI a généralement un effet positif sur les prix.

Actuellement, il se situe à environ 1,5 % pour 5 000 DAI : c'est 1,5 % de profit instantané lorsque vous entrez dans la position, ce qui est assez attrayant, non ? 


![Curve DAI Premium](/img/2020/leveraging-ETH/curve-dai-premium.png "Slippage positif (1.5%) en entrant dans la pool Y 100% depuis DAI")

En fonction de votre préférence en matière de risque et de votre capital, vous pouvez choisir le moment de votre entrée. J'ai réussi à obtenir un bonus positif jusqu'à ~ 3,5 % en entrant dans le ypool, alors attendre peut valoir le coup !

Merci à Grégoire pour la relecture de ce contenu et à [Jimmy](https://twitter.com/jimmyragosa) pour avoir suggéré [DeFiSaver](https://defisaver.com/), essayez-le !

## C'est à vous de jouer

1. Vous pouvez **[mettre votre ETH au travail](http://oasis.app/)**, sans les vendre ! Essayez avec une premier coffre-Maker sûre (>300%).
2. Vous aimez ? Commencez à explorer d'autres stratégies, mais n'oubliez pas de tenir compte du coût du gaz. Utilisez **[FuruCombo](https://furucombo.app)** pour créer des flux plus complexes efficacement.
3. Vous utilisez de plus en plus les coffres Maker ? C'est peut-être le bon moment d'envisager **[DeFiSaver](https://defisaver.com/)** pour réduire vos risques et gérer vos coffres sans stress.

Et à n'oubliez pas, à tout moment, si vous avez besoin d'aide et souhaitez échanger avec plus de 1100 de vos pairs, en français, ça se passe sur le **[🇫🇷 Groupe Telegram DeFi France](https://t.me/defifrance)**.

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/channel/UCefQC4Y-X9MBRuYBKc2waiQ)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}

[^1]: [Le Stability Fee vient de passer à 0](https://twitter.com/MakerDaiBot/status/1290243544670785536) pour tous les collaterals.

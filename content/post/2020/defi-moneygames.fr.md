---
title: "🧭 DeFi Moneygames: Comment comprendre le risque et éviter les pertes ?"
description: "Un peu de contexte sur les DeFi moneygames (YAM, PASTA, BASED, etc.) pour être en mesure de comprendre les risques encourus par les joueurs et comment les minimiser"
date: '2020-08-26T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Yield]
tags: [DeFi, Ethereum, Staking, Memecoin, Foodcoin]
image: /img/2020/defi-moneygames/cover.png
difficulty: "intermediate"
url: defi-moneygames
aliases:
  - p/defi-moneygames
---

Les moneygames alimentaires font fureur dans la finance décentralisée. Aujourd'hui, je voulais écrire un petit article pour les mettre en contexte et donner quelques conseils à ceux qui le souhaitent. Je ne porterai pas de jugement moral sur ces projets, je vous laisse le soin de le faire.

Le lancement de Yearn Finance le mois dernier a probablement été l'événement le plus important de l'année pour DeFi. Si vous ne connaissez pas du tout Yearn, je vous recommande de lire mon article sur le sujet pour vous rafraîchir la mémoire - il vous sera utile de mieux comprendre celui-ci : **[YearnFinance - La DeFi avec pilote automatique ?](https://tokenbrice.xyz/fr/yearn-finance/)**

Le lancement du token de Yearn, YFI, était très innovant à l'époque : 100 % de l'offre a été distribuée à des utilisateurs fournissant des liquidités sur différents pools liés au protocole. Ce schéma de lancement est maintenant devenu un modèle reproduit par d'innombrables projets qui ont vu le jour à la suite de l'immense succès de Yearn : YFII, YFL, YAM, SHRIMP, PASTA, BASED, etc.

En plus de cette pierre angulaire de la "coopérative de farm" fournie par Yearn, de nombreux projets ajoutent une touche de tokonomics à leur actif de base, dans l'espoir de le rendre plus mémorable et engageant. Voici les suspects habituels :

1. **Un modèle déflationniste** (c'est généralement stupide) - **Fuyez !**. Exemple : PASTA. (RIP)
2. **Un mécanisme de rebase** (cela peut devenir intéressant - augmente l'asymétrie d'information). Ce qui compte ici, c'est de trouver un objectif de prix pertinent et de s'assurer que le code de rebasage n'est pas défectueux / n'entraîne pas de problèmes avec d'autres parties du protocole telles que les pools de liquidité (Hello YAM v1). Malheureusement, cela contribue également à transformer le jeu en une situation de type "ponzi" où des investisseurs inexpérimentés se font piller par des agriculteurs expérimentés - les mécanismes de rebase rendent le calcul des rendements délicat.
3. **Des mécanismes à base sociale**, tels qu'un bonus quotidien/hebdomadaire pour les meilleurs détenteurs de X, comme [TACO](https://twitter.com/Taconomics101), ou des récompenses doubles tous les mardis parce que... Taco Tuesdays !
4. Pour certains, la **principale valeur découle de l'angle communautaire** plutôt que de la tokonomics, comme pour [Shrimp](http://shrimp.finance/) qui ambitionne de devenir une sorte de meta moneygame en permettant la création d'un pool avancé (avec incitation en SHRIMP) par quiconque.

{{< notice tip >}}
Si vous voulez un fil conducteur pour filtrer le bruit, **la gouvernance est très généralement parlante. C'est une nécessité et, en fin de compte, un facteur clé dans la réussite de tous ces projets**. Regardez le type de décisions qui sont prises, quel est le processus, et qui façonne le projet, etc.
{{< /notice >}}

---

Voilà le concept de base, si simple et si prêt à l'emploi que nous pourrions créer ensemble un moneygame pour le plaisir :

Imaginez $WINE. Vous le cultivez en verrouillant des tokens DeFi pendant la première semaine. Ensuite, une pool WINE/ETH sera incitée pour plus longtemps (il y a un fort potentiel pour que cela devienne une pool de dumping, plus d'informations à ce sujet ci-dessous).

WINE est déjà très memable et possède un émoji, bon point de départ ! Mais il nous faut plus, il nous faut du fun et de la matière, pourquoi pas :

1. Le plus grand détenteur de WINE a 20 % de chances de se "saouler" tous les jours. Si cela se produit, il sera un ivrogne généreux qui donnera 20 % de tout ses WINE à 100 adresses actives choisies au hasard.
2. Ne soyez pas trop éméchés non plus : chaque transaction de WINE a 1% de chance d'envoyer 50% de la valeur transférée au contrat de récompense à la place - ce qui augmente les récompenses pour les farmers.

Ces mécanismes ne sont pas du tout inspirés, mais ils vous donnent une idée de la facilité avec laquelle ces concepts peuvent être mis en place. Ils peuvent également être mis en œuvre très rapidement grâce à des blocs de code (tels que les contrats de staking) désormais devenus standards (tels que le contrat de staking de Synthetix).

{{< notice warning >}}
$WINE n'existe pas. N'achetez pas $WINE. Achetez du vin ! 🍷
{{< /notice >}}

---

Assez pour le contexte et la théorie - je pourrais me plonger dans les dimensions communautaires du jeu dans le prochain article. Mais pour aujourd'hui, permettez-moi de vous faire partager quelques connaissances pratiques acquises en suant mes gwei :


### Conseils pratiques pour essayer les moneygames

Commençons par les rappels : **n'oubliez pas de prendre en compte les pris en gaz !** Jouer à moneygame implique au moins 1/ stake, 2/claim, 3/vente. Souvent, le stake ne se fait pas directement avec un token basique - mais avec un token qui correspond à une part dans une pool de liquidité - ce qui implique des transactions supplémentaires.

**Deuxièmement, n'achetez jamais un token d'un moneygame**. L'achat d'un tel token comporte un risque incroyable : vous êtes contre une armée de personnes qui les gagnent gratuitement et qui peuvent être impatientes de les vendre.

Enfin, soyons un peu plus pratiques en examinant des exemples réels pour expliciter le scénario de risque de chaque type de pool :


#### NIVEAU = 1 - STAKING BASIQUE - OK SI LE CODE EST SAFU

Avec ces pools, vous mettez en jeu un token DeFi (généralement MKR, COMP, SNX, LEND, wETH et YFI) pour gagner le token du moneygame, YAM par exemple.

Le risque est réduit au minimum : si vous pouvez comparer le code du contrat de staking avec un code existant pour vous assurer qu'il n'y a pas de manigances. Comme vous ne faites que staker et ne fournissez pas de liquidités, vous ne prenez aucun risque économique. Tant que vous pouvez garantir la sécurité du protocole - votre capital n'est pas mis en danger.

Au-delà de ce point (SAFU confirmé), le principal risque que vous prenez est que le token que vous gagnez pourrait ne plus avoir de valeur au moment où vous en aurez assez pour vous en débarrasser. Tenez-vous en à des projets raisonnables pour éviter un tel scénario connu sous le nom de "spirale de la mort" - lorsqu'un token-mème entre dans la phase finale de son existence :

![defi-moneygames-PASTA-deathloop](/img/2020/defi-moneygames/pasta-deathloop.png "La fin de PASTA a été assez abrupte.")


#### NIVEAU = 2 - POOLS 98%/2%

Ces pools sont généralement plus délicates, car elles impliquent de fournir des liquidités à sur un échange décentralisée. Souvent, elles sont fortement orientées vers un token solide et réputé : par exemple, le pool YFLink 98% aLINK / 2% YFL.

Ici, **vous êtes confrontés à un nouveau type de risque : les pertes impermanentes**. Les IL sont plus importantes lorsque les deux actifs impliqués dans le pool évoluent rapidement dans des directions opposées, en termes de prix. Les pools 98/2% ont leur propre catégorie car elles sont un peu plus sûres, bien qu'elles ne soient pas totalement immunisés contre l'IL.

![defi-moneygames-YFV](/img/2020/defi-moneygames/yfv.png "YFV est un autre moneygame qui suit ce modèle de pools 98/2")

#### NIVEAU = REK'T - LES "DUMPING" POOLS

Ces pools sont les plus dangereuses. Je conseille à tous ceux qui ont besoin de conseils de les éviter tout simplement - le jeu est trop risqué pour être joué. Le pool PASTA yyCRV / PASTA Uniswap est un bon exemple de pourquoi.

Disons-le comme ceci : si certains peuvent cultiver des PASTA essentiellement gratuitement en verrouillant quelques tokens DeFi - pourquoi ne pas les utiliser pour acquérir des yyCRV, la machine à faire de l'argent la plus puissante de l'industrie ? C'est précisément ce qui s'est passé.

Dès que le pool d'incitation a été lancé, les agriculteurs de PASTA ont fait un gros dumping pour réclamer ces précieux jetons yyCRV mis en vente. Pourquoi ne l'auraient-ils pas fait ? Le prix du PASTA a chuté d'environ 1 à 0,04 dollar, détruisant tout profit réalisé par ceux qui s'étaient engagés dans les pools, en plus de la perte de leur précieux yyCRV.

Qu'est-ce qui fait qu'un pool est considéré comme un pool de dumping ? **Permettez-moi d'être super explicite ici pour m'assurer que vous n'allez pas faire hara-kiri avec vos précieux tokens** :

1. **Le dumping pool est généralement de 50/50** : 50 du mème shitcoin, 50 d'un token solide comme ETH, wetH ou yyCRV.
2. **Le budget d'incitation de cette pool est généralement bien plus élevé que les pools de stake basiques.** Sinon, comment attirer les plebs ? Bien sûr, ce profit est difficile à réaliser car la plupart des capitaux sont perdus pour l'IL, et les rendements sont gagnés dans le foodcoin qui peut entrer dans la spirale de la mort.
3. **La "Dumping Pool" est généralement lancée quelques jours après les premières**, et dure plus longtemps. En effet, il faut donner quelques jours aux agriculteurs pour qu'ils puissent s'accumuler.

Ne me croyez pas, je ne suis qu'un simple agriculteur - suivez une légende comme [DegenSpartan] (https://twitter.com/DegenSpartan/status/1296619171984232448?s=20) - il est assez gentil pour annoncer publiquement ses dumps (peu de temps) après qu'elles aient commencé.

Bonne chance, et souvenez-vous d'une chose si vous venez de rejoindre l'espace : les moneygames se jouent contre d'autres utilisateurs expérimentés ayant potentiellement des années d'expérience en matière de crypto.

{{< notice note >}}
La plupart sont des jeux à somme nulle : aucune valeur n'est créée, c'est juste un mécanisme complexe de transfert de valeur à 3 ou 4 niveaux.
{{< /notice >}}

**Avez-vous assez confiance en votre expérience pour vous aventurer dans la fosse aux lions ?** Si ça n'est pas le cas, je vous recommande chaudement d'éviter toutes les pools au delà du premier type (staking simple).

---

{{< notice info >}}
Je ne suis pas un conseiller en investissement, quel que soit leur nature : vous prenez vos propres décisions. Je n'ai aucune formation classique et ne possède aucune certification reconnue en la matière. Je partage simplement mon expérience personnelle avec pour but de vous aider à mieux comprendre la finance décentralisée.

**Je ne suis pas responsable de <u>VOS DÉCISIONS D'INVESTISSEMENT</u>**, ni de leurs résultats. La phrase précédente s'applique tout aussi bien pour des lambos que votre potentielle banqueroute.
{{< /notice >}}

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/channel/UCefQC4Y-X9MBRuYBKc2waiQ)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}
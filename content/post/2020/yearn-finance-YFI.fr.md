---
title: "YearnFinance - La DeFi avec pilote automatique ?"
description: "Retour sur le lancement de Yearn Finance V2, l importance de YFI et les raisons pour lesquelles ce moment a marque la DeFi."
date: '2020-08-11T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Yield]
tags: [DeFi, Ethereum, Lending, Aave, Compound, Curve, Leveraging, Yearn]
series: yearn
series_order: 1
image: /img/2020/yearn-finance-YFI/wifeys.jpg
difficulty: "beginner"
url: yearn-finance
---

Il y a quelques semaines, la sortie de Yearn v2 et le lancement du jeton YFI (prononcé "Waifu") ont ébranlé le monde de la finance décentralisée. En effet, toute la recette était là : Yearn est comme un conseiller automatique, il vous aide à économiser et à faire fructifier un capital - évidemment l'un des cas d'utilisation les plus en vogue.

Plus que le produit lui-même, c'est son fondateur André Cronje qui  a été intrumental pour définir la "culture" Yearn. **Son choix d'ouvrir complètement la gouvernance**, a dynamisé une communauté qui s'est rapidement fédérée autour du projet.

Avec cette article, je veux partager aujourd'hui quelques indications pour comprendre pourquoi Yearn a vu le jour, comment il fonctionne et pourquoi il est important.

## Qu'est-ce que Yearn ?

La première version de Yearn a débuté par une simple promesse : elle vous permettait d'obtenir le meilleur taux d'intérêt disponible à tout moment sur un stablecoin donné. En effet, comme il existait de plus en plus d'options pour prêter des Stablecoins (Compound, Aave, dYdX, etc.), l'optimisation du rendement est rapidement devenue essentielle.

Yearn v2 a déjà mis sur le marché un nouveau produit, les yVaults : ils vont au-delà de l'optimisation du rendement (rééquilibrage de Stablecoins entre plusieurs plateformes de prêt) pour offrir plus de retours. Voyons comment cela fonctionne :

### Perspective de l'utilisateur final : Déposer, attendre, l'argent monte

Avant d'entrer dans les détails, voici comment cela fonctionne pour un utilisateur final :

1. Vous possédez un token supporté dans les yVaults, tel que LINK
2. Vous pouvez déposer votre LINK dans le yLINK vault pour les mettres au travail. L'entrée et la sortie des vaults sont optimisées pour être doux en gaz (généralement ~2-3 $).
3. Lorsque vous avez terminé, vous sortez du vault. 0,5% de la valeur **totale** est prélevé par le système pour couvrir tous les frais.

Si le temps passé dans la vault est suffisant pour compenser le coût de sortie, les investisseurs sortent avec un bénéfice payé sur le jeton qu'ils ont entré (ex : plus de LINK).


{{< notice info >}}
Note : Les yVaults sont encore très expérimentaux. Assurez-vous que vous savez dans quoi vous vous engagez. André a une approche assez intéressante, comme le montre sa biographie sur Twitter ["I test in prod"](https://twitter.com/AndreCronjeTech/status/1291252150635560960?s=20).
{{< /notice >}}

****

### Que se passe-t-il sous le capot ?

Les yVault sont étonnants parce qu' **ils abstraient une immense complexité pour les utilisateurs,** et le font mieux que la plupart d'entre nous. Pour en revenir au vault yLINK, voici ce qui se passe pour produire les rendements :

1. **Les LINK sont déposés sur Aave** (Délégation de crédit) et utilisés comme garantie pour ouvrir des positions. Les positions sont maintenues dans une fourchette sûre grâce à un mécanisme de sécurité financé sur une fraction des rendements totaux.
2. **Les Stablecoins sont empruntés et mis en œuvre** pour fournir un rendement. La dernière stratégie repose sur le pool Balancer mUSD/USDC MTA.
3. Tous les rendements réels de la partie stable de la position (les Stablecoins gagnés au-dessus de la dette) sont **vendus pour des LINK**, ce qui augmente les rendements effectifs de l'ensemble de la position (-> plus de levier pour emprunter plus).

Le point critique des yVault est que **ils exploitent les synergies de la DeFi pour fournir des rendements attractifs**. Ils sont conçus pour être flexibles dans l'allocation de leur capital - de sorte qu'ils peuvent facilement être réaffectés pour suivre une stratégie différente avec de meilleurs rendements.

Chaque vault a une stratégie propre. Voici un graphique explicatif soigné pour expliquer la stratégie du vault yCRV :

![Explication de la stratégie du vault yCRV](/img/2020/yearn-finance-YFI/yCRV-vault.png "Explication de la stratégie du vault yCRV")

Je vous laisse donc creuser le graphique et rejoindre le [Yearn Discord](https://discord.gg/HFK5uea) si vous êtes intéressé.

## Pourquoi Yearn est unique

Yearn a dynamité la DeFi. Il faut bien comprendre que Yearn a été rendu possible par les développements survenus au cours de l'année dernière. Yearn exploite les synergies entre plusieurs "DeFi legos". Sans aller trop loin, voici les principaux :

1. **Aave a récemment lancé la fonction de délégation de crédit**, permettant à un smart contract d'emprunter pour le compte d'un autre smart contract. Cette fonctionnalité était nécessaire pour que les yVaults fonctionnent comme ils le font maintenant, car ils permettent la première partie de la plupart des stratégies - obtenir un effet de levier [^2].
2. DEX & Automated Market Makers - en particulier **Curve.fi**, une dépendance évidente pour le vault yCRV.
3. Le **dynamisme global des marchés des Stablecoins**, grâce à de nouveaux entrants tels que mStable ou le lancement du token COMP.

Yearn est un exemple parfait de la composabilité de DeFi [^3].


### Construire le moins possible et assembler des legos

Pourquoi je me concentre sur ce sujet ? Parce qu'en tant que personne travaillant dans l'espace DeFi depuis deux ans, je peux vous dire que la plus grosse erreur opérationnelle que je vois TOUT LE TEMPS - est simple : **des équipes qui réinventent la roue - en reconstruisant ce qui existe déjà et marche bien**.

Je pense que les projets DeFi (comme la plupart des startups) gagneraient énormément à essayer de réduire activement le périmètre du travail qu'ils entreprennent - voici deux questions efficaces qui devraient être posées plus souvent :

1. "Quelle est la valeur unique de notre produit ?"
2. "De quoi avons-nous besoin pour la délivrer ? Pouvons-nous assembler des solutions existantes pour y parvenir ?"

La conception structurelle de Yearn démontre une volonté d'identifier les projets DeFi à fort potentiel et d'exploiter leurs synergies. En bref, en **assemblant plusieurs legos DeFi d'une nouvelle manière,** Andre a efficacement créé un tout nouveau scenario d'utilisation, voir un nouveau sous-ensemble de toute l'industrie.


## Le premier projet DeFi 100% communautaire

Ce titre n'est pas putaclic, je m'y tiens car il y a des arguments pour le défendre !

Tout d'abord, il faut souligner que **Yearn a été un produit fonctionnel traitant des volumes importants pendant plusieurs mois avant le token YFI**. Maintenant, vous pouvez en ajouter :

1. 100% des tokens distribués à la communauté
2. Utiliser une nouvelle approche d'extraction de liquidités, pertinente pour le produit (pool yCRV).
4. La communauté s'est rapidement mobilisée et est en plein essor avec des idées bien articulées.
5. André a abandonné le contrôle des principaux contrats régissant le service, au profit d'un multisig avec des acteurs réputés de l'espace [^4].

{{< notice note >}}
Si je considère et apprécie un processus de gouvernance ouvert comme un net positif, du moins à long terme, c'est aussi un risque - et **c'est généralement ainsi que les gens du secteur le perçoivent.** Une gouvernance ouverte peut être détournée dans une direction qui ne correspond pas au meilleur intérêt du projet.
{{< /notice >}}

### DeFi/Web3 -> Les Communautés régentent les Marques

Vous n'êtes peut-être pas encore à bord, mais pour moi, construire et développer des communautés - c'est essentiellement ma vie. Au fil des ans, je n'ai pas trouvé de sauce secrète, mais j'ai découvert une vérité évidente : **Communauté >> Marque**.

Dans le cas de DeFi, j'ai hâte de voir le **clash des marques** auquel nous allons assister :

* D'une part, les sociétés "corpo" financées par le capital-risque ont tendance à manquer de personnalité et ont plus de mal à soutenir des communautés organiques dynamiques.
* D'autre part, **un projet communautaire est une histoire qui s'écrit tous les jours**, et quand il s'agit de la "marque" Yearn, nous la voyons se développer rapidement : le swag est déjà là !

![Yearn Finance Swag](/img/2020/yearn-finance-YFI/yearn-swag.png "Le swag Yearn n'a mis que quelques jours à arriver !")


## Ressentir le Yearn

Yearn est bien plus que les yVaults ! J'ai concentré cet explicatif sur eux pour plus de clarté, mais il y a plusieurs autres produits Yearn en cours de développement. Sans trop s'y attarder, en voici quelques uns qui sont prometteurs :

* **[yBorrow](https://yborrow.finance/)** - une interface de délégation de crédit généralisée utilisant Aave.  Cela permettra à n'importe qui d'accéder à des chambres vaults comme yCRV à partir d'un token ERC-20 de leur choix.
* ySwap : un nouveau market maker automatisé
* Une mystérieuse solution à effet de levier pour optimiser les retours sur Stablecoins


### La boîte à outils Yearn

Voici quelques outils et ressources développés par la communauté qui s'avèrent très utiles si vous explorez ou utilisez Yearn :

* **[LearnYearn](https://www.learnyearn.finance/)** : Un wiki complet sur Yearn fréquemment mis à jour !
* **[FeelTheYearn](https://feel-the-yearn.vercel.app/)** : Une page simple pour connaître l'état actuel des yVaults : voir les actifs déposés, ainsi que comment ils sont déployés pour générer un retour.
* **[YCosystem](https://ycosystem.info/)** : Un agrégateur communautaire pour trouver tous les liens utiles, des docs aux YIPs, ou encore l'endroit où acheter le swag Yearn !

Que vous soyez intéressé ou non par Yearn, je vous invite à lire le  [forum de gouvernance](https://gov.yearn.finance/) - vous êtes à jamais invité à lire et à participer aux discussions qui façonnent Yearn. Cette fois, il n'y a pas de VC, pas de BS - juste un DAO et un homme-armée nommé [Andre Cronje](https://twitter.com/AndreCronjeTech).


### La famille des Wifeys

Enfin, il serait malhonnête de couvrir Yearn/YFI sans mentionner que YFI a déclenché tout un mouvement - il y a maintenant des dizaines de forks, plus ou moins crédibles. En effet, Yearn est open source et Andre a lui-même invité les gens à le forker, en étant créatif[^5]. Alors que les premiers ne faisaient que "bifurquer les mineurs", en ajustant quelques paramètres, on constate aujourd'hui des approches plus créatives.

Certaines communautés font appel à YFI pour créer leur propre système d'investissement collectif, avec une vision à plus long terme. Ce n'est que le début, mais je pense que nous assisterons à un développement fascinant dans cet espace. Je pense que nous verrons des communautés se réapproprier certaines parties, voire l'ensemble du système d'YFI - vous vous souvenez de la famille Wifeys tout à l'heure ?

Ça a déjà commencé ! Je suis de près [YFLink](https://medium.com/yflink/the-idea-of-yflink-is-born-aa520921a4a3), un fork de YFI ajusté au besoin de la communauté LINK. Pour l'instant, cela ressemble plutot à une coopérative de liquidity mining mais à terme cela pourrait devenir le premier node de staking communautaire pour LINK.

J'ai hâte de voir Yearn grandir !

{{< notice warning >}}
Les yVaults sont un produit DeFi innovant intégrant de nombreux autres services - les risques de défaillance sont donc multipliés. Je ne suis pas un conseiller financier - vous prenez vos propres décisions.

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

[^2]: [Voici Stani (le PDG d'Aave) qui vous explique pourquoi c'est si important](https://twitter.com/StaniKulechov/status/1280500969986498561?s=20)
[^3]: André lui-même est [le premier à reconnaître](https://twitter.com/AndreCronjeTech/status/1290845154430025731?s=20) ce qui a rendu Yearn possible et l'importance de la composabilité.
[^4]: La gouvernance du protocole est maintenant entre les mains du détenteur de YFI. L'accès aux principaux contrats est détenu par un multi-sign, [André n'a pas de clé](https://twitter.com/AndreCronjeTech/status/1285427748761198594?s=20).
[^5]: ["Si vous clonez YFI (vous êtes les bienvenues), changez au moins quelques paramètres afin que nous puissions apprendre de l'experience. Répéter la même chose en boucle n'est pas drôle."](https://twitter.com/AndreCronjeTech/status/1289959986190147585?s=20)
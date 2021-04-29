---
title: "🌽 Livre de recettes pour les marchés d'actifs DeFi"
description: "Les marchés d'actifs comme Aave ou Alchemix sont des outils essentiels en DeFi. Cet article explique et illustre quelques stratégies pour tirer parti des différentes options qu'ils offrent."
date: '2021-04-29T01:13:50.191Z'
categories: [🌌 DeFi, 🔮 Découverte]
tags: [DeFi, Ethereum, Finance décentralisée, Marchés Monétaires, Aave, Curve, Liquity, Mimo Capital, Alchemix, Aave, Polygon, Liquidation]
toc: true
tocNum: true
url: recettes-marchés-d'actifs
---

Sur ce blog, je discute fréquemment des marchés monétaires ou marchés d'actifs en DeFi. Fondamentalement, ils vous permettent de **prêter et d'emprunter des tokens**. Ces deux actions sont devenues comme **des verbes de la DeFi** : ils sont mobilisés directement ou indirectement dans quasiment toutes les stratégies.

Ainsi, bien qu'il soit crucial de comprendre les protocoles que vous utilisez et surtout **les différents [risques encourus sur les marchés monétaires]({{< relref path="/content/posts/2021/money-market-risks.fr.md" >}})**, je vous propose aujourd'hui de nous concentrer plutôt sur le pourquoi et le comment :

1. Quelles stratégies peut-on mettre en place en utilisant les marchés d'actifs ?
2. Comment concrètement les déployer ?

Nous allons donc décortiquer différentes "recettes" pour tirer parti des marchés d'actifs. Prenez ces recettes comme **des inspirations pour développer vos propres stratégies**.

![recettes-marché-d'actif-cover-tokenbrice](/img/2021/money-market-recipes/recettes-marché-d'actif-cover-tokenbrice.png)

{{< notice warning >}}
Cet article ne constitue pas du conseil en investissement : je ne suis pas habilité à en dispenser. Plutôt que de reproduire mécaniquement les stratégies présentées en exemple, je vous invite surtout à chercher à en comprendre la démarche.
{{< /notice >}}

---

## Pari avec effet de levier sur un marché d'actif via le marché d'actif lui même

Les marchés d'actifs ont tous un token associé, par exemple le token AAVE pour Aave. Il sert généralement pour la gouvernance du protocole et permet parfois également de capturer une partie de la valeur que celui-ci génère. Avec cette stratégie, on va donc **utiliser un marché d'actif pour emprunter des actifs qui serviront ensuite à s'exposer au token natif de la plateforme désirée**. 

*   **⚙ Condition :** Optimisme sur l'avenir d'un marché d'actif donné. Il dispose d'un token natif qui dans ce scénario devrait s'apprécier parallèlement à la croissance du marché d'actifs sur moyen/long terme.
*   **📅 Horizon temporel :** 3 - 24 mois. ~3 mois est un minimum recommandé pour que les frais en gas et les coûts d'emprunt n'impactent pas trop les retours de la stratégie.
*   **🔮 Résultat espéré** : le token acquis s'apprécie ce qui permet de rembourser la dette (+intérêts éventuels) à terme en revendant une partie de la position initiale. Une fois la dette remboursée, une partie des tokens acquis peut être conservée. 
*   **🃏 Bonus / Facilitateur :** Si le token en question peut produire un rendement (par ex AAVE dans le Safety Module), cela permettra de rembourser la dette encore plus rapidement ou d'accumuler "gratuitement" du token en question si le scénario d'appréciation de son prix se vérifie.

Bien que cette stratégie soit assez basique, il s'agit d'une de mes préférées. Je vous proposais récemment sur Twitter un exemple de sa mise en pratique que nous détaillerons ici :


<div align ="center">

{{< tweet 1385873962404614144 >}}

</div>

Ici, le protocole en question c'est [Liquity](https://liquity.org) et la mise en place de la stratégie est assez simple, mais connaît deux variations :

### Exposition directe au token natif

Soit en s'exposant directement au token LQTY, ce qui est bien sûr plus risqué :

![mm-long-tokenbrice](/img/2021/money-market-recipes/mm-long-token-tokenbrice.png "Exposition longue sur Liquity via le token natif LQTY")

1. Dépôt d'ETH sur [Liquity](https://www.liquity.org/) via un des frontends, ils serviront de collatéral pour la position.
2. Emprunt de LUSD
3. Swap de LUSD (via ParaSwap pour le meilleur taux !) pour du LQTY, le token natif de Liquity
4. Staking du LQTY, qui génère des LUSD et un peu d'ETH
5. À terme remboursement de la dette (2) via le rendement LUSD (4) et la revente d'une partie des LQTY acquis à l'étape 3 après une appréciation de leur prix.

Ou alors de manière plus prudente, avec une stratégie qui revient à utiliser Liquity pour emprunter des LUSD et les rendre productifs :

### Exposition essentiellement en stablecoins

![mm-long-token-tokenbrice](/img/2021/money-market-recipes/mm-long-tokenbrice.png "Exposition longue sur Liquity via Liquity/Curve")

1. Dépôt d'ETH sur [Liquity](https://www.liquity.org/) via un des frontends, ils serviront de collatéral pour la position.
2. Emprunt de LUSD
3. Staking du LUSD via soit la Stability Pool (-> LQTY + ETH) ou encore la pool LUSD sur Curve Finance (-> Natif + LQTY + CRV).
4. À terme remboursement de la dette (2) via le rendement (3)

{{< notice note >}}
Yearn Finance propose également un vault LUSD qui gère automatiquement la position sur Curve.
{{< /notice >}}

---

## Investir du temps plutôt que de l'argent

L'arrivée d'Alchemix a ouvert de nouvelles perspectives en termes de stratégie. Sur Alchemix, la dette se rembourse toute seule avec le temps. En effet, **le collatéral utilisé (yDAI) est un stablecoin qui produit un rendement (via Yearn)**. Ainsi avec les conditions actuelles l'emprunt est auto-remboursé en trois ans.

Je vous propose donc une stratégie simple pour tirer profit d'Alchemix afin de réaliser un profit. Le principal inconvénient est que **seulement la moitié de la quantité de DAI placées initialement dans Alchemix peut être empruntée en AlUSD** puis investie. Néanmoins comme cette stratégie s'appuie sur stablecoins, elle ne comporte - à priori (⚠ oracles) pas de risque de prix et ne nécessite donc pas de suivi quotidien.

*   **⚙ Condition :** Des DAI qui seront bloqués pendant ~3ans. Seulement la moitié de la somme déposée est mobilisable.
*   **📅 Horizon temporel :** ~3 ans (dépend du taux de retour DAI sur Yearn)
*   **🔮 Résultat espéré** : Dans 3 ans, la dette en AlUSD est entièrement remboursée et les DAI initialement mobilisés sur Alchemix sont à nouveaux libres. Reste à voir ce qu'il s'est passé avec l'investissement réalisé avec les AlUSD empruntés : tout dépend des choix réalisés, je ne prédis pas le futur.
*   **🃏 Bonus / Facilitateur :** Utiliser l'emprunt en AlUSD pour investir dans un token qui peut produire un rendement. Cela permet de réaliser un investissement composé ou bien encore de rembourser la dette Alchemix plus rapidement.

### Long ALCX via Alchemix

Pour illustrer le concept, je vous propose à nouveau une stratégie simple qui revient à long Alchemix via son token ALCX :

![alchemix-investment-tokenbrice](/img/2021/money-market-recipes/alchemix-investment-tokenbrice.png "Investissement financé par de la dette stable sur Alchemix")

1. Dépôt de DAI en collatéral sur Alchemix. Alchemix le déploie sur Yearn Finance pour produire un rendement.
2. Emprunt jusqu'à 50% de la valeur initiale déposée en AlUSD, un stablecoin.
3. Investissement des AlUSD dans le token désiré. Ici pour l'exemple c'est ALCX le token natif de gouvernance d'Alchemix.
4. Stake du token acquis pour produire un rendement
5. Le remboursement de la dette en AlUSD contracté sur Alchemix se fait automatiquement avec le temps. Il est possible de rembourser en avance grâce aux rendements générés (4).

---

## Mettre au travail un collatéral holdé sur le long terme

Je suis en arrivé à la DeFi il y a plusieurs années avec une ambition simple : je voulais mettre au travail mes Ether. À l'époque ça n'était pas une mince affaire mais aujourd'hui il existe de nombreuses solutions très intéressantes. Je vais me concentrer sur l'une d'entre elles : Aave pour deux raisons.

1. Aave a lancé **un programme de liquidity mining** payé en StkAave[^aaveLMmainnet] (Aave V2 - Mainnet).
2. Aave est accessible sur la **sidechain Polygon** où les frais minimes permettent de déployer des stratégies DeFi de manière efficace même avec des petits capitaux. Il y a là aussi un programme de liquidity mining, en MATIC.[^aaveLMmatic]

Pour que cette stratégie soit la plus accessible possible, on va développer l'exemple sur la sidechain Polygon. Elle est donc possible en utilisant n'importe lequel des tokens supportés en collatéral sur le marché Aave/Polygon : MATIC, AAVE, wETH, wBTC, USDC, et DAI. 

### Conditions d'implémentation

La stratégie consiste à **produire des rendements grâce à l'emprunt de stablecoins utilisés pour apporter de la liquidité sur le service d'échange Curve**. Grâce au programme de liquidity mining sur Aave, chaque étape du processus est potentiellement lucrative au moins en MATIC.

*   **⚙ Condition :** Avoir des tokens acceptés commes collatéral sur Aave, et les ramener sur Polygon par exemple en utilisant [le bridge POS](https://wallet.matic.network/bridge/).
*   **📅 Horizon temporel :** Court / moyen terme.
*   **🔮 Résultat espéré** : Rendements en MATIC, stablecoins et ETH.
*   **🃏 Bonus / Facilitateur : /**. Prospectif : mining CRV & effet de levier potentiel quand les tokens LP Curve Polygon sont acceptés en collatéral sur Aave.

### Mettre des ETH au travail sur Polygon

Pour illustrer la stratégie, je pars de l'hypothèse de générer un rendement à partir d'ETH.

![polygon-aave-curve-eth-farming-tokenbrice](/img/2021/money-market-recipes/polygon-aave-curve-eth-farming-tokenbrice.png "Farming sur Polygon via Aave et Curve en utilisant ETH comme collatéral")

1. Dépôt d'ETH en collatéral sur Aave/Polygon (+natif +MATIC)
2. Emprunt de stablecoins (-APR +MATIC)
3. Dépôt et staking des stablecoins sur Curve/Polygon (+natif +MATIC)

À noter que les tokens LP Curve Polygon sont considérés pour un ajout potentiel comme collatéral sur le marché Aave. On peut aussi s'attendre à un potentiel en CRV sur les positions LP sur Polygon si la DAO le décide.

Pour approfondir sur Aave, **[je vous propose un live marathon récemment réalisé avec plusieurs membres de l'équipe](https://www.twitch.tv/videos/994454624)**.

{{< notice note >}}
Il est possible de mettre en œuvre cette stratégie en gardant les tokens utilisés comme collatéraux sur le L1 Aave afin de bénéficier du mining de StkAAVE. Il faudra migrer les stablecoins empruntés du réseau Ethereum vers Polygon en utilisant par exemple [le bridge POS de Matic](https://wallet.matic.network/bridge/).
{{< /notice >}}

---

## Se prémunir contre le risque sur le prix du $ : farming en €

En DeFi, tout se passe en dollar. Ça fait du sens, tout le monde connaît, mais pour un utilisateur européen cela peut poser un vrai risque. En effet, si votre ambition est de générer de quoi vivre avec la DeFi, alors cela signifie que votre sortie se fera éventuellement en Euro. 

![eur-usd-1y](/img/2021/money-market-recipes/eur-usd-1y.png "Évolution du taux de change €/$ sur l'année dernière")

Pour un fermier Européen, il peut donc être **intéressant d'avoir une exposition DeFi en € pour éviter ce risque supplémentaire**. Pour l'instant, il n'y a tout simplement aucune option d'emprunt en Euro autre que [Mimo Capital](https://mimo.capital/). 

Le service vous permet d'emprunter des PAR depuis ETH, wBTC ou USDC. Le token de gouvernance MIMO est également distribué aux possesseurs de vaults actifs ainsi qu'aux apporteurs de liquidité sur les pools Balancer PAR/ETH et PAR/USDC.

Néanmoins le protocole est encore récent et le token PAR n'est pas encore supporté dans l'écosystème, en tant que collatéral sur Aave ou dans une pool Curve par exemple. La situation n'est donc pas encore idéale mais elle a le mérite d'exister !

D'autres solutions DeFi-€ sont en cours de développement. MakerDAO par exemple a mentionné un Euro-DAI, tandis que Jarvis Network travaille sur un € stablecoin synthétique, le jEUR.

### Conditions d'implémentation

Pour farmer nativement en Euros, la meilleure option reste encore ce qu'il est possible de faire avec du EURS. Depuis le lancement de la pool sur Curve, les options sont multiples.

*   **⚙ Condition :** Posséder des EURS / sEUR
*   **📅 Horizon temporel :** 1 mois - années
*   **🔮 Résultat espéré** : Faire fructifier un capital en Euro-stables
*   **🃏 Bonus / Facilitateur :** Posséder des VeCRV.

![EURS-farming-tokenbrice](/img/2021/money-market-recipes/EURS-farming-tokenbrice.png "Options de farming avec le stablecoin EURS")

*   La **pool Curve** directement offre un rendement attractif en CRV même lorsqu'il n'est pas boosté.
*   Pour revendre automatiquement les CRV farmés afin de composer le rendement, un vault est idéal. **[Yearn](https://yearn.finance) propose un vault sur EURS**.
*   Le farming est également possible via le vault EURS de [StakeDAO](https://stakedao.org/), afin d'accumuler aussi des SDT.
*   Ou bien encore, [Harvest](https://harvest.finance) propose également un vault qui compose l'essentiel des rendements tout en rémunérant en FARM.

J'espère que ces différentes recettes sauront vous inspirer. Assurez-vous d'être **[conscient des différents risques liés aux marchés monétaires]({{< relref path="/content/posts/2021/money-market-risks.fr.md" >}})**, utilisés pour toutes ces stratégies.

---

## Ensemble, le 🌾 Blé foisonne

La DeFi, ça marche encore mieux en communauté ! Pour aller plus loin dans votre découverte, **[rejoignez le Discord DeFi France](https://discord.gg/3bWZcK2)**. Vous pourrez échanger avec plus de 1500 DeFians francophones de différentes expériences et horizons. 

En outre, les contributions sont désormais reconnues - en 🌾 Blé ! La gouvernance de la communauté se décentralise, c'est un excellent moment pour s'impliquer.

Enfin pour mieux comprendre ce nouveau système communautaire, le replay de notre direct de présentation est disponible :

{{< youtube fMpYQYXBrfA >}}

[^aaveLMmainnet]: Le programme de liquidity mining StkAAVE a été lancé le 26 Mai suite à vote de gouvernance. [Plus d'infos ici](https://twitter.com/AaveAave/status/1386753673104134155?s=20)
[^aaveLMmatic]: Polygon sponsorise un programme de liquidity mining en MATIC, à la fois [sur Aave](https://blog.polygon.technology/defiforall-kicking-off-l2-defi-summer-with-40-million-usd-in-liquidity-mining-rewards-from-4937d7c6e287) et sur [Curve](https://blog.polygon.technology/continuing-scalability-defi-summer-with-5-million-usd-in-liquidity-mining-rewards-from-polygon-e73a76c5a8ad?gi=9a7b7e130606)
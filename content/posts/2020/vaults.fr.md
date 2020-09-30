---
title: "🤖 Les vaults : stratégies d'investissement DeFi accessibles ?"
description: "Les vaults permettent d'exploiter des programmes d'incitation à l'apport de liquidité en composant automatiquement et fréquemment les gains obtenus. Examinons les options disponibles et leurs contreparties."
date: '2020-09-30T01:13:50.191Z'
categories: [🌌 DeFi, 💸 DeFi pratique]
tags: [DeFi, Ethereum, Curve, yVault, Yearn, Yearn Finance, YFV, Uniswap, UNI, YFII, FARM, Harvest Finance]
---

À mesure que l'écosystème des services financiers décentralisés sur Ethereum se développe et mûrit, l'offre de services devient plus dense et parfois difficile à comprendre. Si les utilisateurs les plus avertis sur le plan technique peuvent se tenir au courant des dernières sorties et couvrir leurs risques de manière appropriée, les investisseurs moins expérimentés peuvent se sentir largués.

Heureusement, il existe des services DeFi adaptés à la diversité des investisseurs qui explorent cet espace. Yearn Finance a été la première plateforme à lancer un type de produits d'investissement passif : les vaults. 

L'idée de base est simple comme 1, 2, 3 :

1. Les vaults sont des **stratégies d'investissement tokénisées** : votre dépôt est représenté par un token (par exemple, yCRV dans la chambre forte de Yearn -> yyCRV/yUSD)
2. **Le vault récolte et réinvestit fréquemment les profits** (ici CRV) pour racheter  l'actif de base fourni, ce qui augmente les rendements.
3. **Les frais sont simplifiés** : les déposants ne paient pas les frais de gaz de l'opération des vaults (comme la récolte). Les frais sont généralement facturés à la sortie du vault.

Donc si vous voulez **éviter les maux de tête** liés à la chasse à la dernière ferme, à la gestion du claim des bénéfices que vous gagnez, au moment et à la manière de les réinvestir, sans oublier, bien sûr, de tenir compte des coûts du gaz de toutes ces opérations dans le calcul de vos bénéfices, les vaults sont une alternative crédible.

<div align=""center>

![Harvest Finance GIF](/img/2020/vaults/harvest.gif)

_Harvest Finance propose plusieurs vaults pour simplifier le farming [(source gif)](https://twitter.com/risk22_/status/1307304283415560193?s=20)_
</div>

Les vaults sont faits pour **abstraire la complexité pour les utilisateurs finaux**.  Vous déposez des tokens et attendez qu'ils élaborent une stratégie pour vous. Voyons donc quelles sont les options disponibles.

{{< notice note >}}
Cet article va droit au but et met en évidence les différents vaults disponibles. Pour en savoir plus sur les débuts de Yearn Finance, [**lisez cet article**]({{< relref path="/content/posts/2020/yearn-finance-YFI.fr.md" >}}). Pour en savoir plus sur les forks de Yearn, [**celui-ci**]({{< relref path="/content/posts/2020/yearn-waifus.fr.md" >}})
{{< /notice >}}

## Le plus simple : les vaults basiques

Les vaults utilisent le token que vous déposez (DAI par exemple) pour mettre en place une stratégie donnée, produire un rendement et le réinvestir automatiquement. 

Le pionnier est bien sûr Yearn avec la vaults yCRV, mais plusieurs options sont maintenant disponibles ou en cours de déploiement. Cet article donne un aperçu structuré des principales possibilités offertes par les vaults. 

Ici, vous déposez un token donné pour en gagner davantage au fil du temps, et éventuellement une récompense supplémentaire. Les tokens que vous fournissez ne sont pas utilisés pour fournir des liquidités sur des échanges décentralisés, **de sorte qu'il n'y a pas d'exposition à des pertes impermanentes**.

Cependant, **comme de plus en plus de produits de type vaults sont mis sur le marché, vous voulez prendre le temps de comprendre ce qui se passe avec celui que vous choisissez**.

Vous trouverez ci-dessous des tableaux résumant les principaux vaults que je connais, avec les tokens qu'ils acceptent, le service qu'ils exploitent et la manière dont le retour est libellé.

La mention "retours composés" signifie que la stratégie génère un retour fréquemment vendu pour le token de base apporté - cette opération est parfois appelée "récolte" (harvest). 

{{< notice tip >}}
La fréquence de la récolte est importante car elle influencera le facteur de composabilité de la position globale, ainsi que le niveau de risque pris sur le prix du token farmé.
{{< /notice >}}

### Vaults Stablecoins & BTC 

En ce qui concerne les vaults, les tokens les plus couramment acceptés en dépôt sont les stablecoins. Ces vaults déploieront votre capital sur le pool Curve Finance pour gagner des tokens CRV, généralement le pool Y. Des projets plus récents, tels que Pickle Finance, permettent également d'exploiter le pool Curve sUSD.

<div align="center">

![pickle-finance-pjar0](/img/2020/vaults/pickle-pjar0.png)

_Infographie détaillant le vault pJar0 de Pickle Finance [source](https://medium.com/@picklefinance/introducing-picklejars-70a311ab65c5)_
</div>

Enfin, certains services comme Harvest ou YFV ont un modèle incitatif en plus de leur vaults : les déposants gagnent le token de gouvernance de la plateforme (FARM ou YFV) en plus du rendement de base.

|  **TOKENS** | **SERVICE** | **FARME SUR** | **RETOURS** |
| :---: | :---: | :---: | :---: |
|  DAI, USDC, USDT, TUSD | Harvest.Finance | Curve | Retour Curve composé + FARM |
|  USDC, USDT, DAI, TUSD, BUSD | DFI.Money | Curve | Retour Curve composé |
|  DAI, USDC, USDT, TUSD | YFV (Seed Pool) | Value | YFV/VALUE  |
|  yCRV | Yearn Finance | Curve | CuRetour Curve composé |
|  pJar 0 + psCRV pool (Curve sUSD) | Pickle Finance | Curve/Pickle | Retour Curve composé + PICKLE |

Étant donné que Curve prend également en charge les pools tokenisés de BTC, il existe désormais des vaults pour la BTC également :

|  **TOKEN** | **SERVICE** | **FARME SUR** | **RETOURS** |
| :---: | :---: | :---: | :---: |
|  wBTC, renBTC & CRVRENWBTC | Harvest.Finance | Curve | Retour Curve composé + FARM |
|  hBTC | DFI.Money | Curve? | Retour composé |

{{< notice note >}}
Avec Harvest.Finance, vous pouvez déposer directement le wBTC ou le renBTC, ou le token CRVRENwBTC, qui représente un dépôt dans le Curve's Pool 5 (pool RenBTC & wBTC).
{{< /notice >}}

### Vaults ETH

Les vaults sur BTC et stablecoins sont intéressants mais peut-être aimeriez-vous conserver une exposition au prix de l'ETH ? 

Vous pouvez obtenir un tel résultat par vous-même en tirant parti de votre ETH. Vous les utiliserez comme collateral pour générer ou emprunter des stablecoins / WBTC qui sont ensuite déployés pour produire un rendement supérieur à votre coût d'emprunt : voici un article que j'ai écrit et qui fournit des conseils et des outils pour tirer efficacement parti de l'ETH - [**🎚 ETH ou DeFi : pourquoi choisir?**]({{< relref path="/content/posts/2020/leveraging-ETH.fr.md" >}})


Toutefois, avec une telle position, vous pouvez être exposé à des liquidations si le prix de l'ETH devait baisser.


Une fois de plus, Yearn a été le pionnier dans ce domaine avec la libération du vault yETH qui a automatisé tout ce processus. Cependant, le volume des dépôts était énorme et le service s'est heurté à des problèmes techniques sur lesquels on travaille actuellement.

Alors, au lieu d'attendre la réouverture de la chambre forte WETH de Yearn, pourquoi ne pas envisager les **options existantes** ? Elles ne sont pas aussi complexes que celles de Yearn, puisqu'elles n'ont pas d'effet de levier sur votre ETH ; l'ETH est simplement déposée quelque part pour produire un rendement.

|  **SERVICE** | **FARME SUR** | **RETOUR** |
| :---: | :---: | :---: |
|  Yearn Finance | Maker + Curve | Retour composé (yDAI) |
|  Harvest.Finance | Dépôt sur Cream | Retour Cream composé + FARM return (fwETH staking) |
|  YFV | Soda | Soda returns normalized to wETH + VALUE |
|  DFI.Money | ? | Retour composé |

Jusqu'à présent, nous nous en sommes tenus à de "simples" vaults où vous déposez un token donné, le laissez reposer un moment et, avec un peu du bon sens, en sortez avec d'autres tokens (+éventuellement quelques tokens supplémentaires de gouvernance). Cependant, avec le lancement du token UNI d'Uniswap, un autre type de vaults plus risqué est disponible.


## Vaults UNI/Uniswap


### Les bases du farming de l'UNI

Avec le lancement du token UNI est venu un programme de distribution instaurant des incitations UNI sur des pools spécifiques :

1. ETH/USDC
2. ETH/USDT
3. ETH/DAI
4. ETH/wBTC

Si vous fournissez des liquidités sur l'un des pools énumérés ci-dessus, vous pouvez placer votre token de pool de liquidités pour un revenu UNI supplémentaire directement vers le site d'Uniswap. Vous gagnerez ainsi un revenu UNI en continu. Toutefois, vous devrez gérer la position vous-même, ce qui signifie que vous devrez réclamer l'UNI (et payer les frais de gaz associés), ainsi que les vendre et les réinvestir.

Ces stratégies sont plus risquées que les vaults de l'ETH/BTC/Stablecoins. En effet, en cultivant des tokens UNI, vous fournissez des liquidités sur l'Uniswap, ce qui comporte un risque de pertes impermanentes.

Mais pourquoi faire face aux tracas de l'"agriculture manuelle" quand vous pouvez **laisser un vault faire le travail à votre place**.


### L'agriculture UNI à l'aide d'un Vault

En effet, peu après le lancement d'Uniswap, plusieurs services ont commencé à proposer des produits de type vaults pour rationaliser l'agriculture de l'UNI. En voici un aperçu :

|  **SERVICE** | **TOKENS** | **RETOUR** |
| :---: | :---: | :---: |
|  Harvest | ETH/USDC, ETH/DAI, ETH/USDT, ETH/wBTC | Retour UNI composé + FARM |
|  Pickle Finance | ETH/DAI, ETH/USDC, ETH/USDT | Retour UNI composé + PICKLE |
|  YFV | ETH/USDC, ETH/wBTC | Retour UNI composé + VALUE |

{{< notice note >}}
Cette liste n'est pas exhaustive. Seuls les vaults sont inclus - des services qui réinvestissent automatiquement les bénéfices pour vous. 
{{< /notice >}}


Il existe d'autres possibilités de cultiver l'UNI, mais elles nécessitent une plus grande intervention de votre part. Par exemple, avec [Sake Swap](http://sakeswap.finance/), vous pouvez placer vos tokens Uni-V2 LP de l'ETH-Stable pour gagner des tokens UNI et SAKE. Cependant, vous devrez réclamer et gérer vous-même les tokens SAKE & UNI que vous aurez gagnés.

Pour en savoir plus sur un vault donné et sur son fonctionnement, n'hésitez pas à consulter ses ressources. Yearn et Harvest Finance disposent d'une excellente documentation avec des infographies expliquant leurs vaults :

* [**Learn Yearn**](https://www.learnyearn.finance/)
* [**Farm Wiki**](https://farm.chainwiki.dev/en/home)

{{< notice warning >}}
Il ne s'agit pas de conseils en matière d'investissement, restez vigilant et faites vos propres recherches.
{{< /notice >}}

Services mentionnés :
- [**Yearn Finance**](https://yearn.finance/)
- [**Harvest Finance**](https://harvest.finance/)
- [**Pickle Finance**](https://pickle.finance/)
- [**DFI.Money**](https://dfi.money/)
- [**YFV**](https://yfv.finance/)

Bonnes récoltes ! 🚜
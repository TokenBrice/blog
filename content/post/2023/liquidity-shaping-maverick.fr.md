---
title: "Maverick et la transition du Liquidity Mining au Liquidity Shaping"
description: "La guerre des DEX fait rage, plus compétitive que jamais. A côté des cartels de la licorne, du lama et de l'échelle, un quatrième centre de pouvoir émerge grâce à des caractéristiques sans précédent : une structure de liquidité inégalée associée à un modèle d'incitation immensément plus efficace : **le façonnage de liquidité**."
date: '2023-07-07T01:13:50.191Z'
categories: [DeFi, Comprendre]
tags: [DeFi, Ethereum, Finance Décentralisée, DEX, veMAV, Maverick, Liquidity, Liquidity Mining, Gestion de Liquidité, Liquidity Shaping, Concentrated Liquidity, veCRV, Solidly, Velodrome]
toc: false
tocNum: false
url: maverick-liquidity-shaping
image: img/2023/liquidity-shaping-maverick/cover.png
---

Cela fait quatre mois que Maverick est sorti, et quelques jours que le jeton MAV a rejoint la mêlée. Pourtant, la plupart des acteurs de la DeFi se demandent encore comment Maverick peut offrir une efficacité du capital 2 à 3 fois supérieure à celle de son principal concurrent, Uniswap. 

Le moment était donc venu de plonger dans les innovations apportées par le modèle et le nouveau paradigme qu'il favorise en matière de gestion des liquidités : **le liquidity shaping** (le façonnage de liquidité).


## Innovations sur DEX ? Plutôt des outils permettant aux LP de s'exprimer

Fondamentalement, un échange décentralisé peut innover à deux niveaux : 

1. **La structure de liquidité** : les options offertes aux fournisseurs de liquidité pour concevoir l'activité d'approvisionnement qui correspond le mieux à leur thèse.
2. Et / ou **le modèle d'incitation** : les outils et les modalités permettant aux DAO et aux projets d'encourager des structures de liquidité personnalisées ou non.

La plupart des nouveaux DEX qui sortent recyclent une infrastructure existante et se concentrent sur l'innovation dans une seule dimension - généralement le modèle d'incitation - comme on l'a vu récemment avec la vague de forks Solidly/Velodrome - **[ve(3,3), la prochaine étape logique après veCRV ?](https://tokenbrice.xyz//content/posts/2023/solidly-velodrome-template.fr.md)**. 

Il y a cependant quelques moments critiques dans l'industrie où un nouveau DEX est sorti et a apporté **une innovation critique sur les deux fronts :**

1. **[Uniswap V1/V2](https://www.defiscan.info/protocols/uniswap-v2/ethereum)** a établi une infrastructure solide pour les pools `x*y=k` et le modèle d'incitation de base : 30 points de base de frais, composé automatiquement & la possibilité d'avoir des programmes de Liquidity Mining sur les tokens LP mis en jeu (ERC20).
2. **Curve** a fourni un modèle de liquidité innovant et efficace pour les actifs indexés (stableswap) tout en étant le pionnier d'un modèle basé sur le ve/gauge pour l'incitation des fournisseurs de liquidité en introduisant une capture de revenus au niveau du jeton (frais d'administration).
3. **[UniswapV3]( https://www.defiscan.info/protocols/uniswap-v3/ethereum)** a fourni les outils nécessaires à la gestion d'une structure de liquidité plus avancée exploitant efficacement la liquidité concentrée et offrant une plus grande flexibilité en termes de frais (frais de 1, 5, 30, 100 points de base, non composés automatiquement).
4. Enfin, **[Maverick](https://www.defiscan.info/protocols/maverick-v2/ethereum)**, qui va encore plus loin qu'UniswapV3 dans la personnalisation de la structure de liquidité qu'il propose, offre une gestion rationalisée des positions (rééquilibrage natif) et un niveau de contrôle sans précédent en ce qui concerne les options d'incitation, marquant la naissance d'un nouveau paradigme : le façonnage de la liquidité.

Chacune de ces innovations fondamentales **permet une plus grande expressivité pour les LPs : ils ont accès à des outils de plus en plus raffinés et personnalisés permettant même aux thèses les plus complexes de trouver un moyen adéquat pour être exprimées onchain**.

Cependant, avant de plonger dans la profondeur de la formation de la liquidité, quelques points sur Maverick sont nécessaires. En effet, pour bien comprendre l'impact du façonnage de liquidité sur Maverick, il faut d'abord maîtriser ses structures de liquidité et leurs conséquences.

## LES STRUCTURES DE LIQUIDITÉ DE MAVERICK

En effet, l'une des principales innovations de Maverick réside dans ses structures de liquidité, qui permettent à l'échange d'atteindre un niveau sans précédent d'efficacité du capital.

Maverick offre quatre options aux apporteurs de liquidité qui pourraient être regroupées en deux catégories pour plus de simplicité :

1. Le mode statique est similaire à une liquidité UNIv3 fournissant une gamme personnalisée, avec **immensément plus de flexibilité**.
2. Et trois modes dynamiques offrent **différents types de rééquilibrage aux LP** pour optimiser davantage leurs gains : gauche (suit le prix à gauche), droite (suit le prix à droite), et les deux (suit le prix dans les deux sens).

### Pourquoi le mode statique de Maverick change la donne

Beaucoup n'ont pas encore compris à quel point le mode statique de Maverick est une amélioration par rapport à UNIv3, alors concentrons-nous un instant sur ce point. Voici un tableau rapide récapitulant les principales différences pour commencer :

| Objet                                                         | Uniswap v3            | Pool Statique Maverick         |
| ------------------------------------------------------------ | --------------------- | ----------------------------- |
| Apport de liquidité en range personalisable et arbitraire, même avec un seul token | ✅                     | ✅                             |
| Permet de distribuer la liquidité de manière discontinue ou inéquitable   | ❌                     | ✅                             |
| Customisation des frais et largeur des ticks                           | 4 tiers de frais | Customisation quasi-infinie |
| Permet la création de token LP wrappé en ERC-20 pour faciliter le dépot des LPs et leur incitation | ❌                     | ✅ (Boosted Pools)             |
| Permet la distribution de récompense aux LPs (Liquidity Mining) | ✅                     | ✅                             |
| Permet une distribution pondérée et précisément ciblée de récompense aux LPs (Liquidity Shaping) | ❌                     | ✅                             |

Comme UniswapV3, Maverick prend en charge la fourniture de liquidité dans **une plage arbitraire personnalisée,** même potentiellement avec un seul jeton, par exemple, une LP sur ETH/USDC de 2000 $ à 2400 $.

Si le prix actuel est inférieur à 2000 $ (au moment de la rédaction : 1900 $), la LP sera alimentée uniquement en ETH et se rééquilibrera progressivement en USDC au fur et à mesure que le prix augmente, pour finir entièrement en USDC à 2400 $.

![eth-lp-univ3.png](img/2023/liquidity-shaping-maverick/eth-lp-univ3.png "The $2000-2400 ETH/USDC LP on UniswapV3")

Mais qu'en est-il des LP dont la thèse est encore plus raffinée ? Qu'en est-il du LP qui voit l'ETH dans cette fourchette pendant une semaine, mais surtout dans la zone des 2150-2250 $ ? Ne serait-il pas agréable pour lui de pouvoir exprimer cette thèse à travers la structure de liquidité qu'il choisit ? C'est précisément ce que permet Maverick :

![eth-lp-mav.png](img/2023/liquidity-shaping-maverick/eth-lp-mav-fr.png "Le même $2000-2400 ETH/USDC LP sur Maverick, avec environ x4 plus de liquidité dans la gamme $2150-$2250")

Dans la capture d'écran ci-dessus, vous voyez une distribution de $2000 à $2400 sur la paire ETH/USDC ; cependant, **à la différence d'Uniswap, qui distribue nécessairement la liquidité de manière égale à travers la gamme de prix, Maverick permet aux LP de choisir**. Pour mieux correspondre à notre thèse, la plupart des liquidités sont concentrées sur les trois ticks couvrant la zone de prix 2150-2250 $.

### Maximiser l'expressivité offerte aux LP

L'expressivité offerte aux LP sur Maverick est virtuellement infinie. Je m'attends à voir émerger rapidement des cas d'utilisation intéressants, en particulier pour les protocoles qui exploiteront Maverick dès le départ (protocoles "natifs Maverick"). Par exemple, vous pourriez envisager Maverick comme **mécanisme de stabilisation du prix d'un stablecoin ou d'un actif indexé**.

En supposant que le projet de stablecoin contrôle une certaine liquidité, il pourrait la fournir de manière très expressive en cas de besoin pour restreindre la fourchette de prix. Voici une structure de liquidité "buy wall"(mur d'achat) sur le LUSD : toute la liquidité de ce LP est fournie sur un seul tick, le premier où le LUSD vaut moins de 1,00 USDC.

![mav-buy-wall.png](img/2023/liquidity-shaping-maverick/mav-buy-wall.png "Une structure de liquidité de mur d'achat de stablecoins sur Maverick")

Avec un prix actuel >1,00 USDC, cette LP est approvisionnée à 100% en USDC et agit comme une réserve d'achat : si le prix du LUSD baisse, la LP sera rééquilibrée. Ces positions sont prometteuses, car elles peuvent exercer une pression à l'achat et à la vente, ce qui permet de mieux contraindre les actifs de référence dans des fourchettes plus étroites, ce qui réduit considérablement le coût de l'incitation à la liquidité.

### Qu'en est-il des modes dynamiques ?

Les modes dynamiques de Maverick offrent une solution pratique et facile pour les LPs qui maximisent leur exposition aux prix du marché afin de maximiser le volume traité. Les trois modes exploitent essentiellement la même structure, mais offrent des options différentes aux LPs :

- Suivre le prix dans un seul sens (gauche ou droite) - il y a des tonnes de paires où cela a beaucoup de sens, comme wstETH/ETH (wstETH étant "up-only" par rapport à ETH grâce au rendement du staking).
- Suivre le prix dans les deux sens, une bonne solution pour les LP qui cherchent à maximiser la liquidité et les frais perçus au détriment d'un risque accru d'IL sur le principal. Il est particulièrement adapté aux paires d'actifs stables et ancrés, mais pas seulement.

![mav-both.gif](img/2023/liquidity-shaping-maverick/mav-both.gif "Explication visuelle du mode both de Maverick")

Ce qu'il faut comprendre ici, c'est que **Maverick fournit un rééquilibrage natif à ses LPs**, et là encore, il va au-delà de ce qui a précédé en termes d'options de personnalisation. Le mot clé est "natif", ce qui signifie que le rééquilibrage peut être **fait de manière intelligente et économe en gas**.

Sur Curve, les LPs n'ont pas d'options : leur liquidité est concentrée, mais tous les LPs d'une paire donnée sont soumis au même régime. Cela facilite la gestion, mais tue l'expressivité. Avec Uniswap, les LPs peuvent rééquilibrer dynamiquement leur position à l'aide d'outils tiers comme Arrakis ; cela s'accompagne d'hypothèses de confiance considérables, de frais potentiels et de coûts de gas élevés. Il permet une plus grande expressivité mais nécessite une gestion plus active.

Bien que le rééquilibrage des liquidités de Maverick, basé sur un TWAP et avec quelques délais pour éviter les manipulations, présente certaines limites, il reste un outil crucial pour aider les LPs à maximiser le temps effectivement passé dans la fourchette / dans le tick de prix actuel.

## LE MODÈLE D'INCITATION DE MAVERICK : LA FAÇONNAGE DE LIQUIDITÉ

Avec une meilleure compréhension de la première innovation fondamentale apportée par Maverick - l'expressivité sans précédent offerte aux LP dans la conception et la gestion de leur position - nous pouvons maintenant explorer la deuxième jambe de Maverick : son nouveau modèle d'incitation.

L'histoire est à la fois courte et longue. **En bref, Maverick offre le même niveau de personnalisation au niveau de l'incitation qu'au niveau de la création des pools.**

Cela nous amène à une histoire plus longue, avec des exemples plus explicites. Il est possible de reproduire la plupart des structures de liquidité et des modèles d'incitation existants sur Maverick. Mais ce qui est encore plus intéressant, ce sont les nouveaux modèles qui n'ont jamais été essayés parce qu'ils n'étaient pas techniquement réalisables avant Maverick : il est temps d'explorer et d'expérimenter !

### Murs d'achat/de vente dynamiques déclenchés par un contrat

Souvenez-vous de l'exemple précédent concernant le projet stablecoin qui déploie des liquidités en tant que mur d'achat pour limiter le prix. **Le projet n'a même pas besoin de ses liquidités pour le faire**, car le même processus peut être reproduit avec une boosted pool :

1. Le projet crée une boosted pool où toutes les liquidités sont distribuées un tick en dessous du prix comme ci-dessus.
2. Le projet fournit des incitations à la boosted pool pour la durée de son choix et les singes feront le reste.

L'ensemble de ce processus peut être automatisé et déclenché entièrement par des contrats intelligents, ce qui signifie qu'un autre contrat pourrait gérer dynamiquement les incitations.

### Le cas de cvxCRV/CRV

Étudions un autre cas d'échec et mat, celui de cvxCRV. En effet, le pool cvxCRV/CRV Curve est le pire des cas :

- Il exploite une structure de pool classique, **absolument sous-optimale pour un actif se négociant dans une fourchette contrainte comme le cvxCRV**.
- Il exploite un **modèle d'incitation de liquidité "stupide" où tous les LPs sont payés de la même manière**, ce qui conduit à des dépôts de cvxCRV, qui représentent 75% du pool, gagnant 75% des récompenses - tout en étant presque inutile du point de vue de la liquidité (car il y a déjà trop de cvxCRV dans ce pool).

#### Que peut-on faire de mieux ?

Tout d'abord, la concentration pourrait être affinée au niveau de la structure de liquidité. Le cvxCRV est un "actif à sens unique" : vous pouvez convertir des CRV en cvxCRV 1:1 par le biais des contrats Convex, mais la conversion de cvxCRV en CRV se fait sur un DEX avec une décote.

=> Cela signifie que le cvxCRV a un prix plafond par rapport au CRV : dans aucun monde, le cvxCRV ne pourrait valoir >1 CRV, et le prix actuel est d'environ 0,95 CRV par cvxCRV.

==> La structure idéale pour une telle pool pourrait être **une concentration allant de 1cvxCRV = 0,9 CRV à 1 cvxCRV = 0,99 CRV, offrant une efficacité de liquidité largement supérieure**.

En ce qui concerne la couche d'incitation, des gains considérables peuvent être réalisés grâce à un petit changement. Au lieu de payer tous les LPs de la même manière alors que le pool est massivement déséquilibré, pourquoi ne pas se concentrer sur ceux qui apportent le plus de valeur au pool, c'est-à-dire la composante CRV ?

=> J'opterais pour deux pools conjointes afin de couvrir au mieux cette paire sur le plan de l'incitation : **Tout d'abord, un LP statique sur dix bins** centré sur le prix actuel - cela permet au prix de s'exprimer avec suffisamment de liquidité et cette structure est déjà >100x plus efficace que le pool Curve V2 existant.

==> Pour enfoncer le clou, nous pouvons **ajouter une pool gauche-droite d'un seul tick au prix pour maximiser l'efficacité de la liquidité**. 

Les détails de cet exemple vous aident à comprendre que si vous amenez ce pool à Maverick, l'effet composé de la structure de liquidité supérieure avec un modèle d'incitation beaucoup plus efficace conduit à des résultats d'une ligue différente. 

![curve-cvxcrv-crv.png](img/2023/liquidity-shaping-maverick/curve-cvxcrv-crv.png "Le pool cvxCRV/CRV sur Curve")

Il y a actuellement 54 millions de dollars de TVL dans le pool cvxCRV/CRV de Curve pour un volume quotidien d'environ 300 000 dollars par jour (0,5 % d'utilisation). Avec une incitation de base de 12% CRV, ~**$6M de jetons CRV sont dépensés chaque année pour maintenir cette liquidité**.

**Sur Maverick, une pool de ~500K$ correctement structuré** (250k$ statique à large gamme + 250k$ gauche-droite) **serait suffisante pour traiter régulièrement le volume quotidien de 300k$** avec des prix plus intéressants que sur Curve. En supposant la même intensité d'incitation, **cela coûterait 60 000 $ par an à maintenir**.


### Proto Liquidity Shaping avec Bunni ?

J'espère qu'à ce stade, vous avez une meilleure idée de la raison pour laquelle le façonnage de liquidité est véritablement révolutionnaire, car il permettra un autre saut d'ordre de grandeur en ce qui concerne l'efficacité des structures de liquidité et des modèles d'incitation. 

Il existe des itérations antérieures, moins complètes, d'un tel concept, fournies par les gestionnaires de liquidité construit au-dessus d'UniswapV3 qui permettent l'incitation sur une gamme personnalisée, par exemple, des récompenses pour LUSD/USDC LP, mais seulement pour la gamme LUSD = 0,999 USDC à LUSD = 1,01 USDC. [Bunni](https://bunni.pro/) est un bon exemple de ce type de services.

Ces services pourraient être qualifiés de "proto liquidity shaping", car ils permettent de forcer une fourchette de prix spécifique, mais ne peuvent pas appliquer des pondérations différentes à chaque tick au sein de cette fourchette : ils sont limités par le modèle de pool Uniswap V3, qui offre moins de flexibilité que Maverick. Au final, les deux sont assez complémentaires car Bunni peut être utilisé pour forcer une large fourchette, qui peut être affinée avec une pool Maverick statique et inégale, et enfin maintenue très liquide au prix actuel avec une pool gauche-droite sur Maverick également.

## MAV TOKEN

Avec des perspectives claires sur la nouvelle structure des pools, le modèle d'incitation et leurs conséquences, nous sommes maintenant prêts à ajouter la dernière pièce du puzzle, une pièce qui vous est probablement plus familière, mais ici aussi, il y a des différences clés : le token MAV. 

Lancé il y a quelques semaines, le token MAV a été distribué aux premiers fournisseurs de liquidités et aux utilisateurs du protocole. Cette distribution n'est que **la première d'une longue série**, et d'autres sont prévues, pour les LPs, mais aussi pour les protocoles qui exploitent Maverick ou s'appuient sur lui. Pour plus de détails sur la distribution prévue, consultez l'article [Maverick Ecosystem Incentive Program](https://medium.com/maverick-protocol/maverick-ecosystem-incentive-program-95cf76dbfa5e).

En tant que lecteurs de ce blog, j'imagine que vous êtes largement familiarisés avec le modèle veCRV et ses implications. Si ce n'est pas le cas, vous avez de la lecture :

**[⚔ Guerre du CRV : comprendre la course à l'accumulation de la capacité à influencer le protocole Curve Finance](https://tokenbrice.xyz/content/posts/2021/crv-wars.fr.md)**.

### veMAV & Liquidity Directing Voting (façonnage des liquidités par le vote)

![vemav](img/2023/liquidity-shaping-maverick/vemav.png)

Le lancement du jeton MAV est séquentiel, actuellement en phase 1, où les utilisateurs peuvent réclamer leur drop, LP MAV, ou le verrouiller pour obtenir veMAV. **La phase 2 introduira le Liquidity Directing Voting de Maverick et marquera le véritable début de la guerre du MAV**. 

La principale différence ici est, bien sûr, l'expressivité permise par Maverick qui aura également un impact sur les tokenomics : contrairement à veCRV ou veBAL, où les projets allouent des liquidités à un pool entier, ici, avec Maverick, **les protocoles seront en mesure de cibler leur pouvoir de vote sur une partie spécifique de la distribution de l'AMM**. Vous trouverez plus d'informations sur veMAV ici : [Introducing Maverick Protocol's Voting-Escrow Model](https://medium.com/maverick-protocol/introducing-maverick-protocols-voting-escrow-model-c29a60120339).

### Stratégie x-chain pour Maverick & veMAV

Un autre point essentiel à noter concernant le jeton MAV est qu'il met en œuvre la norme [Layer Zero's Omnichain Fungible Token (OFT) standard](https://layerzero.gitbook.io/docs/evm-guides/layerzero-omnichain-contracts/oft), ce qui facilite grandement les opérations inter-chaînes. Il permet à MAV d'exister nativement sur toutes les chaînes et devrait faciliter la tâche de l'équipe chargée de lancer le système de jauge sur un nouveau réseau.

À première vue, ce n'est pas grand-chose, mais cela pourrait faire une énorme différence. En effet, Curve et Balancer ont été lents à exporter leur modèle de jauge complet vers des réseaux autres que le réseau principal sur lequel ils opèrent initialement. **Je m'attends à ce que Maverick évolue beaucoup plus rapidement**, et les premières données empiriques le confirment. En ~3 mois d'existence, Maverick a déjà lancé deux chaînes en dehors du réseau principal : zkSync et BSC.

### Une autre différence majeure avec veCRV

veMAV met en œuvre plusieurs autres changements par rapport à un modèle veCRV de base, et je vous invite à les identifier tous. En voici d'autres :

- La pondération des veMAV par MAV n'est pas linéaire ici, même si elle favorise toujours ceux qui s'engagent le plus (4 ans) ; le blocage min d'une semaine donne un veMAV/MAV, tandis que le blocage max donne 5veMAV/MAV.
- Il n'y a **pas de décroissance linéaire** comme pour les veCRV - une amélioration significative de l'expérience utilisateur. Cela pourrait également avoir des conséquences très positives pour les wrappers de liquide veMAV, en rendant plus facile de rester proche du peg.
- Cependant, il existe toujours des incitations à rester engagé. En effet, le ratio veMAV/MAV est calculé à l'aide de la formule `1.5^(lock end - contract launch)`. Avec la fin du lock comme paramètre principal, les holders veMAV qui veulent maximiser leur puissance doivent prolonger leur lock fréquemment.

En ce qui concerne les wrappers, plusieurs projets existants ont déjà exprimé leur intention de s'appuyer sur Maverick ou veMAV, notamment Paladin, SpiralDAO et StakeDAO. Les guerres de MAV seront vicieuses, alors lisez bien tous les détails avant de verrouiller vos MAV ailleurs que dans le contrat veMAV.

## Perspectives d'avenir et mots d'adieu

Maverick est actuellement en ligne sur le mainnet, zkSync et BSC. Il est intéressant de remarquer à quel point il domine le volume sur zkSync, même avec une fraction de la  TVL de ses concurrents :

![zksync-dex-volume.png](img/2023/liquidity-shaping-maverick/zksync-dex-volume.png "Aperçu du volume traité par les principaux DEX sur zkSync (DeFiLlama)")

![zksync-dex-tvl.png](img/2023/liquidity-shaping-maverick/zksync-dex-tvl.png "Aperçu du TVL attiré par les principaux DEX sur zkSync (DeFiLlama)")

Sur le réseau principal, Maverick trouve son audience sur les paires ETH-LSDs (wstETH, swETH, etc.) et les stablecoins. La structure de liquidité efficace de Maverick est très compétitive par rapport à Curve, Uniswap et Balancer.

En ce qui concerne les jetons volatils, les LPs sont encore un peu timides, tout comme il a fallu quelques mois pour que les gens s'habituent à la nouveauté apportée par Uniswap V3. Il est intéressant de noter que les LPs expérimentent davantage sur zkSync, en particulier sur des paires telles que ETH/USDC, grâce à la baisse des coûts du gas, ce qui conduit à une efficacité globale du capital encore plus importante que sur le mainnet, voici les statistiques pour aujourd'hui (06 juillet 2023) : 

- Uniswap V3 - réseau principal : 0.23
- Maverick - réseau principal : 0.3
- Maverick - zkSync : 0.93

### Démarrer avec Maverick en tant qu'utilisateur

Il y a une courbe d'apprentissage pour Maverick, car comprendre comment structurer correctement la liquidité peut être intimidant en raison de toutes les options fournies. Pourtant, plus d'options signifient plus d'expressivité et, par conséquent, plus d'efficacité et de rendement lorsqu'elles sont exploitées de manière adéquate.

**Pour tirer le meilleur parti de Maverick en tant qu'utilisateur et découvrir le protocole dans un environnement où les frais sont peu élevés, je vous recommande de fournir vos premiers LPs sur zkSync** - car cela vous permettra de les modifier à peu de frais si nécessaire. Comme pour la plupart des nouveaux produits DeFi, la meilleure façon de le maîtriser est de l'utiliser et de voir comment il se comporte dans différentes conditions de marché, alors lancez-vous : vous pourriez également bénéficier d'un double airdrop, de sorte que l'expérience peut être très gratifiante.

N'hésitez pas également à aller voir les Boosted Pools, qui en plus de leurs incitations - ont une configuration de la liquidité pré-définie, elles sont donc plus accessibles pour les LPs.

### Liquidity Managers, il est temps de se réveiller !

Du côté des projets, **il est absolument nécessaire que les gestionnaires de liquidité comprennent et maîtrisent Maverick**, car c'est de loin la plateforme qui offre le plus d'efficacité en matière de liquidité. Je serais heureux de les aider dans ce processus, puisque c'est devenu ma spécialité. N'hésitez pas à me contacter si vous souhaitez discuter de la manière dont votre projet pourrait exploiter la mise en forme des liquidités.

{{< notice note >}}
Info : Au cas où vous auriez manqué la nouvelle, je conseille l'équipe de Maverick depuis l'année dernière.

**[Annonce : TokenBrice 🤝 Maverick](https://tokenbrice.xyz//content/posts/2023/maverickxtokenbrice.fr.md)** 
{{< /notice >}}

Il sera intéressant de voir comment se dérouleront les prochains mois de la guerre des DEX ; Maverick étant déjà régulièrement dans le top 5 des DEX Ethereum par volume traité, je pense qu'il n'est pas exagéré de l'envisager dans le top 3 d'ici la fin de l'année, au plus tard lorsque les jauges veMAV seront publiées.

J'espère que cet article vous a aidé à mieux comprendre le changement de paradigme que représente la transition du liquidity mining / ve(3,3) de base à la puissance de Maverick qui met en œuvre le façonnage de la liquidité par le vote. N'hésitez pas à suivre les événements en direct, en surveillant les données onchain comme le font les OGs.

Enfin, pour parfaire votre compréhension de Maverick à l'issue de la lecture de cette article, je ne peux que chaudement vous recommander le marathon réalisé avec Remi et Laurent de MEVCapital :

{{< youtube gvVVshJ0yK4 >}}

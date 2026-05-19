---
title: "Le volume appelle les frais : comment les principaux échanges décentralisés capturent-ils la valeur ?"
description: "Un regard sur le mécanisme de capture de valeur d'Uniswap, de Sushiswap et de Curve pour mieux comprendre comment la valeur s'accroît pour les détenteurs de leur tokens."
date: '2021-01-23T01:13:50.191Z'
reviewed: 2026-05-19
categories: [DEX]
tags: [DeFi, Ethereum, DEX, Decentralized Exchange, Uniswap, Sushiswap, Curve, Balancer, Bancor]
toc: true
tocNum: false
url: dex-echanges-decentralisées-capture-valeur
aliases:
  - p/dex-echanges-decentralisées-capture-valeur
image: /img/2021/dex-value-capture/cover-fr.png
difficulty: "intermediate"
---

J'ai partagé mon point de vue sur de nombreux protocoles DeFi sur ce blog, mais je me suis récemment rendu compte que je n'étais jamais revenu à l'essentiel : les DEX. C'est précisément ce que nous allons faire aujourd'hui, en abordant le sujet principalement en examinant les mécanismes de capture de la valeur.

Les DEX s'appuyant sur des AMM, comme Uniswap, Curve ou SushiSwap, ont tous connu cette année une croissance énorme, tant en termes de liquidités disponibles que de volume, tout comme les frais qu'ils ont perçus. Pour faire simple : **ces DEX sont maintenant les principaux collecteurs de frais qu'il y a en crypto, juste après le réseau Bitcoin et Ethereum eux-mêmes** :

![crypto-fees](/img/2021/dex-value-capture/fees.png)

C'est une réalisation impressionnante ! Aujourd'hui, nous allons donc examiner ce délicieux gâteau et comprendre comment il est divisé. Quelles sont les différentes approches ? À quoi sert leur token / comment établissent-ils leur modèle d'incitation ? Et ensuite, quel sera l'impact de l'arrivée des layer 2 sur tout cela ?

---

## La montée en puissance des Market Maker Automatisés (AMM)

Avec toutes les discussions autour des teneurs de marché automatisés (AMM) ces derniers temps, je voulais, comme d'habitude, prendre du recul et examiner l'état actuel du marché, la position des principaux acteurs et ce qui va suivre.

Nous discuterons des AMM, mais je laisserai à d'autres le soin de régler les détails techniques des bonding curves. Nous aborderons plutôt le sujet sous l'angle de la saisie de la valeur et de la tokenomique.

**L'essor et le développement des AMM a fondamentalement changé le marché**. Avant leur domination, les approches basées sur le carnet d'ordres étaient encore largement utilisées. L'un des principaux mérites des AMM est de changer la logique du service, car il devient **peer to contract** : il n'y a pas besoin d'un ordre correspondant de l'autre côté, grâce à la bonding curve, il y en a toujours un (dans les limites de liquidité et de slippage).

Je pense que c'est l'un des facteurs clés qui leur a permis de se développer en rationalisant tout ce qui concerne les échanges de tokens : de l'acte d'échange lui-même, mais aussi de l'apport de liquidité et même des choses comme la recherche d'un prix pour les actifs.

Nous avons donc notre beau gâteau de commissions DEX, plongeons maintenant dans le mécanisme de capture de la valeur des principaux services pour mieux comprendre leurs principales différences.

{{< notice note >}}
Pour la simplicité de cet article, nous n'aborderons pas les modèles Balancer et Bancor. Ce pourrait être un bon article de suivi.
{{< /notice >}}

---
## Mécanismes de capture de valeur en mode découverte

Au fil des différentes itérations et versions des principaux DEX, leurs mécanismes de capture de la valeur ont évolué. Au départ, il n'y avait pas nécessairement de token et une part des frais d'échange perçus saisie par celui-ci.

### Uniswap : Le besoin de liquidité

En effet, dans les premiers jours de l'AMM, la principale préoccupation était la liquidité - encore très rare à l'époque : Uniswap n'avait pas de token et n'en avait pas besoin pour être le pionnier du front de l'AMM. L'infrastructure initiale et toujours actuelle de distribution des commissions répond à cette exigence : une commission de **30 bps (0,3 %) est prélevée sur chaque transaction et distribuée aux fournisseurs de liquidité**.

C'était la solution idéale pour commencer, car vous avez un problème de liquidité : une liquidité suffisante permettra de réaliser des swaps sans trop de slippage, d'augmenter le volume (s'il y a un besoin pour le token/marché donné) et donc les revenus pour les LP.

Il n'y a actuellement aucune redevance ou saisie de valeur au niveau du token mais il est **prêt à être mis en œuvre** si le DAO devait le décider - la V2 du protocole expédié l'année dernière comprend une fonction de "redevance de protocole"[^1].

### SushiSwap : Capture de valeur au niveau du token

Depuis les premiers jours, l'un des principaux changements apportés au SushiSwap a été une légère réduction de cette redevance à 25 points de base pour **réorienter les 5 points de base restants vers les stakers de SUSHI**, ce qui permet une exposition à une part des frais collectés sur l'ensemble de l'échange plutôt qu'une logique uniquement par paire comme sur Uniswap.

Depuis la phase initiale de distribution, plusieurs ajustements ont été apportés mais le mécanisme est à peu près le même. Onsen a introduit un système de récompense par rotation de nouveaux pools pertinents. Plus important encore pour la tokenomique, ⅔ des récompenses SUSHI gagnées par l'exploitation des liquidités sont désormais acquises sur une période de 6 mois (vesting).

![sushiswap-onsen](/img/2021/dex-value-capture/sushi-onsen.png)

Cette évolution réduit les incitations pour la "liquidité mercenaire", en particulier pour les liquidités gérées par des vaults par exemple & permet de **s'assurer que les grands fournisseurs de liquidités sont également détenteurs de SUSHI à tout moment** (même jusqu'à 6 mois après la fin de leur exploitation), ce qui permet de mieux aligner les intérêts.

Pour parvenir à cette répartition, SushiSwap distribue une commission de 0,25 % pour chaque swap aux LP, tout comme les 0,30 % d'Uniswap. En plus de cette commission, une autre commission de 0,05 % est perçue sur chaque swap sous forme de LP tokens, elle est fréquemment vendue pour des SUSHI distribuée aux stakers.

Les améliorations apportées par Sushi sont pertinentes, mais à mes yeux, le véritable changement de jeu est le modèle Curve, alors voyons voir.

---

## Un aperçu de la fin du jeu ? Curve Finance & CRV

Le modèle de Curve est légèrement plus complexe que le précédent, mais il permet un alignement toujours meilleur des incitations entre les utilisateurs de la plate-forme et les détenteurs de tokens. Voyons comment.

Depuis le lancement du token CRV, les fournisseurs de liquidité sur Curve gagnent des tokens CRV en plus de leurs commissions habituelles (s'ils stakent). Et tout comme le SushiSwap, Curve a introduit une forme de capture de valeur au niveau du token CRV.

![Pools de Curve](/img/2021/dex-value-capture/curve-pools.png "Aperçu des principaux pools de Curve")

Mais le modèle est plus complexe, alors discutons de chaque partie et voyons comment elles interagissent les unes avec les autres.

### 1/ Tutoriel : Le timelock

Pour utiliser les tokens CRV au sein de Curve, le premier choix à faire est la durée de son engagement. L'unité de base est le veCRV, un CRV verrouillé et pondéré dans le temps qui permet la gouvernance. Pour être explicite : **pour pouvoir bénéficier des droits perçus et des autres caractéristiques décrites ci-dessous, vous devez verrouiller votre token CRV pendant au moins un an.**

Le mécanisme est assez simple, vous pouvez verrouiller pendant 1 à 4 ans. 4 ans vous donneront 1 veCRV par CRV, diminuant linéairement jusqu'à 0,25 veCRV par CRV pour une période d'un an. Comme nous l'avons dit précédemment, la veCRV est l'unité de base du système - elle déterminera donc le montant des frais ainsi que le pouvoir de stimulation (boost) et de gouvernance auquel vous aurez accès.

### 2/ Zone de mise à niveau : votre part des frais

Il suffit de placer et de verrouiller des tokens CRV dans le DAO pour avoir droit à une part des frais perçus sur Curve, mais ce n'est que la première étape du voyage. Les commissions sont fréquemment perçues et réglées pour des tokens 3pool LP. Le mécanisme a récemment été lancé et a commencé à distribuer des récompenses.

Veuillez noter que le rendement effectif fluctue car il est lié au volume d'échange de Curve et au prix d'acquisition des tokens CRV. Au moment de la rédaction du présent document, il est d'environ **0,29 $ par an pour 1 vecRV.**

{{< notice note >}}
Pour décrire la prochaine couche de l'oignon de Curve, j'aime utiliser une métaphore inspirée des jeux de rôle en ligne. En effet, il existe trois types de configurations qui conviennent pour décrire les trois prochaines étapes de Curve :

1. **PvE (Player vs Environment)** : où vous affrontez uniquement des monstres (mobs) contrôlés par l'IA
2. **PvP (contre les joueurs)** : lorsque vous vous battez contre d'autres joueurs dans un environnement déterminé (arène/champ de bataille)
3. **RvR (Realm vs Realm)** : où vous vous battez contre d'autres joueurs potentiellement partout (factions)

Nous utiliserons ce cadre de référence pour analyser les trois couches suivantes de l'oignon qu'est Curve.
{{< /notice >}}

### 3/ Le PvE de Curve - Stimulation des récompenses CRV

Comme indiqué précédemment, les fournisseurs de liquidités peuvent mettre en jeu leurs tokens LP pour gagner des CRV en plus de leurs commissions habituelles. Mais ils peuvent également **utiliser leurs tokens veCRV pour booster** un ou plusieurs de leurs pools, augmentant ainsi les CRV gagnée jusqu'à 2,5 fois.

Pour ce faire, il faut un montant de veCRV proportionnel à la valeur en dollars de la position de fourniture de liquidité renforcée. Le coût effectif (en veCRV) pour obtenir le maximum de stimulation n'est pas le même pour chaque pool, ce qui crée une première couche de jeux d'incitation/arbitrage.

![Curve CRV boosting](/img/2021/dex-value-capture/crv-boost.png "Il faut un montant différent de veCRV par $ déposé dans un pool donné pour obtenir le boost maximum.")

C'est un mécanisme intéressant qui permet un meilleur alignement des incitations : **Les personnes qui gagnent  beaucoup de CRV sont également des détenteurs de veCRV importants** (-> bloqués pendant 1 à 4 ans), ce qui permet un bon alignement des intérêts. Pourtant, ce n'est que la première et la plus amicale des couches du méta-jeu de Curve. Allons plus loin dans l'oignon.

### 4/ Le PvP de Curve - Le jeu du poids des jauges

>Si le pool-boosting est en PvE, les jauges sont l'arène PvP de Curve.

Les jauges sont un peu similaires au boosting, mais **au niveau de la plate-forme**. Les détenteurs de VCRV peuvent voter pour **décider de la part de CRV nouvellement frappés allouée à chaque pool**. Des restrictions supplémentaires s'appliquent ici pour empêcher la manipulation des votes :

* Le VeCRV doit être verrouillé avec au moins 7 jours restants.
* Le vote sur le poids des jauges ne peut être modifié par les utilisateurs que tous les 10 jours.

Il permet d'inciter de nouvelles pools, théoriquement sans l'impulsion nécessaire de l'équipe Curve.

### 5/ Le RvR de Curve - Gouvernance et gouvernance inter-protocolaire

La dernière couche de l'oignon réside dans la gouvernance de Curve : les détenteurs de veCRV peuvent voter sur les propositions de la DAO et avec au moins 2 500 veCRV, vous pouvez soumettre une proposition au DAO. Donc, pour résumer, une fois que vous détenez la veCRV, vous :

1. Gagnez une part des droits perçus par l'échange
2. Vous pouvez augmenter vos propres flux de CRV
3. Par le biais de jauges, influencer les futures émissions de CRV sur les pools de Curve.
4. Et enfin, en ce qui concerne la gouvernance, vous avez votre mot à dire sur les paramètres clés du système.

Alors que 1&2 est ce qui intéresse le plus les utilisateurs finaux, **les points 3&4 peuvent être incroyablement précieux pour d'autres dApps, projets DeFi et politiciens inter-protocolaire**[^2].

À partir de là, les possibilités sont pratiquement infinies :
1. Par exemple, imaginez un projet introduisant un nouveau stablecoin. Ne serait-il pas intéressant pour eux d'avoir un pouvoir de gouvernance au sein de Curve pour éventuellement l'inclure dans un pool Curve avec bonus CRV ?
2. Encore plus loin dans l'oignon, les projets DeFi **avec une trésorerie peuvent en allouer une partie au token CRV pour exploiter les avantages des 4 éléments** - 1&2 pour augmenter leurs flux de revenus de trésorerie et 3&4 pour rendre leur plateforme ou service plus attractif.
3. Une autre couche plus profonde : le **[vault yveCRV de Yearn](https://crv.ape.tax)**. Il offre de meilleurs rendements que si vous déposiez vos CRV vous-même (~1,3x), mais les déposants renoncent à la capacité de stimulation et de vote (3&4) en faveur de Yearn - qui peut alors utiliser cette capacité supplémentaire de stimulation/vote pour améliorer le rendement de ses produits.
4. Dernier niveau de profondeur : imaginez un service de crypto/DeFi de type relation presse dans quelques années. Je m'attends à ce qu'ils soient capables de **fournir d'autres projets avec une puissance de proposition** sur les principales DAO comme Curve ou Aave.

### 6/ Prochaines étapes pour Curve

Enfin, nous devons considérer une dernière dimension de Curve, car ce n'est pas n'importe quel DEX. En effet, dès le départ, Curve s'est spécialisé dans les **échanges d'actifs indexés** (pegged assets) et a été optimisé pour cela. L'échange a commencé avec les Stablecoins uniquement, mais nous avons maintenant aussi des représentations de BTC et d'ETH.

Grâce à l'augmentation des liquidités disponibles, Curve exploite maintenant les synergies de DeFi (avec Synthetix) pour proposer des swaps entre les différents actifs pegged disponibles sur Curve, tels que DAI -> wBTC ou USDT -> EURS.

C'est une innovation significative car cela ouvre des marchés actuellement peu ou pas couverts ailleurs (EURS) et permet de minimiser le slippage pour les grandes transactions.

Pour rester concis, les bondings curve d'Uniswap et de Sushiswap sont bien adaptées pour **supporter de nombreux swaps de petite ou moyenne taille, en particulier sur les grands pools** avec un faible glissement. Cependant, elles sont moins optimales pour les gros ordres car le slippage augmente proportionnellement à la part de liquidité du pool requise par la transaction.

{{< notice note >}}
Un service comme **[ParaSwap](https://paraswap.io)** vous aide à simplifier ce processus et à optimiser votre échange.
{{< /notice >}}

---

## Perspectives d'avenir : L2 et ses incitations

Pour conclure cet article, n'oublions pas le prochain changement tectonique pour l'espace Ethereum : la disponibilité croissante des layers 2.

L'année dernière, nous avons vu la valeur des transactions sur l'AMM exploser au détriment des approches basées sur le carnet d'ordres. Les AMM ont rationalisé l'ensemble de l'expérience et se sont révélées très utiles pour le layer 1, de sorte que nous pouvons raisonnablement espérer qu'ils ouvrent la voie aux échanges décentralisés sur L2 aussi.

**Loopring offre déjà un échange décentralisé en production:** un DEX L2 basé sur zk-Sync avec diverses incitations pour les fournisseurs de liquidité. Curve a également travaillé avec Zk-Sync, nous pouvons donc raisonnablement nous attendre à ce qu'ils livrent un produit L2 en direct cette année compte tenu des derniers développements avec Zk-Sync.

![Loopring V2 Stats](/img/2021/dex-value-capture/loopring.png "Les principales pools sur Loopring V2")

D'autre part, Synthetix a récemment déployé son réseau principal Optimism L2 et la force semble forte autour d'un déploiement Uniswap x Optimism. Je plaisantais l'autre jour en disant
> Synthetix Optimism L2 est le testnet d'Uniswap.

Il ne serait pas surprenant de voir l'implémentation du L2 d'Uniswap se déployer d'ici quelques semaines ou quelques mois.

Pendant que nous y sommes, qu'en est-il de tokoenomics x L2 ? Je m'attends à voir les incitations **LP aussi migrer vers la L2**, comme c'est déjà le cas avec Loopring. Synthetix accélère le démarrage de son L2 limité (stake/mint/burn uniquement) avec des incitations SNX.

Les services qui n'ont pas encore de token pourraient avoir un avantage ici car ils peuvent inciter directement le L2. D'autre part, les protocoles qui incitaient déjà fortement leur L1 pourraient manquer de puissance de feu (tokens) pour égaler les incitations offertes par les projets avec des tokens "L2-native".

Il sera fascinant d'observer les sorties des différentes couches 2 et leur impact sur l'utilisation des protocoles et la tokenomique.

{{< notice note >}}
![defi-france-live-16](/img/2021/dex-value-capture/defi-france-live-16.png)
On ne reçoit pas moins qu'0xMaki, une des principales figures derrière SushiSwap pour discuter du sujet ce lundi sur **👉 [la chaîne YouTube DeFi France](https://www.youtube.com/watch?v=JT8N7-gqTjA).**
{{< /notice >}}

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/c/DeFiFrance)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}

## Notes et références

[^1]: Vous trouverez plus d'informations dans la [Documentation Uniswap V2](https://uniswap.org/docs/v2/advanced-topics/fees/).
[^2]: Un concept [d'abord théorisé dans la lettre d'information Bankless]([https://newsletter.banklesshq.com/p/the-life-of-a-protocol-politician]) qui fait référence à une personne ou une entité spécialisée dans l'obtention d'une influence sur divers protocoles décentralisés et qui offre ensuite un accès sur le terrain à cette influence en tant que service.

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

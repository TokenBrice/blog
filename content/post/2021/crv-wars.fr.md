---
title: "⚔ Guerre du CRV : comprendre la course à l'accumulation de la capacité à influencer le protocole Curve Finance"
description: "Un guide concis pour suivre la course à l'accumulation CRV par tous les moyens possibles y compris l'achat de vote (bribes), et pour évaluer les stratégies Curve des protocoles DeFi"
date: '2021-09-28T01:13:50.191Z'
categories: [DeFi, Understanding]
tags: [DeFi, Ethereum, Finance décentralisée, Curve Finance, CRV, Polygon, Convex, CVX, Votium, vlCVX, veCRV, bribe.crv]
toc: true
tocNum: true
url: crv-wars
image: /img/2021/crv-wars/curve-wars-cover-tokenbrice.png
---

Depuis les premiers jours de Curve Finance et du lancement du token CRV, on attend, on envisage et on présume sur ce que la guerre des CRV pourrait amener. Désormais, avec le lancement de Convex puis de Bribe.crv et enfin Votium, tout s'accélère : les votes VeCRV, ça s'achète désormais ! Voyons donc comment cela impacte Curve et la DeFi dans son intégralité.

À première vue, la question est plutôt simple et directe :

1. Curve est le plus grand échange décentralisé de la DeFi en terme de valeur totale déposée.
2. Le token CRV donne accès à 1/ une part des frais collectés 2/ **une capacité de vote pour influencer l'émission de CRV future.**
3. => Avoir le contrôle d'une grande capacité de vote VeCRV permet de **grandement faciliter le développement d'une pool Curve**, puisque cela offre la possibilité de voter pour des rendements CRV importants sur la pool en question.

Néanmoins comme souvent en DeFi, tout n'est pas si simple et le diable est dans les détails. Pour comprendre les enjeux de la guerre des CRV, il faut avoir avoir **bien compris les différents outils construits dessus**. Cela vous permettra ensuite de juger de la pertinence des stratégies déployées par les différents projets qui cherchent à influencer Curve.


## Convex et la séparation du VeCRV

Avant d'analyser les champs de bataille - c'est-à-dire les différents outils utilisés dans cette guerre des CRV, il faut s'attarder plus en profondeur sur un en particulier : Convex. J'en ai déjà parlé sur ce blog, en expliquant [la dimension flywheel de Convex avec le CvxCRV](https://tokenbrice.xyz/content/posts/2021/defi-flywheel.fr.md).

Les interactions de Convex avec Curve vont largement au-delà du CvxCRV qui n'en est qu'un élément.


En fait, **on pourrait décrire Convex comme une séparation entre la gouvernance et les rendements sur VeCRV** en amplifiant chacun des éléments sur un token séparé, je m'explique :


### CvxCRV = VeCRV-yield++

CvxCRV correspond à un VeCRV possédé par Convex. Ils sont verrouillés à jamais, mais la liquidité disponible sur CvxCRV/CRV permet aux déposants de solder leur position.

**En termes de gouvernance, CvxCRV perd toutes ses capacités**. En effet, un possesseur de VeCRV peut voter sur les gauges (émission CRV) et votes de gouvernance. Un possesseur de CvxCRV n'a aucun autre bénéfice que le rendement.

Néanmoins, **le rendement est amplifié par rapport à une simple possession de VeCRV** :

1. Rendement en token 3pool - la part des frais collectés sur Curve - exactement comme VeCRV
2. Rendement en CRV (10% de tous les CRV farmés par Convex partagés entre tous les stakers CvxCRV)
3. Rendement en CVX quasiment équivalent
4. Potentiels airdrops comme Ellipsis

Ainsi, CvxCRV correspond à un compromis simple par rapport à VeCRV : les capacités de gouvernance sont perdues (-> vlCVX) mais en contrepartie le rendement est grandement amplifié et diversifié.


### vlCVX = VeCRV-gov++

À l'autre extrême, Convex propose une autre abstraction intéressante vis-à-vis de Curve. Il s'agit de son token natif CVX. En effet, **chaque CVX correspond à une capacité de vote VeCRV** (qui provient des CvxCRV).

Pour la mobiliser, le déposant doit "vote lock" ses CVX en vlCVX. Ils sont verrouillés pour 16 semaines + 3 jours et donnent ainsi l'accès à la capacité de gouvernance. À l'heure actuelle, le vlCVX est le chemin de loin le plus efficace économiquement pour accumuler de la capacité de vote Curve :


<table>
  <tr>
   <td>
   </td>
   <td>Prix
   </td>
   <td>Capacité de vote
   </td>
   <td>VeCRV-vote/$
   </td>
   <td>Engagement
   </td>
  </tr>
  <tr>
   <td>VeCRV
   </td>
   <td>$2.42
   </td>
   <td>1 veCRV
   </td>
   <td>0.41
   </td>
   <td>4 ans
   </td>
  </tr>
  <tr>
   <td>vlCVX
   </td>
   <td>$8.2
   </td>
   <td>12,75 VeCRV
   </td>
   <td>1.55
   </td>
   <td>16 semaines + 3j
   </td>
  </tr>
</table>


Outre la rentabilité accrue du CVX pour influencer Curve, l'engagement est également moins conséquent que sur VeCRV. Pour la table de comparaison, je suis parti sur une assomption de vérouillage 4 ans sur CRV. L'écart est encore plus en faveur de vlCVX pour des engagements moins longs.

{{< notice warning >}}
Le vlCVX a malgré tout un inconvénient : à l'issue des 16 semaines de verrouillage initiales, des pénalités sont appliquées aux déposants si les tokens restent inactifs pendant plus de 4 semaines.
{{< /notice >}}

Si vous voulez analyser plus en profondeur les rendements offerts par la délégation de CVX et l'achat de vote associé, n'hésitez pas à [lire cet article (EN)](https://medium.com/@portiadog/convex-finance-1cc6c9c1c733) qui propose des calculs plus détaillés :


![bribes-rewards](/img/2021/crv-wars/bribes-rewards.png "Estimation du rendement de la délégation de vote Curve via vlCVX")


### Bribes : une séparation pas si nette

La situation était claire, mais elle ne l'est pas restée longtemps. En effet, il convient tout d'abord de noter que vlCVX n'est pas dénué de rendement : **les possesseurs de vlCVX se partagent 6% de tous les CRV farmés par Convex, sous forme de CvxCRV**.

En outre, ce n'est potentiellement pas le seul rendement auquel les possesseurs de vlCVX sont éligibles. En effet, **la capacité de gouvernance peut également offrir un rendement conséquent via les mécanismes de bribe** (achat de votes).

Différents projets proposent ainsi des incitations pour voter sur la gauge d'une pool Curve donnée. Par exemple, Alchemix propose des récompenses en ALCX, son token natif, qui peut être claim chaque semaine par tous ceux qui ont utilisé leur VeCRV pour voter afin d'augmenter l'allocation CRV de la pool AlUSD.

À long terme, il n'est pas impossible que la séparation initiale prévue par Convex ne soit pas des plus honnêtes. À l'heure actuelle, le rendement sur cvxCRV est environ 60% tandis qu'il n'est qu'à 15% sur CVX. Néanmoins, **lorsque l'on ajoute les bribes dans l'équation, il n'est pas impossible que le rendement du vlCVX soit bien plus important que celui sur cvxCRV.**


## Les champs de bataille

Les services de "bribes" sont ainsi un élément essentiel de l'équation de gouvernance de Curve. Néanmoins avant de les creuser il faut rappeler le chemin de base (veCRV) qui définit le cadre de toutes ses variantes.

VeCRV s'obtient en verrouillant CRV pour une période allant jusqu'à 4 ans. Plus le verrouillage est long, plus le ratio VeCRV/CRV est proche de 1. **Le verrouillage s'épuise progressivement avec le temps ainsi que la capacité de vote**.

C'est pourquoi les vaults construits sur VeCRV opèrent sur une logique de verrouillage perpétuel à 4 ans : afin de préserver une capacité de vote toujours au plus proche du maximum possible, **ils "rafraîchissent" (refresh) le verrouillage fréquemment.**


![ecosysteme-vecrv-tokenbrice](/img/2021/crv-wars/ecosysteme-vecrv-tokenbrice.png "Aperçu de l'ecosystème construit sur veCRV")


### Bribe v0 : incitation directe sur les pools

Avant de vous parler de bribe, il faut rappeler qu'il existe une forme primitive disponible depuis les premiers jours de Curve : les incitations additionnelles (en plus des CRV) pour les apporteurs de liquidité. Synthetix a ainsi été pionnier avec le programme de liquidity mining en SNX sur la pool sUSD.

Les incitations directes sont cumulables avec les bribes, et c'est même recommandé. On verra plus bas comment MIM par exemple a obtenu beaucoup plus d'activité en partageant son budget entre incitation et bribes (après d'une phase initiale sans bribe).


### Bribe.crv de Cronje [sur veCRV]

Vous l'aurez donc compris, les "bribes" sont des achats de votes VeCRV. Ils sont payés à la semaine, généralement le vendredi (jour de prise en compte des votes).

Néanmoins, tout comme il y a plusieurs systèmes pour interagir avec VeCRV, plusieurs mécanismes existent également pour les bribes. On commence donc par celui qui a été disponible en premier : [http://bribe.crv.finance/](http://bribe.crv.finance/)

Ici, l'unité de base c'est le VeCRV. Bribe.crv est une simple interface qui résume les différentes offres et permet de récolter ses bribes. Le vote se fait directement sur Curve.

Après des débuts un peu timides, le service est de plus en plus utilisé et de nombreux projets proposent désormais des bribes. Les rendements des premières semaines ont été excellents, à voir s'ils dureront. Par exemple, j'ai touché **environ 10% de retour sur mes VeCRV (/ prix actuel) en 5 semaines** en votant pour la pool MIM et recevant des tokens SPELL en bribes.

On reviendra sur les résultats obtenus un peu plus bas.


### Votium [sur vlCVX]

L'alternative disponible, c'est [Votium](http://votium.app/). Ici, l'unité de base c'est le vlCVX, les deux services ne sont donc pas concurrents mais complémentaires.

Votium est plus récent donc les bribes disponibles sont encore moins nombreuses. Par contre, **Votium contrôle déjà une capacité de vote impressionnante : environ 8M CVX soit plus de 102M VeCRV**.

Ici le système est potentiellement plus passif qu'avec bribe.crv puisque les déposants peuvent déléguer à Votium qui se chargera de voter chaque semaine pour eux et récolter les bribes correspondants.

Même avec une délégation active, un déposant peut à tout moment reprendre le contrôle et voter pour une pool donnée, directement sur snapshot (-> pas de coût en gas). Le système est donc plus flexible que bribe.crv à ce niveau là.

D'autres services pour gérer les bribes sont également en développement avec une sortie prochaine. Jusqu'à présent le jeu des bribes s'est concentré essentiellement autour de CRV, mais [Paladin](https://www.paladin.vote/), par exemple, entend proposer un mécanisme similaire avec d'autres protocoles également.


## Mise en pratique : tactiques et résultats

Les bases conceptuelles sont un peu lourdes sur ce sujet, mais il est essentiel de les comprendre. Pour rendre le tout plus explicite, passons donc à la pratique avec des exemples concrets.


### Exemple de Spell/MIM

[Abracadabra](http://abracadabra.money/) est un service de type Maker. Différents actifs sont acceptés en tant que collatéral, dont des actifs productifs comme xSUSHI ou encore cvx3pool.

Tout comme Maker produit le DAI, Abracadabra produit un stablecoin (sur le dollar) baptisé MIM. La liquidité disponible sur MIM, ainsi que les opportunités de rendements sont donc un facteur essentiel du succès de la plateforme.

C'est pourquoi Abracadabra est passé progressivement par toutes les formes de bribes directes ou indirecte sur Curve :



1. Tout commence avec une incitation en SPELL (token de gouvernance) sur la pool Curve/MIM.
2. Quand bribe.crv est arrivé, **une partie de cette incitation a été réallouée en bribe** - distribuée donc aux possesseurs de veCRV qui votent pour la gauge MIM.
3. Désormais, avec l'arrivée du vlCVX, l'équipe considère la redirection du budget par ce biais.

En quelques semaines, la pool MIM a ainsi explosé sur Curve, à tous les niveaux :



* Les rendements en CRV ont été vraiment excellents certaines semaines
* Ce qui a attiré de la liquidité et du volume, réduisant légèrement le rendement mais augmentant la capacité à booster la pool
* Grâce à cette dynamique, MIM est désormais la cinquième pool Curve en terme de volume, avec un beau ratio volume/TVL.

![curve-pools](/img/2021/crv-wars/crv-pools.png "Aperçu des plus grandes pools sur Curve (volume)")

En outre, la pool est désormais bien équilibrée et plutôt dense (> $700M liquidité totale).

L'exemple de Abracadabra est extrêmement instructif, puisqu'il démontre toute la pertinence des abstractions construites sur VeCRV : **sans augmenter son budget total, Abracadabra a été en mesure d'attirer bien plus de liquidité qu'à l'époque de la simple incitation directe en SPELL.**

Vous comprenez donc que les projets DeFi qui tirent habilement profit des mécanismes de veCRV, cvxCRV et vlCVX ont un avantage indéniable (**économique ET politique**) face à ceux qui n'ont pas encore saisi toutes leurs subtilités.


### Exemple croisé : sdveCRV VS cvxCRV

En effet, **je considère désormais la compréhension de Curve et la capacité à influencer efficacement sa gouvernance comme une capacité essentielle et requise dans la plupart des projets DeFi, surtout pour les projets de stablecoins.**

Pas besoin de me croire sur parole néanmoins, comparons en pratique deux approches mises en place par des projets avec des enjeux similaires : les stratégies de liquidité sur cvxCRV (de Convex) et sdveCRV (de StakeDAO) - deux abstractions construites sur veCRV.

Bien que les situations soit similaires, il y a des différences de taille :



1. Commençons déjà par rappeler que Convex contrôle plus de 30 fois la quantité de CRV contrôlé par Stake (102M vs 3M).
2. En outre, sdveCRV a de graves problèmes avec son peg : 1 sdveCRV ~= 0.5 CRV


![sdvecrv-peg](/img/2021/crv-wars/sdvecrv-peg.png "Échange sdveCRV/CRV")

#### Plan de liquidité sdveCRV : incompréhension totale et échec cuisant

Passons donc à l'analyse. Initialement la liquidité sdveCRV était contre ETH tout comme pour Yearn. Depuis Convex, l'équipe Stake essaie de réagir pour rendre sdveCRV plus attractif.

Néanmoins, l'équipe n'a clairement pas pris le temps d'analyser la situation et s'est précipitée vers ce qui s'est avéré être **un des échecs de gouvernance les plus cuisants jamais observé sur Curve**.

Après avoir créé une pool sdveCRV/CRV anémique via la Curve Factory, un vote a été soumis pour y ajouter la contrôler gauge (= incentives CRV). Non seulement [le vote a été rejeté massivement](https://dao.curve.fi/vote/ownership/83) mais en outre **la pool sdveCRV est paramétrée de façon aberrante et absolument dangereuse pour les déposants.**

**Inciter les dépôts sur une telle pool serait revenu à envoyer les déposants vers l'abattoir**. En effet, le facteur A (paramètre d'amplification) de la pool est [défini à 200](https://curve.fi/factory/34) --- une valeur correcte pour des actifs qui suivent le même peg, mais délirante si un actif vaut deux fois l'autre. 

![sdvecrv-mim-crv-pools](/img/2021/crv-wars/sdvecrv-mim-crv-pools.png "Comparaison pools Curve (factory) sdvecrv et MIM")

Pour vous donner une idée, même la pool MIM mentionnée plus haut, absolument massive (7000x la liquidité de la pool sdveCRV) n'a pas encore atteint 200 de A factor (119 actuellement, en augmentation).

Ainsi, non seulement Stake n'a pas réussi à résoudre son problème de liquidité sur sdveCRV, mais en outre **un tel déroulé des événements soulève clairement la question de la compréhension des subtilités de Curve/Convex par l'équipe Stake**.

Pour faire revenir le sdveCRV au peg et développer sa liquidité, il leur faudra beaucoup d'effort, dans l'ordre :



* Revoir les paramètres de la pool
* Incitations directes en SDT sur la pool ?

Une fois ces étapes accomplies, l'équipe aurait alors une chance d'obtenir la gauge CRV sur cette pool, mais pas avant. La situation actuelle ressemble donc à une coûteuse impasse : **pas d'issue à moins de faire chauffer (encore plus) la planche à SDT**.


#### Plan de liquidité cvxCRV : décollage immédiat

Le plan de liquidité sur cvxCRV démontre au contraire à quel point le processus peut être efficace. Initialement (et encore aujourd'hui), la pool principale pour cvxCRV est sur Sushiswap, contre CRV.

Cette situation ne fait que très peu de sens : **Sushi est loin d'être optimal pour optimiser la liquidité sur des actifs qui suivent le même peg**. Ainsi, lorsque Curve a lancé les factory pools (V2), la [pool cvxCRV/CRV](https://curve.fi/factory/22) a été une des premières à émerger.

(Notez ici le A Factor à 50 - alors que cvxCRV tient bien plus son peg que sdveCRV...)

![cvxcrv-pool](/img/2021/crv-wars/cvxcrv-pool.png "Pool (factory) cvxCRV/CRV")

Sans avoir d'incitation de la part de Convex ou Curve, la pool a déjà vu un volume important transiter grâce aux agrégateurs de DEX comme Paraswap. Rapidement, il y a eu un vote pour y ajouter la gauge CRV qui est passé - et cette pool est désormais farmable directement via Convex.

La pool reste légèrement déséquilibrée (il y a tant à faire avec des CRV, qui deviennent de plus en plus rares…) mais elle apporte déjà une alternative compétitive à la pool SLP cvxCRV/CRV avec encore une fraction de sa liquidité. 


## Conclusion

J'espère que cet article vous aura aidé à saisir les subtilités de l'écosystème étendu de veCRV et leurs conséquences sur la bataille des CRV. 

Avant de conclure, je tiens à vous rappeler que comme d'habitude l'alpha se trouve dans les creux. Si vous avez compris cet article, n'hésitez pas à exporter l'analyse de la stratégie de liquidité à d'autres projets : je suis certain qu'elle sera instructive !

Je vous le dis souvent, mais ce sera jamais assez : non seulement Curve est le DEX le plus important en DeFi mais c'est également **le protocole le plus avancé en terme de gouvernance et de tokenomics de très loin par rapport à tout ce qu'il se fait d'autre**. Même si vous n'avez aucun intérêt pour Curve/Convex, il est indispensable de comprendre ces protocoles pour bien envisager ce qu'il se passe en DeFi… En espérant que cet article vous y aidera !

{{< notice tip >}}
Pour approfondir votre compréhension du CRV, pilier de la DeFi, je vous propose également deux sessions en direct avec Charlie; un membre de l'équipe Curve :

**[Marathon DeFi Curve Finance dans le détail](https://www.youtube.com/watch?v=G5PbqGtjSDQ)**
{{< /notice >}}

{{< youtube EjuPdHv1bX8 >}}

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

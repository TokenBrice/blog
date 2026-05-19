---
title: "🎲 PoolTogether : L'histoire de la loterie sans perte où tout le monde (y) gagne"
description: "Comment PoolTogether utilise la DeFi pour repenser la loterie sous forme d epargne ludique et moins predatrice."
date: '2021-12-20T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Yield]
tags: [DeFi, Ethereum, POOL, PoolTogether, Lottery, money games]
toc: true
tocNum: false
url: pool-together
aliases:
  - p/pool-together
image: /img/2021/pool-together/cover.png
difficulty: "beginner"
---


La DeFi a permis l’émergence d’un système financier alternatif construit sur des bases fondamentalement différentes : transparence, open-source, composabilité et résistance à la censure. De nombreux cas d'utilisation ont émergé et il est désormais possible d’acheter et d’échanger des tokens sans intermédiaire centralisé, mais aussi prêter ou emprunter et bien plus encore !

Notre sujet du jour, [PoolTogether](https://www.defiscan.info/protocols/pool-together-v5/ethereum) fait lui un pas de plus : il utilise et assemble différents services DeFi pour proposer un “jeu d’argent” d’un type nouveau, qui se veut à la fois plus amusant, mais aussi plus instructif et bien moins dangereux et délétère que sa contrepartie classique.

Je vous propose donc d’explorer ce protocole dans le détail : on commence par son contexte, avant d’analyser son fonctionnement et les différents enjeux qu’il implique. C’est parti !

---

## Le contexte : limites et dangers de la loterie classique

Ce chapitre me fait presque du mal à écrire tellement c’est une évidence mécanique pour moi, mais la réalisation n’est pas encore partagée. Concrètement d’un point de vue sociétal, la loterie est probablement aussi délétère que la cigarette. Il faut considérer :

1. Par sa structure même (jackpot possible et promu), la **loterie cible les populations les plus vulnérables**.
2. Malgré tout, **l’espérance de gain est négative**: les joueurs perdent en moyenne de l’argent en jouant.
3. Il y a aussi de **sérieuses conséquences pour les gagnants**, c’est une expérience complexe et nombreux finissent [fauchés ](https://www.communique-presse-jeu.com/ads/loterie-ils-ont-gagne-mais-ont-tout-perdu/)malgré tout quelques années plus tard. Les joueurs réguliers souffrent également de problèmes d’addiction.
4. La loterie était sauvagement taxée et possédée par l’Etat... jusqu’à présent. **La privatisation revient à donner les bénéfices générés par une activité nettement délétère pour la société à des entreprises privées** - la comparaison avec la cigarette prend encore plus de sens !
5. Enfin, et ça n'est pas propre à la loterie mais **tout aussi misérable, dénonçable et pitoyable** : les jeux d’argent ciblent souvent les populations les plus vulnérables pour leur publicité, en jouant sur les émotions. On l'a vu récemment avec les très nombreuses [publicités pour du paris sportif qui ciblent les jeunes de banlieue](https://www.vice.com/fr/article/n7wjjz/pourquoi-les-sites-de-paris-sportifs-ciblent-les-banlieusards).

![winamax-pub](/img/2021/pool-together/winamax-pub.jpg "Une des publicités les plus critiquées")

### Addictions, dépendances : conséquences

La suite est logique, mécanique et désespérante : en tendance longue, les mises explosent malgré un nombre de joueurs en berne :

![stats-fdj](/img/2021/pool-together/evolution-2007-2017.png)

Le sujet est complexe et comme pour la cigarette, souvent documenté et recherché par les prestataires de service de jeu/paris eux-mêmes. Les chiffres en disent long malgré tout : environ **17% des joueurs sont potentiellement en risque de dépendance ou d’addiction**.

![addictions](/img/2021/pool-together/addictions.png)

> "Enfin, en 2017, la pratique des jeux d’argent sur Internet (jeux de loterie, paris hippiques ou sportifs et poker) représentait 11,2 % des dépenses totales, part en constante progression depuis son autorisation en 2010."

Observatoire Francais des Drogues et Toxicomanie - [Les Francais et les jeux d’argent et de hasard](https://www.ofdt.fr/BDD/publications/docs/eftxjc2a6.pdf) et [graphique ORDT](https://www.ofdt.fr/odj/Donn%C3%A9es%20d%27activit%C3%A9%20Fran%C3%A7aise%20des%20jeux%20(FDJ)%20economie.gouv.fr.htm).

D’autres statistiques sont tout simplement désespérantes mais au final compréhensible : **plus la misère sociale et économique augmente, plus la promesse du jackpot de la loterie attire les crédules**, augmentant ainsi les gains privatisés de la FDJ et autres, et détruisant toujours un peu plus le tissu social.

On s’arrête là mais vous l’aurez compris : quand on sort des études financées par la FDJ ou associées, on se rend vite compte de l’ampleur de la casse sociale que la loterie provoque. Les 22.7% renvoyés aux collectivités ne suffisent clairement pas à compenser les coûts réels de ce “jeu” (vies ruinées, addictions, suicides, familles brisées, etc.).

#### Promotion d’un roman social délétère ?

Enfin, pour finir ce tableau qui dresse le contexte, je vous propose un dernier point plus subjectif : quid de l’impact de la loterie sur le **roman social** ? Le roman social, c’est comme le rêve américain : une fable qui constitue un des fondements de la construction de l’identité nationale (en l'occurrence : tout le monde peut réussir aux US s’ils travaillent assez dur).

C’est un véritable délire collectif (quelques éléments sur la méritocratie [par ici ](https://www.cairn.info/revue-le-debat-2018-5-page-176.htm)si vous en doutez encore), mais qui contribue malgré tout à **définir l’imaginaire associé à la réussite dans une société donnée.**

Permettez moi donc de poser la question : quel impact pour la loterie sur notre roman social ? Là encore c’est plutôt négatif je pense, car cela alimente la fable selon laquelle pour réussir il faut être né dans une bonne famille, ou bien “avoir de la chance” -> devenir une célébrité / pratique du sport de haut niveau ou loterie. **La loterie classique alimente ainsi la vacuité de nos aspirations contemporaines :** un facteur de plus contribuant à la médiocrité ambiante.

Ça, c’est dit. Rentrons maintenant dans le vif du sujet pour voir comment PoolTogether redistribue les cartes.


## L’essentiel pour comprendre le concept

Le principe de PoolTogether est au fond assez simple mais il y a également de nombreux détails et subtilités à cerner pour réellement comprendre ce que le protocole ambitionne de faire.

En DeFi, il y a différentes sources de rendements, par exemple un possesseur d’USDC, un stablecoin, peut le prêter à d’autres personnes pour générer un retour via un service comme Aave ou Compound. **Au fond, PoolTogether est une couche d’abstraction ludique construite au-dessus d’une telle source de rendements**. À haut niveau, cela donne quelque chose comme ça :



1. Des joueurs déposent de l’USDC dans la pool USDC sur PoolTogether - et reçoivent un token correspondant pour reconnaitre leur depot (PTaUSDC)
2. La pool (jeu de smart contracts) déploie les actifs dans différentes stratégies afin de produire un rendement. Le rendement est collecté et sert à alimenter le prix des gagnants.
3. Chaque USDC déposé dans la pool (⇒ PTaUSDC) correspond à un ticket de loterie potentiellement gagnant. Tous les jours, un tirage a lieu grâce à un mécanisme d’aléatoire auditable (ChainLink VRF) pour déterminer les nombreux gagnants, avec initialement 3 échelles de prix : 10 PTaUSDC, 100 PTaUSDC ou bien 2500 PTaUSDC le jackpot.

C’est cette infrastructure qui produit un rendement - et met seulement le rendement en jeu qui permet de qualifier Pool Together de **loterie** **sans perte**. À tout moment, **le joueur peut arrêter de jouer : il récupérera au minimum son capital initial engagé**, s’il n’a jamais gagné la loterie, ou alors plus.

Si on veut être très précis, le seul coût de Pool Together est le “opportunity cost of capital” : l’opportunité potentiellement perdue sur le capital mobilisé, qui pourrait théoriquement produire un meilleur rendement autrement.

---


## PoolTogether v3 : token POOL, sponsors et pool communautaires

Deux versions de PoolTogether sont en ligne : v3 et v4. Le concept reste le même mais l’infrastructure a grandement évolué. Alors avant de voir ce que la v4 a apporté, commençons par la v3 toujours pertinente et [accessible ici](https://app.pooltogether.com/).

Cette mise à jour a été lancée [en Octobre 2020](https://defirate.com/pooltogether-v3/) peu avant [le token POOL](https://medium.com/pooltogether/introducing-pool-23b09f36db48), en Février 2021. Elle apporte de nombreuses améliorations à l’infrastructure de PoolTogether.


### Sponsoring Pools et Reserve Factor

Ainsi, bien que l’explication schématique de tout à l’heure soit utile, il faut y ajouter deux premières subtilités : les sponsorship pools et le reserve factor contrôlé par la gouvernance.



1. Commençons par le plus simple : le **sponsoring**. L’idée c’est de permettre d’avoir du “capital non-joueur” pour augmenter les gains des joueurs : ce capital contribue au rendement produit, mais n’a pas de chance de gagner. Au début, c’était envisagé dans une perspective plutôt bénévole, mais avec le lancement du token les sponsors sont désormais éligibles pour des récompenses en POOL.
2. Le système de **réserve** est encore plus simple : chaque pool a un _Reserve Factor_ qui correspond à un % du rendement capturée par la pool directement. Ces fonds sont utilisés pour garantir la pérennité du protocole.

Avec la v3, on a également vu l’arrivée des _Community Pools_, des pools créées par la communauté directement sur les tokens de leur choix, du moment qu’ils ont une source de rendement ainsi que de nombreuses autres additions qui ont eu plus ou moins de succès.


### 3,3T, Lootboxes & PoolTogether sur Polygon

Par exemple, Olympus DAO propose un _3,3 Together_, où les joueurs mettent en jeu leur rebase OHM : tous les trois jours la rebase de tous les joueurs est distribuée aux trois gagnants.

Ils avaient également d’autres idées innovantes en v3 mais qui n’ont pas pris, principalement à cause des coûts en gas du mainnet. Par exemple, chaque pool a sa _Lootbox_ qui permet à n’importe qui de rajouter un token arbitraire en prix ou même un NFT ! Il suffit de l’envoyer à l’adresse de la lootbox et lorsque le prochain prix sera distribué le NFT/token est envoyé automatiquement au gagnant.

La v3 a également marqué l’arrivée du token POOL quelques mois plus tard et de son airdrop dont on reparlera plus bas.

Enfin, la v3 a également marqué l’arrivée de PoolTogether sur d’autres chaines comme Polygon ou BSC. Néanmoins cette logique connait ses limites car elle aboutit également à une fragmentation de la liquidité.

---


## PoolTogether v4 : Tsunami avec approche cross-chain novatrice

La v4 constitue une itération très importante sur la base proposée en v3. Ici, l’expérience a été simplifiée et retravaillée pour la rendre la plus accessible et fun possible : et ça marche ! Voyons donc comment.


### Approche cross-chain égalitaire

On va bien détailler ce point car il est crucial, PoolTogether a été pionnier en la matière et c’est une dimension qu’on retrouve sur tous les projets : **la stratégie cross-chain**. Elle a pour but d’offrir le même service, quelque soit la chaîne utilisée par l’utilisateur. J’y viens mais avant ça, prenons le temps de comprendre l’approche cross-chain classique de réplication et ses conséquences.


#### L’approche basique : réplication

La plupart des projets se contentent de **répliquer leur service sur toutes les chaînes** : c’est le cas de Sushi par exemple présent sur plus de dix chaînes, mais aussi Pool Together v3 comme décrit plus haut.

Cette approche a le mérite de la simplicité et permet l’accès au service sur toutes les chaînes couvertes - mais elle aboutit à **la fragmentation de la liquidité** ce qui peut rendre ce service moins qualitatif sur les “petites chaînes". Ainsi les joueurs PT v3 Polygon USDC, désormais peu nombreux, jouent pour un prix hebdomadaire de $69. De l’autre coté les joueurs PT v4 USDC se partagent un prix journalier de plus de $100 000.


#### Tsunami

Ainsi avec PoolTogether v4 arrive le modèle baptisé Tsunami où toutes les chaînes sont égales. Pour se faire, PoolTogether introduit une couche d’abstraction entre toutes les chaînes pour redistribuer les prix si nécessaire.

Cela permet de **mutualiser les fonds des déposants sur toutes les chaînes** pour offrir un grand prix attractif plutôt que de multiplier les pools et diviser les prix. Une des conséquences est de permettre aux joueurs sur Polygon (où le coût en gas du dépôt est marginal) de jouer avec les mêmes chances et la même espérance de gain que les joueurs mainnet.

Alors bien sûr, cela nécessite plus de travail de développement et d'implémentation et il y a des conséquences aussi pour les joueurs, la plus notable étant **un délai de un jour entre le dépôt initial et l’éligibilité pour le premier tirage**. Mais ça n’est pas un compromis trop lourd à supporter considérant le fait que PoolTogether se veut être un jeu promouvant l’épargne sur le long terme.


### Révision du modèle de prix

Là où la v3 optait pour de la flexibilité, avec des pools ayant des tirages journaliers ou hebdomadaires, la pool unique v4 peut se permettre un **tirage journalier** vu sa taille. En outre, la structure des prix a été revue afin d'allouer plus de petits prix pour rendre l’expérience un peu moins aléatoire sur le long-terme.

![prize-breakdown-old](/img/2021/pool-together/prize-breakdown-old.png "Première logique de distribution des prix PTv4")

La logique du jackpot est préservée avec le premier et unique gagnant qui empoche $2500 tout de même, mais il y a également près de 720 autres gagnants potentiellement grâce aux prix de $100 et $10.

![tokenbrice-pooltogether-winning](/img/2021/pool-together/winning.png "Environ 2 semaines de tirage sur 5000 PTaUSDC")

En réalité, le nombre de joueurs gagnants est plus faible car il est possible de gagner plusieurs prix à la fois. Néanmoins cette approche permet également de lisser le revenu pour les gros déposants, qui remportent fréquemment des récompenses de $10 ou $100, potentiellement même tous les jours si le dépôt est assez conséquent.

Cette distribution permet ainsi de récompenser fréquemment les joueurs qui utilisent PoolTogether dans une logique d’épargne tout en préservant l’esprit du jeu :

1. Une chance décente (en fonction de la taille du dépôt) d’avoir de petits gains (prix $10 et $100)
2. & faible probabilité d’avoir un gain massif : le jackpot de $2500.

Au-delà du modèle de prix, c’est toute l’expérience autour de l’allocation des prix qui a été revue avec la v4. La gouvernance a d’ailleurs continué a itéré et récemment voté une refonte de la structure des prix : [PTIP-47: Prize Adjustments](https://gov.pooltogether.com/t/ptip-47-prize-adjustments/1752).

![prize-breakdown](/img/2021/pool-together/prize-breakdown.png "La nouvelle distribution des prix")

### Une expérience plus satisfaisante

De nombreux paramètres et détails ont été ajustés pour rendre l’expérience de gain plus fun et agréable. La liste exhaustive est sur [la documentation de PoolTogether](https://docs.pooltogether.com/faq/v3-to-v4-differences), on se contentera de l’essentiel.

Tout d’abord, les gains passent dans une **logique de claim**, là où avant ils arrivaient directement dans le wallet. Pour les joueurs, cela rend les gains plus simples à comprendre et quantifier. En outre, ils sont désormais payés en PTaUSDC, le ticket de loterie PoolTogether v4 et sont donc **composés automatiquement** : gagner augmente vos chances de gagner, avec un simple claim !

![comparaison-pt-vs-epargne](/img/2021/pool-together/comparaison.png "PoolTogether vs l'épargne")

**Les joueurs ont 60 jours pour réclamer leur récompense**, ce qui garantit une forme de suivi et d’engagement, mais permet également une interaction avec le protocole quasiment totalement passive pour ceux qui le souhaitent : dépôt > tous les 59j : claim > retrait quand désiré.

---

On a mentionné le token POOL a plusieurs reprises sans le creuser : c’était volontaire. Maintenant que le système est clair pour vous, je vous propose de finir en analysant sa proposition de valeur.


## Le token POOL

On va parler airdrop bien sûr, mais aussi liquidité et bien évidemment gouvernance : c’est parti !


### Airdrop : tout le monde a gagné !

Pour lancer le token le plus fun de la DeFi, il ne pouvait pas y avoir autre chose qu’un airdrop évidemment. C’est un des airdrops rétroactifs qui a suivi dans le sillage d’Uniswap, mais qui est arrivé encore assez tôt pour ne pas avoir été abusé à outrance par les infameux chasseurs d’airdrops.

**14 % du total supply de POOL** a été distribué aux joueurs qui ont participé avant le 14 janvier 2021, avec une pondération en fonction du montant et de la durée du dépôt. Les joueurs de la première heure, même avec de petits montants, ont ainsi eu une très belle surprise.


### Incitations POOL et LP (v3)

Qui dit token signifie également le plus souvent incitations : PoolTogether ne fait pas défaut à la règle.

Avec le token sont arrivées des incitations en POOL pour tous les joueurs; ainsi que des ajustements sur le modèle de sponsoring décrit plus haut. Il y a également un enjeu de liquidité sur le token POOL désormais.

Après avoir commencé par un modèle d’incitation classique pour les LPs, la gouvernance a décidé d’explorer un modèle qui permet au protocole de [contrôler sa propre liquidité (PTIP-40](https://gov.pooltogether.com/t/ptip-40-olympus-lp-incentives-pool-pool-distribution/1638) grâce au bonding (Ohm-like).


### Définir le fun, ensemble

Le POOL sert ainsi à prendre part aux décisions du protocole et aider à affiner le modèle. En outre, l’implémentation de la gouvernance elle-même est marrante elle aussi. Pour voter, il faut déposer ses tokens POOL dans la pool POOL sur PoolTogether : tout en ayant un rendement de base + des chances de gagner des prix, les joueurs peuvent ainsi se prononcer sur les décisions de gouvernance.

Je qualifie parfois PoolTogether de “protocole le plus fun de toute la DeFi”, une affirmation véridique mais qu’on peut pousser encore plus loin.

La gouvernance de PoolTogether, avec ses décisions, travaille à définir ce qu’est le “fun optimal”, avec des questions très concrètes, comme le nombre de prix ou leur distribution. Avec le lancement de la v4, le nombre de prix a grandement augmenté ce qui permet à plus de joueurs de gagner : plus de la moitié des wallets uniques qui jouent à PTv4 ont gagné au moins une fois :


C’est un bon début, mais il est sans doute possible d’affiner encore plus le modèle pour réjouir toujours plus de joueurs en promouvant l’épargne long terme positivement.


## 🤗 PT Ensemble TokenBrice Live

Je vous quitte sur une offre difficile à refuser : et **si on jouait à PoolTogether ensemble** ? Les règles sont simples : j’ai effectué un dépôt PoolTogether v4 Polygon avec mon wallet public tokenbrice.eth. Toutes les 2 semaines je collecte les récompenses : la moitié repart dans le pot, l’autre moitié est gagnée en giveway par un membre de l’audience Twitch.

Le gagnant reçoit directement des PTaUSDC dans son wallet qu’il n’a plus qu’à activer pour lui aussi jouer de son côté : **le cercle vertueux sans fin de la loterie sans perte** !

Ça se passe sur [ma chaîne Twitch chaque mardi à 17h ](twitch.tv/tokenbrice): abonnez-vous et activez les notifications pour ne rater aucun live. Je les annonce également [sur Twitter](https://twitter.com/TokenBrice).

---

Si vous m’avez lu jusqu’ici, vous reprendrez bien un peu d’alpha ?

**La logique sans perte de PoolTogether s’exporte au-delà de la loterie / épargne**. De nombreux mécanismes sociaux et jeux autour de l’argent peuvent être concernés : paris sportifs, marchés prédictifs, assurance, etc. La famille sans perte sera grande, et PoolTogether connaît déjà un premier cousin qui s’attaque aux prédictions markets : [EntropyFi](https://docs.entropyfi.com/user-guide/game-explained).

Pour aller plus loin, regardez le Marathon Pool Together avec Pierrick :

{{< youtube zzfQ289dhW4 >}}

---

Faites vos jeux,
- 🎲 rien ne va plus [logique archaïque]
- (🎲,🎲) tout ira bien [web3]

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

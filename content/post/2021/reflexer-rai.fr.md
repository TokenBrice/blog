---
title: "🗿 Pourquoi, comment et qu'est-ce que le RAI ?"
description: "Le RAI de Reflexer est un nouveau type d'actif encore unique en DeFi. Il s'appuie également sur un système avec un plan de dégouvernance. Voyons donc comment s'extraire tout à la fois des risques liés aux monnaies fiduciaires, à la centralisation et à la confiance."
date: '2021-09-01T01:13:50.191Z'
categories: [Stablecoin, Lending]
tags: [DeFi, Ethereum, Stablecoins, Reflexer, RAI, Maker, Liquity]
toc: true
tocNum: true
url: reflexer-rai
image: /img/2021/reflexer-rai/cover.gif
difficulty: "intermediate"
---

RAI est une drôle de bête dont la compréhension ou l'intérêt échappe encore à de nombreuses personnes, y compris des gens vraiment calés en DeFi. Il était donc temps de vous proposer un article assez exhaustif dédié à son sujet. J'y ai inclus tout ce que j'estimais pertinent pour comprendre pourquoi un actif comme RAI est nécessaire, ce qu'il apporte et comment il fonctionne.

Préparez-vous un café et accrochez-vous, on est parti pour une belle promenade !


## Comprendre le contexte de RAI

Avant même de commencer à rentrer dans le vif du sujet, je pense qu'il est essentiel de bien comprendre le contexte autour de RAI : c'est-à-dire les principaux actifs stables utilisés aujourd'hui ainsi que leurs limites.

Le contexte pour bien comprendre RAI est assez dense, mais la bonne nouvelle c'est que ce n'est pas la première fois que je traite ce sujet sur le blog. Je vous renvoie donc vers des lectures pertinentes pour approfondir :



1. [Actifs à vocation stable sur Ethereum : quelles approches et quels enjeux ?](https://tokenbrice.xyz/fr/actifs-stables-ethereum/)
2. [Comprendre les innovations sur les marchés monétaires pour envisager leur avenir](https://tokenbrice.xyz/fr/marche-monetaire-innovations/)

Si vous n'avez pas le temps d'explorer le concept approfondi avec les articles proposés au-dessus, voici les deux points essentiels à retenir pour bien comprendre la suite :

1. À l'heure actuelle, **l'écrasante majorité du besoin en stablecoin est couverte par des solutions centralisées nécessitant de la confiance**, les plus utilisées étant USDT (~66 milliard) et USDC (~27 milliard).
2. Quelque soit vos thèses économiques de prédilection, notamment en termes d'inflation, je pense qu'on peut facilement s'accorder sur le besoin d'actifs stables qui ne sont pas corrélés à une monnaie fiduciaire (=gérée par un état).


### Le piège du wUSDC

J'utilise le terme "wrapped USDC" (wUSDC) pour expliciter une situation fréquente dans les stablecoins alternatifs : il permet de décrire de manière concise et appropriée **les solutions qui utilisent essentiellement USDC comme collatéral**, un stablecoin de confiance garanti par un organisme central (Circle).

Dans une situation telle, inutile d'aller plus loin, même pas besoin d'analyser les détails du système : puisque leur collatéral principal peut être gelé ou saisi, **les stablecoins produits de cette manière ne peuvent pas être considérés comme décentralisés ou trustless.** 

Cette famille connaît étonnamment de nombreux adeptes, les principaux étant Maker et Frax.


#### Maker = une majorité de collatéraux nécessitant de la confiance

Avec [Maker (DAI)](https://www.defiscan.info/protocols/sky/ethereum), **environ 60% des DAI sont mintés (frapper monnaie) avec USDC comme collatéral**, chiffre auquel il faut ajouter ceux mintés depuis d'autres collatéraux nécessitant de la confiance: wBTC, TUSD, GUSD, PAX, USDT, renBTC + toutes les paires UniV2 impliquant au moins l'un de ces tokens + tous les collatéraux issus du monde réel comme Centrifuge: New Silver. [Détail sur DAIStats](https://daistats.com/#/).

![dai-collateral](/img/2021/reflexer-rai/dai-collateral.png "Aperçu de la distribution des collatéraux utilisés pour garantir le DAI dans le système MakerDAO.
")

Note : le PSM est un module qui permet d'éviter les envolées de prix sur le DAI au-dessus du dollar. Les DAI mintés par le PSM le sont donc de manière automatique lorsque cela est nécessaire.

La première version de Maker, avant la mise à jour Multi Collateral DAI ([MCD - 18/11/2019](https://medium.com/@MakerDAO/update-the-road-to-multi-collateral-dai-2d4c48092270)) utilisait uniquement ETH comme collatéral et présentait ainsi des garanties bien plus crédibles. Ça n'est plus du tout le cas aujourd'hui. 

🙏 Je remercie néanmoins chaleureusement l'équipe MakerDAO pour leurs très nombreuses contributions à l'écosystème - le modèle Maker MCD est même utilisé comme base par Reflexer !


#### FRAX ? Garanti par l'USDC ou rien (algorithmique)

**Côté FRAX, seul l'USDC est utilisé en collatéral**, sous différentes formes - soit dans Yearn/Compound/Aave pour produire un rendement, soit via les [AMOs (Algorithmic Market Operations Controller](https://docs.frax.finance/amo/overview)). Voici le détail des actifs qui servent à garantir le FRAX, [disponible sur le site officiel](https://app.frax.finance/).

![frax-collateral](/img/2021/reflexer-rai/frax-collateral.png "Aperçu des collatéraux utilisés dans Frax : USDC et toutes ses variantes yield-bearing (risques techniques additionnels) + une part algorithmique (sans collatéral) variable.
")

Frax tout comme DAI développent une myriade d'approches intéressantes, mais comme leur base est centralisée, **ils ne peuvent être considérés comme quelque chose d'autre qu'un mécanisme d'amplification de la liquidité disponible sur USDC, au mieux**. Ils apportent néanmoins **des contributions intéressantes en termes de recherche fondamentale** qui pourront aider à établir une solution plus optimale et qui ne nécessite pas de confiance (trustless).


### Existe-t-il des alternatives pertinentes à RAI?

À ce jour, RAI est un actif unique sans alternative comparable. Cependant il existe des systèmes qui partagent certaines caractéristiques avec RAI, comme **l'utilisation exclusive d'ETH comme collatéral**. 

Ainsi, si vous êtes prêts à vous exposer au dollar, Liquity propose une alternative très pertinente qui a également **le mérite d'être totalement inarrêtable** (ce qui n'est pas encore le cas de RAI) : les contrats n'ont aucune fonction administrative, exactement comme Uniswap V1/V2. Il reste cependant bien sûr les oracles (nécessaires pour un service d'emprunt) et les risques associés.

Maintenant que le décor est posé, passons au plat principal : il est temps d'étudier les mécanismes sous-jacents de RAI. On commence par son minting dans la perspective d'un utilisateur avant d'approfondir sur ce qu'est concrètement RAI et comment il fonctionne.


## Comment le RAI se crée ?

Le RAI de Reflexer est en quelque sorte **à la fois la forme première et finale du DAI de Maker**. Première, dans le sens qu'il revient aux promesses du DAI original (le SAI) : seul l'ETH est utilisé comme collatéral et finale dans la mesure où RAI arrive à s'extraire de la dépendance au dollar.

Reflexer s'appuie ainsi sur une base Maker MCD avec plusieurs changements, notamment l'incorporation du PID controller, la protection contre les liquidations et bien d'autres. On va tranquillement déplier tout ça mais commençons déjà par voir comment le système fonctionne dans la perspective d'un utilisateur.

Tout comme sur Maker, RAI est créé directement par les utilisateurs de Reflexer. Ceux-ci peuvent ouvrir **un "safe" qui leur permet de mettre en jeu des ETH et minter une quantité proportionnelle de RAI**. Chaque utilisateur peut choisir la quantité de RAI minté pour une même somme d'ETH mise en jeu (-> différents niveaux de risque) et doit gérer sa position. **Les liquidations sont possibles et nécessaires** car elles permettent de s'assurer qu'il y ait toujours une valeur en ETH dans le système suffisante pour garantir les RAI émis.

Néanmoins le système innove ici par rapport à Maker grâce à sa fonction "Savior". Elle permet **d'utiliser une position d'apport de liquidité RAI/ETH sur Uniswap V2 comme garantie pour un safe**. Ainsi, si le prix de l'ETH venait à baisser brutalement, ce qui pourrait mettre un safe ouvert et protégé par cette fonction à risque de liquidation, **le Savior retire automatiquement la quantité de liquidité nécessaire pour faire revenir le safe au niveau de collatéralisation désiré**.

Cela permet ainsi aux utilisateurs qui mintent du RAI utilisé ensuite pour l'apport de liquidité de dormir bien plus sereinement !


## Mais RAI, c'est quoi en fait ?

RAI est une nouvelle classe d'actifs à lui tout seul. Il a pour vocation d'être **à faible volatilité, sans pour autant s'appuyer sur un autre actif stable** (monnaie fiduciaire ou or sont les sources les plus classiques). Pour ce faire, RAI s'appuie sur un système qui réagit dynamiquement aux conditions du marché.

Dans le cas de RAI, deux paramètres essentiels sont à prendre en compte :



1. **Le prix de rédemption** (redemption price) = valeur d'une unité de dette dans le système
2. **Le prix sur le marché** (market price) = prix de RAI observé sur le marché

Le système n'a bien sûr pas de contrôle sur le prix de RAI observé sur le marché, qui est déterminé par les acheteurs et les vendeurs. Néanmoins, il peut faire ajuster progressivement certains paramètres pour modifier le prix de rédemption et **faire converger les deux prix à terme**.

On fait donc face à une situation assez facilement généralisable incarnée par un pan entier de l'ingénierie et baptisée **la théorie du contrôle** :

![theorie-du-controle](/img/2021/reflexer-rai/theorie-du-controle.png "Boucle d'asservissement. Ce graphique, ainsi que les deux qui vont suivre sont issus de la traduction française du whitepaper RAI - un grand merci à PhilH & Ben.Oxmo pour leur travail qualitatif
")

Dans le cas de RAI, **le régulateur est algorithmique** et là encore assez standard : c'est le fameux **"PID controller"**. Il repose sur une formule mathématique assez dense qu'il n'est pas nécessaire de comprendre pour saisir la pertinence du système.

Il faut saisir néanmoins un point essentiel : l'inertie inhérente au système. Le régulateur ne peut pas se permettre de faire de brusques changements des paramètres (qui nuiraient à sa relative stabilité), il doit donc opérer dans **une logique plus itérative et progressive**.

Une fois ça saisi, je me permets de rappeler que le système par lui-même ne peut rien sur le prix de RAI. Tout ce qu'il peut faire, c'est faire varier le taux de rédemption, ce qui permet de moduler les incitations des participants du système. Cela crée ainsi des **opportunités d'arbitrage** pour les participants dont l'exécution permet de se rapprocher de l'équilibre entre prix de rédemption et prix sur le marché.

Voyons ça concrètement en pratique.

On retrouve ici une logique qui rappelle les [stablecoins algorithmiques](https://tokenbrice.xyz/fr/algorithmic-stablecoins/), bien que le produit final du système soit totalement différent.


### Quand le prix du marché > prix de rédemption

On commence par cette situation car elle est plus simple à comprendre à mon avis. Dans le cas où le prix sur le marché dépasse le prix de rédemption. Cela signifie donc que toute personne avec des ETH disponibles pourrait potentiellement générer un profit en arbitrant le marché :



1. Dépôt de ETH et mint du RAI ;
2. Vente de RAI sur le marché pour un profit ;
3. (Quand prix du marché &lt; rédemption) rachat de RAI pour rembourser la dette et libérer les ETH. La différence entre les 2 prix sur RAI - frais en gas correspond au profit généré.

![marchesupredemption](/img/2021/reflexer-rai/marchesupredemption.PNG)


Cette situation est d'autant plus intéressante pour ceux qui ont déjà des safes avec de la capacité disponible : ils s'épargnent une étape du scénario présenté plus haut.

Dans ce scénario, il y a donc une incitation à minter du RAI (->augmentation du supply) et à le revendre sur le marché (->pression baissière) qui permettent de progressivement réduire le prix sur le marché, le faisant ainsi converger vers le prix de rédemption. 


### Quand le prix du marché &lt; prix de rédemption

Dans le cas inverse, le taux de rédemption devient positif, ce qui a pour effet de rendre plus coûteuse la dette déjà existante. Les utilisateurs avec des safes actifs ont ainsi intérêt à rembourser leur dette, ce qui a pour effet de réduire le supply de RAI disponible. 

![marcheinfredemption](/img/2021/reflexer-rai/marcheinfredemption.png)


En outre, s'ils avaient convertis leur RAI pour un autre actif (par exemple ETH pour une exposition avec levier), ils devront acquérir des RAI sur le marché (->pression haussière) afin d'être en capacité de rembourser leur dette.

Vous l'aurez compris, les acteurs du système Reflexer ont tout intérêt à suivre le taux de rédemption et réagir en conséquence. Si vous avez un safe actif, je vous invite à le consulter régulièrement - [il est visible sur le site de Reflexer.](https://stats.reflexer.finance/)

Ce taux impacte moins directement les simples possesseurs de RAI, surtout s'ils les utilisent pour produire un rendement (qui peut compenser un taux négatif) mais c'est tout de même une métrique à garder en tête.


### Ajustement dynamique du taux de rédemption

**L'ajustement dynamique du taux de rédemption est une des fonctionnalités essentielles de Reflexer / RAI**. Pour mieux comprendre pourquoi c'est critique, analysons la situation sur Maker pré-MCD :



1. La demande en DAI correspond à (une partie de) la demande pour des stablecoins.
2. Néanmoins, les DAI sont créés en leverageant de l'ETH, ils dépendent donc du besoin/appétit pour du levier sur ETH, une donnée indépendante de la demande pour des stablecoins qui dépend surtout des conditions générales du marchés (bear ou bull et autres).
3. Si la demande est plus forte que l'offre, sur Maker, il n'y a aucun ajustement dynamique. Il faut attendre un vote de la gouvernance (et les délais qui vont avec) afin d'abaisser le Stability Fee. Et c'est pareil dans l'autre sens (offre trop importante).

Ainsi, **l'équilibre entre le côté offre et demande de l'équation est presque impossible à maintenir**, ce qui explique pourquoi le DAI pré-MCD pouvait se retrouver souvent au-dessus de son peg. Maker a résolu ce problème en ajoutant de nombreux types de collatéraux, dont des stablecoins non trustless puis le PSM qui minte automatiquement des DAI depuis USDC quand nécessaire. La solution proposée par Reflexer (ajustement dynamique du taux de rédemption) a le mérite de **résoudre le problème au niveau du système lui-même**, ce qui permet de garder ETH comme seul collatéral.


## FLX et le plan “dégouvernance" de RAI

Outre le RAI, le système de Reflexer a également un second token, FLX, le token de dégouvernance ("ungovernance"). Il est utilisé pour la gouvernance du système et sert également de mécanisme de liquidité de dernier recours (en cas de mauvaise dette), avec un système assez similaire au Safety Module d'Aave.

Le token FLX peut être acheté sur le marché, mais il est surtout **distribué aux principaux acteurs impliqués dans le système** - [la liste exhaustive des incitations en FLX](https://app.reflexer.finance/earn/incentives) est disponible sur le site de Reflexer.

Ainsi, sont éligibles pour des FLX (claimables sur le site de Reflexer, distribution mensuelle) :



1. Les possesseurs de safes qui apportent leur RAI en liquidité sur la paire UNIv2 ETH/RAI (migration en cours, fin prochaine) ou encore UNIv3 RAI/DAI.
2. Mais aussi les apporteurs de liquidité sur FLX/ETH (migration en cours, fin prochaine)
3. Et enfin les stakers de FLX dans l'équivalent du Safety Module chez Reflexer.
4. Il y a également des incitations en FLX liées à l'utilisation de RAI dans divers services DeFi, détaillées dans la dernière partie.

[Le staking de FLX (Uni V2 FLX/ETH)](https://docs.reflexer.finance/incentives/flx-staking) sert à la fois de mécanisme d'incitation à l'apport de liquidité ainsi que de garantie pour le système. Si le système est sous-collatéralisé, les stakers seront dilués (->token LP liquidés) pour que le module acquiert du RAI et ramène le système à l'équilibre.

En situation normale, les stakers bénéficient tout simplement d'un rendement plutôt attractif. Tout comme le Safety Module d'Aave, ce module a un délai pour unstake, afin d'éviter l'exode des liquidités en période critique : il est de 21 jours.

Maintenant que les bases sont posées sur FLX, discutons un peu plus de ses enjeux à long terme.


### Le plan de retrait de la gouvernance

Le système Reflexer a pour vocation à être "governance-minimized". Cela a commencé dès sa mise en place, puisque des décisions qui chez Maker sont prises par la gouvernance (Stability Fee des vaults) sont automatisées chez Reflexer (PID controller).

La vision est tout simplement d'automatiser tout ce qui peut l'être à terme, une fois le système mature, et de donner les clefs des sous-systèmes qui ne peuvent pas l'être à la communauté des holders de FLX. 

L'équipe s'est ainsi fixée trois paliers principaux relatifs à cet objectif [détaillés dans l'article de présentation du FLX](https://medium.com/reflexer-labs/introducing-flx-20755214a465). Chaque palier est adossé à une date : 



* 14 mois après le lancement - 17 Avril 2022 : réduction de la gouvernance au minimum sur les sous-systèmes principaux (liquidation, auction et taxation)
* 18 mois après le lancement - 17 Août 2022 : minimisation de la gouvernance sur tous les contrats principaux, à l'exception du PID controller, des oracles et du mécanisme Savior.
* 3ème étape (date à venir) : passation de pouvoir (vers les holdeurs FLX) des mécanismes restants.

Je pense que ce tour d'horizon est bien assez pour comprendre l'intérêt de RAI et comment il fonctionne. Voyons donc désormais comment RAI est déjà utilisé dans divers protocoles DeFi.


## L'écosystème DeFi autour de RAI

RAI est en train d'être progressivement adopté au sein de l'écosystème DeFi, et cela fait plaisir à voir ! Je vous propose donc de finir avec un petit tour d'horizon des différentes intégrations de RAI dans des protocoles DeFi, en commençant par les marchés monétaires.


### RAI sur Fuse (Rari Capital)

Fuse est un marché monétaire assez innovant puisqu'il permet la création de pool par des acteurs qui ne sont pas l'équipe, et à terme n'importe qui. C'est donc assez logiquement que Fuse a été un des premiers marchés monétaires à supporter RAI. En fonction des pools, il est également possible d'**utiliser RAI comme collatéral sur Fuse**.

RAI est pour l'instant disponible dans 3 pools d'actifs proposants différents niveaux de risques et tokens empruntables :


![fuse-rai](/img/2021/reflexer-rai/fuse-rai.png)

### RAI sur Aave

Après avoir ajouté le support pour RAI il y a déjà quelques semaines, Aave a récemment alloué une enveloppe (très modérée) de StkAAVE pour incentiver les emprunts et dépôts sur RAI. Il aura fallu mettre la lumière sur l' une des contradictions principales de la plateforme : Aave est un marché monétaire décentralisé qui utilise (encore) la grande majorité de son budget pour inciter les emprunts/dépôts sur des stablecoins qui ne le sont pas du tout (USDC et USDT).

À noter : pour l'instant **le max LTV de RAI est de 0 : RAI ne peut donc pas servir de collatéral sur Aave**. Pas de discrimination ici, c'est assez standard de la part d'Aave - il s'agit de la procédure "classique" et prudente lors de l'ajout d'un nouveau type de collatéral. La gouvernance peut voter pour augmenter cette valeur.


### RAI sur Cream

Cream a été l'un des premiers marchés monétaires à supporter RAI. Il s'agit néanmoins d'un marché monétaire de seconde zone extrêmement risqué et sans valeur ajoutée, voire délétère sur le long terme. Je m'arrête donc là, et [vous invite à lire cet article si vous vous demandez pourquoi](https://tokenbrice.xyz/fr/marche-monetaire-risque/).


### RAI sur Idle Finance

Idle Finance est un service qui permet, comme son nom l'indique, de mettre en place des stratégies de rendement passif. Dans le cas de RAI, Idle exploite les rendements disponibles sur Fuse ainsi que Aave. Initialement, il y avait aussi Cream mais la gouvernance a choisi de recentrer les stratégies pour contenir le risque :

Outre le rendement natif en RAI, un dépôt sur Idle Finance vous permet également de bénéficier :



1. D'un rendement en FLX, visible ici.
2. D'un rendement en StkAAVE (correspondant à la part des RAI déployés sur Aave)
3. Et enfin, également d'un rendement en IDLE (bientôt - voté par la gouvernance mais pas encore implémenté)

Ainsi, si vous souhaitez posséder des RAI sur le long terme pour vous prémunir contre les risques relatifs au dollar/euro, le dépôt sur Idle est plutôt attractif pour produire un rendement totalement passif. Attention cependant, cela revient à composer plusieurs risques de smart contract : Reflexer + Aave + Fuse + Idle.


### RAI + Fei Protocol

Fei est un autre stablecoin qui cherche à maximiser la décentralisation. Ici l'approche est différente et repose essentiellement sur la notion de **"Protocol Controlled Value" (PCV)**. En bref, l'essentiel de liquidité sur les paires FEI est contrôlé par le protocole lui-même. Les fonds sont issus de la genèse du protocole où les utilisateurs ont engagé des ETH afin d'acquérir du FEI ainsi que du TRIBE (token de gouvernance) à leur création.

Ainsi, FEI est un stablecoin qui partage une caractéristique avec RAI et LUSD : il est entièrement collatéralisé par des actifs trustless (ETH). Néanmoins, FEI est bien plus proche de LUSD que de RAI dans le sens où il reste indexé au dollar.

Récemment, la DAO de Fei a voté pour **diversifier une partie de la trésorerie du protocole vers RAI** afin de la rendre plus pérenne. Ainsi, jusqu'à $6M (~2M RAI) vont être acquis et déployés sur Aave et Fuse pour produire un rendement.  D'autres DAOs envisagent également de diversifier une partie de leur trésorerie vers RAI (Moloch, DxDAO, Metagame, etc.), je m'attends donc à plus d'initiatives similaires.


## Conclusion

J'espère que cette présentation assez exhaustive de RAI vous aura appris des choses. Comme toujours gardez en tête que je choisis soigneusement mes sujets et cet article ne constitue en rien un conseil en investissement. En l'occurrence, le choix s'est porté sur Reflexer/RAI ici car c'est un système élégant dont l'analyse permet de discuter de nombreuses notions essentielles pour mieux comprendre la DeFi dans son ensemble.

J'espère que la lecture de cet article aura été instructive pour vous.

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais. Ainsi qu'à [Guifel](https://twitter.com/guifel_) de l'équipe Reflexer pour ses suggestions avisées._

Vous n'en avez pas eu assez ? Ça tombe bien, l'équipe Reflexer vous propose des articles très bien écrits pour expliquer le système plus en profondeur - en anglais. Voici ceux dont je recommande particulièrement la lecture :

* Un article [pour comprendre l'approche développée pour sécuriser le protocole](https://medium.com/reflexer-labs/securing-the-money-god-ef21453a299b)
* [Une série de trois articles de simulations, parfait pour articuler en pratique votre compréhension de RAI](https://medium.com/reflexer-labs/rai-system-simulations-part-1-safe-owners-876a6bd55385)
* Enfin, pour les plus braves d'entre vous, sachez aussi que [le whitepaper originel de RAI est également disponible en français](https://github.com/reflexer-labs/whitepapers/blob/master/French/rai-french.pdf)

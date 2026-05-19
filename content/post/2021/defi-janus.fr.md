---
title: "Janus : le nouvel ennemi juré des protocoles DeFi ?"
description: "Essai sur les tensions de gouvernance DeFi entre utilisateurs, detenteurs de tokens, protocoles et incentives contradictoires."
date: '2021-07-05T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Thesis]
tags: [DeFi, Ethereum, Money Markets, Liquity, Curve, CRV, MakerDAO, Convex, CVX, Yearn, Uniswap]
toc: true
tocNum: true
url: defi-janus
aliases:
  - p/defi-janus
image: /img/2021/defi-janus/defi-janus-cover.png
difficulty: "intermediate"
---

La mythologie est souvent utilisée pour illustrer la DeFi. Par exemple, on évoque souvent le dieu cananéen Moloch pour symboliser les enjeux de coordination. Aujourd'hui, je vais identifier avec vous une nouvelle divinité du panthéon DeFi : Janus.

Dans cet article, on analyse les mécanismes des gouvernances ouvertes des protocoles DeFi qui peuvent conduire à l'émergence d'un nouveau genre de défi pour la DeFi, un ennemi juré que je vous propose d'incarner dans la divinité romaine Janus.

Tout comme le dieu aux deux visages, **un protocole Janus souffre d’une ambivalence profonde** : bien qu'il puisse être un succès incontestable en termes d'utilisation, il fait face à de sérieux antagonismes entre ses différentes parties prenantes qui mettent en jeu la pérennité du protocole (utilisateurs, holdeurs, investisseurs, équipe et communauté étendue).

Pour comprendre les Janus, il faut saisir la complexité inhérente de la DeFi et comment elle peut s’accommoder de  **consensus sur des décisions pourtant délétères ou non optimales**. Une fois le contexte posé, on pourra analyser trois Janus, chacun à leur manière : MakerDAO, Yearn Finance et Uniswap.

## Complexité et enjeux de gouvernance : un terreau fertile pour Janus

L'émergence de protocoles Janus dans la situation actuelle est due à de nombreux facteurs difficiles à hiérarchiser. Je les ai regroupés en trois thématiques :

### Mécanismes de gouvernance et vote

La gouvernance des protocoles DeFi se fait **de manière ouverte et transparente**, en plusieurs étapes.

Au fil des discussions sur différents supports comme Discord, la communauté converge vers différentes idées qui peuvent aboutir à des propositions. Les propositions sont formalisées, généralement sur les forums de gouvernance et amendées avant d'atteindre un **consensus informel**.

Des mécanismes de **signalement** (Snapshot) permettent d'identifier les propositions les plus pertinentes. Elles sont par la suite **soumises au vote des détenteurs des tokens** via le mécanisme de gouvernance principal.

La plupart des systèmes de gouvernance fonctionnent encore sur la logique du **1 token = 1 vote**, attribuant ainsi le même poids à tous les possesseurs de tokens quelque soit leur attitude vis-à-vis du projet ou niveau d'engagement par rapport à celui-ci.

![influence-governance](/img/2021/defi-janus/influence-governance.png)

_Mesurer l'influence dans la gouvernance des protocoles DeFi - [source](https://twitter.com/Lsquaredleland/status/1411031620748943360)_

Certains protocoles ont pourtant réussi à remettre en cause cette approche en ajoutant une logique d'engagement temporel : interagir avec la DAO de Curve nécessite d'engager ses CRV pour une période allant de 1 à 4 ans. Un engagement de longue durée augmente le pouvoir de vote effectif obtenu (veCRV).

Malgré tout, la **participation est généralement basse**, même lorsque des mécanismes de délégation sont utilisés.

### Complexité des décisions

Pour évaluer des propositions de gouvernance d'un protocole de finance décentralisée, il faut avoir **une compréhension de tout un ensemble de notions de base relative à Ethereum**, la Blockchain et la DeFi.

À partir de là, il faut idéalement une compréhension approfondie du protocole en question, ainsi que ses **interactions avec les autres protocoles, synergies**, etc. On peut également désormais rajouter à cela toute la complexité additionnelle liée à la multiplication des solutions de scalabilité : sidechains et L2.[^mkrgov]

En outre, la formulation des propositions sur les forums de gouvernance est généralement assez technique, ce qui **rend leur compréhension** difficile et ouvre la porte aux manipulations.

Enfin, la gouvernance souffre d'un véritable effet de masse : au fur et à mesure que les protocoles se développent, la quantité d'informations à digérer pour avoir un vote éclairé augmente en conséquence.

Un membre du forum de gouvernance MakerDAO a estimé son travail hebdomadaire de suivi et de participation à environ 40h par semaine, en augmentation constante :

![maker-governance-overhead](/img/2021/defi-janus/maker-governance-overhead.png)

### Supports de la gouvernance

Bien que la gouvernance soit ouverte et transparente, **elle s'appuie encore souvent sur différents services propriétaires et donc administrés,** le plus souvent par l'équipe elle-même. Cela pose de sérieux problèmes.

Ainsi, les discussions relatives à la gouvernance se font généralement sur Discord et sur le forum de gouvernance - les **deux supports sont généralement modérés directement par l'équipe du projet**.

En outre, l'équipe peut avoir **un contrôle sur les mécanismes de signalement** comme [Snapshot](https://snapshot.org/). Le cumul de toutes ces limitations des systèmes de gouvernance décentralisée peut amener aux situations observées dernièrement, où les possesseurs de tokens ne votent pas dans leurs meilleurs intérêts.

Ce tour rapide des limites actuelles des systèmes de gouvernance était nécessaire pour avoir le contexte pour la suite. Voyons donc les trois Janus que j'ai repérés :


## Uniswap : 1M d'UNI par ci, 1M d'UNI par là


### La proposition 05 en résumé

Un vote précipité qui abouti à la signature d'un chèque quasiment en blanc de 1M UNI pour un groupe de directeurs juridiques de gros projets décentralisés chargés de déployer une stratégie de lobbying DeFI. Très peu de mécanismes de transparence ont été déployés et l'influence de la communauté des UNI holder sur le groupe financé est restreinte.

[Proposition 05 Uniswap Gouvernance - DeFi Education Fund](https://gov.uniswap.org/t/governance-proposal-005-defi-education-fund/12963)


### Compression de la gouvernance

Dans le cas d'Uniswap, tout y était. Tout commence avec un vote précipité alors que des membres de la communauté avaient de **très nombreuses questions ignorées**. La communauté s'inquiète du manque de contrôle sur les fonds alloués sans aucune condition. Chris Blec a regroupé les principales questions et inquiétudes dans [une lettre](https://twitter.com/ChrisBlec/status/1409857319144394758 ) et a réussi à obtenir quelques réponses de l'équipe dans un [Twitter space](https://odysee.com/@ChrisBlec:8/chrisblec-june24-twitterspace:9?r=DeLsAYctGhcLFvkGBKYgE2tN17fUXA9u).

En outre, **l'organisation qui va recevoir les 1M UNI est composée de membres proches de l'équipe Uniswap** et on suspecte également des investisseurs du projet comme a16z d'avoir été décisif dans l'adoption de la décision. La proposition bénéficiait également du soutien direct de l'équipe.

Finalement, la proposition se veut plus large qu'Uniswap puisqu'ils sont officiellement mandatés pour faire du lobbying DeFi, mais on peut se poser la question de la vision de la DeFi portée par de tels profils.

### Transparence ? Peut être. Contrôle ? Non !

Après les réactions aux premières itérations de la proposition, différents mécanismes ont été ajoutés pour apporter plus de transparence sur les agissements du DeFi Education Fund. L'équipe s'est également engagée à implémenter [FailSafe](https://github.com/withtally/safeguard) dès que possible. Cela permettrait à la DAO (holdeurs UNI) de pouvoir exercer un veto sur les transactions réalisées par le multisig.

Néanmoins à l'heure d'aujourd'hui **le contrôle effectif de la DAO reste limité** : le vote est passé et [les 1M UNI sont désormais alloués](https://etherscan.io/address/0x1C95930Dfc1139381265ce45B5f480F1EFae09A1).

Edit du 17 Juillet : peu après avoir reçu les fonds, le multisig [a déjà vendu la moitié de ceux-ci](https://thedefiant.io/sale-of-usdc-raises-concerns-regarding-newly-formed-defi-education-fund/) pour des Stablecoins qui restent encore dans le wallet pour l'instant.

Cet épisode correspond pour moi à l'équivalent d'un détournement de fonds publics, sauf qu'ici les fonds proviennent d'une DAO. L'aventure et ses péripéties mettent également en lumière le pouvoir effectif exercé par les différentes parties prenantes du protocole.

## MakerDAO : déséquilibre d'intérêts antagonistes

Le problème avec Maker est plus général et remonte bien plus loin. C'est un problème courant en DeFi d'alignement d'intérêts divergents de différents participants. En outre, pour répondre rapidement à la demande grandissante pour le DAI, **la multiplication des collatéraux (mise à jour MCD) a grandement impacté la trustlessness et la décentralisation effective de DAI.**

Plus de 60% des garanties du DAI sont des tokens qui nécessitent une forme de confiance comme USDC, wBTC ou TUSD. Le problème existe depuis longtemps et n'est pas prêt de se résoudre, si jamais. J'ai déjà discuté de ce problème sur ce blog, je vous renvoie vers cet article :
**[Actifs à vocation stable sur Ethereum : quelles approches et quels enjeux ?](https://tokenbrice.xyz/fr/actifs-stables-ethereum/)**

### Des frais d'utilisation abusifs

Ici, on va plutôt creuser le problème des frais excessifs qui illustre **un cas classique de maximisation de rente sur une clientèle pensée captive**.[^makerclientelecaptive] DAI étant un stablecoin synthétique frappé directement par l'utilisateur, son frais d'emprunt annuel ne devrait pas excéder 2-3% et cela reste encore coûteux. [Liquity](http://liquity.org/), une alternative à Maker, charge un frais qui revient à 0.5% annuel sur les LUSD empruntés.

Avant la dernière mise à jour, le principal vault ETH de maker (ETH-A) chargeait 5.5% de frais annuel. C'est désormais descendu à 3.5%, mais les frais sur le vault le plus proche des conditions d'emprunt de Liquity (ETH-B, collatéralisation minimale = 130% // 110% sur Liquity) reste à 9% annuel, soit **18 fois plus coûteux que son alternative**.

{{< notice info >}}
Liquity est construit avec une approche de minimisation de la gouvernance, contrairement à Maker, ce qui peut expliquer une partie de l'écart immense observé entre les frais appliqués par les deux plateformes.
{{< /notice >}}

### Une rente pour les holdeurs MKR ?

Les frais de MakerDAO sont habituellement élevés, même s'ils ont été à zéro ou proches à de courtes périodes pour stimuler la demande. Alors **pourquoi la DAO Maker vote systématiquement des frais excessifs** ? La réponse est aussi simple que 1+1=2 :

1. Les frais prélevés sur les vaults Maker sont utilisés pour acheter des MKR tokens sur les marchés et les brûler, rendant le token MKR plus rare.
2. Ils sont votés par la DAO de Maker, en proportion donc des tokens MKR possédés.

La conception même du protocole incite ainsi les possesseurs de MKR à voter pour **extraire les frais maximaux tolérés par les utilisateurs**, et pas un centime de moins. En effet, chaque point de base[^bps] en frais supplémentaire se traduit par plus de MKR brûlés et donc à priori un capital qui s'apprécie pour les possesseurs du token.

Ça peut sembler fabuleux en termes de tokenomics car cela optimise pour le meilleur prix possible sur MKR (théoriquement), mais **cela se fait au détriment des utilisateurs du service** que la plateforme propose - et donc va contre l'intérêt long-terme du protocole.

Il faut également garder en tête que contrairement à la plupart des protocoles, Maker n'a jamais mis en place de mécanisme pour transformer ses utilisateurs en holdeurs (liquidity mining). Je vois donc difficilement comment Maker peut être compétitif avec une telle structure.

## Le cas ambigu de Yearn Finance

Yearn est sans doute l'exemple le plus simple et direct d'un Janus. En à peine un an, Yearn est devenu un **protocole majeur de la DeFi avec $4B d'actifs déposés** et surtout **une profitabilité délirante** que l'équipe aime mettre en avant.

Néanmoins, l'histoire n'est pas aussi rose en fonction de votre perspective. On va donc étudier la situation de Yearn sous 3 angles : du point de vue d'un utilisateur, pour un autre protocole et pour la DAO Yearn elle-même.

### Coté utilisateurs : des frais délirants

Le succès de Yearn s'obtient à quel prix ? Encore une fois, essentiellement **des utilisateurs qui se font littéralement dépouiller par Yearn** - les frais comptent parmis les plus élevés observés pour un gestionnaire d'actif en DeFi, tout en étant complexe :

1. Yearn prend **2% de frais de gestion annuel sur l'ensemble du dépôt**.
2. Yearn prélève également un frais sur la performance de 20% : 20% de tous les actifs farmés partent vers la trésorerie.[^yearnfrais]

Les premier frais est le plus problématique puisque cela signifie que les frais excessivement gourmands de Yearn amène à des vaults qui… perdent de l'argent !

En effet, tout vault qui ne réalise pas au minimum 2% de retour annuel sur Yearn finit dans le rouge une fois les frais de gestion prélevés, sans même prendre en compte les frais de performance...


### Coté protocoles : le câlin de la mort de Yearn

Yearn permet à ses utilisateurs de farmer différents protocoles comme Curve en gérant automatiquement la composition de leurs rendements.

C'est pratique pour l'utilisateur, mais cela signifie également que **Yearn vend systématiquement tous les tokens farmés** par ses vaults : on peut donc se poser la question de l'impact et de la pertinence pour le protocole farmé, qui subit donc une pression vendeuse sur son token natif.

L'arrivée de Convex a démontré qu'un protocole mieux structuré en termes de tokenomics et spécifique à Curve peut proposer une alternative synergistique où les rendements sont largement supérieurs, tout en évitant la vente systématique des tokens farmés. J'analyse la "flywheel" de Convex dans cet article : **[🎡 Flywheel DeFi : synergies de protocoles à protocoles, par tokens interposés](https://tokenbrice.xyz/fr/defi-flywheel/)**

Ainsi, l'arrivée de Convex a mis Yearn face à ses contradictions et Yearn a essentiellement capitulé en intégrant Convex pour optimiser le rendement de ses vaults. Cela signifie désormais que **les utilisateurs de Yearn paient des frais à Convex et aident le protocole à accumuler plus de VeCRV** et creuser ainsi son écart avec Yearn - échec et mat pour Yearn sur Curve.

![vecrv-par-dao](/img/2021/defi-janus/vecrv-par-dao.png)

_Aperçu des veCRV possédés par les différentes DAO - source [Dune Analytics / Banteg](https://duneanalytics.com/banteg/misc)_


### Coté Yearn DAO

Malgré cette situation fondamentale assez inquiétante puisque Yearn propose désormais des **produits essentiellement non compétitifs** (tous les vaults Curve), Yearn se présente comme un des succès incontestables de la DeFi.

En effet, l'équipe semble mesurer le succès du protocole au volume des frais prélevés par celui-ci. L'indicateur est évidemment dangereux puisqu'avec les frais de gestion à 2% annuel, tout dépôt sur Yearn paie systématiquement des frais même si peu ou pas de profit n'est dégagé.

Plutôt que de prendre les frais prélevés comme un indicateur et donc une mesure de succès, le protocole pourrait être optimisé sur la base des profits générés pour les déposants.

Enfin, et même si c'est un sujet plus subjectif, la communication autour du projet est brouillone voire presque dérangeante parfois, par exemple [quand Yearn est comparé](https://thedefiant.io/yearn-revenues-projected-to-surpass-tradfis-fueled-by-thriving-community/) aux gestionnaires d'actifs classiques comme WealthFront ou BlackRock - je trouve ça assez déséquilibré puisque Yearn charge des frais similaires à ces structures mais opère dans un marché bien plus dynamique. En outre, de telles sociétés sont-elles réellement des modèles pertinents à avoir en DeFi ?

![yearn-comp](/img/2021/defi-janus/yearn-comp.png)

Si Yearn se compare aux gestionnaires d'actifs, c'est peut-être parce que la comparaison avec ses pairs DeFi est sans appel :

![defi-asset-manager](/img/2021/defi-janus/defi-asset-manager.jpeg)

En outre, là où Convex travaille à permettre aux holdeurs cvxCRV de voter dans les décisions de la DAO Curve, Yearn s'octroie le contrôle sur la puissance de vote associée aux CRV déposés par ses utilisateurs sur le yveCRV. La même démarche s'observe sur les airdrops alloués aux holdeurs VeCRV : Yearn se les octroie pour acheter des CRV et sponsoriser son vault yveCRV tandis que Convex les rend accessibles à ses déposants.

## Les Janus sont-ils défendables ?

Maintenant qu'on a posé le décor avec trois Janus, reste la question de leur défendabilité. Tous les trois ont des alternatives crédibles, souvent plus récentes et avec des tokenomics plus équilibrées. Voyons donc comment nos Janus évoluent par rapport à celles-ci.

En à peine deux mois d'existence, Convex a déjà dépassé Yearn en termes de valeur totale des actifs déposés. Pour l'instant, les réactions de Yearn n'ont pas réussi à inverser la tendance, et je pense que **seule une révision profonde du modèle permettra au protocole de rester compétitif sur le long-terme**.

Néanmoins **la machine est lancée** : Convex possède déjà plus de deux fois plus de CRV que Yearn et en accumule bien plus rapidement. Et même si Yearn farme de nombreux autres protocoles, il me semble improbable qu'il puisse redevenir compétitif sur Curve.

Côté Marker, de plus en plus de personnes commencent à souligner l'absurdité de la situation actuelle sur DAI, et les alternatives gagnent du terrain. En quelques semaines et avec seulement ETH comme collatéral accepté, Liquity a déjà attiré l'équivalent de plus de 40% de la valeur total déposée dans MakerDAO :

![tokenterminal-tvl-maker-liquity](/img/2021/defi-janus/tokenterminal-tvl-maker-liquity.png "Comparaison des TVL MakerDAO vs Liquity")

Sur Liquity, les frais d'emprunt sont bien plus bas, plus clairs, et distribués directement aux stakers de LQTY. Le service est ainsi plus ouvert et participatif que MakerDAO tout en étant brutalement plus efficace. Là encore, je pense qu'une refonte d'ampleur de MakerDAO serait nécessaire pour que le protocole retrouve sa pertinence et sa compétitivité.

Enfin pour Uniswap, la concurrence est encore plus vive. Le protocole évolue face à des tokenomics matures comme Curve qui a un mécanisme de partage des revenus du protocoles actif depuis bientôt un an, tandis que rien n'est encore proposé sur UNI.

Sur les trois fronts, je pense que la situation forcera Uniswap, Maker et Yearn à se renouveler. Néanmoins avec le rythme de l'industrie, l'étau se resserre et leurs alternatives plus ouvertes, efficaces et synergiques gagnent rapidement du terrain.

Alors que les DAO des trois protocoles se sont désynchronisées de leurs utilisateurs, le meilleur intérêt de ceux-ci leur a été rappelé de la manière la plus simple et efficace que l'on connaisse : avec des mouvements de capitaux conséquents. J'ai hâte de voir ce qui arrive ensuite !

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

[^mkrgov]: Regardez par exemple [cette pré-proposition prise au hasard sur le forum de gouvernance de MakerDAO](https://forum.makerdao.com/t/mip33-maker-stability-price-module/5943)
[^yearnfrais]: [Documentation Yearn Finance - Structure des frais](https://docs.yearn.finance/yearn-finance/yvaults/overview#yvault-fee-structure)
[^makerclientelecaptive]: DAI est encore perçu par beaucoup comme un stablecoin décentralisé qui ne nécessite pas de confiance, bien que ce ne soit plus le cas. Il existe encore peu de Stablecoins qui ne s'appuient que sur des collatérals trustless (ETH) et crédiblement décentralisés (ou en voie) : j'en connais deux - le LUSD de Liquity et le RAI de Reflexer.
[^bps]: Les frais des services financiers sont souvent mesurés en point de base (bps / basis point). Un point de base est un centième de pourcent : 1 bps = 0,01%.
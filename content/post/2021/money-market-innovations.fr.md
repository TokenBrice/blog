---
title: "Comprendre les innovations sur les marchés monétaires pour envisager leur avenir"
description: "Tour des innovations des marches monetaires DeFi: B.Protocol, Alchemix, taux fixes, liquidations et nouveaux designs de pret."
date: '2021-04-14T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Lending]
tags: [DeFi, Ethereum, Money Markets, Aave, Compound, Liquity, Reflexer, BProtocol, Liquidation]
series: money-markets
series_order: 3
toc: true
tocNum: false
url: marche-monetaire-innovations
image: /img/2021/money-market-innovations/cover.png
difficulty: "intermediate"
---

Les marchés monétaires comme [Aave](https://www.defiscan.info/protocols/aave/ethereum), [Compound](https://www.defiscan.info/protocols/compound-v3/ethereum) ou [Maker](https://www.defiscan.info/protocols/sky/ethereum) sont au centre de la DeFi. Pour l'utilisateur final, ils remplissent des fonctions similaires à ce qu'offre une banque dans la finance classique : pouvoir emprunter ou rendre productif des actifs en les prêtant à d'autres.

Néanmoins, **l'analogie s'arrête immédiatement à la comparaison fonctionnelle**. En effet, la logique sous-jacente des marchés monétaires n'a rien à voir avec le fonctionnement d'une banque. Les marchés monétaires bénéficient de tous les avantages de la DeFi, et notamment la transparence de toutes les opérations ainsi que son accessibilité.

Lorsqu'un utilisateur emprunte sur Aave, **le service n'a pas besoin de connaître son âge ou son identité**: il suffit que les conditions soient remplies, c'est-à-dire que le collatéral apporté soit suffisant par rapport à la somme empruntée.

De la même manière, un utilisateur qui dépose des Stablecoins sur Aave pour produire un rendement en les prêtant à d'autres ne fait confiance à personne : il peut vérifier à tout moment quelles adresses empruntent quels montants et **s'assurer ainsi de la solvabilité du système tout entier**.

Cela peut sembler basique pour un DeFian, mais c'est un véritable changement de paradigme. Dans la finance classique, on n'a d'autres choix que de faire confiance à un tiers (auditeur, agence de notation, etc.) pour obtenir cette information - avec le biais qu'on lui connaît.

---

## Découvrir les marchés monétaires

On a déjà beaucoup parlé de marchés monétaires sur ce blog, notamment avec l'article qui propose une méthodologie qualitative pour évaluer leurs risques : **[De l'évaluation du risque sur les marchés monétaires en finance décentralisée](https://tokenbrice.xyz/fr/marche-monetaire-risque/)**

Ou encore celui qui s'intéresse aux différents services d'abstraction et de distribution du risque inhérent aux marchés monétaires : **[🗡 Du risque ? Oui, mais juste un doigt](https://tokenbrice.xyz/fr/tranching-risque-defi/)**

Néanmoins, les marchés monétaires évoluent sans cesse, autant par leurs mises à jour que par l'apport de services tiers construits sur leurs protocoles. En outre, de nouveaux marchés monétaires ambitieux se lancent pour couvrir des besoins encore insatisfaits.

C'est donc précisément notre objet du jour : **comprendre les innovations essentielles en cours sur les marchés monétaires pour mieux envisager leurs évolutions à venir.** Plutôt que de vous faire une liste exhaustive, je vous propose au contraire de regarder une sélection de projets que je pense pertinente pour comprendre la marche de l'industrie.

---

## Les innovations construites sur les marchés monétaires existants

Les marchés monétaires peuvent sembler complexes au premier abord. Les curieux sont le plus souvent effrayés par le risque de liquidation du collatéral déposé lorsque sa valeur ne suffit plus pour sécuriser le montant emprunté.

### Gestion facilitée des positions d'emprunt grâce à DeFiSaver

De très nombreux utilisateurs de DeFi n'ont pas encore bien compris les enjeux à ce niveau là. Nombreux encore sont ceux qui pensent que la liquidation peut être totale et soudaine. Outre l'information et l'éducation, des outils de gestion de ses positions aident les utilisateurs à se sentir plus en confiance.

Heureusement, très vite, des outils facilitant et automatisant la gestion des positions d'emprunts sur les marchés monétaires sont apparus, comme DeFi Saver. Je vous en parlais déjà l'année dernière dans l'article **[🎚 Ether ou DeFi : Pourquoi choisir ?](https://tokenbrice.xyz/fr/leveraging-eth/)**

DeFiSaver agit comme une interface (proxy) entre l'utilisateur et le marché monétaire. Il permet de nouvelles fonctionnalités comme la bien aimée "Save" : lorsque la position passe sous un seuil de collatéralisation défini par l'utilisateur, **DeFiSaver se charge de rééquilibrer automatiquement la position grâce à un flash loan.**

Concrètement, cette fonction vend une partie du collatéral de l'utilisateur pour rembourser un peu de dette et revenir à un ratio de collatéralisation décidé en amont. Un tel outil permet aux emprunteurs les plus agressifs ou inquiets de dormir bien plus sereinement.


### Se réapproprier la liquidation avec B.Protocol

Bien que DeFiSaver soit très utile, cela reste un outil qui ne change pas fondamentalement le fonctionnement des services sous-jacents. D'autres projets vont plus loin, comme [BProtocol](https://www.bprotocol.org/) que j'ai découvert récemment.

L'idée est très simple : au lieu d'emprunter directement sur Maker par exemple, l'utilisateur passe par le contrat de BProtocol. La réserve de fonds dont dispose le protocole lui permet de **liquider la position de l'utilisateur (si besoin est) avant que d'autres liquidateurs s'en chargent.**

![bprotocol explainer](/img/2021/money-market-innovations/bprotocolexplainer.png "Fonctionnement de haut niveau de BProtocol")

Ainsi, ce qui correspond d'habitude à une guerre de gas entre différents liquidateurs devient une opération plus prévisible. Cela permet également de **redistribuer une partie du premium de liquidation à l'utilisateur lui-même plutôt qu'aux mineurs.**

{{< notice note >}}
Sur les marchés monétaires, les utilisateurs déposent un collatéral pour emprunter. Si la valeur de leur collatéral a trop réduit par rapport au montant emprunté, une liquidation est nécessaire.

Habituellement cette liquidation est à la charge d'un autre type d'utilisateur qui est rémunéré (liquidation premium).
{{< /notice >}}

L’idée, simple à un haut niveau, est malgré tout très rassurante pour les utilisateurs tout en permettant de "professionnaliser" les liquidations qui deviennent plus prévisibles. Il y a désormais environ $100 M d'actifs gérés par le protocole qui couvre déjà Maker et Compound (Aave arrive bientôt).

---

## Des innovations sur le modèle de MakerDAO

MakerDAO est sans doute le marché monétaire le plus connu, c'est aussi un cas assez particulier. En effet, MakerDAO remplit une fonction double : oui, le service permet l'emprunt tout comme Aave ou Compound, néanmoins **personne ne vous prête quoi que ce soit quand vous empruntez sur Maker - les emprunteurs frappent directement une monnaie (DAI) qui correspond à leur dette.**

Ainsi, tout en permettant l'emprunt, MakerDAO produit également un actif stable, le DAI, indexé sur le dollar. Bien que le DAI ait ses limites, il reste moins centralisé et nécessite moins de confiance que des modèles de Stablecoins comme USDC. C'est bien pour cela que le modèle de Maker a été maintes fois repris pour servir de nouvelles fins.

### Mimo Capital : à bas le dollar, place à l'euro !

Jusqu'à présent, le dollar était la monnaie fiduciaire de référence pour la DeFi. Quasiment tous les projets de Stablecoins visent à produire un actif qui suit la valeur du dollar. En outre, c'est également la valeur en dollar des actifs volatils qui est considérée par les systèmes d'emprunt pour déterminer le ratio de collatéralisation, aussi bien sur Maker que Compound ou Aave.

Le dollar étant la monnaie fiat la plus courante et la mieux connue, cela faisait du sens pour commencer mais il est également grand temps d'aller au delà pour répondre aux besoins de tout type d'utilisateur et rendre la DeFi plus accessible.

C'est précisément ce que recherche un projet comme Mimo Capital qui propose **un système similaire à MakerDAO mais où l'Euro est la monnaie fiduciaire de base**, au lieu du dollar. Cela signifie que le stablecoin produit par les emprunteurs - le PAR - suit l'Euro, mais également que les prix internes du système sont en €, comme la valeur des collatéraux utilisés (ETH, wBTC ou USDC).

![Mimo-Capital-PAR](/img/2021/money-market-innovations/mimo-capital-par.png "Les principales métriques pour PAR, issues du site officiel.")

Mimo n'arrive pas sur une page blanche puisque les Stablecoins en Euros commencent à émerger. Outre le PAR de Mimo, il existe l'EURS un stablecoin qui suit un modèle centralisé : chaque EURS en circulation est garanti par un Euro fiat possédé par l'émetteur. Ainsi, **les opportunités de rendement commencent à émerger via des expositions en euros**, avec par exemple la pool sEUR/EURS sur Curve également accessible via des vaults sur StakeDAO ou Harvest Finance par exemple.

L'arrivée d'**un système comme Mimo permet aux investisseurs européens d'envisager un circuit dont la devise de référence serait l'Euro**. En utilisant leur ETH ou wBTC comme collatéral, ils peuvent emprunter du PAR (stablecoin €) et le rendre productif via, pour l'instant, deux pools de liquidité sur Balancer, mais à terme, sans doute plus.

Mimo est encore un système assez récent avec environ 25 millions € de collatéral déposé en garantie pour  environ 12.5 M PAR émis (€). Le token de gouvernance associé au service - MIMO - est actuellement distribué à tout détenteur d'un vault actif ainsi qu'aux fournisseurs de liquidité sur les paires PAR/ETH et PAR/USDC.

### Dépasser les monnaies fiduciaires avec Reflexer

**Passer du dollar à l'euro, c'est bien,se passer complètement d'une référence en monnaie fiduciaire, c'est encore mieux !** C'est exactement ce que propose Reflexer, un autre service inspiré du modèle Maker.

Ici, il n'y a pas de prix de référence. Le prix du RAI (actif produit par les emprunteurs) est gouverné directement par le marché (moyenne de prix sur la paire RAI/ETH). Le système a également son prix "interne", le _Redemption Price_ - le taux utilisé lorsque les utilisateurs frappent directement du RAI (en déposant de l'ETH comme collatéral).

![prix du reflexer RAI](/img/2021/money-market-innovations/raiprice.png "Évolution du prix du RAI depuis son lancement")

Différents paramètres du système Reflexer s'ajustent pour **faire converger les deux prix à terme, ou en tout cas les maintenir dans une fourchette étroite**. Bien que cette approche soit bien plus ardue à prendre en main pour l'utilisateur, elle est totalement dissociée de toute corrélation avec le dollar (ou tout autre monnaie fiduciaire), ce qui a de la valeur en soi.

Pour mieux comprendre Reflexer, je vous invite à consulter mon précédent article sur les actifs à vocation stable :

**[Actifs à vocation stable sur Ethereum : quelles approches et quels enjeux ?](https://tokenbrice.xyz/fr/actifs-stables-ethereum/)**

---

## Nouvelle génération de marchés monétaires

Jusqu'à présent, nous avons considéré des innovations construites sur les marchés monétaires principaux existants ou s'inspirant directement de leurs modèles. Il existe également toute une jeune nouvelle vague de marchés monétaires qui explorent des approches différentes.

Je vous propose donc de considérer deux derniers projets qui apportent de véritables changements fondamentaux.


### Alchemix : actifs productifs en collatéral ?

Je ne pouvais pas commencer cette section par un projet autre que Alchemix ! L'idée de ce projet est aussi simple que puissante :

1. Et si, au lieu d'accepter des collatéraux non productifs, on ne prenait que des **collatéraux productifs** comme un stablecoin qui produit un rendement ?
2. Notre collatéral a désormais un rendement : et si le rendement du collatéral servait à rembourser l'emprunt ?
3. Et voilà : **un emprunt qui se rembourse tout seul avec le temps** !

![Alchemix overview](/img/2021/money-market-innovations/alchemix.png "L'infrastructure d'Alchemix")

Alchemix s'est lancé en acceptant le yDAI (DAI déposé sur Yearn Finance) comme collatéral. Les déposants peuvent emprunter **jusqu'à 50% de la valeur de leur yDAI en AlUSD**, un autre stablecoin dollar. Leur collatéral n'est pas à risque, et l'emprunt se rembourse tout seul grâce aux intérêts générés par le yDAI : il faut compter environ 3 ans avec le taux de rendement actuel.

Alchemix est très vite devenu un service très prisé, notamment pour **procéder à des achats conséquents sans pour autant dépenser de crypto**, ce n'est qu'une affaire de patience. Prenons un exemple.

Voici Bob, un fermier DeFi qui a bien travaillé : il souhaite désormais profiter des fruits de son labeur. Il veut mobiliser $50 000 pour s'acheter une voiture. Plutôt que de prélever directement $50 000 sur ses actifs, Bob peut aboutir au même résultat sans rien dépenser grâce à Alchemix :

1. Bob dépose 100 000 DAI sur Alchemix, qui sont déployés sur Yearn
2. Cela lui permet d'emprunter jusqu'à 50 000 AlUSD, qu'il peut ainsi utiliser pour acheter sa voiture.
3. Bob n'a plus qu'à patienter pendant que les rendements du yDAI remboursent son prêt. Dans ~3ans, une fois la dette remboursée, il pourra récupérer ses 100 000 DAI initiaux.

**Un tel flux permet ainsi de dépenser immédiatement sans autre coût que le fait de verrouiller environ 2 fois la somme mobilisée au sein d'Alchemix.** Le futur de l'argent programmable, c'est maintenant !

C'est tellement puissant et novateur que beaucoup ont encore du mal à le croire. Les retours d'expérience des utilisateurs d'Alchemix attirent encore de nombreux sceptiques :

### Liquity : l'efficacité à tout prix

[Liquity](https://www.liquity.org/) est un autre marché monétaire qui innove à plusieurs niveaux. Le concept fondamental à comprendre ici est que **les liquidations sont automatisées et donc beaucoup plus prédictibles et rapides.**

Cela permet à [Liquity](https://www.defiscan.info/protocols/liquity/ethereum) de proposer **des ratios de collatéralisation inférieurs** à d'autres systèmes, ou pour le dire autrement : les utilisateurs de Liquity peuvent mobiliser plus de dollars par ETH déposé que sur un système comme Maker :

{{< notice info >}}
Le ratio prêt/valeur maximum (LTV maximum) détermine le pouvoir d'emprunt des collatéraux. Un prêt à valeur maximale de 50 % signifie que l'on peut emprunter jusqu'à la moitié de la valeur en dollars des collatéraux déposés.
{{< /notice >}}

*   Maker : Ratio minimal = 150% ⇒ environ 66% max LTV
*   Liquity : Collateralisation ratio minimal = 110% ⇒ environ 90% max LTV

Liquity innove également du côté des frais puisque **les emprunts se font sans intérêt** contrairement à d'autres systèmes. Sur Maker/ETH par exemple, le stability fee est de 5.5%. Si vous empruntez 10 000 DAI aujourd'hui, vous devrez rembourser 10 550 DAI dans 1 an (si les frais ne changent pas).

![Liquity](/img/2021/money-market-innovations/liquity.png "Un emprunt sans intérêt et sans autre frais que 0.5% de borrowing fee payé immédiatemment")

Sur Liquity au contraire, il n'y a pas de stability fee. À la place, les utilisateurs paient **un frais unique et immédiat lors de l'emprunt**. Ce frais dépend du "base rate" qui est gouverné par le protocole directement. Il est actuellement à 0.5%.

Sur Liquity, ceux qui déposent des ETH pour frapper des LUSD peuvent ensuite les déployer dans la Stability Pool (LUSD) ou la paire LUSD/ETH pour une rémunération en LQTY – le token natif du service.[^LQTY] Les LQTY peuvent ensuite être stakés pour **obtenir une part des LUSD payés au protocole lors de la contraction d'un prêt** ainsi que les frais de rédemption (ETH ↔ LUSD).

{{< notice note >}}
Liquity est une plateforme dite " governance mimized"  — LQTY n'est donc pas un token de gouvernance.
{{< /notice >}}

Enfin, Liquity innove également en termes de décentralisation puisque **l'interface utilisée pour accéder au service n'est pas gérée par l'équipe derrière le protocole**. Différents "frontends" opérés par des tiers sont proposés tandis que l'équipe se concentre sur le protocole en lui-même. Cela permet de s'assurer que de nombreux "mirrors" existent afin que le service reste toujours aisément accessible.

---

## La prochaine étape pour comprendre les marchés monétaires

J'espère que cette découverte des dernières innovations sur les marchés monétaires aura été instructive pour vous. Je suis ravi de voir l'offre se développer et se densifier pour couvrir des besoins toujours plus variés. Les marchés monétaires sont des éléments essentiels de la DeFi, avec la croissance de l'espace ils sont appelés à devenir de plus en plus prépondérants.

Pour finir, permettez moi de vous rappeler qu'outre les fonctionnalités, **la gestion du risque est l'élément essentiel qui différencie les différents marchés monétaires**. Avant de commencer à déployer des sommes conséquentes sur ceux-ci, je vous invite à vous familiariser avec les risques associés. Ça tombe bien, j'ai écrit ce qui reste à ce jour **la synthèse la plus exhaustive et compréhensible pour comprendre les risques encourus au niveau des marchés monétaires**, je vous invite à la lire :

**[De l'évaluation du risque sur les marchés monétaires en finance décentralisée](https://tokenbrice.xyz/fr/marche-monetaire-risque/)**

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

[^LQTY]: Retrouvez [plus d'infos sur la distribution de LQTY](https://docs.liquity.org/faq/lqty-distribution-and-rewards) dans la doc.

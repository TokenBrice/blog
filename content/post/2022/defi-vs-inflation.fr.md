---
title: "Comment construire un portefeuille DeFi résistant à l'inflation ?"
description: "Et si la DeFi, plus que jamais, offrait des réponses sérieuses et crédibles aux enjeux économiques et financiers ? Illustration avec l'inflation gallopante et les divers produits et stratégies qui peuvent être mis en place pour s'en prémunir."
date: '2022-03-08T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Comprendre]
tags: [DeFi, Ethereum, Finance décentralisée, Stablecoins, Actifs stables, Marchés Monétaires, Reflexer, RAI, Maker, Liquity, Curve, Convex, Aave, APWineFi, vlCVX, Stablecoin, Yearn Finance, Harvest Finance, Fuse, jFiats, Inflation, Dollar, stagflation, PT, FYT]
toc: true
tocNum: false
url: defi-vs-inflation
---


L’inflation est plus que jamais au centre des discussions et préoccupations : personne n’y comprend grand-chose, aucun économiste ne l’a vraiment anticipée, mais nous avons tous un avis dessus. 

Aujourd’hui, on laisse l’économie et la politique de côté pour se concentrer sur le concret : en finance décentralisée, toutes sortes de protocoles sont développés, et une bonne partie d’entre eux **apportent des outils crédibles et novateurs pour préserver et développer le pouvoir d’achat d’un portefeuille**, même lorsque le contexte macroéconomique est des plus incertains.

Je vous propose donc d’évaluer des stratégies impliquants des actifs et protocoles différents, toutes avec le même but : préserver et développer le pouvoir d’achat effectif d’un portefeuille donné. Néanmoins, il faut commencer par la base, le niveau 0 : qu’est-ce que l’inflation et pourquoi nous, DeFians, devrions-nous en soucier ?

![defi-vs-inflation-tokenbrice-cover](/img/2022/defi-vs-inflation/defi-vs-inflation-tokenbrice-cover.jpg)

_L'image de couverture a été réalisée par un généreux contributeur anonyme et met en scène les majestueuses **[Valkyr-E](https://rarible.com/valkyre/created)**_

## α/ Tutoriel : Comprendre l’impact de l’inflation sur un portefeuille crypto

Je ne m’hasarderais pas à rentrer en détail sur l’inflation pour les monnaies fiduciaires ici, mais le concept de base est connu de toutes personnes familières avec les cryptomonnaies. 

Avant de rentrer dans le vif du sujet, partons de la base : l’inflation, telle que définie par l’Insee (Institut National de la Statistique et des Études Économiques) :

> L'inflation est la perte du pouvoir d'achat de la monnaie qui se traduit par une augmentation générale et durable des prix. Elle doit être distinguée de l'augmentation du coût de la vie. La perte de valeur de la monnaie est un phénomène qui frappe l'économie nationale dans son ensemble (ménages, entreprises, etc.).

Rappelons juste que, **tout comme en DeFi où chaque token est associé à un protocole et potentiellement même un écosystème, chaque monnaie fiduciaire s’appuie sur une économie ainsi qu’un ensemble de règles** (système légal).


### L’inflation, point de vue macro (échelle = pays)

L’inflation correspond à la production de nouvelle monnaie, l’important n’est pas tant la quantité de monnaie créée, mais plus **ce qui est fait avec**. On le comprend tous plutôt bien avec deux exemples caricaturaux à chaque extrême :



1. La banque centrale d’un pays A émet une quantité importante de monnaie afin d’investir massivement dans ses infrastructures de transport et son approvisionnement énergétique (= investissements long terme). 

_Ici, l’inflation peut être a priori maîtrisée car la nouvelle monnaie émise sert à financer des investissements développant le potentiel économique du pays sur le long terme (-> compensation)_

2. La banque centrale d’un pays B émet une quantité importante de monnaie afin de financer un plan d’urgence visant à compenser les conséquences prévisibles de précédentes mesures pseudo-sanitaires.

_Dans ce second scénario, la nouvelle monnaie est utilisée pour couvrir une “dépense courante" de l’État. L'équivalent à votre échelle personnelle serait de vous endetter chaque midi pour payer votre déjeuner. C’est évidemment intenable sur le long terme. Dans ce scénario, l’inflation ne peut être que massive car une quantité importante de nouvelle monnaie est émise, tandis que le potentiel économique du pays en question stagne ou se détériore._


### Évaluer l’inflation à venir ?

Assez pour le macro, revenons à notre échelle, avec des choses que l’on connait bien. Voici  l'évolution de la masse monétaire M1 sur le dollar, cela permet de visualiser sa “marketcap” en quelque sorte :

![USD M1 Supply](/img/2022/defi-vs-inflation/USD-m1-supply.png "Une représentation de l'évolution du total circulant d'une PARTIE des dollars")

_Ici on ne regarde que M1 par simplicité mais la tendance est similaire sur M2 et M3._

On s’intéresse ici au dollar qui, bien que challengé, reste la monnaie fiduciaire qui donne le ton. Comme vous pouvez le voir, la courbe part à la verticale depuis le début de la crise Covid. L’allure de la courbe est désormais bien plus effrayante que les pires shitcoins que j’ai pu croiser. Vous en doutez ? Considérez la même information, présentée sous cet angle :

**Le dollar existe depuis 1914. 20% de tous les dollars en circulation ont été créés en 2020. Au rythme actuel, la quantité totale de dollars en circulation double tous les 4-5 ans environ.**

Pour  comparer avec la crypto, nombreux sont ceux qui se soucient de l’inflation / émission de nouveau token sur Curve Finance (CRV). La courbe d'émission sur 4 ans ressemble à ceci :

![crv-release-schedule](/img/2022/defi-vs-inflation/crv-release-schedule.png "Courbe d'émission du token CRV")



Je ne suis pas économiste, mais je connais mes shitcoins. Le chiffre officiel de l’inflation américaine qui nous est donné est 7.5% par an. Comme les chiffres du chômage, c’est une métrique hautement politique qu’il est dur d’apprécier réellement. 

Le chiffre de 7.5% peut sembler élevé, mais il reste faible face à la création monétaire sans précédent réalisée pour faire face au Covid. Je m’attends ainsi à voir cette inflation augmenter encore, ou alors se maintenir sur une période prolongée d’une dizaine d’années.

L’inflation est donc là, à 7.5% minimum pour plusieurs années a priori. Assez pour la macro de boomer, voyons donc l'éventail d’outils que la DeFi nous offre pour lui faire face et la dépasser.


## I/ Battre l’inflation grâce des rendements sur stablecoins “classiques”

La première approche est comme toujours la plus simple, **la méthode brute** : une inflation de 7.5% signifie que des USD laissés tels quels perdront 7.5% de leur valeur sur l’année. Il s’agit donc ici de trouver une source de rendement supérieur à l’inflation : la différence entre les deux correspond au rendement effectif.

Avec une inflation à 7.5% sur l’USD, je pense qu’il est prudent de s’assurer d’**atteindre au moins 1.5x ce chiffre en rendement** pour réellement se considérer à l'abri de l’inflation.

Ici, le jeu est simple et les règles assez faciles à comprendre :



1. On part d’une position dans un stablecoin donné
2. Le but est de la rendre productive, sans assumer de risque d’IL
3. Avec un rendement qui dépasse le chiffre de l’inflation, une fois les frais en gas amortis.


### Simple dépôt de stablecoin

On visera donc **un rendement 10.875% annuel sur stablecoin $ au strict minimum**. Avec les baisses récentes et la compression des rendements c’est de plus en plus difficile, mais encore trouvable même avec un dépôt dans un seul stablecoin sans risque d’IL. Des outils comme [Coindix](https://coindix.com/?kind=stable&sort=-apy&chain=ethereum) peuvent vous aider à trouver le vault de vos rêves :

![coindix](/img/2022/defi-vs-inflation/coindix.png)


Attention cependant, **tous les vaults ne se valent pas** ! Par exemple, on voit de beaux rendements sur Bancor sur la capture d’écran : n’oubliez pas de considérer la volatilité de ces rendements ainsi que les frais en gas pour déployer la position (un LP Bancor est notoirement plus coûteux qu’un dépôt sur Yearn par exemple).


{{< notice warning >}}
Je le mentionne ici pour l’oublier aussi vite après : le protocole [Anchor](https://app.anchorprotocol.com/) vous offre également un rendement “fixe” proche de 20% sur le stablecoin UST. Un tel taux garanti ne s’obtient pas, bien sûr, sans de sérieux compromis qui posent de réelles questions sur la pérennité de l’ensemble de cet écosystème (Terra/Luna).
{{< /notice >}}


### Apport de liquidité + engagement temporel

Toujours en dollar, mais un peu plus risqué, on peut considérer différents types d’engagement, toujours en stablecoin dollar et avec des risques d’IL très maîtrisés. Par exemple, un apport de liquidité entre FRAX et DAI.

![FRAX/DAI LP opportunities on Frax](/img/2022/defi-vs-inflation/frax-dai.png "Opportunités LP sur FRAX/DAI")


Ici, ca se passe chez [Frax Finance](https://frax.finance/), le taux de base (x1) correspond tout juste à notre objectif minimum, mais il est possible d’atteindre jusqu’à x5 avec deux types d’engagement :



* X3 en verrouillant les tokens LP pendant 3 ans
* X2 grâce à vos potentiels veFXS (bien plus dur à atteindre)

Le rendement effectif d’une position verrouillée pour trois ans correspond à environ 3 fois notre objectif minimum, offrant ainsi une protection crédible contre la perte de valeur suite aux conséquences de l’inflation, mais encore faut-il pouvoir assumer les trois ans d’engagement.

L’exemple est pris ici sur DAI, mais la situation est similaire sur les autres stablecoins majeurs ; par exemple, voici les pools FRAX/USDC :

![FRAX/USDC LP opportunities](/img/2022/defi-vs-inflation/frax-usdc.png "Opportunités LP sur FRAX/USDC")

{{< notice tip >}}
Convex pour Frax arrive (optimisation du farming des LPs Frax via Convex), si vous n’avez pas vos propres veFXS, il est probablement pertinent d’attendre la sortie du service pour prendre une décision avec toutes les cartes en main.
{{< /notice >}}

### Spéculation sur le taux de rendement et tokénisation

Pour battre ces fameux 10% de rendement sur le dollar, il existe encore bien d’autres options. Je vous en présente une dernière ici pour vous aider à envisager les autres stratégies possibles.

Pour celle-ci, on s’appuie sur [APWine](https://apwine.fi/), un protocole qui permet la tokénisation des rendements futurs d’actifs productifs. Le principe est à la fois simple et complexe : déposer un actif sur APWine permet de séparer son rendement futur (token FYT: Future Yield Token) du principal sous-jacent (PT: Principal Token). 

À partir de là, différentes stratégies sont possibles, comme par exemple vendre immédiatement le rendement futur (FYT) afin d’augmenter la quantité du principal productif. Un tel outil permet également de mieux gérer son risque dû à la volatilité des taux de rendements.

Restons sur des choses simples et tout de même largement au-dessus des 10% requis : faisons un zoom sur le vault aUSDT de [APWine](https://app.apwine.fi/):

![APWine aUSDT vault](/img/2022/defi-vs-inflation/apwine-USDT-fr.png "Le vault aUSDT sur APWine")


J'exclue d’office la pool PT/FYT qui est plus complexe à comprendre et présente des risques bien plus conséquents que la PT/Underlying offrant un rendement en APW à 44% tout de même.

Ici la stratégie est simple, mais il faut **garder en tête les frais en gas importants liés à l’utilisation d’APWine**. Pour mettre en place la stratégie à partir d’USDT dans le wallet, il faut :



1. Allow + Dépôt d’une partie de ceux-ci sur Aave (55% max)
2. Allow + Dépôt des aUSDT obtenus en 1 sur APwine
3. Allow (x2) + Dépôt des PT et Underlying (USDT) en apport de liquidité
4. Allow + Stake des tokens LPs PT/Underlying pour obtenir le rendement en APW
5. Ne pas oublier également les frais en gas liés aux claims des APW + déroulement de la position à la fin de l’époque (ou avant).

Il est donc préférable d’attendre un jour où les transactions passent sous 30 gwei pour ne pas trop souffrir des coûts en gas sur une telle stratégie.

L’avantage ici, par rapport à Frax par exemple, c’est que **la position est bien plus liquide**. APWine fonctionne avec une logique d’epoch qui durent 90 jours. Ainsi, pour amortir plus facilement les frais en gas il est préférable de déployer la stratégie en début d’epoch : c’est aussi là où les rendements sont généralement les plus élevés.

Le troisième winelisting (là où sont décidés les prochains tokens supportés sur APWine) vient de s’achever, n’hésitez pas à vous y préparer :

![APWine - Winelisting 3](/img/2022/defi-vs-inflation/apw-winelisting3.png "Les résultats du troisième winelisting sur APWine")


APWine est encore un protocole jeune, mais la gouvernance est dynamique. La prochaine étape approche : tout comme sur Curve, ce seront bientôt les holders de veAPW (APW verrouillés) qui [décideront des émissions](https://gov.apwine.fi/t/apgp-2-enable-gauges-for-apw-rewards/171) pour chaque vault donné. Une redistribution des cartes est à envisager, prévoyez en connaissance de cause.


## II/ Positions productives hedgées avec différents stablecoins “alternatifs”

On est resté pour l’instant sur le dollar, c’est plus simple pour commencer. Bien que les stablecoins dollars soient encore largement dominants, il existe désormais **de nombreux stablecoins basés sur d’autres monnaies fiduciaires** comme l’EUR, le JPY (Yen Japonais), le CHF (Franc Suisse), KRW (Won Coréen) ou encore CAD (Dollar Canadien).

Outre les quelques stablecoins centralisés (EURS ou EURT) c’est un marché surtout couvert par des protocoles qui proposent de créer des stablecoins synthétiques à partir d’autres stablecoins. C’est le cas par exemple de [Jarvis Network](https://jarvis.network/), qui utilise l’USDC pour collatéraliser différents types de stablecoins : jEUR, jCHF, jKRW, etc.


### Simple dépôt

Les opportunités natives de rendement sans IL sur de tels stablecoins sont encore assez rares, et se situent généralement sur Curve : l’apport de liquidité contre d’autres stablecoins basés sur la même monnaie fiduciaire, s’il y en a.

![Pool CHF sur Curve Finance](/img/2022/defi-vs-inflation/curve-chf.png "Une pool CHF sur Curve Finance")


Seuls quelques stablecoins ont des options lucratives en dépôt simple jEUR, jCHF, jJPY. Elles s’appuient sur les pools Curve correspondantes, avec des incitations additionnelles offertes par Jarvis et d’autres projets.

Via Jarvis (aussi disponible farmé par Harvest), il est également possible de produire un rendement sans IL sur jCAD et jJPY.


### Apport de liquidité

Malgré tout, il existe une approche un peu différente, plus risquée, mais également potentiellement plus protectrice contre l’inflation : l’apport de liquidité sur deux stablecoins représentants deux monnaies fiduciaires différentes, par exemple EURT/3pool (USD) toujours sur Curve.

Plus intéressant encore, surtout pour les portefeuilles plus modestes, de nombreux stablecoins alternatifs sont disponibles sur Polygon ou Avalanche, avec un écosystème assez dense.

Ainsi Jarvis propose des pools jCHF-USDC, jEUR-USDC ou encore jCAD-USDC avec des rendements supérieurs à 20%. Des outils comme [Harvest.Finance](https://harvest.finance/) ou encore [Beefy.Finance](https://beefy.finance/) peuvent être également utilisés pour composer automatiquement les rendements obtenus :

![Harvest Network Jarvis jFIAT](/img/2022/defi-vs-inflation/harvest-jarvis-2-stables.png "Vaults jFIATs sur Harvest Finance")


Attention : en fonction de votre actif de base (par ex USDC), s’exposer à de l’EUR (ou autre monnaie) peut être lucratif ou coûteux - tout dépend de l’évolution du taux de change USDC/EUR.

Enfin, pour les plus aventuriers d’entrevous, sachez qu’APWine est également disponible sur Polygon et supporte déjà plusieurs tokens de Jarvis, comme par exemple le MooJarvis_4eur :



1. Apport de liquidité sur Curve (4eur)
2. Géré par Beefy Finance (moo)
3. Qui compose le rendement que Jarvis offre automatiquement

Là encore, l’addition des tokens votés lors du winelisting 3 va ouvrir de nouvelles portes avec l’arrivée prochaine sur APWine/Polygon de :



* MooKyber_USDC-jEUR
* MooMai_USDC-MAI


### Emprunts Forex

Enfin, si les liquidations ne vous font pas peur, sachez qu’une pool Fuse sur Polygon ([Pool7 - Jarvis Forex Market](https://polygon.market.xyz/pool/7)) vous permet l’utilisation de différentes jFiat comme collatéral ainsi que pour emprunter. 

![Fuse pool 7](/img/2022/defi-vs-inflation/fuse-pool7.png "Jarvis Forex Market (Fuse/Polygon/Pool7)")


Avec un tel service, presque tout est possible, voici quelques exemples pour vous inspirer :



* Long le USD + short EUR = MAI en collatéral, emprunt jEUR puis vente du jEUR et potentielle boucle
* Short GBP via CHF = jCHF en collatéral, emprunt jGBP puis vente et potentielle boucle.

{{< notice tip >}}
Notez également que les stablecoins productifs m2CAD et m2JPY sont disponibles en collatéral tout en gardant leur rendement intéressant pour des stratégies de leverage plus classique.
{{< /notice >}}


### Trouver son équilibre

Plus qu’une seule position magique, ce qui me plait avec les stablecoins de Jarvis c’est la possibilité de **diversifier facilement vers différents types de monnaies fiduciaires**. Grâce aux frais de transaction modérés sur Polygon, il est tout à fait possible de mélanger plusieurs monnaies et positions différentes pour faire un ensemble cohérent et bien protégé contre son inflation locale. 

Par exemple, pour un Européen (= qui dépense des €) :



* 25% en stable € productif sans IL, par exemple MooJarvis_4eur (+APWine)
* 25% en jEUR/USDC
* 20% en stable dollar productif (par ex stratégie aUSDT APWine)
* & Diversification: 15% jCHF/USDC + 15% jGBP/USDC

Enfin, tant qu’on discute de stablecoins “exotiques” sachez qu’il en existe également quelques-uns qui suivent l’or ou l’argent - ils peuvent être également pertinents dans une telle perspective. Par exemple XAUT (avec pool Curve XAUT/3crv). L’or et l’argent restent des reliques ~~barbares ~~ de boomers, personnellement je n’y vois que très peu d’intérêt pour un DeFian compétent.


## III/ Les stablecoins résistants à l’inflation

Battre l’inflation, c’est chouette. La hedger, encore mieux. Mais **pourquoi pas tout simplement l’abstraire**, en utilisant des produits qui résistent naturellement à celle-ci ? Il n’y a encore que très peu de stablecoins qui ne sont pas adossés à une monnaie fiduciaire, mais l’offre se développe rapidement.


### RAI, le premier stablecoin libéré du dollar

RAI est une drôle de bête, le tout premier “unpegged stablecoin”. Lancé à une valeur de Pi en USD (3.14) en 2021, il évolue entre 3.02 et 3.06 quasiment depuis son lancement. Étant donné son arrivée récente (à peine plus d’un an), il est dur d’envisager comment RAI va se comporter dans une période d’inflation prolongée.

Malgré tout, diversifier une partie de ses stablecoins vers du RAI peut être une option intéressante. En outre, différentes options de rendement existent sur RAI :



* Simple dépôt sans risque d’IL : Idle Finance déposez vos RAI dans Fuse/Aave pour optimiser le retour natif + incentives en FLX de Reflexer + incentives en IDLE.

![RAI on Idle Finance](/img/2022/defi-vs-inflation/rai-idle-0.png "Le vault RAI sur Idle Finance")

![Additional FLX incentives for RAI on Idle Finance](/img/2022/defi-vs-inflation/rai-idle.png "Incentives FLX supplémentaire sur Idle/RAI")

* En assumant des risques d’IL via un apport de liquidité sur Curve contre la 3pool, un meilleur rendement est possible. Le crvRAI peut ensuite être staké directement sur Curve ou via Convex ou encore Yearn.

Le RAI s’appuie sur un mécanisme inspiré de Maker MCD mais avec de nombreuses modifications pour rendre le tout possible. Pour comprendre comment il fonctionne, je vous invite à lire [mon article dédié](https://tokenbrice.xyz/fr/reflexer-rai/).

{{< notice note >}}
🚧 Signale que le protocole mentionné est encore en développement.
{{< /notice >}}

### 🚧 Un stablecoin résistant à l’inflation ? Le FPI de FRAX

Le Frax Price Index, c’est un nouveau protocole qui devrait arriver prochainement au sein de l’écosystème Frax. Le but est de proposer un nouveau stablecoin, qui suivrait le CPI (Consumer Price Index) afin de se prémunir contre l’inflation. Tout comme Frax, **le système s’appuie sur deux tokens** : 
1. le stable - Frax Price Index (FPI) 
2. et le token de gouvernance Frax Price Index Share (FPIS).

[La documentation de Frax](https://docs.frax.finance/frax-price-index/inflation-hedge) vous offre quelques informations sur le token à venir. **Un airdrop de FPIS est prévu** pour les holders de veFXS ou encore cvxFXS. Ainsi, le protocole sera indépendant de FRAX/FXS, bien qu’un mécanisme de capture de valeur vers FXS est prévu au-delà de l’airdrop initial.

Il est dur de se projeter sur un simple design envisagé, mais il est clair qu’un stablecoin qui maintiendrait sa valeur malgré l’inflation est un produit très désirable. **Plusieurs questions se posent quant au maintien du peg sur FPI** : pour maintenir son équilibre, il va falloir que des gens prennent le trade contraire au FPI, c’est à dire “short inflation”. Or, dans le contexte actuel avec une inflation galopante, on a du mal à envisager qui pourrait assumer une telle position.

Néanmoins, l'arrivée du FPI est imminente. On trouve des traces du token [FPIS sur EtherScan](https://etherscan.io/token/0xdb68c6264e9d0f8a6df1fa5a89f205da38698d15) depuis début Mars. J’ai hâte de voir le design proposé par l’équipe Frax pour répondre à ces enjeux conséquents.


### 🚧 Résistance à l’inflation + degen = VOLT

En parallèle au FPI de Frax, il y a un autre projet que je suis de près, que j’attend depuis longtemps et qui porte de grands espoirs pour moi. Le concept de haut niveau est très simple : un produit du type Abracadabra qui ne serait pas une faille de sécurité ambulante.

En effet, Abracadabra permet d’emprunter depuis divers collatéraux productifs, ce qui rend le service désirable. Néanmoins l’infrastructure proche du bidouillage et les agissements des membres de l’équipe font d’Abracadabra un marché monétaire de seconde ou troisième zone. 

L’idée ici, avec Volt, c’est de couvrir la même verticale en utilisant une infrastructure qui a fait ses preuves : la base offerte par Reflexer (RAI). Trois modifications principales sont attendues sur ce modèle :

1. Contrairement à Reflexer qui n’accepte que ETH en collatéral, Volt va diversifier les options disponibles, notamment avec des collatéraux productifs type wstETH. 
2. La valeur de VOLT, le stablecoin du système, sera indexée sur le FPI de Frax. L’infrastructure de Reflexer sera là encore réutilisée (PID controller adapté)
3. L’équipe de Volt travaille également en collaboration avec Fuse et Olympus.

Pour suivre Volt, rien de mieux que [leur Discord ](https://discord.gg/dGhvDmCNGr)!

{{< notice note >}}
Je décris ici le design initial de Volt Protocol, qui a évolué depuis. La vision de créer un service d'emprunt avec un stablecoin résistant à l'inflation demeure, mais les choix techniques ont évolué. Lisez [le whitepaper disponible ici](https://github.com/volt-protocol/whitepaper/blob/main/volt.md) pour les dernières informations.
{{< /notice >}}

## IV/ Battre l’inflation grâce à des rendements sur actifs volatils

**Dans un monde où plus rien ne tient et la valeur fuit, que nous reste-t-il ?** Et pourquoi pas de bons actifs DeFi qui ont fait leurs preuves et sont adossés à des protocoles aux revenus massifs et récurrents partagés directement avec leurs holders ?

Il en existe quelques-uns, très peu. On va les détailler un à un, ainsi que les différentes options disponibles sur ceux-ci pour produire un rendement.


### ETH : l’origine et la fin

Il y a bien sûr l’ETH, qui connaît de nombreuses sources de rendements divers - tout comme sur les stablecoins, rien ne vous empêche de diversifier votre exposition ETH avec plusieurs sources de rendement, par exemple:



* ETH staké avec [Lido Finance ](https://lido.fi/)(rendement faible, mais à priori le plus sûr) [~5%]
* LP [rETH](https://rocketpool.net/) sur Curve (plus novateur, plus lucratif, plus risqué) [~10%]
* Vault covered call options sur ETH via [Stakedao](https://stakedao.org/) ou [Ribbon Finance](https://www.ribbon.finance/) [~25%, risques !]
* Apport de liquidité cross-chain sur un Bridge, par exemple [Celer](https://cbridge.celer.network/#/liquidity) [~10%]

Une position ainsi équilibrée suit l’inflation / la dépasse légèrement avec les rendements obtenus sur les ETH. La profitabilité de la position sur le long-terme dépend bien sûr essentiellement du prix d’entrée moyen sur ETH et de l’évolution de celui-ci.


### CRV, CVX, et FXS : Les trois Parques de la DeFi ?

Chez les romains, les Parques sont trois déesses qui gouvernent la vie des humains :

1. Nona tisse le fil de la vie
2. Decima le déroule
3. Morta le découpe

La DeFi connaît elle aussi ces Parques : trois protocoles qui jouent un rôle critique dans la survie et la croissance de potentiellement tout autre.

En effet, outre l’ETH, il y a plusieurs projets DeFi qui ont déjà fait leurs preuves, contrôlent des flux de revenu conséquents et offrent un service réellement pertinent dans un contexte macro d’inflation prolongée ; j’en vois trois essentiellement :

1. **Curve Finance - CRV** : la mère de tous les yields en DeFi + machine à peg et liquidité.
2. **Convex Finance - CVX** : une option sur CRV, qui contrôle quasi 50% de tous les CRV verrouillés et apporte une réelle valeur ajoutée.
3. **Frax Finance - FXS** : projet stable innovant, DeFi natif, très productif via les AMOs + arrivée de FPI + Frax possède une grosse position sur CVX & quelques autres protocoles.

Tout en étant des tokens adossés à des protocoles essentiels en DeFi, les options de rendement sur ces trois tokens ne manquent pas :

1. CRV -> Dépôt sur Convex en CvxCRV puis stake ou LP cvxCRV/CRV.
2. CVX -> Vote locked sur Convex en vlCVX -> rendement en cvxCRV + bribes
3. FXS -> Dépôt direct sur Frax (veFXS) ou gestion via Convex (cvxFXS).


### D’autres tokens prometteurs

Enfin, il reste d’autres projets qui n’ont pas encore atteint la profitabilité de Curve ou Convex mais représentent des paris crédibles. Dans un monde où l’inflation est là durablement, les outils qui vont permettre de s’en prémunir peuvent devenir très populaire : je vous propose quelques autres thèses toujours en lien avec ce qui a été mentionné dans l’article.


#### APWine.fi (APW) : pari sur l’infrastructure DeFi avancée

Quand l’inflation monte, tout le monde cherche du rendement. Laissez les courir derrière les %, et ciblez plutôt les vendeurs de pioches dans cette ruée vers l’or. C’est la thèse principale derrière un pari sur APW.

Comme vous avez pu le voir dans l’article déjà, APWine offre des produits intéressants pour parier sur l’évolution des rendements ou encore réaliser immédiatement un rendement futur. Au fur et à mesure que la DeFi se développe, la demande pour un produit type APWine ne fait que grandir. Est-ce que ce sera APWine, ou un autre ? À vous de voir !

Avec l’arrivée des APWine Wars, il n’est pas fantoche d’envisager à terme des bribes similaires à ce qu’on peut voir sur Convex.


#### Reflexer (FLX) : pari sur la dégouvernance

Outre l’approche technique très intéressante, Reflexer innove également à un autre niveau. En effet, depuis le lancement du protocole, l’équipe a présenté un “Plan de Dégouvernance” visant à progressivement minimiser le contrôle de l’équipe sur le protocole grâce à deux moyens principaux :

* Automatisation de tout ce qui peut l’être
* Gestion par les holders de FLX pour les situations nécessitant encore une analyse manuelle / prise de décision.

En outre, **Reflexer dépasse désormais RAI**. La Money God League et un ensemble de projet construit l’infrastructure Reflexer, avec le soutien de l’équipe. Il semble donc assez naturel d’envisager un airdrop de ces nouveaux projets, dont VOLT, vers les holders de FLX.

Dernier tuyau : les stakers du LP FLX/ETH dans le Safety Module de Reflexer sont les derniers recours qui permettent de garantir la solvabilité du protocole. Si je devais envisager un airdrop pour remercier la communauté Reflexer, c’est sans doute eux que je viserai en priorité


#### LooksRare (LOOKS) : pari sur les NFTs

Voyez LOOKS comme une option sur le marché NFT. En effet, LooksRare est la première place de marché NFT qui partage ses revenus. Cela se traduit par **un rendement en ETH pour stakers de LOOKS qui a pu atteindre 3 chiffres soutenus pendant les premières semaines**.


![ETH yields on LOOKS staking](/img/2022/defi-vs-inflation/looks-eth-farm.jpeg "Rendement de ~69 000 LOOKS stakés durant les deux premières semaines d’existence du protocole") 

Depuis, le volume de transactions a baissé et le rendement en ETH avec, mais **le staking LOOKS reste l’un des plus gros yields en ETH qui existe**.

Je m’arrête à ces trois suggestions, mais il y a bien sûr d’autres options - à vous de juger. Par exemple, les QI Wars ont commencé et le protocole a une bonne traction. Attention cependant à ne pas tomber dans le piège qui consiste à penser que tous les protocoles qui adoptent le modèle ve + bribes connaîtront le succès de Curve et Convex. Les tokenomics ve vont se multiplier : il s’agit de faire les bons choix !

---

## Bonne chance et joyeuses récoltes 🚜

Je serai tenté de m’excuser pour la longueur de cet article, mais je reste confiant que sa lecture vaut le détour et sera instructive même pour les DeFians les plus avertis.

Si vous avez envisagé d’autres stratégies ou protocoles utiles pour se protéger de l’inflation, n’hésitez pas  à me les suggérer.

Pour approfondir, voici quelques lectures recommandées :



1. [Comprendre les Curve Wars](https://tokenbrice.xyz/fr/crv-wars/) 
2. [Comprendre le modèle du RAI de Reflexer](https://tokenbrice.xyz/fr/reflexer-rai/)

Et enfin pour la pratique, qui reste ESSENTIELLE, le mieux est encore d’essayer avec de petites sommes sur des sidechains/L2 peu coûteux :


1. Le protocole APWine sur Polygon afin de vous familiariser avec ces mécanismes.
2. Minting jFIAT / Apport de liquidité sur Curve + farming pour découvrir Jarvis
3. Long/short sur Forex grâce aux jFiats + Fuse.


{{< notice info >}}
Disclosure: J’ai investi dans la pre-sale d’APWine et je suis un grand utilisateur du protocole. Je suis utilisateur et souvent holder de quasi tous les protocoles mentionnés dans cet article. 

Cet article ne constitue pas un conseil en investissement : je partage simplement mes recherches pour vous aider à faire les votres.
{{< /notice >}}

_🙏 Un grand merci à [Charles](https://twitter.com/C53300), [PhilH](https://twitter.com/phil_h) et [Disiaque](https://twitter.com/disiaque_eth) pour leur relecture attentive et leurs nombreuses suggestions pertinentes._

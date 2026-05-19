---
title: "Pourquoi Polaris ? Le stablecoin qu'il fallait construire"
description: "Pourquoi Polaris vise un stablecoin sans contrepartie, au coeur immuable, après des années de compromis entre croissance et décentralisation."
date: '2026-01-27T01:13:50.191Z'
categories: [Projects, Lending]
tags: [DeFi, Ethereum, Lending, Stablecoins]
series: stablecoin-arc
series_order: 7
url: why-polaris
aliases:
  - p/why-polaris
image: /img/2026/why-polaris/why-polaris-cover.jpg
toc: false
draft: false
type: post
difficulty: "beginner"
---

Les stablecoins ont gagné : ils sont l'épine dorsale de la liquidité DeFi, l'unité de compte des échanges onchain et le cas d'usage DeFi le plus visible vers l'extérieur. Selon toutes les métriques d'adoption, ils sont le primitive la plus réussie que nous ayons construite. Et pourtant, quelque chose a dérapé. Les modèles dominants de stablecoins se sont éloignés de leurs promesses initiales. Ce qui avait commencé comme des expérimentations de monnaie décentralisée est discrètement devenu une collection de dépendances TradFi emballées dans une esthétique de smart contracts. Les fondations se sont dégradées à mesure que la TVL montait. Les stablecoins les plus populaires restent des T-Bills tokenisés qui ne redistribuent pas leur rendement, notamment USDC et USDT.

Il est temps pour moi de sortir du mode furtif et de révéler un projet qui mijote depuis 2 ans : [Polaris](https://polarisfinance.io). Mais avant d'en arriver là, je veux que vous compreniez mon moment "Vitalik a décidé de construire l'ordinateur mondial après le nerf de son démoniste dans WoW". Deux histoires illustrent le schéma que je décris : ce sont deux protocoles que j'ai suivis de près. Ils ont commencé avec des prémisses nouvelles, puis ont fini complètement ailleurs.

## Pigeon un jour, pigeon toujours

En 2022, Rune Christensen a présenté l'Endgame Plan de MakerDAO : une feuille de route stratégique pour l'évolution du protocole. Elle était structurée autour de trois "stances", chacune représentant un équilibre différent entre croissance et résilience.

- **Pigeon Stance :** croissance maximale, aucune résilience. Exposition RWA illimitée. Tous les revenus servent à acquérir de l'ETH. Cette phase était explicitement décrite comme fragile, nécessaire pour amorcer le système, mais pas comme destination.
- **Eagle Stance :** un point de transition. Exposition RWA plafonnée à 25 %. Équilibre entre croissance et résilience. Le plan disait que cette étape arriverait "après 3 ans, sauf report par la gouvernance".
- **Phoenix Stance :** l'objectif final. Résilience maximale. Aucune exposition RWA saisissable. Un stablecoin capable de survivre à la pression autoritaire parce qu'il n'aurait rien à saisir.

La Phoenix Stance était la promesse, et la Pigeon Stance un compromis nécessaire pour l'atteindre. Nous sommes maintenant en 2026, et Maker reste extrêmement dépendant des RWA, toujours en Pigeon Stance. La gouvernance a repoussé la transition indéfiniment. La clause d'échappement intégrée au plan ("sauf report par la gouvernance") est devenue l'état permanent.

DAI est maintenant massivement adossé à des actifs du monde réel. La transition vers USDS a aussi été l'occasion d'ajouter des fonctions de blacklist et de gel : **DAI/USDS est devenu USDC avec des étapes supplémentaires**. Le protocole qui a inventé les stablecoins décentralisés dépend opérationnellement du système financier traditionnel qu'il devait contourner.

![forever-pigeon](img/2026/why-polaris/forever-pigeon.png)

Le pigeon n'a jamais appris à voler.

## Le pivot silencieux

Ethena a lancé USDe avec un narratif convaincant : un stablecoin générant du rendement grâce au basis trade. Des positions delta-neutres entre marchés spot et perpétuels. Le pitch était propre, et rendait accessible à tous une stratégie auparavant bien plus exigeante et complexe à mettre en oeuvre.

Puis les conditions de marché ont changé. Après le 10 octobre 2025, les rendements du basis trade se sont comprimés. Le spread qui finançait les rendements d'USDe s'est resserré à des niveaux incapables de soutenir le rendement promis. Ethena avait un problème. USDe a discrètement déplacé sa source de rendement et commencé à tirer ses retours de T-Bills tokenisés via pyUSD. Le moteur de rendement onchain et crypto-native est devenu un wrapper de T-Bills de plus.

Pourtant, la plupart des détenteurs d'USDe ne l'ont pas réalisé. Demandez autour de vous d'où vient le rendement d'USDe, et les gens répondent encore presque automatiquement : "basis trade". Ils avaient raison il y a environ six mois ou plus, quand ils y ont déposé des fonds, mais ils détiennent maintenant une exposition à des treasuries tokenisés. La boîte noire a changé de contenu, l'étiquette est restée la même, et très peu de gens ont compris ce qui s'était passé.

Pour moi, c'est l'exemple parfait du risque de contrepartie, qui est par nature double :

1. Le risque que la plupart des gens comprennent : vous acceptez que cette contrepartie puisse faire défaut, échouer, etc.
2. La conséquence plus subtile du premier : quand la contrepartie que vous acceptez est offchain, c'est une boîte noire. Elle peut changer. Vous ne faites pas seulement confiance à la contrepartie d'aujourd'hui. Vous faites confiance à toutes les décisions futures que les opérateurs pourraient prendre : vous signez un chèque en blanc sur votre exposition au risque.

Le risque de contrepartie devient pratiquement infini dès que vous l'acceptez.

---

## Un problème de design, pas un problème de personnes

Je ne suis pas ici pour attaquer Rune ou l'équipe Ethena. Les deux ont réussi à faire croître les plus grandes alternatives à USDC et USDT, ce qui mérite le respect. Ils ont pris des décisions rationnelles dans les contraintes auxquelles ils faisaient face. Quand les rendements se compriment, vous cherchez de nouveaux rendements. Quand la gouvernance veut de la croissance, vous lui donnez de la croissance.

Le problème central est l'architecture. Quand le rendement dépend de sources externes, vous louez votre modèle. Dès que ces sources changent, que le basis se compresse, que la réglementation RWA se durcit ou qu'une contrepartie échoue, votre stablecoin change avec elles. Vous ne contrôlez pas vos propres fondations.

La "gouvernance décentralisée" semble résiliente jusqu'au moment où l'on réalise que c'est le mécanisme par lequel les protocoles abandonnent leurs contraintes initiales. La DAO vote le compromis, et le compromis devient permanent.

Ce ne sont pas des histoires isolées, c'est la norme. Les projets commencent décentralisés, puis scalent vers la dépendance. Le résultat est prévisible, mais les utilisateurs finaux se retrouvent avec autre chose que ce pour quoi ils avaient signé.

---

## Ce que Polaris est construit pour être

Ce n'est pas une annonce produit ; le protocole n'est pas encore live. Ce que je veux partager aujourd'hui, c'est un ensemble d'engagements : des décisions architecturales porteuses et non négociables, pour que vous sachiez à quoi vous attendre avec Polaris.

**Sans contrepartie par architecture, pas par promesse.**

Polaris génère du rendement depuis la volatilité grâce à un mécanisme de bonding curve. Pas de RWA. Pas d'exposition CEX. Pas de pipelines de rendement externes qui peuvent se comprimer, pivoter ou être saisis. Le système crée son propre rendement depuis l'actif sur lequel il est construit. Nous voulons construire un protocole capable de scaler sérieusement ; un rendement auto-référentiel est donc la seule façon d'assurer un potentiel de croissance quel que soit son niveau d'échelle actuel.

**Coeur immuable.**

La logique fondamentale de Polaris ne peut pas être changée. Pas "ne sera pas changée sauf approbation de la gouvernance". Ne peut pas. Les mécaniques centrales sont fixées au déploiement. C'est une contrainte que nous nous imposons à nous-mêmes, et à tous ceux qui viendront après. Quand vous interagissez avec Polaris, vous interagissez demain avec le même système qu'aujourd'hui. La "boîte noire" est ici faite de verre, ce qui vous permet de voir que le coeur ne se dénature jamais.

**Stewardship, pas gouvernance.**

Les détenteurs de POLAR ne gouvernent pas Polaris au sens traditionnel. Ils en assurent le stewardship.

Quelle différence ? La gouvernance implique le pouvoir de tout changer, y compris les choses qui ne devraient pas l'être. Le stewardship désigne quelque chose de plus étroit : la capacité d'ajuster des paramètres dans des fourchettes codées en dur et d'orienter les ressources pour accompagner la croissance du protocole. Les détenteurs de POLAR peuvent aider le protocole à s'adapter aux conditions de marché. Ils ne peuvent pas le dénaturer. Ils ne peuvent pas voter pour ajouter une exposition RWA. Ils ne peuvent pas démonter le coeur immuable. Les limites sont imposées par le code, pas par le consensus social.

C'est une "gouvernance" clairement définie et consciente de ses limites. Elle est si inhabituelle et si éloignée de la "gouvernance" habituelle que nous avons décidé d'expliciter sa nature avec un nouveau nom : "stewardship".

## La forme du système

Je vais rester bref ; les mécaniques détaillées arriveront dans les prochaines semaines. Mais voici la structure :

**Trois tokens :**

- **pUSD** : un stablecoin générateur de rendement adossé à du collatéral pETH
- **pETH** : un dérivé ETH avec un prix plancher croissant, créé via la bonding curve
- **POLAR** : le token de stewardship, qui capture le rendement réel de l'activité du protocole

**Trois moteurs :**

- Une bonding curve qui convertit les dépôts d'ETH en pETH, capturant la volatilité comme rendement
- Une architecture CDP optimisée pour la stabilité et la croissance, permettant d'emprunter du pUSD contre du pETH
- Un mécanisme de conversion où POLAR est minté exclusivement par burn de pETH, ce qui relève le plancher de collatéral

Les moteurs se renforcent mutuellement. À mesure que le système grandit, la collatéralisation se renforce. Le rendement scale avec l'adoption au lieu de se diluer. Le flywheel est conçu pour accélérer, pas pour plafonner.

Plus de détails bientôt. Pour l'instant, retenez que l'architecture sert la philosophie, et non l'inverse.

---

## L'appel

Polaris n'est pas live. Vous êtes tôt. Pour l'instant, le meilleur endroit pour découvrir [Polaris est le site](https://polarisfinance.io), et les plus motivés peuvent déjà rejoindre [notre canal d'annonces Telegram](https://t.me/polaris_ann).

J'ai passé des années à écrire sur la DeFi, analyser des protocoles, observer les compromis s'accumuler et les promesses s'évaporer. Si vous avez vu les stablecoins abandonner leurs fondations et senti que quelque chose n'allait pas, vous comprenez pourquoi nous sommes là. Si vous pensez que la décentralisation est une propriété d'architecture, pas de marketing, vous comprenez ce que nous construisons.

Je ne cherche pas encore des utilisateurs. Je cherche des gens qui comprennent.

Polaris n'est pas simplement un autre protocole DeFi : **c'est la réponse immunitaire éruptive de la DeFi au virus USDC/T**. Nous avons passé trop de temps dans les tranchées pour accepter de voir l'espace auquel nous avons dédié nos vies finir capturé, domestiqué et neutralisé comme Internet l'a été. Pour d'autres équipes, ce n'est qu'un travail, une occupation ; une source de rendement parmi d'autres. **Pour nous, c'est le Final Boss :** si nous échouons ici, nous n'aurons été qu'un autre groupe de pions servant un agenda global qui vassalise davantage les populations du monde : notre arc principal vaincu, effacé, neutralisé. **Nous voulons voir une DeFi trustless nous survivre, et être utilisée par nos petits-enfants.**

Les services financiers incensurables, comme la vie privée, sont des armes nécessaires dans les guerres à venir contre les méga-corps et les gouvernements, et nous ne pouvons pas laisser nos soldats sans équipement. Nous n'avons pas l'intention d'être des pions, mais plutôt de concevoir le plateau sur lequel la résistance se bat. À quel point sommes-nous sérieux ? **Sérieux niveau McAfee : nous amenons ce stable à une supply à dix chiffres en deux ans. Contrairement à lui, grâce à notre code immuable, nous n'aurons pas besoin de prendre la fuite ;** mais nous sommes prêts à le faire si cela augmente les chances de succès. "Locked in" décrit mal à quel point nous sommes nés et devenus prêts pour cela.

Je ne suis pas seul dans cette aventure ; je ne suis qu'un membre d'une équipe d'élite, menée par un homme avec qui j'ai travaillé pendant plus de deux ans au [DeFi Collective](https://deficollective.org). Je l'ai vu grandir et s'épanouir dans la DeFi, sans jamais trahir ses principes : il est plus que prêt pour son arc de personnage principal, et vous le verrez beaucoup plus dans les semaines et mois qui viennent : [Robert/0xLuude](https://x.com/0xluude).

**Explorez la vision :** [polarisfinance.io](https://polarisfinance.io/)

**Restez informés :** [suivez Polaris sur Twitter](https://x.com/polarisfinance_)

J'ai à peine effleuré Polaris ici, donc si vous aimez la direction, consultez le site et rejoignez le Telegram pour approfondir.

D'ici là, souvenez-vous que les promesses se transforment vite en compromis si elles ne sont pas imposées par du code immuable.

- TokenBrice, qui entre enfin dans son arc de fondateur, prêt à libérer une demi-décennie d'autisme stablecoin.

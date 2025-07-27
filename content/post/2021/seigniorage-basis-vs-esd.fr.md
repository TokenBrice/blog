---
title: "⚖ L'histoire de deux modèles de seigneuriage : Basis contre ESD"
description: "Une analyse comparative des deux principaux modèles de tokens de seigneuriage actuellement explorés pour produire de nouveaux types de stablecoins sur le réseau Ethereum"
date: '2021-01-16T01:13:50.191Z'
categories: [🌌 DeFi, ⚙ Comprendre]
tags: [DeFi, Ethereum, Stablecoins, Seigniorage, Basis Cash, Empty Set Dollar, Dynamic Set Dollar, USDT, USDC, ESD, DSD, BAC, BAS, MithCash, MIC, MIS, DAIQ, ZAI]
toc: true
tocNum: false
url: seigneuriage-basis-vs-esd
image: /img/2021/seigniorage-basis-vs-esd/cover.png

---

Il y a quelques semaines, j'ai partagé mon premier billet sur les stablecoins algorithmiques en soulignant les principales caractéristiques qui rendaient de tels projets intéressants à mes yeux. Dans cet article, nous allons approfondir le sujet, avec une **analyse comparative des deux principaux modèles** : le modèle Basis et le modèle ESD. 

Tous deux sont utilisés avec succès par le projet qui portent leur nom mais aussi par de nombreux forks, plus ou moins pertinents. Alors que le domaine des stablecoins algorithmiques se structure, il semble y avoir un **consensus autour de ces deux approches, désormais utilisés comme modèle** pour lancer rapidement de nouveaux projets essayant diverses modifications, comme l'ancrage du système à une autre monnaie que le dollar, telle que l'or ou l'euro.

La pléthore de forks existants autorise aux plus récents de s'inspirer des améliorations existantes ou à venir des systèmes en service, ce qui permet de faire un bond en avant dans l'innovation. Mais avant de plonger dans les arcanes du dernier token élastique en or, il est bon de s'assurer que vous comprenez les modèles sous-jacents. C'est la raison pour laquelle nous sommes ici aujourd'hui.

## 1. De vastes bases pour les monnaies élastiques

Pour dire les choses simplement, les deux modèles s'appuient sur le modèle Ampleforth précédent qui a été le premier à proposer des "monnaies élastiques" dont le total circulant réagit aux conditions du marché. Le principal problème avec Ampleforth est que tout le monde est exposé aux rebases, ce qui entrave l'utilisation de l'AMPL comme moyen d'échange.

Les deux nouvelles versions abordent donc ce problème sous un angle différent :

* Avec le modèle de seigneuriage, **le mécanisme de rebase est séparé sur un token différent**, la part - ouvrant la voie à un stablecoin plus utilisable.
* Dans le modèle ESD, il n'y a toujours qu'un seul token mais le verrouillage DAO et LP aboutissent à un résultat similaire.

Les deux modèles introduisent également le mécanisme des obligations/coupons pour **ajouter une incitation positive lorsque le prix est inférieur à l'ancrage**, ce qui contribue à stabiliser davantage le stablecoin.

Ainsi, aujourd'hui, après avoir rappelé les bases, nous allons comparer le modèle Basis (forké par MithCash, OneCoin, et plus) au modèle ESD (utilisé dans DSD, ZAI, DAIQ, etc.).

Je ne vais pas expliquer les modèles en détail mais ce tableau récapitule les principales différences :

| / | MODÈLE BASIS | MODÈLE ESD |
| :------------------------------------: | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **TOKENS** | BAC = stablecoin <br> BAS = une part du protocole <br>BAB = 1  BAC réclamable pendant les phases d'expansion | ESD = stablecoin <br> ESDS = 1  ESD réclamable pendant les phases d'expansion |
| **LIQUIDITÉ** | Paire BAC/DAI : incitations BAS continues (1an) <br>Pas de vérouillage | Incitations ESD/USDC seulement si ESD>1 <br> blocage de 5 epochs|
| **MECANISME RETOUR AU PEG (<1)** | Obligations (BAB) : BAB = BAC(twap)^2 <br> Pas de date d'expiration | Coupons (ESDS) La tarification basée sur un premium, expire après 90 epochs (30 jours) |
| **LORS DE L'EXPANSION (>1), QUI L'OBTIENT?** | Boardroom BAS (stake) + Trésorerie | Répartition dynamique entre LP et DAO en fonction de la dette protocolaire |
| **AUTRES MÉCANISMES IMPORTANTS** | Paire Uni BAS/DAI avec les incitations BAS <br>BAS/DAI & BAC/DAI farmable par les vaults - Harvest, Pickle, etc. | DAO auto compound mais avec un long lockup<br>Lockups -> intégrations limitées par tiers |

---

## 2. ⛽ Vue d'ensemble : l'efficacité en gaz

Avant d'entrer dans les détails de chaque élément, voici un autre point clé des systèmes à prendre en compte si vous voulez y participer : quel coûts en gaz pour l'utilisateur ?

Vous trouverez ici quelques indications sur le nombre et les flux de transactions nécessaires pour participer aux différentes parties du système que nous avons décrit, vous aidant à évaluer si cela a un sens pour vous, en ce qui concerne le gaz.

Dans l'ensemble, les **positions fournissant des liquidités sont celles qui nécessitent le plus de transactions**, en particulier dans le modèle ESD où vous devez lier et délier vos tokens LP et réclamer des récompenses.

*Je garde la terminonolgie en anglais car c'est une boucherie incompréhensible en français. Referrez-vous à la note en bas de page si un terme vous manque.* [^1]

#### 2.1. LP - Basis Cash ⭐⭐⭐

* Entrée : Stake token LP
* Récompense : Réclamation (continu)
* Sortie : Unstake le token LP

#### 2.2. LP - ESD ⭐

* Entrée : Stage -> Bound
* Réclamation de récompense : Unstage-> Stage> (attendre 5 epochs) -> Claim
* Sortie : Unstage -> (attendre 5 epochs) -> Unbound

En ce qui concerne la Boardroom et la DAO, **le flux est moins lourd en termes de transactions**, donc plus avantageux pour les petits détenteurs :

#### 2.3. Boardroom - Basis Cash ⭐⭐⭐

* Entrée : Stake BAS
* Récompense : Claim (après la fin d'une epoch >1,05)
* Sortie : Unstake BAS

Remarque : pendant les phases d'expansion, vous pouvez laisser les BAC s'accumuler dans la boardroom et réclamer plusieurs jours de récompense en même temps.

#### 2.4. ESD - DAO ⭐⭐⭐⭐

* Entrée : Stage ESD -> Bound ESD 
* Récompense : aucune transaction requise
* Sortie : Unstage ESD -> (attendre 15 epochs) -> Unbond ESD 

Note : Pendant les phases d'expansion, les récompenses produites par le DAO sont automatiquement composées (= bounded) sans qu'une action soit requise de la part de l'utilisateur final.

---
## 3. Analyse algorithmique comparative des stablecoins : Basis vs ESD

Vous trouverez l'essentiel de mon analyse dans le tableau suivant. Si vous connaissez bien les deux projets, cela devrait suffire, sinon vous pouvez lire les explications pour chaque avantage et inconvénient sous le tableau.

|                 |                           Modèle Basis                            |                          Modèle ESD                             |
| :-------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| **👍Avantages** | Pool stablecoin plus liquides <br> La part est "fluide" <br>Meilleur système de coupons <br>Fermes (intégrations de tiers) | Détenteurs plus engagés <br>Cycles plus rapides : peuvent s'adapter de manière plus dynamique aux marchés |
| **👎Inconvénients** | Utilité limité de BAS quand BAC<1 <br> Prix de BAS 100%  corrélé à BAC | Système moins accessible <br> Système de coupon plus risqué (expiration) <br> Lots massifs de nouveaux ESD |

---

{{< notice warning >}}
**Attention  : Il ne s'agit pas de conseil en investissement.**  Je ne suis pas qualifié pour en fournir. Il s'agit d'une simple analyse technique de deux systèmes de seigneuriage mis en œuvre sur le réseau Ethereum : le compte-rendu d'un agriculteur 🚜
{{< /notice >}}

Maintenant que nous sommes à l'aise avec les bases de chaque modèle et de leur efficacité en matière de gaz, détaillons les avantages et les inconvénients de chacun :

---

### 3.1. 👍 Avantages du modèle Basis

#### 3.1.1. Des pools plus liquides

Dans le modèle de Basis, les apporteurs de liquidité sur **BAC/DAI sont continuellement récompensés par des tokens BAS**. Comme la récompense BAS se poursuit même lorsque BAC est en phase de contraction, nous n'observons pas la même réduction composée de la liquidité que celle observée dans le modèle ESD : lorsque le prix de l'ESD est en baisse et que les fournisseurs de liquidité se retirent en même temps.

![liquidity-esd-bac-tokenbrice](/img/2021/seigniorage-basis-vs-esd/liquidity-esd-bac.png "La liquidité totale disponible sur les paires ESD/USDC et BAC/DAI depuis le début.")

Nous pouvons voir que la liquidité de **ESD est assez peu stable** alors que celle de BAC est principalement corrélée au prix de BAC (attendu).

#### 3.1.2. Part fluide

La part est fluide en ce sens qu'il n'y a actuellement aucun engagement requis pour être éligible au BAC de la Boardroom. Bien que cela puisse également rendre le prix du BAS plus difficile à stabiliser, cela rend la composante de récompense de l'expansion du système plus largement accessible et moins manipulable.

#### 3.1.3. De meilleurs coupons

**Les coupons de Basis (BAB - Bounds) n'ont pas de date d'expiration**. Ils peuvent être échangés contre 1 BAC tant que le BAC est > 1,05. Cela rend l'achat de coupons moins risqué que dans le cadre de l'ESD où ils expirent.

#### 3.1.4. Intégrable par un tiers

Les récompenses du modèle de base sont distribuées par le biais d'un **contrat de staking standard**, permettant et facilitant l'intégration par des tiers. Il existe déjà des vaults Harvest & Pickle pour simplifier l'exploitation des pools BAC/DAI, BAS/DAI, MIC/USDT et MIS/USDT.

![harvest-basis-cash-mith-cash](/img/2021/seigniorage-basis-vs-esd/harvest.png "BasisCash & MithCash vaults sur Harvest Finance")

### 3.2. 👎 Les inconvénients du modèle Basis

#### 3.2.1. La part a une faible utilité lorsque BAC&lt;1

La principale faiblesse, et de loin la plus importante à ce jour, de la mise en œuvre actuelle du modèle Basis est la **faible utilité de la part**. Dans les phases d'expansion, son prix s'apprécie généralement en raison du BAC nouvellement frappé auquel il donne accès. 

Cependant, l'utilité du BAS est faible dans les phases de contraction, à l'exception de son pouvoir de gouvernance. En phase de contraction, la seule option de gain potentiel est de s'engager dans le pool BAS/DAI pour des BAS supplémentaires, mais c'est un jeu très risqué avec une action de prix BAS baissière (contraction).

Plusieurs projets travaillent déjà sur des solutions pour y remédier.

#### 3.2.2. Le prix de l'action est corrélé à 100 % au prix du stablecoin

Le deuxième inconvénient est une conséquence directe du premier. En raison du manque d'utilité du BAS en dehors du BAC en expansion, **son prix est directement corrélé au prix du BAC**. Une utilité supplémentaire sur le BAS pourrait permettre aux deux tokens d'avoir des cycles plus indépendants, apportant plus de stabilité au modèle dans son ensemble.

---

### 3.3. 👍 Avantages du modèle d'ESD

#### 3.3.1. Des détenteurs plus engagés

Dans le modèle d'ESD, il n'y a **pas d'accès à l'ESD nouvellement créée sans s'engager pour plusieurs epochs**, au moins 5 avec le LP. Cela rend les grands détenteurs plus susceptibles d'être activement impliqués dans le processus de frappe et de stabilisation.

#### 3.3.2. S'adapter de manière plus dynamique aux conditions du marché

Dans l'ensemble, le système d'ESD fonctionne sur une **période trois fois plus courte que Basis**, ce qui permet des ajustements plus fluides et dynamiques. Le DSD va encore plus loin avec une epoch de 2 heures (= 12x le rythme de Basis).

### 3.4. 👎 Les inconvénients du modèle ESD

#### 3.4.1. Complexité globale du système

En raison des vérouillages, stage, boundi et autres limites supplémentaires nécessaires pour mettre en œuvre la fonctionnalité de partage directement au niveau des stablecoins, les systèmes basés sur l'ESD ont tendance à être plus **complexes à appréhender**, en particulier pour les nouveaux arrivants. 

On peut même le constater dans les mèmes, où les joueurs ESD/DSD aiment se mimer avec un haut coefficient intellectuel. L'expiration des coupons rend le système de stabilisation extrêmement peu convivial pour les nouveaux arrivants, ce qui n'est pas nécessairement une mauvaise chose en soi, mais voyez le point suivant.

#### 3.4.2. Incitation plus faible des coupons	

Les coupons ESD ont une date d'expiration, ce qui transforme le système des coupons en un peu de roulette russe. En raison de cette conception, il existe de sérieux risques de perdre tout le capital engagé en brûlant l'ESD pour les coupons, même si le système ESD se maintient à long terme. En effet, une fois que l'ESD est transformée en coupon, le propriétaire dispose de **90 epochs (~30 jours) pour les réclamer avant leur expiration.**

#### 3.4.3. Lots d'ESD nouvellement frappés

Enfin, la logique d'émission des systèmes basés sur l'ESD, associée aux vérouillages tend à produire des **"raindrop epochs "** où la plus grande partie de l'ESD nouvellement frappée est déverrouillée, ce qui peut déclencher une violente action sur le prix du stablecoin.

Lors de la dernière phase d'expansion, la période autour de l'epoch 396 était célèbre et effrayante parce que la plupart des DSD nouvellement frappés y sont devenus transférables :

![DSD-epoch-396-397-tokenbrice](/img/2021/seigniorage-basis-vs-esd/dsd-raindrop.png "Après la dernière phase d'expansion, plus de 30M de DSD ont été libérés en seulement deux epochs (396 et 397), un moment redouté pour les détenteurs de DSD et de coupons").

*Oui, il s'agit de DSD, mais des tendances similaires sont observées sur l'ESD. C'est dû au vérouillage dans la DAO et au calendrier d'émission.*

---

## 4. La boîte à outils Algostable

Avant de vous laisser partir, voici un rapide aperçu des principaux outils utiles au suivi et à la gestion des positions pour les quatre projets. Nous avons de la chance ! Il existe des outils communautaires supers conçus pour vous aider à suivre les stablecoins algorithmiques. 

{{< notice tip >}}
**[Vfat en particulier](https://vfat.tools/)** a été très réactif en mettant à jour ses outils de suivi et de gestion pour les projets les plus récents. Il inclut même un **[aperçu des tokens de seigneuriage](https://vfat.tools/seigniorage/)** maintenant :

![vfat-seigniorage-overview](/img/2021/seigniorage-basis-vs-esd/vfat.png "Aperçu des principaux tokens de seigneuriage sur Vfat")
{{< /notice >}}

* Pour l'ESD, votre tableau de bord principal est [ESDTools](https://esd.tools/)
* Pour DSD, [DSDTools](https://dsd.tools/).
* Pour Basis Cash, **[BCTools](https://bc.tools/)**. 

Vous pouvez utiliser [ce tableau de bord pour suivre la sortie des ESD et DSD nouvellement frappés](https://duneanalytics.com/tongnk/esd_1).

Enfin, les quatre projets sont supportés par [Zapper](https://zapper.fi/) et [DeBank](https://debank.com/) pour suivre vos investissements. Vous pouvez également utiliser [Pickle](https://pickle.finance/) ou [Harvest](https://harvest.finance/) pour gérer votre position dans les pools BAC/DAI, BAS/DAI, MIC/USDT et MIS/USDT.

### 4.1. Ressources supplémentaires

- Pour en savoir plus sur le contexte des stablecoins algorithmiques, n'hésitez pas à **[lire mon précédent article sur le sujet](https://tokenbrice.xyz/content/posts/2020/algorithmic-stablecoins.fr.md)**. 
- Pour en savoir plus, les francophones apprécieront cette **[🇫🇷 vidéo de 50 min expliquant les deux modèles](https://www.youtube.com/watch?v=TuenkIZZEq0)** 
- Si vous lisez l'Anglais, cet article publié sur Derebit vaut la lecture : **[Stabilité, élasticité et réflexivité : A Deep Dive into Algorithmic Stablecoins](https://insights.deribit.com/market-research/stability-elasticity-and-reflexivity-a-deep-dive-into-algorithmic-stablecoins/)**.

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/c/DeFiFrance)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}

---

[^1]: Stage/Unstage est la première étape d'engagement avec le mecanisme, une forme de SAS. Un fois staged, vous pouvez "bound" pour etre éligible aux récompenses s'il y en an. Il vous faudra parfois "claim" c'est à dire signer une transaction pour récupérer les tokens gagnés. 
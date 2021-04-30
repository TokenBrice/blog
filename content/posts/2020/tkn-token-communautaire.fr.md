---
title: "TKN, le token commununautaire" 
description: "Une introduction à TKN, le token communautaire de Monolith - portefeuille Ethereum avec une carte Visa : coffre communautaire, TKN burn et contrats."
date: '2020-07-05T10:13:50.191Z'
categories: [👾 Monolith]
tags: [DeFi, Ethereum, Monolith, TKN]
---

![Monolith TKN - Le token communautaire](/img/2020/tkn-token-communautaire/cover.jpeg)

TKN est un élément central de l'offre Monolith. Dans ce billet, je vais aborder les bases de sa tokenomique en deux sections :

1. 🏦 Le "Coffre Communautaire"
2. 🔥 TKN Burn

Avant de vous lancer dans les complexités de TKN, je vous recommande de lire rapidement [l'article de prise en main de Monolith]({{< relref "monolith-prise-en-main.fr.md" >}}). Bien que je décris brièvement le mécanisme de top-up ci-dessous, vous trouverez dans cet article un aperçu complet de Monolith et vous pourrez ainsi anticiper bon nombre de vos questions d'utilisation.

_ℹ Traduction personnelle d'une [production originale Monolith](https://medium.com/monolith/tkn-101-the-community-token-8ba00a13fbc7)._

---

### 🏦 Le Coffre Communautaire de TKN

Le coffre communautaire est un contrat intelligent vers lequel une commission de 1% est versée lorsqu'un utilisateur recharge sa carte Monolith avec un autre token que le TKN.

Voici un exemple de ce qui se passe sous le capot lorsqu'un utilisateur sélectionne 1 ETH à convertir en Euros pour charger sa carte :

1. 💳 1.00 ETH est vendu au taux du marché pour créditer le compte de la carte de crédit de l'utilisateur.

1. 🗝 Le **1% de contribution communautaire** (0,01 ETH) facturé **est envoyé directement vers notre Community Chest**. La contribution communautaire est levée lorsque l'utilisateur recharge son compte à l'aide du token TKN.

1. 🔮 Une **redevance (0,0101 ETH) de 1%** est payée à Monolith. La redevance est levée sur les tokens stables (tels que DAI, USDC, ou USDT).

[Vous pouvez consulter tous les tarifs ici](https://monolith.xyz/pricing/).

![Recharge (top-up) de la carte Monolith](/img/2020/tkn-token-communautaire/1-top-up.png)

---

### 🔥 Le mécanisme de burn

Les détenteurs de **TKN peuvent le brûler (burn)** en échange d'une quantité proportionnelle de tokens stockés dans le contrat coffre commununautaire.

Le fait de brûler détruit les TKN, ce qui réduit le total circulant, augmentant ainsi proportionnellement la part disponible pour les prochains burns.

#### ♨️ TKN Exemple de burn

Illustrons le mécanisme qui se cache derrière cela en utilisant une situation hypothétique et simplifiée basée sur trois hypothèses :

1. Il y a un total de 10000 TKN en circulation
2. Le coffre communautaire de TKN contient 100 ETH et 1000 DAI
3. Un utilisateur possédant 500 TKN décide de les brûler

Tout d'abord, nous devons calculer le pourcentage de l'offre totale de TKN que possède l'utilisateur qui brûle ses tokens - son pourcentage proportionnel de ce qui est stocké dans le coffre communautaire TKN :

`Part (du coffre) = quantité de TKN brûlés / total TKN circulant`
*⇒ 500 / 10000 = 5%*

En brûlant 500 TKN, notre utilisateur hypothétique réclamera 5 % des biens contenus dans le coffre communautaire de TKN, ce qui correspond à

⇒ `5 % de 100 ETH & 5 % de 1000 DAI`
→ 5 ETH **+** 50 DAI

![Un exemple hypothétique de TKN Burn](/img/2020/tkn-token-communautaire/2-tkn-burn.png)

Un burn de 500 TKN suivant la première rapportera un pourcentage proportionnel plus élevé puisque l'offre totale est maintenant réduite à 9500 :
⇒ 500 / 9500 = 5.263%

#### 📜 Le contrat du Coffre Communautaire

Le Coffre Communautaire (Asset Contract) [est maintenant en ligne](https://etherscan.io/address/asset-contract.tokencard.eth), ce qui signifie que les contributions envoyées par les utilisateurs avec les dernières versions du portefeuille de contrats (v2.2.0 et plus) sont maintenant automatiquement collectées.

Qu'est-ce qui rend le Community Chest si spécial ? **C'est un système de contrat intelligent, il fonctionne de manière ouverte et transparente.**

Vous n'avez pas besoin d'utiliser l'application Monolith pour brûler votre TKN. Vous pouvez simplement appeler la fonction en utilisant le service de votre choix.

Nous sommes actuellement en train de [migrer](https://medium.com/monolith/your-monolith-account-is-due-for-an-upgrade-35b1814a01ed) les utilisateurs qui ont déployé leur Contract Wallet avant que la nouvelle version ne soit opérationnelle (v1.x -> v3.2.0), afin qu'ils puissent contribuer à la Community Chest. Nous allons ensuite ajouter au Community Chest avec les contributions collectées avant sa mise en ligne.

#### 📘 Comment brûler vos TKN

Rendez-vous sur la page [TKN Token Contract - Write Page](https://etherscan.io/address/0xaaaf91d9b90df800df4f55c205fd6989c977e73a#writeContract). Là, vous pouvez appeler la 9ème fonction, _burn_.

![brûler les jetons TKN](/img/2020/tkn-token-communautaire/3-burning-tkn.png)

Il suffit d'un paramètre :

quantité (uint256)_ : la quantité de TKN à brûler. L'entrée sur Etherscan est en Wei, il peut donc s'avérer plus facile d'utiliser un outil comme [Ethereum Unit Converter](https://www.etherchain.org/tools/unitConverter) pour convertir en une unité que vous connaissez bien comme Ether/TKN.

Pour brûler votre TKN contenu dans votre portefeuille Monolith, vous devrez [l'importer dans Metamask]({{< relref "monolith-metamask-etherscan.fr.md" >}}).

---

Nous espérons que cela a permis d'aborder notre tokénomique, mais si vous avez d'autres questions, nous vous invitons à vous joindre à la discussion sur notre [Discord](https://discord.gg/YrrFpFd) ou [sur notre Télégram francophone](https://t.me/Monolith_fr).

Et n'oubliez pas : vous pouvez essayer Monolith dès aujourd'hui - [💳  commandez votre carte](https://monolith.xyz).

---

_Cet article ne constitue ni une offre de vente, ni une sollicitation d'une offre d'achat, ni une recommandation d'une quelconque cryptodevise, jeton (token), investissement, sécurité ou tout autre produit ou service._

_En outre, rien dans cet effet n'est destiné à fournir des conseils juridiques ou d'investissement et rien dans cet article ne doit être interprété comme une recommandation d'acheter, de vendre ou de détenir une quelconque cryptocarte, un quelconque jeton (token), un quelconque investissement ou une quelconque sécurité, ou de s'engager dans une quelconque stratégie d'investissement ou transaction financière._
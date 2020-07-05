---
title: "Interagir avec votre wallet Monolith via MetaMask et EtherScan" 
description: "Un tutoriel pour apprendre à utiliser son portefeuille Monolith avec MetaMask et EtherScan, utile pour interagir avec des tokens non supportés, ou en tant que processus de secours."
date: '2020-07-05T10:13:50.191Z'
categories: [🌌 DeFi, 👾 Monolith]
tags: [DeFi, Ethereum, Monolith]
---

![infrastructure du portefeuille Monolith](/img/2020/monolith-metamask-etherscan/cover.jpeg)

Chez Monolith, nous travaillons sans relâche pour offrir une expérience digne d'Ethereum. Nos cartes en sont un élément clé, mais le **contract wallet** est tout aussi important. Il permet à nos utilisateurs de notariser leur relation avec leurs actifs sur le réseau Ethereum.

Cet article vous présente comment utiliser votre portefeuille Monolith avec EtherScan et MetaMask afin d'interagir avec vos fonds en toute autonomie.

_ℹ Traduction personnelle d'une [production originale Monolith](https://medium.com/monolith/importing-using-your-monolith-wallet-with-metamask-and-etherscan-a22862283929)._

### Ce dont vous aurez besoin :

1. Sur votre téléphone : [l'application Monolith](https://monolith.app.link/rUNR0lu2Q1)
2. Sur votre ordinateur : [Chrome](https://www.google.com/chrome/), [Chromium](https://www.chromium.org/), ou [Brave](https://brave.com) + [MetaMask](https://metamask.io/)

### Importation de votre portefeuille Monolith dans MetaMask

#### 1/ Trouver sa seed phrase

Vous pouvez trouver votre seed phrase dans les paramètres de sécurité dans l'onglet Wallet. Vous en aurez besoin pour importer votre portefeuille Monolith dans MetaMask.

#### 2/ Installer MetaMask

Vous devez installer l'extension du navigateur [Metamask](http://metamask.io) sur votre ordinateur.

ATTENTION : _MetaMask ne vous permet **pas** d'importer une seed phrase si vous avez un portefeuille existant. Si vous souhaitez conserver votre configuration actuelle, vous pouvez utiliser un second navigateur, compatible avec MetaMask ([Chrome](https://www.google.com/chrome/), [Chromium](https://www.chromium.org/), [Brave](https://brave.com) )_

#### 3/ Importer votre seed dans MetaMask

Le processus est simple - il suffit de se référer au GIF ci-dessous :

#### 🚨 À noter 🚨

Il est beaucoup plus sûr d'utiliser un stylo et du papier que de stocker votre seed phrase numériquement ! Ce que vous avez vu sur ce gif est une boucherie en terme de sécurité qu'on ne se permet que sur wallet démo avec $3. Pour plus, mieux vaut prendre le temps.

![Importation d'une phrase d'amorce de Monolith Wallet dans une nouvelle installation de MetaMask](/img/2020/monolith-metamask-etherscan/1-import.gif)

Lorsque vous importez votre portefeuille dans MetaMask, **vous verrez un solde ETH qui diffère du solde affiché dans l'application Monolith - c'est normal.**

Le solde que vous voyez dans MetaMask est le solde de "l'adresse du propriétaire" (owner address), appelé "gas tank" dans l'application Monolith.

![Les interactions entre votre owner/gas tank et votre portefeuille de contrat de Monolith en utilisant MetaMask et EtherScan](/img/2020/monolith-metamask-etherscan/2-owner-address.png)

Après avoir pris le contrôle total de votre portefeuille, nous pouvons maintenant procéder :

### Interagir avec votre portefeuille de contrats

#### 4/ Trouver l'adresse de votre wallet Monolith

Vous trouverez l'adresse de votre portefeuille de contrats dans l'application Monolith en cliquant sur le bouton d'action (+) et ensuite sur "Recevoir".

Pour trouver l'adresse du propriétaire, vous devez vous référer au Monolithe. Une fois dans l'application, vous devez ouvrir l'onglet "⚙ Settings", et vous référer à l'adresse après "PK" en bas de la page - il suffit de la toucher pour la copier.

Nous avons surligné l'adresse en rouge ci-dessous :

![Trouver l'adresse de votre propriétaire à partir de l'application mobile Monolith](/img/2020/monolith-metamask-etherscan/3-trouver-son-owner.jpeg)

#### 5/ Authentification sur EtherScan

💡 **_Avant de poursuivre, assurez-vous que vous êtes connecté à MetaMask et que vous avez importé votre owner address Monolith (-> étape 3)._**

Pour interagir avec votre portefeuille de contrats sur Etherscan, visitez l'onglet "Contrat".

Bien que l'onglet "Read" donne des informations sur le portefeuille, pour cet exercice, nous nous concentrerons sur l'onglet "Write" utilisé pour lancer les opérations.

Vous pouvez vous connecter en haut de l'onglet "Write" comme indiqué ci-dessous :

![Connexion à votre portefeuille Monolith avec MetaMask et EtherScan](/img/2020/monolith-metamask-etherscan/4-authentication.gif)

#### 6/ Signer d'une transaction

Maintenant que vous avez la possibilité de signer des transactions, nous allons utiliser la méthode _bulkTransfer_ pour vous montrer comment envoyer un jeton ERC-20 non pris en charge dans l'application à partir de votre adresse Monolith.

Pour ce faire, nous aurons besoin de deux choses :

1. **une adresse de destination**

1. **Une liste de tokens**, formatée comme suit : [adresse-contrat du jeton1, adresse-contrat du jeton2, etc.]

**En utilisant ce processus, le solde total de chaque jeton énuméré sera transféré - Vérifiez donc tout avant de signer une transaction _bulkTransfer_.**

L'exemple (ci-dessous), montre comment récupérer la totalité des jetons NEC stockés dans un wallet.

![Utiliser la fonction *bulkTransfer* du Monolith Contract Wallet pour récupérer un jeton ERC-20 qui n'est pas encore pris en charge dans l'application à partir de votre Monolith wallet](/img/2020/monolith-metamask-etherscan/5-transaction.gif)

### Besoin d'aide ?

Pas de panique, notre communauté sera ravie de vous aider, directement en français sur [Telegram](https://t.me/Monolith_fr), ou bien sur [Discord](https://discord.gg/6UsVxu) et [Twitter](http://twitter.com/Monolith_web3).
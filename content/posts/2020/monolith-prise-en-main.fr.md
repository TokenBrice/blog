---
title: "Vivre sans banque en 7 étapes : prise en main de Monolith" 
description: "À la découverte du portefeuille Ethereum Monolith qui propose une carte de crédit Visa tout en vous permettant de conserver un contrôle total sur vos actifs."
date: '2020-07-05T10:13:50.191Z'
categories: [🌌 DeFi, 👾 Monolith]
tags: [DeFi, Ethereum, Monolith]
---

![cover](/img/2020/monolith-prise-en-main/cover.jpeg)

Le développement de l'écosystème de la finance décentralisée (DeFi) offre davantage de moyens de dépenser, d'emprunter, de prêter et de déplacer des actifs sans avoir à faire confiance à un tiers.

Il a inauguré une nouvelle ère dans le domaine de la finance, une ère où les gens peuvent revendiquer le contrôle total de leurs actifs - un élément essentiel de l'offre de DeFi.

Comme notre logo l'indique, chez Monolith, nous travaillons à la mise en place d'un portail vous permettant d'interagir de manière transparente avec DeFi, en utilisant :

1. Un portefeuille Ethereum qui servira de passerelle vers cet écosystème financier décentralisé
2. Une carte de crédit Visa (disponible en France) qui, associée à notre portefeuille, vous permet de dépenser vos actifs Ethereum-natifs partout.

Cet article vous guidera dans le processus de création de votre portefeuille Monolith et pour la commande de votre carte.

ℹ _Traduction personnelle d'une [production originale Monolith](https://medium.com/monolith/7-steps-to-living-bankless-e2a536902e91)._

---

### Étape 1 - Installation et prise en main de l'application 📲

**L'essentiel de vos interactions avec Monolith se font [via l'application mobile](https://monolith.app.link/ETH-IS-MONEY).** Vous pourrez commander et gérer votre carte, ainsi que recevoir, échanger et négocier vos données cryptées.

**[🕸 Lien intelligent pour télécharger l'application Monolith 🌌](https://monolith.app.link/ETH-IS-MONEY)**

Lorsque vous ouvrez l'application pour la première fois, il vous sera demandé de la sécuriser à l'aide d'un code PIN à 6 chiffres. Le code PIN est spécifique à votre téléphone - si vous l'oubliez, vous pouvez toujours récupérer votre compte tant que vous avez votre seed phrase (plus d'informations ci-dessous).

![écrans de bienvenue -monolith](/img/2020/monolith-prise-en-main/1-welcome.png)

Votre portefeuille Monolith utilise 2 types d'authentification :

1. **Un code PIN** permettant l'accès au portefeuille, qui peut être changé ultérieurement en Fingerprint/FaceID (dans les paramètres de l'application + activer "Biometrics").
2. **Authentification au niveau de l'appareil** qui vous est demandé pour effectuer des transactions. Il s'agit du code PIN/empreinte digitale /FaceID de votre téléphone

**ℹ "La seed phrase" c'est une liste __ordonnée__ de 12 mots qui est nécessaire et suffisante pour restaurer l'accès à votre compte. Prenez en soin !**

### Étape 2 - Déploiement de votre Contract Wallet 🔐

Une fois que votre application est sécurisée, vous pourrez déployer votre "contract wallet". Le "contract wallet" c'est un smart contract dont vous seul avez le contrôle et où sont sécurisés vos tokens.

![monolith-seed](/img/2020/monolith-prise-en-main/2-backup.png)

Les nouveaux utilisateurs peuvent simplement passer par et appuyer sur "Create New Seed". Les utilisateurs qui ont déjà un portefeuille Monolith peuvent le restaurer en utilisant l'option "Recover Exisiting Seed".

Votre seed phrase est affichée la première fois que vous déployez votre portefeuille. Vous pouvez la consulter plus tard dans l'onglet Wallet > Sécurité. **N'oubliez pas de la sauvegarder pour pouvoir récupérer vos avoirs, même si votre téléphone est perdu.**

#### Votre portefeuille Monolith - Présentation

Le portefeuille de contrats stocke vos fonds tout en vous donnant accès à des options de sécurité pour protéger davantage vos actifs. Son code est open-source et [accessible sur Github](https://github.com/Monolith/contracts).

Monolith vous permet également d'établir une **limite de dépenses quotidiennes** afin de fixer un plafond à la valeur des actifs pouvant être envoyés depuis votre portefeuille. Comme mesure de sécurité supplémentaire, vous pouvez également établir des **adresses de confiance**, qui n'ont pas de plafond et vous permettent de recevoir n'importe quel montant de vos avoirs si votre seed phrase est compromise.

**En un seul clic, vous déployez votre propre instance du [Smart Contract Wallet](https://github.com/tokencard/contracts). Personne d'autre que vous n'y a accès ou n'en a le contrôle.**

![Déploiement du Contract Wallet Monolith](/img/2020/monolith-prise-en-main/3-deploy.gif)

Maintenant que votre portefeuille est déployé et sécurisé, l'étape suivante consiste à commander votre carte de crédit Visa.

Comme la carte permet de vendre des tokens en euros ou en livres sterling, nous sommes confrontés à des exigences réglementaires supplémentaires, ce qui signifie que nous devons confirmer votre identité et votre adresse.

Pour commencer, cliquez sur l'onglet "Carte" ("💳").


### Étape 3 - Vérifier votre identité (KYC) 🛂

Pour commander une carte, nous devons vérifier votre identité. Notre procédure KYC est standard : **vous aurez besoin d'un document officiel (carte d'identité ou passeport) et vous devrez prendre un selfie.**

En fournissant ces informations, nous aurons recours à des tiers pour effectuer des contrôles de votre identité, comme la validation de votre adresse : il s'agit de confirmer que vous êtes bien la personne qui possède les documents soumis.

En plus de valider votre identité, nous effectuons également des contrôles sur vos sources de fonds (AML). En faisant appel à des tiers, nous devons valider que le tokens que vous mettez dans le portefeuille n'est pas issue du blanchiment d'argent. 

### Étape 4 - Vérifiez votre adresse et commandez votre carte Monolith 🛸

Il est possible que, dans le cadre des contrôles, nous ayons besoin d'informations complémentaires pour prouver que vous habitez à l'adresse indiquée. Cela ne devrait pas vous inquitier, notre équipe support / compliance peut vous contacter et vous demander un document de preuve d'adresse.

**Veuillez vous assurer que vous disposez de l'un des documents suivants, sur lequel figurent votre nom et votre adresse (il doit être daté de <= 3 mois)** :

- Facture de services publics : internet, électricité, gaz... La seule que nous ne pouvons pas accepter est une facture de téléphone portable.

- Gouvernement / Fiscalité : votre déclaration d'impôts, ou tout document officiel du gouvernement mentionnant votre nom et votre adresse fera l'affaire.

Lors de la commande de votre carte, vous pouvez décider de la devise de base qu'elle utilisera : GBP (£) ou EUR (€). La devise de base de la carte a une incidence sur [la structure des frais](https://monolith.xyz/pricing/), aussi assurez-vous d'en tenir compte lorsque vous commandez votre carte. Pour un français qui vit et dépense en France, le choix d'une carte € est assez évident.

### Étape 5 - Activation de votre carte 💳

Pour des raisons de sécurité, votre carte est expédiée désactivée. Une fois que vous aurez reçu la carte, vous aurez la possibilité de l'activer dans l'application.

Vous pouvez activer la carte en allant sur l'onglet "Carte" ("💳") et en tapant les 4 derniers chiffres de votre numéro de carte.

### Étape 6 - Votre premier Top-Up

Votre carte activée, vous êtes presque prêt ! Il ne vous reste désormais plus qu'à charger votre carte en vendant des tokens : ça s'appelle "top-up" dans l'application.

#### 1/ Ajout de fonds dans votre portefeuille

Appuyez sur le bouton d'action (➕), puis sur "Receive" pour afficher l'adresse de votre portefeuille et le code QR. Cela vous permettra de recevoir des tokens d'un autre compte.

Le mot **Top-up** réfère à l'action de vendre des tokens pour des € prêts à être dépensés sur votre carte Monolith. 

#### 2/ Remplissage de votre Gas Tank

Une fois que vous avez un peu d'ETH dans votre portefeuille de contrat, vous devrez **remplir votre gas tank** Le "gas" est très important car il vous permet de recharger votre carte et d'envoyer des jetons dans d'autres portefeuilles

Le "Gas Tank", c'est la balance ETH de l’adresse qui contrôle votre contrat, celle dont vous avez la seed phrase, et qui signe toute les transactions.

Vous pouvez donc remplir votre gas tank avec des ETH en appuyant sur votre niveau de gas, surligné en rouge :

![Monolith Gas Tank](/img/2020/monolith-prise-en-main/4-gas.jpeg)

À partir de là, l'application vous guidera tout au long du processus :

![Monolith Recharge Gas](/img/2020/monolith-prise-en-main/5-gas-top-up.gif)

#### 3/ Recharger votre carte Monolith

Avec un peu d'argent dans votre portefeuille et du gaz dans le "tank", vous pouvez maintenant faire le plein : c'est à dire vendre des tokens pour des euros - et vous préparer à utiliser votre carte de crédit Visa.

![Recharge de 10 USDC sur une carte Monolith GBP (des cartes EURO sont également disponibles)](/img/2020/monolith-prise-en-main/6-card-top-up.gif)

_ℹ️ Les transactions de top-up peuvent prendre jusqu'à 90 secondes pour être finalisées._

### Étape 7 - Dépenser avec votre carte Monolith

Votre carte fonctionnera partout où Visa est accepté dans le monde. Votre premier achat doit être effectué avec le code (paiement ou retrait), mais après cela, vous devriez être libre d'utiliser votre carte comme vous le feriez normalement - en magasin, en ligne ("Verified by Visa"), ou bien sans contact.

La carte fonctionne également avec **Google Pay and Curve**.

![l'onglet carte portefeuille Monolith](/img/2020/monolith-prise-en-main/7-card.jpeg)

Vous pouvez consulter tous les détails concernant les limites et les frais dans l'onglet "Pricing" sur [notre site web](https://monolith.xyz/pricing).

Félicitations, vous êtes maintenant prêt à **[télécharger l'application Monolith](monolith.app.link/ETH-IS-MONEY)** et à commencer votre voyage DeFi - et pour vous le rappeler une dernière fois, n'oubliez pas de **SAUVEGARDER VOTRE SEED PHRASE** - vous en aurez besoin.

### Vous avez besoin d'aide ?

Pas de problème - Participez à la discussion de la communauté française sur [Telegram](https://t.me/monolith_fr), [Discord](https://discord.gg/6UsVxu) ou [Twitter](http://twitter.com/Monolith_web3)
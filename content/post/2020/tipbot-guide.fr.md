---
title: "💰 Tip.CC - Guide d'utilisation du service de dons en cryptomonnaie sur Discord"
description: "Un guide pour prendre en main TipBot.CC, le bot Discord crypto qui propose un wallet, des dons, différents jeux et plusieurs outils bien pratiques."
date: '2020-09-14T01:05:50.191Z'
categories: [Tutorial]
tags: [Ethereum, Discord, Dons]
toc: true
tocNum: false
image: /img/2020/tipbot/cover.png
difficulty: "beginner"
---

## A/ Introduction	

Bienvenue dans ce guide d’utilisation en français pour tip.cc. Vous y découvrirez son but, son utilité, et comment s’en servir avec les commandes principales du bot Discord.

Cette traduction est officieuse, et j’espère seulement apporter de la visibilité pour tip.cc à la communauté francophone, en lui donnant l’outil pour apprendre à s’en servir à son plein potentiel.

{{< notice note >}}
Ce guide a été rédigé par **Loico** du [Discord francophone CryptoMatrix](https://discord.gg/mW94vUU). 🙏 Un grand merci à lui !
{{< /notice >}}

### 🧲 Aide Rapide : Que faire d'un tip ?

Vous avez reçu un tip via [tip.cc](https://tip.cc/) et vous ne savez pas quoi en faire ? Lisez ça !

Si vous avez reçu un tip, cela veut dire que **quelqu’un vous a envoyé de la crypto-monnaie via Discord. Voici une aide rapide pour voir et récupérer votre crypto-monnaie**.


1. Entamez une discussion privée avec le bot, en cliquant sur son nom.


![guide-Discord-tipbot](/img/2020/tipbot/image23.jpg "Trouver TipBot")


2. Puis écrivez `$bals` dans le champ prévu pour envoyer un message.


![guide-Discord-tipbot](/img/2020/tipbot/image13.jpg "DM à Tipbot")


3. Une discussion en message privé va s’ouvrir, avec le montant de vos tips reçu.

![guide-Discord-tipbot](/img/2020/tipbot/image9.jpg "Vos balances tipbot")

4. Pour récupérer le tip (dans ce cas d’exemple, des TKN) et l’envoyer sur votre wallet préféré, écrivez `$withdraw TKN`

🚨 **Soyez averti, le withdraw entraîne des frais de réseau.** 

![guide-Discord-tipbot](/img/2020/tipbot/image1.jpg)


5. Renseignez l’adresse de destination de votre portefeuille TKN (par exemple, l’adresse ERC-20 de votre metamask)

![guide-Discord-tipbot](/img/2020/tipbot/image4.jpg "Retrait de TKN")

6. Confirmez, en écrivant `all` ou le montant souhaité. Votre crypto arrivera dans votre wallet 😀

## B/ Présentation de Tip.cc

### Qu’est-ce que Tip.cc ?

Tip.cc est un service de don conçu pour être facilement ajouté sur n'importe quel serveur Discord. Il comprend **un service de tips directement entre utilisateurs**, un portefeuille de crypto-monnaies, et quelques outils de visibilités sur les crypto-monnaies. 

Avec ce bot, vous pouvez envoyer des tokens aux membres de **tous les serveurs Discord sur lequel Tip.cc et vous êtes tous deux présents**. Vous pouvez également en recevoir de manière très rapide et facile, grâce à un portefeuille de crypto-monnaies sans frais et sécurisé. 

{{< notice info >}}
Vos cryptos sur Tip.CC ne sont pas liées au serveur Discord sur lequel vous les avez reçus. Elles sont associées à votre compte Discord lui-même.
{{< /notice >}}

L’utilisation de ce bot présente énormément de surprises ! 

Participer à des airdrops, recevoir une enveloppe rouge, jeter un oeil rapide sur vos crypto-monnaies favorites, demander le prix du gas sur Ethereum... **Vous apprendrez même, en suivant ce guide, à envoyer des crypto-monnaies à plusieurs utilisateurs dans une seule transaction.**

Un autre bon point à mentionner : il n’y a **pas de minimum requis pour les transactions**, et pas de frais sur les transaction. Les seuls frais sont ceux de la blockchain correspondant à la cryptomonnaie utilisée pour un deposit ou un withdraw. Et **si il y a un montant minimum pour un withdraw, c’est celui pour couvrir les frais de la blockchain**.

Ce bot, à l’heure de la publication de ce guide, est maintenu à jour, et supporte de plus en plus de cryptomonnaie différentes. Vous pouvez voir la [📑 liste de toutes les cryptomonnaies supportées ici](https://tip.cc/currencies).

### Tip.cc est lié à votre compte Discord

{{< notice tip >}}
Il est **fortement conseillé d’avoir un 2FA actif sur votre compte Discord**: c’est la sécurité de votre compte Discord qui fait la sécurité de votre portefeuille Tip.cc
{{< /notice >}}

*   Comme dit plus haut, votre portefeuille étant lié à votre compte Discord, vous pouvez utiliser le même portefeuille avec **tous les serveurs Discord ayant activé Tip.cc** (CryptoMatrix, Monolith, Tip.cc…). Mais vous ne pourrez pas l’utiliser en revanche sur les serveurs n’ayant pas Tip.cc.
*   Vous pouvez voir la balance de votre portefeuille **en euro ou en dollars**, selon le paramètre utilisé sur les serveurs Discord que vous utilisez.
*   L’échange de crypto-monnaies entre utilisateur se base actuellement sur le P2P et la confiance. Le développement du bot étant actif, un système plus élaboré pourrait voir le jour prochainement.
*   Vous pouvez **déposer des crypto-monnaies sur votre compte Tip.cc depuis n’importe quel autre portefeuille, tout comme en retirer vers un autre portefeuille**. Ceci engendre des frais liés au frais de la blockchain de la cryptomonnaie visé. Attention à surveiller le prix du gas sur Ethereum par exemple. 

## C/ Utilisation de Tip.cc

🚨 Depuis plusieurs mois, les frais de transaction sur Ethereum ont augmenté significativement. Lorsque les coûts en gaz sont excessifs, vous pouvez avoir des messages d’erreur lorsque vous demandez une adresse de Dépôt à Tip.cc. Si cela vous arrive, réessayez la commande adéquate lorsque les coûts de transaction (gas) seront plus modérés.

🚩 L’utilisation de Tip.cc se fait via des commandes à écrire dans des messages. Un préfixe est désigné avant chaque commande. Le préfixe par défaut est `$`, mais il est paramétrable, et peut être différent sur chaque serveur Discord. ( Exemple : `$` sur le serveur CryptoMatrix, `!` sur le serveur Monolith)

**Ce guide utilisera le préfixe par défaut `$`**

### 1. Manipulation du portefeuille Tip.cc:

{{< notice tip >}}
Par précaution, nous vous conseillons d'utilisez la commande $bals uniquement en message privé.
{{< /notice >}}

Le `$withdraw` et le `$deposit` quant à eux ne peuvent se faire qu’en message privé.

*   `$balances` et son raccourci `$bals` 

Voir le contenu de votre wallet. 

Vous pouvez aussi préciser  `$bals eur` pour voir le total en euros. En discussion privé avec Tip.cc, le total s'affiche en dollars sans cette précision.

![guide-Discord-tipbot](/img/2020/tipbot/image12.jpg "Balances sur Tipbot")

*   `$balance eth` et son raccourci `$bal ethereum`

Voir la somme d’une crypto spécifique de votre wallet. Remplacez `ethereum` par la crypto-monnaie souhaité. Les raccourcis comme `btc`ou `tkn` marche, tout comme les noms complets comme `bitcoin` ou `monolith`.
    
![guide-Discord-tipbot](/img/2020/tipbot/image3.jpg "Balance ETH")


*   `$currencies`

Voir toutes les crypto-monnaies supporté par Tip.cc. Vous pouvez naviguer avec les flèches bleues pour toute les découvrir. Chaque Discord utilisant Tip.cc peut choisir de limiter la liste des crypto-monnaies disponible à sa convenance.

![guide-Discord-tipbot](/img/2020/tipbot/image20.jpg "Les tokens supportés sur TipBot")

*   `$withdraw btc`

En utilisant cette commande en message privé, vous recevrez une demande d’adresse pour envoyer votre retrait vers l’adresse de votre choix. Vous pouvez aussi envoyer une photo de votre QR code en message privé au bot.

![guide-Discord-tipbot](/img/2020/tipbot/image5.jpg "Retirer du BTC")

Une confirmation vous sera ensuite demandée pour le montant.

![guide-Discord-tipbot](/img/2020/tipbot/image11.jpg "Confirmation de retrait")


*   `$deposit btc`

Commande pour permettre le dépôt de crypto-monnaies sur votre portefeuille Tip.cc . `$deposit xtz` fera apparaître un code QR ainsi que l’adresse de dépôt de la crypto-monnaie visé pour votre portefeuille.

![guide-Discord-tipbot](/img/2020/tipbot/image8.jpg "Dépôt de BTC")

{{< notice tip >}}
La commande deposit ne fonctionne qu’en message privé avec Tip.cc. Si vous l’écrivez dans un salon public, vous recevrez automatiquement un message privé.
{{< /notice >}}

### 2. Interaction avec les utilisateurs du Discord:

#### 1. Les tips `$tip`

Exemple: `$tip @user 1 TKN`


Cette commande est la base de vos interactions avec les autres utilisateurs. Pour envoyer de la crypto-monnaie à un autre utilisateur du Discord, il suffit d’écrire `$tip`, son pseudo `@user`, le montant `10`, et la crypto-monnaie, `btc`. Ce qui donne : `$tip @user 1 btc`

![guide-Discord-tipbot](/img/2020/tipbot/image14.jpg "Tip de 5 TKN")


Vous pouvez aussi tiper plusieurs personnes en même temps : `$tip @userA @userB 20 TKN` ou encore `$tip all @role 70 USDC`

Vous pouvez tiper un groupe entier avec cette commande, la somme se verra partagée équitablement pour le rôle dans une limite de 40 membres.


Plein de variantes sont possible: changez `online` à la place de `all` pour ne tiper que les utilisateurs en ligne. La combinaison de groupe et possible avec `and`.

> Exemple :  `$tip 4 online @Utopiste and 10 offline @Analyste 15 ETH`

Voici la liste des paramètres disponibles:

- `offline`: choisir uniquement des membres hors ligne

> ex: `$tip 5 offline @Analyste 5 ETH`

-    `online`: choisir uniquement des membres en ligne

>ex: `$tip online @Utopiste 0.9 BTC`

-    `all`: choisir tous les membres d’un groupe

>ex: `$tip all @Utopiste 10 LINK`

-    `each`: donne à chacun la même somme

>ex: `$tip all @Utopiste 1 LINK each`

-    `and`: combine des tips

>ex: `$tip all @Utopiste 1 LINK and 2 ETH`


-    `random`: donne à une personne choisie aléatoirement votre tip

>ex: `$tip a random person 10 USDC`


-    `recently active`: pour viser des personnes avec une activité récente sur le Discord...


-    `active in the last x minutes`: remplacez x par un nombre


-    `active in the last x messages`: remplacez x par un nombre


-    `active x messages`: remplacez x par un nombre


-    `active x m`: remplacez x par un nombre, m pour minute


{{< notice tip >}}
La commande $tip help permet de voir (en anglais) toutes les combinaisons de tips possibles.
{{< /notice >}}

Marre d’être mentionné pour recevoir des poussières avec les distributions aléatoires ? Vous pouvez désactiver et réactiver les mentions avec une seul et même commande: `$tip nomention`

Vous pouvez aussi [📖 retrouver toutes les commandes ici](https://tip.cc/guides/tipping). 

#### 2. Les airdrops

Les airdrops permettent de tip aléatoirement des utilisateurs via un message. Cinq types de airdrop sont disponibles: 

1.   Le **Airdrop** classique, ou il faut réagir à un message airdrop pendant un temps donné
2.   Le **Phrasedrop**, ou il faut écrire une phrase correctement pour avoir une chance de gagner.
3.   Le **Mathdrop**, ou il faut résoudre une équation mathématique pour être sélectionné.
4.   Le **Redpacket**, une enveloppe rouge pour le premier à réagir au airdrop. 
5.   **Triviadrop**, où il faut répondre correctement à une question aléatoire sur l’univers des crypto-monnaies.

##### Airdrop Classique 

*   `$airdrop &lt;montant> for [durée] for [maximum d’utilisateur]`
*   `$airdrop &lt;montant>`

Les gains sont séparés entre tous les utilisateurs ayant réagi dans les limites imposées.


> ex: `$airdrop 100 satoshis for 30 seconds for 10 people`

> ou: `$airdrop 0.2 ETH`


![guide-Discord-tipbot](/img/2020/tipbot/image16.png "Tipbot Airdrop - Cliquez sur 🎉 pour collecter !")


##### PhraseDrop 

*   `$phrasedrop [montant] for [durée] for [maximum d’utilisateur] [phrase]`

Les gains sont séparés entre tous les utilisateurs ayant réécrit la phrase correctement dans les limites imposées.

> ex: `phrasedrop $20 for 4 minutes for 10 users "Le Discord de CryptoMatrix c’est le meilleur"`


##### MathDrop 

*   `$mathdrop [montant] for [durée] for [maximum d’utilisateur] [expression]`

Les gains sont séparés pour les utilisateurs ayant résolu l’équation dans les limites imposées.


> ex: `$mathdrop 5 TKN for 5 minutes for 3 users "2 + 40"`



##### Enveloppe Rouge


*   `$redenvelope [montant] [durée]`

Le premier utilisateur à réagir dans le temps imparti récolte la somme.

>ex: `$redenvelope 0.005 btc 10s`

![guide-Discord-tipbot](/img/2020/tipbot/image18.png "Red Packet")



##### TriviaDrop 



*   `$triviadrop [montant] for [durée] for [maximum d’utilisateur]`

Les gains sont répartis parmi les utilisateurs répondant correctement. Vous recevez une notification par DM si vous répondez correctement.

> ex: `$triviadrop $1 for 30 minutes for 10 users`

![guide-Discord-tipbot](/img/2020/tipbot/image21.png "Trivia Drop")


### 3. Interaction avec les outils du bot

Tip.cc comprend des outils sympathiques à utiliser en plus de sa fonction de wallet et de tip :

*   `$ticker lend`

Vous pouvez utiliser cette commande pour avoir des informations sur le prix d’un token, ainsi que son graphique en 1D si celui-ci est listé sur coingecko. Remplacez `lend` par le token que vous souhaitez.

![guide-Discord-tipbot](/img/2020/tipbot/image24.jpg "Ticker Lend sur Tipbot")


*   `$uniswap 0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e`

Affiche les informations d’un token listé sur uniswap. Vous pouvez soit écrire l’adresse contrat du token, **soit écrire son nom** s’il fait partie des plus connus. (exemple: `$uniswap tkn`)

![guide-Discord-tipbot](/img/2020/tipbot/image6.jpg "Aperçu de la paire YFI/ETH Uniswap dans TipBot")


*   `$gas`

Les prix de gas Ethereum et Bitcoin à l’instant T vous sont accessible via cette commande. Les données sont récupérées depuis mempool.space et [ETH Gas Station](https://ethgasstation.info/).

![guide-Discord-tipbot](/img/2020/tipbot/image19.jpg "Aperçu des coûts des transaction")


*   `$mining eth`

Affiche le hashrate et la difficulté de la crypto-monnaie demandée. Les informations sont récupérées depuis MiningPoolStats. Remplacez `eth` par une des  crypto-monnaies présente dans les données de MiningPoolStats.stream.

![guide-Discord-tipbot](/img/2020/tipbot/image7.jpg)


*   `$pools eth`

Affiche les pools les plus actives de la crypto-monnaie demandée. Les informations sont récupérées depuis MiningPoolStats. Remplacez **eth** par une des  crypto-monnaies présente dans les données de MiningPoolStats.stream. Vous pouvez naviguer avec les flèches bleues en réactions sous le message.

![guide-Discord-tipbot](/img/2020/tipbot/image10.jpg "Top 10 ETH Mining Pool")

*   `$convert`

Une fonction de conversion est présente avec Tip.cc. Vous pouvez voir à quoi correspond une somme, en  fiat et en crypto, grâce à cette commande.

> ex: `$convert 100€ ; $convert 100$ ETH ; $convert 10 ETH ...`

*   `$faucet btc`

Le bot Tip.cc comprend lui-même un faucet pour aider à découvrir et utiliser les fonctions du service. Vous devez préciser btc, eth, ou autre crypto-monnaie dans la commande, puis suivez le lien pour effectuer un vote pour tip.cc sur top.gg. L’action est possible chaque 12h . Le service de faucet n’est en rien relié avec les Discords hébergeant Tip.cc. 


![guide-Discord-tipbot](/img/2020/tipbot/image25.jpg)
![guide-Discord-tipbot](/img/2020/tipbot/image17.jpg)
 

*   `$help`

Cette commande vous fournira un panneau d’aide à l’utilisation en anglais. Vous pouvez naviguer à l’aide des réactions.

![guide-Discord-tipbot](/img/2020/tipbot/image2.jpg "Message d'intro Tipbot")


*   `$monikers`

Affiche la liste des surnoms. Un surnom est un mot ou une suite de mots pré-paramétrés pour une transaction, avec son montant et sa crypto-monnaie fixe. Chaque surnom à son pluriel, vous pouvez donc écrire pour les gourmands `$tip @user 3 pizzas`. 

Des surnoms peuvent être écrits au lieu des transactions traditionnelles. Il existe quelques surnoms de base, mais les administrateurs de votre Discord peuvent en ajouter si vous avez quelques suggestions sympathiques à leur fournir. 

Si la crypto-monnaie n’est pas précisée, la transaction sera effectuée avec la monnaie par défaut choisie par le Discord (BTC pour le serveur CryptoMatrix, TKN pour le serveur Monolith). La crypto-monnaie par défaut peut être changée par les administrateurs.

![guide-Discord-tipbot](/img/2020/tipbot/image15.jpg "Monikers")


J’espère que la lecture vous aura apporté les précisions attendues pour utiliser Tip.cc en toute sérénité ! 

{{< notice note >}}
🙏 Ce guide vous est fourni par Loico. Il vous a été utile ? 

Rejoignez [le serveur Discord CryptoMatrix](https://discord.gg/mW94vUU) pour le remercier en personne !
{{< /notice >}}

## Ressources externes

- [Site officiel](https://tip.cc/)
- [Guide officiel](https://tip.cc/guides)
- [Crypto-monnaies supportés](https://tip.cc/currencies)
- [Discord Tip.cc](https://Discord.gg/fzdvTkR) 
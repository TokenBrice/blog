---
title: "L'état et le futur des Stablecoins algorithmiques"
description: "Une analyse de DSD, ESD et Basis Cash pour dresser le portrait-robot de ce qui pourrai bien être le stablecoin de demain."
date: '2020-12-28T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Stablecoin, Yield]
tags: [DeFi, Ethereum, Stablecoins, Basis Cash, Empty Set Dollar, sUSD, ESD, DSD, BAC, BAS]
series: stablecoin-arc
series_order: 2
image: /img/2020/algorithmic-stablecoins/cover.png
difficulty: "intermediate"
url: algorithmic-stablecoins
aliases:
  - algorithmic-Stablecoins
---

Depuis début décembre, une nouvelle tendance se dessine dans le DeFi : les Stablecoins algorithmiques. Plusieurs projets ont été lancés et ont connu une croissance importante, suscitant encore plus d'intérêt pour ce sous-ensemble de l'espace.

Avant de nous plonger dans ce qu'ils sont et ce qu'ils impliquent, abordons d'abord les marchés envisageables. Les Stablecoins sur Ethereum sont massifs : ils circulent autour de 20B USDT, 3.5B USDC & 1B DAI. Comme vous pouvez le constater, la majeure partie du volume est actuellement desservie par des Stablecoins nécessitant une certaine forme de confiance, tels que **USDC ou USDT : la société émettrice a le pouvoir de geler les actifs et de manipuler les soldes**.

Maker a exploré une autre approche avec le DAI qui comporte beaucoup moins de compromis - cependant, l'extensibilité est réduite. En outre, il est difficile de considérer le DAI comme "suffisamment trustless" aujourd'hui alors que 60% des garanties utilisées pour le frapper ne le sont pas (USDC, wBTC, TUSD, etc.)

Il convient donc de rappeler que jusqu'à présent, il existe une demande insatisfaite évidente dans le domaine des Stablecoins - ceux qui ont atteint un total circulant important l'ont fait avec des compromis significatifs, ce qui leur a permis de satisfaire les marchés bien qu'il s'agisse de services nécessitant de la confiance, et qui en sont plus ou moins dignes (en particulier USDT).

La raison pour laquelle j'écris cet article aujourd'hui est qu'après avoir suivi l'évolution de l'espace des Stablecoins pendant des années, il semble que nous ayons atteint une percée passionnante avec une nouvelle génération de Stablecoins capables d'offrir **à la fois une évolutivité et une trustlessness**. Le sujet n'est ni simple ni facilement accessible, surtout pour les nouveaux arrivants. Je ferai de mon mieux pour vous guider pas à pas dans le processus de réflexion.

---

### Pourquoi avons-nous besoin de Stablecoins trustless ?

Avant de nous plonger dans quel projet  fait quoi et à quelle fin prenons un peu de recul. Nous avons établi qu'il existe une demande importante de Stablecoins, et qu'aucune des offres phares actuelles n'est suffisamment trustless. Mais qu'est-ce que cela signifie exactement ?

En termes simples, la **trustlessness signifie que l'ensemble du système ne nécessite aucun point de confiance central pour fonctionner correctement**. On parle souvent de "résistance à la censure", une propriété différente qui découle de la trustlessness. D'un point de vue pratique, voici donc quelques questions pour vous aider à évaluer la trustlessness : plus les autorisations sont permissives, moins le projet a tendance à être trustless :

1. Est-ce que les tokens peuvent être saisis ou gelés ?
2. Le code ou les paramètres du protocole peuvent-ils être mis à jour ? Dans quelles conditions ? Par qui ?
3. Le protocole dépend-il de services tiers, tels qu'un flux de prix (oracle) qui pourrait être manipulé ?
4. Qui/quoi peut frapper de nouveaux tokens ? Est-ce à l'initiative de l'utilisateur (quelqu'un prend une action) ou du protocole (une décision que le protocole prend en fonction de paramètres donnés) ?

La dernière question est particulièrement pertinente, car elle met en évidence un élément essentiel des Stablecoins algorithmiques : **leur "banque centrale" est un contrat intelligent** - personne ne la contrôle, elle réagit simplement aux paramètres du système. Nous y reviendrons plus loin.

Avec cette pièce, nous allons donc examiner les principaux modèles disponibles : Ampleforth, Basis Cash, Empty Set Dollar, et Dynamic Set Dollar. Je ne vais pas me plonger dans l'histoire de l'espace et les spécificités de chaque modèle, n'hésitez pas à consulter cet article de Deribit Insights si vous avez besoin de plus de contexte :

👉 [Stabilité, élasticité et réflexivité : A Deep Dive into Algorithmic Stablecoins](https://insights.deribit.com/market-research/stability-elasticity-and-reflexivity-a-deep-dive-into-algorithmic-Stablecoins/)

Donc, au lieu de plonger dans les détails de chaque système, je vais dessiner **un croquis montrant les principes fondamentaux sur lesquels cette génération de Stablecoins est construite**, en me basant sur les paramètres et les approches de conception communs à tous les projets.

---
### Central Smart Contract

La première dimension intéressante est la "banque centrale" du système - c'est-à-dire qui/quoi peut imprimer de nouveaux tokens et à quelles conditions ? **L'USDC et l'USDT reproduisent à peu près une banque centrale** - une entité est chargée du projet et de l'émission de nouveaux tokens.

Comme Maker n'est qu'un contrat intelligent permettant à ses utilisateurs de frapper le DAI à partir de certaines garanties, l'approche est différente ici. Pour l'essentiel, **Maker/DAI vous permet d'être votre propre banque centrale**. La banque centrale de Maker est donc un contrat intelligent, mais elle exige une intervention humaine pour frapper le DAI.

Les Stablecoins algorithmiques vont encore plus loin, puisque **l'apport humain est retiré du processus de frappe**. Dans ces systèmes, personne n'a la capacité de frapper des tokens - seul le contrat intelligent qui le gère le peut. C'est très élégant et minimal, mais cela nécessite un ensemble d'incitations soigneusement conçues pour s'assurer que les Stablecoins finiront par se rapprocher de leur valeur nominale. Pour dire les choses simplement, **avec des Stablecoins algorithmiques, la banque centrale est un contrat intelligent autonome.**

### Une armée de stabilisateurs

Avec les Stablecoins algorithmiques, surtout à leurs débuts, les ruptures de peg sont fréquentes. Pour ramener le stablecoin à son point d'ancrage, les protocoles prévoient différents types d'incitations.

Lorsque le stablecoin vaut plus d'un dollar, **le protocole frappe de nouveaux jetons et les distribue comme incitation** aux utilisateurs qui fournissent des liquidités ou qui verrouillent leur token, ce qui contribue à faire baisser le prix.

Lorsque le stablecoin se négocie en dessous de 1 $, le système des coupons (ou obligations) entre en jeu : **Les utilisateurs peuvent brûler leurs Stablecoins pour un coupon** le représentant + une prime. Toutefois, ils ne pourront réclamer le coupon qu'une fois que le prix sera de nouveau supérieur au dollar.

Comme vous pouvez le voir, à un niveau élevé, ces mécanismes sont simples. Ils comportent des subtilités que vous devez maîtriser si vous voulez participer au système. **Les utilisateurs qui les comprennent et les suivent peuvent aider le protocole à se stabiliser**, et si c'est le cas, ils peuvent gagner de l'argent dans le processus. Ces règles simples conduisent donc à l'émergence d'une armée de stabilisateurs, qui utilisent tous les mécanismes pour stabiliser le prix :

Cette conception pousse la théorie du jeu et le jeu de mime à un autre niveau :

![DSD Meme](/img/2020/algorithmic-stablecoins/dsd-meme.jpeg "Un meme DSD")

### Phase d'expansion agressive

Comme l'approvisionnement en Stablecoins algorithmiques est élastique, leur mécanisme est rapidement mis à l'épreuve. En effet, au moment du lancement, l'offre circulante de Stablecoins est généralement faible et les incitations intéressantes créent une forte demande.

Par exemple, **Basis Cash a été lancé avec 50 000 jetons BAC** distribués aux premiers participants. Environ un mois après, il y a maintenant **40M de BAC en circulation** : ils ont été produits parce que le BAC s'est échangé à plus d'un dollar la plupart des jours depuis le lancement. Jusqu'à présent, il n'y a pas eu de phase où le BAC s'est négocié à >1$, donc le système de coupons de la base (BAB) n'a pas encore été testé.

{{< notice info >}}
L'expansion et la contraction sont phasés dans des "epochs". L'epoch de Basis Cash a une durée de 24 heures. ESD est de 8h et DSD est de 2h.
{{< /notice >}}

En revanche, l'ESD et le DSD ont déjà connu plusieurs cycles d'expansion et de contraction chacun, le protocole fonctionnant comme prévu :

![DSD Market Cap au cours des 7 derniers jours](/img/2020/algorithmic-stablecoins/dsd-mktcap.png "DSD Market Cap montre clairement les phases d'expansion/contraction")

### Exploiter la composabilité du DeFi

Un autre principe clé des Stablecoins algorithmiques est la composabilité. On y pense souvent comme à "comment puis-je brancher mon produit/service fini sur d'autres". Ces projets vont beaucoup plus loin, car **ils utilisent d'autres protocoles comme Uniswap comme partie centrale de leur système dès le début.** Basis, ESD et DSD ont tous trois des composantes principales :

1. Un mécanisme interne de verrouillage/prise en charge des phases d'expansion (DAO ou Boardroom)
2. Un mécanisme de "burn&redeem" pour les phases de contraction
3. Une paire Uniswap (/USDC ou /DAI)

Leur structure même démontre une compréhension du DeFi et de sa composabilité. En plaçant la (les) paire(s) Uniswap au cœur du protocole, cela aide à bien des niveaux - puisque **Uniswap est la base du DeFi que les utilisateurs connaissent bien.**

Bien que l'Uniswap soit le principal pool, la liquidité des autres DEX est de plus en plus examinée. Avec le lancement d'Omakase, Sushi a ajouté deux nouveaux pools de Stablecoins algorithmiques incitatifs : ESD/ETH & DSD/USDC.

La composabilité est essentielle pour les Stablecoins algorithmiques et plusieurs projets prennent déjà des mesures pour s'intégrer davantage dans l'écosystème. Dans les prochains mois, nous devrions en voir les prochaines étapes avec l'arrivée de certains Stablecoins algorithmiques comme garantie sur les plateformes de prêt.

### Oracle Minimaliste

Les oracles sont utilisés comme paramètre de base dans le système algorithmique des Stablecoins: : ils sont la **source de vérité pour le prix du stablecoin**. Il est essentiel de s'assurer que l'oracle est résistant et ne peut pas être manipulé.

Pour ce faire, la génération précédente de projets, en particulier Maker, avait tendance à suringénierieser. Dans les premiers temps, le paramètre d'entrée de Maker était presque le prix pur et brut de l'ETH. Cependant, pour rendre le système moins sujet aux "liquidations éclair", Maker a construit son propre oracle, et utilise plusieurs délais et moyennes avec le prix de liquidation pour **ajouter une certaine inertie à son système**.

D'autre part, comme nous l'avons vu précédemment, nos Stablecoins algorithmiques ont tendance à être minimalistes et à exploiter la composabilité du DeFi. **Avec leurs paires Uniswap, ils ont déjà une un flux de prix décent avec une liquidité importante, ce qui le rend difficile à manipuler**. Le prix Uniswap est donc utilisé comme base, mais généralement calculé comme un TWAP (Time Weighted Average Price) afin d'éviter les manipulations de prix juste avant les rebases.

Tout en étant minimalistes, les systèmes sont efficaces et élégants : à mesure que ces projets de Stablecoins se développent, leur liquidité sur l'Uniswap devrait augmenter, rendant l'oracle plus résistant et le prix plus difficile à manipuler.

Pour ma part, je suis enthousiaste quant à la direction que prend ce sous-ensemble de l'espace. Que vous ayez l'intention de participer ou non à la phase d'amorçage de ces Stablecoins, je pense qu'il est très utile de vous documenter sur eux car ils sont un bon indicateur des principales tendances de l'espace.

---

### 🧰 Boîte à outils pour les Stablecoins algorithmique

Avant de nous séparer, permettez-moi de vous présenter quelques outils utiles pour suivre l'évolution de ces Stablecoins. Tout d'abord, chaque projet possède son propre tracker qui fournit les principales mesures de l'époque actuelle :

- **[Basis Cash Tools](https://bc.tools/)**
- **[Outils de suivi ESD](https://esd.tools/)**
- **[Outils de suivi DSD](https://dsd.tools/)**

Enfin, vous pouvez consulter des informations plus détaillées sur le système ESD et DSD sur ce tableau de bord : **[ESD/DSD Bonding](https://duneanalytics.com/tongnk/esd_1)**

### Disclaimer

{{< notice warning >}}
**CET ARTICLE NE CONSTITUE PAS UN CONSEIL EN INVESTISSEMENT.**

Je ne suis pas un conseiller financier qualifié, mais qui en a vraiment quelque chose à foutre ? C'est de DeFi qu'on parle.
{{< /notice >}}

Je me suis senti légitime d'écrire cet article parce que j'ai suivi de près le Basis Cash, le Empty Set Dollar et le Dynamic Set Dollar, ainsi que le Basis Dollar & Share moins attentivement. Frax est un autre projet hybride qui mérite d'être examiné - je n'en ai pas parlé car je ne le connais pas encore assez.

{{< notice note >}}
**💰 Bag Disclosure** : Je possède des BAC/BAS (Basis Cash), ESD (Empty Set Dollar) et DSD (Dynamic Set Dollar).
{{< /notice >}}

J'espère que cette lecture vous a éclairé. Si c'est le cas, vous pouvez **[me suivre sur Twitter](https://twitter.com/tokenbrice/)** ou ce blog par RSS (tout en bas de la page 👇) pour être informé de la publication des prochains articles.

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/channel/UCefQC4Y-X9MBRuYBKc2waiQ)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}

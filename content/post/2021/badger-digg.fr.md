---
title: "L'histoire de BadgerDAO : une intro via DIGG"
description: "Analyse de BadgerDAO, de ses vaults, de DIGG et de sa position entre gestion d actifs DeFi et Bitcoin sur Ethereum."
date: '2021-01-30T01:13:50.191Z'
reviewed: 2026-05-19
categories: [Yield]
tags: [DeFi, Ethereum, Badger, BadgerDAO, DIGG]
toc: true
tocNum: true
url: badger-digg
image: /img/2021/badger-digg/cover.png
difficulty: "beginner"
---

Malgré son lancement il y a à peine quelques semaines, BadgerDAO s'est rapidement transformé en une centrale DeFi **hébergeant maintenant > 1,2 milliard de dollars d'actifs**. Bien que j'ai rapidement évoqué Badger dans des articles ou des émissions précédentes, je pense qu'il est temps de consacrer un article à DIGG, sans oublier son contexte.

## Une introduction à Badger DAO

BadgetDAO est un projet communautaire avec une proposition de valeur claire : aider **à construire l'infrastructure nécessaire pour relayer BTC dans la DeFi**. Cette vision fondamentale se manifeste à travers tous leurs produits, tous centrés autour de représentations de Bitcoin sur Ethereum comme wBTC ou sBTC et les tokens natifs - BADGER et maintenant DIGG.

### Proposition de valeur claire : Optimisation de BTC sur Ethereum

La première couche de cet oignon est assez simple : Badger offre un service de type Yearn pour les BTC sur Ethereum : les utilisateurs peuvent déposer des tokens représentant une position dans un pool de BTC Curve pour gagner BADGER & DIGG en plus de l'APY natif.

![badger-stats](/img/2021/badger-digg/badger-stats.png "Aperçu des principales métriques de Badger avec Sett.Vision")

Il existe également des vaults (appelés "setts") pour BADGER et DIGG eux-mêmes, ainsi que leurs tokens LP respectifs sur Uniswap et SushiSwap.

{{< notice tip >}}
Les vaults comme ceux de Yearn sont inspirés du design des aTokens sur Aave : au départ, lorsque le coffre est lancé, la correspondance entre l'actif de base et le token du vault est de 1:1. Au fur et à mesure que le vault accumule des tokens supplémentaires grâce à ses récoltes, son token représente de plus en plus l'actif sous-jacent.
{{< /notice >}}

Cette proposition de valeur n'est pas nouvelle en soi et aurait pu être fournie directement par Yearn. Ce qui rend Badger spécial, c'est **la façon dont l'équipe aborde la construction du produit et toute la vision sous-jacente derrière celui-ci.**

### Une approche communautaire

Depuis le début, la communauté a été mise au centre avec Badger. C'est clairement visible simplement en regardant les distributions de tokens [^1] :

![aperçu de la distribution de badger](/img/2021/badger-digg/badger-breakdown.png "Aperçu de la distribution initiale du token BADGER")

![aperçu de la distribution de digg](/img/2021/badger-digg/digg-breakdown.png "Aperçu de la distribution initiale du token DIGG")

En effet, les deux plus grandes parts du total circulant des deux tokens ont été allouées au programme de liquidity mining - récompensant les utilisateurs actifs du protocole ainsi que la trésorerie du DAO chargée de structurer les opérations à long terme du protocole et sa croissance.

Les aidrops, ainsi que les vaults, ont créé une boucle très attrayante pour les destinataires : contrairement au airdrop UNI où le choix était simplement vendre ou attendre, avec BADGER & DIGG, les personnes **optimistes quant au protocole dès le départ avaient la possibilité de s'impliquer avec leurs tokens reçus grâce aux vaults.**.

L'aidrop initial de BADGER reconnaissait les actions clés liées à Bitcoin sur Ethereum, ainsi que les donateurs de gitcoin. Le deuxième airdrop (DIGG) a récompensé les interactions avec l'écosystème de Badger lui-même.

En plus de l'élan créé par le lancement et la distribution initiale, la communauté a pu le maintenir grâce à un esprit de meme florissant : une distribution de NFT a été organisée sur Meme[^2], disponible pour les déposants dans le sett bBADGER ou le sett wBTC/BADGER Uniswap.

Au total, 6 NFTs différents étaient disponibles et le premier à les collecter pouvait réclamer une prime BADGER. Le fait d'être détenteur ou farmer de ces NFT a été reconnu dans la distribution initiale de DIGG et leur inclusion dans Badger comme multiplicateur de rendement est en cours de discussion.

<video autoplay loop muted playsinline title="Un des 6 Badger x Meme NFTs - Satoshi">
  <source src="/img/2021/badger-digg/badger-nft-satoshi.mp4" type="video/mp4">
  Your browser does not support video. <a href="/img/2021/badger-digg/badger-nft-satoshi.gif">View GIF</a>
</video>

{{< notice tip >}}
Si vous êtes très optimiste sur le prix d'un token à court terme, c'est généralement une mauvaise idée d'entrer dans une position à 50/50 fournissant des liquidités sur celui-ci, surtout si vous vous attendez à ce que l'autre actif de la paire (ETH, Stablecoins ou ici wBTC) reste relativement stable sur la même période. Si vous craignez que ce scénario se produise avec Badger ou DIGG, vous pouvez déposer dans les coffres-forts de BADGER ou de DIGG uniquement (pas de risque de perte impermanente).
{{< /notice >}}

---

## Alors, on DIGG ?

DIGG est la deuxième grande étape du projet DAO de Badger : un nouveau type de représentation de BTC vivant sur la Blockchain Ethereum. Contrairement à la wBTC ou à la renBTC, **DIGG n'est pas soutenu par stock de BTC**. Il utilise plutôt le mécanisme de rebase initié par Ampleforth pour tenter de livrer à terme un actif qui suit le prix de BTC.

Avant de nous plonger dans le fonctionnement de DIGG, parlons rapidement du pré et post-lancement.

### Wen DIGG ?

Le lancement de DIGG était un événement très attendu. Alors que de l'extérieur, il semble que cela ait pris plus de temps que prévu, ce qui s'est passé à l'intérieur était fascinant : la **communauté initiale réunie autour de Badger a participé activement aux décisions clés entourant DIGG.**

Après discussion au sein de la communauté, il a été décidé de partir avec une offre de départ relativement faible (4000) permettant un **test de stress dès le début du mécanisme de rebase**. Les rebases ont également commencé dès le tout début - 24h après le lancement du token.

![wen-digg](/img/2021/badger-digg/wen-digg.jpeg "Wen DIGG meme contest")

Badger étant Badger, la machine à hype était bien sûr au point avec un concours de mèmes "Wen DIGG ?" pour s'assurer que tout le monde soit au courant.

Alors sans plus attendre, plongeons dans le vif du sujet : les rebases.

### Les rebases

Le DIGG est ce qu'on appelle une "monnaie élastique", comme l'a initié Ampleforth. Cela signifie que l'offre totale de DIGG n'est pas fixée, mais fluctue quotidiennement en fonction du prix moyen pondéré dans le temps de le DIGG par rapport à son ancrage - le BTC.

Plus le DIGG est "en dehors de son périmètre", ce qui signifie que son prix est supérieur au prix de BTC, plus l'offre de DIGG est diluée, le DIGG supplémentaire produit étant distribuée proportionnellement à tous les détenteurs - et il se passe la même chose dans l'autre sens : contraction si le prix est inférieur à l'ancrage.

Tout comme pour l'AMPL, avec DIGG, tous les détenteurs (y compris les tokens de pool de liquidité) sont touchés par la rebase, qu'elle soit positive ou négative. Cependant, avec DIGG, tout comme avec les tokens de seigneuriage, il existe **un mécanisme pour abstraire la rebase afin de permettre une meilleure composabilité au sein de DeFi : c'est bDIGG**, nous en discuterons juste après.

Les rebases se font à une heure fixe, pour DIGG c'est 15h EST, c'est 21h pour mes chers lecteurs français.

{{< notice tip >}}
Les tokens de rebasage exploitent des mécanismes similaires à ceux impliqués dans les Stablecoins algorithmiques / tokens de seigneuriage, alors n'hésitez pas à lire mon **[précédent billet sur le sujet](https://tokenbrice.xyz/fr/seigniorage-basis-esd/)** pour plus d'informations.
{{< /notice >}}

Par exemple, après le premier jour, la rebase de genèse était positive et a déclenché une production et une redistribution d'environ 12% de l'offre initiale. Plusieurs rebases positives ont suivi.

Pour l'instant, le mécanisme de rebase est assez simple, mais il pourrait être mieux aligné sur les incitations de l'ensemble à l'avenir pour aider le DIGG à maintenir son ancrage.


### Prochaine étape pour les Setts

Avec le lancement du DIGG, la prochaine grande étape pour Badger, en tant que protocole, est de commencer à **accroître son efficacité en termes de capital** : pour le dire plus simplement, permettre à ses utilisateurs **d'emprunter à partir de leurs positions dans les setts**.

Pour être plus clair (tout en extrapolant un peu) : imaginez le Badger actuel, avec une fonction supplémentaire vous permettant de frapper des DAI à partir de vos sets comme vous le faites avec vos ETH sur Maker. Vous ne le feriez pas ?

En effet, les setts constitueraient un collateral tout à fait souhaitable, étant donné qu'ils prennent de la valeur par rapport à l'actif de base. Ainsi, les setts BTC  par exemple, pourraient être aussi sûrs que leurs actifs sous-jacents (ex wBTC), compte tenu des risques supplémentaires liés au fait que l'actif sous-jacent est dans une position d'apporteur de liquidité.

Toutefois, avant que nous n'ayons un marché de prêt natif sur Badger, je m'attends à voir différents **tokens et setts liés à Badger acceptés en collateral** sur d'autres plateformes de prêt.

Sur ce point, j'aimerais attirer votre attention sur le bDIGG en particulier. Bien qu'il représente une position faite à 100% de DIGG qui se rebase, **bDIGG lui-même ne se rebase pas**. C'est comme une couche d'abstraction construite sur DIGG, un tampon de rebase entre autres choses. Cela facilite l'intégration dans d'autres protocoles, et je m'attends à voir un jour une large gamme de supports pour bDIGG.

---

## La fin de jeu pour BadgerDAO & la DeFi

La fin du jeu pour Badger serait comme celle que j'ai décrite précédemment, avec un écosystème complet autour du CLAW ou quel que soit son nom.[^3] Badger deviendrait de plus en plus un service de type Synthetix où les détenteurs se verraient proposer différentes options de participation plus ou moins active à l'écosystème, avec les récompenses appropriées.

Comme les services comme Badger intègrent des éléments du marché monétaire tels que l'emprunt, ils **augmentent l'efficacité du capital pour leurs utilisateurs**. Ce qui était autrefois une représentation de la BTC produisant 20 % d'APY est maintenant le même + vous pouvez emprunter une partie de sa valeur en Stablecoins pour augmenter encore le rendement, si cela correspond à votre appétit pour le risque.

Cette logique est plus grande que Badger, comme on l'observe ailleurs aussi, on pourrait l'appeler la **"plateformisation de DeFi**". Yearn met en place une approche similaire avec l'Iron Bank, où certains services pourront emprunter avec une garantie insuffisante, ce qui créera un fossé d'efficacité du capital pour les chanceux éligibles.

De plus, pour revenir à Badger, l'adoption d'un tel modèle pourrait signifier des revenus natifs et durables qui pourraient être liés à au token BADGER ou son sett. Si l'on considère que la plupart des rendements proviennent actuellement d'incitations à l'apport des liquidités, il serait assez synergique d'en tirer parti.

Compte tenu **[du succès du modèle Curve / CRV](https://tokenbrice.xyz/fr/dex-echanges-decentralisees-capture-valeur/)**, il est logique de voir de plus en plus de protocoles en adopter les éléments : l'essentiel étant de donner à vos détenteurs la possibilité d'engager leurs tokens pour participer à la gouvernance, de puiser dans les flux de revenus de la plateforme et d'augmenter leurs propres rendements obtenus par l'utilisation du service.

_🙏 Un grand merci à HHK, Charles, Thomas, Erwan, [PhilH](https://twitter.com/phil_h) & FrenchTony pour leur relecture attentive de l'édition française de cet article et sa traduction en Anglais._

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/c/DeFiFrance)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}

---

## Notes & Références

[^1]: Les graphiques proviennent de [Badger's DAO liquidity mining launch announcement](https://badgerdao.medium.com/badger-dao-liquidity-mining-launch-b2415301bd31#:~:text=Tokens%20distributed%3A%20%24BADGER%20and%20%24,2nd%20product%20of%20the%20DAO.).
[^2]: **[Meme](https://dontbuymeme.com/collections/badger)** est un mécanisme de distribution pour la NFT où les utilisateurs mettent en jeu un token donné (bBADGER dans notre cas) pour gagner des points - les ananas. Ils peuvent ensuite échanger les ananas contre le NFT de leur choix.
[^3]: Ça n'est pas de la spéculation pure - BadgerDAO considère déjà comment utiliser les [synergies avec UMA et SushiSwap à cet effet](https://twitter.com/spadaboom1/status/1354826775801561091?s=20).
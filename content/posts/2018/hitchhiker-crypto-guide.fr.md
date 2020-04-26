---
title: 'Naviguer le cryptomonde : le guide pour repérer les arnaques et shitcoins'
description: >-
  Un aperçu des principales choses à regarder avant d'investir dans un projet de
  crypto, et des astuces pour repérer les signaux inquiétants.
date: '2018-07-05T10:36:03.488Z'
categories: []
keywords: []

---

![](/img/2018/hitchhikerguide/cover.jpeg)

Vous voulez investir dans une ICO, or acheter des cryptomonnaies déjà sur le marché ? Bienvenue à bord ! Avant de vous mettre à l’eau, je vous propose un petit guide pour vous aider à naviguer le Far-Ouest : il inclut des astuces et des exemples pris sur des projets existants. C’est en quelque sorte une synthèse de ce que j’ai appris de mes expériences (et échecs), et de mes échanges la communauté.

### Le Whitepaper est TOUJOURS la source la plus intéressante

Les whitepapers (WP pour le reste de l’article) peuvent faire peur. Bien que certains restent assez concis, d’autres peuvent atteindre une bonne cinquantaine voir centaine de pages. Malgré la taille, ils vous en disent long ! **C’est toujours la première chose que je regarde lorsque je commence à considérer sérieusement d’investir sur une crypto**. Alors, qu’est-ce qu’on y cherche dans ce fameux WP ?

#### Un Anglais irréprochable

Surprenant ? Pas vraiment si vous considérez la chose sous cette angle : **comment faire confiance à une équipe pour un développer projet décentralisé de grande envergure si elle n’est pas capable de sortir 20 pages sans fautes ?** Ça peut sembler petit, voir même mesquin mais croyez-moi : si vous y trouvez un Anglais douteux voir de nombreuses fautes, mieux vaut commencer à courir !

#### Des grandes promesses, quasi rien sur la technique

C’est probablement le plus fréquent, vu que la plupart des gens zappent la partie technique des WP (voir le WP tout entier). Même si vous n’y comprenez pas grand-chose, la différence entre un WP qui essaie d’étouffer ses mensonges et un autre plus transparent est assez facile à voir. [SFIcoin en est l’exemple parfait — NE PAS INVESTIR : ARNAQUE](http://www.sficoin.co/white-paper/white-paper.pdf), il coche presque toutes les cases du WP pipeau :

*   **Des grandes promesses vides** : « Le prochain système de paiement global »
*   **Des affirmations non sourcées / pas vérifiables** : leur WP détaille leur prétendue vision, leur roadmap, les cas d’usages envisagés mais il n’y a RIEN sur la tech.
*   **«On sera les premiers à X »**: cette phrase est un gyrophare à elle toute seule. Il n’y a aucune certitude dans le monde des cryptos.
*   **Un WP fait par des marketeux** (pour des marketeux) : beaucoup de visuels , un design plutôt soigné mais dans l’ensemble c’est vide de tout sens.

![stellar-wp](/img/2018/hitchhikerguide/stellar-wp.png)

Il est normal qu’un WP devienne technique à un moment donné (ici celui de Stellar — XLM particulièrement complexe), ce qui l’est moins c’est quand le langage technique est utilisé pour couvrir l’absence de fond.

#### Le Darwin Awards des whitepapers

Vous voulez un exemple du pire des whitepapers ? [Narbonne est un bon candidat](https://narbonne.io/Narbonne.pdf), je n’ai pas trouvé pire depuis l’avoir découvert il y a 7 mois. Sur les 22 pages du WP, environ 18 vous racontent des banalités sur le futur qui semblent être copiées/collées. L’ensemble du papier ne se mouille pas et reste très générique et simplement bizarre. Il y a tellement de choses à coté de la plaque, qu’il fallait choisir. Permettez moi de vous présenter le tableau comparant Narbonne, Wa**w**es et Ether**i**um. Oui vous avez bien lu, ils ont réussi à faire une faute sur « Ethereum » et « Waves ».

![narbonne-wp](/img/2018/hitchhikerguide/narbonne-wp.png) Comparaison très subjective faite par Narbonne vs Ethereum et Waves

L’ensemble du tableau est démontable, ce qui en fait un bon exercice. Je vous en donne quelques uns et vous laisse faire la suite :

*   “Bookkeeping at the blockchain” (impossible de traduire cette chose, désolé) — je suppose qu’il parle de traçabilité ? Il y a plein de projets qui s’en chargent sur Ethereum, comme par exemple [Request (REQ)](https://request.network/).
*   “Mobile Banking”: un projet comme [OmiseGo](https://omisego.network/) fait déjà ça très bien.
*   “AI, chatbot, voice control”: aucun intérêt pour le projet, qui est une infrastructure pour des banques. Par contre c’est des beaux buzzwords, ce qui explique sans doute leur présence.

#### À quoi ressemble un bon whitepaper ?

Un whitepaper est avant tout un **document technique**, il couvre généralement :

1.  La vision de l’équipe pour le projet et quel problème leur solution résoudra,
2.  Un aperçu des solutions techniques envisagées pour répondre au problème, et pourquoi elles ont été choisies,
3.  Les détails techniques de l’implémentation des solutions proposées,
4.  Une roadmap crédible,
5.  Des détails techniques sur le token (type, quantité, mécanismes…),
6.  Des détails sur l’ICO s’il y en a une.

Pour vous faire la main, rien de mieux que l’original. Je vous invite vraiment à lire [le whitepaper de Bitcoin écrit par le mystérieux Satoshi](https://bitcoin.org/bitcoin.pdf). Vous pouvez aussi aller voir par exemple :

*   [Le whitepaper d’Ethereum](https://github.com/ethereum/wiki/wiki/White-Paper) qui nous rappelle que quand le fond est solide, nul besoin de fioriture: c’est un wiki Github.
*   Les whitepapers de Cardano : il y a [un WP « philosophique »](https://www.cardano.org/en/philosophy/) et des [papiers académiques](https://www.cardano.org/en/academic-papers/). Je pense qu’ils arrivent bien à rendre accessible un projet très vaste à ceux que ça intéresse.

### Le mythe des transactions par seconde

Maintenant que les WP sont couverts, on passe à un autre gros morceau : les transactions par seconde (TPS).

#### Transaction par seconde : Un mensonge pratique

En bref, **les TPS ça ne veut rien dire**. Alors pourquoi on voit ça partout ? Et bien c’est un peu comme les GHz avec les processeurs — avant on ne voyait que ça dans les pubs aussi. D’une certaine façon ça se comprend : **cela donne l’impression** d’avoir un standard pour comparer des choses qui ne sont pas comparables. Plus c’est haut mieux c’est, non ?

Et bien non ! Prenez deux processeurs : un monocœur, 32 bits, cadencé à 3.5 GHz et un autre octocœur (ça en fait huit, comme la pieuvre), 64 bits et cadencé à 2 GHz. Devinez lequel offre le plus de puissance ? Les performances du second écrasent celles du premier.

C’est un peu la même chose avec les cryptos, sauf que cette fois-ci ce n’est pas qu’une question de puissance. Permettez moi un petit rappel en provenance de [mon précédent article](https://medium.com/@BBerdah/la-d%C3%A9centralisation-expliqu%C3%A9e-en-12-minutes-pour-monsieur-tout-le-monde-9804b056bad4) pour ceux qui l’auraient raté :

> Lorsque l’on fait le choix de décentraliser un système, ce n’est pas pour la performance. On le fait pour les avantages que la décentralisation apporte. Cela permet de créer de nouveaux types de services qu’on ne pouvait tout simplement pas créer sans décentraliser.

Bien que les TPS ne veulent rien dire, on les voit partout. Les investisseurs novices accordent une grande importance à cet indicateur pourtant trompeur. La plupart des projets se targuent d’un certain nombre de TPS. Parfait — cela nous donne un élément pour juger de leur honnêteté :

#### Utiliser les TPS pour lire à travers les lignes

Imaginez Acoin, qui se targue de supporter 1 million de transactions par seconde tandis que Bcoin n’en supporte que 10. Et la décentralisation dans tout ça ? La vision de l’équipe ? La communauté ? En regardant simplement le chiffre avancé, je sais déjà que Acoin est un shitcoin, tandis que Bcoin pourrait être sérieux.

![nano](/img/2018/hitchhikerguide/nano.gif)

**L’état de l’art actuel permet de supporter ~10 000 TPS pour les projets les plus avancés sans atteindre une centralisation excessive.** Tout coin qui promet plus fait des compromis ou manipule la vérité :

*   **Des compromis sur la décentralisation.** Le meilleur exemple est bien sûr [EOS et ses 21 «block producers »](https://medium.com/@CryptoPeterG/eos-centralization-problem-bd7a392eeed2) qui font la pluie et le beau temps sur le réseau.
*   **L’hypothèse de labo :** vous trouverez parfois des coins qui promettent des TPS de malade, dans les 100 000 ou plus et vous le prouvent avec un testnet. Seulement voilà il faut creuser un peu — le testnet n’a probablement que quelques noeuds. C’est facile de monter dans les TPS sur trois nœuds, mais ça devient de plus en plus dur quand les nœuds se multiplient.
*   Ils s’appuient sur des **solutions jamais testées à l’échelle**. [NANO](https://nano.org/en) utilise un nouveau type de ledger appelé block-lattice ce qui lui permet de supporter jusqu’à 7 000 TPS en conditions idéales. [IOTA](https://www.iota.org/) utilise une autre solution radicalement nouvelle, le Tangle pour atteindre ~800 TPS aujourd’hui mais potentiellement beaucoup plus. Ces deux projets sont essentiellement l’état de l’art actuel en terme de vitesse : n’importe quel projet qui promet des TPS supérieures sans apporter une solution radicalement nouvelle se paye votre tête.
*   **Ils comptent les mécanismes « off-chain »** dans leur calcul des TPS. Sans se perdre dans la technique, cet type de système conduit actuellement à une centralisation excessive. Retour au premier point.
*   **Ils comptent des mécanismes nouveaux et pas encore implémentés**, comme le sharding. Ethereum, qui a l’une des communautés de développeur la mieux fournie, aura encore besoin d’une ou deux années pour l’implémenter à grande échelle. Comment des inconnus pourraient le faire en 6 mois ?
*   Ils sortent tout simplement un nombre sans lien avec la réalité.

_Note : Les projets de cryptos commencent souvent de manière plutôt centralisée. Ce qui importe c’est que l’équipe en soit consciente et aie un plan pour ouvrir progressivement le réseau. Par exemple, maintenant que l’infrastructure de NEO commence à être bien établie,_ [_l’équipe avance vers de plus en plus de décentralisation_](https://neo.org/blog/details/4089)_._

Avant de conclure, on va faire un petit tour par le monde des ICOs : une jungle si dense qu’elle mérite sa propre section.

### Les signals d’alarmes des ICOs

#### Des promos massives pour ceux qui arrivent tôt

Une belle recette pour un coin qui se fait massacrer à l’entrée sur le marché, c’est des bonus massifs (>30%) pour les premiers investisseurs de l’ICO. Cela signifique que :

*   Comme les premiers ont eu les coins ristournés à 30% ou plus, cela **les pousse à les liquider au prix de vente de l’ICO (voir plus bas) le jour de la mise sur le marché** pour sécuriser autant de % de bénéfices gratuits et faciles, s’ils vendent assez vite.
*   Pourquoi avoir besoin de pousser autant la vente ? Souvent, cela cache **une cryptomonnaie qui n’a que peu d’utilité** et n’a donc pas lieu d’être.
*   Même si par miracle les deux situations au décrites plus haut n’ont pas lieu, il y un autre problème cette fois-ci garanti : les bonus attirent les baleines, les mecs qui possèdent des millions (de $$) d’une monnaie. Ces mêmes baleines posent de sérieux **problème pour la gouvernance et la décentralisation du projet**.

#### Pas de produit, pas de démo, pas de code

L’un des gros risques des ICOs ce que vous investissez essentiellement sur une idée ou une vision. Certains vont chercher les sous dès que le whitepaper est prêt, tandis que d’autres ne viennent pas les mains vides : démo, version alpha… Le second type de projet est bien plus sûr ! Si une démo/alpha existe, allez l’essayer avant d’investir.

Même si vous n’êtes pas développeur, rien ne vous empêche d’aller faire un tour sur le répertoire GitHub du projet. **Il est aisé de voir si une équipe est active ou non**, même sans regarder le code. Cette méthode est cependant très faillible car il est également facile de falsifier une apparence d’activité sur GitHub.

#### Une team à la ramasse

Si vous envisager sérieusement d’investir dans une ICO, je vous conseille vivement de prendre 15 minutes pour faire vos recherches sur les membres de l’équipe les plus importants. Allez voir leur LinkedIn, leur Twitter, ce qu’ils ont fait avant, etc. Si vous trouvez des profils inactifs ou peu garnis, c’est généralement mauvais signe. Vous trouverez peut être des choses intéressantes, comme l’implication d’un des membres de l’équipe dans un autre projet qui s’est avéré être une arnaque.

![L’équipe de [BANANO](https://banano.co.in), un fork de NANO qui ne se prend pas trop au sérieux](/img/2018/hitchhikerguide/team.png))
L’équipe de [BANANO](https://banano.co.in), un fork de NANO qui ne se prend pas trop au sérieux

Une présence sociale limitée ou de mauvaise qualité c’est un signe inquiétant. Ces gars que vous vérifiez, ce sont les mêmes qui vont devoir promouvoir un projet, trouver des utilisateurs et des partenaires. S’ils ne sont pas capable de se marketer eux-même un minimum, c’est mal parti pour le projet.

Un autre grand classique c’est **le fameux prestigieux conseiller (advisor)… qui n’a en fait rien à voir avec le projet**. Si le projet de vos rêves prétend avoir comme conseiller une figure qui pèse, assurez vous de la réalité du lien entre les deux. Si vous voyez Satoshi comme conseiller, vous pouvez commencer à courir !

#### Une répartition des tokens plutôt gourmande

Généralement vous trouverez dans les WP que vous lirez un graphique (le plus souvent notre bien aimé Camembert) qui résume la répartition des tokens prévue par l’équipe. Si il n’est pas là, cela revient à vous dire «_Je veux bien de ton argent mais tu ne sauras pas ce que je ferai avec_» . Vous commencez à connaître la musique, il est temps de se mettre à la course à pied !

Les projets les plus transparents vous proposerons même deux camemberts : un reprenant la distribution des tokens entre les différents acteurs, et un autre détaillant les dépenses.

![La distribution des tokens chez Storm ([source](https://blog.stormtoken.com/token-structure-and-ceo-update-bd055860251e))](/img/2018/hitchhikerguide/distribution.png)
La distribution des tokens chez Storm ([source](https://blog.stormtoken.com/token-structure-and-ceo-update-bd055860251e))

C’est normal que l’équipe garde une partie des tokens, et c’est même plutôt bénéfique pour la pérennité du projet. **Ce qu’il faut surveiller c’est la part qu’ils prennent : entre 10 et 30 % c’est plutôt classique.**

À l’inverse, il y a des projets comme Ripple (XRP) où la team s’octroie 60 % de l’ensemble des tokens. C’est un risque énorme pour ceux qui les achètent : déjà c’est un vecteur de centralisation. En outre, cela veut dire que l’équipe a tout ce qu’il lui faut pour manipuler le prix de sa monnaie comme elle le veut.

_Note : Il y a quelques mois, les gens ont commencé à faire entendre leur voix à Ripple précisément contre cette répartition gourmande. La team a donc mis en place un smart contract qui leur diffuse un milliard de tokens chaque mois,_ [_le reste (55 milliards de XRP) étant bloqué._](https://ripple.com/dev-blog/explanation-ripples-xrp-escrow/) _Ça ne résout rien au problème de centralisation._

_En outre, je suis curieux de savoir ce que l’équipe peut bien faire de $ 500 millions chaque mois (XRP actuellement à $ ~0.5). C’est censé être pour leur développement et pourtant ça ne va pas bien vite ! Enfin,_ **_comme ces tokens sont verrouillés, ils ne sont pas comptabilisé dans le stock en circulation (~39 milliards de XRP)_** _ce qui peut artificiellement rassurer les investisseurs les plus naïfs. En réalité il y a 100 milliards de token XRP. Point de vue purement personnel : l’ensemble de l’opération ressemble à un coup marketing assez malin mais aussi malhonnête vis à vis des investisseurs._

#### Conclusion

J’ai écrit cet article pour vous apporter quelques astuces pour repérer les projets douteux. J’espère que vous avez désormais bien compris que **plus vous vous renseignez avant d’acheter, plus vous minimisez le risque**. Je vous conseille fortement de NE PAS ACHETER SUR UNE IMPULSION. Même si c’est le meilleur projet du monde, il sera encore là demain. Entre temps vous allez peut être trouver des points de contention.

Pour finir, voici quelques petites astuces pour se faire une idée rapide sur un projet :

*   Une recherche google `site:reddit.com "nom du coin (+scam/shitcoin/issues...)"`. S’il y a des choses douteuses sur le projet, elle seront probablement déjà documentée sur Reddit. Ne vous fiez pas au subreddit de la crypto en question, Reddit devient de plus en plus tribal.
*   **Ne faites jamais confiance à une seule source, croisez les sans cesse !** Il y a des gens cupides qui promeuvent des projets douteux partout. Même un gars qui vous semble honnête et sympa (salut, tu veux mon 06 ?) peut tourner au vinaigre sans prévenir.
*   Il y a des services qui permettent à la communauté d’organiser sa petite enquête. [ICOCheck](https://icocheck.io/) semble plutôt fiable mais là encore ça ne vous dispense pas de faire votre propre recherche.

Enfin le dernier point mais pas des moindres : **je vous recommande très fortement de ne pas mettre un centime dans une ICO lors de votre première année sur le marché.** La plupart échouent brutalement. Vous vous en sortirez bien mieux en vous contentant des cryptos top 25/50/100 en fonction du risque que vous voulez prendre. Même parmi celle-ci il y a plein d’arnaques alors soyez prudents.

Amusez vous bien !

[Cet article est une publication originale d’EcoCrypto.fr, l’incorruptible publication crypto française bientôt référence.](https://ecocrypto.fr/vulgarisation/naviguer-le-cryptomonde-le-guide-pour-reperer-les-arnaques-et-shitcoins/)

PS : Si vous avez vos propres astuces que vous n’avez pas retrouvé dans cet article, n’hésitez pas à les partager en commentaire.
---
title: "Adieu au GHO Liquidity Committee et réflexions sur l'essor du novlangue DeFi"
description: "J'ai démissionné du GHO Liquidity Committee - cet article explique pourquoi et réfléchit sur les défis principaux observés dans la gouvernance et les comités DeFi"
date: '2024-02-08T01:13:50.191Z'
categories: [Projects]
tags: [DeFi, Ethereum, Decentralized Finance, Stablecoins, Liquidity, GHO, GHO Liquidity Committee]
url: farewell-glc
difficulty: "intermediate"
---

J’ai démissionné du GHO Liquidity Committee et je souhaite, dans cet article de blog, partager plus de contexte sur ses aventures et les leçons que nous pouvons en tirer.

* [Message onchain de tokenbrice.eth](https://etherscan.io/verifySig/35543)
* [Transaction de retrait du signataire](https://etherscan.io/tx/0x39760c8cd33beba102cbcb6a3c50489a24b1a50d8290de7c42c09845cf814dba)

Pour ceux dont la première réaction sera « pas envie de lire tout ça », voici un récapitulatif des principaux manquements que je vois dans le comité qui ont conduit à ma décision :

1. Le modèle opérationnel du comité est inefficace et empêche l'émergence et la mise en œuvre d'une vision cohérente.
2. Le champ de responsabilités du comité est flou, menant à une attitude passive (vis-à-vis des faux pas de gouvernance) assumée par la plupart des membres.
3. Le comité est principalement composé de professionnels de la gouvernance qui manquent de toute expertise sérieuse sur le sujet en question – la gestion de liquidité. Cela résulte en des opérations inefficaces, des conflits d'intérêts en raison de leurs nombreux autres engagements, et une utilisation sous-optimale des ressources du Comité.

La gouvernance est toujours un défi. En effet, cela peut sembler fou de donner du pouvoir à des gens aléatoires sur internet, et ça l'est souvent. Il y a une hypothèse démocratique intégrée dans les opérations de gouvernance – bien que la plupart des gouvernances soient purement plutocratiques – qui entrave sévèrement toute structuration sérieuse qui permettrait d'atteindre des objectifs communément acceptés. Le GHO Liquidity Committee a été nommé par la gouvernance Aave précisément parce qu'elle a reconnu – dans un éclair de lucidité – son incompétence et son ineptie en matière de gestion directionnelle de la liquidité.

Pourtant, je vais vous dire ce qui est encore plus fou : donner du pouvoir à des gens que la foule perçoit comme des « experts » sur un sujet. C'est tout un spectacle : l'expert le plus reconnu et médiatique d'un domaine donné n'est jamais celui qui est réellement le plus informé sur le sujet. Moi, pour ma part, je sais pas mal de choses sur la question, avec mon propre domaine de spécialisation — la gestion, la modélisation et l'incitation de la liquidité — un sujet prone à la manipulation de la perception publique plus que tout autre en raison des enjeux financiers inhérents associés.

## Le cas des CRV Wars

Illustrons : en matière de liquidité, le mot dans la rue est que Curve est le meilleur modèle, et que tous les pros et experts utilisent Curve, non ? **C'est si bon que lors du dernier round (62), les projets dépensent 1 $ pour recevoir 0,7 $ d'incitations pour leurs pools** : une donation instantanée de 30 % du montant qu'ils dépensent en pots-de-vin aux détenteurs de veCRV/vlCVX. Cela signifie que si les projets qui ont corrompu avaient alloué le même montant à un mining de liquidité direct, ils auraient délivré 30 % de plus $ à leurs LPs et ainsi attiré plus de liquidité pour le même coût, tout cela sans assumer le risque de prix associé aux fluctuations de CRV pendant une semaine.

![curve-bribes](img/2024/farewell-glc/votium-round-62.png)

Alors, que se passe-t-il là ? Pas mal de choses, et ce n'est pas le plat principal du menu d'aujourd'hui, juste l'entrée, donc je vais passer rapidement là-dessus :

1. **La plupart des projets n'ont personne en interne compétent en liquidité**, donc ils font souvent des gaspillages aléatoires comme ceux-ci. De nombreux projets DeFi proéminents reconnus pour les jeux de liquidité sont de gros dépensiers mais pas exactement astucieux.
2. **Les Curve Wars sont un meme depuis un moment** : il n'y a pas eu de véritables nouveaux entrants dans ces guerres depuis des lustres – simplement parce que ce n'est pas rentable financièrement pour la plupart des joueurs, surtout ceux sans liens avec l'écosystème Curve. De plus, les structures de liquidité disponibles sur Curve (stableswap et V2) sont sous-optimales par rapport à Uniswap ou Maverick pour de nombreux types très courants de tokens DeFi – LSDs, LRTs, stablecoins loosely peggés, et wrappers liquides. Vous pouvez marquer en toute confiance tout protocole produisant un token de ce type construisant sa liquidité principalement sur Curve comme inapte en gestion de liquidité.
3. Ce qui reste sont des **« protocoles insiders »**, des équipes construisant sur l'écosystème Curve qui possèdent généralement des positions veCRV/vlCVX importantes, leur permettant de récupérer une grande part de leurs pots-de-vin (1. Posséder veCRV/vlCVX ⇒ 2. Poster un pot-de-vin ⇒ 3. Voter sur le pool que vous venez de corrompre ⇒ 4. Collecter et répéter au round suivant). Cette tactique manipule la perception publique en faisant croire que de l'argent réel est dépensé dans ces guerres Curve. Certains de ces insiders sont à l'origine des protocoles externes, comme Inverse ou Alchemix, qui ont décidé d'embrasser l'anneau du lama pour le meilleur et pour le pire.

Ne me croyez pas sur parole ; regardez simplement les top dépensiers : Frax, Convex, Alchemix, CLever (Aladin), Prisma, Conic, Inverse, etc. **Pour faciliter la visualisation, voici les top dépensiers du dernier round, classés par montant dépensé, avec les protocoles insiders surlignés en rouge** :

![curve-bribes](img/2024/farewell-glc/top-bribers.png "Top pots-de-vin dans l'époque Votium CRV 62")

Assez avec Curve, les lamas me détestent déjà ; je voulais juste souligner l'exemple de Curve, « le roi de la liquidité », étant un lieu peu efficace pour construire et maintenir la liquidité. Curve, « faiseur ou briseur de stablecoins », en tant que DEX avec des structures de liquidité sous-optimales pour la plupart des pools de stablecoins : **Le novlangue est arrivé en DeFi, et la perception publique/les mots utilisés sont souvent complètement en désaccord avec la réalité observable onchain**. Malheureusement, un pattern similaire a été observé avec le GHO Liquidity Committee, le sujet d'aujourd'hui, donc passons-y.

## Le cas du GHO Liquidity Committee

**Le GHO Liquidity Committee est un exemple parfait de mauvaise attribution d'expertise**, car il était composé d'un mélange malsain de « politiciens DeFi » professionnels (plus sur cela ci-dessous), de personnes avec une faible expertise et un intérêt vested dans un DEX donné, et de personnes proches de la DAO Aave / ex équipe Aave mais dépourvues de toute expertise sur le sujet de la liquidité.

Cela a conduit à un gaspillage de ressources, des luttes sans fondement, et des décisions heavily mal informées. Au final, le **GLC est comme un gros sac d'argent que tout le monde essayait de tirer pour diriger vers un protocole dans lequel ils ont un intérêt**.

Plongeons-y : quelles étaient ses limitations, et qu'est-ce que quiconque intéressé par la gouvernance, basée sur un comité ou non, peut en apprendre ?

### Modèle opérationnel du GLC

Dans ses premiers mois, le GLC opérait de manière erratique, menant parfois plusieurs initiatives qui étaient en désaccord les unes avec les autres et qui avaient besoin d'une vision plus cohérente. C'était simplement un groupe de degens avec une grande quantité de GHO dans un multisig **qui sprayait et priait**. Le summum a été atteint quand des pots-de-vin ont été alloués à un pool dont la forme de liquidité était préjudiciable aux efforts de repegging, qui, heureusement pour le Comité, s'est retrouvé hors range avant que les émissions ne commencent, permettant sa terminaison prompte : un net burn de GHO.

J'ai finalement été élu chef du comité et [ai assumé une dictature temporaire et basée sur des objectifs](https://x.com/TokenBrice/status/1719328410479059227?s=20). Cela a permis au comité d'arrêter d'allouer des ressources sur un soutien de liquidité qui faisait un disservice à la cause du repegging de GHO et **de concentrer l'énergie, les ressources et les efforts là où cela comptait vraiment.**

Pourtant, l'histoire a aussi soulevé des sourcils et attiré l'attention des médias ([CoinDesk](https://www.coindesk.com/business/2023/11/28/aaves-gho-stablecoin-nears-elusive-dollar-peg/), [DeFiant](https://thedefiant.io/benevolent-dictator-succeeds-in-bringing-aave-s-stablecoin-gho-near-parity-with-usd), etc.) car elle soulignait l'échec de la gouvernance par elle-même – du moins du point de vue desdits médias. **Pendant mes deux mandats, deux objectifs ont été fixés : le premier a été manqué de quelques points de base (après une augmentation de ~200 bps), et le second a été manqué de quelques jours**. Mes objectifs étaient ambitieux, surtout en considérant qu'ils reposaient autant sur des livrables externes au comité de liquidité (gestion des taux d'intérêt, staking single-sided pour GHO, etc.). Après deux mandats, j'ai laissé tomber le rôle de leader début janvier.

⇒ Quand la gouvernance élit un comité pour gérer une tâche spécifique, elle reconnaît son inefficacité sur la question. **De tels comités ne devraient pas hésiter à nommer un leadership, car la propriété et la responsabilité peuvent être très saines,** surtout dans les gouvernances « décentralisées » où les éminences sont souvent grises, et donc la propriété et la responsabilité souvent manquantes.

### Champ d'application du GLC

Le GLC a hérité de plusieurs « dettes de gouvernance » : des décisions prises par la gouvernance qui s'avèrent absolument indéfendables dans l'état actuel des choses et des opérations. Il a même échoué à trouver la volonté de les contester et a plutôt décidé de les appliquer malgré l'avertissement de quelques membres du comité.

Exemple : Mobiliser le CRV du comité en tant que sdCRV, une option sous-optimale au niveau technique, car elle nécessite un vote hebdomadaire du comité (pas de report de vote), a une faible liquidité, et prive le comité de son pouvoir de vote de gauge CRV dû sauf s'il possède veSDT / bénéficie d'une délégation de boost veSDT, tout cela dans un beau désordre éthique, car cela renforce les liens avec un protocole/équipe qui opère avec de nombreuses pratiques questionable et plusieurs membres du comité sont détenteurs de veSDT et proches de ladite équipe.

{{< notice note >}}
⇒ Le champ d'application de tout comité nommé doit être clairement défini – et le comité devrait être capable et disposé à contester les décisions précédemment prises par la gouvernance sur son domaine d'expertise.
{{< /notice >}}

### Ce que signifie « professionnalisme » en novlangue DeFi

Les participants à des groupes comme le GHO Liquidity Committee sont censés être des « professionnels » — vous, chers lecteurs, et moi comprendrions par là : maîtres de leur sujet, précis, toujours essayant de servir le but du comité, et disponibles pour leur mission.

Mais nous sommes mal placés, car en novlangue DeFi, « professionnalisme » a un sens entièrement différent ; c'est en fait l'opposé, car les profils « professionnels » DeFi tendent à :

* Ne pas faire de vagues, et éviter tout ce qui est perçu comme « politique », même si cela signifie associer avec des escrocs : vous ne pouvez pas mettre des partenaires commerciaux dans une position difficile.
* Faire taire les vérités difficiles à avaler mais qui seraient d'intérêt public pour permettre à la communauté d'apprendre des erreurs passées. Par exemple, **l'échec des développeurs de GHO à anticiper le depeg n'est jamais discuté**. Cependant, il avait été attendu par beaucoup – moi inclus — jusqu'à un an avant le lancement de GHO. Le modèle de taux d'intérêt et l'absence d'une option de staking single-sided pour GHO au lancement étaient tous deux des manques évidents que tout développeur de stablecoin compétent aurait dû anticiper et résoudre **avant le lancement**.
* Utiliser des structures comme le GLC pour promouvoir le protocole dans lequel ils ont des intérêts vested par tous les moyens possibles, même si cela signifie arriver à des situations qui, si décrites honnêtement, qualifieraient de conflits d'intérêts.
* Démontrer, par leurs initiatives onchain et la communication qu'ils partagent dans des groupes privés, une compréhension approximative, sinon manquante, du sujet de leur expertise.

{{< notice note >}}
⇒ Les participants à la gouvernance devraient apprendre à mieux placer leur confiance. Grâce à leurs plateformes existantes, les figures les plus visibles publiquement sont généralement sélectionnées quand les comités sont élus.
{{< /notice >}}

Ma présence dans ce comité était une anomalie qui a émergé par nécessité, car la gouvernance savait qu'une compréhension profonde de la modélisation de liquidité, surtout Maverick, était nécessaire pour donner au GLC les meilleures chances de succès. De nombreux experts réels traînant autour des forums de gouvernance et des Discords restent impuissants malgré leurs connaissances et bonnes intentions simplement parce qu'ils ne sont pas des figures bien connues en DeFi.

### L'essor des politiciens DeFi et ses conséquences

La gouvernance est un théâtre. Quiconque impliqué en DeFi le sait, mais même moi j'ai été surpris de réaliser l'étendue de la scénarisation des interactions de gouvernance. Tout comme en politique IRL, où nous avons des politiciens professionnels dépourvus d'expertise sur les sujets qu'ils gèrent, nous observons le même phénomène en DeFi, où une caste de politiciens assume une responsabilité croissante sur diverses DAOs.

**De tels profils se spécialisent dans les opérations liées à la gouvernance et opèrent exactement comme les spécialistes PR IRL : leur soin principal est sur la perception publique et comment la manipuler pour atteindre leur but** (généralement obtenir l'allocation d'un budget important de la DAO à leur structure de gouvernance). La discussion de gouvernance ne se passe pas publiquement sur le forum — le forum n'est qu'une scène. Les discussions réelles se passent en coulisses : dans des appels, des réunions IRL, et des DMs. Les discussions sur le forum sont évitées autant que possible, surtout si elles sont anticipées comme controversées. Le forum est simplement là pour enregistrer des matters précédemment et privément discutés : regardez les conversations sur la plupart des propositions : elles paraissent si fausses que, à ce stade, on pourrait suspecter que des bots parlent entre eux, ce qui me rappelle une fois de plus la politique IRL. Cela m'est arrivé plusieurs fois qu'un tel profil me contacte alors que je tapais une réponse à leur post de gouvernance, essayant d'éviter toute forme de discours public :

![typing](img/2024/farewell-glc/gov-typing.png)

{{< notice note >}}
⇒ Les politiciens DeFi confirmés (= ceux qui gagnent leur argent principalement/seulement via des activités liées à la gouvernance) devraient simplement être interdits de participer à toute structure ayant même un pouvoir distant – car ils sont le fléau de la décentralisation, le diable en Prada de la DeFi. La professionnalisation de la gouvernance est synonyme de sa capture et donc de sa centralisation.
{{< /notice >}}


## Mots de la fin

Comme [Hayden le dit](https://x.com/haydenzadams/status/1710510768469237827?s=20), **la gouvernance se trouve au bas de la liste des tiers en termes de décentralisation et devrait donc être une solution de dernier recours.** Non seulement elle est inefficace, mais elle est aussi simplement trop prone à être manipulée, et la probabilité que cela arrive augmente avec le pouvoir et les ressources que la gouvernance gère. **Une fois qu'une gouvernance donnée a suffisamment grandi, sa corruption est simplement inévitable**, du moins sous le modèle de gouvernance plutocratique dominant actuel : 1 token = 1 vote, bonjour l'âge de pierre de la gouvernance où nous semblons être coincés depuis cinq ans.

Pour conclure, permettez-moi une dernière analogie avec la politique IRL puisque nous avons établi que des acteurs similaires participent à la gouvernance DeFi. Les professionnels de la gouvernance adorent rejeter des idées parce qu'ils les jugent « trop politiques ». Cela leur permet d'apparaître comme des figures raisonnables, non alignées. Pourtant, **le non-alignement n'existe pas : chaque décision est politique**. Ceux qui disent le contraire tendent généralement à être positionnés à l'extrême-centre du spectre : un alignement maximaliste brutal du profit enveloppé dans un costume de neutralité douce, aka l'équivalent DeFi d'un Emmanuel Macron.

En ce qui concerne les comités nommés par la gouvernance, il est peu probable que je participe à un autre après celui-ci – sauf si son champ d'application est clairement défini et qu'il est donné les moyens de contester les décisions sous-optimales de la gouvernance.
---
title: "Est-ce une Renaissance du Lending ?"
description: "De nouveaux modèles sont explorés à la fois pour les protocoles CDP et les marchés monétaires, et certains protocoles fusionnent même les deux en un seul : est-ce une renaissance des protocoles de prêt ?"
date: '2024-07-01T01:13:50.191Z'
categories: [Lending]
tags: [DeFi, Ethereum, Decentralized Finance, Stablecoins, Money Markets, Liquity, Tapioca, Dyad, BOLD, LUSD, LQTY, Aave, Morpho, Interest Rate]
url: lending-protocol-renaissance
image: img/2024/lending-protocol-renaissance/0-lending-protocol-renaissance-cover.png
difficulty: "intermédiaire"
---

Au cours des derniers mois, nous avons vu une avalanche de protocoles de prêt novateurs et excitants arriver sur le marché, tels que Morpho, DYAD, Fluid ou Tapioca ; encore plus sont attendus dans les mois à venir, comme Liquity V2 (Bold) ou Euler V2. Tous sont innovants, dans l'arène, essayant des choses au point que je me demande si nous ne vivons pas une renaissance des protocoles de prêt après quelques années à ressasser les mêmes concepts.

Ainsi, dans cet article, j'aimerais vous faire un tour des idées intéressantes que j'ai vues être explorées — nous passerons en revue certains des protocoles mentionnés ci-dessus et, pour chacun, nous nous concentrerons sur la compréhension de leur innovation principale.

## Protocoles de Position de Dette Collatéralisée (CDP) vs Marché Monétaire

Plongeons-y, en commençant par un rappel sur les différences entre les protocoles CDP (ex : Maker ou Liquity) et les marchés monétaires (ex : Aave ou Morpho). Cela sera utile car nous discuterons des deux dans cet article et nous finirons même avec un projet fusionnant les deux modèles en un seul protocole.


<table>
  <tr>
   <td>
   </td>
   <td><strong><em>CDP (ex : Liquity)</em></strong>
   </td>
   <td><strong><em>Marché Monétaire (ex : Aave)</em></strong>
   </td>
  </tr>
  <tr>
   <td><em>Taux d'Intérêt pour l'Emprunteur</em>
   </td>
   <td><em>Prévisible, peut même être fixe ou frais d'initiation seulement</em>
   </td>
   <td><em>Volatile, entièrement dépendant de l'utilisation du pool</em>
   </td>
  </tr>
  <tr>
   <td><em>Collatéral Accepté</em>
   </td>
   <td><em>Options généralement limitées, ne peut pas mélanger les collatéraux</em>
   </td>
   <td><em>Collatéraux variés : une position donnée peut mélanger plusieurs collatéraux à la fois</em>
   </td>
  </tr>
  <tr>
   <td><em>Actifs qui Peuvent Être Empruntés</em>
   </td>
   <td><em>Seulement le stablecoin du protocole (DAI sur Maker, LUSD sur Liquity)</em>
   </td>
   <td><em>Divers – tout actif activé comme actif empruntable</em>
   </td>
  </tr>
  <tr>
   <td><em>Ré-hypothéque du Collatéral</em>
   </td>
   <td><em>Aucune</em>
   </td>
   <td><em>Les collatéraux sont déposés dans un pool et donc potentiellement re-prêtés à d'autres utilisateurs</em>
   </td>
  </tr>
  <tr>
   <td><em>Défi Principal du Protocole</em>
   </td>
   <td><em>Stabiliser le stablecoin produit & sécuriser suffisamment de liquidité sur celui-ci</em>
   </td>
   <td><em>Attirer suffisamment d'actifs empruntables (USDC, ETH) pour satisfaire la demande d'emprunt</em>
   </td>
  </tr>
  <tr>
   <td><em>Risque Principal du Protocole</em>
   </td>
   <td><em>Défaillance de l'oracle ⇒ valeur du collatéral non évaluée précisément ⇒ certains utilisateurs peuvent emprunter plus que la valeur de leur collatéral ⇒ spirale de mort du stablecoin</em>
   </td>
   <td><em>Défaillance de l'oracle ⇒ valeur du collatéral non évaluée précisément ⇒ certains utilisateurs peuvent emprunter plus que la valeur de leur collatéral ⇒ tous les actifs empruntables sont drainés</em>
   </td>
  </tr>
</table>


Les protocoles CDP se distinguent par leur capacité à faciliter des coûts d'emprunt moins chers, stimulant ainsi plus de demande du côté des emprunteurs, un exploit difficile à réaliser. Cela est dû à la caractéristique unique des CDP, où l'utilisateur contracte directement une dette contre le protocole, éliminant le besoin de sourcer et de payer un déposant de stablecoin externe exigeant un taux d'intérêt compétitif, comme c'est le cas avec un marché monétaire comme Aave. Le défi principal avec les CDP réside dans la stabilité et la liquidité du stablecoin produit.

D'un autre côté, les marchés monétaires tendent à être plus flexibles. Grâce à leur structure, ils permettent aux utilisateurs de mélanger et d'assortir les collatéraux et peuvent rapidement intégrer de nouveaux. Pourtant, ils tendent à nécessiter plus de maintenance, car les paramètres des collatéraux doivent être constamment ajustés pour refléter les réalités du marché. Cela crée une charge assez importante pour la gouvernance, comme vu sur Aave, où [plus de mille propositions](https://boardroom.io/aave/overview) ont déjà été traitées en quatre ans et demi : environ 22 par mois. Ça fonctionne, mais ça semble sur-ingénierie ; il doit sûrement y avoir une meilleure façon.

## DYAD : Flirter avec le tabou du collatéral endogène

Dyad est un protocole CDP qui implémente plusieurs idées novatrices, comme délivrer un emprunt gratuit à ses utilisateurs, qui doivent posséder un NFT pour participer (Note). Il sert également de couche de coordination de base du protocole. Je vous invite à [lire la documentation](https://dyad.gitbook.io/dyad-docs-v2/) pour vous familiariser davantage avec lui. Concentrons-nous aujourd'hui sur l'approche novatrice de Dyad pour gérer un sujet clé pour les protocoles CDP : la sur-collatéralisation.

{{< notice info >}} Pour les stablecoins, on parle de collatéral endogène vs exogène. Pour le savoir rapidement, posez-vous cette question : si le stablecoin échoue, le collatéral échoue-t-il aussi ? Si oui, votre collatéral est endogène (ex : mes bien-aimés & défunts [stablecoins basés sur seigniorage](https://tokenbrice.xyz/posts/2021/seigniorage-basis-vs-esd/)) ; si non, il est exogène (ex : ETH pour Liquity). {{< /notice >}}

Les stablecoins utilisant un collatéral endogène ou aucun collatéral peuvent scaler rapidement, comme vu avec ESD, Basis Cash, ou Terra/UST. Cependant, ils peuvent et généralement explosent encore plus vite. Pour cette raison, utiliser un collatéral endogène est considéré comme une pratique risquée – digne d'un Red Flag / F instantané sur l'agence de notation de stablecoins [Bluechip](https://bluechip.org/).


![1-endogenous-collateral-bluechip](img/2024/lending-protocol-renaissance/1-endogenous-collateral-bluechip.png "Red Flags sur Bluechip")


Ce sur quoi j'aimerais me concentrer aujourd'hui concernant Dyad est son token utilitaire, KEROSENE, qui est un mécanisme pour allouer le droit de mint contre le surplus de collatéral existant dans le système. Par défaut, le ratio de collatéralisation minimal du système est de 150 %. Cependant, les détenteurs de KEROSENE peuvent le déposer dans leurs Notes pour réduire leur ratio de collatéral exogène à 100 %.

Ainsi, KEROSENE n'est pas techniquement un collatéral endogène mais un mécanisme pour pricer et permettre aux utilisateurs d'utiliser la sur-collatéralisation exogène du protocole. L'utilité de KEROSENE lui donne une « valeur déterministe » correspondant à son utilité lorsqu'il est déposé dans une Note. Puisque KEROSENE est principalement farmé en fournissant de la liquidité sur DYAD, cela pourrait entretenir un volant d'inertie intéressant.

![2-dyad-defillama](img/2024/lending-protocol-renaissance/2-dyad-defillama.png "TVL de Dyad sur Defillama")

Lancé à la fin de l'année, le protocole a vu une croissance douce et régulière, bien que encore limitée. Le déploiement est progressif : les fonctionnalités de base sont live (Note, minting de DYAD, incitations LP, utilité KEROSENE), mais beaucoup plus arrive : sDYAD, momentum (un mécanisme pour mieux aligner les participants du protocole), un marché de prêt, etc. Ça vaut la peine de suivre pour tout amateur de stablecoin comme moi.

## Liquity v2 – Le taux de base de la DeFi

Le LUSD de Liquity reste l'un des stablecoins décentralisés les plus réussis sur le mainnet, donc quand la v2 a été annoncée, elle a attiré beaucoup d'attention. Après avoir recherché une approche novatrice utilisant un modèle de réserve, l'équipe a pivoté vers un protocole CDP, grandissant des leçons de la première itération. La v2 est attendue pour la fin de l'année.

Aujourd'hui, je veux me concentrer sur un aspect en particulier, la gestion des taux d'intérêt.

La gestion des taux d'intérêt est cruciale pour tous les protocoles de prêt, même les protocoles CDP. Le taux peut être facilement défini en fonction du taux d'utilisation du marché sur les marchés monétaires. Pour les protocoles CDP, répliquer une approche similaire est impossible, et d'autres voies doivent être explorées ; plusieurs l'ont été :

* Défini par la gouvernance (ex : Maker / DAI) : bien que cette approche offre de la flexibilité, elle génère de l'incertitude pour les emprunteurs et des défis en gouvernance.
* Algorithmique (ex : Liquity / LUSD) : pas de gouvernance est toujours mieux, quand possible ; cependant, cela ne vient pas sans inconvénients non plus. Dans le cas de Liquity, les frais d'initiation fixés se sont avérés inflexibles, ce qui a conduit le protocole à s'ajuster à un environnement de taux d'intérêt plus élevé avec des redemptions et, ainsi, par une baisse de l'offre globale de LUSD.

Avec la v2, le protocole passe à un modèle de taux d'intérêt (plus de frais d'initiation), ce qui devrait déjà fournir plus d'agilité. Ce qui est plus intéressant est [comment ce taux d'intérêt est décidé : directement par les utilisateurs](https://www.liquity.org/blog/liquity-v2-why-user-set-interest-rates). L'équipe introduit un autre jeu au niveau du protocole avec des paramètres simples : les redemptions seront traitées en fonction du taux d'intérêt payé par l'utilisateur, du plus bas au plus haut.

Ainsi, les utilisateurs qui choisissent un taux d'intérêt très bas se mettent en première ligne pour les redemptions, tandis que ceux qui choisissent le plus haut seront protégés au maximum. Pour faciliter la participation de tout utilisateur, la délégation de taux d'intérêt sera possible, avec divers délégués délivrant différents mandats attendus au lancement.

Cela permettra au protocole de s'ajuster rapidement à tous types d'environnements de marché, des taux bas aux hauts, évitant les longues phases de redemption comme vues en v1 tout en restant immuable et en délivrant une plus grande prévisibilité aux emprunteurs.

![3-bold-stability](img/2024/lending-protocol-renaissance/3-bold-stability.png)

Au fur et à mesure que le protocole gagne en adoption, le taux d'intérêt moyen observé pourrait même informer au-delà de Liquity v2 lui-même, car il correspondra à un taux de base que les emprunteurs sont prêts à payer sur un protocole minimisant les risques et immuable. Les protocoles plus risqués devront offrir un taux d'intérêt plus bas pour attirer les emprunteurs. La v2 regroupe beaucoup d'autres innovations intéressantes. Pour vous mettre à jour, je recommande de vérifier [le thread des threads de Bojan](https://x.com/bjnpck/status/1772227278606389496).

## Tapioca – Convergence CDP x Marché Monétaire

Tapioca a été lancé il y a quelques semaines seulement et est encore en cours de déploiement progressif, car certains composants du protocole doivent encore être mis en live. Dans la mise en lumière d'aujourd'hui, j'aimerais me concentrer sur deux éléments principaux :

1. Convergence des modèles CDP et Marché Monétaire avec Tapioca
2. Le modèle innovant de verrouillage de token utilisé

Plongeons-y. Pour plus de contexte sur Tapioca, comme souvent, [la documentation officielle](https://docs.tapioca.xyz/tapioca) est une excellente source.

### Convergence de CDP et Marché Monétaire

Les protocoles CDP font face à un défi : ils doivent délivrer un rendement compétitif sur le stablecoin qu'ils produisent pour stimuler la demande. Liquity v2 redirigera la plupart des frais collectés, grâce au taux d'intérêt, aux stakers BOLD, Maker a le DSR / sDAI, etc.

Pourtant, une autre façon d'assurer que les minteurs de stablecoin peuvent accéder à des rendements compétitifs est de construire un marché monétaire sur le stablecoin : c'est précisément ce que fait Tapioca. En effet, Tapioca est essentiellement un double protocole.

D'abord, il y a le CDP—marqué « Big Bang », où les utilisateurs peuvent mint USDO contre un collatéral sélectionné : tokens gas et LSDs. La sélection de collatéral est volontairement restrictive, car les tokens acceptés ici affectent directement le backing d'USDO. Les emprunteurs paient un taux d'intérêt et, en fonction de la situation de peg d'USDO, potentiellement un frais d'initiation jusqu'à 1 % (si underpeg). Cela permet aux utilisateurs de loop-leverage leur exposition ETH / LSD ou simplement d'utiliser leur ETH / LSD comme collatéral pour emprunter de l'USDO.

Ensuite, il y a le marché monétaire — marqué « Singularity », qui fournit des marchés isolés où les utilisateurs peuvent fournir divers types de collatéraux pour emprunter USDO, fourni par les emprunteurs du côté CDP. Cela crée un rendement natif pour les détenteurs d'USDO qui est décorrélé du côté CDP, ainsi qu'une approche élégante pour gérer tous types de collatéraux :

* Majors résistants à la censure ⇒ collatéral CDP = backing USDO
* Dérivés / tokens plus risqués ⇒ Singularity = rendement aux détenteurs USDO sans compromettre le backing d'USDO.

Cette structure duale permet à Tapioca d'héberger divers collatéraux, avec des mesures de mitigation de risque appropriées pour chacun. Puisque singularity utilise des marchés isolés, le risque pour chaque collatéral intégré là est isolé, et il peut être géré davantage avec sa paramétrisation (LTV, taux d'intérêt, et bonus de liquidation) et des limites.

### twAML : un modèle innovant de verrouillage de token

Après avoir suivi et commenté les évolutions des DEX, commençant par veCRV et [les améliorations observées avec Velodrome (veNFT)](https://tokenbrice.xyz/crv-vs-velo/), j'anticipais de voir des modèles de verrouillage de token utilisés sur des protocoles de prêt aussi. Cela a été fait, mais seulement de manière primitive, avec des émissions basées sur gauge & verrouillage de token de gouvernance pour les allouer, comme vu sur Prisma.

Tapioca délivre enfin avec une approche excitante utilisant un nouveau type de verrouillage de token (twAML), à la fois pour leur token de gouvernance TAP et pour les fournisseurs du marché monétaire, pour sécuriser le côté supply et ainsi stimuler plus de demande d'emprunt. Ainsi, après que Velodrome ait amélioré le modèle veCRV et délivré la première amélioration crédible sur veCRV, nous pourrions voir sa troisième itération se concrétiser. Voici les points forts :


<table>
  <tr>
   <td colspan="4" ><strong><em>Aperçu Principal des Modèles de Verrouillage</em></strong>
   </td>
  </tr>
  <tr>
   <td><em>Nom</em>
   </td>
   <td><em>veCRV</em>
   </td>
   <td><em>veNFT (ex : veVELO)</em>
   </td>
   <td><em>twAML (ex : twTAP)</em>
   </td>
  </tr>
  <tr>
   <td><em>Signification</em>
   </td>
   <td><em>Vote Escrowed</em>
   </td>
   <td><em>Vote Escrowed NFT</em>
   </td>
   <td><em>Time Weighted Average Magnitude Lock</em>
   </td>
  </tr>
  <tr>
   <td><em>Position Verrouillée Représentée par</em>
   </td>
   <td><em>Aucune</em>
   </td>
   <td><em>NFT</em>
   </td>
   <td><em>NFT</em>
   </td>
  </tr>
  <tr>
   <td><em>Position Verrouillée Transférable</em>
   </td>
   <td><em>Non</em>
   </td>
   <td><em>Oui</em>
   </td>
   <td><em>Oui</em>
   </td>
  </tr>
  <tr>
   <td><em>Ratio TKN &lt;> veTKN</em>
   </td>
   <td><em>Uniquement dépendant de la durée de temps, un veTKN par TKN si verrouillage de 4 ans</em>
   </td>
   <td><em>même que veCRV</em>
   </td>
   <td><em>Dépend de twAML – la durée moyenne de verrouillage des autres verrouilleurs : si égal/supérieur, alors un veTKN par TKN</em>
   </td>
  </tr>
  <tr>
   <td><em>Décroissance veTKN &lt;> TKN</em>
   </td>
   <td><em>Oui, linéaire dans le temps (ex, après 2 ans de verrouillage, seulement 0,5 veTKN par TKN)</em>
   </td>
   <td><em>même que veCRV</em>
   </td>
   <td><em>Pas de Décroissance</em>
   </td>
  </tr>
  <tr>
   <td><em>Revenus pour les Verrouilleurs</em>
   </td>
   <td>
<ol>

<li><em>Part pro-rata des frais collectés sur Curve</em>

<li><em>Pots-de-vin potentiels</em>

<li><em>Revenus de boost LP</em>
</li>
</ol>
   </td>
   <td>
<ol>

<li><em>Rebase hebdomadaire ajouté au veNFT</em>

<li><em>Frais de la pool votée</em>

<li><em>Pots-de-vin potentiels</em>
</li>
</ol>
   </td>
   <td>
<ol>

<li><em>Intérêts USDO Accumulés </em>

<li><em>Parts de Profit de Liquidation</em>

<li><em>Frais de Création USDO</em>

<li><em>Frais de Mint Flash</em>
</li>
</ol>
   </td>
  </tr>
</table>




L'innovation principale réside dans la flexibilité et la couche supplémentaire de théorie des jeux que ce modèle implémente. Au lieu d'une correspondance linéaire veTKN à TKN, dépendant du temps verrouillé et maxant à quatre ans, comme avec veCRV et veAERO, twAML regarde la durée moyenne de verrouillage des autres verrouilleurs (pondérée par magnitude). En pratique, atteindre une correspondance 1:1 TKN&lt;->veTKN ne nécessite plus un verrouillage de quatre ans mais simplement de verrouiller pour autant / plus longtemps que les verrouillages existants. Ainsi, le temps de verrouillage augmentera rapidement pendant la première époque, passant du maximum initial de 4 semaines jusqu'à ce qu'il trouve un point d'équilibre et potentiellement commence à décroître.

![4-twTAP](img/2024/lending-protocol-renaissance/4-twTAP.png "Aperçu de twTAP")

Libéré pour la première fois avec un ajustement dynamique, le twAML a été rencontré avec une dégénérescence excessive et a rapidement dépassé les quatre ans. Ainsi, l'équipe est retournée au travail et a changé l'ajustement en basé sur époque. La nouvelle itération est attendue dans les semaines à venir, un autre développement à surveiller pour les amateurs de stablecoins et de tokens verrouillés.

Tapioca est un protocole assez costaud, deux ans de travail. J'ai à peine effleuré la surface ici, car il y a beaucoup d'autres composants dignes de commentaire :

* Il est nativement omnichain utilisant le standard de token fongible omnichain de Layer 0
* Tapioca, comme Liquity, sera l'un des rares protocoles CDP à rediriger les frais générés par le minting de stablecoin vers ses détenteurs de token via le modèle twTAP.
* Les récompenses pour les verrouilleurs USDO sont distribuées en oTAP, un token d'option connecté à la logique twAML.
* Le protocole est keen sur l'accumulation de Liquidité Possédée par le Protocole, à la fois pour TAP et USDO, ce qui lui permettra de baisser ses coûts de maintenance de liquidité et potentiellement de le transformer en une entreprise profitable.

Je voulais couvrir plus de protocoles, mais cet article est déjà costaud, donc je m'arrête là pour aujourd'hui. Il y a beaucoup de développements excitants pour les protocoles de prêt dignes de discussion, comme la croissance des marchés isolés avec des protocoles comme Morpho ou Silo. Tout cela et plus me font croire qu'après des années de domination d'Aave & Maker sur le paysage des protocoles de prêt, nous pourrions voir des challengers monter à une taille similaire, sinon les dépasser dans les années à venir.

Je surveillerai, et vous devriez aussi.

_Merci à Gray pour l'image de couverture._
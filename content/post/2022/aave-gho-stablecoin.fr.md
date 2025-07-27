---
title : "Le stablecoin GHO d'Aave peut-il aider le protocole à se développer davantage et à dépasser MakerDAO et DAI ?"
description : "On examine le design de GHO et anticipe ses principaux défis pour croître ainsi que de la valeur qu'il peut apporter à la DAO d'Aave."
date: '2022-08-22T01:13:50.191Z'
catégories : [DeFi, Understanding]
tags : [DeFi, Ethereum, Finance décentralisée, Stablecoins, Actifs stables, Marchés monétaires, Aave, GHO, Taux d'intérêt]
toc : true
tocNum : true
url : aave-gho-stablecoin
image: /img/2022/aave-gho-stablecoin/aave-gho-stablecoin-cover.png
---

Il y a quelques semaines, le concept du stablecoin GHO a été introduit sur le forum de gouvernance Aave et a déclenché une vague d'excitation à travers la DeFi. En effet, l'idée d'un stablecoin décentralisé, sur-collatéralisé, peg à l'USD et natif de la DAO d'Aave est une prochaine étape logique pour le protocole.

Dans cet article, nous examinerons le concept présenté avant de voir comment la DAO et l'équipe d'Aave pourraient le mettre sur le marché et en faire un stablecoin potentiellement aussi important que le DAI. Bien sûr, les informations sont encore rares, aussi la deuxième partie de l'article est fondée sur des extrapolations s'appuyant sur le modèle présenté et mon expérience en DeFi.

## Introduction à GHO, le stablecoin natif d'Aave

Depuis ses débuts, l'un des principaux défis d'[Aave](https://www.defiscan.info/protocols/aave/ethereum) a été d'attirer suffisamment de dépôts en stablecoin, car c'est le choix préféré de la plupart des emprunteurs. Ainsi, la création d'un stablecoin natif de la DAO est une prochaine étape naturelle et devrait également permettre de réduire les coûts pour les emprunteurs. Puisque ce stablecoin est minté, il devrait être plus économique à emprunter.

Plongeons donc dans les principales caractéristiques du GHO telles que présentées sur le forum de la gouvernance.

### Un stablecoin surcollatéralisé peg à l'USD

GHO sera un stablecoin surcollatéralisé, frappé en utilisant des aTokens comme garantie. Donc, dans un sens, c'est similaire à MakerDAO mais légèrement plus efficace puisque toutes les collatéraux seront des actifs productifs générant des intérêts (aTokens) - en fonction de leur demande d'emprunt.

En ce qui concerne la dénomination, il est également intéressant de voir qu'Aave n'inclut pas "USD" dans le nom. Compte tenu de l'agressivité des régulateurs américains, c'est probablement un avantage net d'un point de vue juridique. Cependant, cela ne semble pas être le seul facteur de décision, puisque le fondateur d'Aave, Stani, a fait allusion à un échange potentiel de devises plus tard :


> La référence à une devise a des limites sur le long terme, vous pourriez potentiellement vouloir échanger la parité d'un actif sous-jacent à un autre (pour diverses raisons) ou suivre quelque chose d'autre et être lié à un USD dans le ticker serait un facteur limitant. En plus de cela, tout le monde fait déjà cela, ce qui rend la situation un peu répétitive et restrictive du point de vue de la communication. DAI suit le même chemin en fait et a été utile pour construire un récit au fil des ans.
> - Stani sur [le post d'introduction de GHO d'Aave](https://governance.aave.com/t/introducing-gho/8730/27)


### Taux d'intérêt et remise stkAAVE

Le modèle de taux d'intérêt pour GHO est actuellement son composant le plus décevant, car le post initial envisageait un taux d'intérêt directement déterminé par la DAO d'Aave, tout comme cela fonctionne sur Maker. Cependant, cela serait inefficace et ajouterait une charge inutile à la gouvernance. 

Les réactions de la communauté dicteront la direction à prendre. Néanmoins, j'espère sincèrement pour Aave que le choix final se portera sur un modèle où le taux d'intérêt est déterminé algorithmiquement par les conditions du marché, tout comme pour les autres jetons sur Aave où l'offre et la demande sur le pool dictent le taux d'intérêt.

Si la communauté Aave estime qu'il est nécessaire d'impliquer la DAO dans la détermination du taux d'intérêt - une absurdité à mon sens puisqu'une DAO n'est absolument pas apte à gérer les paramètres opérationnels d'un système - alors un modèle hybride pourrait être envisagé avec un taux de base fixe voté par la DAO, et modulé dans une fourchette en fonction des conditions du marché.

En effet, l'évolution dynamique du taux d'intérêt peut aider à protéger le peg de GHO en dissuadant les événements de génération massive, tout comme [comment le baseRate fonctionne sur Liquity](https://docs.liquity.org/faq/lusd-redemptions#how-is-the-baserate-calculated) pour protéger LUSD d'un dé-peg vers le bas. Initialement, à 0,5%, les frais augmentent lorsque la demande augmente et diminuent progressivement pour revenir à 0,5% lorsque la demande se stabilise.

Le post mentionne également une réduction des frais pour les emprunteurs de GHO qui stakent des tokens AAVE, créant ainsi des synergies supplémentaires. Enfin, 100% des taux d'intérêt payés par les déposants iront à la DAO Aave (contre un facteur de réserve de l'ordre de ~10% pour la plupart des autres tokens), ce qui signifie que si GHO atteint une capitalisation significative, il pourrait devenir une mine d'or pour la DAO. **Avec une capitalisation similaire à celle de DAI, et un taux d'intérêt moyen de 3,5 % (hypothèse haute), la DAO gagnerait près de 150 000 $ par jour grâce au taux d'intérêt de GHO**.

J'ai réalisé quelques calculs rapides et un peu schématiques pour estimer le revenu potentiel pour la DAO d'Aave en fonction de la capitalisation de GHO et du taux d'intérêt moyen :

<table>
  <tr>
   <td><p style="text-align: center">Capitalisation de GHO</p>
   </td>
   <td><p style="text-align: center">Taux d'intérêt moyen</p>
   </td>
   <td><p style="text-align: center">Revenus annuels pour la DAO</p>
   </td>
   <td><p style="text-align: center">Revenus journaliers pour la DAO</p>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$1.5B (FRAX market cap)</p>

   </td>
   <td><p style="text-align: center">
1%</p>

   </td>
   <td><p style="text-align: center">
$15,000,000.00</p>

   </td>
   <td><p style="text-align: center">
$41,095.89</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$6.6B (DAI market cap) </p>

   </td>
   <td><p style="text-align: center">
1%</p>

   </td>
   <td><p style="text-align: center">
$66,000,000.00</p>

   </td>
   <td><p style="text-align: center">
$180,821.92</p>
   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$52B (USDC market cap)</p>

   </td>
   <td><p style="text-align: center">
1%</p>

   </td>
   <td><p style="text-align: center">
$520,000,000.00</p>

   </td>
   <td><p style="text-align: center">
$1,424,657.53</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$1.5B</p>

   </td>
   <td><p style="text-align: center">
3.50%</p>

   </td>
   <td><p style="text-align: center">
$52,500,000.00</p>

   </td>
   <td><p style="text-align: center">
$143,835.62</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$6.6B</p>

   </td>
   <td><p style="text-align: center">
3.50%</p>

   </td>
   <td><p style="text-align: center">
$231,000,000.00</p>

   </td>
   <td><p style="text-align: center">
$632,876.71</p>

   </td>
  </tr>
  <tr>
   <td><p style="text-align: center">
$52B</p>

   </td>
   <td><p style="text-align: center">
3.50%</p>

   </td>
   <td><p style="text-align: center">
$1,820,000,000.00</p>

   </td>
   <td><p style="text-align: center">
$4,986,301.37</p>

   </td>
  </tr>
</table>

Références du tableau :

1. GHO Marketcap : 1,5 milliards = l'offre actuelle de FRAX, 6,6 milliards celle de DAI, et 52 milliards celle de USDC - on peut rêver.
2. Taux d'intérêt moyen du GHO : 1% serait très compétitif, 3,5% dans la fourchette haute des taux habituels.


### Facilitateurs et RWA

La conception de GHO prévoit des "facilitateurs", embarqués par la gouvernance d'Aave, qui seraient en mesure de frapper le GHO. Le premier facilitateur serait le protocole Aave lui-même, mais d'autres suivront, qu'il s'agisse de protocoles ou d'entités. Cette partie est passionnante, car elle ouvre largement l'espace de conception du GHO. Après sa mise en circulation, nous pourrions voir d'autres protocoles demander à devenir des facilitateurs et construire sur Aave et GHO.


![gho-facilitators](/img/2022/aave-gho-stablecoin/gho-facilitators.png)


Il y a également des mentions explicites de positions sous-collatéralisées basées sur des références telles qu'un score de crédit. Chaque facilitateur aura une capacité maximale de frappe de GHO déterminée par la DAO.


### "Décentralisation" et absence de résistance à la censure

Le GHO est présenté comme un stablecoin décentralisé par l'équipe d'Aave, avec même quelques mentions de résistance à la censure. Cependant, elles ne sont jamais directement associée à GHO :

> L'utilisation des stablecoins ne fera que croître à mesure que les crypto-monnaies s'intègrent davantage à une base d'utilisateurs moins crypto-natifs. Les stablecoins décentralisés fournissent une monnaie libellée en fiat résistante à la censure sur la blockchain. Voici GHO, une monnaie stable multi-collatérale décentralisée, entièrement garantie et native du protocole Aave.

À moins que j'aie mal compris la conception, GHO sera **aussi "décentralisé" que DAI et aura une faible résistance à la censure** en raison de la composition de son collatéral. En effet, en supposant que tous les aTokens qui peuvent actuellement être utilisés comme collatéral pour emprunter sur Aave seront également utilisables pour emprunter GHO, la composition du collatéral de GHO sera dominée par des tokens censurables tels que USDC :


![aave-collateral](/img/2022/aave-gho-stablecoin/aave-collateral.png)


Source : [DeFiLlama](https://defillama.com/protocol/aave-v2)

En effet, si l'on exclut les stETH utilisés comme collatéral pour emprunter des ETH et s'exposer avec levier aux rendements du staking, l'USDC est le principal collatéral utilisé sur Aave, avec un autre token nécessitant de la confiance (wBTC) non loin derrière. **La composition du collatéral serait néanmoins bien meilleure que celle de DAI**, qui est soutenu à plus de 50 % par des USDC purs. 

![dai-collateral](/img/2022/aave-gho-stablecoin/dai-collateral.png "Plus de 75% du collatéral de DAI est désormais constituté de tokens censorables")

Une autre tranche de ~25 % de la garantie provient d'autres garanties requises par la confiance ou de positions fournissant de la liquidité réflexive (comme le DAI/USDC LP utilisé comme garantie pour frapper le DAI).

Pour plus d'informations sur la conception envisagée pour GHO, n'hésitez pas à lire [le message du forum sur la gouvernance](https://governance.aave.com/t/introducing-gho/8730) et les réponses.


## A quoi pourrait ressembler Aave avec GHO ?

Maintenant que le décor est planté en ce qui concerne le GHO, nous pouvons entrer dans un territoire plus spéculatif et examiner comment le lancement du GHO pourrait se dérouler en pratique.

En effet, l'interaction entre le protocole Aave et GHO est tout à fait passionnante à considérer : alors que le post initial mentionne Aave x GHO, ainsi que l'activation de l'eMode (permettant un effet de levier important sur des paires sélectionnées telles que USDC/DAI) sur GHO, il est assez maigre en détails, alors je vais devoir spéculer un peu.

aGHO serait un collatéral fascinant sur Aave, mais il pourrait également créer des risques réflexifs importants s'il est autorisé à emprunter GHO. Ainsi, **Je m'attends à ce que l'aGHO soit empêché de frapper des GHO** afin d'éviter une collatéralisation réflexive comme nous le voyons actuellement sur DAI.

Néanmoins, cela permettrait de créer des boucles d'arbitrage de stablecoin intéressantes, comme aUSDC > Mint GHO > aGHO > Emprunt d'un autre stablecoin. Avec l'eMode, cela ferait de Aave & GHO un protocole très efficace pour l'arbitrage de stablecoins. De plus, le taux d'intérêt du GHO deviendrait une sorte de "taux d'intérêt de base des stablecoins" et pourrait aider à contrôler le taux d'intérêt d'autres stablecoins comme l'USDC.


### Stratégie de liquidité du GHO

Une autre partie critique et essentielle de la conception de tout stablecoin est sa stratégie de liquidité. Puisque CRV, CVX, et BAL sont acceptés comme garantie sur Aave, il pourrait y avoir des choses passionnantes faites avec les CRV, CVX, et BAL accumulés par la trésorerie, grâce au facteur de réserve. Les verrouiller dans leurs protocoles natifs permettrait à la DAO d'Aave de diriger les incitations vers les pools impliquant au GHO.


![aaveDAO-treasury](/img/2022/aave-gho-stablecoin/aaveDAO-treasury.png "État actuel de la trésorerie d'Aave avec ~615K CRV")
Source : [Rapport sur la trésorerie d'Aave](https://governance.aave.com/t/aave-treasury-report/5575/37) (juillet 2022)

Tout comme Frax s'éloigne actuellement de USDT et DAI et tente d'établir la Frax Basepool (FRAX/USDC) comme paire de base sur Curve pour d'autres stablecoins, nous pourrions envisager un mouvement similaire de la part d'Aave. De plus, de nombreux projets actuellement exposés à l'USDC et au DAI cherchent à diversifier leurs liquidités. GHO pourrait arriver au bon moment pour permettre à DeFi d'être moins dépendante de l'USDC.

Cependant, alors que Frax contrôle un pouvoir de gouvernance et de vote important dans les Curve Wars, ce n'est pas le cas pour la DAO Aave. Les soldes actuels de la trésorerie CRV/CVX seront clairement insuffisants pour inciter les pools à atteindre le milliard de dollars, ce qui pourrait pousser la DAO Aave à envisager l'acquisition de plus de tokens CRV/CVX. Avec les revenus importants que la DAO percevra du taux d'intérêt de GHO, elle devrait avoir suffisamment de moyens pour soutenir une liquidité appropriée, quelle que soit la capitalisation de GHO.

Enfin, Aave a été historiquement proche de Balancer, avec la pool Balancer 80% AAVE / 20% wETH utilisé dans le module de sécurité depuis la transition vers le token AAVE. La trésorerie possède déjà 200k BAL et [un achat additionel de 100K BAL est prévu](https://governance.aave.com/t/arc-strategic-partnership-with-balancer-part-2/7813). Nous pourrions donc nous attendre à un jeu passionnant pour GHO sur Balancer. Pourtant, lorsqu'il s'agit de stablecoin, Curve reste à la fois le roi et le faiseur de roi : Je ne vois pas comment Aave pourrait faire croître suffisamment la liquidité de GHO sans s'impliquer d'une manière ou d'une autre dans [la guerre du CRV](https://tokenbrice.xyz/content/posts/2021/crv-wars.fr.md").

En plus des incitations du protocole de base (comme le taux d'intérêt d'emprunt dynamique ou géré par la DAO) et du mécanisme de liquidation, la stratégie de liquidité est probablement l'un des éléments les plus cruciaux pour un stablecoin, car elle a également un impact sur la façon dont l'ancrage est maintenu.


## Conclusion

J'espère que cet article vous a permis de mieux comprendre les enjeux de la guerre des stablecoins. La fin de l'année sera intéressante, avec la sortie du GHO qui approche et le stablecoin de Curve, également surcollatéralisé, dont la sortie a été annoncée avant la fin de cette année. La multiplication des stablecoins est une prochaine étape naturelle pour DeFi, car la plupart des protocoles établis voient leur conception converger :



* Frax a commencé comme un stablecoin seulement, a maintenant FraxSwap et bientôt FraxLend.
* Aave a commencé comme un marché monétaire, bientôt avec son propre stablecoin natif.
* Curve a commencé comme un DEX, mais l'ajout de son propre stablecoin pourrait bientôt permettre des emprunts efficaces pour les fournisseurs de liquidités.

En fin de compte, comme l'ont montré mes calculs rapides plus haut, la principale raison pour laquelle un protocole crée son stablecoin est assez évidente : c'est là où il y a le plus d'argent à faire, ainsi qu'une demande massive et une adéquation produit/marché.


{{< notice note >}}
L'"artiste" de l'image de couverture de cet article est une IA impressionnante (et légèrement effrayante) appelée [Midjourney](https://www.midjourney.com/). Elle a reçu le message suivant : Un fantôme lumineux, mignon et amical, frappant les pièces de sa propre monnaie dans un environnement cyberpunk, 4k, cartoon, détails complets, unreal engine. --ar 19:10`
{{< /notice >}}

---
title: "💦 Pools de Liquidité avec programmes d'incitation - La Tier List" 
description: "Une liste hiérarchisée qui présente différents **programmes d'incitation au dépôt de liquidité Balancer, Uniswap, et Curve Finance.**"
date: '2020-07-07T01:13:50.191Z'
categories: [DeFi, Practical]
tags: [DeFi, Ethereum, Prêts, Apports de liquidités, Actifs synthétiques, Balancer, Curve, Programme d'incitation, Liquidity Mining, Ampleforth]
toc: true
tocNum: true
image: /img/2020/yield-farmer-tier-list/cover.png-
---

La DeFi est comme un gâteau à plusieurs étages. Lorsque vous passez sa porte pour la première fois, faire un dépôt sur Aave et voir votre solde augmenter vous laisse bouche bée. Peu de temps après, grâce à vos propres recherches ou à vos discussions avec la communauté, vous vous rendez compte qu'il y a plus que cela **- il pourrait aussi y avoir une cerise sur le gâteau !**

Il existe de nombreuses façons d’obtenir des rendements sur un capital donné en utilisant la finance décentralisée sur Ethereum. **Aujourd'hui, nous excluons toute stratégie impliquant un effet de levier** - la manière la plus simple de réaliser un tel exploit. Il y a encore beaucoup de cultures de haute qualité à planter ! 

En effet, l'efficacité du capital augmente à un rythme rapide dans la DeFi grâce à de nouvelles primitives financières comme Compound, Balancer ou Curve. **Il est désormais possible d'atteindre jusqu'à trois niveaux de rendement**, et il existe des pools pour tous les différents profils de risque, allant d'une exposition à 100 % en stablecoin à une exposition à 100 % en ETH / tokens ERC-20.

**La guerre de la liquidité ne fait que commencer !** Suivez de près la gouvernance des protocoles dans lesquels vous êtes investi, c'est devenu encore plus crucial maintenant. En attendant, puisque la DeFi s'apparente de plus en plus à un jeu, permettez-moi d'importer un concept hérité de ce milieu : la tier list (liste des niveaux). 

Dans les jeux de stratégies ou de combat, on utilise des tiers lists pour établir une typologie des personnages/classes et un classement. Aujourd'hui, je vais rapporter ce concept à la DeFi pour organiser les pools de liquidité les plus intéressants en groupes cohérents.

## AVANT DE COMMENCER

ℹ À noter - Ce contenu suppose une compréhension de base du monde de la finance décentralisée sur Ethereum. Lisez les ressources d'introduction si c'est la première fois que vous en entendez parler :



1. Ce document ne couvrira pas les stratégies d'investissement de base de DeFi, détaillées dans le **[📖 Guide des services DeFinanciers](https://tokenbrice.xyz/content/posts/2020/definancial-services-guide.fr.md")**. 
2. Pour plus d'informations concernant les outils que vous pouvez utiliser pour mettre en œuvre et gérer ces stratégies, veuillez consulter la **[🧰 Trousse à outils du cultivateur DeFi](https://tokenbrice.xyz/content/posts/2020/defi-farmer-toolbox.fr.md)**.

**_Il ne s'agit pas de conseils en matière d'investissement et ce document ne doit pas être lu comme autre chose qu'une liste structurée de pools de liquidités avec programmes d'incitation._**

### Suggérez les vôtres !

Ce billet peut être un document vivant. N'hésitez pas à suggérer des pools avec incitation qui manqueraient. Si vous connaissez bien Github, **[vous pouvez faire une pull request](https://github.com/TokenBrice/blog/blob/master/content/posts/2020/yield-farmer-tier-list.md)**. Sinon, il vous suffit de prendre contact et de partager de la documentation sur le pool et son programme d'incitation.

Enfin, permettez-moi de faire la distinction entre :

1. **Liquidity Mining** : une action de base de la plateforme (telle que l'approvisionnement en liquidité) est récompensée par le token natif de la plateforme (ex : BAL sur Balancer)
2. **Programmes d'incitation à la liquidité** (Liquidity Incentive Program) : un pool de liquidité spécifique est éligible à des récompenses supplémentaires, par la mise en jeu des tokens du pool ou des distributions hebdomadaires (mercredi sur Balancer)

La bonne nouvelle, c'est que vous pouvez cumuler les deux ! Voyons comment.

---

![TokenBrice-Yield-Farmer-Tier-List-DeFi](/img/2020/yield-farmer-tier-list/yield-farmer-tier-list.png)

---

## Niveau 1 : Le tiercé DeFi

Tout en vous présentant les principales possibilités de gains que j'ai trouvées, je vous ferai part de considérations plus générales sur l'apport de liquidités sur Balancer, telles que des réflexions sur la pondération du pool pour vous aider à prendre des décisions en connaissance de cause.

Avant de poursuivre notre rêve le plus fou, le trio de rendement tant attendu, prenons donc une minute pour réfléchir à ce que cela implique. En ce qui concerne les rendements, la crème de la crème est généralement un pool de liquidité avec programme d'incitation, ce qui signifie qu'il est éligible aux récompenses liquidity mining BAL, en plus du programme d'incitation aux liquidités (et des commissions sur les swaps).

**Il y a exactement un pool Balancer qui répond à ces critères avec deux stablecoins** à ma connaissance, donc c'est par là que nous commençons :


### Pool Balancer 50% mUSD / 50% USDC

mstable[^1] est une méta-stablecoin. Vous pouvez aller sur leur application pour verrouiller vos USDT, USDC, DAI & TUSD pour frapper des mUSD. Une fois que vous possédez mUSD, plusieurs possibilités de retours sont disponibles.

La plus directe est la fonction "Save" de l'application mStable. Elle permet de verrouiller vos mUSD afin de générer un rendement grâce au prêt.

![mstable](/img/2020/yield-farmer-tier-list/mstable.png)

Il s'agit là d'un simple rendement qui ne méritera pas à lui seul un reportage ici. 

Cependant, c'est l'introduction parfaite au pool Balancer mUSD/USDC, notre premier tiercé de la journée. Qu'est-ce qu'un tiercé gagnant ? C'est assez simple : 3 couches de rendements :

1. **Commissions sur les swaps** : C'est un pool de liquidité qui facilite les transactions et qui rapporte des frais.
2. **BAL liquidity mining**- c'est un pool équilibré 50/50 avec une faible commission (5 bps) gagnant le montant maximum de BAL possible (facteur d'extraction = 1).
3. **[Programme d'incitation pool MTA](https://medium.com/mstable/introducing-meta-mta-mstables-protocol-token-6e1032291ccf)** programme sur ce pool.

| EXPOSITION | RÉCOMPENSES EN | DISPONIBLES DEPUIS | L1 APR | L2 APR | L3 APR / BUDGET INCITATIF |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 50 % USDC<br/>50 %mUSD | Native<br/>BAL<br/>MTA | 26 juin 2020 | Variable | ?? BAL | 50 000 MTA/semaine |

_Récompenses natives = gagnées dans le token que l'exposition de base (généralement une commission prélevée sur les transactions facilitées)_

À noter : Les ratios respectifs des quatre stablecoins soutenant le mUSD (la moitié de l'exposition) peuvent varier, allez à l'application m stable [^2] pour les visualiser :

![mstable-asset-distribution](/img/2020/yield-farmer-tier-list/musd.png)

Ce pool est particulièrement attractif car l'exposition est à 100% basée sur des stablecoins, malgré un rendement très solide grâce au ratio minier max BAL + le programme d'incitation payé dans le très attendu token MTA.

Note/Attention : 💬 Des discussions sont en cours dans le canal de gouvernance [Balancer Discord](https://discord.com/invite/ARJWaeF) pour abaisser le ratio d'exploitation du BAL sur les paires stablecoin/stablecoin, de sorte que les rendements du BAL seront probablement moins élevés à l'avenir._

### Pools 90/10 avec programme d'incitation 


#### Pool Balancer 90% SNX / 10% USDC 

Vous avez l'impression d'avoir raté la montée du SNX ? Pour les capitaux moyen (&lt ; 5000 SNX), il est peu judicieux de staker si l'on tient compte des coûts du gaz. Ce pool est une excellente alternative pour une exposition aux SNX avec un bon potentiel de rendement.

| EXPOSITION | RÉCOMPENSES EN | DISPONIBLES DEPUIS | L1 APR | L2 APR | L3 APR / BUDGET INCITATIF |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 90% SNX<br/>10% USDC | Native<br/>BAL<br/>SNX | 5 juin 2020 | Variable | 23 % pour un BAL à 10 $ | FAIT |

Ici, comme le pool est fortement orienté vers le SNX, le retour du BAL n'est pas maximisé. Vous vous souvenez du facteur 1 pour l'exploitation du BAL sur la pool mUSD ? Ici, il est de 0,36 : vous obtenez environ un tiers de la quantité de BAL que vous gagnez dans un pool à 50/50 et à faible frais. 

Cependant, les pools 90/10 sont très utiles pour minimiser fortement le risque de pertes impermanentes si vous pensez que le token a un grand potentiel d'appréciation.

Le [programme d'incitation sur ce pool est maintenant terminé](https://blog.synthetix.io/balancer-snx-usdc-liquidity-trial/), il est donc de nouveau un pool normal à deux-niveaux rendement.

#### Pools Balancer JRT

Le réseau Jarvis propose un programme d'incitation sur trois pools, tous à 90 % JRT + 10 % DAI, ETH ou USDC. Le modèle de récompense est similaire à celui du pool précédent :

| EXPOSITION | RÉCOMPENSES EN | DISPONIBLES DEPUIS | L1 APR | L2 APR | L3 APR / BUDGET D'INCITATION |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 90% JRT<br/>10% ETH, DAI ou USDC | Native<br/>BAL<br/>JRT | 17 juin 2020 | Variable | 23 % pour un BAL à 10 $ | 70 000 JRT/semaine |

[📖 Introduction au programme d'incitation](https://medium.com/jarvis-network/liquidity-program-with-balancer-db23aa0ce10)

Note : le prix du token JRT a été assez actif ces derniers temps. Faites vos propres recherches.

⚡ Mise à jour (_08 Juillet_): les JRT supplémentaires sont désormais distributés sur TOUTES les pools Balancer vérifiées (whitelisted):

### AMPL Geyser

L'AMPL est une bête à part entière, je vous invite donc à en lire plus [^3] avant de vous plonger dans celui-ci. Ici, l'exposition est de 50 % d'ETH et 50 % d'AMPL. En plus de vos commissions, vous avez droit à des AMPL supplémentaires & ainsi qu'aux habituels rééquilibrages d'AMPL (sur vos AMPL = 50 % du capital total).

| EXPOSITION | RÉCOMPENSES EN | DISPONIBLES DEPUIS | L1 APR | L2 APR | L3 APR / BUDGET INCITATIF |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 50 % ETH<br/>50 % AMPL | Native<br/>AMPL | 21 avril 2020 | Variable | Variable - Rééquilibrages AMPL | 36 911 AMPL/mois |

[📖 AMPL Geyser Incentive Program Introduction](https://www.ampltalk.org/app/forum/ampl-geyser-19/topic/about-the-geyser-21/)

L'impact des rééquilibrages peut être difficile à calculer. Ce tableur a récemment été créé pour [🧮 aider les investisseurs d'AMPL à calculer l'impact des rééquilibrages](https://www.publish0x.com/canuhodl/ampleforth-dollar-ampl-calculator-spreadsheet-for-investors-xmdjxvy) 

![ampleforth-geyser](/img/2020/yield-farmer-tier-list/ampl-geyser.png)

Le code du Geyser est audité [^4] et assuré sur Nexus Mutual [^5]. Le calcul de la récompense tient ici compte du temps mis en jeu - ce pool est donc le mieux utilisé sur le long terme.

---

## Niveau 2 : Combien de rendements peut-il y avoir ?

### Pools Synthetix avec programme d'incitation

Synthetix a été le pionnier des programmes d'incitation à la liquidité avec le premier pool Uniswap sETH/ETH (+SNX). Les pools Synthetix sont toujours très attractifs, nous allons considérer les deux pools les plus attractives :

Veuillez noter que le Curve token (CRV), l'une des récompenses pour l'exploitation des liquidités des deux pools présentés ci-dessous, n'est pas encore disponible. [Les mécanismes actuellement documentés du CRV] (https://github.com/curvefi/curve-dao-contracts/blob/master/doc/readme.pdf) peuvent être modifiés avant le lancement.

### L'OG : Pool Curve sUSD 

Tout comme le pool mUSD/USDC, ce pool est exposée à 100 % à des stablecoins, mais les récompenses sont payées en SNX. 

| EXPOSITION | RÉCOMPENSES EN | DISPONIBLE DEPUIS | L1 APR | L2 APR | L3 APR / BUDGET D'INCITATION |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 31,58 % USDT<br/>30,67% USDC<br/>24,62% suSD<br/>13,13% DAI | Native<br/>SNX | 22 avril 2020 | ~5 % | CRV (pas encore en ligne) | 48 000 SNX / semaine |

[📖Information sur le programme](https://blog.synthetix.io/new-curve-pool-launch/)

Ce pool est l'un des premiers programmes d'extraction de liquidités qui existe encore, mais il est encore très compétitif. Si vous avez lu mes précédents guides, vous le savez déjà [^6]. 

### La variante BTC-OG : Pool Curve renBTC/sBTC/wBTC

[curve-synthetix-balancer-ren-btc-pool](/img/2020/yield-farmer-tier-list/curve-btc.png)

Celui-ci est similaire au premier, avec des tokens différents. Ici, votre exposition aux prix est de 100 % en BTC, tandis que vos récompenses pour l'exploitation des liquidités sont constituées de quatre tokens DeFi : BAL, SNX, REN & CRV. 

| EXPOSITION | RÉCOMPENSES EN | DISPONIBLES DEPUIS | L1 APR | L2 APR | L3 APR / BUDGET INCITATIF |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 44,54% renBTC<br/>32,21% wBTC<br/>23,26% sBTC | Native<br/>SNX, REN, BAL & CRV | 19 juin 2020 | ~5 % | BAL<br/>CRV | 10 000 SNX/semaine<br/>25 000 REN/semaine |

[📖Information sur le programme](https://blog.synthetix.io/btc-yield-farming-pool/)

Comme ces deux pools Curve ont une exposition totale à des actifs stables (USD) ou relativement stables (BTC), ils constituent une excellente ressource pour "parquer" les bénéfices réalisés sur des pools plus risquées basés sur l'ERC-20. Vous conservez un taux de retour décent sur l'actif de base (~3-5%) tout en ayant un beau potentiel haussier sur les récompenses de l'exploitation des liquidités.

---

## Niveau 3 : Deux niveaux de rendement, c'est bien aussi !

### La Pool Balancer de votre ERC-20 préféré

Balancer est assorti d'un programme intégré de liquidity mining en BAL. Il s'applique à tout pool impliquant des tokens figurants sur la liste blanche. Par conséquent, tout pool Balancer est déjà doublement gagnant : vous avez droit à des commissions sur les swaps facilités + les récompenses minières BAL.

Examinons le profil de rendement d'un pool Balancer ERC-20 générique (vérifié) :

| EXPOSITION | RÉCOMPENSES EN | DISPONIBLES DEPUIS | L1 APR | L2 APR | L3 APR / BUDGET INCITATIF |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 50% wETH<br/>50% ERC20 | Native<br/>BAL | Juin | Variable | ~60% pour un Bal à 10$ | - |

Au-delà de l'équilibrage, les programmes d'incitation à la liquidité sont à la mode, attendez-vous à en voir d'autres, ainsi que plus de liquidity mining. Vous pouvez **utiliser un service comme [Pool FYI](https://pools.fyi/)** qui possède désormais une balise "Incentive" pour trouver les meilleures opportunités**. Pour Balancer, utilisez [ce site web](http://www.predictions.exchange/balancer/%5B%5D) pour explorer les pools et vérifier leur facteur d'exploitation BAL.

### Un dépôt simple sur Compound

Depuis le lancement du COMP, un dépôt simple peut également être considéré comme un double rendement. En effet, en plus du retour de base que le dépôt rapporte, les utilisateurs peuvent désormais bénéficier des récompenses du COMP. Vous pouvez [les calculer ici](http://www.predictions.exchange/compound/None).

| EXPOSITION | RÉCOMPENSES EN | DISPONIBLES DEPUIS | L1 APR | L2 APR | L3 APR / BUDGET INCITATIF |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Dépend | Native<br/>COMP | Juin | Variable | Variable dans COMP | - |

## ⚠ RISQUES ASSUMÉS - À LIRE

Chaque pool comporte ses propres ensembles de risques, dont voici un aperçu pour vous aider à en tenir compte. Lorsque vous investissez dans un pool de liquidités, vous prenez les risques suivant :

1. /TOUJOURS/ Le risque de base du réseau Ethereum (attaque 51%, etc.)
2. /TOUJOURS/ Vous assumez également le risque lié aux smart contracts de tous les tokens impliqués dans le pool.
3. /TOUJOURS/ Ainsi que le risque lié aux smart contracts de l'échange qui peuvent avoir des problèmes.
4. /TOUJOURS/ Un risque économique, les pertes impermanentes (pertes par rapport à la détention brute) - qui seront fortement affectées par vos choix de tokens et la pondération des pools.
5. /ENTRÉE & SORTIE/ Les risques associés à tout service que vous utilisez, tel que [Zapper.fi](https://zapper.fi), au moment de la transaction.

Je vous présente le profil de risque de l'un des pools pour vous aider à le modéliser : le pool mUSD/USDC. Tout comme les rendements, le profil de risque est un gâteau à plusieurs étages :

1. Je ne développerai pas sur le risque du réseau Ethereum
2. Ici, nous avons deux tokens dans le pool : mUSD & USDC. Pour calculer le risque, nous devons examiner la distribution actuelle de mUSD. Les tokens (USDC & USDT) comportent des risques réels, puisque par exemple [Circle peut geler les soldes USDC de n'importe quel compte](https://support.usdc.circle.com/hc/en-us/articles/360001314526-Circle-USDC-Risk-Factors).
3. Ici, nous utilisons Balancer. Leurs smart contrats ont été audités récemment par Trail of Bits[^4] Néanmoins, le protocole est assez récent.
4. Nous avons de la chance avec les pertes impermanentes - étant donné que le pool implique deux tokens stables, le risque est minimisé.
5. Tout dépend des outils que vous utilisez ici. Gardez à l'esprit que vous assumez également un risque associé à mUSD/Mstable.

{{< notice tip >}}

Cet article a éveillé votre curiosité ? Vous êtes tombés au bon endroit — nous avons un ecosystème dynamique en français pour vous aider à suivre et comprendre la finance décentralisée. Du plus accessible au plus spécialisé :
1. **[💬 Le serveur Discord DeFi France](https://discord.gg/3bWZcK2)** pour échanger avec la communauté.
2. **[☕ La version française du Daily Gwei](https://thedailygweifr.substack.com/)** pour des articles et résumés très accessibles.
3. **[🗞 La newsletter BanklessFR](https://banklessfr.substack.com/)** pour comprendre les concepts fondamentaux.
4. **[🎥 La chaine Youtube DeFi France](https://www.youtube.com/channel/UCefQC4Y-X9MBRuYBKc2waiQ)** pour approfondir avec des lives pointus.
5. & Bien sûr [ce blog](/fr/) qui creuse des sujets spécifiques liés à la pratique de la DeFi.

{{< /notice >}}

---

*Merci à [Grégoire](https://twitter.com/gregoireljda) pour son aide dans la relecture de cet article.*
*& merci à [Jon](https://twitter.com/otherbright) pour sa dernière relecture très attentive de la version française.*

[^1]: [mStable](https://mstable.org) est un "meta stablecoin" regroupant plusieurs stablecoins (USDC, USDT, TUSD & DAI) sous le tokens mUSD, tandis que les stablecoins vérouillés sont mobilisés de manière similaire à Curve (prêt et apport de liquidité).
[^2]: Vous pouvez consulter la distribution actuelle des tokens sous-jacent à mUSD sur l'application [mStable app](https://app.mstable.org/).
[^3]: [Ampleforth (AMPL)](http://ampleforth.org/) est une "monnaie adaptative fondée sur une économie solide". Elle vise à fournir un nouveau type d'actif dont les mouvements de prix ne sont corrélés à aucun autre.
[^4]: [Certik - Rapport d'audit 28 février 2020](https://github.com/ampleforth/ampleforth-audits/blob/master/token-geyser/v1.0.0/CertiK_Verification_Report.pdf)
[^5]: Il y a actuellement 51 643 NXM mis en jeu sur le contrat AMPL Geyser [`0xd36132e0c1141b26e62733e018f12eb38a7b7678`](https://etherscan.io/address/0xd36132e0c1141b26e62733e018f12eb38a7b7678). ![AMPL-Geyser-Insurance](/img/2020/yield-farmer-tier-list/ampl-geyser-insurance.png)
[^6]: Le pool Curve sUSD a déjà été mentionné dans le cadre d'une stratégie d'investissement de DeFi basée sur une participation de SNX dans le [Guide des services DeFinanciers](https://tokenbrice.xyz/fr/posts/2020/definancial-services-guide/#5-a-le-synthetixcurve-kebb-alias-the-4-steaks-yieldburger).


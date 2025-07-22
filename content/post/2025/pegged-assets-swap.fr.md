---
title: "Les guerres des swaps sur les actifs pegged"
description: "Et si l'incitation constante n'était pas la meilleure façon de maintenir la liquidité, en particulier pour les actifs pegged ? Dans cet article, j'explore l'impact de la liquidité alimentée par la dette pour les swaps d'actifs pegged."
date: '2025-07-08T01:13:50.191Z'
categories: [🌌 DeFi]
tags: [DeFi, Ethereum, Finance Décentralisée, Curve Finance, CRV, Velodrome, Velo, veCRV, veVELO, Aerodrome, veAERO, Ekubo, Uniswap, Fluid, EulerSwap, Dette Intelligente, Collatéral Intelligent]
url: pegged-assets-swap
---

Chers lecteurs, cela fait un moment ! Comme vous le savez probablement, la gestion de la liquidité est à la fois ma passion et ma profession. Dans cet article, je souhaite revenir aux fondamentaux et offrir une brève histoire au travers du prisme des swaps d'actifs pegged. En détaillant la structure de liquidité et les plateformes qui soutiennent le mieux ces paires, nous approfondirons notre compréhension des concepts clés qui restent cruciaux. Nous aurons également l'opportunité de parler de Fluid DEX et EulerSwap, les deux lancements les plus intéressants de l'année pour la construction de liquidité, qui méritent définitivement plus d'attention ici.

![pegged-assets-swap-cover](https://raw.githubusercontent.com/TokenBrice/blog/refs/heads/master/static/img/2025/pegged-assets-swap/pegged-assets-swap-cover.png)


### Les débuts des swaps d'actifs pegged (2018-2019)

Il était une fois, il y a plus de cinq ans, **tout ce que nous avions pour échanger sur le mainnet était Uniswap, Bancor, et quelques DEX basés sur des carnets d'ordres maladroits comme EtherDelta.** Ainsi, pour les swaps d'actifs pegged, les options étaient limitées, et nous utilisions le pool USDC/USDT d'Uniswap V2, ce qui était presque de la folie pure.

Examinons cette anecdote historique pour comprendre **le niveau de gaspillage atteint** à l'époque. En ce qui concerne les pools de liquidité, le paramètre clé est l'évolution relative des prix des deux actifs : si vous avez fait du LP volatile, vous êtes familier avec cela. Si vous fournissez de la liquidité pour, disons, LINK/ETH, la pire douleur pour vous, en termes de perte impermanente, serait, par exemple, que l'ETH monte en flèche pendant que LINK s'effondre : votre position de LP diminue en ETH (qui augmente en prix) et accumule du LINK (qui chute).

USDC/USDT est une autre histoire, car les deux actifs sont fortement corrélés, avec une différence de prix maximale jamais observée d'environ 10 % lors d'un événement spécifique (le dépeg de l'USDC lié à SVB) ; en temps normal, les deux ont une différence de prix de l'ordre des points de base. Cependant, UNIv2 distribue la liquidité sur toute la plage de prix, ce qui signifie qu'il alloue une quantité égale de liquidité partout, de 1 USDC = 0.0000000001 USDT à 1 USDC = 10000000000000 USDT. Pour le dire simplement : 99,9 % de la liquidité dans un UNIv2_USDC/USDT ne sera jamais utilisée. Je pense que c'est plus clair sur le graphique :


![liquidity-structures](https://raw.githubusercontent.com/TokenBrice/blog/refs/heads/master/static/img/2025/pegged-assets-swap/liquidity-structure.png "x*y=k vs StableSwap")


La seule liquidité utile là-dedans (en supposant 1 USDC ≃ 1 USDT) se trouve à l'intersection des deux lignes vertes, représentant une part très minime de la courbe de distribution de liquidité entière.

D'un autre côté, notez la distribution de liquidité StableSwap, affichée en bleu, sur le même graphique. Pour des actifs à des prix similaires, la zone couverte par la courbe est bien plus grande qu'avec l'invariant d'Uniswap.


### La révolution StableSwap pour les swaps d'actifs pegged (2020)

Une fois que StableSwap fut disponible, la liquidité des stablecoins a rapidement migré vers cette solution, car elle était significativement plus efficace (on parle d'améliorations >100x en efficacité par rapport à UNIv2). C'était **la première instance en direct de liquidité concentrée vue sur le mainnet, avant UNIv3**. Les deux sont difficiles à comparer, car UNIv3 est beaucoup plus flexible, tandis que Curve-StableSwap est plus spécialisé ; cependant, il faut rendre à César ce qui est à César. En plus de l'efficacité accrue, Curve a fourni un modèle d'incitation - veCRV+émissions CRV, qui a été [couvert plusieurs fois sur ce blog déjà](https://tokenbrice.xyz/crv-wars/).

Les incitations sont critiques pour les paires d'actifs pegged, car elles ont des caractéristiques spécifiques :


1. Elles ont tendance à être globalement **à faible volume** (par rapport à une paire volatile)
2. **Les frais que les LP peuvent facturer sont beaucoup plus faibles** (jusqu'à récemment, la convention était de 0,3 % à 1 % par transaction pour les actifs volatils, et 0,05 % pour les actifs pegged)
3. **Leur volume vient par pics** corrélés à des événements associés à l'actif (par exemple, le dépeg de l'USDC fut l'un des jours de volume les plus élevés jamais enregistrés pour l'USDC)

À cause de tout cela, je pensais jusqu'à récemment que les structures d'incitation étaient encore plus critiques pour les paires d'actifs pegged que pour les actifs volatils. Avec l'arrivée de Fluid DEX et EulerSwap, je ne pense plus que ce soit le cas. Cependant, avant d'approfondir ces derniers, nous devons d'abord aborder une autre étape historique significative dans la liquidité des actifs pegged : la sortie d'Uniswap V3.


### L'arrivée de la liquidité concentrée d'Uniswap V3 (2021)

Uniswap V3 est sorti et a offert une liquidité concentrée personnalisable à pratiquement tous les types d'actifs, permettant des gains d'efficacité massifs pour tous les fournisseurs de liquidité. Cependant, comme ce n'était pas uniquement pour les actifs pegged, cela signifiait presque des pertes impermanentes amplifiées pour les LP d'actifs volatils. Compte tenu de la nouveauté de la structure de liquidité, ainsi que du manque d'infrastructure au début, le lancement d'UNIv3 fut initialement lent.

Cependant, la concentration personnalisable a apporté des avantages tangibles, en particulier pour une sous-catégorie d'actifs pegged que j'ai qualifiée de « actifs vaguement pegged » : pensez à des paires comme :



* wstETH/ETH (corrélés, mais wstETH est en hausse constante contre ETH),
* LUSD/USDC (corrélés, mais LUSD peut légèrement sur/sous-peg)

Dans de tels cas, **la liquidité concentrée d'UNIv3 a permis aux LP de reproduire une distribution similaire en efficacité à celle de StableSwap de Curve, mais ajustée aux particularités des prix des tokens**, et cela s'est traduit une fois de plus par des gains d'efficacité massifs. Cependant, le déverrouillage final (selon l'état actuel de l'industrie) n'est arrivé que des années plus tard avec l'arrivée de Fluid DEX et EulerSwap.


### La dette comme liquidité (2025)

Je ne m'étendrai pas trop sur les modèles de Fluid et EulerSwap dans cet article pour des raisons de concision, car je veux me concentrer davantage sur ce que cela signifie pour la construction de liquidité. En résumé, Fluid a trouvé une manière créative de transformer la dette en liquidité avec la « Dette Intelligente » (Smart Debt).

Imaginez un utilisateur moyen fournissant un collatéral ETH et empruntant de l'USDC. Veut-il spécifiquement de l'USDC ? Très probablement, il s'en fiche tant qu'il emprunte un token stable et sûr indexée sur le dollar. Il prendrait probablement aussi de l'USDT.

C'est précisément ce que fait la dette intelligente. Dans un vault de dette intelligente, notre emprunteur emprunte un mélange d'USDC et d'USDT, qui évolue constamment : sa dette sert désormais de liquidité pour la paire USDC/USDT. Ce que cela signifie pour les emprunteurs, c'est **une réduction des coûts d'emprunt, car ils gagnent maintenant des frais de trading**, ce qui peut potentiellement compenser les intérêts d'emprunt.

![fluid-smart-debt](https://raw.githubusercontent.com/TokenBrice/blog/refs/heads/master/static/img/2025/pegged-assets-swap/fluid-smart-debt.png)

C'est du point de vue de l'emprunteur, mais passons maintenant à la perspective d'un protocole. Qu'est-ce que cela signifie pour Circle et Tether ? Essentiellement, **une liquidité à un coût pratiquement nul, sans aucune forme d'incitation.** Rien de vraiment nouveau pour Circle, qui a été sponsorisé par tout l'écosystème pendant des années – mais pour un autre stablecoin, disons un GHO, BOLD, ou FRAX, c'est énorme.

Je me suis concentré sur Fluid ici, mais le raisonnement est similaire pour EulerSwap, bien que l'implémentation soit différente. EulerSwap est encore en mode test et génère déjà un volume sérieux sur USDC/USDT.

Si vous comprenez cela, vous pouvez saisir ma thèse, qui stipule simplement : « Je ne vois pas une DeFi où Euler/Fluid/Similaires ne dominent pas éventuellement les swaps d'actifs pegged. »

Vous ne le voyez pas encore ? Rappelez-vous ce qui suit :

* Les paires d'actifs pegged ont généralement un faible volume ⇒ faibles frais
* Ainsi, elles nécessitent une forte incitation pour être maintenues sur un DEX classique
* Fluid et Euler peuvent maintenir cette liquidité à un coût proche de zéro.

⇒ Si (cela a déjà commencé) il y a une course vers le bas en termes de frais pour les swaps d'actifs pegged, les DEX réguliers n'ont absolument aucune chance de la gagner.


### 0xOrb, un challenger potentiel (~2026) ?

Maintenant, pour vous donner une image précise de tout le paysage des swaps d'actifs pegged, je dois mentionner un autre projet pas encore en ligne, mais prometteur : [0xOrb](https://orbswap.org/). La promesse est simple : **StableSwap, mais avec n actifs, n pouvant aller jusqu'à 1000**.

Ainsi, pour les stablecoins, vous pourriez imaginer un méga-pool bien approvisionné en USDC et USDT, qui ensuite intègre des stablecoins « alternatifs » et leur offre une grande liquidité contre les majors. L'approche a du mérite pour la longue traîne des actifs pegged, mais je ne vois pas de tels pools dominer le volume principal (USDC<>USDT ou cbBTC<>wBTC).

En plus de cela, de tels pools pourraient être inter-chaînes, bien que je pense que l'avantage ici est absolument marginal, voire **défavorable** (⇒ augmente les risques et la complexité de l'infrastructure sans avantages), **puisque l'USDC et l'USDT sont de plus en plus transférables 1:1 rapidement entre les chaînes grâce à des produits comme [CCTP](https://www.circle.com/cross-chain-transfer-protocol)**.


### Qu'est-ce que cela signifie pour les acteurs DEX purs établis ?

Tout d'abord, la mise en garde la plus importante : nous parlons ici des swaps d'actifs pegged. Reproduire le même playbook sur des paires volatiles est beaucoup plus difficile, [comme on l'a vu avec le vault Smart Debt+Collateral ETH/USDC de Fluid et les pertes subies par ses LP](https://gov.fluid.io/t/current-issues-with-eth-usdc-pool/1606).

Les DEX qui génèrent la majeure partie de leur volume et de leurs frais grâce à des paires volatiles, comme Aerodrome, ne seront probablement pas impactés par ces nouveaux entrants. **La réalité est, cependant, beaucoup plus sombre pour les DEX axés sur les actifs pegged**, et je veux examiner deux d'entre eux pour conclure cet article :


### Curve : fin de partie à moins de changements majeurs

Les swaps d'actifs pegged restent cruciaux pour Curve, toujours considéré comme le foyer de la liquidité des stablecoins. En effet, il y a eu des tentatives pour capturer du volume volatile avec CryptoSwap, mais cela s'est avéré infructueux.

Avec l'arrivée de Fluid et EulerSwap, je pense que Curve est le DEX qui a le plus à perdre, et je ne le vois pas maintenir un volume important (ils ont déjà été éjectés du top 10 il y a un moment) à moins que des changements significatifs ne se produisent :



* **Révision de veCRV** : tirer parti des apprentissages des modèles plus récents comme veAERO pour optimiser l'allocation des émissions CRV.
* **Augmentation de l'efficacité des DEX en exploitant crvUSD** : par exemple, en permettant des prêts crvUSD aux LP de Curve.
* **Nouvelle structure de liquidité pour les actifs volatils** : afin de pouvoir prétendre à capturer le volume associé.


### Ekubo : le dernier arrivé confiant qui court à sa perte

La situation d'Ekubo est sans doute encore pire, car ils sont arrivés récemment à la fête. À première vue, Ekubo sur Ethereum est un DEX à croissance rapide qui génère des volumes sérieux. Ekubo est essentiellement une alternative à UNIv4, avec un peu plus de personnalisation de la structure de liquidité et une DAO qui s'est révélée moins extractive que celle d'Uniswap (la barre la plus basse de toutes, mais quand même).

Le problème réside dans l'origine du volume : la grande majorité (>95 %) provient d'une paire USDC/USDT avec des frais de 0,00005 % et fortement incitée. Ekubo joue essentiellement une course vers le bas qu'il ne peut pas gagner, car Ekubo ne peut pas maintenir des frais extrêmement bas à long terme (les LP doivent vivre), tandis que Fluid/Euler le peuvent (si les emprunteurs reçoivent même un rendement de 0,1 % sur leur dette grâce à la dette intelligente, ils sont mieux lotis qu'avant et donc satisfaits).

![ekubo-stats](https://raw.githubusercontent.com/TokenBrice/blog/refs/heads/master/static/img/2025/pegged-assets-swap/ekubo.png "Statistiques Ekubo, au 07 juillet 2025")

Avec un pool de 2,6 M$ de TVL, traitant environ 130 M$ de volume quotidien pour 662 $ de frais collectés, incité à environ 8 % en EKUBO, ils approchent déjà rapidement la limite de ce qu'ils peuvent faire.

L'aspect le plus amusant de tout cela est qu'**Ekubo lui-même a initié la course vers le bas avec les frais de swap USDC/USDT et sera spectaculairement vaincu à son propre jeu**. La DeFi ne cesse jamais de divertir.

Comme toujours, j'espère que cet article a été instructif et a approfondi votre compréhension du jeu des swaps d'actifs pegged. J'ai hâte de voir mon personnage se faire démolir par la communauté Ekubo simplement pour avoir exprimé une opinion basée sur des faits : leur réaction m'a donné une confiance extrême dans mon évaluation, car j'ai observé la même réponse lorsque :

* J'ai dénoncé les pratiques de sécurité absurdes de MAI, et il a été piraté + dépeggé peu après.
* J'ai dénoncé le gaslighting et les mensonges de R/David Garai, et R a été piraté et est tombé l'oubli <6 mois plus tard.
* J'ai critiqué le comportement de l'équipe de Prisma, et ils ont été piratés et ont fermé le protocole <12 mois plus tard.

Et la liste continue. Bonne chance à tous, en particulier aux détenteurs de bags EKUBO – essayez d'avoir un peu de classe dans votre désarroi, cela vous servira bien.
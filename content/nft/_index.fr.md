---
title: "Les NFTs expliqués sans prise de tête par un crypto-native"
date: 2021-06-26T13:24:40+02:00
description: Les NFTs permettent l'existence de nouveaux types d'objets numériques dont peu encore comprennent réellement l'apport. Je vous explique les fondamentaux, ce qu'ils permettent de faire et comment les mobiliser.
url: nft
---

## ⌚ Les NFTs en 2 minutes

Les tokens non-fongibles (NFTs) sont des **objets numériques programmables** qui peuvent incorporer tous types de médias et permettent de nouvelles formes d'interactions entre les créateurs et leur communauté.

Ils sont souvent mal compris et vite jugés, particulièrement par des personnes qui ne sont pas encore informées sur les enjeux relatifs à la décentralisation et la désintermédiation. En effet, pour bien saisir l'apport des NFTs, il faut comprendre plusieurs notions essentielles :

### La fongibilité

{{< notice info >}}
Un bien est dit fongible quand **une unité est équivalente à une autre**. C'est le cas par exemple pour les monnaies liquides comme l'Euro ou le Dollar qui sont standardisées.
{{< /notice >}}

Grâce aux NFTs, il est possible **de créer des objets dits non-fongibles car uniques mais également des collections d'objets** qui partagent différents attributs. 

J'explique l'apport de la fongibilité en profondeur dans cet article publié en 2018 : **[Les tokens non fongibles expliqués par Tortank et Dracaufeu]({{< relref path="/content/posts/2018/nft.fr.md" >}})**.

{{< notice note >}}
La fongibilité est aussi un enjeu sur les tokens considérés fongibles comme Ethereum ou Bitcoin. Puisque leur blockchain est publique, les transactions peuvent être tracées. Certains tokens sont contaminés (tainted) car impliqués dans des vols ou autres affaires illicites, et peuvent être refusés par différents services.
{{< /notice >}}

### Histoire publique et vérifiable

Les NFTs existent sur des blockchains publiques, il est ainsi possible de **consulter leur historique complet depuis leur création** : leur origine, tous leurs possesseurs, ainsi que les différents échanges et leur prix.

Cette caractéristique est particulièrement pertinente pour le marché de l'art, où seul l'historique des œuvres célèbres est habituellement vérifiable grâce à des intermédiaires de confiance.

J'approfondi l'apport de cette propriété dans cet article : **[Les tokens non-fongibles (NFTs) : le poids et l'apport de l'histoire vérifiable]({{< relref path="/content/posts/2021/nft-usecases.fr.md" >}})**.

### Objet et propriété intellectuelle

Je décris les NFTs comme des objets numériques, faute de mieux. J'entends par là qu'ils peuvent incorporer des **références vers tout type de médias**, mais aussi **une logique programmatique** par exemple pour gérer la propriété intellectuelle. 

Cela permet également de redéfinir les termes du marché : **les créateurs peuvent ainsi capturer une commission sur les reventes de leurs œuvres** sur des marchés secondaires.


### Composabilité

Tout comme la DeFi, les NFTs sont **composables**. Un NFT peut ainsi en posséder un autre, qui correspond à un accessoire par exemple (MoonCats). Certains NFTs disposent également d'un modèle 3D qui leur permet d'être incarné dans le MetaVerse et disponible dans certains jeux.

![isotile-mooncats](/img/others/isotile-mooncats.png "☝ Mes MoonCats qui se pavannent dans leur chambre grâce à Isotile.")

Si le sujet des NFTs vous intéresse, vous pouvez **[revoir les précédent lives NFT ici]**(https://www.youtube.com/watch?v=buCQbnM6mHw&list=PLreQl_vxgtPj0CF6Bsh7GPn_r9Vlm-kqz) et **[me suivre sur Twitch[https://twitch.tw/tokenbrice/]** pour ne pas rater les prochains. J'y mets fréquemment en jeu des NFTs !

## 🧰 Trousse à outils NFT

De nombreux outils permettent de **créer des NFTs**. Ils utilisent différentes solutions pour l'hébergement des médias référencés. [Rarible](https://rarible.com/) ou encore [NiftyKit](https://niftykit.com/) sont un bon point de départ.

Une fois créés, les NFTs peuvent être **achetés et vendus grâce à des services** comme [Foundation](https://foundation.app/), [OpenSea](https://opensea.io/). Chaque service à ses règles, potentiellement un token, et s'adapte pour certains types de NFTs.

**Les collections de NFTs peuvent également avoir des index [NFT20](https://nft20.io/)** qui permettent l'échange d'un NFT à l'autre ou depuis ETH. Cela facilite également l'établissement du fameux floor - le prix "minimal" pour une œuvre issue d'une certaine collection.

Les adeptes des collections apprécient également différent outils qui permettent d'apprécier la rareté relative de chaque oeuvre comme **[RarityTools](https://rarity.tools/)**.

Différents outils permettent de **visualiser les NFTs et d'organiser des collections**. Des musées et expositions existent, et des vernissages virtuels ont même lieux dans le MetaVerse : [la Gallery of Crypto Art dans le Metaverse](https://www.artsy.net/gallery-of-crypto-art).

La nature programmable des NFTs permet d'envisager de **redéfinir les termes même de la possession**. Les approches de "partialisation" permettent ainsi de posséder collectivement une oeuvre unique, par exemple [Spectre.zyx](https://spectre.xyz/).

---

## 🧪 NFT utilitaires en DeFi

Les NFTs permettent de définir des collections d'objets. Ils sont ainsi **utilisés en finance décentralisée** lorsque cela est pertinent. Cela devient de plus en plus fréquent :

*   Sur **Uniswap V3**, les positions d'apport de liquidité sont représentées par un NFT.
*   Sur **Curve**, un NFT sert de reçu pour les swaps inter-actifs via Synthetix (6 min de délais)
*   Sur **Mai.Finance**, un marché monétaire, le vault est représenté par un NFT
*   Sur **StakeDAO**, les utilisateurs stakent leur xSDT pour gagner des points servant à mint des NFT qui donnent des bonus sur la plateforme
*   Enfin **Alchemix** qui a récemment subi un souci technique sur AlETH offre un NFT aux utilisateurs qui remboursent l'argent indûment reçu. 

![uniswap-v3-LP-NFT](/img/others/uniswapv3-lp-nft.gif "Visuel d'un NFT-LP Uniswap V3")

---

## Mon approche des NFTs

Je m'intéresse tout particulièrement aux **collections d'art génératif**, une nouveauté permise par la programmabilité d'Ethereum.

Depuis le succès de CryptoPunks, les projets de ce type se multiplient. Les NFTs permettent l'existence de collections d'art génératifs réellement innovantes :
- Contrairement aux collections classiques (type carte Pokémon ou Magic), la possession des objets et leur rareté sont réelles et vérifiables.
- Avec les bonnes dispositions, il est possible d'héberger les médias référencés de manière pérenne.
- La génération des paramètres du NFT peut également se faire de manière aléatoire mais totalement vérifiable (on-chain) grâce à la VRF de Chainlink, comme pour les **[Luchadores](https://luchadores.io)**.

Je participe aux générations des collections qui m'intriguent et me semblent pertinentes. J'essaie également de soutenir des artistes qui débutent en supportant leur travail et le faisant découvrir sur Twitch ou Twitter. 

![gallerie-nft](/img/others/gallerie-nft.jpeg "Exposition virtuelle de mes NFTs")

Vous pouvez consulter **[ma collection de NFTs avec une exposition virtuelle dans le MetaVerse par ici](https://oncyber.io/tokenbrice)**.
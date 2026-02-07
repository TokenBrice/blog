---
title: "NFTfi: NFT meets DeFi, liquidity and leverage ensue"
description: "DeFi offers NFT projects tools to solve their main limitations (like liquidity) while NFTs allow to make DeFi more fun and digestible: a perfect pairing?"
date: '2022-03-29T01:13:50.191Z'
categories: [NFT]
tags: [DeFi, Ethereum, Decentralized Finance, NFT, Forgotten Wizard, Luchadores, NFTfi]
tocNum: false
url: nftfi-defi-nft
image: /img/2022/nft-defi-infrastructure/nft-defi-infrastructure-tokenbrice.png
difficulty: "beginner"
---

Decentralized finance has opened up a world of possibilities: a myriad of previously necessary intermediaries are now supernumerary. Nevertheless, it is intimidating because of its potential complexity and interdisciplinary. In addition to the obvious technical dimension, DeFi also invokes concepts from various disciplines: economics, social sciences, "memetics", etc.

Thus, for years now, NFTs have served as a gateway to the decentralized world, demonstrating the benefits of tokenization and disintermediation to a population still not very fond of DeFi. 

So today I propose to converge the two main themes of this blog into one captivating topic: the emergence of DeFi infrastructure for NFTs, or the arrival of NFTs/gamification in DeFi - it's all about perspective.

## DeFi + NFT => NFTfi : a world of possibilities for your JPEGs

The use cases at the crossroads of DeFi and NFTs are numerous and in full development. Rather than an exhaustive list, I propose to analyze a few emblematic projects to understand how they assemble elements from both universes to offer a relevant service.

This infography is a good starting point to deepen your analysis of the NFTfi landscape if this article arouses your curiosity:

![nftfi-landscape](/img/2022/nft-defi-infrastructure/nftfi-landscape.jpeg "Map of NFTfi projects (source UnUniFi Protocol)")

Let's start with the most intuitive one for those who are already a bit up to date with DeFi: the arrival of a financial infrastructure to exchange, but also to lend, to make productive or to split NFTs. To tackle this vast subject, let's start from the first layer: the infrastructure used to buy and sell NFTs.

### NFT buying and selling services

Until recently, NFTs were in a strange in-between situation. In essence, NFTs allow disintermediation and more direct interaction between creators and their audience. With this disintermediation comes a massive reduction in the costs incurred to bring a work to market and new possibilities, such as their interactivity.

Only thing is, NFTs are still exchanged mainly on a service that is not up to their standards, I named OpenSea - which still remains dominant although the situation is changing rapidly since the arrival of LooksRare.

Without going into too much detail, OpenSea has many limitations:



* A near-weary fee for each exchange - 2.5% - and that is reserved exclusively for the team.
* A basic lack of respect for the NFT community: violation of their privacy, manipulation, etc.
* A certain disregard for the most community-based NFT projects: the verification mechanisms on OpenSea are not very transparent and do not really depend on the volume. Pitiful projects, but carried by celebrities, have been verified quickly while Luchadores, for example, are still waiting.
* A lack of investment in its own development: the platform is slow to evolve and does not listen to its users.
* A 100% business approach: [OpenSea has done 9 fundraisings](https://www.crunchbase.com/organization/opensea/company_financials) so far, and this despite the gargantuan profits they generate via the excessive fees charged: $100M in volume **on 1 day ⇒ $2.5M in the team's pockets** (- operational fees, but still...)

So we get a situation close to the US ISPs: OpenSea is used by everyone in the NFT world, but also **virtually hated by a significant part of its users**.

So let's start by looking at the data which speaks for itself:

![looksrare-vs-opensea](/img/2022/nft-defi-infrastructure/looksrare-vs-opensea.png "Volume observed on LooksRare and OpenSea")


We're just looking at volume here. In terms of number of users and transactions OpenSea still dominates. You can find all the data on the super dashboard [from Hildoby](https://twitter.com/hildobby_) : [LooksRare VS Opensea (Dune Analytics)](https://dune.xyz/hildobby/LooksRare-VS-OpenSea).

Many of us were waiting for a credible alternative, and fortunately it has arrived: LooksRare. The case is worth digging into, but in short LooksRare is the exact opposite of OpenSea:



* Transaction fees are reduced to 2% and **redistributed entirely** to LOOKS token stakers.
* The LooksRare team is very attentive to the community and in two months of existence, they have already implemented many features requested by their users.
* The LOOKS token has been airdropped to OpenSea users. It can now be obtained by buying or selling NFT on Looksrare: **a direct distribution** to the users of the service.
* A POL (Protocol Owned Liquidity) strategy is implemented by the protocol: a significant part of the liquidity on LOOKS is owned directly by the protocol.

The protocol already has nearly $13M in ETH+LOOK deployed on UniswapV3 to support liquidity - here's [LooksRare's wallet](https://debank.com/profile/0xc8c57e4c73c71f72ca0a7e043e5d2d144f98ef13) to see for yourself. The fees collected on the LP are used to... bring more and more liquidity!

![looksrare-pol](/img/2022/nft-defi-infrastructure/looksrare-pol.png)

This new set of rules allows LooksRare to be extremely competitive compared to Opensea, since the fee is 20% lower, and each purchase/sale is also paid in LOOKS. The result is clear: both buyers and sellers benefit from preferring LooksRare to Opensea.

![looksrare-vs-opensea-cost](/img/2022/nft-defi-infrastructure/looksrare-vs-opensea-cost.jpeg "LooksRare vs Opensea cost comparison")

### Tokenization explained with NFTs partialization

Exchanging NFTs is great: you still need to understand what's in the box! We will therefore detail the stakes of tokenization with several examples. Indeed, the possibilities offered by the latter are immense, so let's illustrate them!

Let's take the time to explain the concept. Tokenization is the action of creating a token (a token that **represents** something). At first sight like that, the interest can be hard to conceive. However, tokenizing also allows for a form of "alchemy": a transmutation - a change in the type of token from fungible to non-fungible, and vice versa.

Let's take an example that illustrates the benefits of tokenization - the case of **fractionalizing an NFT**.

1. We start with a specific non-fungible token, CryptoPunk #666 for example.
2. We lock it in a contract that issues 10 000 PUNK tokens, ERC-20 tokens. 
3. We now have a token that represents 1/10,000 of the original CryptoPunk #666. This token is a classic ERC-20 and therefore easily exchangeable via Uniswap or other (⚠️ Liquidity)

⇒ Tokenization here allows **collective ownership of a unique asset** (the NFT CryptoPunk #666).

This concept, while illustrating the benefits of tokenization also corresponds to a real use case. The reality is of course more complex, since we have only described here the collectivization mechanism (1 NFT ⇒ 10 000 ERC20). The reverse path is also possible to recover access to the locked NFT: 10 000 PUNK ⇒ NFT CryptoPunk #666: this is privatization.

This model is the one of [Spectrum.xyz](https://spectre.xyz/litepaper), a service that allows to manage the collectivization and privatization of NFTs.


![spectre-xyz](/img/2022/nft-defi-infrastructure/spectre.png)

In addition to the collective possession, such a solution also has an interest in terms of liquidity: the obtained token (PUNK) is a classic ERC20, it is thus much easier to develop solutions allowing its immediate purchase and sale than with an NFT, which requires the meeting of a simultaneous demand and offer.


### Tokenization to develop liquidity: vaults

Once tokenization is well understood, the next chapter - NFT vaults - is almost a given. One of the challenges of NFTs is the liquidity of the markets. Non-fungibility is great for making collections of 10,000 coins, all of which are unique but similar - but what about the valuation and exchange of these?

Besides LooksRare and Opensea mentioned above, there are other marketplaces for NFTs that rely on a different logic: this is **the NFT vault model** - which has many interests, but also limitations - the main one being that this approach is only possible with large collections (several hundred units) and/or quite popular (high demand).



1. [MINT] A "vault" (smart contract) specific to a collection is created; users can deposit their NFTs in it. 
2. When a user deposits an NFT in the vault, its contribution is recognized by the emission of an ERC20 token.
3. [REDEEM] At any time, the ERC20 token can be exchanged for any NFT in the vault. The ERC20 token is then destroyed.

{{< notice warning >}}
⚠️ As you can see, the vault assumes that all NFTs are equivalent: so it is better to enter a vault with an NFT among the least rare of the given collection. 
{{< /notice >}}

The leader in this field is probably [NFTX](https://nftx.io/vault/0x87931e7ad81914e7898d07c68f145fc0a553d8fb/info/), but there is also [NFT20](https://nft20.io/). This method allows you to get an ERC20 token - for example the WIZARD - that corresponds to a claim on any NFT in the vault, in this case any of the 215 Forgotten Wizard Cult (NFTs) contained in [the vault.](https://nftx.io/vault/0x87931e7ad81914e7898d07c68f145fc0a553d8fb/info/)

![nftx-wizard-list](/img/2022/nft-defi-infrastructure/nftx-wizard-list.png "The Forgotten Wizard Cult vault ur NFTX")

The liquidity on the WIZARD token can be developed against ETH for example, allowing the immediate purchase of any wizard contained in the vault. The reverse is also possible: any owner of a Forgotten Wizard Cult can deposit it in the vault in order to obtain 1 WIZARD which he can then sell for ETH.

And finally NFTX goes even further since the platform's native token as well as the collected fees are used to offer incentives to deṕoser in the vault and develop liquidity. **Users who** **deposit NFTs into the vault are thus eligible for a staking fee** - and higher returns are possible for those who deposit + LP: the financialization of NFTs is launched!

![nftx-wizard](/img/2022/nft-defi-infrastructure/nftx-wizard.png "Staking returns (red) and LP (purple) on the WIZARD token")


The focus here is on liquidity, but keep in mind that switching from an NFT to an ERC-20 comes with many other benefits:



1. If the liquidity on the pair is sufficient - then it also becomes **a price source**.
2. Price source (oracle) + liquidity means... collateral of course! With these two elements, there is nothing to prevent the WIZARD from being considered as **collateral for borrowing** other tokens like stablecoins. This is feasible but much more complex starting directly from the NFT.
3. Finally, keep in mind that there is no limit to tokenization, as long as there is an interest. We stayed here on single tokenization cases, but **tangled tokenization** scenarios are also possible.

An ERC-20 token that represents a claim on a given Wizard is great. Now imagine that you have the same thing for CryptoPunks, BAYC and so on - this is the case on NFTX. There is nothing to prevent us from considering an additional tokenization step to create an **NFT index** represented by an ERC20 token but which would itself **be exchangeable against the tokens representing the underlying assets:** :

One could thus imagine the NFT-Bluechip-Index, an ERC-20 token created by locking 1 WIZARD + 1 PUNK + 1 BAYC. This token would be easily liquid, and thus allow for easy exposure to all three collections in a single transaction. In addition, the token would remain fully collateralized at all times by 1 NFT from each collection. An owner of the NFT-Bluechip-Index could do the opposite at any time, i.e.:



1. [With the NFT-Bluechip contract] : burn 1 NFT-Bluechip-Index to get 1 WIZARD + 1 PUNK + 1 BAYC
2. [Using NFTX contracts/vaults] burn of 1 WIZARD + 1 PUNK + 1 BAYC to retrieve one NFT (of your choice from those in the vault) from each underlying collection. 


### Idol : NTFs to tokenize a DeFi yield

To continue and finish on tokenization, know that it also allows to link the two worlds - NFTs and DeFi: the perfect example here is the [IdolsNFT](https://www.theidols.io/) project.

The IdolsNFT were initially sold via a bonding curve for a price between 0.25 and 0.5 ETH. All ETH collected during the sale are staked via Lido (StETH). Owning an Idol makes you eligible for the corresponding share of the returns. Here, it is the yield generated by the StETH that is tokenized.

![idols-nft](/img/2022/nft-defi-infrastructure/idol-nfts.png)


And the project goes even further! Indeed, there is also an ERC-20 in the story, the VIRTUE, initially distributed to the first buyers. From now on, to obtain VIRTUE, it is necessary to bond stETH (-> which increases the productive capital of the project). 

The VIRTUE corresponds to a proxy exposure on NFT Idols: for each sale of an NFT Idol, a fee of 7.5% is taken and given to the VIRTUE stakers.

![idolnfts-virtue-cycle](/img/2022/nft-defi-infrastructure/idol-cycle.png)

Thus, the Idols, "Guardians of Ethereum" use NFTs to make ETH staking more fun and interactive. In addition, the capture of fees on the VIRTUE token allows to avoid an "external capture" of fees generated by IdolsNFT exchanges as it is the case for NFTs exchanged on NFTX for example. 

Finally, the large owners of the collection have a clear path to compound their return if their conviction is strong:

1. Possession of several IdolsNFT ⇒ Yield in stETH
2. Composition of farmed stETH via bonding ⇒ VIRTUE
3. Stake of VIRTUE ⇒ Yield in ETH
4. Staking ETH with Lido ⇒ StETH ⇒ Bonding for VIRTUE then stake

Whatever happens with this collection, I think it has laid the foundation for what NFTs collections augmented by and synergistic with DeFi can be. I expect to see many more relevant variations on this model.


### Aggregation of various liquidity sources

In this article, we have already mentioned three different platforms to buy or sell NFTs: OpenSea, LooksRare and NFTX. The reality is even denser, there is an armada of marketplaces for NFTs, more or less successful and more or less specialized, here are some others: [Rarible](https://rarible.com/), [Superrare](https://superrare.com/), [Foundation](https://foundation.app/), [NFT20](https://nft20.io/), etc.

Faced with this myriad of options, buyers do not necessarily have the time, inclination, energy or knowledge to explore all their options before concluding a transaction. The situation is very similar to buying/selling an ERC20 token in DeFi: liquidity is very fragmented. Logically, the solution is therefore similar to the one deployed in DeFi: aggregation.

![gem.xyz](/img/2022/nft-defi-infrastructure/gem-xyz.png "Gem, the NFT aggregator")


Thus, there are several services capable of directing "orders" to different marketplaces, or even ŕealising a "swipe" across multiple platforms with a single transaction: these are [Genie](https://genie.xyz) and [Gem](https://gem.xyz). 

Here again, it is the responsiveness of the team and the composability of the service that will make the difference in the long run: Gem seems to be ahead of the game thanks to its advanced integration of LooksRare (claim LOOKS possible for buyers via Gem).

---

## NFT + DeFi => Games with real stakes

If DeFi has discovered the huge market that is NFTs recently, the reverse march is also observed: **the arrival of DeFi components in NFTs projects** - we often talk about GameFi to describe this trend.

It has been several years since the first iterations of GameFi appeared, with games that can become a credible source of income for their players: the most famous is of course [Axie Infinity](https://axieinfinity.com/), but there are many others: [AaveGotchi](https://www.aavegotchi.com/), [CryptoRaiders](https://cryptoraiders.xyz/), etc.

Unfortunately I'm not very active on these projects myself, so I propose to detail one that is more familiar to me: Luchadores. Here again, we find DeFi components that are grafted on the NFT project:

* Owning a Luchador (NFT) gives the right to a return in LUCHA (ERC20 token).
* The protocol owns about [60% of the liquidity on the two LUCHA pairs](https://debank.com/profile/0x0cb11b92fa5c30eafe4ae84b7bb4df3034c38b9d), thanks to the funds raised during the sale of the first pinatas.

{{< notice note >}}
The 🪅 are ERC-1155 tokens that contain 1 accessory for Luchadores, whose rarity is determined by verifiable randomness ([Chainlink VRF](https://blog.chain.link/vrf-v2-mainnet-launch/)).
{{< /notice >}}


* The protocol also has about 30 Luchadores (⇒Yield in LUCHA) purchased with part of the profits from the first pinata: the purchase was made using an aggregator.
* A marketplace is available for accessories, with payment in LUCHA: a redistribution of the collected fees is also possible.

![luchadores](/img/2022/nft-defi-infrastructure/luchadores.png)

The game is not yet available (Alpha by the end of March!), but interactions of this type will only become more dense as it develops. With the arrival of the game, new features will come: staking your LUCHA tokens will allow you to get MASK, a non-transferable token but necessary to buy different items to increase the power of your Luchadores.

From the launch of the game, players will earn LUCHA for each victory. Depending on their ranking, the amount of LUCHA obtained increases: the best players will be able to get interesting returns, for a very moderate initial cost (1 Luchador, potentially minted for \~0.03 ETH). Be prepared!

If you discover Luchadores with this article, feel free to read this introduction: **[🤼 Long live free (and verifiable onchain) wrestling](https://tokenbrice.xyz/luchadores-nft/)**

## What next? 

In this article, we have stayed on the visible part of the iceberg. At the crossroads of DeFi and NFTs, there are still many new possible use cases. I propose to make a list with the main services that explore these fields: 


### FloorDAO : NFT x DeFi x DAO

[FloorDAO](https://floor.xyz/) is sort of an extra layer built on top of NFTX. FloorDAO uses the OlympusDAO model but adapted for NFTs. The objective is to ensure a return and support liquidity on the collections concerned (Punk and Wizard for the moment). How does it work? Simple: for the concerned collections, the owners of the corresponding NFTX token (ex WIZARD for Forgotten Wizards) as well as the LP (WIZARD/ETH) can bond it to obtain FLOOR tokens.

![floordao-bond](/img/2022/nft-defi-infrastructure/floordao-bond.png "The relevance of the bonding varies according to the needs of the FloorDAO and the evolution of the price of FLOOR.")

The collected tokens and LPs are used by FloorDAO to generate a return (NFTX staking). The community (gFLOOR holders) votes to decide which assets to acquire next. Olympus uses the inflation of its governance token to acquire strategic assets such as DAI, LUSD, or CRV; FloorDAO does the same thing but targets NFTX tokens and therefore backs them with an NFT.   

Here again, the protocol owns a share of its own liquidity on FLOOR/ETH (on Uniswap) and the fees generated by the position contribute to the returns of the FloorDAO treasury.

### NFTs to collateralize loans (without going through an ERC20/vault)

The main limitation to overcome here is of course the fact that the sale of NFT is done in a bid/ask logic and is therefore not immediate. Several projects are nevertheless tackling the problem:

* [DropsDAO](https://drops.co) : which imports the logic of lending pools, for NFT collections
* [Arcade.xyz](https://www.arcade.xyz/) : OGs remember ETHLend, the ancestor of Aave. Arcade is the same logic but for NFTs : a borrowing service without pool, which works by offer/demand.
* [JPEGd'69](https://twitter.com/JPEGd_69) - which should launch soon and allow CryptoPunks to be used as collateral.
* Or [NFTfi](https://www.nftfi.com/).


### Pricing of NFTs / oracle

For borrowing, a price source is needed to determine if the position is solvent. Here again, several projects are working on this:

* [Abacus](https://abacus.wtf/) - a decentralized service to price an NFT
* [Pilgrim](https://pilgrim.money/) - an AMM / valuation method for NFTs


### Renting of NFTs

Renting allows for example to borrow an NFT to play a game without having to own it. It also creates opportunities for large NFT owners in a GameFi collection.

* [Rentable](https://beta.rentable.world/), a generalist protocol for NFT rentals.
* Ship lending + revenue sharing generated with on [Cometh](https://www.cometh.io/)
* [Axie Infinity scholarship model](https://www.gfinityesports.com/cryptocurrency/axie-infinity-scholarship-what-is-it-how-to-apply-axs/)

---

If you found this peek into the NTFfi landscape insightful, you are now sitting at the crossroads:
- you can [read my other articles on NFTs here](https://tokenbrice.xyz/categories/nft/) 
- or [explore the depths of DeFi](https://tokenbrice.xyz/categories/defi/)

Enjoy!
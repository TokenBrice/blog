---
title: Le respect de la vie privée sur internet - l'exception qui devrait être norme
description: >-
  Un aperçu des pratiques de traçage des grands sites français et comment s''en protéger. Quelques pistes pour la vie privée de ses utilisateurs sur son site
date: '2018-07-25T10:54:13.745Z'
categories: [Analysis, Privacy]
tags: [facebook, google, ad model, privacy, trackers, ecocrypto]
image: img/2018/user-privacy/cover.jpeg
---

En 2018, respecter la vie privée de ses utilisateurs lorsque l’on lance un site c’est un jeu d’enfant, non ? Avec les révélations de Snowden sur NSA et toutes celles qui ont suivi, les hébergeurs et autres fournisseurs de service ont dû revoir leur pratiques ? C’est ce qu’on croyait nous aussi, et l’illusion est bien vite retombée. C’est parti pour un petit tour des pratiques : qui collecte vos donnés, comment et à quelles fins ?

Link to [the English translation of this article.](https://tokenbrice.xyz/posts/2018/users-privacy.fr.md" lang="fr" >}})

### Un peu de contexte

Vous le savez sans-doute, sinon on vous invite à lire le manifeste – EcoCrypto respecte ses utilisateurs et leur attention. Pour leur attention, c’est notre problème, mais concernant le respect de la vie privée de nos utilisateurs c’est bien plus large que nous : on doit vérifier le moindre service qu’on utilise pour s’assurer qu’il n’y a pas d’abus.

En publiant [le manifeste](https://ecocrypto.fr/manifeste/), on a également réalisé que peu de gens sont réellement informés sur l’ampleur de la traque en ligne, alors cet article a pour vocation d’offrir un petit tour d’horizon pour montrer à quel point nous sommes suivis où que nous allons. Nous proposerons également deux jeux de recommandations en fin d’article : un qui concerne tout le monde et décrit les bases pour couvrir vos traces en ligne et une méthodologie destinées à ceux qui gèrent des sites souhaitant respecter au mieux la vie privée de leurs utilisateurs.

La folie des trackers
---------------------

Commençons par la base : qu’est-ce qu’un tracker ? En bref, c’est un petit «programme » que quelqu’un peut installer sur son site – cela permet aux différents services qu’il utilise de collecter des données sur ses visiteurs afin d’apporter des fonctionalités supplémentaires.

Un tracker agit comme un petit mouchard pour un service tiers **– chaque tracker c’est un invité de plus à la table du festin qu’on se paye sur nos données.**

### Une « petite dizaine » de trackers, la norme ?

N’importe quel site de presse a au minimum une bonne dizaine de trackers. Pas besoin de nous croire sur parole, [une petite extension comme Ghostery](https://www.ghostery.com/) permet de les visualiser très simplement.

Voici un petit tour d’horizon d’une sélection de site qui compte parmis les plus fréquentés en France :

- leMonde.fr compte 32 trackers différents,
- leFigaro.fr – 35
- Mediapart – 21
- l’Express – 49
- tf1.fr – 35
- France2.fr – 18
- Le site de l’[Agence France Presse](http://afp.com) – 12
- Et enfin le plus « propre » qu’on ait pu trouvé, [l’Humanité](https://www.humanite.fr/) en compte 10.

*Note : Le nombre de tracker peut varier par page. Les chiffres donnés ci-dessus correspondent à une mesure prise sur la page d’accueil de chaque site et faite le 18 Juillet 2018. Si vous utiliser un AdBlocker, il faut le désactiver pour voir tous les trackers présents sur un site.*

![Elle.fr \[Weekly women magazine\] — **53 trackers**; Liberation.fr \[Daily newspaper\] — **40 trackers**](img/2018/user-privacy/trackers.png)
Elle.fr : 53 trackers différents détectés – un record ?; Libération est pas mal non plus avec ses 40 trackers

**Souvent, la présence de ces trackers n’est pas connue même des gens qui travaillent sur le site**. Nous avons contacté des publications cryptos françaises de premier plan afin de les alerter quant à leur pratiques dangereuses. Tous sont très surpris de « découvrir » l’ampleur de la traque qu’ils mettent eux-même en place. D’autres diront qu’ils se sont gentillement payés notre tête – à vous de voir.

Ce petit tour au musée des horreurs nous apprend deux choses :

1. Les responsables de 99 % des sites internet n’ont clairement pas le respect de la vie privée de leurs utilisateurs en ligne de mire.
2. Les utilisateurs de ces sites ne sont pas assez sensibilisés aux enjeux que cela représente, ce qui ne crée pas/peu de demande pour des sites plus propres et respectueux de leur vie privée.

Ainsi **le changement, s’il y en a un, viendra des utilisateurs : on doit être exigeant et intransigeant**. Mais pour se faire, encore faut-il savoir contre quoi on se bat, faisons un petit tour d’horizon non exhaustif du pistage en ligne.

### Typologie des trackers

Il y a plusieurs types de trackers, voici les plus courants :

- **Tracker des services de publicité** : ceux-ci permettent aux webmasters (et aux service de pub) d’avoir plus d’information sur ce que vous faites lorsque vous accéder au site : pages vues, boutons pressés, position de la souris, et bien sûr tout un tas d’information sur la machine, la connexion et l’utilisateur. Les plus courants : DoubleClick, et Facebook Ads. On parle plus en détails d’une partie d’entre eux : les pixels.
- **Tracker des services de statistiques** : le plus connu est Google Analytics mais de nombreux autres existent – ils auront le droit à leur propre section plus bas.
- **Tracker des réseaux sociaux** : ils permettent des intégrations directes des services social (comme liker la page Facebook sans quitter le site), mais cela implique aussi que l’internaute est reconnu et identifié (via son profil Facebook/Twitter/autres). Pas besoin d’interagir avec ces boutons pour que la reconnaissance ait lieu, c’est la toute la beauté du mécanisme : souriez, vous êtes trackés.

#### Les statistiques de visite : Un profil très détaillé

Chaque webmaster fait fasse au même problème : il a besoin de statistiques précises pour savoir combien de lecteurs il y a, les pages qu’ils apprécient, d’où ils viennent… Pour se faire la référence est un service proposé par Google : Google Analytics.

L’offre de Google Analytics est simple : Google est expert en collecte et traitement des données – laissez les faire. Il suffit de mettre en place un petit tracker sur votre site, et Google se charge de tout : collecte, traitement et présentation des données. C’est vraiment très pratique et désormais il devient dur de trouver un site qui ne l’utilise pas. Le problème ? Et bien toute la donnée passe par Google : **Google collecte donc directement la donnée à la source sur 99 % des sites les plus fréquentés**.

> **Si chaque site était un bistro, alors c’est comme si on avait un Google Home (Alexa version Google) avec le micro toujours allumé placé au milieu du bar. C’est déjà gênant si ce n’est que quelques bistros/sites, mais cela devient une véritable Stasi du web si tous les sites l’implémentent.**

Il faut avoir été webmaster avec le script de Google Analytics implémenté au mois une fois pour comprendre l’ampleur du profil qu’il permet de dresser sur chaque internaute. Impossible de chiffrer précisément ce que Google appelle les « metrics and dimensions » car cela dépend du paramétrage fait pour chaque site. **Sachez cependant qu’il y en a plus de 400 disponibles.** [La liste est ici (Anglais).](https://developers.google.com/analytics/devguides/reporting/core/dimsmets#mode=web)

Pour ceux qui ont un site à gérer, on propose une alternative dans en fin d’article.

### Publicité et respect de la vie privée : strictement incompatibles

On est passé un peu vite sur les trackers pour les services de publicité alors il fallait y revenir ici. Permettons nous un petit retour aux bases de la pub en ligne :

- Ça se paye par action : coût par clic, coût par mille vues, coût par action spécifique (inscription, téléchargement d’app…)
- Une action n’en vaut pas une autre – un clic peut provenir d’une personne totalement en dehors de la cible du site ou alors au contraire de quelqu’un qui va devenir un fan.
- Les campagnes peuvent être modifiées et mises à jour en temps réel.

Avec ces bases rappelés, on comprend bien vite que : **le** **respect de la vie privée et publicité en ligne sont strictement incompatibles**. En effet, pour rendre la publicité la plus efficace possible, il faut collecter le maximum de données pour pouvoir la cibler de plus en plus et éviter les dépenses inutiles.

![](img/2018/user-privacy/privacy.jpeg)
*À gauche : « Je suis heureux que Facebook s’attaque au problème du respect de la vie privée… » // Au milieu, Zuckerberg, PDG de Facebook annonce à un publicitaire : « Nudiste, marié, 75 000 annuel, bon buveur, possède un minivan, collectionneur de Beanie Babies \[ours en peluche\]… »*

Il ne faut pas se laisser berner pas les envolées lyriques des sites de presse et consorts sur la vie privée – **tous les sites les plus visités en France ont recours à la publicité et utilisent une abondance de trackers divers et variés : en bref ils n’ont aucun respect pour la vie privée de leurs utilisateurs, pire encore – ils la monétisent.**

#### Espionnés par un simple « Pixel »

Pas encore convaincu ? Permettez nous de faire un petit zoom sur un type de tracker bien particulier, les « Pixels » des services de publicité en ligne comme Facebook Ads. Là encore, c’est un outil qui fonctionne un peu comme Google Analytics. Le webmaster met en place un script sur son site et en échange il a accès à des informations détaillés sur la manière dont les gens interagissent avec son site.

L’intérêt pour le webmaster réside dans le faits que ces infos sont disponibles directement sur la plateforme Facebook Ads – ce qui facilite l’optimisation des publicités : c’est donc un incontournable pour quiconque consacre de sérieux budgets à la pub Facebook. Grâce au pixel, le webmaster pourra faire le liens entre une publicité sur Facebook et des actions sur son propre site (inscription, achat, téléchargement…).

Cela pose précisément le même problème que Google Analytics : le pixel de Facebook (et autres) est désormais très répandu, **ce qui donne à Facebook un accès de première main à la données de la plupart des plus grands sites web**.

![An example of a retargeting scenario using Facebook (source: [Lyfe Marketing](https://www.lyfemarketing.com/spa-owners-facebook-customers/facebook-retargeting-example/))](img/2018/user-privacy/pixel.png)
Exemple de retargeting sur Facebook (source: [Lyfe Marketing](https://www.lyfemarketing.com/spa-owners-facebook-customers/facebook-retargeting-example/))

Le pixel permet en outre de faire du **retargeting** : ce terme un peu barbare désigne toutes les formes de publicités où **le ciblage se fonde sur les actions réalisées précédemment par le prospect**. Dans le cas du retargeting via Facebook Pixel, voici le scénario le plus simple :

1. Vous visitez un site donné (mettons pour acheter une tondeuse)
2. Souriez, vous êtes trackés. Grâce au pixel, ce même site sait qui vous êtes sur Facebook : suite à votre première visite sur le site, vous avez été ajoutés à une liste de retargeting.
3. Vous allez sur Facebook et découvrez des promos d’enfer sur des tondeuses à gazon, directement au sein de votre fil d’actualités.

### **Les petites suprises découvertes au PASSAGE**

Avant d’en venir aux outils, faisons un petit détour par un point hautement spécifique qui illustre le défi que représente le respect de la vie privée en ligne. Vous connaissez peut être WordPress ? C’est l’un des frameworks (~moteur) qui permet la création de blogs et de sites [les plus courants](https://managewp.com/blog/statistics-about-wordpress-usage) – ce qu’on utilise sur EcoCrypto pour l’instant.

Par défaut, une installation WordPress utilise un service qui s’appelle Gravatar : il permet à chaque utilisateur du blog (=auteur mais aussi toute personne qui poste un commentaire) d’avoir une photo de profil personnalisé, plutôt sympa, non ?

Sauf que… Pour se faire, Gravatar utilise l’email de l’utilisateur. **Ainsi, par défaut, l’email de chaque nouvel inscrit (ou personne qui commente) sur un WordPress fait un aller-retour vers les serveurs de Gravatar**. Chaque personne peut ensuite aller sur Gravatar.com et associer une photo à son email : et paf – sa photo est partout là où Gravatar est implémentée, en une seule manipulation. Pratique n’est-ce pas ?

Sauf qu’avec l’aller-retour, Gravatar est en mesure de compiler une liste des mails des utilisateurs de chaque installation WordPress – tu la veux toujours ta photo de profil personnalisée ?

[Les alternatives](https://wordpress.org/plugins/wp-user-avatar/) existent et sont faciles à mettre en place, mais comme Gravatar est activé par défaut sur toute installation de WordPress, il reste prévalent. **Le fait qu’il soit installé par défaut couplé à l’ignorance de la pratique permet à Auttomatic (développeur de Gravatar) de se gaver d’emails au dépend de ses utilisateurs, et ce depuis des années.**

Ce type de problème est récurrent en matière de respect de la vie privée : dans l’absolu tout le monde est pour. Dans les faits, peu de gens prenent le temps de s’y intéresser réellement et au niveau des sociétés, le respect de la vie privée n’est considéré que comme un acte de communication mais rarement implémenté au niveau du logiciel même.

### Alors, on fait comment ?

On a essayé de rester concis et pas trop technique : forcément, on a zappé plein de choses et ce n’est pas du tout exhaustif. Des dizaines (centaines?) de techniques différentes existent pour pister les internautes et certaines sont beaucoup plus durs à contrer qu’en installant une extension, comme [le fingerprinting par exemple](https://panopticlick.eff.org/).

Ce qui a inspiré cet article c’est la surprenante complexité de la mise en place d’un simple blog qui respecte la vie privée de ses utilisateurs. **À force de trop laisser le sujet aux experts, on arrive dans une situation où le viol de la vie privée est devenu la norme – à ceux qui veulent la respecter de ramer**. Le tout pendant qu’Apple, Facebook ou Google et consorts se targuent de se battre pour nos libertés individuelles. Regardons la réalité en face : ils organisent méticuleusement un système où le concept même de vie privée deviendra marginal.

Ça fait beaucoup et il va falloir commencer à gueuler… Ou bien on aurait déjà dû le faire il y a 10 ans ? Il n’est jamais trop tard !

### Trousse à outils : Couvrir ses traces en ligne

La bonne nouvelle c’est que couvrir vos traces implique bloquer toute publicité ainsi que tout script qui détecte les bloqueurs de pub. Vivre caché a du bon !

On va donc proposer un ensemble d’extension pour couvrir vos traces, en restant sur le strictement indispensable.

##### 1. bloquer les pubs

On conseille [Nano AdBlocker](https://chrome.google.com/webstore/detail/nano-adblocker/gabbbocakeomblphkmmnoamkioajlkfo) qui marche de pair avec [Nano Defender](https://chrome.google.com/webstore/detail/nano-defender/ggolfgbegefeeoocgjbmkembbncoadlb?hl=en) pour gérer les messages anti-adblock. Il y a aussi [uBlock Origin (Firefox)](https://addons.mozilla.org/fr/firefox/addon/ublock-origin/) parmis les plus courants.

Quelque soit votre choix d’AdBlocker, n’oubliez pas d’activer la EasyListFR pour bien tout bloquer. Voici un petit GIF qui montre la manipulation.

![](img/2018/user-privacy/adblock-fr.gif)

Pour tester votre installation, on conseille [LeMonde.fr](https://lemonde.fr) – environ la moitié du site devrait avoir disparu – si c’est le cas, c’est que tout marche parfaitement : les pubs sont bloquées ! Il vous restera encore les articles sponsorisés et les éditos à charge, mais ça c’est un autre problème.

##### 2. Lister et bloquer les trackers

Les pubs ce n’est que le début. Maintenant passons aux trackers. La bonne nouvelle c’est qu’à ce niveau là on a une extension qui met tout le monde d’accord : [Privacy Badger.](https://www.eff.org/privacybadger)

![](img/2018/user-privacy/privacy-badger.png)

Elle est dévelopé par [l’EFF – Electronic Frontier Foundation](https://www.eff.org/about) qui lute pour la vie privée en ligne depuis des années déjà – ce n’est pas une raison pour avoir une confiance aveugle dans l’extension mais ça rassure quand même un peu. Pas besoin de paramétrage spécifique mais n’hésitez pas à aller voir les trackers trouvés par Privacy Badger et à en désactiver.

*Note : Plus haut, on vous parlait de [Ghostery](https://www.ghostery.com/),* *ça fait aussi très bien le travail.*

##### 3. Utiliser HTTPS, partout

Lorsque vous visitez un site utilisant HTTPS, les échanges entre votre navigateur et le site sont encryptés. L’HTTPS est désormais courant, mais certains sites ne le mettent pas en place systématiquement : ils vous font passer de HTTP à HTTPS et vice versa. [HTTPS Everywhere](https://www.eff.org/https-everywhere), une autre extension de l’EFF résout ce problème : elle force l’HTTPS partout où cela est possible.

##### Dernière notes sur les outils

Pour être rigoureux, préférez [Firefox](https://www.mozilla.org/fr/firefox/) à **Google** Chrome, utlisez le [TOR browser pour les choses sensibles](https://www.torproject.org/projects/torbrowser.html.en) ou idéalement [TAILS si la confidentialité est une nécessité absolue](https://tails.boum.org/) : c’est un système d’exploitation conçu pour vous aider à couvrir vos traces. Si vous voulez passer du coté obscur du web, lisez et renseignez vous bien.

Pour garder l’article concis et accessible, on a choisi 3 extensions vraiment indispensables. Pour être vraiment caché, il vous faudra aller BEAUCOUP plus loin.

On pourrait lister mille autres outils, mais **l’essentiel est de se renseigner et comprendre ce qu’il se passe sous le capot.** À partir de là vous serez à même de savoir quels outils sont adaptés à vos besoins. La vie privée de nos jours, ça se mérite hélas.

En France, on a la chance d’avoir des associations comme la Quadrature du Net qui militent depuis des années pour nos droits en ligne tout en développant leurs propres solutions et guides pour nous aider à sortir couverts : [Controle tes données ! ](https://controle-tes-donnees.net/)

### Pour les Webmasters : Comment respecter la vie privée de ses utilisateurs

Pour ceux qui gèrent un site, l’essentiel est de trouver une alternative à Google Analytics fiable et respectueuse de la vie privée des utilisateurs. Pour EcoCrypto, on a choisi [Matomo](https://matomo.org/) qui est une solution open source et à héberger soit-même. Héberge soit-même sa solution d’analytics, c’est essentiel : les données sur vos visiteurs ne doivent pas quiter vos serveurs.

En fonction de votre hébergeur, cela va être plus ou moins compliqué à mettre en place. Si votre hébergeur supporte [Softaculous](https://www.softaculous.com/), installer Matomo est l’affaire de 5 minutes et quelques clics sinon il faudra avoir ou apprendre quelques compétences techniques.

Pour le reste, tout va dépendre de votre site et du framework qui le fera tourner. Du coup plutôt que de donner une liste d’outils, on propose une méthodologie :

1. **Minimisation des services tiers** : essayez d’utiliser aussi peu de service tiers (les extensions WordPress par exemple) que possible. Chaque service est un vecteur de risque en terme de sécurité du site et pour la vie privée de vos utilisateurs. **Même un service honnête à un moment donné peut devenir marchand-goinffre de données sans prévenir.**
2. **Faire ses recherches sur les services tiers nécessaires** : malgré le 1), vous allez avoir besoin de différents outils tiers. Renseignez vous sur leurs développeurs, faites des recherches pour voir si d’autres personnes en ont étudié le code et ont trouvé des choses suspicieuses, sur les différentes alternatives qui existent. Préférez les services open-source autant que possible.
3. **Oubliez la publicité en ligne sur les services traditionnels** (Social, Google…) – vous ne pourrez pas y être efficace (coût/résultat) sans fliquer vos utilisateurs.
4. **Faites vous aider** – de nombreuses personnes déjà sensibilisées aux enjeux de la vie privée en ligne ne demandent qu’à [aider d’autres à faire de même](https://www.laquadrature.net/fr/contact).
---
title: " Comment évaluer les processus de développement et la stack technique ?"
description: >-
  TODO
date: '2019-02-18T15:00:20.293Z'
categories: [📔 Guide, 🧐 Enquêter avant de signer]
tags: [job research, pre-screening, researching companies]
toc: true
---

En tant que développeur, rechercher un emploi et discuter avec des employeurs potentiels est un manège épuisant : il faut trouver les offres qui correspondent vraiment, les décoder, partir à la pêche à l’information, etc. Au fil de ce parcours éprouvant il vous reste encore à vous faire une idée du fond de la chose : la stack technique et surtout la méthodologie de développement mise en place au sein de la société en question.

C’est assez compliqué de se faire une idée du processus de développement sans avoir mis les pieds dans une société donnée. Pour faire un choix réfléchi le mieux reste encore d’avoir un accès en interne avant de prendre une décision, comme lorsque vous recevez une offre d’emploi à l’issue d’un stage ou d’une mission freelance. En dehors de ces scénarios, il est encore possible d’aller cherche des informations avant de vous décider. Par exemple, lors du recrutement, vous pouvez demander de passer une journée dans les bureaux pour voir comment les choses se passent vraiment.

Pas de panique si ça n’est pas possible, il vous reste des options. Il y a des signaux perceptibles depuis l’extérieur qui peuvent vous livrer quelques indices quant aux déroulement des développements et à la culture de la société. On a écrit ce guide pour vous donner nos tuyaux pour évaluer les processus de développement d’une société, autant depuis l’intérieur que de l’extérieur. 



## ÉVALUER LES PROCESSUS DE DÉVELOPPEMENT D’UNE SOCIÉTÉ, COMME SI VOUS Y ÉTIEZ

Commençons par le plus évident : l’offre d’emploi elle-même.  

### L’OFFRE D’EMPLOI : LE POINT DE DÉPART

La lire avec un œil critique peut en dire beaucoup. Au delà des exagérations habituelles (Marc Jeanson propose un tableau de correspondance hilarant), le diable est dans les détails.



![developer job ads ](/img/2019/csg/dev-job-ads.png)

Sur l’offre, les conditions de travail peuvent vous aider à vous faire une idée de la confiance que l’équipe de management place en ses développeurs. Le temps partiel est possible et les horaires flexibles ou décalées sont envisageables ? C’est généralement plutôt bon signe et ça indique une société qui ne cherche pas à imposer une vision unique du travail à tous ses développeurs.  

Le point le plus éloquent est sans-doute l’attitude vis à vis du travail à distance. Les bénéfices du travail à distance sont nombreux et variés : gain de productivité, réduction des coûts, santé des salarié, etc. (source) L’enjeu est dans sa mise en place. Il y a tout d’abord une question de confiance, comme pour le temps partiel ou les horaires décalées. En outre, avoir des équipes performantes à distance implique également une communication fluide. Une société qui encourage le travail à distance a donc probablement des outils et une méthodologie efficace pour coordonner le travail de ses développeurs.

Quand à la stack, ça vaut la peine de l’éplucher comme il se doit. Par exemple, des fautes d’orthographe dans le nom des technologies et des frameworks indiquent presque certainement une offre écrite par des profils RHs qui n’ont pas pris la peine de faire un aller-retour avec un développeur. C’est de mauvais augure pour la suite de la discussion. Concernant les technologies en elle-même, c’est l’objet de la prochaine section.

### LA STACK TECHNIQUE

Par rapport à la stack présentée sur l’offre, on vous laissera seul juge de sa pertinence vis à vis de votre profil. Pour aller au-delà de ce qui est indiqué dans l’offre, vous avez plusieurs options. 

Si vous êtes un développeur front, la tâche est aisée : une analyse rapide du site et notamment des en-têtes vous donnera les technologies, frameworks et services utilisés. Pour aller plus vite et défricher le terrain, un service comme BuiltWith peut vous aider.

Pour un développeur back la tâche est beaucoup plus ardue : il n’y a rien de public que vous puissiez analyser directement. Il existe cependant des services pour retrouver les stacks techniques des sociétés. Ils fonctionnent le plus souvent sur un mode déclaratif : la donnée n’est donc ni exhaustive ni parfaite.

![devops-stack-stackshare](C:\Users\shylv\Documents\Markdown\Jobs\NEXTEN\ARTICLES\COMPANY_SCREENING_GUIDE\CSG4-rsc/devops-stack-stackshare.PNG)
//WN_devops-stack-stackshare.PNG//

Pour les startups en vogue et notamment les sociétés américaines, StackShare.io fonctionne plutôt bien. Un service comme Siftery peut également vous aider bien que son objet soit plus large : il liste toutes les technologies, SaaS et services utilisés par une société donnée.

### RECHERCHE ET OPEN SOURCE

Pour se faire une idée de l’ambiance au sein de l’équipe de développeur, allez faire un tour sur les différents supports de communication de la société de votre choix. Lorsque les équipes techniques implémentent des pratiques telles que les hackdays ou organisent/vont à des conférences, ils ne manquent généralement pas de le faire savoir. Cela laisse des traces que vous pouvez retrouver comme des articles, des vidéos, ou des posts sur les réseaux sociaux. Ce genre de pratiques permettent de casser un peu la monotonie du quotidien ; elles sont d’autant plus essentielles si le travail à distance est courant dans l’équipe.

N’oubliez pas d’aller voir sur GitHub ou ailleurs si la société que vous analysez contribue à des projets open-source. En dehors de la dimension collaborative, cela traduit généralement une certaine rigueur et expérience dans leurs pratiques. Pour open-sourcer un projet, les revues de code doivent être carrées et la documentation solide.

Enfin, derrière la société il y a aussi des gens qui peuvent vous aider à compléter le profil technique. On détaille une technique pour refaire et éplucher l’organigramme d’une boîte dans notre guide sur les ressources humaines et l’ambiance. \WN-CSG3-RH-LINK\ Elle marche tout aussi bien pour les équipes techniques. Une fois que vous avez le nom des développeurs et décideurs techniques, n’hésitez pas à essayer de les retrouver sur GitHub, StackOverflow voir Reddit. La plupart des gens utilisent des pseudos sur ces sites mais ça vaut quand même le coup d’essayer.

On le mentionnait en introduction, les signes extérieurs restent assez limités. Ils permettent de se faire une idée mais n’offriront pas de certitudes. Pour aller plus loin, il vous faudra un accès à l’intérieur de l’entreprise. C’est l’objet de la deuxième partie.

## LES SIGNES D’UNE MÉTHODOLOGIE DE DÉVELOPPEMENT DÉFAILLANTE

La bonne nouvelle c’est qu’une fois dedans pas besoin d’y faire des vieux os pour réaliser si l’équipe technique est bien rodée ou si elle va dans le mur : quelques jours ou semaines suffiront.

### LA MÉTHODE AGILE PAS SI AGILE QUE ÇA

On commence par un concept tellement entendu qu’il déclenche presque des grognements rien qu’à être prononcé : la méthodologie de développement agile. Sur le papier et dans les offres d’emplois, toutes les sociétés s’en disent adeptes. En réalité ce n’est bien souvent qu’un vœu pieux voir un argument marketing.  

Adopter la méthode agile c’est plus qu’une simple gestion de projet avec des cycles raccourcis : cela implique un changement de vision et de méthodologie. Pour revoir les bases, on vous invite à lire l’introduction proposée par Trello, qui est claire et vous propose de bonnes sources pour approfondir.

Ainsi, on peut retrouver tous les éléments de la méthode agile dans une société qui, dans les faits, est encore loin du compte. Chaque outils et concepts de la méthode sont repris, mais la vision se perd dans l’implémentation. Faisons un petit tour d’horizon des signes d’une agilité qui s’est perdue en route :

#### LES DAILY STANDUPS À RALLONGE

Un des éléments clef du framework Scrum ce sont les meetings journaliers, normalement debout (« standups » ) qui se doivent d’être rapides et efficaces. Normalement un standup c’est environ 1 min par personne pour faire le point sur ce qui a été fait et ce qui va être fait. On ne rentre pas dans les détails techniques, le but est simplement de partager son avancement et ses points bloquants.


Dans les faits, on se retrouve souvent avec des standups qui durent beaucoup trop longtemps ou deviennent le lieu de discussion sur les choix techniques. Cela traduit l’absence d’un Scrum Master apte à cadrer les équipes dans leur échanges et à les former à la méthode.

#### DES OUTILS AGILES ?

En termes d’outil, la méthode scrum implique un tableau Kanban pour suivre l’avancement des tâches. Il peut être physique, mais le plus souvent on utilise un service comme JIRA :



![jira](/img/2019/csg/scrumboard.png)



Si vous avez accès aux tableaux de l’équipe de développement, prenez le temps de les analyser. Lisez quelques tickets pour voir si vous y comprenez quelque chose. Cela vous permettra de vous faire une idée de l’efficacité de l’organisation de l’équipe.

Les revues de codes sont également à surveiller de près. Idéalement, on fait des revues de codes croisées : personne ne merge son propre code. C’est un autre développeur qui le fait, afin de vérifier que le code soit propre et convenablement documenté. Ces revues de code doivent avoir lieu le plus tôt possible, avant même la fin du développement de la fonctionnalité. Cela permet de repérer les problèmes de méthodologie de développement en amont.  En outre, cela rend l’équipe responsable et permet de s’assurer que tout le monde a une bonne compréhension, à terme, de l’ensemble de l’infrastructure.

#### LE PRODUCT OWNER : UN RÉFÉRENT UNIQUE

La mise en place d’une méthodologie agile implique deux rôles essentiels : le scrum master qu’on a déjà mentionné et le product owner (PO). Ce dernier représente les intérêts du client : il a autorité pour définir les fonctionnalités du produit final. Il est responsable de la « backlog » (cahier des charges), c’est à dire en bref qu’il définit les tâches et leur priorisation.

Cela suffira pour les rappels théoriques, voyons plutôt les écarts qu’on observe en pratique. Le problème le plus courant est sans doute celui du faux product owner : un PO qui n’a pas l’autonomie nécessaire à sa fonction. Il doit faire valider ses décisions par un supérieur (lead-dev, ou CTO) ce qui réduit (détruit ?) l’agilité et ajoute une couche hiérarchique qui n’a rien à faire là. Dans la même veine, on a parfois plusieurs POs, ou un PO flottant ou encore un PO mal défini.

### L’INTÉGRATION CONTINUE (CI)

La méthode Scrum est souvent associée à une logique d’intégration continue : plutôt que d’implémenter les changements sur l’application par lots, chaque développement est implémenté dès qu’il est finalisé. Le plus souvent, une telle approche est rendue possible grâce à un système de container pour uniformiser les environnements de développement (Docker est de très loin le plus commun) et divers autres outils comme Travis ou SemaphoreCI.

La première difficulté réside dans la mise en place de Docker, partout. Cela permet de s’assurer que l’environnement est uniforme, des machines de développement à la production. Souvent, Docker est utilisé sur les machines de développement mais plus rarement sur le staging ou en production. Les développeurs n’ont ainsi pas la main sur l’environnement final ce qui complexifie grandement la tâche.

Avec une logique de container bien implémentée, il n’y a que très peu de différences entre les environnements. Passer de l’environnement de développement au staging, puis du staging à la prod ne devrait prendre que quelques minutes.

### INFRASTRUCTURE DE L’APPLICATION

L’intégration continue va souvent de pair avec une infrastructure constituée de micro services. L’application est composée d’une multitude de « petits » services. Ils sont souvent spécialisés dans une seul tâche. Ils communiquent entre eux via des API, le plus souvent REST.  


![microservices](/img/2019/csg/microservices.png)

Outre les gains en terme de sécurité et de fiabilité de l’application, cela facilite également grandement la maintenance de celle-ci. Il devient ainsi possible de faire évoluer l’application service par service et cela facilite grandement la coopération. En outre, cela permet également à un développeur de devenir rapidement opérationnel sur le produit puisqu’il n’a besoin de se familiariser qu’avec un seul micro service pour commencer à contribuer.

À l’inverse, une architecture plus monolithique complexifie la prise en main et l’intégration du travail de nouveaux développeurs. Elle constitue un risque de plus en plus critique au fur et à mesure que le projet gagne en ampleur. Soyez attentifs à l’infrastructure générale de l’application et évitez les masses uniformes autant que possible.



### LA SÉNIORITÉ DE L’ÉQUIPE

On finit avec un point essentiel : l’expérience des équipes. Trop souvent en startup, on a des équipes de développement très junior avec un lead-dev/CTO à peine plus expérimenté que ses collègues. Cela n’est pas forcément synonyme d’un échec assuré mais ça augure souvent de nombreuses hésitations et aller-retours sur les choix techniques.

En outre, avoir un profil expérimenté à bord permet aux profils plus juniors de monter plus rapidement en compétence. Savoir se débrouiller par soi-même est une capacité appréciable mais ça ne doit pas être une fatalité. Sans abuser, il devrait y avoir quelqu’un disponible pour vous aider lorsque vous êtes bloqués sur un sujet donné.

## ALLER AU DELÀ DU CODE

On ne vous apprendre rien : plus que le code en lui-même c’est la méthodologie qui encadre le développement qui importe quant à la qualité du rendu final. On espère néanmoins vous avoir apporté quelques indicateurs utiles pour apprécier les méthodes de développement de la société de votre choix.  

Une boîte, c’est (hélas ?) plus que du code. Il faut aussi des gens pour faire connaître le produit, le mettre dans les mains des bonnes personnes pour qu’il soit utilisé et apprécié. Parfois, le code est solide mais c’est le marketing qui est à la ramasse. Pour éviter de telles situations, on a écrit un [guide pratique pour vous aider à jauger l’efficacité du marketing d’une startup](({{< relref "csg-mkt1.fr.md" >}})). 

Bonne nouvelle : c’est bien plus facile que pour les processus de développement.  
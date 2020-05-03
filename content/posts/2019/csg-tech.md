---
title: 'How to evaluate the development process and technical stack of a company'
description: >-
  TODO
date: '2019-02-18T15:00:20.293Z'
categories: [📔 Guide, 🧐 Spy Before You Sign]
tags: [job research, pre-screening, researching companies]
canonicalUrl: https://nexten.io/blog/spy-before-you-sign-how-to-evaluate-dev-process
toc: true
---

As a developer, looking for work and discussing with potential employers is exhausting: you need to find job offers that correspond to your wishes, and to do so, you need to decode them by fishing for information on the web or other references. For a technical job, the most relevant piece of information is of course the tech stack and the development methodology that is applied within the company.



[Vous parlez français ? Lisez cet article dans votre langue]({{< relref path="csg-tech.fr.md" lang="fr" >}})



Without having seen the company from inside, evaluating their development process seems a complicated task. To make the most calculated choice, the most helpful input is indeed an access to the inside of the company in question. This is the case when you get a job offer right after an internship or freelance contract, and otherwise, when having a first interview, you can always ask to spend a day in the offices in order to see how work is done.



No worries if that’s not possible, there are more options! There are signs that give you an idea about internal work flows and company culture and good news: they can be observed from the outside. This guide will help you identify the development processes of a company from the inside and outside.



## Evaluating development processes of a company, like you were a part of it



Let’s start with the most obvious: the job offer.



### The Job offer



When looking at job offers with a strong sense of criticism, they unveil a great deal. Marc Jeanson wrote a hilarious interpretation of the typical wordings, and even though he might be exaggerating, truth is that the devil is in the details.



![developer job ads ](/img/2019/csg/dev-job-ads.png)



The working conditions for instance give you an idea about how the management trusts their developers. Part-time and flexible hours are usually a sign that the company does not impose one way of working to all their developers, because upper management understands that every developer likes working in his style.



The most significant aspect certainly is the attitude towards remote working. The benefits are numerous and undeniable: productivity gain, cost reduction, well being of employees, etc. ([source](https://www.forbes.com/sites/andrealoubier/2017/07/20/benefits-of-telecommuting-for-the-future-of-work/#280a08d16c65)). The efficiency of remote working depends on its implementation. First, it requires trust, just like for part-time and flexible hours. Then there’s mastering a frictionless communication, which is the key to productivity gain. A company that promotes remote working is therefore very likely to have put in place efficient methodology and tools to coordinate their remote workers and can be seen as well organised and understanding the needs and preferences of today’s rockstars: you developers 😎.



When it comes to the tech stacks in the job offers, it sure is possible to make some conclusions on their commitment. Typos in the technology & framework names usually mean that the job offers has been written by an HR profile, which did not consider a developers opinion on the job post – a very bad sign for the next steps in the recruitment process.



### The Tech Stack



As for the technologies mentioned in the job offer, obviously it’s up to you to decide if they match with your preferences and skills. There are however more ways to check the tech stacks beyond the job description.



If you’re a frontend developer, it’s pretty straight forward: quickly have a look at the website. Here, especially headers will present to you the used technologies, frameworks and technologies. A service like [BuiltWith](https://builtwith.com/) will help you to explore them even faster.



Looking into the backend is by definition a little more complicated – there is nothing public to analyse. There exist however services that will let you discover tech stacks of companies. The catch is that they are mostly declarative and the data is thus not exhaustive nor perfect.



![devops tools](/img/2019/csg/devops-stack-stackshare.png)



For trending startups and American companies, [Stackshare](https://stackshare.io/stacks) works pretty well. While addressing a broader use, a service like [Siftery](https://siftery.com/) can also help you. It lists all technologies, SaaS and services a company uses.



### Research and open source



In order to get an impression of the culture of the developer team, you should have a look at the communications done by the company. If the tech teams implement things like hackdays or visit/organise conferences, there’s usually a good atmosphere in the team. Evidence can usually be found on social media in the form of articles, videos and photos. Such practices help to break down the daily monotony and are a good way to bring the team together (especially for remote teams).



Do also not forget to check GitHub or others for open-source projects the company contributed to. Next to the collaborative aspect, this usually means rigorousness and experience in execution as open-source projects demand a meticulous code review and a solid documentation.



Behind a company there’s always people, who can be used to complete the tech profile of the company in question. The method to recreate and understand a company’s organisational chart ([explained in our guide on HR and atmosphere)]({{< relref "csg-hr.md" >}}), works perfectly well for tech teams as well. Once you identified the developers and decision makers, find them on GitHub, StackOverflow or even Reddit. They will mostly use nicknames, but if you can find them, you will gain great insights.



While the insights gained from the outside of the organisation are a good start, they are not a 100% reliable. That’s why in the second part of this guide, we’ll focus on accessing the internal stuff. Go.



## Signs of a failing development practices



The good news is, once inside the organisation, some days or weeks are enough to tell if the tech team is working efficiently or if they are not up to the task.



### The not so agile Agile approach



Let’s start with the methodology that is so common that is doesn’t mean much anymore: Agile Development. On paper and in the job descriptions, almost every company follows the practice, but in reality it’s often only a good old marketing pun.



Adopting Agile development is more than just simple project management with short cycles: it implies a vision and perspective shift. To recheck the basics, we suggest to read [Trello’s introduction](https://blog.trello.com/beginners-guide-scrum-and-agile-project-management) to the topic. It’s clear and presents nice sources to dive deeper into the subject.



All its tools and concepts are explained, making it simple to spot signs of a bad execution of the methodology. Below, we’ll list the signs that point to an not so agile Agile execution.



#### The extended Daily Standups



A key element of the Scrum framework are quick and efficient daily meetings. During these so called standups every person has one minute to explain what has been and will be done. The goal  is not to enter into technical details.


Instead of simply sharing one’s progress and the things that are blocking it, the standups often take too long or turn into discussion on technical choices. This means that a Scrum master is missing in order to limit the exchanges and teaching the methodology.



#### Agile tools?



The scrum method implies a Kanban board in order to follow progress. It can be physical, but usually a service like JIRA is used:



![jira](/img/2019/csg/scrumboard.png)



If you have access to the development board, take the time to analyse it. Read some tickets to check if you understand them. The way they are written tells you much about efficiency and organisation of the team.



The same goes for code reviews – have a close look. Ideally, no one merges his own code. It should always be another developer to make sure the code is sufficiently documented. These code reviews should take place as soon as possible, even before the end of functional development. It helps to point out methodology problems before hand. On top of that, it makes the team responsible and verifies that everyone, in the long term, understands the whole of the infrastructure.



#### The product owner: a unique reference



There are two essential roles to put into place an agile methodology: the Scrum master who we already mentioned and the product owner (PO). The latter represents the client’s interests and thus has the final say on the functionalities of the final product. He’s responsible for the backlog, i.e. defining the tasks and their prioritisation.



Enough theory, let’s get to the practical. The most common problem is the fake product owner: a PO who is not autonomous in his position. If the PO needs validation by a superior (lead dev, or CTO), agility is reduced (lost?) and it adds a layer of hierarchy (the enemy of agility). With the same logic, another negative sign would be multiple POs, a semi PO or even a badly defined PO.



### Continuous integration (CI)



The scrum methodology is often linked with continuous integration: instead of deploying changes to the application in batches, every development is deployed when it’s done. In most cases, this approach is enabled by a container system which standardises the development environments ([Docker](https://docker.com/) is by far the most used) and some other tools like [Travis](https://travis-ci.org/) or [SemaphoreCI](https://semaphoreci.com/).



The first step is putting Docker into place everywhere, so the environment is standardised from the development machines to production. Often Docker is only used on the development machines and not on staging or in production, meaning that developers are not developing in the final environment.



### Application infrastructure



Continuous integration often goes hand in hand with an infrastructure consisting of multiple micro services, which are often specialised in a certain task and are communicating between each other via APIs (most often REST).



![microservices](/img/2019/csg/microservices.png)



Other than improving the security and liability of the application, they also simplify its maintenance. It’s possible to develop the application service by service which greatly facilitates cooperation. Moreover it also enables developers to be operational in a short matter of time, because they just have to familiarise themselves with one micro service to start contributing.



On the contrary, a more monolithic architecture complexifies the work and its integration for new developers. Its a risk that grows with the size of the project. Better be careful about the overall application structure and avoid monolithic apps.



### The team’s seniority



Let’s finish with an essential aspect: the experience of the team. Too often, development teams in startups are too junior with a Lead Dev/CTO who is barely more experienced than his colleagues. This does not necessarily equal failure, but most certainly entails hesitations and much back and forth on technical choices.



Furthermore, an experienced team member allows younger colleagues to evolve their competences quicker. To find a solution all by oneself is appreciated, but can be a huge blockade at times. There should always be someone you can talk to if you are blocking for a longer period on a subject.



## Diving deeper than code



It's clear to you: more than the code itself, it’s the methodology guiding the development that improves the final quality. We hope to have given you some nice ideas about how to evaluate the development methods of your chosen company.



In the end, a company is more than code (unfortunately😥). There is also need for people who communicate the product to the right people for it to used and appreciated. Sometimes the code is solid but the marketing team f---s up. To avoid such situations, we wrote a [guide on how to evaluate a company based on marketing efficiency.]({{< relref "csg-mkt1.md" >}}) Good news: it’s much easier than doing it by development processes.



As a final note, in order to avoid having back and forth discussions with HR profiles, we offer an approach that is completely different: first discussing with a tech profile, so you immediately know if the project is for you or not. On [Nexten](https://nexten.io/?utm_source=blog&utm_campaign=CSG) there is no middleman. Developers are directly contacted by CTOs or Tech Leads, so the discussion starts with Tech.
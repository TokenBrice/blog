---
title: The Edge of the Static Web
date: '2019-03-18T09:44:14.735Z'
description: Go static to dramatically improve performance, indexation, and rendering consistency
tags: [web development, static websites, static web, dynamic websites, Gatsby, Jekyll, Hugo, Forestry, Netlify]
categories: [Analysis]
---

`This article is the second of a series which examines the technical reasons behind the renewed interest for static websites, from both a content writer and a developer perspective.
It also provides you with useful tools and services to build a static website. If you want to learn more about the macro perspective behind the shift toward the static web, feel free to read:`

[Static web - back to the roots?]({{< relref "static-roots.md" >}})

### Static websites serve their purpose better

Let's leave the tech aside for a second and take a step back. What's the first goal of a website? Let me gonna risk the "to be seen and read" answer. So then how can speed and performance be so much overlooked? It's a direct factor in the equation.

Consider for instance the New York Times, which is far from the worst in terms of development practices. Let's load the same page ([Health Section](https://www.nytimes.com/section/health)) in two different "versions":

1.  The full one, including all trackers, ads, and unnecessary scripts. Rendered using Chrome, private browsing with no extensions.[^1]
2.  The cleaned one, using Firefox and several extensions to remove most advertisements, tracking and other unnecessary scripts.[^2]

_The tests were realized on my laptop with a connection speed of ~7 Mbps upload/download._

Here are the eloquent results:

|          /           | **FULL/BLOATED VERSION** | **BAREBONE/SUFFICIENT VERSION** | **OBSERVED Δ** |
| :------------------: | :----------------------: | :-----------------------------: | -------------- |
| **PAGE WEIGHT (MB)** |           4.9            |              1.01               | 79% lower      |
|  **NB OF REQUESTS**  |           295            |               25                | 91.5% lower    |
|  **LOAD TIME (S)**   |           5.21           |              2.07               | 60 % lower     |

The results we observe are consistent with our experimentations. **Static websites are about 10 times lighter than their dynamic counterpart.** So how comes dynamic became the standard, especially during the 2005-2015 period where the connection speeds were still limited?

### From the Dynamic Heresy

If you think about this from today's perspective, the whole thing is absurd - the very existence of WordPress is essentially senseless, considering its primary usage. Instead of looking at the issue from the perspective of static websites being relevant, it's much clearer with the tables shifted: **dynamic websites are unnecessary in 95% of their current usage scenarios.**

Of course, there are specific situations where having a dynamic website is a necessity - any case you want to render a user input for instance, like a forum or a board. **However, the default behavior should be to build a static website**.

Indeed, if your content is static (= rarely changed once published, like most websites), why choose a dynamic engine? All your users see the same pages every time. So, using a dynamic engine **means that it forces a computation on both the server and user side every time a page is rendered**: it is incredibly wasteful and irresponsible.

On the other hand, a static website is built once on deployment and then simply served to all its viewers. It dramatically reduces the resource and network usage both for the server and the user.

So how did we get there?

Well it's a tricky question but **mostly a matter of convenience.** Back in 2005 and until recently, dynamic websites were all the rage. New frameworks were popping up everywhere, and clients wanted to offer an incredible experience on their website, often at the expense of performance.

So, when a developer was tasked with building a new website, he would look at the available building blocks and find shiny dynamic rendering engines. Going static back them was almost like reinventing the wheel with each development.

### To the Static Serenity

#### Organic Performance

The overall speed and resource usage of a website have a tremendous impact on its organic performance. It was true 10 years ago, but it is even more now with the rise of mobile — **poor performance destroys the average time on page, therefore annihilating the CTR** (Click-Through-Ratio)… That is if the page manages to rank in the first place.

I've been working in SEO for the last few years, and I already so considerable shifts in the industry. When I started, we could grab the first spot with a well-written and researched content piece on a long-trend keyword, using a bare WordPress and requiring little to no backlinks. Nowadays the competition is intense: every detail counts, and none can be overlooked.

**A website performance is like a K-factor affecting all potential interactions users can have with it.** Platforms like WordPress emerged to allow people to create websites without having to worry about this. Paradoxically, after years of development, such frameworks are now so bloated that they require an intense and complex optimization process — they are no longer accessible to non-tech profiles.

On the other hand, **most static website generators are able to build websites complying with SEO best practices, out of the box**. This includes sitemap.xml/robots.txt generation, OpenGraph, Twitter Cards, Schema.org (rich previews), taxonomies, href lang/multilingual markup and others.

So we reached the current weird situation where despite WordPress' relative simplicity, the most straightforward option to build a blog that will be read is actually to create a static website, even for non-developers.

## Static Websites - Resources and Services

Now that you have the data, you might be considering a switch to static? Welcome aboard! The next section introduces resources that will help you build a blazing fast and optimized static website.

Since the release of Jekyll in 2008, the framework adopted by GitHub, static websites are gaining traction. New frameworks and services have been developed to facilitate the conception of a static website:

### Static Websites Engines

| Logo                                               | Framework                                         | Language | Description                                                  |
| -------------------------------------------------- | ------------------------------------------------- | -------- | ------------------------------------------------------------ |
| {{< figure src="/img/2019/staticweb/jekyll.png" alt="Jekyll Logo">}}   | [Jekyll](https://jekyllrb.com/)                   | Ruby     | Available as a Gem or integrated with GitHub Pages. Jekyll is fast and efficient but offers minimal features out of the box. Many plugins are offering additional functionalities. |
| {{< figure src="/img/2019/staticweb/gatsby.png" alt="Gatsby Logo">}}   | [Gatsby](https://www.gatsbyjs.org/)               | React    | Along with Jekyll, Gatsby is the most popular static website framework. It offers very good performance and a large range of plugin as well as integrations with many third-party services. |
| {{< figure src="/img/2019/staticweb/hugo.png" alt="Hugo Logo">}}       | [Hugo](https://gohugo.io/)                        | Go       | Hugo puts forward its impressive performance, especially while building large websites. It offers anything you need to build a website compliant with SEO best practices out of the box. |
| {{< figure src="/img/2019/staticweb/hexo.png" alt="Hexo Logo">}}       | [Hexo](https://hexo.io/)                          | NodeJS   | Another fast static website generator with a built-in package manager to install plugins and themes. |
| {{< figure src="/img/2019/staticweb/pelican.png" alt="Pelican Logo">}} | [Pelican](https://docs.getpelican.com/en/stable/) | Python   | Pelican is another interesting alternative for pythonistas however it doesn't have as many much third-party resources available (themes, plugins…) as the previous ones. |

Static websites are also a perfect fit for documentation or e-books. Some frameworks were explicitly developed for the purpose, such as [GitBook](https://www.gitbook.com/) or [Docusaurus](https://docusaurus.io/).

{{< figure src="/img/2019/staticweb/gitbook-screen.png" alt="GitBook Preview" title="Preview of a website built with GitBook">}} 

Finally, if you want to explore all potential options, [check this excellent, exhaustive database](https://www.staticgen.com/) maintained by netlify (more about them below). 

### Content Management System

Once your website is up and running, you might want to implement a content management system so that your editor can easily submit new pieces of content. If you are a developer building a blog for yourself, you probably don't need a CMS. However, they are convenient for those who make sites maintained my non-technical profiles.

{{< figure src="/img/2019/staticweb/forestry-screen.png" alt="forestry CMS" title="Preview of the editor interface on Foresty">}} 

#### A Git repository, the base CMS

Using a Github (or Gitlab) repo as your CMS comes with many advantages over a traditional CMS, including among others: 

-   Version control, 
-   User and permission management,
-   Branches (staging, pre-prod, prod)
-   Access to the full files' history.

It can seem intimidating if you have non-technical profiles interacting with your website, but it doesn't have to be: **they don't have to use the Git CLI to push a commit,** they can do all of it from Github's website. We cover in depths the writing/editing flow of static websites in 🔴 -> StaticWebsite_MKT.md /WN/.

#### Alternative CMS

If a git repo is too limited for your needs, you can consider one of the following alternatives. They are all built on top of a repo, so using a git repo as CMS should be your first step.

| Logo                                                 | Name                                       | Description                                                  |
| ---------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------ |
| {{< figure src="/img/2019/staticweb/netlify.png" alt="Netlify Logo">}}   | [Netlify CMS](https://www.netlifycms.org/) | A CMS built for static website generator able to integrate with the most common frameworks. Netlify is a pretty exhaustive suite of services for static websites including tools for CD/CI, user management (CMS), forms and images management. |
| {{< figure src="/img/2019/staticweb/forestry.jpg" alt="Forestry Logo">}} | [Forestry](https://forestry.io/)           | A compelling alternative to Netlify that focuses on the UX of the editor. Forestry is a great choice if you are looking for a visual CMS to facilitate the contributions of non-tech profiles to a static website. Forestry also includes other tools, as Netlify does. |
| {{< figure src="/img/2019/staticweb/vapid.png" alt="Vapid Logo">}}       | [Vapid](https://www.vapid.com/)            | a third alternative that focuses on simplicity. Vapid is a "pure" CMS, made "for people who build websites for other people". Vapid is easy to customize and maintain, as it only uses HTML tags to function. |

### Continuous Integration & Deployment

Both [Netlify](https://www.netlify.com/) and Forestry offer a continuous deployment service integrated with their CMS. They are usually the two most suitable options if you are building a website that will be maintained by someone else.

However, if you are simply looking for a CI/CD solution and don't need the CMS you can either use Netlify without its CMS component or consider the usual CI/CDs services that all offer resources facilitating the support for static websites:

| Logo                                                      | Name        | Resource                                                     |
| --------------------------------------------------------- | ----------- | ------------------------------------------------------------ |
| {{< figure src="/img/2019/staticweb/semaphore.png" alt="Semaphore CI Logo">}} | SemaphoreCI | [Official Documentation - Continuous Deployment of a Static Website](https://docs.semaphoreci.com/article/97-continuous-deployment-static-website) |
| {{< figure src="/img/2019/staticweb/CircleCI.png" alt="CircleCI Logo">}}      | CircleCI    | [Blog Post - Automate Your Static Site Deployment with CircleCI](https://circleci.com/blog/automate-your-static-site-deployment-with-circleci/) |
| {{< figure src="/img/2019/staticweb/codeship.png" alt="CodeShip Logo">}}      | CodeShip    | [Blog Post - Continuous Delivery for Static Sites](https://blog.codeship.com/continuous-delivery-for-static-sites/) |

### How CALLR build their tech blog

Check this post to see some tips on how we built our own tech blog, using [Hugo, Docker, and GitLab](https://blog.callr.tech/static-blog-hugo-docker-gitlab).

[^1]: Base Rendering of `https://www.nytimes.com/section/health` using `Chrome Version 72.0.3626.121 (64-bit)` {{< figure src="/img/2019/staticweb/nyt-bloated.png" alt="nyt-bloated" title="Preview of the NYT-health section, BLOATED version">}} 
[^2]: Ad and tracker-filtered rendering of `https://www.nytimes.com/section/health` using`Firefox Version 65.0.1 (64-bit) using uBlock Origin and Privacy Badger` {{< figure src="/img/2019/staticweb/nyt-light.png" alt="nyt-light" title="Preview of the NYT-health section, LIGHT version">}} 
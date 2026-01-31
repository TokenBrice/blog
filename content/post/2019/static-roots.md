---
title: Static web - back to the roots?
date: '2019-03-04T09:44:14.735Z'
description: Exploring the shift back to static site generators to sanitize web development practices
tags: [web development, static websites, static web, SEO, Markdown]
categories: [Analysis]
image: /img/2019/staticweb/jamstack.png
url: static-roots
difficulty: "beginner"
---

`This article goes back to the early years of the web to understand why dynamic websites are so prevalent today. Then, we consider what static websites bring in terms of performance, editing speed, and organic results.`

At first, the web was static.

The early days Internet was a place for tinkerers. Despite the frequent comparisons between MySpace and Facebook, the two services are fundamentally different. They are also a **good representation of the "Internet Paradigm" of their respective time of fame**.

Both are social networks, yet creating a page on MySpace required a basic understanding of HTML and CSS. The service was launched in 2003 after all. On the other hand, Facebook's easy to use interface contributed to its success and helped it reach 2+ billion users.

Behind the MySpace/Facebook antagonism lies on the most critical point of tension on the internet - **how to interact with the content we edit?** There are mostly two ways to look at this:

1.  **WYSIWYG (What You See Is What You Get)** — As the name suggests, in this paradigm the goal is to have an editor as close as the final rendering. WordPress was one of the most visible early proponent of WYSIWYG, but others joined. The Medium editor (featured below), built using [TinyMCE](https://en.wikipedia.org/wiki/TinyMCE), is now regarded as one of the best WYSIWYG experience available online. 
2.  **Efficiency First** — WYSIWYG editors are easy to get started with but tend to be either clunky or limited. Ultimately, introducing some form of syntax adds complexity, but it also allows more control over the final rendering of the content. Moreover, since the formatting is enforced with syntax (HTML, CSS, Markdown…), it's no longer dependent on the editor used.

{{< figure src="/img/2019/staticweb/mediumeditor.png" alt="Medium Editor" >}}

## The Dawn of WordPress

WordPress quickly took over the web: it currently holds about 60% of the CMS market share. WordPress is so commonplace that we can even look at it from a venture point encompassing the whole web: **about a third of all websites use WordPress**.[^1]

Success does not mean relevance. Indeed, power users are leaving WordPress in drove for various reasons:

-   **Editing**: The WP Editor, even the new Guttenberg, is a pain. It's slow, clunky, and comes with a convoluted block logic. Using it to format and edit content results in a pure waste of time considering the alternative options. Besides, it does not support any "smart feature" by default such as footnotes or tables of content. They require an absurdly complex workflow or yet another plugin.
-   **Security**: Because of its success, WordPress is a prime target for hackers. Any large WP-based website will have to implement additional measures (plugins?) to handle different types of attacks. Moreover, WordPress supports all version of PHP ranging from 5.2.4 (released 12 years ago) to 7.2. Cross this with all the potential plugins and themes, and you get an endless list of attack vectors. Here is an [overview of the most common ones](https://kinsta.com/blog/is-wordpress-secure/).
-   **Performance**: Out of the box, WordPress performance is atrocious. With some plugins (cache, CDN…) and other settings you can speed it up - but is it your job? **Isn't the point of a web framework to minimize the optimization effort?**
-   **Plugin Bloat**: Because of all the plugins WordPress requires, it ends up slowing down the website and hindering security. **A fresh WP install needs 5-10 plugins to be usable and 10-15 to be "optimized"**.[^2]

## Make It Static!

Back when WordPress was released in 2003, the competition was unconvincing. However, this was 15 years ago. In the meanwhile, we saw exciting **tools and frameworks emerge both to format written content and to host and render it for the end-user.** It's the development of both, hand in hand, that paved the way for the static web. 

Let's start with editing, focusing on Markdown.

### The Rise of Markdown

While WordPress was getting fatter and fatter, alternatives developed both to host website and format content. 

For the content, new lightweight markup languages like Markdown offer a credible alternative even for a non-technical profile. Markdown's promise is simple: take an hour to [master the cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) to cut down formatting time to virtually 0. 

Indeed, Markdown is reasonably straightforward, quick to master yet incredibly potent. A writer using a markdown editor and some shortcuts can write and format its content at the same time. On top of that, Markdown offers many exporting options (HTML, PDF, LaTex, Doc…) and ensures that your formatting stays consistent whatever the end format is.

Finally, it might seem, but it's not given: with markdown you can handle text-related features (footnotes, tagging, linking to a section, table of contents, diagrams and charts) at the document-level instead of having to interact with yet another layer. **It dramatically improves the maintainability and portability of your content.**

{{< figure src="/img/2019/staticweb/jamstack.png" alt="JAMStack" >}}

### Version control is not just about code: writers love it too!

Version control and git-based development rapidly developed in the software world for solid reasons. It makes the whole development process more reliable and safe. Furthermore, the user permission management system, the branch logic and the access to the full file history as well as the ability to compare files between to versions are incredibly useful to avoid breaking changes or fix them.

While the developers got all these fancy new tools, us writers were still editing our articles in Word to copy paste it in the WordPress WYSIWYG editor and then start our formatting struggle. Why not share the goodies?

Indeed, as paradoxical as it can seem, a Github repo makes for a very compelling CMS:

-   **Easy User/Access Management**. The branch logic fits the editing process. For instance, if there is a need to keep a tight grip over the content published, the merging power on the master branch can be granted only to the chief editor to ensure consistency.
-   **Branch Logic**: while using a repo as a CMS, branches can serve various purposes. It's possible to use one branch as a staging environment so that the writers can see the final rendering of their content on their machine.
-   **File History**: with GitHub repos, you can access the whole history of a file and easily compare two versions. It is handy, especially if your blog has a lot of different contributors.
-   **No setup**: the repository can be opened in a click. From here, another click with a service like [Netlify](https://www.netlify.com/docs/deploy-button/) is enough to have a blog up and running.

## Beyond the lack of performance lies exclusion

So far, we stayed very pragmatic as we addressed static websites' benefits in terms of performance or increased efficiency. Let's take a step back and consider the big picture for a minute.

The average website size is now well over 3 MB[^3] (as 2017). **More the size itself, the macro-level issue lies in the trend**. Here is the evolution of the average website page since 2011 for reference[^3]:

{{< figure src="/img/2019/staticweb/pagebloat.png" alt="Web performance page bloat" >}}

To give you a reference for comparison on blog.call.tech, our homepage weights 10 KB and an average page (image included) weights about 400 KB.

>   Why do I need to download a full and bloated 3+ MB page to get simple textual information that might be just a few bits?

You and I are sitting here, probably on a modern laptop/smartphone with a decent connection. What about those who live in countries where the Internet service is poor? Most of the Internet is made of text; it should be lightweight. Why do I need to download a full and bloated 3+ MB page to get simple textual information that might be just a few bits?

#### Mind the people using your websites

It might seem like a first world problem; in reality, it's a terrible third world problem. **Poorly designed websites result in the exclusion of regular people from services they could benefit from.** Moreover, the unnecessary data usage bloats the network creating congestions, higher demands and eventually pushing the price of the service up.

Let us go as far as stating this: **publishing an unnecessary dynamic website in 2019 is an abuse of a common good.** The Internet network is a shared resource, why don't we try to avoid another tragedy of the commons using nothing more than common sense?

##### Slow websites are lonely

So let us merely ask a question to those who design those websites 12-times more massive than they should be: why so much hate? In perfect conditions, **the average Internet user with his 7.2 MB/s average connection will need more than 3 seconds**[^4] to get one page.

What's the impact? Neil Patel, a well-known figure in the SEO community, produced a very comprehensive info-graphics covering this topic.[^5] He estimates that **40% (53% on mobile) of users abandon a website that takes more than 3 seconds to load.** So crossing the two numbers, you get the following absurdity:

**News, media and other sites are loosing up to 40% of their potential traffic because of their poor performance stemming from their baseless choice of a dynamic rendering engine. This figure does not include the organic traffic lost because of a lack of SEO-compliance.**

So let's skim the fat. Do we need this many scripts? How could having a dynamic engine continuously regenerating the same static content have become the standard of the Internet? Is this really this hard to implement proper handling of images (resizing, compression, load order) in 2019?

>   How could having a dynamic engine continuously regenerating the same static content have become the standard of the Internet? 
>
>   -   Florent Chauveau

## Getting started with the static web

We are convinced that static websites will become commonplace shortly. In the meantime, it's super easy to beat a bloated dynamic website at the SEO-game using a static one: now it the time to play!

Hugo was a fit for our tech blog as it helped us streamline the content editing process while achieving impressive organic results:

{{< figure src="/img/2019/staticweb/searchconsole.png" alt="Blog.CALLR.tech Organic performance" >}}

Luckily, the offer of static website generators and other related services greatly expanded since the release of Jekyll in 2008. 

If you are considering a static engine for your next website, please check our [follow-up article covering the main frameworks and tools you can use as well some tips and best practices to develop killer static websites.]({{< relref "static-edge.md" >}})

## References

[^1]: [WordPress Market Share](https://kinsta.com/wordpress-market-share/) — Kinsta.com, 2019
[^2]: 1/ Cache/Minification plugin, 2/CDN, 3/ Image Compressor, 4/ SEO (YoastSEO, RankMath), 5/ Redirect, 6/Security, 7/ Comment Spam Management, 8/Formatting (Code Syntax, Shortcode, External Links, etc.) Any other common feature will require yet another plugin, including: multilingual, social share buttons, markdown import, footnotes, table of content, carousel…
[^3]: [The average web page is 3MB. How much should we care?](https://speedcurve.com/blog/web-performance-page-bloat/) — Tammy Everts, Speed Matters, August 2017
[^4]: [List of countries by Internet connection speeds](https://en.wikipedia.org/wiki/List_of_countries_by_Internet_connection_speeds#Average_connection_speeds) — Wikipedia
[^5]: [How Loading Time Affects Your Bottom Line](https://neilpatel.com/blog/loading-time/) — Neil Patel, Neil Patel Blog, August 2018
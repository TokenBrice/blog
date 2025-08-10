---
title: Respecting Users Privacy - The oddity that must become a standard
description: >-
  Where did our online privacy go? It disappeared down the Google-Apple-Facebook
  flush. A read to put you on tracks to win it back.
date: '2018-07-25T10:54:13.745Z'
categories: [Analysis, Privacy]
tags: [facebook, google, ad model, privacy, trackers, ecocrypto]
image: /img/2018/user-privacy/cover.jpeg
---

In 2018, respecting your users’ privacy should be easy, right? After the revelations made by Snowden about the NSA practices and all other that followed, web hosting providers and other services changed their practices, right? That’s what we thought — and the illusion didn’t last for long. Today we take you on a little data tour: who’s collecting them, how, and for what?

### SETTING UP THE CONTEXT

You might know it; else we recommend you to read the manifesto — we recently launched a publication, EcoCrypto, that respects its users and their attention.

Regarding their attention, that’s our issue. However, when it comes to respecting our users’ privacy, it’s much bigger than us: we must double check each third party service we use to ensure they’re not abusing our (and your) trust.

When we published the [manifesto](https://ecocrypto.fr/manifeste/), we realized **how little people knew about the systematized data harvest that happens online**. We decided to write an article to provide a comprehensive overview of the main tracking solution currently enforced pretty much everywhere on the web. At the end of the article, we propose two sets of recommendations. The first one is for everyone: the very basics on how to protect your privacy online. The second one is specific to webmasters: how to respect your users’ privacy.

### THE TRACKER MANIA

> **Each additional tracker is one more guest at the feast held on our privacy.**

Let’s start with the basics: what’s a tracker? Essentially, it’s a small script one can place on his/her website — it allows the different services used to collect data on the visitors, therefore enabling new services for the webmaster.

A tracker is like a snitch for a third party — **each additional tracker is one more guest at the feast held on our privacy.**

### A SMALL DOZEN OF TRACKERS, THE MINIMUM?

_Note: To stay true to the original article (written in French for a French public), we kept French websites as examples. The situation is similar all around the globe, even worse in some countries ._

Any media website is using at the very least a dozen trackers. No need to trust us, [check by yourself using Ghostery](https://www.ghostery.com/): it lets easily you visualized all the trackers present on a website.

Here is a little tracker-tour of a selection of the most visited websites in France:

*   leMonde.fr \[France’s #2 (audience) daily national newspaper\] — **32** different trackers
*   leFigaro.fr \[#1 Daily national newspaper\] —** 35**
*   Mediapart \[Online only publication\] — **21**
*   l’Express \[Weekly magazine\] — **49**
*   tf1.fr \[#1 Private TV channel\] —** 35**
*   France2.fr \[#1 Public TV channel\] — **18**
*   Agence France Presse (AFP — French news agency) — **12**
*   Finally, the cleanest of the bunch, l’Humanité, still has **10 different trackers.**

_Note: The measure was made on July the 18th, on the Homepage of every website. Remember to disable any adblocker or script blocker to see all the trackers on a given website._

![Elle.fr \[Weekly women magazine\] — **53 trackers**; Liberation.fr \[Daily newspaper\] — **40 trackers**](/img/2018/user-privacy/trackers.png)
Elle.fr \[Weekly women magazine\] — **53 trackers**; Liberation.fr \[Daily newspaper\] — **40 trackers**

Quite often, the people working on/for these websites don’t even know about the trackers. We reached out to French crypto publications to let them know about their privacy-intrusive practices. All said they were “surprised” to discover how extensive the net was. Some might say they were laughing at our face — you are the judges.

From this little visit to the horror gallery we can conclude two things:

1.  The owners/webmasters of 99% of internet websites are apparently not even thinking about respecting their user privacy.
2.  The users of these websites don’t know about the tracking and its consequences. Therefore, they don’t ask/push for practices that would be both cleaner and more respectful of their privacy.

If there is any change coming up, it will come from the users: we need to be demanding and uncompromising. To do so, one must know what one is fighting against — let’s start a quick tour of some of the shadiest practices taking place in the online tracking world.

### A TYPOLOGY OF THE TRACKERS

There are several different types of trackers, here’s an overview:

*   **Advertising trackers**: These trackers allow webmasters (and advertising services) to collect additional data when a user goes on a website — this data is then used to increase the effectiveness of the ads. The most common are Double Click and Facebook Ads. We’ll give more details on a subsection of the advertising trackers — the pixels — a little below.
*   **Statistics services trackers**: the most famous is Google Analytics, but there are many others. They’ll have their section.
*   **Social networks trackers:** they allow for a direct integration of social media on a website, such as liking a Facebook page from a media website. It means that the user is identified (through his/her Facebook/Twitter/X profile). One last thing: no need to interact with the buttons to be recognized — that’s the whole beauty of the mechanism. Smile! You’re being spied on.

#### VISITOR STATS… AND AN EXTREMELY DETAILED PROFILE

Each webmaster has the same issue: he/she needs stats to know the most visited pages or articles, where his/her users are coming from, how many are they… To do so, the go-to is to implement Google Analytics.

The value proposition of Google Analytics is pretty straightforward: Google is an expert on data collection and processing, you’re probably not. Implement this little script and Google will do most of the work for you: collecting the data, processing it, or presenting it in comprehensive dashboards. It’s convenient, and most (if not all) websites now use it. The issue? All the data is going through Google, putting it another way: **Google is now collecting data on 99% of any websites users, straight at the source (on the website).**

If each website were a bar, the Google Analytics situation would be similar to having a Google Home with the mic always on at the very center of the room. It’s already annoying and problematic when it’s just a few bars/websites. However, now, since almost all websites use this mechanism, it became the web all-seeing eye / all-hearing ear.

Anyone who handled a website with Google Analytics implement knows what we’re talking about: the amount of data available on any user is staggering. It’s hard to give a precise number because each implementation of Google Analytics is different. Google itself boasts about its **400 different “metrics and dimensions**” — [here is the list.](https://developers.google.com/analytics/devguides/reporting/core/dimsmets#mode=web)

Webmaster rejoice! We suggest an alternative at the end of the article.

### ONLINE ADVERTISING AND USER PRIVACY: STRICTLY IRRECONCILABLE

When we talked about advertising trackers, it was a rapid overview. Allow us to zoom in a little here. First, some basics about online advertising:

*   It’s paid by action: cost per click, per thousand views, per specific action (register, download an app…)
*   All actions are not equal — a click can come from someone completely outside your main target or on the contrary from the potentially perfect customer
*   Online advertising campaigns can be adjusted in real time and at any time.

When the basics are clearly stated, it’s easy to understand that there is a choice to be made between privacy and online advertising. To optimize the online ads, one must collect more and more data to improve his/her targeting and avoid unnecessary expenses.

![](/img/2018/user-privacy/privacy.jpeg)

Online media and social networks often get quite lyrical about their “fight to protect users’ privacy” — don’t let yourself be fooled. **All the most visited websites are big users of online advertising services and use many trackers: in short, they have no respect for their users’ privacy. Even worse: they are making money out of its violation.**

### THE SPY-PIXEL

Still unconvinced? You think that “ethical advertising” is a thing? Let us zoom on a specific kind of trackers: the advertising “Pixels,” such as the [Facebook Pixel](https://www.facebook.com/business/learn/facebook-ads-pixel). Once again, it’s a little script that works a bit like Google Analytics. The webmaster implements the pixel on his/her website and gain access to extra (advertising-related) statistics and services.

On of the main interest for webmasters is that all the data collected will be available straight in Facebook Ads — it makes it much easier to optimize the ads: it’s a mandatory tracker for anybody who is dedicating a significant budget to the platform. Thanks to the pixel, the website owner can make the connection between the ads on Facebook and actions undertook on his website: signups, purchases, downloads, and others.

One of the problems with the Facebook’s pixel is the same as Google Analytics: since the pixel is now everywhere, Facebook is collecting data right at the source on most of the most visited websites.

![An example of a retargeting scenario using Facebook (source: [Lyfe Marketing](https://www.lyfemarketing.com/spa-owners-facebook-customers/facebook-retargeting-example/))](/img/2018/user-privacy/pixel.png)
An example of a retargeting scenario using Facebook (source: [Lyfe Marketing](https://www.lyfemarketing.com/spa-owners-facebook-customers/facebook-retargeting-example/))

Besides, the pixel allows a specific kind of advertising campaigns called “retargeting”: the term refers to any ad where the targeting is made using the previous behavior of the prospects. A typical retargeting flow using Facebook (Pixel and Ads service) looks like that:

1.  You go to a given website, let’s say a lawnmower shop.
2.  Smile, someone’s is spying on you! Thanks to the pixel, you’re immediately recognized, your “Facebook ID” (unique identifier of your Facebook profile) is added to a retargeting list.
3.  You go on Facebook and discover incredible sales of lawnmower straight in your newsfeed.

### THE LITTLE GIFTS DISCOVERED BY THE WAY

Before we delve into our recommendations, let us examine a concrete example that tells a lot about the challenge it became to respect the privacy of your website users online.

Ever heard of WordPress? It’s a framework (~engine) allowing you to create blogs and websites easily — this is what we use on EcoCrypto… for now.

A default WordPress installation uses a service called Gravatar: thanks to it, each user (=anybody who write articles or comment on one) can have his/her very own profile picture.

Even better, users can go on gravatar.com, create their account and set their profile picture once — Tada! Your picture is now on every WordPress using Gravatar without having you to set it up again. Nice, right?

Except that the reality behind the gimmick is quite ugly. Gravatar uses the email to match its user with his/her profile picture. It means that **by default, anyone commenting on a Wordpress sees his/her email getting a free round-trip to Gravatar’s servers.** With the round trip, Gravatar can build a list of the users of every WordPress installation — still looking for that sweet custom profile pic?

Many alternatives exist, and they can be set up in a few clicks, but since Gravatar is enabled on all installations, it’s still widely used. **The default installation, combined with the widespread ignorance of the practice allows Auttomatic (Gravatar’s developers) to stuff itself with the emails of its users unknowingly collected over the years.** _To go further, here’s_ [_an interesting read on Gravatar’s privacy issues._](https://meta.stackexchange.com/questions/44717/is-gravatar-a-privacy-risk)

This kind of scenario repeats itself over and over again when it comes to privacy. Everyone agrees with and supports the concept, yet only a few really look into it. On the business side, the “respecting your users’ privacy” theme is nothing else than a potential communication topic: it’s rarely enforced at the software level.

### SO, WHAT CAN WE DO?

We tried to stay concise and not delve too much into the technical details — we’ve omitted many practices, this article is not exhaustive at all. Dozens, probably hundreds of different tricks and mechanisms exist to track and spy on users online. Some are much more insidious and harder to counter than others, such as [fingerprinting.](https://panopticlick.eff.org/)

What inspired this article is the surprisingly hard journey to set up a simple blog that respects its readers’ privacy. **We’ve left this topic to the experts, and because of that we are reaching a situation where violating the privacy is now the norm — and those who want to respect it struggle.** All of this happening while Apple, Google, Facebook and others are painting themselves as “privacy champion” in front of the general audience, while they are the first to systemize the very end of the idea of privacy. We should fight back, or maybe we should have ten years ago already? It’s never too late!

### TOOLBOX: THE BARE MINIMUM TO PROTECT YOUR PRIVACY

The good news (there is one!) is that protecting your privacy necessitates that you block all the ads — as well as the script that detects if you have an adblocker or not. Stealth has a bright side!

What follows is the bare minimum setup, you must go much further to be really covered, if ever possible:

#### 1\. BLOCK THE ADS

For Chrome users, we recommend the [Nano Adblocker](https://chrome.google.com/webstore/detail/nano-adblocker/gabbbocakeomblphkmmnoamkioajlkfo) + [Nano Defender](https://chrome.google.com/webstore/detail/nano-defender/ggolfgbegefeeoocgjbmkembbncoadlb?hl=en) (anti ad-block defuser) combo: it’s easy to set up and works well. Firefox users can use [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/) for similar results.

Note: Whatever adblocker you chose, don’t forget to enable the EasyList corresponding to your country. Here’s a demo GIF for the French list:

![](/img/2018/user-privacy/adblock-fr.gif)

You can try your setup by visiting any media website with the adblocker enabled; you’ll see a lot of free space! Insidious ads such as sponsored posts (“native advertising” as professionals call them) are not blocked — beware.

#### 2\. LIST AND BLOCK THE TRACKERS

Ads are only the start. Now we need to tackle the trackers. The good news is that there are very extensions to take care of this for you.

![](/img/2018/user-privacy/privacy-badger.png)

Privacy Badger is developed by [the EFF — the Electronic Frontier Foundation](https://www.eff.org/about), a nonprofit that has been defending civil liberties in the digital word for years — it’s not enough to blindly trust them, but it does provide reassurance. You don’t need any specific setting, but you might want to have a look at the trackers list (by clicking on the extension icon) and disable those you don’t need. At the beginning of the article, we mentioned [Ghostery](https://www.ghostery.com/) — it also works quite well, and might be easier to use for some.

#### 3\. USE HTTPS, EVERYWHERE

When you visit a website that uses HTTPS, the exchanges between your browser and the website are encrypted. HTTPS is now widespread, but its implementation on certain websites is quite messy: they’ll make you switch back and force between the secured and regular HTTP. [HTTPS Everywhere](https://www.eff.org/https-everywhere), another browser extension from the EFF solves the issue: it forces websites to use HTTPS whenever it’s available.

#### ADDITIONAL NOTES ON PRIVACY TOOLS

If you want to be even safer, use [Firefox](https://www.mozilla.org/fr/firefox/) instead of **Google** Chrome. If you’re looking for sensitive stuff online, [use TOR at least, it’s super easy to set up](https://www.torproject.org/projects/torbrowser.html.en). Finally, if you want to be a little safer, look for more sensitive stuff, or leak critical information please check [TAILS — an operating system (Linux based) made for privacy](https://tails.boum.org/). Before going to the dark side of the web, READ and document yourself.

To keep the article short-ish, we limited ourselves to three tools. **To really cover your digital steps, you’ll have to go much further.**

We could have easily listed a hundred of different [tools](https://hackernoon.com/tagged/tools) relevant for different situations — it would be pointless. You need to be able to pick the most suitable tools for your usage by yourself. To do so, there is no other way than lifting the hood to delve into the technical stuff. **Privacy is not given nowadays; you must fight for it.**

All around the globe, nonprofits are doing their part with their means. The EFF edits a [Surveillance Self Defense guide](https://ssd.eff.org/en) which could be an excellent place to start.

### RESPECTING USERS PRIVACY AS A WEBMASTER

If you are handling a website, the most critical action you could start with is breaking free from Google Analytics. We have chosen [Matomo](https://matomo.org/), an open-source and **self-hosted** analytics solution. The self-hosted part means that the data stays on our servers: it’s essential.

Depending on your hosting provider, setting up Matomo might be more or less accessible. If your hosting provides supports [Softaculous](https://www.softaculous.com/), the installation will be done in a few clicks. Else, you might need to learn a thing or two on server management.

The other actions you can undertake will depend on the services and framework you use. Rather than a list of tools, let us suggest a methodology:

1.  **Third-party services minimization**: reduce to the very minimum the number of third-party services you use. Each new service is a potential risk both for your website [security](https://hackernoon.com/tagged/security) and for your users’ privacy. Even a decent, honest service can go rogue in a flash, and it won’t warn you about it.
2.  **Investigate any third-party service you do implement**: despite 1/, you’ll have to use some third-party services. Look into the developers of these services, their other products, the reviews. There might even be other people who audited their code and talked about it. Use open-source services whenever it’s possible.
3.  **Forget about online advertising** on the main services (Social media, Google…) — you can’t reach cost-efficiency on these services without violating your users’ privacy.
4.  **Ask for help!** More and more people are getting “privacy-fluent” and would be [happy to help](https://www.eff.org/) a well-intentioned webmaster to establish a decent setup.

This article is the translation of an original (French) [EcoCrypto.fr](https://ecocrypto.fr) story.
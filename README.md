## Tokenbrice.xyz, a blog respecting your privacy

> I made this blog as a callout: I'm no dev, I can barely code, and yet I was able to respect my reader's privacy, to an unprecedented level in the space.

[![Generator is Hugo](https://img.shields.io/badge/Generator%20is-Hugo-ff4088?&logo=hugo)](https://github.com/gohugoio/hugo)
[![Theme is MemE](https://img.shields.io/badge/Theme%20is-MemE-2a6df4?&logo=meme)](https://github.com/reuixiy/hugo-theme-meme)
[![Source on GitHub](https://img.shields.io/badge/Source%20on-GitHub-181717?&logo=github)](https://github.com/tokenbrice/blog/)
[![Hosted on IPFS](https://img.shields.io/badge/Hosted%20on-IPFS-65c2cb?&logo=ipfs)](https://ipfs.io/)

To do so, TokenBrice.xyz relies on **open source frameworks** and solutions such as Hugo (rendering of the blog) or Matomo (privacy-conscious analytics).

For those interested, this blog implements **full IP anonymisation, cookies non-propagation** in compliance with the [CNIL guidelines](https://www.cnil.fr/sites/default/files/typo/document/Configuration_piwik.pdf) - an independent French' administrative body acting as a privacy watchdog.

Tokenbrice.xyz is also replicated on [IPFS](https://ipfs.io/). I'm not entirely happy with the infrastructure just yet, but I think it's significant progress compared to most existing websites:

![tokenbrice-xyz-infrastructure-overview](https://github.com/TokenBrice/blog/blob/master/static/img/2020/hello-world/infrastructure.png)

### [More info here](https://tokenbrice.xyz/posts/2020/hello-world/)

### To Build & Run

```sh
yarn install
yarn run build  // Build module javascript for page "about" and generate main.js in /static/js
hugo  // Allow to use main.js in Hugo. Send static/js/main.js in public
yarn run optimize // Optimize images of public/img
```

### Local development

```sh
git config --global --add safe.directory /workspace
git submodule update --init --recursive
hugo --gc --minify
hugo server
```
or
```sh
docker-compose up -d --build
```
and open `http://localhost:1313`

### How to add filters

If you need to add filters, follow the procedure below :

Open data/filters.json and add filters and add values for fr and en.

```
[
 "fr": {
    "tags": {
      ...
      "values" : [
      ...
        {
          "key": "newkey",
          "name": "French name translation"
        },
      ]
  }
  "en": {
      "tags": {
        ...
        "values" : [
        ...
          {
            "key": "newkey",
            "name": "English name translation"
          },
        ]
    }
]
    
```

Then add the "newkey" to your data/media.json

```
 {
    "tags": ["newkey"],
    "name": "Post Name",
    "host": "Host name",
    "link": "link to media",
    "date": "date"
 },
```

And finally compile the new main.js using `yarn run build` (local) or `yarn run build:production`


### How to add a new filter category

A filter is composed of a name, a class and an array of values object.

Edit data/filters.json and add your new filter category

```
[
 "fr": {
    "newCategory": {
      "name": "Nouvelle Catégorie",
      "class": "categoryClass"
      "values" : [
      ...       
    ]
  }
  "en": {
      "newCategory": {
        "name": "New Category",
        "class": "categoryClass"
        "values" : [
        ...       
      ]
    }
]
    
```

After that you need to add the key of your category add style to src/js/App.vue

```
export default {
        data() {
            return {
                ...
                selectedFilters: {
                   ...
                   newCategory: [],
                },
        },
        ...
}

...

<style>
   ...
   .categoryClass {
     cssRules: here
   } 
</style>

```

Follow by using `yarn run build` and your new category should be visible (clear web browser cache)
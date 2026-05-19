## tokenbrice.xyz

> Brutally honest DeFi, built on a privacy-respecting static stack.

This repository contains the bilingual EN/FR TokenBrice blog. It is built with Hugo Extended `0.161.1`, a fork of `hugo-theme-stack`, self-hosted assets, and Matomo analytics.

[![Generator is Hugo](https://img.shields.io/badge/Generator%20is-Hugo-ff4088?&logo=hugo)](https://github.com/gohugoio/hugo)
[![Source on GitHub](https://img.shields.io/badge/Source%20on-GitHub-181717?&logo=github)](https://github.com/tokenbrice/blog/)

### Local development

```sh
make setup
make serve
```

Open `http://localhost:1313`.

Docker is also available:

```sh
docker-compose up -d --build
```

### Verification

Use the same checks CI uses before shipping:

```sh
make verify
```

The verification path runs:

- front matter validation
- content safety validation for raw scripts/iframes and missing image alt text
- TypeScript typechecking
- Hugo production build
- generated-site local reference validation

Individual commands are also available:

```sh
make validate
make validate-content
make typecheck
make build
make validate-site
```

### Assets

Static images live under `static/img`. When new static images are added, refresh derived assets and dimensions:

```sh
make webp
make avif
make imgdims
```

`data/imageDims.json` is used by render hooks to emit image dimensions and reduce layout shift.

### Search

The site uses the theme JSON search index at `/search/index.json` and `/fr/search/index.json`. Pagefind is intentionally not built in CI so there is a single search path.

### Privacy

The client-side Matomo integration disables cookies and avoids sending raw search terms or clicked URLs. Search analytics are bucketed by query length, and social clicks are recorded by host only.

IP anonymization, retention, and opt-out behavior must be enforced in the Matomo server configuration. Keep those settings aligned with the CNIL-friendly privacy claim before changing analytics behavior.

### Content Rules

- Do not add raw `<script>` tags in Markdown content.
- Raw `<iframe>` embeds must use `youtube-nocookie.com` and include a `title`.
- Markdown images must include alt text.
- Prefer shortcodes or layout partials for embeds and structured data.

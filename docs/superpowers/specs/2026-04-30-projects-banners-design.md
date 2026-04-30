# Projects banners — design spec

**Date:** 2026-04-30
**Status:** Approved (pending implementation plan)

## Goal

Add two call-out banners promoting Pharos (`pharos.watch`) and Polaris
(`polarisfinance.io`) on the blog. Both projects are stablecoin-related
ventures the author contributes to. The banners should drive informed
clicks and pass full SEO link equity to both destinations.

## Decisions

| Topic | Decision |
|---|---|
| Placement | **D + B** — homepage hero (above article list) **and** end-of-post call-out (after article body) |
| Content | Logo emblem + project name + 1-line tagline |
| Visual style | **A** — dark navy showcase band with two cards side-by-side |
| Bilingual | Full EN/FR translation of taglines via per-project YAML; EN fallback if FR missing |
| Link attributes | `target="_blank" rel="noopener"` — no `noreferrer`, no `nofollow` (preserve referer attribution + link equity) |
| Tracking parameters | None (no UTMs added at link level) |

## Architecture (Approach 1: data-driven partial + targeted layout overrides)

### File structure

**New files:**
- `data/projects.yaml` — single source of truth for project metadata
- `layouts/partials/projects-banner.html` — renders the banner band
- `assets/scss/_projects-banner.scss` — banner styles (imported from main SCSS)
- `static/img/projects/pharos/emblem.png` — copied from `stablecoin-dashboard/public/apple-touch-icon.png`
- `static/img/projects/polaris/emblem.svg` — copied from `polaris-landing/public/emblem.svg`

**Edited files (surgical):**
- `layouts/index.html` — new override of the theme's homepage; insert `{{ partial "projects-banner.html" . }}` immediately before the existing `<section class="article-list">`
- `layouts/partials/article/article.html` — new override of the theme's article wrapper; insert `{{ partial "projects-banner.html" . }}` between `article/components/content` and `article/components/footer` (i.e., after the article body, before the license/share footer)
- `i18n/en.toml` + `i18n/fr.toml` — one new key, `projectsBannerLabel` (`"Projects"` / `"Projets"`)
- `assets/scss/custom.scss` — append `@import "projects-banner";` (matches existing pattern alongside `glossary-links`, `breadcrumbs`, etc.)

### Data model — `data/projects.yaml`

```yaml
projects:
  - id: pharos
    name: Pharos
    url: https://pharos.watch
    emblem: img/projects/pharos/emblem.png
    tagline:
      en: Stablecoin analytics dashboard
      fr: Tableau de bord d'analyse des stablecoins
  - id: polaris
    name: Polaris
    url: https://polarisfinance.io
    emblem: img/projects/polaris/emblem.svg
    tagline:
      en: Self-scaling stablecoin OS
      fr: OS stablecoin auto-évolutif
```

The partial reads `Site.Data.projects.projects`, iterates, picks
`tagline[Page.Language.Lang]` with `tagline.en` as fallback.

### Banner partial — rendering contract

**Output (per banner instance):**

```html
<section class="projects-banner" aria-label="{{ T "projectsBannerLabel" }}">
  <div class="projects-banner__band">
    <ul class="projects-banner__cards">
      {{ range $.Site.Data.projects.projects }}
      <li class="projects-banner__card">
        <a class="projects-banner__link"
           href="{{ .url }}"
           target="_blank"
           rel="noopener"
           aria-label="Visit {{ .name }} — {{ index .tagline $.Page.Language.Lang | default (index .tagline "en") }}">
          <img class="projects-banner__emblem"
               src="/{{ .emblem }}"
               alt="{{ .name }}"
               width="64" height="64"
               loading="lazy">
          <div class="projects-banner__text">
            <h3 class="projects-banner__name">{{ .name }}</h3>
            <p class="projects-banner__tagline">{{ index .tagline $.Page.Language.Lang | default (index .tagline "en") }}</p>
          </div>
        </a>
      </li>
      {{ end }}
    </ul>
  </div>
</section>
```

Key properties:
- One outer `<section>`, one inner `__band`, one `<ul>` for cards
- Each card is an `<a>` containing emblem + name + tagline
- `aria-label` on each link composes naturally for screen readers
- `loading="lazy"` on emblems (small, non-critical, OK in both placements)
- Hugo template chooses tagline language with EN fallback via `default`

### Visual design (CSS)

**Layout:**
- Outer `<section>`: full content-width container (matches blog's main column)
- `.projects-banner__band`: 28px desktop / 20px mobile internal padding, 8px border-radius
- `.projects-banner__cards`: CSS grid, `grid-template-columns: 1fr 1fr` ≥768px, `1fr` <768px, 16px gap
- Vertical margin around the section: 40px top/bottom

**Colors (fixed — does not adapt to site `data-scheme`):**
- Outer band background: linear gradient `#0a1628` → `#1a2f54`
- Card background: subtle inner darker block (e.g., `rgba(0,0,0,0.18)`) for separation against the band
- Project name text: `#f5f1e8` (cream, ~18px, weight 600)
- Tagline text: `#a8b3c5` (muted blue-grey, ~13px)

**Interactions:**
- Card hover: `translateY(-2px)` + slight box-shadow
- `:focus-visible` on link: visible focus ring (cream outline, 2px)
- `@media (prefers-reduced-motion: reduce)`: no transform on hover
- `@media print`: `.projects-banner { display: none; }` — promotional, not content

### Layout integration

**Homepage:** copy `themes/hugo-theme-stack/layouts/index.html` to
`layouts/index.html` and insert `{{ partial "projects-banner.html" . }}`
immediately before the existing `<section class="article-list">` line.

**Post pages:** copy `themes/hugo-theme-stack/layouts/partials/article/article.html`
to `layouts/partials/article/article.html` and insert
`{{ partial "projects-banner.html" . }}` between
`{{ partial "article/components/content" . }}` and
`{{ partial "article/components/footer" . }}`. This places the banner
inside `<article class="main-article">`, after the body content, before
the license/tags/lastmod block.

### Bilingual handling

- Tagline copy lives in `data/projects.yaml` per language
- `projectsBannerLabel` lives in `i18n/{en,fr}.toml`
- Hugo's multilingual page-rendering handles `/` vs `/fr/` paths
  automatically; the partial resolves language via `$.Page.Language.Lang`

## Edge cases

- **Empty `projects` list** → partial guards with `{{ with $.Site.Data.projects.projects }}…{{ end }}`, renders nothing if absent
- **Missing tagline for active language** → `default (index .tagline "en")` falls back to English
- **Missing emblem asset** → broken image; mitigated by manual review (only 2 projects, sourced once)
- **Print** → `@media print` hides the section
- **Reduced motion** → hover lift disabled
- **Dark/light theme toggle** → banner stays its own dark zone; verified in both modes during testing

## Out of scope / explicitly deferred

- WebP conversion of the Pharos PNG emblem (file is 15KB; revisit if Lighthouse flags)
- UTM tracking parameters on outbound links
- Adding a third project (data-driven approach makes this trivial later)
- Contextual "projects I contribute to" sentence (declined during brainstorming)
- About-page integration of the banners (declined; existing project bullets stay)

## Verification plan

After implementation:
1. `hugo server --disableFastRender` → load homepage; banner renders above article list
2. Open any post → banner renders after article body, before license footer
3. Visit `/fr/` homepage and any FR post → French taglines render
4. Toggle dark/light theme via the existing toggle → banner stays dark-themed in both modes
5. Resize viewport to <768px → cards stack vertically, no overflow
6. Click each banner card → opens project site in a new tab; verify Referer header is sent (devtools network panel)
7. Run `hugo --gc --minify` → builds without template warnings
8. Manual a11y check: tab through banner → both cards focusable, focus ring visible, screen-reader label reads "Visit Pharos — Stablecoin analytics dashboard"
9. Optional: Lighthouse run on homepage → confirm no perf/a11y regressions vs baseline in `lighthouse-reports/`

## Implementation effort estimate

5 new files (data YAML, partial, SCSS, 2 image assets) + 2 layout overrides + 1 SCSS import line + 2 i18n keys + ~80 lines SCSS. Single-session task. No new dependencies.

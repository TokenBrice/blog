# Projects Banners Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two SEO-friendly call-out banners promoting Pharos and Polaris on the blog homepage and end-of-post, driven by a single data file and rendered by one shared partial.

**Architecture:** Hugo data file (`data/projects.yaml`) + one shared partial (`layouts/partials/projects-banner.html`) inserted via two surgical theme overrides (`layouts/index.html`, `layouts/partials/article/article.html`). Bilingual EN/FR taglines resolved per page from the data file. Dedicated SCSS partial imported into `assets/scss/custom.scss`. Logos served from `static/img/projects/` matching the existing static-image convention.

**Tech Stack:** Hugo 0.148.2 Extended, hugo-theme-stack, SCSS via Hugo Pipes, YAML data files, TOML i18n.

**Spec:** `docs/superpowers/specs/2026-04-30-projects-banners-design.md`

---

## File structure

| Path | Action | Responsibility |
|---|---|---|
| `static/img/projects/pharos/emblem.png` | Create | Pharos lighthouse emblem (180×180 PNG) |
| `static/img/projects/polaris/emblem.svg` | Create | Polaris star/compass emblem (88×88 SVG) |
| `data/projects.yaml` | Create | Project metadata (name, URL, emblem path, EN/FR taglines) |
| `i18n/en.toml` | Modify | Add `projectsBannerLabel = "Projects"` |
| `i18n/fr.toml` | Modify | Add `projectsBannerLabel = "Projets"` |
| `layouts/partials/projects-banner.html` | Create | Renders the banner band from data |
| `assets/scss/_projects-banner.scss` | Create | Banner styles (band, cards, responsive, a11y) |
| `assets/scss/custom.scss` | Modify | `@import "projects-banner";` |
| `layouts/index.html` | Create | Theme override; inserts partial above article list |
| `layouts/partials/article/article.html` | Create | Theme override; inserts partial between content and article footer |

---

## Task 1: Place logo assets and seed data + i18n

**Files:**
- Create: `static/img/projects/pharos/emblem.png` (copied)
- Create: `static/img/projects/polaris/emblem.svg` (copied)
- Create: `data/projects.yaml`
- Modify: `i18n/en.toml`
- Modify: `i18n/fr.toml`

- [ ] **Step 1: Copy logo assets**

```bash
mkdir -p static/img/projects/pharos static/img/projects/polaris
cp /home/ahirice/Documents/git/stablecoin-dashboard/public/apple-touch-icon.png \
   static/img/projects/pharos/emblem.png
cp /home/ahirice/Documents/git/polaris-landing/public/emblem.svg \
   static/img/projects/polaris/emblem.svg
```

Verify both files exist and are non-zero:
```bash
ls -la static/img/projects/pharos/emblem.png static/img/projects/polaris/emblem.svg
```
Expected: both files listed, sizes ~15KB and ~2.4KB respectively.

- [ ] **Step 2: Create `data/projects.yaml`**

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

- [ ] **Step 3: Append i18n keys**

In `i18n/en.toml`, append at end:
```toml
[projectsBannerLabel]
other = "Projects"
```

In `i18n/fr.toml`, append at end:
```toml
[projectsBannerLabel]
other = "Projets"
```

- [ ] **Step 4: Verify Hugo can read the data file**

Run:
```bash
hugo --renderToMemory --quiet 2>&1 | head -20
```
Expected: no errors. (The data file is loaded but unused at this point — Hugo just validates the YAML.)

- [ ] **Step 5: Commit**

```bash
git add static/img/projects/ data/projects.yaml i18n/en.toml i18n/fr.toml
git commit -m "feat(banner): seed projects data, i18n keys, and emblem assets"
```

---

## Task 2: Create the SCSS partial

**Files:**
- Create: `assets/scss/_projects-banner.scss`
- Modify: `assets/scss/custom.scss`

- [ ] **Step 1: Create `assets/scss/_projects-banner.scss`**

```scss
.projects-banner {
    margin: 40px 0;

    &__band {
        background: linear-gradient(135deg, #0a1628 0%, #1a2f54 100%);
        border-radius: 8px;
        padding: 28px 24px;

        @media (max-width: 767px) {
            padding: 20px 16px;
        }
    }

    &__cards {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 16px;
        list-style: none;
        margin: 0;
        padding: 0;

        @media (max-width: 767px) {
            grid-template-columns: 1fr;
        }
    }

    &__card {
        margin: 0;
    }

    &__link {
        display: flex;
        align-items: center;
        gap: 18px;
        padding: 20px;
        background: rgba(0, 0, 0, 0.18);
        border-radius: 6px;
        text-decoration: none;
        color: inherit;
        transition: transform 0.15s ease, box-shadow 0.15s ease;

        &:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
        }

        &:focus-visible {
            outline: 2px solid #f5f1e8;
            outline-offset: 2px;
        }
    }

    &__emblem {
        flex-shrink: 0;
        width: 64px;
        height: 64px;
        border-radius: 8px;
    }

    &__text {
        min-width: 0;
    }

    &__name {
        margin: 0 0 4px;
        font-size: 18px;
        font-weight: 600;
        color: #f5f1e8;
        line-height: 1.2;
    }

    &__tagline {
        margin: 0;
        font-size: 13px;
        color: #a8b3c5;
        line-height: 1.4;
    }

    @media (prefers-reduced-motion: reduce) {
        &__link {
            transition: none;
            &:hover { transform: none; }
        }
    }

    @media print {
        display: none;
    }
}
```

- [ ] **Step 2: Add the import to `assets/scss/custom.scss`**

Read the file first to find the right place. Append at end (after the existing imports), one new line:
```scss
@import "projects-banner";
```

- [ ] **Step 3: Verify SCSS compiles**

```bash
hugo --renderToMemory --quiet 2>&1 | head -30
```
Expected: no SCSS compilation errors (no "ERROR" lines).

If errors appear about a missing variable or import order, adjust the position of the new `@import` accordingly.

- [ ] **Step 4: Commit**

```bash
git add assets/scss/_projects-banner.scss assets/scss/custom.scss
git commit -m "feat(banner): add projects-banner SCSS partial"
```

---

## Task 3: Create the banner partial template

**Files:**
- Create: `layouts/partials/projects-banner.html`

- [ ] **Step 1: Create `layouts/partials/projects-banner.html`**

```go-html-template
{{- with $.Site.Data.projects.projects -}}
{{- $lang := $.Page.Language.Lang -}}
<section class="projects-banner" aria-label="{{ T "projectsBannerLabel" }}">
    <div class="projects-banner__band">
        <ul class="projects-banner__cards">
            {{- range . }}
            {{- $tagline := index .tagline $lang | default (index .tagline "en") -}}
            <li class="projects-banner__card">
                <a class="projects-banner__link"
                   href="{{ .url }}"
                   target="_blank"
                   rel="noopener"
                   aria-label="{{ T "projectsBannerLabel" }}: {{ .name }} — {{ $tagline }}">
                    <img class="projects-banner__emblem"
                         src="{{ .emblem | absURL }}"
                         alt="{{ .name }}"
                         width="64" height="64"
                         loading="lazy">
                    <div class="projects-banner__text">
                        <h3 class="projects-banner__name">{{ .name }}</h3>
                        <p class="projects-banner__tagline">{{ $tagline }}</p>
                    </div>
                </a>
            </li>
            {{- end }}
        </ul>
    </div>
</section>
{{- end -}}
```

Notes:
- `with` guard renders nothing if `data/projects.yaml` is empty or missing
- `$.Page.Language.Lang` resolves to `"en"` or `"fr"` per the current rendering page
- `default (index .tagline "en")` falls back to English if a tagline is missing for the current language
- Emblem `src` uses `absURL` so the partial works correctly under both `/` and `/fr/` paths
- Note: `<h3>` is intentional — the banner appears below `<h2>`-level page headings on both placements, so document outline stays sane

- [ ] **Step 2: Verify the partial template parses**

```bash
hugo --renderToMemory --quiet 2>&1 | head -30
```
Expected: no template-execution errors. (The partial is defined but not yet referenced — Hugo only validates template syntax at this point.)

- [ ] **Step 3: Commit**

```bash
git add layouts/partials/projects-banner.html
git commit -m "feat(banner): add projects-banner partial"
```

---

## Task 4: Wire up homepage override

**Files:**
- Create: `layouts/index.html` (override of theme's `themes/hugo-theme-stack/layouts/index.html`)

- [ ] **Step 1: Read the theme's `index.html` for reference**

```bash
cat themes/hugo-theme-stack/layouts/index.html
```

Confirm the structure starts with `{{ define "main" }}` and the article list is rendered by `<section class="article-list">`.

- [ ] **Step 2: Create `layouts/index.html`**

Copy the theme template verbatim, then insert one line — `{{ partial "projects-banner.html" . }}` — immediately before `<section class="article-list">`.

```go-html-template
{{ define "main" }}
    {{ $pages := where .Site.RegularPages "Type" "in" .Site.Params.mainSections }}
    {{ $notHidden := where .Site.RegularPages "Params.hidden" "!=" true }}
    {{ $filtered := ($pages | intersect $notHidden) }}
    {{ $pag := .Paginate ($filtered) }}

    {{ partial "projects-banner.html" . }}

    <section class="article-list">
        {{ range $index, $element := $pag.Pages }}
            {{ partial "article-list/default" . }}
        {{ end }}
    </section>

    {{- partial "pagination.html" . -}}
    {{- partial "footer/footer" . -}}
{{ end }}

{{ define "right-sidebar" }}
    {{ partial "sidebar/right.html" (dict "Context" . "Scope" "homepage") }}
{{ end }}
```

- [ ] **Step 3: Verify rendering on the homepage**

Start the dev server:
```bash
hugo server --disableFastRender --port 1314
```

Then in another terminal, fetch the homepage HTML and confirm the banner block is present:
```bash
curl -s http://localhost:1314/ | grep -c 'projects-banner'
```
Expected: a number ≥ 4 (one for the section class, one for band, one for cards, one or more for cards/links).

Also fetch the FR homepage:
```bash
curl -s http://localhost:1314/fr/ | grep -A1 'projects-banner__tagline' | head -10
```
Expected: includes `Tableau de bord d'analyse des stablecoins` and `OS stablecoin auto-évolutif`.

Stop the dev server (Ctrl-C in its terminal) before continuing.

- [ ] **Step 4: Visual smoke check**

Re-run `hugo server --disableFastRender --port 1314` and open http://localhost:1314 in a browser. Confirm:
- Dark navy banner appears above the article list
- Both Pharos and Polaris cards render with emblems and taglines
- Navigate to http://localhost:1314/fr/ — taglines render in French
- Toggle dark/light theme — banner stays dark navy in both modes
- Resize browser to <768px — cards stack vertically

Stop the dev server.

- [ ] **Step 5: Commit**

```bash
git add layouts/index.html
git commit -m "feat(banner): render projects banner on homepage"
```

---

## Task 5: Wire up post-page override

**Files:**
- Create: `layouts/partials/article/article.html` (override of theme's `themes/hugo-theme-stack/layouts/partials/article/article.html`)

- [ ] **Step 1: Read the theme's `article.html` for reference**

```bash
cat themes/hugo-theme-stack/layouts/partials/article/article.html
```

Confirm the partial body is just header → content → footer inside `<article>`.

- [ ] **Step 2: Create `layouts/partials/article/article.html`**

Copy the theme template verbatim, then insert one line — `{{ partial "projects-banner.html" . }}` — between the content partial and the footer partial.

```go-html-template
<article class="{{ if .Params.image }}has-image {{ end }}main-article">
    {{ partial "article/components/header" . }}

    {{ partial "article/components/content" . }}

    {{ partial "projects-banner.html" . }}

    {{ partial "article/components/footer" . }}

    {{ if or .Params.math .Site.Params.article.math }}
        {{ partialCached "article/components/math.html" . }}
    {{ end }}
</article>
```

- [ ] **Step 3: Verify rendering on a post page**

Start the dev server:
```bash
hugo server --disableFastRender --port 1314
```

Fetch any post and verify the banner appears. Get the URL of any post first:
```bash
curl -s http://localhost:1314/ | grep -oE 'href="/[a-z-]+/"' | head -3
```

Pick one (e.g., `/crv-wars/`) and verify both the article body and banner exist:
```bash
curl -s http://localhost:1314/crv-wars/ | grep -cE 'projects-banner|article-content'
```
Expected: ≥ 2 (at least one for the banner, one for the article).

Verify the banner renders BEFORE the article footer (license/copyright). Pipe through grep to find both classes:
```bash
curl -s http://localhost:1314/crv-wars/ | grep -nE 'projects-banner|article-footer' | head -4
```
Expected: line numbers for `projects-banner` are LESS THAN line numbers for `article-footer`.

Also check a French post:
```bash
curl -s http://localhost:1314/fr/ | grep -oE 'href="/fr/[a-z-]+/"' | head -2
```
Pick one and verify it has French taglines:
```bash
curl -s http://localhost:1314/fr/<slug>/ | grep -A1 'projects-banner__tagline' | head -10
```
Expected: French strings appear.

Stop the dev server.

- [ ] **Step 4: Visual smoke check**

Re-run `hugo server --disableFastRender --port 1314` and open a post in the browser:
- Banner appears after the article body
- License/share footer appears AFTER the banner (not before)
- Mobile viewport: cards stack
- Click each card: opens the project site in a new tab; in DevTools Network tab, confirm the request to the project includes `Referer: http://localhost:1314/...`

Stop the dev server.

- [ ] **Step 5: Commit**

```bash
git add layouts/partials/article/article.html
git commit -m "feat(banner): render projects banner after article body"
```

---

## Task 6: Production build verification

**Files:** none modified — verification only.

- [ ] **Step 1: Run a clean production build**

```bash
hugo --gc --minify 2>&1 | tail -20
```
Expected:
- No "ERROR" or "WARN" lines mentioning the banner partial, the data file, or i18n keys
- Build completes; "Pages" count is non-zero

- [ ] **Step 2: Confirm rendered HTML in `public/`**

```bash
grep -l 'projects-banner' public/index.html public/fr/index.html | wc -l
```
Expected: `2` (banner present on both EN and FR homepages).

```bash
find public -name 'index.html' -path '*/post/*' -o -name 'index.html' -path '*/[a-z-]*/' 2>/dev/null | head -5 | xargs grep -l 'projects-banner' | wc -l
```
Expected: ≥ 1 (banner present on at least one post page).

- [ ] **Step 3: Confirm assets are emitted**

```bash
ls -la public/img/projects/pharos/emblem.png public/img/projects/polaris/emblem.svg
```
Expected: both files exist with non-zero sizes.

- [ ] **Step 4: Commit (if anything changed during verification)**

If git status shows nothing modified, skip. Otherwise commit any small fixups:
```bash
git status
```

---

## Task 7: Optional — Lighthouse regression check

**Files:** none modified — verification only.

- [ ] **Step 1: Run Lighthouse against the homepage**

Use the existing `lighthouse.sh` script in the repo root:
```bash
./lighthouse.sh
```
(Or follow the script's documented invocation.)

- [ ] **Step 2: Compare against the most recent baseline in `lighthouse-reports/`**

Confirm:
- Performance score did not drop more than 2 points
- Accessibility score did not drop at all
- No new contrast or focus-visible warnings related to `.projects-banner`

If a regression appears, file a follow-up — do NOT block the merge on this for v1.

---

## Self-review checklist (run before handing off)

- [ ] Spec coverage: every section of `docs/superpowers/specs/2026-04-30-projects-banners-design.md` maps to at least one task above
- [ ] No placeholders (no "TBD", no "implement later", no "similar to Task N")
- [ ] Every code block is complete and runnable as-is
- [ ] File paths are absolute or repo-relative and unambiguous
- [ ] Naming consistent across tasks (`.projects-banner__*` BEM throughout)
- [ ] Commit messages follow conventional-commits style and describe the actual change

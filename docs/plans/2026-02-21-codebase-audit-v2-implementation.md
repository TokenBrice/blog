# Codebase Audit V2 — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Eliminate tech debt across code quality, performance, SEO, and CSS architecture following DRY/KISS/YAGNI principles.

**Architecture:** Hugo 0.148.2 Extended blog with hugo-theme-stack. All fixes use root-level overrides — theme files in `themes/` are never modified. Changes are grouped into 3 risk phases: zero-risk housekeeping, low-risk SEO, medium-risk CSS refactor.

**Tech Stack:** Hugo (Go templates, SCSS via Hugo Pipes, TypeScript via js.Build), GitHub Pages deployment

**Design doc:** `docs/plans/2026-02-21-codebase-audit-v2-design.md`

---

## Task 1: Fix .gitignore

**Files:**
- Modify: `.gitignore`
- Delete: `.gitignore.new`

**Step 1: Replace .gitignore contents**

Replace the entire contents of `.gitignore` with:

```gitignore
# Node modules and dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Hugo build outputs
public/
resources/_gen/
.hugo_build.lock

# Development files
.DS_Store
.vscode/
.idea/
*.swp
*.swo

# Build artifacts
dist/
build/

# Environment files
.env
.env.local
.env.production

# Image optimization cache
.image-cache/

# Logs
*.log

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Backup files
*.backup

# Lighthouse reports
lighthouse-reports/
```

Note: Added `lighthouse-reports/` and `*.backup` which weren't in `.gitignore.new` but are needed. Removed `package.json` and `package-lock.json` exclusions from old `.gitignore` (they should be tracked).

**Step 2: Delete .gitignore.new**

```bash
rm .gitignore.new
```

**Step 3: Verify**

```bash
hugo server --disableFastRender &
# Check site builds with no errors
kill %1
```

**Step 4: Commit**

```bash
git add .gitignore
git rm .gitignore.new
git commit -m "chore: replace .gitignore with comprehensive patterns

Adds exclusions for resources/_gen, .image-cache, *.backup, build
artifacts, env files, and editor swap files. Removes outdated
exclusion of package.json/package-lock.json."
```

---

## Task 2: Remove tracked .backup files

**Files:**
- Remove: `content/categories/**/*.backup` (11 files)

Note: The `public/categories/**/*.backup` files mentioned in the audit are in the build output directory (already gitignored). Only `content/` backups need removal.

**Step 1: Find and remove tracked backup files**

```bash
git ls-files '*.backup' | xargs git rm
```

**Step 2: Verify no backup files remain tracked**

```bash
git ls-files '*.backup'
# Expected: empty output
```

**Step 3: Commit**

```bash
git commit -m "chore: remove tracked .backup files from content/categories

11 category image backups from a prior migration. Now excluded
by *.backup pattern in .gitignore."
```

---

## Task 3: Deduplicate glossary.json

**Files:**
- Modify: `data/glossary.json`

**Step 1: Identify duplicates**

Search for the 5 duplicate IDs in the EN section: `bid-ask-spread`, `limit-order`, `market-depth`, `market-order`, `volume`. Each appears twice. Keep the first occurrence, remove the second (including its trailing comma if needed to keep valid JSON).

**Step 2: Run deduplication**

Use a script to find and remove exact duplicate objects:

```bash
python3 -c "
import json
with open('data/glossary.json') as f:
    data = json.load(f)
for lang in ['en', 'fr']:
    if 'terms' in data.get(lang, {}):
        seen = set()
        unique = []
        for term in data[lang]['terms']:
            tid = term.get('id', '')
            if tid not in seen:
                seen.add(tid)
                unique.append(term)
        removed = len(data[lang]['terms']) - len(unique)
        data[lang]['terms'] = unique
        print(f'{lang}: removed {removed} duplicates')
with open('data/glossary.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write('\n')
"
```

**Step 3: Verify JSON is valid and Hugo builds**

```bash
python3 -c "import json; json.load(open('data/glossary.json'))" && echo "Valid JSON"
hugo server --disableFastRender &
sleep 3
kill %1
echo "Build OK"
```

**Step 4: Commit**

```bash
git add data/glossary.json
git commit -m "fix: remove 5 duplicate glossary entries

Deduplicates bid-ask-spread, limit-order, market-depth,
market-order, volume which each appeared twice in EN section."
```

---

## Task 4: Override scrollspy.ts — clean console output

**Files:**
- Create: `assets/ts/scrollspy.ts` (copy from `themes/hugo-theme-stack/assets/ts/scrollspy.ts`)

**Step 1: Copy theme file to root override**

```bash
mkdir -p assets/ts
cp themes/hugo-theme-stack/assets/ts/scrollspy.ts assets/ts/scrollspy.ts
```

**Step 2: Replace console.warn with console.debug**

In `assets/ts/scrollspy.ts`, change 3 instances:

- Line 54: `console.warn("No header matched query", headers);` → `console.debug("No header matched query", headers);`
- Line 60: `console.warn("No toc matched query", tocQuery);` → `console.debug("No toc matched query", tocQuery);`
- Line 66: `console.warn("No navigation matched query", navigationQuery);` → `console.debug("No navigation matched query", navigationQuery);`

**Step 3: Verify Hugo builds (TS compilation)**

```bash
hugo --gc --minify 2>&1 | head -5
echo "Exit: $?"
```
Expected: Exit 0, no TypeScript errors

**Step 4: Commit**

```bash
git add assets/ts/scrollspy.ts
git commit -m "refactor: demote scrollspy warnings to debug level

console.warn fires on every page without a ToC (normal behavior).
Override theme file to use console.debug instead."
```

---

## Task 5: Override main.ts — remove alert()

**Files:**
- Create: `assets/ts/main.ts` (copy from `themes/hugo-theme-stack/assets/ts/main.ts`)

**Step 1: Copy theme file to root override**

```bash
cp themes/hugo-theme-stack/assets/ts/main.ts assets/ts/main.ts
```

**Step 2: Fix clipboard error handler**

In `assets/ts/main.ts`, replace lines 87-90:

```typescript
// BEFORE (lines 87-90):
                    .catch(err => {
                        alert(err)
                        console.log('Something went wrong', err);
                    });

// AFTER:
                    .catch(err => {
                        console.error('Clipboard copy failed:', err);
                    });
```

**Step 3: Verify Hugo builds**

```bash
hugo --gc --minify 2>&1 | head -5
echo "Exit: $?"
```

**Step 4: Commit**

```bash
git add assets/ts/main.ts
git commit -m "fix: replace blocking alert() with console.error in clipboard handler

alert() blocks the UI thread. Silent error logging is appropriate
for a non-critical copy-to-clipboard failure."
```

---

## Task 6: Remove duplicate CSS declaration

**Files:**
- Modify: `assets/scss/glossary-links.scss:33`

**Step 1: Remove redundant line**

In `assets/scss/glossary-links.scss`, remove line 33 (`max-width: 300px;`). Line 34 (`max-width: clamp(200px, 80vw, 300px);`) already supersedes it.

Also remove line 31 (`white-space: normal;`) which overrides line 29 (`white-space: nowrap;`) — the intent is `normal` (wrapping tooltip text), so line 29 is the redundant one. Actually both are intentional: line 29 prevents wrapping for short text, line 31 re-enables it for long text with max-width constraint. The `white-space: nowrap` on line 29 is immediately overridden on line 31 though — this is dead code. Remove line 29.

Final cleanup — remove these redundant lines:
- Line 29: `white-space: nowrap;` (overridden by line 31)
- Line 33: `max-width: 300px;` (overridden by line 34)

**Step 2: Verify the tooltip still works**

```bash
hugo server --disableFastRender &
sleep 3
# Open a glossary page with term links and verify tooltips render correctly
kill %1
```

**Step 3: Commit**

```bash
git add assets/scss/glossary-links.scss
git commit -m "fix: remove 2 redundant CSS declarations in glossary tooltip

Removes white-space: nowrap (immediately overridden) and
max-width: 300px (superseded by clamp())."
```

---

## Task 7: Article title h2 → h1

**Files:**
- Modify: `layouts/partials/article/components/details.html:14`

**Step 1: Check theme CSS for h2-specific selectors**

```bash
# Search theme SCSS for any h2.article-title or h2 .article-title selectors
grep -rn 'h2.*article-title\|article-title.*h2' themes/hugo-theme-stack/assets/scss/
```

If any h2-specific selectors exist, note them for CSS override. If only `.article-title` class selectors are used, no CSS change needed.

**Step 2: Change h2 to h1**

In `layouts/partials/article/components/details.html`, line 14:

```html
<!-- BEFORE -->
        <h2 class="article-title">

<!-- AFTER -->
        <h1 class="article-title">
```

Also change the closing tag on line 18:

```html
<!-- BEFORE -->
        </h2>

<!-- AFTER -->
        </h1>
```

**Step 3: Verify build and visual appearance**

```bash
hugo server --disableFastRender &
sleep 3
# Check an article page — title should look identical
# Check homepage article list — titles there use a different template, unaffected
kill %1
```

**Step 4: Commit**

```bash
git add layouts/partials/article/components/details.html
git commit -m "fix(seo): change article title from h2 to h1

Articles had no h1 element, breaking semantic document outline.
Theme styles .article-title by class, so visual output is unchanged."
```

---

## Task 8: Add alt text to list.html

**Files:**
- Create: `layouts/_default/list.html` (override from `themes/hugo-theme-stack/layouts/_default/list.html`)

**Step 1: Copy theme file to root override**

```bash
cp themes/hugo-theme-stack/layouts/_default/list.html layouts/_default/list.html
```

**Step 2: Add alt attributes to images**

In `layouts/_default/list.html`:

Line 35-38 — resource-based image:
```html
<!-- BEFORE -->
                        <img src="{{ $Permalink }}"
                            width="{{ $Width }}"
                            height="{{ $Height }}"
                            loading="lazy">

<!-- AFTER -->
                        <img src="{{ $Permalink }}"
                            width="{{ $Width }}"
                            height="{{ $Height }}"
                            loading="lazy"
                            alt="{{ .Title }}">
```

Line 40 — permalink-based image:
```html
<!-- BEFORE -->
                        <img src="{{ $image.permalink }}" loading="lazy" />

<!-- AFTER -->
                        <img src="{{ $image.permalink }}" loading="lazy" alt="{{ .Title }}" />
```

**Step 3: Verify**

```bash
hugo server --disableFastRender &
sleep 3
# Check a category page (e.g., /categories/analysis/) — images should show alt text in HTML source
kill %1
```

**Step 4: Commit**

```bash
git add layouts/_default/list.html
git commit -m "fix(a11y): add alt text to section/category list images

Override theme list.html to add alt=\"{{ .Title }}\" to both
resource-based and permalink-based category images."
```

---

## Task 9: Add og:image:alt and twitter:image:alt

**Files:**
- Create: `layouts/partials/head/opengraph/provider/base.html`
- Create: `layouts/partials/head/opengraph/provider/twitter.html`

**Step 1: Create directory and copy theme files**

```bash
mkdir -p layouts/partials/head/opengraph/provider
cp themes/hugo-theme-stack/layouts/partials/head/opengraph/provider/base.html layouts/partials/head/opengraph/provider/base.html
cp themes/hugo-theme-stack/layouts/partials/head/opengraph/provider/twitter.html layouts/partials/head/opengraph/provider/twitter.html
```

**Step 2: Add og:image:alt in base.html**

In `layouts/partials/head/opengraph/provider/base.html`, after line 52 (the closing `{{- end -}}` of the image block), add:

```html
    {{- $description := partialCached "data/description" . .RelPermalink -}}
    <meta property='og:image:alt' {{ printf "content=%q" (default .Title $description) | safeHTMLAttr }} />
```

Wait — `$description` is already defined at line 2. So just add after line 52:

```html
    <meta property='og:image:alt' {{ printf "content=%q" (default .Title $description) | safeHTMLAttr }} />
```

Place it inside the `{{- if $image.exists -}}` block, before the closing `{{- end -}}`.

**Step 3: Add twitter:image:alt in twitter.html**

In `layouts/partials/head/opengraph/provider/twitter.html`, after line 15 (twitter:image), add:

```html
    {{- $description := partialCached "data/description" . .RelPermalink -}}
    <meta name="twitter:image:alt" {{ printf "content=%q" (default .Title $description) | safeHTMLAttr }} />
```

Wait — `$description` is already defined at line 7. So just add after line 15:

```html
    <meta name="twitter:image:alt" {{ printf "content=%q" (default .Title $description) | safeHTMLAttr }} />
```

Place it inside the `{{- if $image.exists -}}` block, before the closing `{{- end -}}`.

**Step 4: Verify**

```bash
hugo --gc --minify 2>&1 | head -5
# Check rendered HTML for og:image:alt in public/index.html
grep -o 'og:image:alt.*content="[^"]*"' public/index.html | head -1
grep -o 'twitter:image:alt.*content="[^"]*"' public/index.html | head -1
```

**Step 5: Commit**

```bash
git add layouts/partials/head/opengraph/provider/
git commit -m "fix(seo): add og:image:alt and twitter:image:alt meta tags

Override OG providers to include alt text for social media image
previews, using page description or title as fallback."
```

---

## Task 10: Move font loading from JS to head

**Files:**
- Create: `layouts/partials/footer/components/custom-font.html` (empty override)
- Modify: `layouts/partials/head/custom.html`

**Step 1: Create empty font override to disable JS-based loading**

```bash
mkdir -p layouts/partials/footer/components
```

Create `layouts/partials/footer/components/custom-font.html` with empty content (this overrides the theme's JS-based font loader with nothing).

**Step 2: Add font stylesheet link to head/custom.html**

In `layouts/partials/head/custom.html`, after line 4 (the preconnect to fonts.gstatic.com), add:

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap">
```

**Step 3: Add CDN preconnect (Task 2.6)**

In the same file, after the new font link, add:

```html
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
```

**Step 4: Add Matomo dns-prefetch (Task 2.7)**

Add:

```html
<link rel="dns-prefetch" href="https://ecocrypto.fr">
```

**Step 5: Verify font loading**

```bash
hugo server --disableFastRender &
sleep 3
# Page should render with Lato font — same as before but loaded earlier
# Check that fonts.googleapis.com link appears in <head>, not in footer JS
kill %1
```

**Step 6: Commit**

```bash
git add layouts/partials/footer/components/custom-font.html layouts/partials/head/custom.html
git commit -m "perf: move font loading from JS to head, add resource hints

- Move Google Fonts Lato from JS-injected link to proper stylesheet
  tag in <head> for earlier discovery and JS-independent loading
- Add preconnect for cdn.jsdelivr.net (PhotoSwipe, Vibrant.js)
- Add dns-prefetch for ecocrypto.fr (Matomo analytics)"
```

---

## Task 11: Convert glossary.css → SCSS

**Files:**
- Move: `assets/css/glossary.css` → `assets/scss/glossary.scss`
- Modify: `layouts/glossary/list.html:6-7`
- Modify: `layouts/glossary/glossary-term.html:6-7`

**Step 1: Move CSS file to SCSS directory**

```bash
mv assets/css/glossary.css assets/scss/glossary.scss
```

**Step 2: Minimal SCSS changes**

The file is a 1:1 port. Make these targeted changes only:

1. **Remove 3 `!important` declarations** (lines 907, 911, 915). These are redundant because the base selectors already use `color: var(--card-text-color-main)` and `color: var(--card-text-color-secondary)` — the CSS variables themselves change in dark mode via the theme's `:root[data-scheme="dark"]` block. The `[data-scheme="dark"] .term-name` etc. selectors are entirely redundant dead code. Remove lines 906-916 completely (the 3 redundant dark mode selectors).

2. **Replace hardcoded hex colors with CSS variables** where theme equivalents exist:
   - `#3B82F6` (blue, used for example section) → `var(--glossary-example-color, #3B82F6)` — define in file header
   - `#F59E0B` / `#D97706` (amber, used for risks) → `var(--glossary-risks-color, #F59E0B)` — define in file header
   - `#8B5CF6` (purple, used for FAQ) → `var(--glossary-faq-color, #8B5CF6)` — define in file header

   Add at top of file:
   ```scss
   /* Glossary section accent colors */
   $glossary-example-color: #3B82F6;
   $glossary-risks-color: #F59E0B;
   $glossary-risks-header-color: #D97706;
   $glossary-faq-color: #8B5CF6;
   ```

   Then replace hardcoded hex values with these variables using SCSS interpolation where needed for rgba():
   - Line 439: `rgba(59, 130, 246, 0.05)` → `rgba($glossary-example-color, 0.05)` (SCSS understands hex→rgb)
   - Line 440: `rgba(59, 130, 246, 0.2)` → `rgba($glossary-example-color, 0.2)`
   - Line 442: `#3B82F6` → `$glossary-example-color`
   - Line 462: `#3B82F6` → `$glossary-example-color`
   - Line 471: `rgba(251, 191, 36, 0.08)` → `rgba($glossary-risks-color, 0.08)`
   - Line 472: `rgba(251, 191, 36, 0.25)` → `rgba($glossary-risks-color, 0.25)`
   - Line 474: `#F59E0B` → `$glossary-risks-color`
   - Line 494: `#D97706` → `$glossary-risks-header-color`
   - Line 559: `rgba(139, 92, 246, 0.05)` → `rgba($glossary-faq-color, 0.05)`
   - Line 560: `rgba(139, 92, 246, 0.02)` → keep as-is (same pattern, just lower opacity)
   - Line 578: `#8B5CF6` → `$glossary-faq-color`
   - Line 583: `#8B5CF6` → `$glossary-faq-color`
   - Line 613: `rgba(139, 92, 246, 0.08)` → `rgba($glossary-faq-color, 0.08)`

**Step 3: Update template imports**

In `layouts/glossary/list.html`, replace lines 6-7:

```html
<!-- BEFORE -->
{{ $glossaryCSS := resources.Get "css/glossary.css" | minify | fingerprint }}
<link rel="stylesheet" href="{{ $glossaryCSS.RelPermalink }}">

<!-- AFTER -->
{{ $glossarySCSS := resources.Get "scss/glossary.scss" | toCSS | minify | fingerprint }}
<link rel="stylesheet" href="{{ $glossarySCSS.RelPermalink }}" integrity="{{ $glossarySCSS.Data.Integrity }}" crossorigin="anonymous">
```

In `layouts/glossary/glossary-term.html`, replace lines 6-7:

```html
<!-- BEFORE -->
{{ $glossaryCSS := resources.Get "css/glossary.css" | minify | fingerprint }}
<link rel="stylesheet" href="{{ $glossaryCSS.RelPermalink }}">

<!-- AFTER -->
{{ $glossarySCSS := resources.Get "scss/glossary.scss" | toCSS | minify | fingerprint }}
<link rel="stylesheet" href="{{ $glossarySCSS.RelPermalink }}" integrity="{{ $glossarySCSS.Data.Integrity }}" crossorigin="anonymous">
```

**Step 4: Verify build and visual output**

```bash
hugo server --disableFastRender &
sleep 3
# Navigate to /glossary/ — should look identical
# Navigate to a specific glossary term page — should look identical
# Toggle dark mode — should look identical (and work without !important)
# Check mobile viewport — responsive styles should work
kill %1
```

**Step 5: Remove empty css directory if no files remain**

```bash
ls assets/css/
# If only glossary-term.css remains, leave directory for Task 12
# If empty, rmdir assets/css/
```

**Step 6: Commit**

```bash
git add assets/scss/glossary.scss layouts/glossary/list.html layouts/glossary/glossary-term.html
git rm assets/css/glossary.css 2>/dev/null || true
git commit -m "refactor: convert glossary.css to SCSS

- Extract 4 hardcoded hex colors into SCSS variables
- Remove 3 redundant dark mode selectors (CSS variables handle theming)
- Remove 3 unnecessary !important declarations
- Add SRI integrity to glossary stylesheet link
- No visual changes"
```

---

## Task 12: Convert glossary-term.css → SCSS

**Files:**
- Move: `assets/css/glossary-term.css` → `assets/scss/glossary-term.scss`
- Modify: `layouts/glossary/glossary-term.html:8-9`

**Step 1: Move CSS file to SCSS directory**

```bash
mv assets/css/glossary-term.css assets/scss/glossary-term.scss
```

**Step 2: Minimal SCSS changes**

1. **Replace hardcoded FAQ color** with the variable from glossary.scss:
   - Line 88: `rgba(139, 92, 246, 0.05)` → leave as-is (can't import from sibling SCSS without shared variables file, and creating one violates YAGNI for 2 occurrences)
   - Line 90: `rgba(139, 92, 246, 0.15)` → leave as-is
   - Line 108: `#8B5CF6` → leave as-is

   Actually, since these files are loaded independently (not through the main SCSS pipeline), SCSS variable sharing would require a separate `_variables.scss` partial. That's a bigger refactor than justified. Keep hardcoded values here — they're consistent with glossary.scss's variables.

   The conversion benefit is: Hugo Pipes SCSS processing, SRI integrity, and future ability to use nesting/mixins.

**Step 3: Update template import**

In `layouts/glossary/glossary-term.html`, replace lines 8-9:

```html
<!-- BEFORE -->
{{ $termCSS := resources.Get "css/glossary-term.css" | minify | fingerprint }}
<link rel="stylesheet" href="{{ $termCSS.RelPermalink }}">

<!-- AFTER -->
{{ $termSCSS := resources.Get "scss/glossary-term.scss" | toCSS | minify | fingerprint }}
<link rel="stylesheet" href="{{ $termSCSS.RelPermalink }}" integrity="{{ $termSCSS.Data.Integrity }}" crossorigin="anonymous">
```

**Step 4: Clean up empty css directory**

```bash
rmdir assets/css/ 2>/dev/null && echo "Removed empty css/" || echo "css/ not empty or already gone"
```

**Step 5: Verify**

```bash
hugo server --disableFastRender &
sleep 3
# Navigate to a glossary term page — should look identical
# Check dark mode — should work
# Check mobile layout — should work
kill %1
```

**Step 6: Commit**

```bash
git add assets/scss/glossary-term.scss layouts/glossary/glossary-term.html
git rm -r assets/css/ 2>/dev/null || true
git commit -m "refactor: convert glossary-term.css to SCSS

Moves to Hugo SCSS pipeline with SRI integrity.
Removes empty assets/css/ directory. No visual changes."
```

---

## Task 13: Extract difficulty color variables

**Files:**
- Modify: `assets/scss/custom/difficulty-badges.scss`

**Step 1: Add SCSS variables at top of file**

Add after line 1 (`/* Expertise Level / Difficulty System */`):

```scss
// Difficulty color palette
$difficulty-beginner: #22c55e;
$difficulty-beginner-dark: #16a34a;
$difficulty-intermediate: #fbbf24;
$difficulty-intermediate-dark: #ca8a04;
$difficulty-expert: #f87171;
$difficulty-expert-dark: #dc2626;
```

**Step 2: Replace all hardcoded color instances**

Replace each hardcoded hex with its variable:

Light mode dot colors (lines 13, 17, 21):
- `background-color: #22c55e;` → `background-color: $difficulty-beginner;`
- `background-color: #fbbf24;` → `background-color: $difficulty-intermediate;`
- `background-color: #f87171;` → `background-color: $difficulty-expert;`

Dark mode dot colors (lines 28, 32, 36):
- `background-color: #16a34a;` → `background-color: $difficulty-beginner-dark;`
- `background-color: #ca8a04;` → `background-color: $difficulty-intermediate-dark;`
- `background-color: #dc2626;` → `background-color: $difficulty-expert-dark;`

Widget bar fills (lines 126, 130, 134):
- `background-color: #22c55e;` → `background-color: $difficulty-beginner;`
- `background-color: #fbbf24;` → `background-color: $difficulty-intermediate;`
- `background-color: #f87171;` → `background-color: $difficulty-expert;`

Widget bar fills dark (lines 147, 151, 155):
- `background-color: #16a34a;` → `background-color: $difficulty-beginner-dark;`
- `background-color: #ca8a04;` → `background-color: $difficulty-intermediate-dark;`
- `background-color: #dc2626;` → `background-color: $difficulty-expert-dark;`

Nav tab borders/backgrounds (lines 194-206):
- `border-color: #22c55e;` → `border-color: $difficulty-beginner;`
- `rgba(34, 197, 94, 0.08)` → `rgba($difficulty-beginner, 0.08)`
- `border-color: #fbbf24;` → `border-color: $difficulty-intermediate;`
- `rgba(251, 191, 36, 0.08)` → `rgba($difficulty-intermediate, 0.08)`
- `border-color: #f87171;` → `border-color: $difficulty-expert;`
- `rgba(239, 68, 68, 0.08)` → `rgba($difficulty-expert, 0.08)`

Nav tab dark mode (lines 211-224):
- `border-color: #16a34a;` → `border-color: $difficulty-beginner-dark;`
- `rgba(34, 197, 94, 0.12)` → `rgba($difficulty-beginner, 0.12)` (same base color, different opacity)
- `border-color: #ca8a04;` → `border-color: $difficulty-intermediate-dark;`
- `rgba(251, 191, 36, 0.12)` → `rgba($difficulty-intermediate, 0.12)`
- `border-color: #dc2626;` → `border-color: $difficulty-expert-dark;`
- `rgba(239, 68, 68, 0.12)` → `rgba($difficulty-expert, 0.12)`

**Step 3: Verify**

```bash
hugo --gc --minify 2>&1 | head -5
echo "Exit: $?"
# Check compiled CSS contains correct hex values
grep -o '#22c55e\|#16a34a\|#fbbf24\|#ca8a04\|#f87171\|#dc2626' public/scss/style.*.css | head -20
```

**Step 4: Commit**

```bash
git add assets/scss/custom/difficulty-badges.scss
git commit -m "refactor: extract difficulty colors to SCSS variables

Replaces 18 hardcoded hex color instances with 6 SCSS variables.
Color changes now require editing one line instead of nine."
```

---

## Task 14: Extract error color variable

**Files:**
- Modify: `assets/scss/glossary-links.scss:64-65`
- Modify: `assets/scss/custom.scss:4-6`

**Step 1: Add error color to :root**

In `assets/scss/custom.scss`, add to the `:root` block (after line 5):

```scss
:root {
  --body-text-color: #595959;
  --error-color: #e74c3c;
}
```

**Step 2: Use variable in glossary-links.scss**

In `assets/scss/glossary-links.scss`, lines 64-65:

```scss
// BEFORE
.glossary-term-missing {
  color: #e74c3c;
  border-bottom: 1px dotted #e74c3c;

// AFTER
.glossary-term-missing {
  color: var(--error-color);
  border-bottom: 1px dotted var(--error-color);
```

**Step 3: Verify**

```bash
hugo --gc --minify 2>&1 | head -5
```

**Step 4: Commit**

```bash
git add assets/scss/custom.scss assets/scss/glossary-links.scss
git commit -m "refactor: extract error color to CSS variable

Replaces hardcoded #e74c3c with var(--error-color) for
glossary missing term styling. Defined in :root for reuse."
```

---

## Task 15: Final verification

**Files:** None (verification only)

**Step 1: Full build test**

```bash
hugo --gc --minify
echo "Exit: $?"
```

Expected: Exit 0, no errors

**Step 2: Verify all page types render**

```bash
hugo server --disableFastRender &
sleep 3
# Test these URLs:
# http://localhost:1313/ (homepage)
# http://localhost:1313/p/defi-bullshit-detector/ (article page)
# http://localhost:1313/glossary/ (glossary hub)
# http://localhost:1313/glossary/apy/ (glossary term)
# http://localhost:1313/categories/analysis/ (category list)
# http://localhost:1313/difficulty/beginner/ (difficulty filter)
# http://localhost:1313/fr/ (French homepage)
kill %1
```

**Step 3: Verify h1 is present on article pages**

```bash
grep -c '<h1 class="article-title">' public/p/defi-bullshit-detector/index.html
# Expected: 1
```

**Step 4: Verify no !important in glossary CSS**

```bash
grep '!important' public/scss/glossary.*.css 2>/dev/null
# Expected: no output (all removed)
```

**Step 5: Verify SRI on glossary stylesheets**

```bash
grep 'integrity="sha256' public/glossary/index.html | head -2
# Expected: 2 lines with integrity attributes
```

**Step 6: Check git status is clean**

```bash
git status
# Expected: clean working tree, all changes committed
git log --oneline -15
# Expected: ~14 commits for this audit
```

# Development dependency audit (2026-10-02)

## Scope and result

This is development/CI tooling for a static Hugo site, not a server-side npm
application. The generated website does not ship `node_modules`.

- Base: `e2263b1027ad43b106258e83133768a7d775e7c0`.
- A fresh root `npm audit --json` reported **32 affected package entries**
  (17 moderate, 15 high), representing 19 distinct advisory URLs. The earlier
  count of 27 was a snapshot of an older advisory database.
- `npm audit --omit=dev` reported zero before and after the update.
- The publishing workflow separately fetched `@lhci/cli@0.15.1` with `npx`.
  That dependency graph was outside the root lockfile and resolved Lighthouse
  12.6.1. A fresh isolated install reported another 14 affected package entries
  (2 low, 1 moderate, 11 high). These counts overlap; do not add them together
  or describe them as distinct exploitable vulnerabilities.
- The final lockfile covers local Lighthouse, browser tests, and Lighthouse CI.
  A fresh `npm ci` followed by `npm audit` reports **zero known advisories**
  in the combined graph at the date above. This does not prove the site, tools,
  installed Chrome, GitHub Actions, or their upstream supply chain are secure.

## What actually runs

Hugo builds the static site; TypeScript only typechecks the existing sources.
`test:browser` launches an already-installed Chrome through `puppeteer-core`
and blocks third-party page requests. `lighthouse.sh` uses the installed,
locked Lighthouse binary. `lighthouse:ci` uses the locked LHCI binary against
`public/`, collecting the existing eight URLs three times with mobile settings.
Reports stay on disk and in GitHub Actions artifacts. No LHCI server or public
upload target is configured, and Lighthouse error telemetry is explicitly off.

The Pages deployment remains independent of its non-blocking Lighthouse job.
PR validation does not deploy. It now runs the same complete Lighthouse flow
so wrapper compatibility is tested before merge. Score and byte-budget warnings
remain warnings; missing/invalid reports or metric samples fail the compatibility
check instead of silently becoming warn-only missing-audit results.

## Reachability and remediation

| Advisory family | Baseline path / realistic prerequisite | Resolution |
| --- | --- | --- |
| OpenTelemetry baggage allocation | Lighthouse → Sentry → OpenTelemetry; requires processing attacker-controlled baggage in an instrumented runtime. The static site is not such a runtime and Lighthouse error reporting is opt-in. | Supported Lighthouse/Sentry dependencies now resolve OpenTelemetry 2.11.0. |
| WebSocket memory disclosure / resource exhaustion | Lighthouse/Puppeteer use WebSockets to speak to local Chrome. A malicious peer, exposed debug endpoint, or compromised local browser would be relevant; ordinary static-site visitors do not connect to the Node tool. | `ws` 7.5.13 and 8.22.0, preserving each upstream major range. |
| Archive symlink/path traversal | Puppeteer → browser installer → extract-zip; requires extraction of a malicious archive. This repository uses preinstalled Chrome, rather than downloading browsers in its test script. | Puppeteer 25.12.0 uses the current browser tooling and removes the old extract-zip chain. |
| FTP, proxy-address parsing / classification | Old browser tooling and LHCI proxy-agent → get-uri → basic-ftp; relevant when using attacker-controlled proxy/PAC/FTP inputs. The configured audits use a local static server. | Current Puppeteer removes the old branch; the remaining LHCI FTP parser is narrowly overridden to 6.2.1. |
| Brace expansion resource exhaustion | Old Lighthouse/Sentry → minimatch → brace-expansion; requires hostile patterns processed by the tooling. | Current upstream dependency graph removes the affected branch. |
| Temporary-file traversal/symlinks | LHCI/inquirer → tmp; relevant to hostile temp-directory/prefix inputs. Current filesystem report upload does not use the interactive editor. | Scoped tmp 0.2.7 override. |
| UUID buffer bounds | LHCI → uuid; advisory affects caller-supplied buffers in v3/v5/v6. LHCI uses v4 IDs without those buffers. | Scoped uuid 11.1.1 override. |

These are exposure assessments from this repository's execution paths, not proof
that every upstream advisory is unreachable in every future use of the tools.

## Compatibility choices

- Lighthouse **13.5.0** and Puppeteer Core **25.12.0** are exact direct pins.
  TypeScript remains on its existing 5.x range, locked at 5.9.3.
- Node.js **24 LTS** is the tested development/CI line, recorded in `.nvmrc`,
  `package.json` engines and all three workflow Node selections. Lighthouse
  already required Node >=22.19 before this cleanup; the previous Node 20
  workflow setting was incompatible. Puppeteer 25 also raises its Node floor
  and is ESM-only. Our smoke test was already ESM and does not use the removed
  product/isConnected/clickCount APIs or synchronous executablePath/defaultArgs.
- LHCI **0.15.1** is still the latest published wrapper. Installing it unchanged
  would restore Lighthouse 12.6.1 and advisories. The scoped overrides below
  deliberately cross its declared ranges; they are not blanket `audit --force`.
- Both `@lhci/cli` and `@lhci/utils` resolve `$lighthouse`: the former launches
  its CLI subprocess and the latter imports `generateReport`. Both interfaces
  still exist in 13.5.0. Existing category/metric/resource-summary assertions
  are preserved. Lighthouse engine upgrades can change measured scores; do not
  treat differences from old 12.6.1 results as site regressions by themselves.
- Under LHCI, `tmp` **0.2.7** preserves its fileSync API, and `uuid` **11.1.1**
  is a patched CommonJS-compatible release. Do not blindly move uuid to its
  ESM-only later majors while LHCI still uses `require`.
- LHCI's `get-uri` is restricted to `basic-ftp` **6.2.1**. The APIs it calls
  (`Client`, access/list/lastMod/downloadTo/close) remain available. Version 6
  rejects separate transfer hosts by default, a security-hardening change.
  The site's local audit flow does not need FTP. Proxy-agent is not forced to
  a new ESM-only major.

Remove each override when an upstream LHCI release naturally resolves a patched,
compatible dependency. Re-run the complete browser and Lighthouse flow when
changing overrides; a zero audit count or successful CLI `--version` is not
sufficient evidence of compatibility. LHCI still brings deprecated
inflight/glob/rimraf packages; those maintenance warnings are not hidden, and
are not currently audit findings. Replacing the wrapper is a separate design
choice, not necessary for this bounded upgrade.

## Reproduction and regression checks

```sh
nvm use
npm ci
npm audit
npm audit --omit=dev
npm run test:tooling
npm run test:validators
npm run validate:glossary
npm run validate:frontmatter
npm run validate:content
npm run typecheck
bash scripts/build-images.sh
HUGO_ENV=production HUGO_ENVIRONMENT=production hugo --gc --minify --environment production
npm run validate:site
npm run test:browser
npm run lighthouse:ci
```

Use Hugo Extended 0.161.1, Python 3/PyYAML, the documented image tools, and an
installed Chrome/Chromium. `CHROME_PATH` can select the browser. `make verify`
also covers source, tooling tests, image generation, build and output checks;
browser and full Lighthouse checks remain explicit commands.

LHCI is configured with `includePassedAssertions: true` because its default
output contains only failed assertions. The regression suite exercises the real
LHCI assertion command to protect this integration.

The report verifier requires 24 HTML/JSON report pairs, one representative run
per URL, the pinned engine, no runtime error, and 72 populated median assertions
with all three finite samples. Its regression tests include missing reports,
missing/invalid metric samples, incorrect medians, version drift, public-upload
configuration and ordinary budget warnings. Local before/after Hugo production
builds were byte-identical across all 5,935 files. Final browser/CI results are
recorded on the PR, rather than implied by the lockfile.

## Primary references

- [Lighthouse 13.5.0 release](https://github.com/GoogleChrome/lighthouse/releases/tag/v13.5.0)
- [Puppeteer changelog and v25 migration](https://pptr.dev/CHANGELOG)
- [LHCI 0.15.1 CLI package](https://github.com/GoogleChrome/lighthouse-ci/blob/v0.15.1/packages/cli/package.json)
- [LHCI 0.15.1 utilities package](https://github.com/GoogleChrome/lighthouse-ci/blob/v0.15.1/packages/utils/package.json)
- [WebSocket exhaustion advisory](https://github.com/advisories/GHSA-96hv-2xvq-fx4p)
- [WebSocket disclosure advisory](https://github.com/advisories/GHSA-58qx-3vcg-4xpx)
- [OpenTelemetry advisory](https://github.com/advisories/GHSA-8988-4f7v-96qf)
- [Archive traversal advisory](https://github.com/advisories/GHSA-jmr9-qjv8-65gv)
- [FTP parser advisory](https://github.com/advisories/GHSA-c475-qrg2-pj4r)
- [tmp traversal advisory](https://github.com/advisories/GHSA-ph9p-34f9-6g65)
- [UUID advisory](https://github.com/advisories/GHSA-w5hq-g745-h8pq)
- [basic-ftp v6 compatibility](https://github.com/patrickjuchli/basic-ftp/releases/tag/v6.0.0)
- [Node.js supported release lines](https://nodejs.org/en/about/previous-releases)

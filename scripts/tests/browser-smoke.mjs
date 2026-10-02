import puppeteer from "puppeteer-core";
import assert from "node:assert/strict";
import fs from "node:fs/promises";
import { existsSync } from "node:fs";
import { createServer } from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";
// Exercise the exact production artifact. Nothing is sent to third-party sites.
const repoRoot = fileURLToPath(new URL("../../", import.meta.url));
const publicRoot = path.resolve(
  process.env.BROWSER_PUBLIC_DIR || path.join(repoRoot, "public"),
);
const artifacts = path.resolve(
  process.env.BROWSER_ARTIFACTS_DIR ||
    path.join(repoRoot, "lighthouse-reports/browser-smoke"),
);
await fs.mkdir(artifacts, { recursive: true });
const contentTypes = {
  ".html": "text/html",
  ".js": "text/javascript",
  ".css": "text/css",
  ".json": "application/json",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".webp": "image/webp",
  ".avif": "image/avif",
  ".woff2": "font/woff2",
  ".ico": "image/x-icon",
};
const server = createServer(async (request, response) => {
  try {
    const pathname = decodeURIComponent(
      new URL(request.url, "http://localhost").pathname,
    );
    let file = path.resolve(publicRoot, "." + pathname);
    if (!file.startsWith(publicRoot + path.sep) && file !== publicRoot)
      throw new Error("Invalid path");
    if ((await fs.stat(file)).isDirectory())
      file = path.join(file, "index.html");
    response.setHeader(
      "Content-Type",
      contentTypes[path.extname(file)] || "application/octet-stream",
    );
    response.end(await fs.readFile(file));
  } catch {
    response.statusCode = 404;
    response.end("Not found");
  }
});
await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
const root = `http://127.0.0.1:${server.address().port}`;
const executablePath =
  process.env.CHROME_PATH ||
  [
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
  ].find(existsSync);
let browser;
let page;
const errors = [];
async function go(route) {
  await page.goto(root + route, { waitUntil: "networkidle0" });
}
async function screenshot(name) {
  await page.screenshot({
    path: path.join(artifacts, name + ".png"),
    fullPage: false,
  });
}
try {
  if (!executablePath)
    throw new Error(
      "Set CHROME_PATH to an installed Chrome or Chromium executable.",
    );
  browser = await puppeteer.launch({
    executablePath,
    headless: true,
    args: ["--no-sandbox", "--disable-dev-shm-usage"],
  });
  page = await browser.newPage();
  page.on("pageerror", (error) => errors.push(String(error)));
  await page.setRequestInterception(true);
  page.on("request", (request) =>
    request.url().startsWith(root + "/") || request.url().startsWith("data:")
      ? request.continue()
      : request.abort(),
  );
  await page.emulateMediaFeatures([
    { name: "prefers-color-scheme", value: "light" },
    { name: "prefers-reduced-motion", value: "reduce" },
  ]);
  await page.setViewport({ width: 1440, height: 960 });
  for (const lang of ["", "/fr"]) {
    await go(lang + "/");
    assert.equal(
      await page.$$eval(".home-projects__project", (x) => x.length),
      2,
    );
    assert.deepEqual(
      await page.$$eval(".home-projects__intro", (xs) =>
        xs.map((x) => new URL(x.href).pathname),
      ),
      [lang + "/pharos/", lang + "/why-polaris/"],
    );
    const widths = await page.$$eval(".home-projects__project", (xs) =>
      xs.map((x) => x.getBoundingClientRect().width),
    );
    assert.ok(Math.abs(widths[0] - widths[1]) < 1);
    assert.equal(
      await page.$eval("#sidebar-search-input", (x) =>
        x.labels[0].textContent.trim(),
      ),
      lang ? "Rechercher" : "Search",
    );
    await screenshot(`${lang ? "fr" : "en"}-desktop`);
  }
  await go("/pharos/");
  await page.keyboard.press("Tab");
  await page.keyboard.press("Enter");
  assert.equal(
    await page.evaluate(() => document.activeElement.id),
    "main-content",
  );
  await page.keyboard.press("Tab");
  assert.ok(
    await page.evaluate(() =>
      document.querySelector("#main-content").contains(document.activeElement),
    ),
  );
  await page.focus("#TableOfContents a");
  await page.keyboard.press("Enter");
  assert.match(
    await page.evaluate(() => document.activeElement.tagName),
    /^H[2-6]$/,
  );
  for (const height of [600, 768]) {
    await page.setViewport({ width: 1173, height });
    await go("/fr/difficulty/beginner/");
    const overflow = await page.$eval("#main-menu", (e) => ({
      client: e.clientHeight,
      scroll: e.scrollHeight,
    }));
    assert.ok(overflow.scroll > overflow.client);
    await page.focus("#dark-mode-toggle button");
    const rect = await page.$eval("#dark-mode-toggle button", (e) => ({
      y: e.getBoundingClientRect().y,
      bottom: e.getBoundingClientRect().bottom,
    }));
    assert.ok(rect.y >= 0 && rect.bottom <= height, JSON.stringify(rect));
  }
  await page.setViewport({ width: 1173, height: 768 });
  await go("/fr/glossary/");
  for (const query of [
    "trésorerie",
    "tresorerie",
    "tre\u0301sorerie",
    "  TRESORERIE  ",
  ]) {
    await page.$eval(
      "#glossary-search",
      (e, q) => {
        e.value = q;
        e.dispatchEvent(new Event("input", { bubbles: true }));
      },
      query,
    );
    assert.equal(
      await page.$eval("#result-count", (e) => Number(e.textContent)),
      2,
      query,
    );
  }
  await page.$eval("#glossary-search", (e) => {
    e.value = "";
    e.dispatchEvent(new Event("input", { bubbles: true }));
  });
  await page.focus('.alphabet-link[data-letter="T"]');
  await page.keyboard.press("Enter");
  assert.equal(
    await page.evaluate(() => document.activeElement.id),
    "letter-T",
  );
  await page.keyboard.press("Tab");
  assert.ok(
    await page.evaluate(() =>
      document.querySelector("#letter-T").contains(document.activeElement),
    ),
  );
  for (const fragment of ["#cat=%ZZ", "#cat=%22%5D%5B", "#cat=unknown"]) {
    await go("/fr/glossary/" + fragment);
    assert.ok(
      (await page.$eval("#result-count", (e) => Number(e.textContent))) > 0,
    );
  }
  for (const lang of ["", "/fr"]) {
    await go(lang + "/archives/");
    await page.waitForFunction(() =>
      Array.from(
        document.querySelectorAll(
          ".article-list--tile article.has-image .article-details",
        ),
      ).some((x) => x.style.background),
    );
    assert.equal(await page.evaluate(() => typeof Vibrant.from), "function");
  }
  await go("/search/?keyword=stablecoin");
  await page.waitForSelector(".search-result--list article");
  assert.ok(
    !(await page.$eval(".search-result--list", (e) => e.textContent)).includes(
      "&rsquo;",
    ),
  );
  const history = await page.evaluate(() => window.history.length);
  await page.focus(".search-page-form input");
  await page.keyboard.press("Enter");
  await page.keyboard.press("Enter");
  assert.equal(await page.evaluate(() => window.history.length), history);
  await page.setViewport({ width: 390, height: 844 });
  for (const lang of ["", "/fr"]) {
    await go(lang + "/");
    assert.ok(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= innerWidth,
      ),
    );
    await screenshot(`${lang ? "fr" : "en"}-mobile`);
    await page.click("#toggle-menu");
    assert.equal(
      await page.$eval("#toggle-menu", (e) => e.getAttribute("aria-expanded")),
      "true",
    );
    await page.focus("#dark-mode-toggle button");
    await page.keyboard.press("Enter");
    assert.equal(
      await page.evaluate(() => document.documentElement.dataset.scheme),
      "dark",
    );
    await page.click("#toggle-menu");
    await screenshot(`${lang ? "fr" : "en"}-mobile-dark`);
    await page.click("#toggle-menu");
    await page.click("#dark-mode-toggle button");
    await page.click("#toggle-menu");
  }
  for (const route of [
    "/about/",
    "/fr/a-propos/",
    "/static-roots/",
    "/static-edge/",
  ]) {
    await go(route);
    const missing = await page.$$eval(".article-content img", (images) =>
      images
        .filter(
          (img) =>
            !img.getAttribute("width") ||
            !img.getAttribute("height") ||
            img.loading !== "lazy" ||
            !img.srcset,
        )
        .map((img) => img.src),
    );
    assert.deepEqual(missing, [], `Responsive image attributes: ${route}`);
    assert.ok(
      await page.evaluate(
        () => document.documentElement.scrollWidth <= innerWidth,
      ),
      `No mobile overflow: ${route}`,
    );
    await screenshot(route.replaceAll("/", "") + "-mobile");
  }
  assert.deepEqual(errors, []);
  console.log(
    "PASS: project parity, EN/FR links, search labels, keyboard jumps, short sidebars, accent glossary search, malformed fragments, archives palette, entity decoding, search history and mobile dark/menu checks.",
  );
} catch (error) {
  if (page) await screenshot("failure").catch(() => {});
  throw error;
} finally {
  await browser?.close();
  await new Promise((resolve) => server.close(resolve));
}

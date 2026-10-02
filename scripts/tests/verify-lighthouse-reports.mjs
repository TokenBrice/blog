import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

// A warn-only budget must not hide a broken audit, missing metric or override.
// This deliberately checks our small LHCI configuration, not every LHCI option.
export function verifyReports(root = process.cwd()) {
  const readJSON = (file) => JSON.parse(fs.readFileSync(path.resolve(root, file), 'utf8'));
  const { ci } = readJSON('.lighthouserc.json');
  const { devDependencies } = readJSON('package.json');
  assert.equal(ci.upload.target, 'filesystem');
  assert.equal(ci.assert.includePassedAssertions, true, 'LHCI must retain passing assertions');
  const routes = ci.collect.url.map((url) => new URL(url).pathname);
  assert.equal(new Set(routes).size, routes.length, 'Audit routes must be unique');
  const runs = ci.collect.numberOfRuns;
  assert.ok(Number.isInteger(runs) && runs > 0);
  const manifest = readJSON(path.join(ci.upload.outputDir, 'manifest.json'));
  assert.equal(manifest.length, routes.length * runs, 'Missing Lighthouse reports');
  for (const route of routes) {
    const entries = manifest.filter((entry) => new URL(entry.url).pathname === route);
    assert.equal(entries.length, runs, `Missing samples: ${route}`);
    assert.equal(entries.filter((entry) => entry.isRepresentativeRun).length, 1);
    assert.equal(new Set(entries.map((entry) => entry.jsonPath)).size, runs);
    for (const entry of entries) {
      const report = readJSON(entry.jsonPath);
      assert.equal(report.lighthouseVersion, devDependencies.lighthouse);
      assert.ok(!report.runtimeError, `Lighthouse runtime error: ${route}`);
      assert.equal(new URL(report.requestedUrl).pathname, route);
      assert.equal(new URL(report.finalDisplayedUrl || report.finalUrl).pathname, route);
      assert.equal(report.configSettings.formFactor, ci.collect.settings.formFactor);
      assert.match(fs.readFileSync(path.resolve(root, entry.htmlPath), 'utf8'), /<!doctype html>/i);
    }
  }
  const assertions = readJSON('.lighthouseci/assertion-results.json');
  const configured = Object.entries(ci.assert.assertions);
  assert.equal(assertions.length, routes.length * configured.length, 'Missing budget assertions');
  for (const route of routes) {
    for (const [key, [level, options]] of configured) {
      const [auditId, ...property] = key.split(':');
      const matches = assertions.filter((result) =>
        new URL(result.url).pathname === route && result.auditId === auditId &&
        (result.auditProperty || '') === property.join('.'));
      assert.equal(matches.length, 1, `Missing or duplicate assertion: ${route} ${key}`);
      const [result] = matches;
      const limit = options.minScore === undefined ? 'maxNumericValue' : 'minScore';
      assert.equal(result.name, limit, `Audit did not run: ${route} ${key}`);
      assert.equal(result.level, level);
      assert.equal(result.expected, options[limit]);
      assert.equal(options.aggregationMethod, 'median');
      assert.equal(result.values.length, runs, `Incomplete metric samples: ${route} ${key}`);
      assert.ok(result.values.every(Number.isFinite), `Invalid metric: ${route} ${key}`);
      const sorted = [...result.values].sort((a, b) => a - b);
      const median = (sorted[Math.floor((runs - 1) / 2)] + sorted[Math.floor(runs / 2)]) / 2;
      assert.equal(result.actual, median, `Incorrect median: ${route} ${key}`);
      const passed = limit === 'minScore' ? median >= result.expected : median <= result.expected;
      assert.equal(result.passed, passed);
      // Ordinary score/byte budget warnings remain non-blocking.
    }
  }
  return { reports: manifest.length, assertions: assertions.length };
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const result = verifyReports();
  console.log(`OK: ${result.reports} Lighthouse reports and ${result.assertions} median assertions verified`);
}

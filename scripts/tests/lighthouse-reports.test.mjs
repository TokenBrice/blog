import assert from 'node:assert/strict';
import { test } from 'node:test';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { verifyReports } from './verify-lighthouse-reports.mjs';

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'tb-lighthouse-test-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  const write = (file, data) => {
    const output = path.join(root, file);
    fs.mkdirSync(path.dirname(output), { recursive: true });
    fs.writeFileSync(output, JSON.stringify(data));
  };
  const config = { ci: {
    collect: { url: ['http://localhost/'], numberOfRuns: 3, settings: { formFactor: 'mobile' } },
    assert: { assertions: { 'categories:performance': ['warn', { minScore: 0.85, aggregationMethod: 'median' }] } },
    upload: { target: 'filesystem', outputDir: 'reports' },
  } };
  write('.lighthouserc.json', config);
  write('package.json', { devDependencies: { lighthouse: '13.5.0' } });
  const report = { lighthouseVersion: '13.5.0', requestedUrl: 'http://localhost:4321/',
    finalDisplayedUrl: 'http://localhost:4321/', configSettings: { formFactor: 'mobile' } };
  const manifest = [0, 1, 2].map((i) => ({ url: report.requestedUrl,
    isRepresentativeRun: i === 1, jsonPath: `reports/${i}.json`, htmlPath: `reports/${i}.html` }));
  for (const entry of manifest) {
    write(entry.jsonPath, report);
    fs.writeFileSync(path.join(root, entry.htmlPath), '<!doctype html><title>Lighthouse</title>');
  }
  write('reports/manifest.json', manifest);
  const results = [{ url: report.requestedUrl, auditId: 'categories', auditProperty: 'performance',
    level: 'warn', name: 'minScore', expected: 0.85, actual: 0.9, values: [1, 0.8, 0.9], passed: true }];
  write('.lighthouseci/assertion-results.json', results);
  return { root, write, config, report, manifest, results };
}

test('complete reports and median assertions pass', (t) => {
  assert.deepEqual(verifyReports(fixture(t).root), { reports: 3, assertions: 1 });
});
test('ordinary budget warning remains non-blocking', (t) => {
  const f = fixture(t);
  Object.assign(f.results[0], { actual: 0.5, values: [0.4, 0.5, 0.6], passed: false });
  f.write('.lighthouseci/assertion-results.json', f.results);
  assert.doesNotThrow(() => verifyReports(f.root));
});
for (const [name, mutate] of Object.entries({
  'missing report': (f) => f.write('reports/manifest.json', f.manifest.slice(1)),
  'duplicate report': (f) => f.write('reports/manifest.json', [f.manifest[0], f.manifest[0], f.manifest[1]]),
  'wrong Lighthouse version': (f) => f.write('reports/0.json', { ...f.report, lighthouseVersion: '12.6.1' }),
  'audit runtime error': (f) => f.write('reports/0.json', { ...f.report, runtimeError: { code: 'FAILED' } }),
  'wrong final route': (f) => f.write('reports/0.json', { ...f.report, finalDisplayedUrl: 'http://localhost/404/' }),
  'missing HTML output': (f) => fs.writeFileSync(path.join(f.root, 'reports/0.html'), ''),
  'missing assertion': (f) => f.write('.lighthouseci/assertion-results.json', []),
  'invalid metric': (f) => { f.results[0].values[0] = null; f.write('.lighthouseci/assertion-results.json', f.results); },
  'missing metric sample': (f) => { f.results[0].values.pop(); f.write('.lighthouseci/assertion-results.json', f.results); },
  'incorrect median': (f) => { f.results[0].actual = 1; f.write('.lighthouseci/assertion-results.json', f.results); },
  'unknown audit': (f) => { f.results[0].name = 'auditRan'; f.write('.lighthouseci/assertion-results.json', f.results); },
  'changed threshold': (f) => { f.results[0].expected = 0; f.write('.lighthouseci/assertion-results.json', f.results); },
  'public upload': (f) => { f.config.ci.upload.target = 'temporary-public-storage'; f.write('.lighthouserc.json', f.config); },
})) {
  test(`rejects ${name}`, (t) => {
    const f = fixture(t);
    mutate(f);
    assert.throws(() => verifyReports(f.root));
  });
}

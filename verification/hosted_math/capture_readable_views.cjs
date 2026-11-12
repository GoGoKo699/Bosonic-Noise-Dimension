#!/usr/bin/env node
'use strict';
// Supplement the structural collector with settled, unobscured page images.
// This does not replace its report or certify that a human inspected the images.
const fs = require('node:fs');
const path = require('node:path');
const cp = require('node:child_process');
const crypto = require('node:crypto');
const {chromium} = require('playwright');
const {VIEWPORTS, safePath, waitForHostedMath} = require('./capture_hosted_math.cjs');
const digest = bytes => crypto.createHash('sha256').update(bytes).digest('hex');

async function main() {
  const [root, reportDirectory, output] = process.argv.slice(2);
  if (!root || !reportDirectory || !output || process.argv.length !== 5)
    throw new Error('Usage: capture_readable_views.cjs ROOT COLLECTOR_DIRECTORY NEW_OUTPUT_DIRECTORY');
  if (fs.existsSync(output)) throw new Error('Output must be a new directory');
  const report = JSON.parse(fs.readFileSync(path.join(reportDirectory, 'hosted-report.json')));
  const inventory = JSON.parse(fs.readFileSync(path.join(reportDirectory, 'math-source.json')));
  if (report.status !== 'pass' || report.capture_method !== 'playwright-github' ||
      report.revision !== inventory.revision || report.repository !== inventory.repository)
    throw new Error('A passing, matching structural report is required');
  const git = args => cp.execFileSync('git', ['--no-replace-objects', ...args], {cwd: root});
  if (git(['rev-parse', inventory.revision + '^{tree}']).toString().trim() !== report.tree)
    throw new Error('Git tree differs from the structural report');
  fs.mkdirSync(output, {recursive: true});
  const receipt = {schema_version: 1, kind: 'supplementary_visual_capture',
    repository: report.repository, revision: report.revision, tree: report.tree,
    structural_report_sha256: digest(fs.readFileSync(path.join(reportDirectory, 'hosted-report.json'))),
    method: 'Actual GitHub Chromium pages; wait for math and fonts, reset scroll, capture without changing page content or styling.',
    pages: [], limits: 'Supplementary images only; source comparison and visual inspection remain separate.'};
  const browser = await chromium.launch({headless: true});
  try {
    for (const viewport of VIEWPORTS) {
      const context = await browser.newContext({viewport, deviceScaleFactor: 1, colorScheme: 'light'});
      try {
        for (const [index, source] of inventory.pages.entries()) {
          if (!safePath(source.path) || digest(git(['show', inventory.revision + ':' + source.path])) !== source.source_sha256)
            throw new Error('Source binding failed: ' + source.path);
          const expectedURL = 'https://github.com/' + inventory.repository + '/blob/' + inventory.revision + '/' + source.path;
          if (source.url !== expectedURL) throw new Error('Unexpected source URL');
          const page = await context.newPage();
          try {
            const response = await page.goto(source.url, {waitUntil: 'domcontentloaded', timeout: 60000});
            if (response?.status() !== 200 || page.url() !== source.url) throw new Error('Pinned GitHub page unavailable');
            const article = page.locator('article.markdown-body').first();
            await article.waitFor({state: 'visible', timeout: 30000});
            await page.evaluate(async () => {
              for (let y = 0, count = 0; y < document.body.scrollHeight && count < 200; y += 900, count++) {
                window.scrollTo(0, y);
                await new Promise(resolve => setTimeout(resolve, 50));
              }
            });
            await waitForHostedMath(article, source.expressions.length);
            await page.evaluate(async () => {
              await Promise.race([document.fonts.ready, new Promise(resolve => setTimeout(resolve, 5000))]);
              window.scrollTo(0, 0);
              await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
            });
            await page.waitForTimeout(750);
            const before = await page.evaluate(() => ({scrollY: window.scrollY, width: innerWidth, height: innerHeight}));
            if (before.scrollY !== 0 || before.width !== viewport.width) throw new Error('Viewport did not settle at the top');
            const name = String(index + 1).padStart(4, '0') + '-' + viewport.width + '.png';
            await page.screenshot({path: path.join(output, name), fullPage: true, timeout: 30000});
            const bytes = fs.readFileSync(path.join(output, name));
            receipt.pages.push({path: source.path, url: page.url(), source_sha256: source.source_sha256,
              viewport, before, observed_at: new Date().toISOString(), screenshot: name,
              size_bytes: bytes.length, sha256: digest(bytes)});
            fs.writeFileSync(path.join(output, 'visual-captures.json'), JSON.stringify(receipt, null, 2) + '\n');
          } finally { await page.close(); }
        }
      } finally { await context.close(); }
    }
  } finally { await browser.close(); }
  console.log('Saved ' + receipt.pages.length + ' settled GitHub page images for visual inspection.');
}

main().catch(error => {console.error(error); process.exitCode = 1;});

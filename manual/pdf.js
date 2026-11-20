// Build the manual PDF from site/index.html. Run from anywhere: paths are relative to this script.
// Usage: node pdf.js [out.pdf]     (needs: npm i playwright && npx playwright install chromium)
const { chromium } = require('playwright');
const path = require('path'); const fs = require('fs'); const { pathToFileURL } = require('url');
(async () => {
  const site = path.join(__dirname, 'site', 'index.html');
  const out = process.argv[2] || path.join(__dirname, 'out', 'LFH_v1_Build_Manual.pdf');
  fs.mkdirSync(path.dirname(out), { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto(pathToFileURL(site).href); await p.waitForTimeout(800);
  await p.pdf({ path: out, format: 'A4', printBackground: true, margin: { top: '12mm', bottom: '12mm', left: '10mm', right: '10mm' } });
  await b.close(); console.log('wrote', out);
})();

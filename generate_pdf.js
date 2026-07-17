const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  const htmlPath = path.resolve(__dirname, 'planner_source', 'index.html');
  await page.goto('file:///' + htmlPath.replace(/\\/g, '/'), { waitUntil: 'networkidle0' });

  await page.pdf({
    path: path.resolve(__dirname, 'secure', 'planner-tdah-produtivo.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: 0, right: 0, bottom: 0, left: 0 }
  });

  await browser.close();
  console.log('PDF gerado com sucesso!');
})();

const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const { Options } = require('selenium-webdriver/chrome');

const axios = require('axios');
const cheerio = require('cheerio');

(async function example() {
  const options = new Options();
  options.addArguments('--ignore-certificate-errors');
  const driver = new Builder().forBrowser('chrome').setChromeOptions(options).build();


  try {
    await driver.manage().window().maximize(); // Maximize the window
    await driver.get('https://www.seedchecks.com/');

    const html = await axios.get('https://www.seedchecks.com/');
    const $ = cheerio.load(html.data);
    
    // Find and click the "Submit your deck" button
    const submitButton = await driver.findElement(By.xpath(`//div[contains(text(), "Submit your deck")]`));
    await submitButton.click();
    
    // Wait for the input fields to appear
    await driver.wait(until.elementLocated(By.css('input[type="text"]')), 10000);
    
    // Find the input fields based on the labels
    const labels = ['Link to deck', 'Link to memo','One or two sentences describing what you do', 'Startup website (if available)','Email address', 'Personal LinkedIn URL','Region your startup targets','Startup valuation'];
    for (let i = 0; i < labels.length; i++) {
      const label = labels[i];
      const inputField = await driver.findElement(By.xpath(`//label[contains(text(), "${label}")]//following-sibling::*[self::input or self::textarea or self::select]`));
      const options = await inputField.findElements(By.tagName('option'));
        if (options.length >= 2) {
            await options[1].click();
      } else {
        const randomText = Math.random().toString(36).substring(7);
        await inputField.sendKeys(randomText);
        console.log(`Wrote "${randomText}" into ${label}`);
      }
    }
    // Add a wait time before quitting (in milliseconds)
    await new Promise(resolve => setTimeout(resolve, 5000)); //5 seconds wait time 
  } finally {
    // await driver.quit();
  }
})();

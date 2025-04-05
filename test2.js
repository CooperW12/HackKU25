import puppeteer from 'puppeteer';

function sleep(ms){ //the snoozer
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
  try {
    console.log("connecting to browser...");
    const browser = await puppeteer.connect({
       browserWSEndpoint: '???' //<----challenge (impossible)
       });
    
    console.log("Navigating to URL...");
    await page.goto('https://gmail.com', {
      waitUntil: 'domcontentloaded',
      timeout: 30000000
    });
    await sleep(1000);

    html = await page.content(); // <----SEND TO PYTHON AI THING
    selector = "" //FROM FLASK?
    
    console.log("Clicking");
    await page.waitForSelector(selector, { visible: true });
    await page.click(selector);
    
  
    console.log("Closing browser...");
    browser.disconnect();
  } catch (error) {
    console.error("Error:", error);
    process.exit(1);
  }
})();
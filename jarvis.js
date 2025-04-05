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

    html = await page.content(); // <----SEND TO PYTHON AI THING
    selector = "" //FROM FLASK?

    //console.log("Clicking");
    //await page.waitForSelector(selector, { visible: true });
    //await page.click(selector);
    
    console.log("Disconnecting...");
    browser.disconnect();
  } catch (error) {
    console.error("Error:", error);
    process.exit(1);
  }
})();
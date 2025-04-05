import puppeteer from 'puppeteer';

function sleep(ms){ //the snoozer
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
  try {
    console.log("Launching browser...");
    const browser = await puppeteer.launch({ headless: false });
    
    console.log("Opening new page...");
    const page = await browser.newPage();
    
    console.log("Navigating to URL...");
    await page.goto('https://gmail.com', {
      waitUntil: 'domcontentloaded',
      timeout: 300000000
    });
    console.log("4. Page loaded successfully!");
    
    //console.log("5. Typing in search box...");
    //await page.waitForSelector("input[name='username']", { visible: true });
    //await page.type("input[name='username']", 'blah blah blah');
    await sleep(1000);

    html = await page.content(); // <----SEND TO PYTHON AI THING
    selector = "" //FROM FLASK?
    
    console.log("Clicking");
    await page.waitForSelector(selector, { visible: true });
    await page.click(selector);
    
  
    console.log("8. Closing browser...");
    await browser.close();
  } catch (error) {
    console.error("Error:", error);
    process.exit(1);
  }
})();
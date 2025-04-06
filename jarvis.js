import puppeteer from 'puppeteer';

function sleep(ms){ //the snoozer
    return new Promise(resolve => setTimeout(resolve, ms));
}

import fs from 'fs'; // Default import

function saveStringToFile(filepath, text) {
  fs.writeFile(filepath, text, (err) => {
    if (err) {
      console.error("An error occurred while writing the file:", err);
    } else {
      console.log("File has been saved successfully.");
    }
  });
}

let testJSON = {
    "status": "CONTINUE",
    "target_element": "textarea.gLFyf",
    "command": "TYPE",
    "message": "cheap airfryers near me"
};

(async () => {
    try {
      //CONNECT LIVE
      //console.log("connecting to browser...");
      //const browser = await puppeteer.connect({
      //   browserWSEndpoint: '???' // <----challenge (impossible)
      //   });
  
      //MANUAL LAUNCH
      console.log("Launching browser...");
      const browser = await puppeteer.launch({ headless: false });
      
      console.log("Opening new page...");
      let page = await browser.newPage();
      
      console.log("Navigating to URL...");
      await page.goto('https://google.com', {
        waitUntil: 'domcontentloaded',
      });
      console.log("4. Page loaded successfully!");
  
  
      const interactableElementsString = await page.$$eval(
          'a, button, input, select, textarea, [role="button"], [onclick]',
          (elements) => JSON.stringify(
            elements.map((el) => ({
              tag: el.tagName.toLowerCase(),
              text: el.textContent.trim(),
              id: el.id,
              classes: el.className,
              href: el.href || null,
              type: el.type || null,
              name: el.name || null,
              role: el.getAttribute('role'),
              onClick: el.getAttribute('onclick'),
            })),
            null,  // Replacer (optional)
            2     // Indentation for pretty-printing
          )
        );
  
      // Usage
      const filePath = 'testweb.txt'; // Specify the desired file path
      saveStringToFile(filePath, interactableElementsString);
  
      await sleep(1000);
  
      let selector = testJSON["target_element"]
  
      switch (testJSON["command"]) {
          case "CLICK":
              console.log("Clicking");
              await page.locator(selector).click();
              break;
          case "TYPE":
              console.log("typing");
              await page.locator(selector).fill(testJSON["message"]);
              await page.keyboard.press('Enter'); // Simulates pressing the Enter key
              break;
          default:
              console.log("couldnt process command?...")
              break;
      }
    
    console.log("Disconnecting...");
    browser.disconnect();
  } catch (error) {
    console.error("Error:", error);
    process.exit(1);
  }
})();
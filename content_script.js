//listen for messages from popup
console.log("Content script loaded!"); //shows up in web console

browser.runtime.onMessage.addListener((message) => {
  console.log("Received in content script:", message); //same as above
  return Promise.resolve("Message received!");
});

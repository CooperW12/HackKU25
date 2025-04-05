//Listen for messages from popup
console.log("Content script loaded!"); //Shows up in web console

browser.runtime.onMessage.addListener((message) => {
  console.log("Received in content script:", message); //Same as above
  return Promise.resolve("Message received!");
});

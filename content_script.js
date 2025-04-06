
// Listen for messages from popup
console.log("Content script loaded!");

browser.runtime.onMessage.addListener(async (message) => {
    if (message.action === "userPrompt") {
        console.log("Friendly Neighborhood User: ", message.prompt);
        
        // Get the HTML of the current page
        
        // Send back to popup.js
    }
    else if (message.action === "apiResponse") {
        console.log("A message from far, far away: ", message.data.response);
        // Do something with the message from the heroku server
    }
    return Promise.resolve("Message received");
});
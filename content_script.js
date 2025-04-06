//Listen for messages from popup
console.log("Content script loaded!"); //Shows up in web console

browser.runtime.onMessage.addListener((message) => {
    if (message.action === "userPrompt") {
        console.log("Friendly Neighborhood User: ", message.prompt);
    }
    else if (message.action === "apiResponse") {
        console.log("A message from far, far away: ", message.data.response);
        //basically do something with the message we recieve from the heroku server
    }
    return Promise.resolve("Message received");
});

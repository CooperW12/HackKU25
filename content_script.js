// Listen for messages from popup
console.log("Content script loaded!");

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "userPrompt") {
        console.log("Friendly Neighborhood User: ", message.prompt);
        const instruction = message.prompt;
        const htmlCode = document.documentElement.outerHTML;

        const jsonObject = {
            htmlCode: htmlCode,
            instruction: instruction
        };
        console.log("Sending to popup:", jsonObject);
        sendResponse(jsonObject);
    }
    else if (message.action === "apiResponse") {
        console.log("API Response:", message.data);
        // Process the API response here
    }
    return true; // Required for async response
});
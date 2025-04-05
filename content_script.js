// Listen for messages from popup
browser.runtime.onMessage.addListener((message) => {
    if (message.action === "userPrompt") {
      console.log("Prompt received in content script:", message.prompt);
      // You can forward this to your backend API here
    }
  });

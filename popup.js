document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('prompt-input');
    const button = document.getElementById('submit-btn');
    
    button.addEventListener('click', () => {
      const prompt = input.value.trim();
      if (prompt) {
        // Log to console (visible in Browser Toolbox)
        console.log("User prompt:", prompt);
        
        // Send to content script (optional)
        browser.tabs.query({active: true, currentWindow: true})
          .then(tabs => {
            browser.tabs.sendMessage(tabs[0].id, {
              action: "userPrompt", 
              prompt: prompt
            });
          });
        
        // Clear input
        input.value = '';
      }
    });
  });

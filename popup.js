document.getElementById('prompt-input').style.resize = 'vertical';

document.addEventListener('DOMContentLoaded', () => {
    const titleElement = document.getElementById('typing-title');
    const fullText = "Jarvis Prompt";
    let i = 0;
    
    function typeWriter() {
      if (i < fullText.length) {
        titleElement.innerHTML += fullText.charAt(i);
        i++;
        setTimeout(typeWriter, 100); //type speed adjuster
      }
    }
    
    setTimeout(typeWriter, 300); //Create the animation
    const input = document.getElementById('prompt-input');
    const button = document.getElementById('submit-btn');
  
    button.addEventListener('click', async () => {
      const prompt = input.value.trim();
      if (prompt) {
        //Log to popup console
        console.log("POPUP LOG:", prompt);
        
        //Send to content script
        try {
          const tabs = await browser.tabs.query({active: true, currentWindow: true});
          await browser.tabs.sendMessage(tabs[0].id, {
            action: "userPrompt",
            prompt: prompt
          });
          console.log("Message sent to content script");
        } catch (err) {
          console.error("Failed to send message:", err);
        }
        
        // 3. send to background script if we have one.
        //browser.runtime.sendMessage({
          //action: "userPrompt", 
          //prompt: prompt
        //}).then(response => {
          //console.log("Background response:", response);
        //}).catch(err => {
          //console.error("Background error:", err);
        //});
        
        input.value = '';
      }
    });
  });
console.log("JARVIS content script loaded - enhanced version");

// Utility functions
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function getPageState(userGoal = null) {
  // Get all interactable elements
  const interactableElements = Array.from(document.querySelectorAll(
    'a, button, input, select, textarea, [role="button"], [onclick], [contenteditable="true"]'
  )).map(el => {
    const rect = el.getBoundingClientRect();
    return {
      tag: el.tagName.toLowerCase(),
      text: el.textContent?.trim() || '',
      id: el.id,
      classes: el.className,
      href: el.href || null,
      type: el.type || null,
      name: el.name || null,
      placeholder: el.placeholder || null,
      role: el.getAttribute('role'),
      onClick: el.getAttribute('onclick'),
      value: el.value || null,
      isVisible: rect.width > 0 && rect.height > 0 && 
                getComputedStyle(el).visibility !== 'hidden' && 
                getComputedStyle(el).display !== 'none',
      position: {
        x: Math.round(rect.left + window.scrollX),
        y: Math.round(rect.top + window.scrollY)
      },
      size: {
        width: Math.round(rect.width),
        height: Math.round(rect.height)
      }
    };
  }).filter(el => el.isVisible);


  // Structure data for AI model
  const pageState = {
    elements: interactableElements,
    userGoal: userGoal || 'Navigate or complete unspecified task',
  };

  return pageState;
}

// Enhanced command execution with AI response handling
async function executeAICommand(aiResponse) {
  try {
    const command = JSON.parse(aiResponse);
    
    switch (command.status.toLowerCase()) {
      case 'continue':
        if (command.command === 'click' && command.args.target_element) {
          const element = document.querySelector(command.args.target_element);
          if (element) {
            element.scrollIntoView({ behavior: 'smooth', block: 'center' });
            await sleep(300);
            element.click();
            return { success: true, action: 'click', selector: command.args.target_element };
          }
        } 
        else if (command.command === 'fill' && command.args.target_element) {
          const element = document.querySelector(command.args.target_element);
          if (element) {
            element.scrollIntoView({ behavior: 'smooth', block: 'center' });
            element.focus();
            element.value = command.args.fill_text;
            element.dispatchEvent(new Event('input', { bubbles: true }));
            element.dispatchEvent(new Event('change', { bubbles: true }));
            return { success: true, action: 'fill', selector: command.args.target_element };
          }
        }
        break;
        
      case 'user_needed':
        return { 
          success: true, 
          action: 'user_needed', 
          message: command.flavor 
        };
        
      case 'done':
        return { 
          success: true, 
          action: 'done', 
          message: command.flavor 
        };
    }
    
    return { success: false, error: 'Invalid command structure' };
  } catch (e) {
    console.error('Error executing AI command:', e);
    return { success: false, error: e.message };
  }
}

// Message handler for communication with popup/background
browser.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
  console.log("JARVIS received message:", message);
  
  try {
    switch (message.action) {
      case 'getPageState':
        try {
          const pageState = await getPageState(message.userGoal);
          return { success: true, pageState }; // This structure is crucial
      } catch (error) {
          return { success: false, error: error.message };
      }
        break;
        
      case 'executeAICommand':
        const result = await executeAICommand(message.aiResponse);
        sendResponse(result);
        break;
        
      case 'takeAction':
        // Direct action without AI (fallback)
        if (message.command === 'click' && message.selector) {
          const element = document.querySelector(message.selector);
          if (element) {
            element.click();
            sendResponse({ success: true });
          } else {
            sendResponse({ success: false, error: 'Element not found' });
          }
        }
        break;
        
      default:
        sendResponse({ success: false, error: 'Unknown action' });
    }
  } catch (error) {
    console.error("Error handling message:", error);
    sendResponse({ success: false, error: error.message });
  }
  
  return true; // Keep message channel open for async response
});
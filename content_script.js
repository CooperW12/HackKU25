//Listen for messages from popup
/*
console.log("Content script loaded!"); //Shows up in web console

browser.runtime.onMessage.addListener((message) => {
    if (message.action === "userPrompt") {
        console.log("Friendly Neighborhood User: ", message.prompt);
    }
    else if (message.action === "getPageHTML") { // NEW
        console.log("Sending page HTML to popup");
        return Promise.resolve(document.documentElement.outerHTML);
    }
    else if (message.action === "apiResponse") {
        console.log("A message from far, far away: ", message.data.status);
        //basically do something with the message we recieve from the heroku server
    }
    return Promise.resolve("Message received");
});
*/
console.log("Content script loaded!");
browser.runtime.onMessage.addListener((message) => {
    if (message.action === "userPrompt") {
        console.log("User prompt:", message.prompt);
    }
    else if (message.action === "getPageHTML") {
        console.log("Creating optimized HTML snapshot");
        
        // Clone the document to avoid modifying the live page
        const clonedDoc = document.cloneNode(true);
        
        // Remove elements we don't need
        const elementsToRemove = clonedDoc.querySelectorAll(
            'script, style, link, meta, noscript, svg, img, video, audio, iframe, canvas, path, g'
        );
        elementsToRemove.forEach(el => el.remove());
        
        // Get interactive elements and their context
        const interactiveElements = clonedDoc.querySelectorAll(
            'a, button, input, select, textarea, [role="button"], [role="link"], [tabindex], [onclick], [href]'
        );
        
        // Create a simplified container
        const simplifiedContainer = clonedDoc.createElement('div');
        
        // Add important structural elements and interactive elements
        interactiveElements.forEach(el => {
            // Include the element and 2 levels up of parent hierarchy for context
            const contextWrapper = clonedDoc.createElement('div');
            contextWrapper.innerHTML = el.outerHTML;
            simplifiedContainer.appendChild(contextWrapper);
            
            // Include labels for inputs
            if (el.tagName === 'INPUT' && el.id) {
                const label = clonedDoc.querySelector(`label[for="${el.id}"]`);
                if (label) {
                    simplifiedContainer.appendChild(label.cloneNode(true));
                }
            }
        });
        
        // Include page title and main landmarks
        if (clonedDoc.title) {
            const titleEl = clonedDoc.createElement('h1');
            titleEl.textContent = clonedDoc.title;
            simplifiedContainer.prepend(titleEl);
        }
        
        const mainContent = clonedDoc.querySelector('main, [role="main"], .main-content') || 
                            clonedDoc.querySelector('body');
        if (mainContent) {
            const mainClone = mainContent.cloneNode(true);
            // Clean up the main content clone
            ['script', 'style', 'link', 'img'].forEach(tag => {
                mainClone.querySelectorAll(tag).forEach(el => el.remove());
            });
            simplifiedContainer.appendChild(mainClone);
        }
        
        console.log("Optimized HTML size:", simplifiedContainer.outerHTML.length);
        return Promise.resolve(simplifiedContainer.outerHTML);
        
    }
    else if (message.action === "apiResponse") {
        console.log("AI response:", message.data);
        // Process the response as needed
    }
    return Promise.resolve("Message received");
});
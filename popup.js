document.getElementById('prompt-input').style.resize = 'vertical';

document.addEventListener('DOMContentLoaded', () => {
    const titleElement = document.getElementById('typing-title');
    const prompts = [
        "Jarvis, cancel my Amazon subscription.",
        "Jarvis, show me the Nasdaq.",
        "Jarvis, show me air fryer deals.",
        "Jarvis, take me to LeBron highlights!"
    ];
    let promptIndex = 0;
    let isTyping = true;
    let i = 0;
    const HEROKU_API = 'https://shrouded-waters-48660-941c6e92b405.herokuapp.com/ask';
    
    function typeWriter() {
        const currentPrompt = prompts[promptIndex];
        if (isTyping) {
            if (i < currentPrompt.length) {
                titleElement.innerHTML = currentPrompt.substring(0, i + 1);
                i++;
                setTimeout(typeWriter, 100);
            } else {
                isTyping = false;
                setTimeout(typeWriter, 2000);
            }
        } else {
            if (i > 7) {
                titleElement.innerHTML = currentPrompt.substring(0, i - 1);
                i--;
                setTimeout(typeWriter, 50);
            } else {
                isTyping = true;
                promptIndex = (promptIndex + 1) % prompts.length;
                setTimeout(typeWriter, 500);
            }
        }
    }
    
    setTimeout(typeWriter, 300);
    
    const input = document.getElementById('prompt-input');
    const button = document.getElementById('submit-btn');

    const showSubmitFeedback = () => {
        button.style.transform = 'scale(0.95)';
        button.style.backgroundColor = '#2a56c0';
        setTimeout(() => {
            button.style.transform = 'scale(1)';
            button.style.backgroundColor = '#4285f4';
        }, 200);
    };

    async function queryAI(pageState) {
        try {
            // Convert elements array to a string representation
            const elementsStr = Array.isArray(pageState.elements) 
                ? JSON.stringify(pageState.elements, null, 2)
                : String(pageState.elements);
            
            const aiPrompt = `You are Jarvis. Analyze this page state and user goal:
    Goal: ${pageState.userGoal}
    Interactable Elements: ${elementsStr}
    
    Respond with JSON following the exact schema provided.`;
            
            console.log("AI Prompt:", aiPrompt);
            
            // Get response from backend
            const aiResponse = await accessBackend(elementsStr, pageState.userGoal);
            
            // Ensure the response is properly stringified
            if (typeof aiResponse === 'object') {
                return JSON.stringify(aiResponse);
            }
            
            // If it's already a string, try to parse it to validate
            try {
                JSON.parse(aiResponse);
                return aiResponse;
            } catch {
                throw new Error("Invalid JSON response from API");
            }
            
        } catch (error) {
            console.error("Error in queryAI:", error);
            // Return a safe fallback response
            return JSON.stringify({
                status: "continue",
                command: "search",
                args: {
                    query: pageState.userGoal,
                },
                flavor: "Error processing AI response"
            });
        }
    }

    const handleSubmit = async () => {
        const prompt = input.value.trim();
        if (!prompt) return;
    
        showSubmitFeedback();
        console.log("Processing prompt:", prompt);
    
        try {
            const [tab] = await browser.tabs.query({ active: true, currentWindow: true });
            for (let i = 0; i < 5; i++){
                // Step 1: Get current page state from content script
                const response = await browser.tabs.sendMessage(tab.id, {
                    action: "getPageState",
                    userGoal: prompt
                });
                
                // Check if we got a valid response
                if (!response || !response.success) {
                    throw new Error("Failed to get page state from content script");
                }
                
                console.log("Received page state:", response.pageState);
        
                // Step 2: Send to AI and get response
            
                const aiResponse = await queryAI({
                    ...response.pageState,
                    userGoal: prompt // Ensure userGoal is included
                });

        
                
                console.log("AI Response:", aiResponse);
        
                // Step 3: Execute the AI's command
                const executionResult = await browser.tabs.sendMessage(tab.id, {
                    action: "executeAICommand",
                    aiResponse: aiResponse
                });
                
                // Handle the execution result
                if (!executionResult.success) {
                    //throw new Error(executionResult.error || "Command execution failed");
                    console.log("eror");
                }
        
                console.log("Execution result:", executionResult);
        
                // Handle different statuses
                if (executionResult.action === 'user_needed') {
                    alert(`Jarvis needs your help: ${executionResult.message}`);
                } else if (executionResult.action === 'done') {
                    alert(`Success: ${executionResult.message}`);
                }
        
                input.value = '';
            
            }
            } catch (error) {
                console.error("Error during automation:", error);
                alert(`Jarvis encountered an error: ${error.message}`);
                
                // Fallback: Open a new tab with Google search
                if (error.message.includes("No receiver") || error.message.includes("Could not establish connection")) {
                    browser.tabs.create({
                        url: `https://www.google.com/search?q=${encodeURIComponent(prompt)}`
                    });
                }
        
        }
    };

    const accessBackend = async (html, instruction) => {
        try {
            const response = await fetch(HEROKU_API, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    htmlCode: html,
                    instruction: instruction
                })
            });

            return await response.json();
        } catch (err) {
            console.error("API Fetch Error:", err);
            throw err;
        }
    };

    button.addEventListener('click', handleSubmit);

    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit();
            button.classList.add('keyboard-submit');
            setTimeout(() => button.classList.remove('keyboard-submit'), 300);
        }
    });

    // Focus input when popup opens
    input.focus();
});
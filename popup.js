document.getElementById('prompt-input').style.resize = 'vertical';

document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements
    const titleElement = document.getElementById('typing-title');
    const input = document.getElementById('prompt-input');
    const button = document.getElementById('submit-btn');
    const loadingIndicator = document.getElementById('loading-indicator');
    const flavorText = document.getElementById('flavor-text');
    const flavorContent = document.getElementById('flavor-content');
    const statusText = loadingIndicator.querySelector('.status-text');

    // Animation variables
    const prompts = [
        "Jarvis, cancel my Amazon subscription.",
        "Jarvis, show me the Nasdaq.",
        "Jarvis, show me air fryer deals.",
        "Jarvis, take me to LeBron highlights!"
    ];
    let promptIndex = 0;
    let isTyping = true;
    let i = 0;

    // API endpoint
    const HEROKU_API = 'https://shrouded-waters-48660-941c6e92b405.herokuapp.com/ask';
    
    // Typing animation for title
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
    
    // Start typing animation
    setTimeout(typeWriter, 300);

    // Button feedback animation
    const showSubmitFeedback = () => {
        button.style.transform = 'scale(0.95)';
        button.style.backgroundColor = '#2a56c0';
        setTimeout(() => {
            button.style.transform = 'scale(1)';
            button.style.backgroundColor = '#4285f4';
        }, 200);
    };

    // Query AI with proper error handling
    async function queryAI(pageState) {
        try {
            const elementsStr = Array.isArray(pageState.elements) 
                ? JSON.stringify(pageState.elements, null, 2)
                : String(pageState.elements);
            
            const aiPrompt = `You are Jarvis. Analyze this page state and user goal:
    Goal: ${pageState.userGoal}
    Interactable Elements: ${elementsStr}
    
    Respond with JSON following the exact schema provided.`;
            
            console.log("AI Prompt:", aiPrompt);
            
            const aiResponse = await accessBackend(elementsStr, pageState.userGoal);
            
            if (typeof aiResponse === 'object') {
                return JSON.stringify(aiResponse);
            }
            
            try {
                JSON.parse(aiResponse);
                return aiResponse;
            } catch {
                throw new Error("Invalid JSON response from API");
            }
            
        } catch (error) {
            console.error("Error in queryAI:", error);
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

    // Main submission handler with loading state
    const handleSubmit = async () => {
        const prompt = input.value.trim();
        if (!prompt || button.disabled) return;

        // Set loading state
        button.disabled = true;
        loadingIndicator.style.display = 'flex';
        flavorText.style.display = 'none';
        let timeoutSeconds = 0;
        const timeoutInterval = setInterval(() => {
            timeoutSeconds++;
            statusText.textContent = `Processing (${timeoutSeconds}s)...`;
        }, 1000);

        try {
            const [tab] = await browser.tabs.query({ active: true, currentWindow: true });
            
            for (let i = 0; i < 5; i++) {
                // Update status text
                statusText.textContent = `Step ${i+1}/5: Analyzing page...`;
                
                // Get page state
                const response = await browser.tabs.sendMessage(tab.id, {
                    action: "getPageState",
                    userGoal: prompt
                });
                
                if (!response?.success) {
                    throw new Error("Failed to get page state");
                }

                // Query AI
                statusText.textContent = `Step ${i+1}/5: Consulting AI...`;
                const aiResponse = await queryAI({
                    ...response.pageState,
                    userGoal: prompt
                });

                // Execute command
                statusText.textContent = `Step ${i+1}/5: Executing...`;
                const executionResult = await browser.tabs.sendMessage(tab.id, {
                    action: "executeAICommand",
                    aiResponse: aiResponse
                });

                // Update flavor text
                if (executionResult.message) {
                    flavorContent.textContent = executionResult.message;
                    flavorText.style.display = 'block';
                }

                if (executionResult.action === 'user_needed') {
                    break;
                }
            }
        } catch (error) {
            console.error("Error during automation:", error);
            flavorContent.textContent = `Error: ${error.message}`;
            flavorText.style.display = 'block';
            
            // Fallback: Open Google search if connection fails
            if (error.message.includes("No receiver") || error.message.includes("Could not establish connection")) {
                browser.tabs.create({
                    url: `https://www.google.com/search?q=${encodeURIComponent(prompt)}`
                });
            }
        } finally {
            // Clear loading state
            clearInterval(timeoutInterval);
            button.disabled = false;
            loadingIndicator.style.display = 'none';
            statusText.textContent = 'Processing...';
            input.value = '';
        }
    };

    // Backend API access
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

    // Event listeners
    button.addEventListener('click', handleSubmit);

    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            button.style.boxShadow = '0 0 0 3px rgba(66, 133, 244, 0.5)';
            setTimeout(() => {
                button.style.boxShadow = 'none';
            }, 300);
            handleSubmit();
        }
    });

    // Focus input when popup opens
    input.focus();
});
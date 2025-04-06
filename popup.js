
document.getElementById('prompt-input').style.resize = 'vertical';

document.addEventListener('DOMContentLoaded', () => {
    const titleElement = document.getElementById('typing-title');
    const input = document.getElementById('prompt-input');
    const button = document.getElementById('submit-btn');
    const loadingIndicator = document.getElementById('loading-indicator');
    
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

    const showSubmitFeedback = () => {
        button.style.transform = 'scale(0.95)';
        button.style.backgroundColor = '#2a56c0';
        setTimeout(() => {
            button.style.transform = 'scale(1)';
            button.style.backgroundColor = '#4285f4';
        }, 200);
    };

    const sendToBackend = async (html, instruction) => {
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

            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (err) {
            console.error("API Fetch Error:", err);
            throw err;
        }
    };

    const handleSubmit = async () => {
        const prompt = input.value.trim();
        if (prompt && !button.disabled) {
            // Set loading state
            button.disabled = true;
            loadingIndicator.style.display = 'flex';
            showSubmitFeedback();
            
            let timeoutSeconds = 0;
            const timeoutInterval = setInterval(() => {
                timeoutSeconds++;
                loadingIndicator.querySelector('span').textContent = 
                    `Processing your request... (${timeoutSeconds}s)`;
            }, 1000);

            try {
                // Get current tab's HTML
                const tabs = await browser.tabs.query({active: true, currentWindow: true});
                const html = await browser.tabs.sendMessage(tabs[0].id, {
                    action: "getPageHTML"
                });

                // Send to backend
                const apiData = await sendToBackend(html, prompt);
                
                // Send response to content script
                await browser.tabs.sendMessage(tabs[0].id, {
                    action: "apiResponse",
                    data: apiData
                });

                console.log("POPUP LOG:", {
                    userInput: prompt,
                    apiResponse: apiData
                });

            } catch (err) {
                console.error("Submission Error:", err);
                button.style.backgroundColor = '#ff4444';
                setTimeout(() => {
                    button.style.backgroundColor = '#4285f4';
                }, 1000);
            } finally { //other thing that MATTERS
                // Reset UI
                clearInterval(timeoutInterval);
                button.disabled = false;
                loadingIndicator.style.display = 'none';
                loadingIndicator.querySelector('span').textContent = 'Processing your request...';
                input.value = '';
            }
        }
    };

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
});


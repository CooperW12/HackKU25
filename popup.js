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

    const HEROKU_API = 'https://shrouded-waters-48660-941c6e92b405.herokuapp.com/';
    
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
    input.style.resize = 'vertical';

    const showSubmitFeedback = () => {
        button.style.transform = 'scale(0.95)';
        button.style.backgroundColor = '#2a56c0';
        setTimeout(() => {
            button.style.transform = 'scale(1)';
            button.style.backgroundColor = '#4285f4';
        }, 200);
    };

    const fetchFromHeroku = async (jsonData) => {
        try {
            const encodedData = encodeURIComponent(JSON.stringify(jsonData));
            const response = await fetch(`${HEROKU_API}ask/${encodedData}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (err) {
            console.error("API Fetch Error:", err);
            throw err;
        }
    };

    const handleSubmit = async () => {
        const prompt = input.value.trim();
        if (!prompt) return;

        showSubmitFeedback();
        
        try {
            const tabs = await chrome.tabs.query({active: true, currentWindow: true});
            
            // Get HTML and prompt from content script
            const jsonData = await chrome.tabs.sendMessage(tabs[0].id, {
                action: "userPrompt",
                prompt: prompt
            });
            
            // Send to Heroku
            const apiData = await fetchFromHeroku(jsonData);
            
            // Send response to content script
            await chrome.tabs.sendMessage(tabs[0].id, {
                action: "apiResponse",
                data: apiData
            });

            console.log("Full cycle complete:", apiData);

        } catch (err) {
            console.error("Submission Error:", err);
            button.style.backgroundColor = '#ff4444';
            setTimeout(() => {
                button.style.backgroundColor = '#4285f4';
            }, 1000);
        }
        
        input.value = '';
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
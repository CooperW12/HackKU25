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
    const prompts = [
        "Jarvis, cancel my Amazon subscription.",
        "Jarvis, show me the Nasdaq.",
        "Jarvis, show me air fryer deals.",
        "Jarvis, take me to LeBron highlights!"
    ];
    let promptIndex = 0;
    let isTyping = true;
    let i = 0;
    
     //Heroku API endpoint
    const HEROKU_API = 'https: //shrouded-waters-48660-941c6e92b405.herokuapp.com/';
    
    function typeWriter() {
        const currentPrompt = prompts[promptIndex];
         //Typing function to type and delete text above the prompt
        if (isTyping) {
            if (i < currentPrompt.length) {
                titleElement.innerHTML = currentPrompt.substring(0, i + 1);
                i++;
                setTimeout(typeWriter, 100);  //Type speed
            } else {
                 //Delete after pause
                isTyping = false;
                setTimeout(typeWriter, 2000);  //Pause at full message
            }
        } else {
             //deleting
            if (i > 7) {  //This keeps the 'Jarvis,' part of the statement
                titleElement.innerHTML = currentPrompt.substring(0, i - 1);
                i--;
                setTimeout(typeWriter, 50);  //Deleting speed (faster)
            } else {
                 //Next prompt
                isTyping = true;
                promptIndex = (promptIndex + 1) % prompts.length;
                setTimeout(typeWriter, 500);  //Pause before next prompt
            }
        }
    }
    
     //Starts animation
    setTimeout(typeWriter, 300);
    
     //Input handling schtuff :P
    const input = document.getElementById('prompt-input');
    const button = document.getElementById('submit-btn');
    input.style.resize = 'vertical';

     //Add visual feedback function
    const showSubmitFeedback = () => {
        button.style.transform = 'scale(0.95)';
        button.style.backgroundColor = '#2a56c0';
        setTimeout(() => {
            button.style.transform = 'scale(1)';
            button.style.backgroundColor = '#4285f4';
        }, 200);
    };

     //Scrapes webpage's HTML
    const getPageHTML = async () => {
        try {
            const tabs = await browser.tabs.query({active: true, currentWindow: true});
            const html = await browser.tabs.sendMessage(tabs[0].id, {
                action: "getPageHTML"
            });
            return html;
        } catch (err) {
            console.error("Failed to get page HTML:", err);
            return null;
        }
    };

     //Send data to Flask
    const sendToFlask = async (prompt, html) => {
        try {
            const response = await fetch(HEROKU_API, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    htmlCode: html,
                    instruction: prompt
                })
            });
            
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (err) {
            console.error("API Error:", err);
            throw err;
        }
    };

     //submission function
    const handleSubmit = async () => {
        const prompt = input.value.trim();
        if (prompt) {
            showSubmitFeedback(); //Visual feedback for user when attempting to submit prompt
            
            try {
                 //Get that scraped HTML we got earlier
                const pageHTML = await getPageHTML();
                
                 //Send to content script
                const tabs = await browser.tabs.query({active: true, currentWindow: true});
                await browser.tabs.sendMessage(tabs[0].id, {
                    action: "userPrompt",
                    prompt: prompt
                });

                 //Send to Flask
                const apiData = await sendToFlask(prompt, pageHTML);
                
                 //api response to console
                await browser.tabs.sendMessage(tabs[0].id, { //enables communication 
                    action: "apiResponse",
                    data: apiData
                });

                console.log("POPUP LOG:", {
                    userInput: prompt,
                    htmlSent: !!pageHTML,  //true if HTML was captured
                    apiResponse: apiData
                });

            } catch (err) {
                console.error("Submission Error:", err);
                 //error feedback
                button.style.backgroundColor = '#ff4444';
                setTimeout(() => {
                    button.style.backgroundColor = '#4285f4';
                }, 1000);
            }
            
            input.value = '';
        }
    };

    button.addEventListener('click', handleSubmit);

    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) { //that crisp enter to submit keyboard feedback
            e.preventDefault();
            button.style.boxShadow = '0 0 0 3px rgba(66, 133, 244, 0.5)';
            setTimeout(() => {
                button.style.boxShadow = 'none';
            }, 300);
            handleSubmit();
        }
    });
});
});
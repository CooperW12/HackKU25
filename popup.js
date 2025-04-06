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
    
    //Heroku API endpoint
    const HEROKU_BASE_URL = 'https://shrouded-waters-48660-941c6e92b405.herokuapp.com';
    
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
<<<<<<< HEAD
            // put all good code here
            //make json input obj
            json_obj = {}

            my_url = HEROKU_API + "/ask/" + json.stringify(json_obj);
            const response = await fetch(my_url);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
=======
            const tabs = await browser.tabs.query({active: true, currentWindow: true});
            if (!tabs[0]) throw new Error("No active tab found");
            
            const html = await browser.tabs.sendMessage(tabs[0].id, {
                action: "getPageHTML"
            });
            return html;
        } catch (err) {
            console.error("Failed to get page HTML:", err);
            titleElement.textContent = "Error: Couldn't access page content";
            titleElement.style.color = "#ff4444";
            setTimeout(() => {
                titleElement.style.color = "#4285f4";
            }, 3000);
            return null;
        }
    };

    //Send data to Flask
    const sendToFlask = async (prompt, html) => {
        console.log("sending request now...");
        try {
            //Create JSON with required structure
            const requestData = {
                htmlCode: html,
                instruction: prompt
            };
            
            //Encode for URL transmission
            const encodedData = encodeURIComponent(JSON.stringify(requestData));
            const request_url = `${HEROKU_BASE_URL}/ask/${encodedData}`;

            const response = await fetch(request_url, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error(`Server responded with ${response.status}`);
            }

>>>>>>> 15c8f942184ddb5c96ea29e1b26c291bcba0f0a8
            const data = await response.json();
            console.log("Heroku API Response:", data.response);
            return data;
        } catch (err) {
            console.error("API Fetch Error:", err);
            throw err;
        }
    };

    //submission function
    const handleSubmit = async () => {
        const prompt = input.value.trim();
        if (!prompt) return;

        showSubmitFeedback();
        const originalBtnText = button.textContent;
        button.disabled = true;
        button.textContent = "Processing...";

        try {
            const pageHTML = await getPageHTML();
            if (!pageHTML) return;
            
<<<<<<< HEAD
            try {
                //Send to content script
                const tabs = await browser.tabs.query({active: true, currentWindow: true});
                const htmlResponse = await browser.tabs.sendMessage(tabs[0].id, {
                    action: "userPrompt",
                    prompt: prompt
                });
                
                //the JSON object, we are so back
                const requestData = {
                    htmlCode: htmlResponse.htmlCode,
                    instructions: prompt
                };

                const encodedData = encodeURIComponent(JSON.stringify(requestData));
                const apiUrl = 
                //Fetch
                const apiData = await fetchFromHeroku();
                
                //api response to console
                await browser.tabs.sendMessage(tabs[0].id, {
                    action: "apiResponse",
                    data: apiData
                });

                console.log("POPUP LOG:", {
                    userInput: prompt,
                    apiResponse: apiData.response
                });

            } catch (err) {
                console.error("Submission Error:", err);
                //error feedback
                button.style.backgroundColor = '#ff4444';
                setTimeout(() => {
                    button.style.backgroundColor = '#4285f4';
                }, 1000);
            }
=======
            const apiData = await sendToFlask(prompt, pageHTML);
>>>>>>> 15c8f942184ddb5c96ea29e1b26c291bcba0f0a8
            
            const tabs = await browser.tabs.query({active: true, currentWindow: true});
            await browser.tabs.sendMessage(tabs[0].id, {
                action: "processResponse",
                prompt: prompt,
                html: pageHTML,
                apiData: apiData
            });

            console.log("POPUP LOG:", {
                userInput: prompt,
                htmlSent: !!pageHTML,
                apiResponse: apiData
            });

            titleElement.textContent = "Request completed successfully";
            titleElement.style.color = "#4CAF50";
            setTimeout(() => typeWriter(), 2000);

        } catch (err) {
            console.error("Submission Error:", err);
            button.style.backgroundColor = '#ff4444';
            titleElement.textContent = `Error: ${err.message}`;
            titleElement.style.color = "#ff4444";
            setTimeout(() => {
                button.style.backgroundColor = '#4285f4';
                typeWriter();
            }, 3000);
        } finally {
            input.value = '';
            button.disabled = false;
            button.textContent = originalBtnText;
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
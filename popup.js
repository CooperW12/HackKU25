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
    
    function typeWriter() {
        const currentPrompt = prompts[promptIndex];
        //Typing function to type and delete text above the prompt
        if (isTyping) {
            if (i < currentPrompt.length) {
                titleElement.innerHTML = currentPrompt.substring(0, i + 1);
                i++;
                setTimeout(typeWriter, 100); //Type speed
            } else {
                //Delete after pause
                isTyping = false;
                setTimeout(typeWriter, 2000); //Pause at full message
            }
        } else {
            //deleting
            if (i > 7) { //This keeps the 'Jarvis,' part of the statement
                titleElement.innerHTML = currentPrompt.substring(0, i - 1);
                i--;
                setTimeout(typeWriter, 50); //Deleting speed (faster)
            } else {
                //Next prompt
                isTyping = true;
                promptIndex = (promptIndex + 1) % prompts.length;
                setTimeout(typeWriter, 500); //Pause before next prompt
            }
        }
    }
    
    //Starts animation
    setTimeout(typeWriter, 300);
    
    //Input handling schtuff :P
    const input = document.getElementById('prompt-input');
    const button = document.getElementById('submit-btn');

    // Add visual feedback function
    const showSubmitFeedback = () => {
        button.style.transform = 'scale(0.95)';
        button.style.backgroundColor = '#2a56c0';
        setTimeout(() => {
            button.style.transform = 'scale(1)';
            button.style.backgroundColor = '#4285f4';
        }, 200);
    };

    // Shared submission function
    const handleSubmit = async () => {
        const prompt = input.value.trim();
        if (prompt) {
            showSubmitFeedback(); // Visual feedback
            
            console.log("POPUP LOG:", prompt);
            
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
            
            input.value = '';
        }
    };

    // Click handler
    button.addEventListener('click', handleSubmit);

    // Enter key handler
    input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit();
            
            // Extra visual feedback for keyboard users
            button.classList.add('keyboard-submit');
            setTimeout(() => button.classList.remove('keyboard-submit'), 300);
        }
    });
});
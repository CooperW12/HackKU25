let input = document.querySelector('input');

input.addEventListener('change', e => setValue(e.target.value));

async function setValue(value) {
    await browser.storage.local.set({ value });
}

async function init() {
    let result = await browser.storage.local.get('value'); // Fixed: Correct API usage
    let value = result.value || 0; // Default to 0 if undefined
    
    input.value = value;
    await setValue(value); // Optional: Persist default value
}

init().catch(e => console.error(e));

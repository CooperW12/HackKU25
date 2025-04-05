from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def read_file_skip_errors(file_path, encoding='utf-8'): #encoding errors from html >:(
    try:
        with open(file_path, 'r', encoding=encoding, errors='replace') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return ""
    except Exception as e:
         print(f"An error occurred: {e}")
         return ""

htmlCode = read_file_skip_errors("testweb.txt")

#htmlCode = "imagine this is a website with a basic login page and we want to view our messages on our account keep responding until status is DONE assume the user completes any actions at USER_NEEDED status"

client = OpenAI(api_key=os.environ['API_KEY'], base_url="https://api.deepseek.com")

systemPrompt = """
The user will provide you with html code of a webpage, instuctions on where they wish to go to.
You also need to determine the status of the webpage
The status can be one of three things:
"CONTINUE" - no need for user input to get where needed, look for the next selector needed to get to the goal
"USER_NEEDED" - the user is needed for something (i.e. username/password) 
"DONE" - the goal webpage has been reached

if the status is determined to be "CONTINUE", please find the html element to click on and output the css selector.
the example output for status "CONTINUE" would look like:
{
    "status": CONTINUE
    "target_element": [FILL HERE]
    "message": [5-8 word description of what you did] 
}

if the status is determined to be "USER_NEEDED", please prompt the user with what they need to do
the example output for status "USER_NEEDED" would look like:
{
    "status": USER_NEEDED
    "target_element": [FILL HERE]
    "message": [what the user needs to do (example: 'Please input your username.')]  
}

if the status is determined to be "DONE", please tell the user that you have arrived at the destination
the example output for status "DONE" would look like:
{
    "status": DONE
    "message": We have arrived at your destination.
}
"""

instruction = "i want to view my data structures class"

response = client.chat.completions.create(
    model = "deepseek-chat",
    messages = [
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": "INSTRUCTION: " + instruction + "CODE: " + htmlCode},
        ],
        stream = False
)

print(response.choices[0].message.content)
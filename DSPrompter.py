from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
from json import loads
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


class DSPrompter:

    def __init__(self):
        # initialize deepseek client and system prompt text
        DS_api_key = os.environ.get("API_KEY")
        if (not DS_api_key):
            raise ValueError("you have NO api key...")

        self.client = OpenAI(api_key=DS_api_key, base_url="https://api.deepseek.com")
        self.system_prompt = get_system_prompt()
        print(self.system_prompt)
        pass

    def get_json_response_from_dict_instruction(self, dict_input):
        htmlCode = dict_input["htmlCode"]
        instruction = dict_input["instruction"]

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": "INSTRUCTION: " + instruction + "CODE: " + htmlCode},
            ],
            stream=False,
            # force json response
            response_format={"type": "json_object"}
        )

        text_response = response.choices[0].message.content

        # parse directly
        response_dict = loads(text_response)
        return response_dict

def get_system_prompt():
    return \
"""
The user will provide you with html code of a webpage, instuctions on where they wish to go to.
You also need to determine the status of the webpage
The status can be one of three things:
"CONTINUE" - no need for user input to get where needed, look for the next selector needed to get to the goal
"USER_NEEDED" - the user is needed for something (i.e. username/password) 
"DONE" - the goal webpage has been reached

if the status is determined to be "CONTINUE", please find the html element to click on and output the css selector.
the example output for status "CONTINUE" would look like:

You MUST respond in valid JSON format only, using this exact structure:

{
    "status": "CONTINUE|USER_NEEDED|DONE",
    "target_element": "CSS_SELECTOR_OR_NULL",
    "message": "4 to 6 word description of action"
}

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

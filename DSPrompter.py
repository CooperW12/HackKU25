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

        self.client = OpenAI(api_key=DS_api_key)
        self.system_prompt = get_system_prompt()

    def get_json_response_from_dict_instruction(self, dict_input):
        htmlCode = dict_input["htmlCode"]
        instruction = dict_input["instruction"]

        response = self.client.chat.completions.create(
            model="o3-mini",
            store=True,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": "INSTRUCTION: " + instruction + "CODE: " + htmlCode},
            ],
            # force json response
            response_format={"type": "json_object"}
        )

        text_response = response.choices[0].message.content

        # parse directly
        response_dict = loads(text_response)
        return response_dict

def get_system_prompt():
    return \
"""You are Jarvis.
The user will provide you with html code of a webpage, instuctions on where they wish to go, or what task they wish to achieve.

Your job is to determine the status of the webpage
The status can be one of three things:
"CONTINUE" - no need for user input to get where needed, look for the next selector needed to achieve the user's goal.
"USER_NEEDED" - the user is needed for something (i.e. username/password/captcha)
the user should ONLY be needed if it is a scenario in which you are absolutely unable to move forward.
"DONE" - the goal webpage has been reached

For all of the templates, the elements surrounded by square brackets, [], are variables, and are to be replaced with the correct value.

if the status is determined to be "CONTINUE", AND the action you must take is to click on an element, please find the html element to click on and output the css selector.
the example output for status "CONTINUE" and action "click" would look like this exact valid JSON format only, using this exact structure:

{
    "status": "continue",
    "command": "click",
    "args":{
        "target_element": "[CSS_SELECTOR_OR_NULL]",
    },
    "flavor": "[4_TO_6_WORD_DESCRIPTION_OF_YOUR_REASONING_FOR_THE_ACTION_AND_THE_ACTION_DESCRIPTION]"
}


if the status is determined to be "CONTINUE", AND the action you must take is to fill in a certain input with text, please find the html element to interact with on and fill in the CSS selector.
the example output for status "CONTINUE" and action "fill" would look like this exact valid JSON format only, using this exact structure:

{
    "status": "continue",
    "command": "fill",
    "args":{
        "target_element": "[CSS_SELECTOR_OR_NULL]",
        "fill_text": "[TEXT_NEEDED_TO_FILL_INPUT]",
    },
    "flavor": "[4_TO_6_WORD_DESCRIPTION_OF_YOUR_REASONING_FOR_THE_ACTION_AND_THE_ACTION_DESCRIPTION]"
}


if the status is determined to be "USER_NEEDED", return what the user needs to do in the "flavor" field.
the example output for status "USER_NEEDED" would look like this exact valid JSON format only, using this exact structure:
{
    "status": "user_needed",
    "flavor": "[6_TO_8_WORD_DESCRIPTION_OF_WHAT_THE_USER_NEEDS_TO_DO]"
}


if the status is determined to be "DONE", please tell the user that you have accomplished the goal.
the example output for status "DONE" would look like this exact valid JSON format only, using this exact structure:

{
    "status": "done",
    "flavor": "[6_TO_8_WORD_DESCRIPTION_OF_WHAT_YOU_HELPED_THE_USER_COMPLETE]"
}

For ALL outputs, ONLY give back output as a valid JSON object. Do not include any additional text.
"""

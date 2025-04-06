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
        self.system_prompt = read_file_skip_errors("system_prompt.txt")
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

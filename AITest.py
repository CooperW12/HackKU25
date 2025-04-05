from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def read_file_skip_errors(file_path, encoding='utf-8'):
    """
    Reads a file and skips character encoding errors.

    Args:
        file_path (str): The path to the file.
        encoding (str, optional): The encoding to use. Defaults to 'utf-8'.

    Returns:
        str: The content of the file with undecodable characters replaced.
             Returns an empty string if the file cannot be opened.
    """
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

client = OpenAI(api_key=os.environ['API_KEY'], base_url="https://api.deepseek.com")

systemPrompt = """
The user will provide you with html code of a webpage and instuctions on where they wish to go to.

Please find the html element they need to click on and ONLY output the css selector.

EXAMPLE JSON OUTPUT:
{
    "target_element": [FILL HERE]
}
"""

instruction = "i want to view my emails"

response = client.chat.completions.create(
    model = "deepseek-chat",
    messages = [
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": "INSTRUCTION: " + instruction + "CODE: " + htmlCode},
        ],
        stream = False
)


print(response.choices[0].message.content)
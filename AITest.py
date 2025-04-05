from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

file = open("testweb.txt", "r")
htmlCode = file.read()

client = OpenAI(api_key=os.environ['API_KEY'], base_url="https://api.deepseek.com")

systemPrompt = """
The user will provide you with html code of a webpage and instuctions on where they wish to go to.

Please find the html element they need to click on and ONLY output the css selector.

EXAMPLE JSON OUTPUT:
{
    "target_element": [FILL HERE]
}
"""

instruction = "I want to look at my data structures and algorithms class"

response = client.chat.completions.create(
    model = "deepseek-chat",
    messages = [
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": "INSTRUCTION: " + instruction + "CODE: " + htmlCode},
        ],
        stream = False
)


print(response.choices[0].message.content)
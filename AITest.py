from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

client = OpenAI(api_key=os.environ['API_KEY'], base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model = "deepseek-chat",
    messages = [
        {"role": "system", "content": "you are helpful assistant"},
        {"role": "user", "content": "Hello"},
        ],
        stream = False
)


print(response.choices[0].message.content)
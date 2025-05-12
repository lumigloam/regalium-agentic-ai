import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_user(message):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}]
    )
    return completion.choices[0].message.content

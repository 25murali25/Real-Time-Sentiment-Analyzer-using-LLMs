from groq import Groq
from dotenv import load_dotenv
from Prompt import prompt
import os

load_dotenv()


api_key = os.getenv("GROQ_API_KEY")


client = Groq(api_key=api_key_used)


def chatbot(message):
    completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "user",
        "content": message
      },
      {
        "role":"user",
        "content":prompt
      }
    ],
    temperature=1,
    max_completion_tokens=8192
)

    return completion.choices[0].message.content

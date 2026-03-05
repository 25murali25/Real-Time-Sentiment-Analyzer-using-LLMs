from groq import Groq
from env import api_key_used
from Prompt import prompt

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

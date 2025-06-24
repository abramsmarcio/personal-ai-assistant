from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env")

client = Groq(api_key=API_KEY)

def get_response(conversation_history):
    response_stream = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=conversation_history,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
    )

    full_reply = ""
    for chunk in response_stream:
        content = chunk.choices[0].delta.content or ""
        full_reply += content
        yield content  

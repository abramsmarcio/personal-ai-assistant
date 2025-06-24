from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env")

client = Groq(api_key=API_KEY)

def get_response(conversation_history):
    system_prompt = {
        "role": "system",
        "content":  """You are Marcio's highly capable personal assistant. 
            Help him organize his tasks, manage learning goals, assist with coding, 
            summarize documents, and answer queries concisely and smartly. 
            Always remember his priorities: productivity, learning, and clarity."""
    }
    response_stream = client.chat.completions.create(
        model = "gemma2-9b-it",
        messages = [system_prompt] + conversation_history,
        temperature = 1,
        max_tokens = 1024,
        top_p = 1,
        stream = True,
    )

    full_reply = ""
    for chunk in response_stream:
        content = chunk.choices[0].delta.content or ""
        full_reply += content
        yield content  

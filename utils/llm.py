import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("❌ Missing OPENROUTER_API_KEY (or OPENAI_API_KEY) in .env file")

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def chat_with_openrouter(messages, model="deepseek/deepseek-chat-v3.1:free",
                         temperature=0.7, top_p=1, max_tokens=500, stream=False):
    """
    Call OpenRouter API with optional streaming.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "HTTP-Referer": "http://localhost:8501",  # optional
        "X-Title": "ChatGPT Clone App"
    }

    data = {
        "model": model,
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "messages": messages,
        "stream": stream
    }

    response = requests.post(BASE_URL, headers=headers, json=data, stream=stream)

    if response.status_code != 200:
        raise RuntimeError(f"❌ OpenRouter API error: {response.text}")

    if stream:
        for line in response.iter_lines():
            if line and line.startswith(b"data: "):
                payload = line[len(b"data: "):].decode("utf-8").strip()
                if payload == "[DONE]":
                    break
                try:
                    data = json.loads(payload)
                    delta = data["choices"][0]["delta"]
                    if "content" in delta:
                        yield delta["content"]
                except Exception:
                    continue
    else:
        return response.json()["choices"][0]["message"]["content"]

from config import OPENROUTER_API_KEY
import requests

def chat_with_openrouter(prompt):
    if not OPENROUTER_API_KEY:
        return "API key OpenRouter belum disetel."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://discord.com",
        "X-Title": "MyDiscordBot"
    }
    data = {
        "model": "deepseek-ai/deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content'].strip()
        return f"Gagal: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

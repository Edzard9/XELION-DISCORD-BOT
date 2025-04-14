import requests

def get_meme():
    try:
        response = requests.get('https://meme-api.com/gimme', timeout=10)
        data = response.json()
        if 'url' in data:
            return data['url']
        return "Gagal mengambil meme."
    except Exception as e:
        return f"Gagal ambil meme: {e}"

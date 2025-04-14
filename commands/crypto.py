import requests

def get_crypto_price(symbol):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
        response = requests.get(url, timeout=10).json()
        if symbol in response:
            return f"Harga **{symbol.capitalize()}** saat ini: ${response[symbol]['usd']}"
        return "Koin tidak ditemukan."
    except Exception as e:
        return f"Gagal mengambil data crypto: {e}"

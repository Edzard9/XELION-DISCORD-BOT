import requests
from config import CURRENCYFREAKS_API_KEY

def convert_currency(amount, from_currency, to_currency):
    try:
        url = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={CURRENCYFREAKS_API_KEY}&symbols={to_currency.upper()}&base={from_currency.upper()}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if "rates" in data and to_currency.upper() in data["rates"]:
            rate = float(data["rates"][to_currency.upper()])
            converted = amount * rate
            return f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"
        else:
            return f"Gagal konversi. Pastikan kode mata uang benar."
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

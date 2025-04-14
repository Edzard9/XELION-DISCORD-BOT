import requests
from bs4 import BeautifulSoup

def cari_kbbi(kata):
    try:
        url = f"https://kbbi.kemdikbud.go.id/entri/{kata}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        hasil = soup.find('div', {'class': 'container body-content'})
        makna = hasil.find_all('ol')
        if makna:
            return '\n'.join([m.text for m in makna])
        else:
            return "❌ Kata tidak ditemukan di KBBI."
    except:
        return "⚠️ Terjadi kesalahan saat mencari kata di KBBI."

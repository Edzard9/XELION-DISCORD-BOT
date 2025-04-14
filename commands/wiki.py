import wikipedia

wikipedia.set_lang("id")

def wiki_search(query):
    try:
        hasil = wikipedia.summary(query, sentences=2)
        return f"📚 **{query}**\n{hasil}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Kata tersebut ambigu. Coba lebih spesifik. Contoh:\n{', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return "Topik tidak ditemukan di Wikipedia."
    except:
        return "Terjadi kesalahan saat mencari Wikipedia."

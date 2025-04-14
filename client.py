import discord

from commands.meme import get_meme
from commands.ai import chat_with_openrouter
from commands.kbbi import cari_kbbi
from commands.wiki import wiki_search
from commands.currency import convert_currency
from commands.crypto import get_crypto_price
from commands.translate import translate_text
from commands.quote import get_random_quote
from commands.funfact import get_fun_fact
from commands.help import help_message
from commands.quiz import get_quiz_question, current_quiz, check_answer
from commands.slot import play_slot_machine
from commands.wyr import get_would_you_rather


import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Bot siap! Login sebagai {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        original_content = message.content
        content = original_content.lower()
        user_id = message.author.id

        if content.startswith('$meme'):
            await message.channel.send(get_meme())

        elif content.startswith('$ask'):
            prompt = original_content[len('$ask '):].strip()
            if prompt == "":
                await message.channel.send("Tolong masukkan pertanyaan.")
                return
            await message.channel.send("Sebentar ya... 🤖")
            await message.channel.send(chat_with_openrouter(prompt))

        elif content.startswith('$kbbi'):
            kata = original_content[len('$kbbi '):].strip()
            await message.channel.send(cari_kbbi(kata))

        elif content.startswith('$wiki'):
            query = original_content[len('$wiki '):].strip()
            hasil = wiki_search(query)
            await message.channel.send(hasil)

        elif content.startswith('$remindme'):
            try:
                parts = original_content.split(' ', 2)
                waktu = int(parts[1][:-1])
                satuan = parts[1][-1]
                pesan = parts[2]
                detik = waktu * 60 if satuan == 'm' else waktu
                await message.channel.send(f"⏰ Reminder disetel dalam {waktu}{satuan}")
                await asyncio.sleep(detik)
                await message.channel.send(f"🔔 Waktunya {message.author.mention}! Pesan: {pesan}")
            except:
                await message.channel.send("Format salah! Contoh: `$remindme 10m minum air!`")

        elif content.startswith('$timer'):
            try:
                durasi = int(original_content.split()[1])
                await message.channel.send(f"⏳ Timer selama {durasi} detik...")
                await asyncio.sleep(durasi)
                await message.channel.send(f"⏰ Timer selesai {message.author.mention}!")
            except:
                await message.channel.send("Contoh: `$timer 10`")

        elif content.startswith('$poll'):
            pertanyaan = original_content[len('$poll '):].strip()
            msg = await message.channel.send(f"\U0001F4CA **Polling**: {pertanyaan}\n👍 = Ya\n👎 = Tidak")
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")

        elif content.startswith('$convert'):
            try:
                _, amount, from_cur, to_cur = original_content.split()
                hasil = convert_currency(float(amount), from_cur.upper(), to_cur.upper())
                await message.channel.send(hasil)
            except:
                await message.channel.send("Format salah! Contoh: `$convert 100 USD IDR`")

        elif content.startswith('$crypto'):
            symbol = original_content[len('$crypto '):].strip().lower()
            await message.channel.send(get_crypto_price(symbol))

        elif content.startswith('$translate'):
            try:
                text = original_content[len('$translate '):]
                translated = translate_text(text, 'id')
                await message.channel.send(translated)
            except:
                await message.channel.send("Gagal menerjemahkan. Format: `$translate hello`")

        elif content.startswith('$quote'):
            await message.channel.send(get_random_quote())

        elif content.startswith('$funfact'):
            await message.channel.send(get_fun_fact())

        elif content.startswith('$help'):
            await message.channel.send(help_message())

        elif content.startswith('$slot'):
            result, win = play_slot_machine()
            hasil = ' | '.join(result)
            if win:
                await message.channel.send(f"{hasil}\n🎉 Menang!")
            else:
                await message.channel.send(f"{hasil}\n😢 Coba lagi!")

        elif content.startswith('$quiz'):
            soal = get_quiz_question(user_id)
            await message.channel.send(f"🧠 Kuis: {soal['pertanyaan']}")

        elif user_id in current_quiz:
            benar, jawaban = check_answer(user_id, original_content.strip().lower())
            if benar:
                await message.channel.send("✅ Benar!")
            else:
                await message.channel.send(f"❌ Salah! Jawaban yang benar adalah: **{jawaban}**")

        elif content.startswith('$wyr'):
            pertanyaan = get_would_you_rather()
            await message.channel.send(f"❓ Would You Rather:\n**{pertanyaan}**")

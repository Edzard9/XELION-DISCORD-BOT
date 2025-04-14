import asyncio

async def set_reminder(message, waktu, satuan, pesan):
    detik = waktu * 60 if satuan == 'm' else waktu
    await message.channel.send(f"⏰ Reminder disetel dalam {waktu}{satuan}")
    await asyncio.sleep(detik)
    await message.channel.send(f"🔔 Waktunya {message.author.mention}! Pesan: {pesan}")

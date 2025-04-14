import asyncio

async def start_timer(message, durasi):
    await message.channel.send(f"⏳ Timer selama {durasi} detik...")
    await asyncio.sleep(durasi)
    await message.channel.send(f"⏰ Timer selesai {message.author.mention}!")

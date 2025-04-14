async def create_poll(message, pertanyaan):
    msg = await message.channel.send(f"\U0001F4CA **Polling**: {pertanyaan}\n👍 = Ya\n👎 = Tidak")
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")

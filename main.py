from client import MyClient
import discord

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("YOUR-BOT-TOKEN")  # token bot discord

import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#client.run('OTQyMTY2MzgxNDM1MTc5MDg5.Yggi0Q.vHCKwDkcniBuC3xYi7T6QUbebSQ')
client.run(TOKEN)
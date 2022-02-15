import os
import discord
import string

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n')
    
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    guild = discord.utils.get(client.guild, name=GUILD)
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to {guild.name} and dont forget, All Hail Almighty Sineth')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    temp_message = message.content
    if "sineth" in temp_message.lower() :
        await message.channel.send('All Hail Sineth The Great!')

client.run(TOKEN)


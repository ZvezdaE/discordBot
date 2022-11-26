import os
import discord
import string
from discord.ext import commands
import tile_generation

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', case_insensitive = True)

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)

class main_game():
    def __init__(self):
        self.game_dict = {}

    def add_user(self, user_Id):
        if user_Id in self.game_dict:
            self.game_dict[user_Id].new_map()
        else:
            self.game_dict[user_Id] = tile_generation.character()

    def char_move(self, user_id, user_name, dir):
        if user_id in self.game_dict:
            return user_name + ", " + self.game_dict[user_id].move(dir)
        else:
            return "\n> Use !start to start a new map"
    
    def desc(self, user_id):
        return self.game_dict[user_id].loc_desc()
    
    def check_user(self, user_id):
        return user_id in self.game_dict
        

this_game = main_game()

@bot.command(name="Baby")
async def baby(ctx):
    await ctx.reply("> Play that funky music white boy!")
    
@bot.command(name='n', help="Move North")
async def move_N(ctx):
    __id = ctx.message.author.id
    __name = ctx.message.author.name
    await ctx.reply(this_game.char_move(__id, __name, "N"))

@bot.command(name="s", help="Move South")
async def move_S(ctx):
    __id = ctx.message.author.id
    __name = ctx.message.author.name
    await ctx.reply(this_game.char_move(__id, __name, "S"))

@bot.command(name="e", help="Move East")
async def move_E(ctx):
    __id = ctx.message.author.id
    __name = ctx.message.author.name
    await ctx.reply(this_game.char_move(__id, __name, "E"))

@bot.command(name="w", help="Move West")
async def move_W(ctx):
    __id = ctx.message.author.id
    __name = ctx.message.author.name
    await ctx.reply(this_game.char_move(__id, __name, "W"))

@bot.command(name='start', help="Start a new map")
async def start(ctx):
    __id = ctx.message.author.id
    __name = ctx.message.author.name
    this_game.add_user(__id)
    await ctx.reply("\n> **" + __name + "**\n" + this_game.desc(__id))

@bot.command(name="go")
async def go(ctx, dir = ""):
    __id = ctx.message.author.id
    __name = ctx.message.author.name
    if not this_game.check_user(__id):
        desc_text = "\n> Use !start to start a new map"
    else:
        dir = dir.lower()
        if dir == "n" or dir == "north":
            desc_text = this_game.char_move(__id, __name, "N")
        elif dir == "s" or dir == "south":
            desc_text = this_game.char_move(__id, __name, "S")
        elif dir == "e" or dir == "east":
            desc_text = this_game.char_move(__id, __name, "E")
        elif dir == "w" or dir == "west":
            desc_text = this_game.char_move(__id, __name, "W")
        else:
            desc_text = "\n> **" + __name + "**\nYou need to supply a direction, the following can be used:\n n or north \n s or south \n e or east \n w or west"

    await ctx.reply(desc_text)
    
"""
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
"""

bot.run(TOKEN)


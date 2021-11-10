"""WARNING:
    This file is not made for main build. This file is used for debugging purposes.
    Please use the bot.py file instead of this. 
    Do note this code is not commented or sorted out in any form."""
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from discord_slash import SlashCommand, SlashContext
import asyncio
import logging

print("WARNING:")
print("You are using the devolopment version of the bot.")
print("We do not suggest this, if you would like to use this in production")
print("please use the file named \"bot.py\"")

logging.basicConfig (level=logging.INFO)

load_dotenv()

token = os.environ["TOKEN"]
prefix = os.environ["PREFIX"]
member = os.environ["MEMBER_ID"]
mod = os.environ["MOD"]
admin = os.environ["ADMIN"]
guild = os.environ["GUILD"]

client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)

@client.event
async def on_connect():
    print("Connected to discord.")

@client.event
async def on_ready():
    print("Bot started")
    await asyncio.sleep(5)
    print("Moderator:" + mod)
    print("Admin:" + admin)
    print("Member:" + member)
    print("Guild:" + guild)


#client.load_extension("cogs.moderation")
#client.load_extension("cogs.fun")
#client.load_extension("cogs.info")
#client.load_extension("cogs.giveaway")

client.run(token)
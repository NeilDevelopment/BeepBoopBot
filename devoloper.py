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

logging.basicConfig (level=logging.DEBUG)

load_dotenv()

token = os.environ.get('token')
prefix = "!"

client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)

@client.event
async def on_connect():
	print("Connected to discord.")

@client.event
async def on_ready():
    print("Started")

#client.load_extension("cogs.moderation")
#client.load_extension("cogs.fun")
#client.load_extension("cogs.info")
#client.load_extension("cogs.giveaway")

dev_mod = os.getenv("MODERATOR_ROLE")
dev_admin = os.getenv("ADMIN_ROLE")
dev_member = os.getenv("MEMBER_ROLE")
dev_guild = os.getenv("GUILD_ID")
asyncio.sleep(10)
print("")
print("")
print("")
print("")
print("Moderator:" + dev_mod)
print("Admin:" + dev_admin)
print("Member:" + dev_member)
print("Guild:" + dev_guild)

client.run(token)
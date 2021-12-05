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

#logging.basicConfig (level=logging.INFO)

load_dotenv()

# Load everything from my system variables(Set on my pc, won't work for you.)
token = os.environ["TOKEN"]
prefix = os.environ["PREFIX"]
member = os.environ["MEMBER_ID"]
mod = os.environ["MOD"]
admin = os.environ["ADMIN"]
guild = os.environ["GUILD"]
logs = os.environ["LOG_CHANNEL"]

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
    print("Log Channel:" + logs)


@client.command()
async def reload(ctx, *, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send("Reloaded " + extension)

@client.command()
async def load(ctx, *, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send("Loaded " + extension)

@client.command()
async def unload(ctx, *, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send("Unloaded " + extension)


#client.load_extension("cogs.moderation")
#client.load_extension("cogs.fun")
#client.load_extension("cogs.info")
#client.load_extension("cogs.giveaway")
#client.load_extension("cogs.logs")

client.run(token)
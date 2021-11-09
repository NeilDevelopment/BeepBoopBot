import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from discord_slash import SlashCommand, SlashContext
import asyncio

print("--------------------------")
print("Beep Boop Bot is starting.")
print("--------------------------")
print("Loading ENV file.")

# This loads the ENV configuration file.
load_dotenv()
# Loads the token from the ENV file.
token = os.getenv("TOKEN")
# Loads the prefix from the ENV file.
prefix = os.getenv("PREFIX")
# Loads the Member role ID from the ENV file.
member = os.getenv("MEMBER_ROLE")
# Loads the Admin role ID from the ENV file.
moderator = os.getenv("MODERATOR_ROLE")
print("Loaded ENV file.")

client = commands.Bot(command_prefix=prefix)
# Removes the default help command.
client.remove_command('help')
# Main slash commands setup.
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)

@client.event
async def on_connect():
	print("Connected to discord.")

@client.event
async def on_ready():
	print("-----------------------")
	print("Beep Boop Bot is ready.")
	print("-----------------------")

print("Loading cogs")
for filename in os.listdir('./cogs'):
	if filename.endswith(".py"):
		client.load_extension(f'cogs.{filename[:-3]}')
		print(f"\"{filename[:-3]}\" cog has been loaded.")

""" evoloper stuff
Everything here is for devolopment and testing."""

"""
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
"""
client.run(token)
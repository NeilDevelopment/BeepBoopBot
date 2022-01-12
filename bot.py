import os
print("Checking your dependencies...")
os.system("python3 dependencie_checker.py")
print("All dependencie are installed.")

import discord
from discord.ext import commands
from discord.commands import slash_command
from dotenv import load_dotenv
import asyncio
import sys
import subprocess
import logging

logging.basicConfig (level=logging.INFO)


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
log_channel = os.getenv("LOG_CHANNEL")
print("Loaded ENV file.")

client = commands.Bot(command_prefix=prefix)
# Removes the default help command.
client.remove_command('help')
# Main slash commands setup.

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
client.run(token)
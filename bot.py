from colorama import Fore, Back, Style
import pyfiglet
import os
import platform

print(Fore.YELLOW + "Checking your dependencies...")
operatingsystem = platform.system()
if operatingsystem != "Windows":
	os.system("python3 dependencie_checker.py")
else:
	os.system("python dependencie_checker.py")
print(Fore.GREEN + "All dependencie are installed.")

ascii_text = pyfiglet.figlet_format("BeepBoopBot")
print(Fore.CYAN + ascii_text)

import discord
from discord.ext import commands
from discord.ext.commands.bot import when_mentioned
from dotenv import load_dotenv
import asyncio
import sys
import subprocess
import logging
from discord.commands import \
    slash_command

# Developer logging
#logging.basicConfig (level=logging.INFO)


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

client = commands.Bot(command_prefix=prefix)
# Removes the default help command.
client.remove_command("help")

@client.event
async def on_ready():
	# print("")
	# print(Fore.GREEN + "BeepBoopBot has started!")
	# print("")
	pass

for filename in os.listdir('./cogs'):
	if filename.endswith(".py"):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)
"""Loader"""
from click import command
from colorama import Fore, Style
import pyfiglet, asyncio, time, platform

ascii_text = pyfiglet.figlet_format("BeepBoopBot V2")
print(Fore.CYAN + ascii_text)
time.sleep(3)
"""[Disabled] Dependencie checker"""
# print(Fore.YELLOW + "Checking your dependencies...")
# operatingsystem = platform.system()
# if operatingsystem != "Windows":
# 	os.system("python3 dependencie_checker.py")
# else:
# 	os.system("python dependencie_checker.py")
# print(Fore.GREEN + "All dependencie are installed.")

import discord, os
from discord.commands import \
    slash_command
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("TOKEN")
guild_id = os.getenv("GUILD_ID")

client = commands.Bot(command_prefix=None, help_command=None)

@client.event
async def on_ready():
    print(Fore.GREEN + "[SUCCESS] " + Fore.LIGHTGREEN_EX + f"Connected to Discord as \"{client.user}\"")

for filename in os.listdir('./commands'):
    if filename.endswith(".py"):
        client.load_extension(f'commands.{filename[:-3]}')
        print(Fore.BLUE + "[INFO] " + Fore.MAGENTA + "(COMMANDS) " + Fore.WHITE + f"Loaded \"{filename[:-3]}\" command")

@client.event
async def on_application_command_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        em = discord.Embed(title="No permission :x:", description="You don't have enough permission(s) to execute that command!", color=discord.Color.red())
        await ctx.respond(embed=em)

print(Fore.BLUE + "[INFO] " + Fore.CYAN + "Connecting to Discord API...")
client.run(token)
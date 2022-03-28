"""Loader"""
from click import command
from colorama import Fore, Style
import pyfiglet, time, platform, subprocess, sys

ascii_text = pyfiglet.figlet_format("BeepBoopBot V2")
print(Fore.CYAN + ascii_text)
time.sleep(3)
"""Dependencie checker"""
operatingsystem = platform.system()

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
if 'py-cord' not in installed_packages:
    if operatingsystem != "Windows:":
        print(Fore.RED + "Module \"py-cord\" is missing! Install it by doing pip install py-cord==2.0.0b1\n" + Fore.BLUE + "Please make sure to have the " + Fore.GREEN + "\"==2.0.0\"" + Fore.BLUE + " or it won't work!") 
        exit()
    else:
        print(Fore.RED + "Module \"py-cord\" is missing! Install it by doing pip3 install py-cord==2.0.0b1") 
        exit()
else:
    pass
if "python-dotenv" not in installed_packages:
    if operatingsystem != "Windows:":
        print(Fore.RED + "Module \"python-dotenv\" is missing! Install it by doing pip install python-dotenv") 
        exit()
    else:
        print(Fore.RED + "Module \"python-dotenv\" is missing! Install it by doing pip3 install python-dotenv") 
        exit()
else:
    pass
if "asyncio" not in installed_packages:
    if operatingsystem != "Windows:":
        print(Fore.RED + "Module \"asyncio\" is missing! Install it by doing pip install asyncio") 
        exit()
    else:
        print(Fore.RED + "Module \"asyncio\" is missing! Install it by doing pip3 install asyncio") 
        exit()
else:
    pass
if "DateTime" not in installed_packages:
    if operatingsystem != "Windows:":
        print(Fore.RED + "Module \"datetime\" is missing! Install it by doing pip install datetime") 
        exit()
    else:
        print(Fore.RED + "Module \"datetime\" is missing! Install it by doing pip3 install datetime") 
        exit()
else:
    pass
print(Fore.BLUE + "[INFO] " + Fore.CYAN + "Connecting to Discord API...")
import discord, os
from discord.commands import \
    slash_command
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
guild_id = os.getenv("GUILD_ID")
dev_mode = os.getenv("DEV_MODE")

client = commands.Bot(help_command=None)

@client.event
async def on_ready():
    print(Fore.GREEN + "[SUCCESS] " + Fore.LIGHTGREEN_EX + f"Connected to Discord as \"{client.user}\"")

for filename in os.listdir('./commands'):
    if filename.endswith(".py"):
        client.load_extension(f'commands.{filename[:-3]}')
        print(Fore.BLUE + "[INFO] " + Fore.MAGENTA + "(COMMANDS) " + Fore.WHITE + f"Loaded \"{filename[:-3]}\" command")

for filename in os.listdir('./events'):
    if filename.endswith(".py"):
        client.load_extension(f'events.{filename[:-3]}')
        print(Fore.BLUE + "[INFO] " + Fore.MAGENTA + "(EVENTS) " + Fore.WHITE + f"Loaded \"on_{filename[:-3]}\" event")

if dev_mode == "YES":
    for filename in os.listdir('./developer'):
        if filename.endswith(".py"):
            client.load_extension(f'developer.{filename[:-3]}')
            print(Fore.BLUE + "[INFO] " + Fore.MAGENTA + "(DEVELOPER) " + Fore.WHITE + f"Loaded \"{filename[:-3]}\" cog")
else:
    pass

@client.event
async def on_application_command_error(ctx, error):
    if isinstance(error,commands.CheckFailure):
        em = discord.Embed(title="No permission :x:", description="You don't have enough permission(s) to execute that command!", color=discord.Color.red())
        await ctx.respond(embed=em)

client.run(token)
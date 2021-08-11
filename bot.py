import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 

print("------------------------------")
print("Ultimate Core Bot is starting.")
print("------------------------------")
print("Loading ENV file.")
load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")
member = os.getenv("MEMBER_ROLE")
moderator = os.getenv("MODERATOR_ROLE")
print("Loaded ENV file.")

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_connect():
	print("Connected to discord.")

@client.event
async def on_ready():
	print("---------------------------")
	print("Ultimate Core Bot is ready.")
	print("---------------------------")

for filename in os.listdir('./cogs'):
	print("Loading cogs")
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f"\"{filename[:-3]}\" cog has been loaded.")

client.run(token)
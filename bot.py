import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
from discord_slash import SlashCommand, SlashContext
import logging
import asyncio

print("--------------------------")
print("Beep Boop Bot is starting.")
print("--------------------------")
print("Loading ENV file.")
load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")
member = os.getenv("MEMBER_ROLE")
moderator = os.getenv("MODERATOR_ROLE")
print("Loaded ENV file.")

client = commands.Bot(command_prefix=prefix)
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)

@client.event
async def on_connect():
	print("Connected to discord.")

@client.event
async def on_ready():
	print("-----------------------")
	print("Beep Boop Bot is ready.")
	print("-----------------------")
	await asyncio.sleep(5)
	print("Logs clear in 20 seconds.")
	await asyncio.sleep(10)
	print("Logs clear in 10 seconds.")
	await asyncio.sleep(5)
	print("Logs clear in 5 seconds.")
	await asyncio.sleep(1)
	print("Logs clear in 4 seconds")
	await asyncio.sleep(1)
	print("Logs clear in 3 seconds")
	await asyncio.sleep(1)
	print("Logs clear in 2 seconds")
	await asyncio.sleep(1)
	print("Logs clear in 1seconds")
	await asyncio.sleep(1)
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("-----------------------")
	print("Beep Boop Bot is ready.")
	print("-----------------------")

print("Loading cogs")
for filename in os.listdir('./cogs'):
	if filename.endswith(".py"):
		client.load_extension(f'cogs.{filename[:-3]}')
		print(f"\"{filename[:-3]}\" cog has been loaded.")

# Logging: 
logging.basicConfig(level=logging.INFO)

client.run(token)
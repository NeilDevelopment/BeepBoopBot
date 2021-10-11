import discord
from discord.ext import commands, ipc
from dotenv import load_dotenv
import os 
from discord_slash import SlashCommand, SlashContext
import asyncio
import logging

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

# Debug Mode.

Debug_Mode = False
Debug_Boolean = bool(Debug_Mode)


# Make a class named "BeepBoopBot" which uses runs the IPC server.
class BeepBoopBot(commands.Bot):

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)

		self.ipc = ipc.Server(self, secret_key = "Neil")

	async def on_ipc_ready(self):
		"""Called upon the IPC Server being ready"""
		print("Ipc server is ready.")

	async def on_ipc_error(self, endpoint, error):
		"""Called upon an error being raised within an IPC route"""
		print(endpoint, "raised", error)

client = BeepBoopBot(command_prefix=prefix)
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True, sync_on_cog_reload=True)

@client.event
async def on_connect():
	print("Connected to discord.")

@client.event
async def on_ready():
	if Debug_Boolean is True:
		logging.basicConfig(level=logging.INFO)
		print("-----------------------")
		print("Debug Mode: True")
		print("Beep Boop Bot is ready.")
		print("-----------------------")
	else:
		print("-----------------------")
		print("Debug Mode: False")
		print("Beep Boop Bot is ready.")
		print("-----------------------")

print("Loading cogs")
for filename in os.listdir('./cogs'):
	if filename.endswith(".py"):
		client.load_extension(f'cogs.{filename[:-3]}')
		print(f"\"{filename[:-3]}\" cog has been loaded.")

@client.ipc.route()
async def get_guild_count(data):
	return len(client.guilds) # returns the len of the guilds to the client

@client.ipc.route()
async def get_guild_ids(data):
	final = []
	for guild in client.guilds:
		final.append(guild.id)
	return final

@client.ipc.route()
async def get_guild(data):
	guild = client.get_guild(data.guild_id)
	if guild is None: return None

	guild_data = {
		"name": guild.name,
		"id": guild.id,
		"channels": [c.id for c in guild.channels],
		"channel_names": [c.name for c in guild.channels],
		"prefix" : "?"
	}

	return guild_data

@client.ipc.route()
async def get_channel_ids(data):
	guild = client.get_guild(data.guild_id)
	if guild is None: return None

	guild_data = {
		"channels": [c.id for c in guild.channels],
	}

	return guild_data

@client.ipc.route()
async def get_channel_name(data):
	guild = client.get_guild(data.guild_id)
	if guild is None: return None

	guild_data = {
		"channel_names": [c.name for c in guild.channels],
	}

	return guild_data

@client.ipc.route()
async def send_message(data):
	name = data.channel
	channel = discord.utils.get(guild.text_channels, name=name)
	msg = data.msg
	await channel.send(msg)

@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')
	await ctx.send("Done!")

client.ipc.start()
client.run(token)
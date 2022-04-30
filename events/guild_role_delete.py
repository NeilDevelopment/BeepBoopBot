import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class guild_channel_create(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    log_channel = os.getenv("LOG_CHANNEL")

    @commands.Cog.listener()


def setup(client):
    client.add_cog(guild_channel_create(client))
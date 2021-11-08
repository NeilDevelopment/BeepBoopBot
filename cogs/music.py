import discord
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, client):
        self.bot = client

def setup(client):
    client.add_cog(Music(client))

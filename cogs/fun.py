from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.bot = client


def setup(client):
    client.add_cog(Fun(client))
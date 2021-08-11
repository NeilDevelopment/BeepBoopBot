from discord.ext import commands

class Giveaway(commands.Cog):

    def __init__(self, client):
        self.bot = client


def setup(client):
    client.add_cog(Giveaway(client))
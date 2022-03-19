import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class timeout(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    moderator_role = os.getenv("MODERATOR_ROLE")

    @commands.slash_command(guild_ids=[int(guild_id)])
    async def version(self, ctx):
        await ctx.respond("Running version 2.0 of BeepBoopBot.")

def setup(client):
    client.add_cog(timeout(client))
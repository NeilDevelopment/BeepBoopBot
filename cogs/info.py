import discord
from discord.ext import commands

class Info(commands.Cog):

    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def help(self, ctx):
        e = discord.Embed(title="BeepBoop Bot Help")
        e.add_field(name="Docs", value="[Click here!](https://github.com/NeilDevolopment/BeepBoopBot/wiki)")
        e.add_field(name="Commands", value="[Click here!](https://github.com/NeilDevolopment/BeepBoopBot/wiki/Commands)")
        await ctx.send(embed=e)

    @commands.command()
    async def version(self, ctx):
        await ctx.send("Running version 0.6 of BeepBoop Bot.")

def setup(client):
    client.add_cog(Info(client))
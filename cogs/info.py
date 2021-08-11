from discord.ext import commands

class Info(commands.Cog):

    def __init__(self, client):
        self.bot = client

        @commands.command()
        async def help(ctx):
            e = discord.Embed(title="BeepBoop Bot Help")
            e.add_field(name="Docs", description="[Click here!](https://github.com/NeilDevolopment/BeepBoopBot/wiki)")
            e.add_field(name="Commands", description="[Click here!](https://github.com/NeilDevolopment/BeepBoopBot/wiki/Commands)")
            await ctx.send(embed=e)

        @commands.command()
        async def version(ctx):
            await ctx.send("Running version 0.6 of BeepBoop Bot.")

def setup(client):
    client.add_cog(Info(client))
import discord, os, random
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class timeout(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    moderator_role = os.getenv("MODERATOR_ROLE")

    @commands.slash_command(guild_ids=[int(guild_id)])
    async def flip(self, ctx, choice: Option(str, "Pick your choice", choices=["Tails", "Heads"])):
        choices = ["Heads", "Tails"]
        randomcoin = random.choice(choices)
        if randomcoin == choice:
            e = discord.Embed(title=f"{randomcoin}! You won", color=discord.Color.green())
            await ctx.respond(embed=e)
        else:
            e = discord.Embed(title=f"{randomcoin}! You lost", color=discord.Color.red())
            await ctx.respond(embed=e)
        
def setup(client):
    client.add_cog(timeout(client))
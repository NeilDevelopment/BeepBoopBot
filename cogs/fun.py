import discord
from discord.ext import commands
import random
import asyncio 

class Fun(commands.Cog):

    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=['8ball', '8BALL'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later."
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]
        em = discord.Embed(title='Magic 8ball!',
                           colour=discord.Colour.blue())
        em.add_field(name=f"**Question:** {question}",
                     value=f"**Answer:** {random.choice(responses)}")
        await ctx.send(embed=em)

    @commands.command()
    async def count(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        messages = await channel.history(limit=None).flatten()
        count = len(messages)
        embed = discord.Embed(
            title="Total Messages",
            colour=0x2859b8,
            description=f"There were {count} messages in {channel.mention}")
        await ctx.send(embed=embed)

    @commands.command()
    async def flip(self, ctx):
        choices = ["Heads", "Tails"]
        rancoin = random.choice(choices)
        e = discord.Embed(title="Rolling...", color=discord.Color.blue())
        msg = await ctx.send(embed=e)
        await asyncio.sleep(3)
        e = discord.Embed(title=f"{rancoin}", color=discord.Color.blue())
        await msg.edit(embed=e)

def setup(client):
    client.add_cog(Fun(client))
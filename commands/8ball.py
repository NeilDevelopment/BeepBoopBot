import discord, os, random
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class eightball(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    moderator_role = os.getenv("MODERATOR_ROLE")

    @commands.slash_command(guild_ids=[int(guild_id)])
    async def _8ball(self, ctx, question: Option(str, "The question you want to ask 8ball", required=True)):
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
                     "Very doubtful.",
                     "Yeah",
                     "No",
                     "Alright, that's a yes from me!"]
        em = discord.Embed(title='Magic 8ball!',
                           colour=discord.Colour.blue())
        em.addfield(name=f"**Question:** {question}",
                     value=f"**Answer:** {random.choice(responses)}")
        await ctx.respond(embed=em)

def setup(client):
    client.add_cog(eightball(client))
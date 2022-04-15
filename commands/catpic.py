import discord, requests, os
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class catpic(commands.Cog):
    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")

    @commands.slash_command(guild_ids=[int(guild_id)])
    async def cat(self, ctx):
        response = requests.get('https://aws.random.cat/meow')
        data = response.json()
        embed = discord.Embed(title = 'Kitty Cat 🐈', description = 'Cats :star_struck:', colour = discord.Colour.purple())
        embed.set_image(url=data['file'])
        await ctx.respond(embed=embed)


def setup(client):
    client.add_cog(catpic(client))
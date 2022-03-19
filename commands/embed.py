import discord, os, random
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    moderator_role = os.getenv("MODERATOR_ROLE")

    @commands.slash_command(guild_ids=[guild_id])
    async def embed(self, ctx, title: Option(str, "The title for the embed", required=True), description: Option(str, "The description for the embed", required=True), channel: Option(discord.TextChannel, "The channel to send the embed to", required=True)):
            sending = discord.Embed(title=f"Sending Embed to #{channel.name}", color=discord.Color.blue())
            await ctx.respond(embed=sending, ephemeral=True)
            embed = discord.Embed(title=title, description=description, color=discord.Color.embed_background)
            embed.setauthor(name=ctx.author.name, iconurl=ctx.author.avatarurl)
            await channel.send(embed=embed)
        
def setup(client):
    client.add_cog(embed(client))
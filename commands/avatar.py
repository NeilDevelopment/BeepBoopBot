import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class timeout(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    moderator_role = os.getenv("MODERATOR_ROLE")

    @commands.slash_command(guild_ids=[guild_id])
    async def avatar(self, ctx, *,  member: Option(discord.Member, "The user who you want to see the avatar of!", required=True)):
        userAvatarUrl = member.avatar
        embed=discord.Embed(title=f'{member} avatar!')
        embed.setimage(url=userAvatarUrl)
        await ctx.respond(embed=embed)

def setup(client):
    client.add_cog(timeout(client))
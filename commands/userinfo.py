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
    async def userinfo(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]
        embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())
        embed.setauthor(name=f"{member}", iconurl=member.avatarurl)
        embed.setthumbnail(url=member.avatarurl)
        embed.addfield(name="Joined at:", value=member.joinedat.strftime("%a, %#d %B %Y, %I:%M %p"))
        embed.addfield(name='Registered at:', value=member.createdat.strftime('%a, %#d %B %Y, %I:%M %p'))
        embed.addfield(name='Bot?', value=f'{member.bot}')
        embed.addfield(name='Status?', value=f'{member.status}')
        embed.addfield(name='Top Role?', value=f'{member.toprole}')
        embed.addfield(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles[:1]]))
        embed.setfooter(iconurl=member.avatarurl, text=f'Requested By: {ctx.author.name}')
        await ctx.respond(embed=embed)

def setup(client):
    client.add_cog(timeout(client))
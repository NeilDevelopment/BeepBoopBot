import discord, os
from discord.ext import commands
from discord.commands import \
    slash_command, Option


class kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    admin_role = os.getenv("ADMIN_ROLE")

    @commands.slash_command(guild_ids=[int(guild_id)])
    @commands.has_role(int(admin_role))
    async def kick(self, ctx, member: Option(discord.Member, "The user to kick", default=None, required=True), reason: Option(str, "Reason for the kick", default="No reason specified", required=False)):
        if member:
            await member.kick(reason=reason)
            e = discord.Embed(title="Member kicked!", description=f"{member.mention} has been kicked for {reason}!", color=discord.Color.green())
            await ctx.respond(embed=e)
        else:
            e = discord.Embed(title="User not specified! :x:", description=f"You have not specified a user!", color=discord.Color.red())

def setup(client):
    client.add_cog(kick(client))
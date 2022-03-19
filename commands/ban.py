import discord, os
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    guild_id = os.getenv("GUILD_ID")
    admin_role = os.getenv("ADMIN_ROLE")

    @commands.slash_command(guild_ids=[int(guild_id)])
    @commands.has_role(int(admin_role))
    async def ban(self, ctx, member: Option(discord.Member, "The user to ban", default=None, required=True), reason: Option(str, "Reason for the ban", default="No reason specified", required=False)):
        if member:
            await member.ban(reason=reason)
            e = discord.Embed(title="Member banned!", description=f"{member.mention} has been banned for {reason}!", color=discord.Color.green())
            await ctx.respond(embed=e)
        else:
            e = discord.Embed(title="User not specified! :x:", description=f"You have not specified a user!", color=discord.Color.red())

def setup(client):
    client.add_cog(ban(client))

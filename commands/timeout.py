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
    @commands.has_role(int(moderator_role))
    async def timeout(self, ctx, member: Option(discord.Member, "The user to timeout", default=None, required=True), duration: Option(int, "The duration that the user should be timed out for! (s|m|h|d)", default=None, required=True), reason: Option(str, "Reason for the timeout", default="No reason specified", required=False)):
        if member:
            def convert(time):
                pos = ["s","m","h","d"]

                time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

                unit = time[-1]

                if unit not in pos:
                    return -1
                try:
                    val = int(time[:-1])
                except:
                    return -2


                return val * time_dict[unit]
            convtime = convert(duration)
            if convtime == -1:
                await ctx.respond("You didn't answer with a proper unit. Example: `1m` which is 1 minute")
            else:
                duration = datetime.timedelta(seconds=convtime)
                await member.timeout_for(duration)
                e = discord.Embed(title="Timed out member!", description=f"{member.mention} has been timed out for {duration}\nReason: {reason}!", color=discord.Color.green())
                await ctx.respond(embed=e)
        else:
            e = discord.Embed(title="User not specified! :x:", description=f"You have not specified a user!", color=discord.Color.red())

def setup(client):
    client.add_cog(timeout(client))
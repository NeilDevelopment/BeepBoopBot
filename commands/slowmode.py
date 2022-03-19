import discord, os, traceback
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class slowmode(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    admin_role = os.getenv("ADMIN_ROLE")

    @commands.slash_command(guild_ids=[guild_id])
    async def slowmode(self, ctx, time: Option(int, "Time to change the slowmode to (s|m|h|d", default="No reason specified", required=False)):
        try:
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
            convtime = convert(time)
            if convtime == 0:
                embed = discord.Embed(title='Slowmode turned off')
                await ctx.respond(embed=embed)
                await ctx.channel.edit(slowmode_delay=0)
            if convtime == "off":
                embed = discord.Embed(title='Slowmode turned off')
                await ctx.respond(embed=embed)
                await ctx.channel.edit(slowmode_delay=0)
            elif convtime > 21600:
                embed = discord.Embed(
                    title='You cannot have a slowmode above 6 hours..')
                await ctx.respond(embed=embed)
            else:
                await ctx.channel.edit(slowmode_delay=time)
                embed = discord.Embed(title=f'Slowmode set to {time} seconds.')
                await ctx.respond(embed=embed)
        except Exception:   
            traceback.print_exc()

def setup(client):
    client.add_cog(slowmode(client))
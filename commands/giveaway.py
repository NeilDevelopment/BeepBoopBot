import discord, os, asyncio, random
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class giveaway(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    admin_role = os.getenv("ADMIN_ROLE")

    @commands.slash_command(guild_ids=[int(guild_id)])
    @commands.has_role(admin_role)
    async def giveaway(self, ctx, channel: discord.TextChannel, time, prize):
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

        timeconv = convert(time)
        if time == -1:
            await ctx.respond(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
            return
        elif time == -2:
            await ctx.respond(f"The time must be an integer. Please enter an integer next time")
            return            

        await ctx.respond(f"The Giveaway will be in {channel.mention} and will last {time}!")


        embed = discord.Embed(title = "Giveaway!", description = f"Prize: {prize}", color = ctx.author.color)

        embed.add_field(name = "Hosted by:", value = ctx.author.mention)

        embed.set_footer(text = f"Ends {time} from now!")

        my_msg = await channel.send(embed = embed)

        await my_msg.add_reaction("🎉")


        await asyncio.sleep(timeconv)


        new_msg = await channel.fetch_message(my_msg.id)


        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)

        await channel.send(f"Congratulations! {winner.mention} won **{prize}**!")

        e = discord.Embed(title = "Giveaway Ended!", description = f"Prize: {prize}", color = ctx.author.color)
        e.add_field(name=f"Winner:", value=f"{winner.mention}", inline=False)
        e.add_field(name = "Hosted by:", value = ctx.author.mention, inline=False)

        e.set_footer(text = f"Giveaway ended!")

        await my_msg.edit(embed=e)

def setup(client):
    client.add_cog(giveaway(client))
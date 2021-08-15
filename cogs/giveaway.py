import discord
from discord.ext import commands
import os 
import random
import asyncio

class Giveaway(commands.Cog):

    def __init__(self, client):
        self.bot = client
        admin_role = os.getenv("ADMIN_ROLE")
        guildid = os.getenv("GUILD_ID")

    @commands.command()
    async def giveaway(self, ctx, ):
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

        time = convert(time)
        if time == -1:
            await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
            return
        elif time == -2:
            await ctx.send(f"The time must be an integer. Please enter an integer next time")
            return            

        await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")


        embed = discord.Embed(title = "Giveaway!", description = f"Prize: {prize}", color = ctx.author.color)

        embed.add_field(name = "Hosted by:", value = ctx.author.mention)

        embed.set_footer(text = f"Ends {answers[1]} from now!")

        my_msg = await channel.send(embed = embed)

        await my_msg.add_reaction("🎉")


        await asyncio.sleep(time)


        new_msg = await channel.fetch_message(my_msg.id)


        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.bot.user))

        winner = random.choice(users)

        await channel.send(f"Congratulations! {winner.mention} won **{prize}**!")

        e = discord.Embed(title = "Giveaway Ended!", description = f"Prize: {prize}", color = ctx.author.color)
        e.add_field(name=f"Winner:", value=f"{winner.mention}", inline=False)
        e.add_field(name = "Hosted by:", value = ctx.author.mention, inline=False)

        e.set_footer(text = f"Ends {answers[1]} from now!")

        await my_msg.edit(embed=e)

def setup(client):
    client.add_cog(Giveaway(client))
import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class serverinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    moderator_role = os.getenv("MODERATOR_ROLE")

    @commands.slash_command(guild_ids=[int(guild_id)])
    async def serverinfo(self, ctx):
            findbots = sum(1 for member in ctx.guild.members if member.bot)
            embed = discord.Embed(title = 'Infomation about ' + ctx.guild.name + '.', colour = discord.Colour.fromrgb(54,151,255))
            embed.setthumbnail(url = str(ctx.guild.iconurl))
            embed.addfield(name = "Guild's name: ", value = ctx.guild.name)
            embed.addfield(name = "Guild's owner: ", value = str(ctx.guild.owner))
            embed.addfield(name = "Guild's verification level: ", value = str(ctx.guild.verificationlevel))
            embed.addfield(name = "Guild's id: ", value = str(ctx.guild.id))
            embed.addfield(name = "Guild's member count: ", value = str(ctx.guild.membercount))
            embed.addfield(name="Bots", value=findbots, inline=True)
            embed.addfield(name = "Guild created at: ", value = str(ctx.guild.createdat.strftime("%a, %d %B %Y, %I:%M %p UTC")))
            await ctx.respond(embed =  embed)

def setup(client):
    client.add_cog(serverinfo(client))
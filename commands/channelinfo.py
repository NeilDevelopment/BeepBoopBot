import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class channelinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    moderator_role = os.getenv("MODERATOR_ROLE")

    @commands.slash_command(guild_ids=[int(guild_id)])
    async def channelinfo(self, ctx, channel: discord.TextChannel):
        nsfw = self.client.getchannel(channel.id).isnsfw()
        embed = discord.Embed(title = 'Channel Infromation: ' + str(channel),
        colour = discord.Colour.fromrgb(54, 151, 255))
        embed.addfield(name = 'Channel Name: ', value = str(channel.name))
        embed.addfield(name = "Channel's NSFW Status: ", value = str(nsfw))
        embed.addfield(name = "Channel's id: " , value = str(channel.id))
        embed.addfield(name = 'Channel Created At: ', value = str(channel.createdat.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.addfield(name = 'Channel Type: ', value = str(channel.type))
        await ctx.respond(embed = embed)

def setup(client):
    client.add_cog(channelinfo(client))
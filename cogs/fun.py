import discord
from discord import guild
from discord.ext import commands
import random
import asyncio 
import datetime
from discord_slash import cog_ext, SlashContext
import os

from discord_slash.utils.manage_commands import get_guild_command_permissions

class Fun(commands.Cog):

    def __init__(self, client):
        self.bot = client
    
    @cog_ext.cog_slash(name="8ball", description="Ask 8ball a question!")
    async def _8ball(self, ctx: SlashContext, *, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later."
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful.",
                     "Yeah",
                     "No",
                     "Alright, that's a yes from me!"]
        em = discord.Embed(title='Magic 8ball!',
                           colour=discord.Colour.blue())
        em.add_field(name=f"**Question:** {question}",
                     value=f"**Answer:** {random.choice(responses)}")
        await ctx.send(embed=em)

    @cog_ext.cog_slash(name="count", description="Count a channel's messages.")
    async def _count(self, ctx: SlashContext, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        messages = await channel.history(limit=None).flatten()
        messagecount = len(messages)
        embed = discord.Embed(
            title="Total Messages",
            colour=0x2859b8,
            description=f"There were {messagecount} messages in {channel.mention}")
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="flip", description="Flip a coin.")
    async def _flip(self, ctx: SlashContext):
        choices = ["Heads", "Tails"]
        randomcoin = random.choice(choices)
        e = discord.Embed(title="Rolling...", color=discord.Color.blue())
        msg = await ctx.send(embed=e)
        await asyncio.sleep(3)
        e = discord.Embed(title=f"{randomcoin}", color=discord.Color.blue())
        await msg.edit(embed=e)


    @cog_ext.cog_slash(name="channelinfo", description="Get information about a channel.")
    async def _channelinfo(self, ctx: SlashContext, channel: discord.TextChannel):
        nsfw = self.bot.get_channel(channel.id).is_nsfw()
        embed = discord.Embed(title = 'Channel Infromation: ' + str(channel),
        colour = discord.Colour.from_rgb(54, 151, 255))
        embed.add_field(name = 'Channel Name: ', value = str(channel.name))
        embed.add_field(name = "Channel's NSFW Status: ", value = str(nsfw))
        embed.add_field(name = "Channel's id: " , value = str(channel.id))
        embed.add_field(name = 'Channel Created At: ', value = str(channel.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.add_field(name = 'Channel Type: ', value = str(channel.type))
        await ctx.send(embed = embed)

    @cog_ext.cog_slash(name="avatar", description="Get a user's profile picture")
    async def _avatar(self, ctx: SlashContext, *,  member : discord.Member=None):
        userAvatarUrl = member.avatar_url
        embed=discord.Embed(title=f'{member} avatar!!')
        embed.set_image(url=userAvatarUrl)
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="userinfo", description="Get information about a user.")
    async def _userinfo(self, ctx: SlashContext, member: discord.Member):
        roles = [role for role in member.roles]
        embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{member}", icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))
        embed.add_field(name='Registered at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p'))
        embed.add_field(name='Bot?', value=f'{member.bot}')
        embed.add_field(name='Status?', value=f'{member.status}')
        embed.add_field(name='Top Role?', value=f'{member.top_role}')
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles[:1]]))
        embed.set_footer(icon_url=member.avatar_url, text=f'Requested By: {ctx.author.name}')
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="serverinfo", description="Get information about the server.")
    async def _serverinfo(self, ctx: SlashContext):
            findbots = sum(1 for member in ctx.guild.members if member.bot)
            embed = discord.Embed(title = 'Infomation about ' + ctx.guild.name + '.', colour = discord.Colour.from_rgb(54,151,255))
            embed.set_thumbnail(url = str(ctx.guild.icon_url))
            embed.add_field(name = "Guild's name: ", value = ctx.guild.name)
            embed.add_field(name = "Guild's owner: ", value = str(ctx.guild.owner))
            embed.add_field(name = "Guild's verification level: ", value = str(ctx.guild.verification_level))
            embed.add_field(name = "Guild's id: ", value = str(ctx.guild.id))
            embed.add_field(name = "Guild's member count: ", value = str(ctx.guild.member_count))
            embed.add_field(name="Bots", value=findbots, inline=True)
            embed.add_field(name = "Guild created at: ", value = str(ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
            await ctx.send(embed =  embed)
    
    @cog_ext.cog_slash(name="embed", description="Create a embed")
    async def _embed(self, ctx: SlashContext, *,str, content: str):
        embed = discord.Embed(title="Embed Creator", description=content, color=0x00ff00)
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="Decode", description="Decode a message", guild_ids=[851785650230919178])
    async def _decode(ctx: SlashContext, *, message: str):
        base64_string = message
        base64_bytes = base64_string.encode("ascii")
        decoded_bytes = base64.b64decode(base64_bytes)
        decoded_string = decoded_bytes.decode("ascii")
        await ctx.reply(decoded_string)


    @cog_ext.cog_slash(name="Encode", description="Encode a message", guild_ids=[851785650230919178])
    async def encode(ctx: SlashContext, *, message: str):
        message_bytes = message.encode("ascii")

        base64_bytes = base64.b64encode(message_bytes)
        encoded_string = base64_bytes.decode("ascii")
        await ctx.reply(encoded_string)

def setup(client):
    client.add_cog(Fun(client))
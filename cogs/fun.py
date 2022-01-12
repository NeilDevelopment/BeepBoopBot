import discord
from discord import guild
from discord.colour import Color
from discord.commands import slash_command
from discord.ext import commands
import random
import asyncio 
import datetime
import os
import base64

class Fun(commands.Cog):

    def __init__(self, client):
        self.bot = client
    
    @slash_command()
    async def _8ball(self, ctx, *, question):
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
        em.addfield(name=f"**Question:** {question}",
                     value=f"**Answer:** {random.choice(responses)}")
        await ctx.send(embed=em)

    @slash_command()
    async def count(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        messages = await channel.history(limit=None).flatten()
        messagecount = len(messages)
        embed = discord.Embed(
            title="Total Messages",
            colour=0x2859b8,
            description=f"There were {messagecount} messages in {channel.mention}")
        await ctx.send(embed=embed)

    @slash_command()
    async def flip(self, ctx):
        choices = ["Heads", "Tails"]
        randomcoin = random.choice(choices)
        e = discord.Embed(title="Rolling...", color=discord.Color.blue())
        msg = await ctx.send(embed=e)
        await asyncio.sleep(3)
        e = discord.Embed(title=f"{randomcoin}", color=discord.Color.blue())
        await msg.edit(embed=e)


    @slash_command()
    async def channelinfo(self, ctx, channel: discord.TextChannel):
        nsfw = self.bot.getchannel(channel.id).isnsfw()
        embed = discord.Embed(title = 'Channel Infromation: ' + str(channel),
        colour = discord.Colour.fromrgb(54, 151, 255))
        embed.addfield(name = 'Channel Name: ', value = str(channel.name))
        embed.addfield(name = "Channel's NSFW Status: ", value = str(nsfw))
        embed.addfield(name = "Channel's id: " , value = str(channel.id))
        embed.addfield(name = 'Channel Created At: ', value = str(channel.createdat.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.addfield(name = 'Channel Type: ', value = str(channel.type))
        await ctx.send(embed = embed)

    @slash_command()
    async def avatar(self, ctx, *,  member : discord.Member=None):
        userAvatarUrl = member.avatarurl
        embed=discord.Embed(title=f'{member} avatar!!')
        embed.setimage(url=userAvatarUrl)
        await ctx.send(embed=embed)

    @slash_command()
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
        await ctx.send(embed=embed)

    @slash_command()
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
            await ctx.send(embed =  embed)

    @slash_command(guild_ids=[851785650230919178])
    async def embed(self, ctx, title, description, channel: discord.TextChannel):
            sending = discord.Embed(title=f"Sending Embed to #{channel.name}", color=discord.Color.blue())
            msg = await ctx.respond(embed=sending)
            embed = discord.Embed(title=title, description=description, color=0x00ff00)
            embed.setauthor(name=ctx.author.name, iconurl=ctx.author.avatarurl)
            embed = discord.Embed(title=title, description=description, color=0x00ff00)
            embed.setauthor(name=ctx.author.name, iconurl=ctx.author.avatarurl)
            await asyncio.sleep(1) # So people can't spam and get the bot rate limited
            await channel.send(embed=embed)
            doneembed = discord.Embed(title=f"Send Embed to #{channel.name}", color=discord.Color.green())
            await msg.edit(embed=doneembed)

def setup(client):
    client.add_cog(Fun(client))
import discord
from discord.ext import commands
import random
import asyncio 
import datetime

class Fun(commands.Cog):

    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=['8ball', '8BALL'])
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
                     "Very doubtful."]
        em = discord.Embed(title='Magic 8ball!',
                           colour=discord.Colour.blue())
        em.add_field(name=f"**Question:** {question}",
                     value=f"**Answer:** {random.choice(responses)}")
        await ctx.send(embed=em)

    @commands.command()
    async def count(self, ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel
        messages = await channel.history(limit=None).flatten()
        count = len(messages)
        embed = discord.Embed(
            title="Total Messages",
            colour=0x2859b8,
            description=f"There were {count} messages in {channel.mention}")
        await ctx.send(embed=embed)

    @commands.command()
    async def flip(self, ctx):
        choices = ["Heads", "Tails"]
        rancoin = random.choice(choices)
        e = discord.Embed(title="Rolling...", color=discord.Color.blue())
        msg = await ctx.send(embed=e)
        await asyncio.sleep(3)
        e = discord.Embed(title=f"{rancoin}", color=discord.Color.blue())
        await msg.edit(embed=e)


    @commands.command(aliases = ['channelstats', 'ChannelInfo', 'Channelinfo'])
    async def channelinfo(self, ctx, channel:discord.TextChannel):
        nsfw = self.bot.get_channel(channel.id).is_nsfw()
        embed = discord.Embed(title = 'Channel Infromation: ' + str(channel),
        colour = discord.Colour.from_rgb(54, 151, 255))
        embed.add_field(name = 'Channel Name: ', value = str(channel.name))
        embed.add_field(name = "Channel's NSFW Status: ", value = str(nsfw))
        embed.add_field(name = "Channel's id: " , value = str(channel.id))
        embed.add_field(name = 'Channel Created At: ', value = str(channel.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.add_field(name = 'Channel Type: ', value = str(channel.type))
        await ctx.send(embed = embed)

    @commands.command(aliases = ['ava', 'Avatar', 'AVATAR'])
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        embed=discord.Embed(title=f'{avamember} avatar!!')
        embed.set_image(url=userAvatarUrl)
        await ctx.send(embed=embed)```

    @commands.command(aliases=['whois', 'Whois', 'WHOis', 'WHOIS'])
    async def userinfo(self,ctx, member: discord.Member):
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

    @commands.command(aliases = ['guildinfo', 'Serverinfo', 'ServerInfo', 'GuildInfo', 'Guikldinfo'])
    async def serverinfo(self, ctx):
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

def setup(client):
    client.add_cog(Fun(client))
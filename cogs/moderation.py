import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import os 
from dotenv import load_dotenv
import json

class Moderation(commands.Cog):

    def __init__(self, client):
        self.bot = client

    admin_role = os.getenv("ADMIN_ROLE")    
    guildid = os.getenv("GUILD_ID")

    @cog_ext.cog_slash(name="nick", description="Change someone's nickname.")
    @commands.has_permissions(change_nickname=True)
    async def _nick(self, ctx, member: discord.Member, name):
        await member.edit(nick=name)
        embed = discord.Embed(title='Nick Name Successfully Changed!')
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="clear", description="Clear messages.")
    @commands.has_permissions(manage_messages=True)
    async def _clear(self, ctx, amount: int):
        await ctx.message.delete()
        await ctx.send("Clearing messages, this may take a while..", delete_after=10)
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'{amount} messages has been cleared', delete_after=5)

    @cog_ext.cog_slash(name="slowmode", description="Set slowmode.")
    async def _slowmode(self, ctx, time: int):
        try:
            if time == 0:
                embed = discord.Embed(title='Slowmode turned off')
                await ctx.send(embed=embed)
                await ctx.channel.edit(slowmode_delay=0)
            if time == "off":
                embed = discord.Embed(title='Slowmode turned off')
                await ctx.send(embed=embed)
                await ctx.channel.edit(slowmode_delay=0)
            elif time > 21600:
                embed = discord.Embed(
                    title='You cannot have a slowmode above 6 hours..')
                await ctx.send(embed=embed)
            else:
                await ctx.channel.edit(slowmode_delay=time)
                embed = discord.Embed(title=f'Slowmode set to {time} seconds.')
                await ctx.send(embed=embed)
        except Exception:
            traceback.print_exc()

    @cog_ext.cog_slash(name="softban", description="Softban someone.")
    async def _softban(self, ctx, member: discord.Member, *, reason='No reason provided'):
        await member.ban(reason=reason)
        await member.unban(reason=reason)
        embed = discord.Embed(title=f'Successfully softbanned {member}')
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name="ban", description="Ban someone.")
    @commands.has_permissions(ban_members=True)
    async def _ban(self, ctx, member: discord.Member = None, *, reason=None):
        if member is None:
            em = discord.Embed(title='Please specify a member.')
            await ctx.send(embed=em)
            return
        await member.ban(reason=reason)
        em = discord.Embed(title=f'You banned {member}')
        await ctx.send(embed=em)

        embed = discord.Embed(
            title=f'You have been banned from {guild.name}', description=f'Banned by {member}')
        embed.add_field(name='Reason:', value=f'{reason}')
        await member.send(embed=embed)

    @cog_ext.cog_slash(name="unban", description="Unban someone.")
    @commands.has_permissions(ban_members=True)
    async def _unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                em = discord.Embed(title=f'You Unbanned {user.mention}')
                await ctx.send(embed=em)
                return

    @cog_ext.cog_slash(name="kick", description="Kick someone.")
    @commands.has_permissions(administrator=True)
    async def _kick(self, ctx, member: discord.Member = None, *, reason='No reason provided'):
        if not member:
            em = discord.Embed(title='Please specify a member.')
            await ctx.send(embed=em)
            return
        await member.kick()
        em = discord.Embed(title=f'You kicked {member}')
        await ctx.send(embed=em)
        embed = discord.Embed(
            title=f'You have been kicked from {ctx.guild.name}', description=f'Kicked by {member}')
        embed.add_field(name='Reason:', value=f'{reason}')
        await member.send(embed=embed)

    @cog_ext.cog_slash(name="warn", description="Warn someone.")
    @commands.has_permissions(kick_members=True)
    async def _warn(self, ctx, member: discord.Member, *, reason="No reason Provided"):
        with open('warnings.json', 'r') as f:
            warns = json.load(f)
        if str(ctx.guild.id) not in warns:
            warns[str(ctx.guild.id)] = {}
        if str(member.id) not in warns[str(ctx.guild.id)]:
            warns[str(ctx.guild.id)][str(member.id)] = {}
            warns[str(ctx.guild.id)][str(member.id)]["warns"] = 1
            warns[str(ctx.guild.id)][str(member.id)]["warnings"] = [reason]
        else:
            warns[str(ctx.guild.id)][str(member.id)]["warnings"].append(reason)
        with open('warnings.json', 'w') as f:
            json.dump(warns, f)
            await ctx.send(f"{member.mention} was warned for: {reason}")

            embed = discord.Embed(
                title=f'You have been warned in {ctx.guild.name} ', description=f'You received a warning from {ctx.author}')
            embed.add_field(name='Reason:', value=f'{reason}')
            await member.send(embed=embed)

    @cog_ext.cog_slash(name="removewarn", description="Remove a warning.")
    @commands.has_permissions(manage_guild=True)
    async def _removewarn(self, ctx, member: discord.Member, num: int, *, reason='No reason provided.'):
        with open('warnings.json', 'r') as f:
            warns = json.load(f)

        num -= 1
        warns[str(ctx.guild.id)][str(member.id)]["warns"] -= 1
        warns[str(ctx.guild.id)][str(member.id)]["warnings"].pop(num)
        with open('warnings.json', 'w') as f:
            json.dump(warns, f)
            await ctx.send('Warn has been removed!')
            embed = discord.Embed(
                title=f'Your warn in {ctx.guild.name}  been removed', description=f'Your warning was removed by {ctx.author}')
            await member.send(embed=embed)

    @cog_ext.cog_slash(name="warns", description="Get a user's warnings.")
    @commands.has_permissions(manage_messages=True)
    async def _warns(self, ctx, member: discord.Member):
        with open('warnings.json', 'r') as f:
            warns = json.load(f)

        num = 1
        warnings = discord.Embed(title=f"{member}\'s warns")
        for warn in warns[str(ctx.guild.id)][str(member.id)]["warnings"]:
            warnings.add_field(name=f"Warn {num}", value=warn)
            num += 1
        await ctx.send(embed=warnings)

    @cog_ext.cog_slash(name="setstatus", description="Set the bot's status!", default_permission=False, permissions={
    guildid: [
        discord_slash.utils.manage_commands.create_permission(admin_role, discord_slash.utils.manage_commands.SlashCommandPermissionType.ROLE, True)
    ]
})
    async def _setstatus(self, ctx, *, status):
        await self.bot.change_presence(activity = discord.Game(name=status))
        em = discord.Embed(title=f'Status set to {status}')
        await ctx.send(embed=em)


def setup(client):
    client.add_cog(Moderation(client))

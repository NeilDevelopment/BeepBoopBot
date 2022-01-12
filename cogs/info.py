import discord
from discord.ext import commands
from discord.commands import slash_command
import datetime

class Info(commands.Cog):

    def __init__(self, client):
        self.bot = client

    @slash_command(guild_ids=[851785650230919178])
    async def help(self, ctx: SlashContext):
        select = create_select(
            options=[
                create_select_option("Moderation", value="Moderation"),
                create_select_option("Giveaway", value="Giveaway"),
                create_select_option("Fun", value="Fun"),
            ],

            placeholder="Choose a module",
            min_values=1,
            max_values=1,
        )
        e = discord.Embed(title="Please specify a module.",
                          timestamp=datetime.datetime.now(datetime.timezone.utc), color=discord.Color.blue())
        e.add_field(name="Moderation",
                    value=f"Contains all the moderation commands.", inline=False)
        e.add_field(name="Giveaway",
                    value=f"Contains all the giveaway commands.", inline=False)
        e.add_field(name="Fun",
                    value=f"Contains all the fun commands.", inline=False)
        await ctx.send(embed=e, components=[create_actionrow(select)])

    @slash_command()
    async def _version(self, ctx: SlashContext):
        await ctx.send("Running version 1.2 of BeepBoopBot.")

    @commands.Cog.listener()
    async def on_component(self, ctx):
        if ctx.selected_options[0] == "Moderation":
            embed = discord.Embed(title="Moderation", description="`nick` - Set's a user's nickname.\n `clear` - Clears a amount of messages.\n `ban` - Bans a member\n `unban` - Unbans a member\n `kick` - Kicks a member.\n `warn` - Warns a member\n `removewarn` - Removes a warn from a member.\n `warns` - Check a member's warns. \n\n **Syntax's and more information [here](https://github.com/NeilDevolopment/BeepBoopBot/wiki/Commands#moderation)!**", color=discord.Color.blue())
            await ctx.edit_origin(embed=embed)
        if ctx.selected_options[0] == "Fun":
            embed = discord.Embed(title="Fun",
                                  description=f"`8ball` - Ask 8ball a question.\n `count` - Find the totally amount of messages sent in the channel.\n `flip` - Flip a coin.\n `channelinfo` - Get information about a channel.\n `avatar` - Get a user's profile picture.\n `userinfo` - Get information about a user.\n `serverinfo` - Get information about the server.\n `embed` - Make an embed \n\n **Syntax's and more information [here](https://github.com/NeilDevolopment/BeepBoopBot/wiki/Commands#fun)!**", color=discord.Color.blue())
            await ctx.edit_origin(embed=embed)
        if ctx.selected_options[0] == "Giveaway":
            embed = discord.Embed(title="Giveaway",
                                  description=f"`giveaway` - Host a giveaway. \n\n **Syntax's and more information [here](https://github.com/NeilDevolopment/BeepBoopBot/wiki/Commands#giveaway)!**", color=discord.Color.blue())
            await ctx.edit_origin(embed=embed)

def setup(client):
    client.add_cog(Info(client))

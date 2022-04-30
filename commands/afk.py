import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option
from data import Data

class afk(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    guild_id = os.getenv("GUILD_ID")
    admin_role = os.getenv("ADMIN_ROLE")
    
    @commands.slash_command(guild_ids=[int(guild_id)])
    async def afk(self, ctx: discord.ApplicationContext, reason: str):
        """
        Sets your AFK status
        """

        already_afk = Data.afk_entry_exists(ctx.author)

        if already_afk:
            Data.c.execute(
                """UPDATE afks SET afk_reason = :new_reason
                WHERE user_id = :user_id""",
                {"new_reason": reason, "user_id": ctx.author.id},
            )
        else:
            Data.create_new_afk_data(ctx.author, reason)

        Data.conn.commit()
        await ctx.respond(
            f"You have been AFK'd for the following reason:\n{reason}",
            allowed_mentions=discord.AllowedMentions.none(),
        )

    @commands.slash_command(guild_ids=[int(guild_id)])
    async def unafk(self, ctx: discord.ApplicationContext):
        """
        Unset your AFK status
        """

        already_afk = Data.afk_entry_exists(ctx.author)

        if already_afk:
            Data.delete_afk_data(ctx.author)
            await ctx.respond("You are no longer AFK'd")
        else:
            await ctx.respond("You are not currently AFK'd")


def setup(client):
    client.add_cog(afk(client))
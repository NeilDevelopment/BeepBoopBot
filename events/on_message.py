import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option
from data import Data
import asyncio

class on_message(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    moderator_role = os.getenv("MODERATOR_ROLE")

    async def process_afk(self, message: discord.Message):
        async def run_afk(afk_entry):
            user = await self.bot.fetch_user(int(afk_entry[0]))
            if user in message.mentions:
                afk_reason = afk_entry[1]
                await message.channel.send(
                    f"{user} is currently AFK because:\n*{afk_reason}*",
                    allowed_mentions=discord.AllowedMentions.none(),
                )

        Data.c.execute("SELECT * FROM afks")
        afks = Data.c.fetchall()
        afk_tasks = [run_afk(afk) for afk in afks]
        await asyncio.gather(*afk_tasks)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author != self.bot.user:
            await self.process_afk(message)


def setup(client):
    client.add_cog(on_message(client))
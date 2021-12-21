import discord
from discord.ext import commands
import os
from discord.gateway import DiscordWebSocket
from dotenv import load_dotenv
import datetime

class Logs(commands.Cog):

    def __init__(self, client):
        self.bot = client
        self.log_channel = os.getenv("LOG_CHANNEL")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = discord.Embed(title=f"Message deleted in {message.channel.name}", description=f"{message.content}", color=0xc25252, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{message.author.name}", icon_url=f"{message.author.avatar_url}")
        embed.set_footer(text=f"{message.author.id}")
        channel = self.bot.get_channel(int(self.log_channel))
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
            embed = discord.Embed(title=f"Message edited in {message_before.channel.name}", description=f"**Before:** {message_before.content}\n**+After:** {message_after.content}", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
            embed.set_author(name=f"{message_before.author.name}", icon_url=f"{message_before.author.avatar_url}")
            embed.set_footer(text=f"ID: {message_after.author.id}")
            channel = self.bot.get_channel(int(self.log_channel))
            await channel.send(embed=embed)

def setup(client):
    client.add_cog(Logs(client))
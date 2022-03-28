import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class message_delete(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    log_channel = os.getenv("LOG_CHANNEL")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        embed = discord.Embed(title=f"Message deleted in {message.channel.name}", description=f"{message.content}", color=0xc25252, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{message.author.name}", icon_url=f"{message.author.avatar}")
        embed.set_footer(text=f"{message.author.id}")
        channel = self.client.get_channel(int(self.log_channel))
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(message_delete(client))
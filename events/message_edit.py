import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class message_edit(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    log_channel = os.getenv("LOG_CHANNEL")

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
            embed = discord.Embed(title=f"Message edited in {message_before.channel.name}", description=f"**Before:** {message_before.content}\n**+After:** {message_after.content}", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
            embed.set_author(name=f"{message_before.author.name}", icon_url=f"{message_before.author.avatar.url}")
            embed.set_footer(text=f"ID: {message_after.author.id}")
            channel = self.client.get_channel(int(self.log_channel))
            await channel.send(embed=embed)

def setup(client):
    client.add_cog(message_edit(client))
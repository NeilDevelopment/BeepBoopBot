import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class guild_channel_update(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    log_channel = os.getenv("LOG_CHANNEL")

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        if before.name != after.name:
            e = discord.Embed(title=f":pencil: Text channel updated: {before.name}", color=discord.Color.orange(), timestamp=datetime.datetime.utcnow())
            e.add_field(name="Renamed", value=f"{before.name} -> {after.name}")
            channel = self.client.get_channel(int(self.log_channel))
            await channel.send(embed=e)

def setup(client):
    client.add_cog(guild_channel_update(client))
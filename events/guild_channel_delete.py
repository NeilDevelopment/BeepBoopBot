import discord, os, datetime
from discord.ext import commands
from discord.commands import \
    slash_command, Option

class guild_channel_create(commands.Cog):

    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    log_channel = os.getenv("LOG_CHANNEL")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        e = discord.Embed(title=f":wastebasket: Text channel deleted: {channel}", color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
        e.add_field(name="Name", value=f"{channel}")
        channel = self.client.get_channel(int(self.log_channel))
        await channel.send(embed=e)

def setup(client):
    client.add_cog(guild_channel_create(client))
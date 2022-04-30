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
    async def on_guild_role_create(self, role):
        e = discord.Embed(title=f":crossed_swords: Role created: {role.name}", color=discord.Color.green(), timestamp=datetime.datetime.utcnow())
        e.set_footer(text=f"ID: {role.id}")
        channel = self.client.get_channel(959417909996830770)
        await channel.send(embed=e)

def setup(client):
    client.add_cog(guild_channel_create(client))
import os, discord
from discord.ext import commands
from discord.commands import \
    slash_command
from utils import search_youtube

guild_id = os.getenv("GUILD_ID")

class Youtube(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.yt_search_url = "https://www.youtube.com/results?search_query="
        self.yt_video_url = "https://www.youtube.com/watch?v="

    @commands.slash_command(guild_ids=[int(guild_id)])
    async def youtube(self, ctx: discord.ApplicationContext, query: str):
        await ctx.defer()
        first_result = await search_youtube(query)
        await ctx.respond(first_result)


def setup(client):
    client.add_cog(Youtube(client))
import discord, os, urbanpython
from discord.ext import commands
from discord.commands import \
    slash_command

class urban(commands.Cog):

    def __init__(self, client):
        self.client = client

    urban = urbanpython.Urban(os.getenv("URBAN_API_KEY"))
    guild_id = os.getenv("GUILD_ID")
    moderator_role = os.getenv("MODERATOR_ROLE")

    @commands.slash_command(name="urban", guild_ids=[int(guild_id)])
    async def urban_dictionary(self, ctx: discord.ApplicationContext, query: str):
        await ctx.defer()
        try:
            result = self.urban.search(query)
        except IndexError:
            await ctx.respond(
                f"No definition found for term: {query}",
                allowed_mentions=discord.AllowedMentions.none(),
            )
            return

        body = f"**Definition:**\n{result.definition}\n\n**Example:\n**{result.example}"
        written_on = result.written_on[:10]

        urban_embed = discord.Embed(
            title=f"Urban Dictionary: {query}",
            color=discord.Color.blue(),
            description=body,
            url=result.permalink,
        )
        urban_embed.set_author(
            name=str(ctx.author), icon_url=ctx.author.avatar.url
        )
        urban_embed.set_footer(
            text=f"By {result.author} on {written_on}\n👍 {result.thumbs_up} | 👎 {result.thumbs_down}"
        )

        if len(urban_embed) > 6000:
            urban_embed.description = urban_embed.description[:5900] + "..."
            await ctx.respond(
                "This definition is too big, so some of the contents were hidden",
                embed=urban_embed,
            )
        else:
            await ctx.respond(embed=urban_embed)

def setup(client):
    client.add_cog(urban(client))
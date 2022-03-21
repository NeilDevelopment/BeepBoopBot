import discord
from discord.ext import commands
import os
from discord.commands import \
    slash_command

class Snipe(commands.Cog):

    deleted_msgs = {}
    edited_msgs = {}
    snipe_limit = 7

    guild_id = os.getenv("GUILD_ID")

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        ch_id = message.channel.id

        if not message.author.bot:
            if message.content:
                if ch_id not in self.deleted_msgs:
                    self.deleted_msgs[ch_id] = []

                self.deleted_msgs[ch_id].append(message)

            if len(self.deleted_msgs[ch_id]) > self.snipe_limit:
                self.deleted_msgs[ch_id].pop(0)

    @commands.Cog.listener()
    async def on_message_edit(
        self, before: discord.Message, after: discord.Message
    ):
        ch_id = before.channel.id

        if not before.author.bot:
            if before.content and after.content:
                if ch_id not in self.edited_msgs:
                    self.edited_msgs[ch_id] = []

                self.edited_msgs[ch_id].append((before, after))

            if len(self.edited_msgs[ch_id]) > self.snipe_limit:
                self.edited_msgs[ch_id].pop(0)

    @commands.slash_command(guild_ids=[int(guild_id)])
    async def snipe(self, ctx, limit: int = 1):

        if limit > self.snipe_limit:
            await ctx.respond(
                f"Maximum snipe limit is {self.snipe_limit}", ephemeral=True
            )
            return

        try:
            msgs: list[discord.Message] = self.deleted_msgs[ctx.channel.id][
                ::-1
            ][:limit]
            snipe_embed = discord.Embed(title="Message Snipe", color=discord.Color.blue())

            if msgs:
                await ctx.defer()
                top_author: discord.Member = await ctx.bot.get_or_fetch_user(
                    msgs[0].author.id
                )

                if top_author:
                    if avatar := top_author.avatar:
                        snipe_embed.set_thumbnail(url=avatar.url)

            for msg in msgs:
                snipe_embed.add_field(
                    name=str(msg.author), value=msg.content, inline=False
                )

            await ctx.respond(embed=snipe_embed)

        except KeyError:
            await ctx.respond(
                "There's nothing to snipe here...", ephemeral=True
            )

    @commands.slash_command(name="editsnipe",guild_ids=[int(guild_id)])
    async def edit_snipe(
        self, ctx, limit: int = 1
    ):


        if limit > self.snipe_limit:
            await ctx.respond(
                f"Maximum snipe limit is {self.snipe_limit}", ephemeral=True
            )
            return

        try:
            msgs = self.edited_msgs[ctx.channel.id][::-1][:limit]
            editsnipe_embed = discord.Embed(title="Edit Snipe", color=discord.Color.blue())

            if msgs:
                await ctx.defer()
                top_author: discord.Member = await ctx.bot.get_or_fetch_user(
                    msgs[0][0].author.id
                )

                if top_author:
                    if avatar := top_author.avatar:
                        editsnipe_embed.set_thumbnail(url=avatar.url)

            for msg in msgs:
                editsnipe_embed.add_field(
                    name=str(msg[0].author),
                    value=f"{msg[0].content} **-->** {msg[1].content}",
                    inline=False,
                )

            await ctx.respond(embed=editsnipe_embed)

        except KeyError:
            await ctx.respond(
                "There's nothing to snipe here...", ephemeral=True
            )


def setup(bot):
    bot.add_cog(Snipe())
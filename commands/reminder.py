import discord, os, datetime, asyncio
from discord.ext import commands
from discord.commands import \
    slash_command, Option
from data import Data
from utils import str_time_to_timedelta
import uuid

class avatar(commands.Cog):

    reminders_loaded = False
    def __init__(self, client):
        self.client = client

    guild_id = os.getenv("GUILD_ID")
    moderator_role = os.getenv("MODERATOR_ROLE")

    async def reminder(
        self,
        reminder_id: str,
        user: discord.User,
        seconds: float,
        reminder_msg: str,
        reminder_start_time: datetime,
    ):
        await asyncio.sleep(seconds)
        rem_start_time_str = f"<t:{int(reminder_start_time.timestamp())}:R>"
        try:
            await user.send(
                f"You asked me to remind you {rem_start_time_str} about:"
                f"\n*{reminder_msg}*",
                allowed_mentions=discord.AllowedMentions.none(),
            )
        except discord.Forbidden:
            pass
        Data.delete_reminder_entry(reminder_id)

    async def load_reminder(self, reminder_data: list):
        reminder_id = reminder_data[0]
        user = await self.bot.fetch_user(reminder_data[1])
        reminder_msg = reminder_data[2]
        started_at = datetime.strptime(reminder_data[3], Data.datetime_format)

        now = datetime.now()
        due_at = datetime.strptime(reminder_data[4], Data.datetime_format)

        asyncio.create_task(
            self.reminder(
                reminder_id,
                user,
                (due_at - now).total_seconds(),
                reminder_msg,
                started_at,
            )
        )

    async def load_pending_reminders(self):
        print("Loading pending reminders...")

        Data.c.execute("SELECT * FROM reminders")
        reminders = Data.c.fetchall()

        reminder_load_tasks = list(map(self.load_reminder, reminders))
        await asyncio.gather(*reminder_load_tasks)

        self.reminders_loaded = True  # TODO: Make this globally accessible
        print(f"Loaded {len(reminders)} pending reminders!")

    @commands.Cog.listener()
    async def on_ready(self):
        await self.load_pending_reminders()

    @commands.slash_command(guild_ids=[int(guild_id)])
    async def remind(
        self,
        ctx: discord.ApplicationContext,
        remind_time: str,
        message: str,
    ):
        """
        Set a reminder. Example: /remind 1d 2h 12m 5s make lunch (All time options are not required)
        """

        # Wait till bot finishes loading all reminders
        # Prevents duplicate reminders
        if not self.reminders_loaded:
            await ctx.respond(
                "The bot is starting up. Please try again in a few minutes."
            )
            return

        now = datetime.now()
        remind_timedelta = str_time_to_timedelta(remind_time)
        time_to_end = f"<t:{int((now + remind_timedelta).timestamp())}:R>"

        reminder_id = uuid.uuid4()
        Data.create_new_reminder_entry(
            reminder_id.hex,
            ctx.author,
            message,
            now.strftime(Data.datetime_format),
            (now + remind_timedelta).strftime(Data.datetime_format),
        )

        asyncio.create_task(
            self.reminder(
                reminder_id.hex,
                ctx.author,
                remind_timedelta.total_seconds(),
                message,
                now,
            )
        )

        await ctx.respond(
            f"Reminder set for {time_to_end} about:\n{message}",
            allowed_mentions=discord.AllowedMentions.none(),
        )


def setup(client):
    client.add_cog(avatar(client))
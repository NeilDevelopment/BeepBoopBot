import os
import sqlite3
import uuid
from typing import Union


class Data:
    data_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(data_dir, "db.sqlite3")
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    datetime_format = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def create_tables(cls):
        cls.c.execute(
            """
            CREATE TABLE IF NOT EXISTS "guilds" (
                "id"	INTEGER NOT NULL UNIQUE,
                "infractions"	TEXT DEFAULT '[]',
                "mute_role"	INTEGER DEFAULT NULL,
                "activated_automod"	TEXT DEFAULT '[]',
                "welcome_message"	TEXT DEFAULT NULL,
                "leave_message"	TEXT DEFAULT NULL,
                "welcome_channel"	TEXT DEFAULT NULL,
                "leave_channel"	TEXT DEFAULT NULL,
                "auto_role"	TEXT DEFAULT NULL,
                "prefix"	TEXT DEFAULT '!',
                "auto_responses"	TEXT DEFAULT '{}',
                "clear_cap"	INTEGER DEFAULT NULL,
                PRIMARY KEY("id")
            )
            """
        )

        cls.c.execute(
            """
            CREATE TABLE IF NOT EXISTS "webhooks" (
                "channel_id"	INTEGER NOT NULL,
                "webhook_url"	TEXT
            )
            """
        )

        cls.c.execute(
            """
            CREATE TABLE IF NOT EXISTS "afks" (
                "user_id"	INTEGER NOT NULL UNIQUE,
                "afk_reason"	TEXT NOT NULL,
                PRIMARY KEY("user_id")
            )
            """
        )

        cls.c.execute(
            """
            CREATE TABLE IF NOT EXISTS "reminders" (
                "id"	TEXT NOT NULL UNIQUE,
                "user_id"	INTEGER,
                "reminder_msg"	TEXT,
                "start_time"	DATETIME,
                "due"	DATETIME,
                PRIMARY KEY("id")
            )
            """
        )

        cls.c.execute(
            """
            CREATE TABLE IF NOT EXISTS "reaction_roles" (
                "id"	TEXT NOT NULL UNIQUE,
                "guild_id"	INTEGER NOT NULL,
                "channel_id"	INTEGER,
                "message_id"	INTEGER,
                "emoji"	TEXT,
                "role_id"	INTEGER,
                PRIMARY KEY("id")
            )
            """
        )

        cls.conn.commit()

    # Guild Data
    @classmethod
    def create_new_guild_data(cls, guild):
        cls.c.execute(
            """INSERT INTO guilds VALUES
            (:guild_id, '[]', NULL, '[]', NULL, NULL, NULL, NULL, NULL, 's!', '{}', NULL)
            """,
            {"guild_id": guild.id},
        )
        cls.conn.commit()
        print(f"Created data entry for guild {guild.name}")

    @classmethod
    def check_guild_entry(cls, guild):
        cls.c.execute(
            "SELECT * FROM guilds WHERE id = :guild_id", {"guild_id": guild.id}
        )
        guild_data = cls.c.fetchone()

        if guild_data is None:
            cls.create_new_guild_data(guild)

    # Webhook Data
    @classmethod
    def create_new_webhook_data(cls, channel, webhook_url):
        cls.c.execute(
            "INSERT INTO webhooks VALUES (:channel_id, :webhook_url)",
            {"channel_id": channel.id, "webhook_url": webhook_url},
        )
        cls.conn.commit()
        print(f"Created webhook entry for channel with ID {channel.id}")

    @classmethod
    def webhook_entry_exists(cls, channel) -> Union[str, bool]:
        cls.c.execute(
            "SELECT webhook_url FROM webhooks WHERE channel_id = :channel_id",
            {"channel_id": channel.id},
        )
        webhook_data = cls.c.fetchone()

        if webhook_data:
            return webhook_data[0]

        return False

    # AFK Data
    @classmethod
    def create_new_afk_data(cls, user, afk_reason):
        cls.c.execute(
            "INSERT INTO afks VALUES (:user_id, :afk_reason)",
            {"user_id": user.id, "afk_reason": afk_reason},
        )
        cls.conn.commit()
        print(f"Created AFK entry for user {user}")

    @classmethod
    def delete_afk_data(cls, user):
        cls.c.execute(
            "DELETE FROM afks WHERE user_id = :user_id", {"user_id": user.id}
        )
        cls.conn.commit()
        print(f"Deleted AFK entry for user {user}")

    @classmethod
    def afk_entry_exists(cls, user) -> bool:
        cls.c.execute(
            "SELECT afk_reason FROM afks WHERE user_id = :user_id",
            {"user_id": user.id},
        )
        afk_data = cls.c.fetchone()
        return afk_data is not None

    # Reminders Data
    @classmethod
    def create_new_reminder_entry(
        cls, reminder_id, user, msg, start_time, due
    ):
        cls.c.execute(
            "INSERT INTO reminders VALUES (:id, :user_id, :msg, :start_time, :due)",
            {
                "id": reminder_id,
                "user_id": user.id,
                "msg": msg,
                "start_time": start_time,
                "due": due,
            },
        )
        cls.conn.commit()
        print(f"Created reminder for user {user}")

    @classmethod
    def delete_reminder_entry(cls, reminder_id):
        cls.c.execute(
            "DELETE FROM reminders WHERE id = :id", {"id": reminder_id}
        )
        cls.conn.commit()
        print(f"Deleted reminder with ID {reminder_id}")

    # Reaction Roles Data
    @classmethod
    def create_new_reaction_role_entry(
        cls, guild, channel, message, emoji, role
    ):
        rr_id = uuid.uuid4().hex

        cls.c.execute(
            "INSERT INTO reaction_roles VALUES (:id, :guild_id, :channel_id, :message_id, :emoji, :role_id)",
            {
                "id": rr_id,
                "guild_id": guild.id,
                "channel_id": channel.id,
                "message_id": message.id,
                "emoji": emoji,
                "role_id": role.id,
            },
        )
        cls.conn.commit()
        print(f"Created reaction role with ID {rr_id}")

    @classmethod
    def delete_reaction_role_entry(cls, rr_id: str):
        cls.c.execute(
            "DELETE FROM reaction_roles WHERE id = :id",
            {"id": rr_id},
        )
        cls.conn.commit()
        print(f"Deleted reaction role with ID {rr_id}")
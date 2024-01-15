import asyncio
import logging
import logging.handlers
import sys
from typing import List, Optional

import discord
import openai
from aiohttp import ClientSession
from discord.ext import commands
from motor import motor_asyncio

from config.config import Config
from database import DiscordDatabase
from utilities.logger import setup_logger

sys.stdin.reconfigure(encoding="utf-8")
sys.stdout.reconfigure(encoding="utf-8")
config = Config()

bot_token = config.token

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
logger = setup_logger()
logger.setLevel(logging.INFO)
log = logging.getLogger()

debug = any('debug' in arg.lower() for arg in sys.argv) or config.debug_mode
if debug:
    log.info("Debug mode is on")
    bot_token = config.debug_token


class Bot(commands.Bot):
    def __init__(self, *args, initial_extensions: List[str],
                 db_client: motor_asyncio.AsyncIOMotorClient,
                 web_client: ClientSession,
                 testing_guild_id: Optional[int] = None,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.db_client = db_client
        self.web_client = web_client
        self.testing_guild_id = testing_guild_id
        self.initial_extensions = initial_extensions
        self.config = config
        self.log = logging.getLogger()
        self.debug = debug

    async def setup_hook(self) -> None:
        self.remove_command('help')

        for extension in self.initial_extensions:
            self.log.info(f"Loading {extension}")
            try:
                await self.load_extension(extension)
            except Exception as e:
                self.log.error(f"Failed to load extension {extension}. Error: {e}")

        if self.testing_guild_id and config.sync_testing_guild:
            self.log.info(f"Syncing commands for guild {self.testing_guild_id}")
            guild = discord.Object(self.testing_guild_id)
            self.tree.copy_global_to(guild=guild)
            # await self.tree.sync(guild=guild)
            self.log.info(f"Synced commands for guild {self.testing_guild_id}")


async def start_bot():

    async with ClientSession() as client:
        discord_db = DiscordDatabase(config.mongo_uri, config.database_name, config.user_collection_name,
                                     config.guild_collection_name)
        async with Bot(commands.when_mentioned, db_client=discord_db, web_client=client,
                       initial_extensions=config.initial_extensions, intents=intents,
                       testing_guild_id=config.testing_guild_id) as bot:
            await bot.start(config.token)

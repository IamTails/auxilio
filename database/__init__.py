import logging
from datetime import datetime

import motor.motor_asyncio
from models.user import User


class DiscordDatabase:
    def __init__(self, mongo_uri, database_name, user_collection_name, guild_collection_name):
        self.mongo_uri = mongo_uri
        self.database_name = database_name
        self.guild_collection_name = guild_collection_name
        self.user_collection_name = user_collection_name
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.mongo_uri)
        self.guild_collection = self.client[self.database_name][self.guild_collection_name]
        self.user_collection = self.client[self.database_name][self.user_collection_name]
        self.log = logging.getLogger()

    #############################################
    # User operations                           #
    #############################################
    async def get_user(self, guild_id: int, user_id: int):
        user = await self.user_collection.find_one(
            {
                'guild_id': int(guild_id),
                'user_id': int(user_id)
            }
        )

        if user:
            return User.from_existing(self, user)
        else:
            user = User.create(self, user_id, guild_id)
            await user.save(guild_id)
            return user

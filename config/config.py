import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from ..env file


class Config:
    def __init__(self):
        self.token = os.getenv('DISCORD_TOKEN',
                               "")  # Use environment variable as token
        # Use environment variable as debug_mode
        self.debug_mode = os.getenv('DEBUG_MODE', False)
        self.debug_token = os.getenv('DEBUG_TOKEN',
                                     "")  # Use environment variable as debug_token
        self.sync_testing_guild = os.getenv('SYNC_TESTING_GUILD',
                                            False)  # Use environment variable as sync_testing_guild_id
        # Use environment variable as mongo_uri
        self.mongo_uri = os.getenv('MONGO_URI', "")
        # Use environment variable as database_name
        self.database_name = os.getenv('DATABASE_NAME', "")
        self.user_collection_name = os.getenv('USER_COLLECTION_NAME',
                                              "users")  # Use environment variable as user_collection_name
        self.guild_collection_name = os.getenv('GUILD_COLLECTION_NAME',
                                               "guilds")  # Use environment variable as guild_collection_name
        self.testing_guild_id = os.getenv('TESTING_GUILD_ID',
                                          "")  # Use environment variable as testing_guild_id
        self.initial_extensions = ['modules.cogs.ping', 'modules.cogs.dev']  # List of initial extensions

        # Use environment variable as error_webhook
        self.error_webhook = os.getenv('ERROR_WEBHOOK', "")

    def get_token(self, debug=False):  # Get token
        if self.debug_mode or debug:  # If debug_mode is True
            return self.debug_token  # Return debug_token
        return self.token  # Return token

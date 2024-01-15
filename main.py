import asyncio

from api.serve import start_server
from bot.auxilio import start_bot, log


async def main():
    await asyncio.gather(start_server(), start_bot()
    )


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    except Exception as e:
         log.error(f"An unexpected error occurred: {e}")

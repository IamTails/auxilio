import asyncio
from aiohttp import web

API_KEY = ""


async def ping(request):
    api_key = request.headers.get('X-API-Key')
    if api_key != API_KEY:
        return web.json_response({'error': 'Invalid API key'}, status=401)
    return web.json_response({'ping': "pong"})


async def start_server():
    app = web.Application()
    app.router.add_get('/', ping)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    print('Server started at http://localhost:8080')



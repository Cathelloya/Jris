from aiohttp import web
from collections.abc import Callable

event_handlers: dict[str, Callable[[dict[str]], []]] = {}


async def handle(request):
    json: dict[str] = await request.json()

    handler = event_handlers.get(json.get('post_type'))
    if handler is not None:
        await handler(json)

    return web.Response(text="OK")


app = web.Application()
app.add_routes([web.post('/', handle)])

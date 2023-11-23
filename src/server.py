from aiohttp import web


async def handle(request):
    json = await request.json()

    print(json)

    return web.Response(text="OK")


app = web.Application()
app.add_routes([web.post('/', handle)])

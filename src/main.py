from aiohttp import web
from dotenv import load_dotenv

load_dotenv()


async def handle(request):
    return web.Response(text="Hello, world!.")


app = web.Application()
app.add_routes([web.get("/", handle)])

if __name__ == "__main__":
    web.run_app(app)

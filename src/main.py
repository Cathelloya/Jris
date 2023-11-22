from aiohttp import web
from dotenv import load_dotenv
import os

load_dotenv()


async def handle(request):
    return web.Response(text="Hello, world!")


app = web.Application()
app.add_routes([web.get("/", handle)])

if __name__ == "__main__":
    web.run_app(app, port=os.getenv("LISTEN_PORT"))

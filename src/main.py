import server
from aiohttp import web
import os

if __name__ == '__main__':
    web.run_app(server.app, port=int(os.getenv('SERVER_PORT') or "5701"))

import server
import client
from aiohttp import web
import os


async def handle_message(data: dict[str]):
    if data['sub_type'] == 'friend':
        msg = data['raw_message']
        user_id = data['user_id']
        await client.send_message({
            "user_id": user_id,
            "message": msg
        })


server.event_handlers['message'] = handle_message

if __name__ == '__main__':
    web.run_app(server.app, port=int(os.getenv('SERVER_PORT') or "5701"))

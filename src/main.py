import server
import client
import reply_dict
from aiohttp import web
import os


async def handle_message(data: dict[str]):
    if data['message_type'] == 'private':
        msg = reply_dict.reply_to(data['raw_message']) or "我听不懂。"
        user_id = data['user_id']

        await client.send_message({
            "user_id": user_id,
            "message": msg
        })

    elif data['message_type'] == 'group':
        user_msg: str = data['raw_message']
        if not user_msg[:5].lower() == 'jris ':
            return

        msg = reply_dict.reply_to(user_msg[5:]) or "我听不懂。"
        group_id = data['group_id']

        await client.send_message({
            "group_id": group_id,
            "message": msg
        })


server.event_handlers['message'] = handle_message

if __name__ == '__main__':
    web.run_app(server.app, port=int(os.getenv('SERVER_PORT') or "5701"))

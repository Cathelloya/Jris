from nakuru import CQHTTP, GroupMessage, FriendMessage
from dotenv import load_dotenv
import os

load_dotenv()


app = CQHTTP(
    host=os.getenv("HOST") or "127.0.0.1",
    port=os.getenv("PORT") or 5701,
    http_port=os.getenv("HTTP_PORT") or 5700,
    token=os.getenv("TOKEN"),
)


@app.receiver("FriendMessage")
async def _(app: CQHTTP, source: FriendMessage):
    msg = source.raw_message

    if msg == "在吗":
        return await app.sendFriendMessage(
            user_id=source.user_id,
            message="在的",
        )


@app.receiver("GroupMessage")
async def _(app: CQHTTP, source: GroupMessage):
    if not source.raw_message[:5].lower() == "jris ":
        return

    msg = source.raw_message[5:]

    if msg == "摸摸头":
        return await app.sendGroupMessage(
            group_id=source.group_id,
            message="摸摸头",
        )


if __name__ == "__main__":
    app.run()

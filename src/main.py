from nakuru import CQHTTP, GroupMessage, FriendMessage
from dotenv import load_dotenv
from .reply_dict import reply_to
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

    await app.sendFriendMessage(
        user_id=source.user_id,
        message=reply_to(msg) or "我不知道你在说什么呢。",
    )


@app.receiver("GroupMessage")
async def _(app: CQHTTP, source: GroupMessage):
    if not source.raw_message[:5].lower() == "jris ":
        return

    msg = source.raw_message[5:]

    await app.sendGroupMessage(
        group_id=source.group_id,
        message=reply_to(msg) or "我不知道你在说什么呢。",
    )


if __name__ == "__main__":
    app.run()

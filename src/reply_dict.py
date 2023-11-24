import asyncio
import random
import re
from typing import Union, Callable, Awaitable
import ai_models

ReplyDictValue = Union[str, list[str], Callable[[str, list[str]], Awaitable[str]]]
ReplyDict = dict[str, ReplyDictValue]

reply_dict: ReplyDict = {
    r"^不要(.+)": "放心，我不会{}",
    r"^你?在吗\??": "在的",
    r"^摸摸头$": ["好捏！", "不去追求现实中实际存在的人，而来找机器人寻求安慰，难道不是贯彻了荒诞主义吗？"],
    r"(.+)在哪里\??": ["{0}在{0}附近", "我不知道{}在哪里"],
    r"^可以(.+)吗": ["当然可以{}", "打咩，绝对不可以{}!"],
    r".+": lambda m, _: ai_models.instruct_llm(m)
}


async def reply_to(msg: str) -> str:
    msg = msg.strip()

    reply: ReplyDictValue | None = None
    matches: list[str] = []

    for k, v in reply_dict.items():
        new_matches = re.match(k, msg)
        if new_matches:
            reply = v
            matches.extend(new_matches.groups())
            break

    if reply is None:
        return "不知该如何回答呢..."

    if callable(reply):
        return await reply(msg, matches)

    if isinstance(reply, list):
        return random.choice(reply).format(*matches)

    try:
        return reply.format(*matches)
    except IndexError:
        return "我出错啦！"


async def run_tests():
    print(await reply_to("在吗?"))
    print(await reply_to("你在吗"))
    print(await reply_to("他在吗?"))
    print(await reply_to("不要回复"))
    print(await reply_to("摸摸头"))
    print(await reply_to("你在哪里?"))
    print(await reply_to(""))


if __name__ == '__main__':
    asyncio.run(run_tests())

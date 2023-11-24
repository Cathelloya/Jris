import asyncio
import random
import re
from typing import Union, Callable, Awaitable
import ai_models
import utils

ReplyFunc = Callable[[str, list[str]], Union[Awaitable[str], str]]
ReplyDictValue = Union[str, list[str], ReplyFunc, list[ReplyFunc]]
ReplyDict = dict[str, ReplyDictValue]

reply_dict: ReplyDict = {
    r"^不要(.+)": "放心，我不会{}",
    r"^你?在吗\??": "在的",
    r"^摸摸头$": ["好捏！", "不去追求现实中实际存在的人，而来找机器人寻求安慰，难道不是贯彻了荒诞主义吗？"],
    r"(.+)在哪里\??": ["{0}在{0}附近", "我不知道{}在哪里"],
    r"^可以(.+)吗": ["当然可以{}", "打咩，绝对不可以{}!"],
    r"^画(.+)": [
        lambda _, m: utils.encode_cqcode({
            "_type": "image",
            "url": ai_models.get_text_to_image_url(m[0].strip())}),
        "不想画了，放过我吧"
    ],
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

    if isinstance(reply, list):
        reply = random.choice(reply)

    if reply is None:
        return "不知该如何回答呢..."

    if callable(reply):
        result = reply(msg, matches)
        if isinstance(result, Awaitable):
            return await result
        else:
            return result

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
    print(await reply_to("画 a cat"))


if __name__ == '__main__':
    asyncio.run(run_tests())

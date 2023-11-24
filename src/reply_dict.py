import random
import re
from typing import Union

ReplyDictValue = Union[str, list[str]]
ReplyDict = dict[str, ReplyDictValue]

reply_dict: ReplyDict = {
    "^不要(.*)": "放心，我不会{}",
    r"^你?在吗\??": "在的",
    "^摸摸头$": ["好捏！", "不去追求现实中实际存在的人，而来找机器人寻求安慰，难道不是贯彻了荒诞主义吗？"],
    r"(.*)在哪里\??": ["{0}在{0}附近", "我不知道{}在哪里"],
    "^可以(.*)": ["当然可以{}", "打咩，绝对不可以{}!"]
}


def reply_to(msg: str) -> str | None:
    msg = msg.strip()

    reply: ReplyDictValue | None = None
    matches: list[str] = []

    for k, v in reply_dict.items():
        new_matches = re.match(k.format(*matches), msg)
        if new_matches:
            reply = v
            matches.extend(new_matches.groups())
            break

    if reply is None:
        return None

    if isinstance(reply, list):
        return random.choice(reply).format(*matches)

    try:
        return reply.format(*matches)
    except IndexError:
        return None


if __name__ == '__main__':
    print(reply_to("在吗?"))
    print(reply_to("你在吗"))
    print(reply_to("他在吗?"))
    print(reply_to("不要回复"))
    print(reply_to("摸摸头"))
    print(reply_to("你在哪里?"))

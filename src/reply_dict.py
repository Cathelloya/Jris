import random


reply_dict: dict[str, str | list[str]] = {
    "在吗": "在的",
    "摸摸头": ["好捏！", "不去追求现实中实际存在的人，而来找机器人寻求安慰，难道不是贯彻了荒诞主义吗？"],
}


def reply_to(msg: str) -> str | None:
    msg = msg.strip()
    reply = reply_dict.get(msg)

    if reply is None:
        return None

    if isinstance(reply, list):
        return random.choice(reply)

    return reply

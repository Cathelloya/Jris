import os
from aiohttp import ClientSession
from typing import Any

CLIENT_PORT = os.getenv("CLIENT_PORT")
if CLIENT_PORT is None:
    CLIENT_PORT = "5700"

BASE_URL = "http://localhost:" + CLIENT_PORT


async def send_data(path: str, data: dict[str, Any]) -> int:
    async with ClientSession() as session:
        async with session.post(BASE_URL + path, json=data) as response:
            return response.status


async def send_message(data: dict[str, Any]):
    if await send_data("/send_msg", data) != 200:
        print("Error: failed to send message")

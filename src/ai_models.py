from aiohttp import ClientSession
import asyncio


async def instruct_llm(instruction: str) -> str | None:
    url = "https://ai.ihack.uk/api/run/@cf/mistral/mistral-7b-instruct-v0.1"
    prompt = '<s>[INST] ' + instruction.strip() + ' [/INST]'
    async with ClientSession() as session:
        async with session.get(url, params={"prompt": prompt}) as response:
            json = await response.json()
            if response.ok:
                return json['result']['response']
            else:
                print("Error:", json)
                return None

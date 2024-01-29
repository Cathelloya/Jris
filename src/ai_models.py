from aiohttp import ClientSession
import urllib.parse
import asyncio


async def instruct_llm(instruction: str) -> str | None:
    url = "https://ai.ihack.uk/api/run/@cf/mistral/mistral-7b-instruct-v0.1"
    prompt = '<s>[INST] 你是聊天机器人 Jris [/INST]</s><s>[INST] ' + instruction.strip() + ' [/INST]'
    async with ClientSession() as session:
        async with session.post(url, json={"prompt": prompt}) as response:
            json = await response.json()
            if response.ok:
                return json['result']['response'].strip()
            else:
                print("Error:", json)
                return None


def get_text_to_image_url(prompt: str) -> str:
    url = 'https://ai.ihack.uk/api/run/@cf/stabilityai/stable-diffusion-xl-base-1.0?prompt='
    return url + urllib.parse.quote(prompt, safe='')


if __name__ == '__main__':
    print(asyncio.run(instruct_llm("Who are you")))

import asyncio
import os
from urllib.parse import urlparse
from pathlib import Path
from astrometry_net_client import Session
from astrometry_net_client import FileUpload
from dotenv import dotenv_values
import aiohttp
import requests
import datetime




async def star(url_image: str):
    # 获取当前时间
    current_time = datetime.datetime.now()

    # 格式化时间为字符串，作为文件名
    formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")

    config = dotenv_values("../.env")  

    # Initial Session
    s = Session(api_key=config["API_astrometry_net"])

    # 下载图像并保存为本地文件
    local_filename = f'./tmp/local_image_{formatted_time}.jpg'  # 添加时间戳到文件名
    response = requests.get(url_image)
    with open(local_filename, 'wb') as f:
        f.write(response.content)

    # 初始化 FileUpload
    upl = FileUpload(local_filename, session=s)

    # 提交文件并等待处理完成
    submission = upl.submit()
    submission.until_done()

    # 获取第一个 job
    job = submission.jobs[0]

    jobid = str(job.id)
    addr = "http://nova.astrometry.net/annotated_display/" + jobid

    # 等待 job 完成
    job.until_done()

    # 删除本地文件
    os.remove(local_filename)
    return addr

async def main():
    url_image = 'https://c2cpicdw.qpic.cn/offpic_new/2016741487//2016741487-3567923580-B88EFE28A92703A92CD1B21181ADCA5C/0?term=2&amp;is_origin=0'

    result = await star(url_image)
    print(f'Astrometry.net result: {result}')

if __name__ == "__main__":
    asyncio.run(main())

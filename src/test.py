import datetime 
from dotenv import dotenv_values
import requests

# 获取当前时间
current_time = datetime.datetime.now()

# 格式化时间为字符串，作为文件名
formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")

config = dotenv_values("../.env")  

url_image = 'https://c2cpicdw.qpic.cn/offpic_new/2016741487//2016741487-3567923580-B88EFE28A92703A92CD1B21181ADCA5C/0?term=2&amp;is_origin=0'

# 下载图像并保存为本地文件
local_filename = f'./tmp/local_image_{formatted_time}.jpg'  # 添加时间戳到文件名

response = requests.get(url_image)
with open(local_filename, 'wb') as f:
    f.write(response.content)

import requests
import time


response = requests.get('https://ai.ihack.uk/instruct')

# 定义目标URL
url = 'https://ai.ihack.uk/instruct'

# 设置请求头
headers = {
    'Content-Type': 'application/json',
}

# 定义请求体
data = {
    'prompt': '你好',
}

# 发送生成文本的请求
response_generate = requests.post(f'{url}/api/run/@cf/mistral/mistral-7b-instruct-v0.1', json=data, headers=headers, stream=True)

# 打印生成的文本
for line in response_generate.iter_lines():
    if line:
        print(line.decode('utf-8'))

# 添加指令
data['prompt'] = '[INST] 你好 [/INST]'
response_instruction = requests.post(f'{url}/api/run/@cf/mistral/mistral-7b-instruct-v0.1', json=data, headers=headers, stream=True)

# 打印生成的文本
for line in response_instruction.iter_lines():
    if line:
        print(line.decode('utf-8'))

# 等待10秒钟
time.sleep(10)

# 关闭请求
response_generate.close()
response_instruction.close()

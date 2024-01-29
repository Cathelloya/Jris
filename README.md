# Jris

Jris is a WIP QQ chatbot written in Python.

## Configuration

1. Install Python 3.8 or above.
2. Install dependencies with `pip3 install -r requirements.txt`.
3. To use Starry sky identification, you need to sign in https://nova.astrometry.net/ to get an API key, and set it in ``/src/star.py``
   
    ```python
    def star(url_image: str):
    # 初始化 Session
    s = Session(api_key='Your API key')

    # 下载图像并保存为本地文件
    local_filename = './tmp/local_image.jpg'
    response = requests.get(url_image)
    with open(local_filename, 'wb') as f:
        f.write(response.content)
    ```


## Usage

1. (Optional) Set up `go-cqhttp` in `cqhttp` folder (However, it is recommended to run `go-cqhttp` somewhere else).
2. Configure `.env` according to `.env.example`, otherwise the default values will be used.
3. Run `python3 src/main.py` to start the bot.

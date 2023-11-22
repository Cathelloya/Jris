from nakuru import CQHTTP
from dotenv import load_dotenv
import os

load_dotenv()


app = CQHTTP(
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    http_port=os.getenv("HTTP_PORT"),
    token=os.getenv("TOKEN"),
)

app.run()

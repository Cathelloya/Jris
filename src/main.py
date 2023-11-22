from nakuru import CQHTTP
from dotenv import load_dotenv
import os

load_dotenv()


app = CQHTTP(
    host=os.getenv("HOST") or "127.0.0.1",
    port=os.getenv("PORT") or 5701,
    http_port=os.getenv("HTTP_PORT") or 5700,
    token=os.getenv("TOKEN"),
)

if __name__ == "__main__":
    app.run()

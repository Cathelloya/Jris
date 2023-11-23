import os

CLIENT_PORT = os.getenv("CLIENT_PORT")
if CLIENT_PORT is None:
    CLIENT_PORT = "5700"

BASE_URL = "http://localhost:" + CLIENT_PORT

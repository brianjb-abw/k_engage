import os
import requests
from dotenv import load_dotenv
import jwt

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("SECRET")
EMAIL = os.getenv("EMAIL")

full_token = os.getenv("FULL_TOKEN")





inner_token = full_token.split(".", -1)[1]


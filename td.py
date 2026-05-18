# 
# Working file for token decoding.
# Not part of app's main routine.
#

import os
import requests
from dotenv import load_dotenv
import jwt

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("SECRET")

bearer = os.getenv("BEARER")

payload = bearer.split(".", -1)[1]

print(payload)
import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("SECRET")
EMAIL = os.getenv("EMAIL")

url = "https://graphql.klutchcard.com/graphql"

payload = {
    "query": """
        mutation($clientId: String, $secretKey: String) {
            createSessionToken(clientId: $clientId, secretKey: $secretKey)
        }
    """,
    "variables": {
        "clientId": CLIENT_ID,
        "secretKey": SECRET
    }
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers, json=payload)
data = response.json()

print(data)

if "errors" in data:
    print("\nAuth failed:")
    for err in data["errors"]:
        print(" ", err.get("message"))
elif "data" in data:
    session_token = data["data"]["createSessionToken"]
    print(f"\nSession token: {session_token}")

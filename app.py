import os
import requests
import dotenv
from k_payloads import k_payloads 
from cards import cards

dotenv.load_dotenv(override=True)

BEARER = os.getenv("BEARER")

url = "https://graphql.klutchcard.com/graphql"

headers = {
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json"
}


def get_token():
    CLIENT_ID = os.getenv("CLIENT_ID")
    SECRET = os.getenv("SECRET")

    del headers["Authorization"]
    f_dotenv = dotenv.find_dotenv()

    payload = k_payloads["get_token"]
    payload["variables"]["clientId"] = CLIENT_ID
    payload["variables"]["secretKey"] = SECRET

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    print(data)
    new_sess_token = data["data"]["createSessionToken"]
    print(f"new token {new_sess_token}")

    os.environ["BEARER"] = new_sess_token
    print(f"new env var 'BEARER' {os.environ["BEARER"]}")
    dotenv.set_key(f_dotenv, "BEARER", os.environ["BEARER"])
    dotenv.load_dotenv(override=True)

    headers["Authorization"] = data["data"]["createSessionToken"]
    print(f"headers {headers}")

def get_balance():
    payload = k_payloads["bal"]

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    print(data)
    print(f"\n\n    Balance:  . . . . . . . .   $ {data["data"]["account"]["revolvingLoan"]["balance"] * -1}\n\n")

def get_cards():
    payload = k_payloads["card_list"]

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    cards = data['data']['cards']
    card_ct = 0

    print(f"\n\n--- CARDS ---\n")
    for card in cards:
        if card['status'] != "TERMINATED":
            print(f"{card['lastFour']}\t\t{card['name']:12}\t{card['status']}\n")
            card_ct += 1

    print(f"\nrun complete: {card_ct} cards processed")

def get_trans():
    payload = k_payloads["trx_list"]
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    t_list = data['data']['transactions']

    print(f"\n\n*** TRANSACTIONS ***\n--------------------\n")
    for t in t_list:
        print(f"{t['transactionDate']}")
        if t['card']:
            print(f"  card:    {t['merchantName']} - {cards[t['card']['id']]['last_4']}")
        else:
            print(f"  card:    {t['merchantName']}")
        print(f"  amt:     {t['amount']:>10,.2f}")
        print(f"  status:  {t['transactionStatus'].lower()}\n")

# MAIN ROUTINE

prompt = "\n\n\nSelect task (T = token, B = balance, CL = card list, XL = transaction list, Q = quit): "

while True:
    curr_task = input(prompt)
    curr_task = curr_task.upper()

    if curr_task == "T":
        get_token()
        BEARER = os.getenv("BEARER")
        print(f"bearer var: {BEARER}")
    elif curr_task == "B":
        get_balance()
        print(cards["1234"])
    elif curr_task == "CL":
        get_cards()
    elif curr_task == "XL":
        get_trans()
    elif curr_task == "Q":
        print("\n As you wish, exiting ...")
        break
    else:
        print("\n** ERR: invalid task, exiting ...")
        break


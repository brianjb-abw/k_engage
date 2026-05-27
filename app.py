import os
import requests
import dotenv
from datetime import datetime, timedelta
from k_payloads import k_payloads 
from cards import cards


f_dotenv = dotenv.find_dotenv()
dotenv.load_dotenv(override=True)

p_url = "https://graphql.klutchcard.com/graphql"
sb_url = "https://sandbox.klutchcard.com/graphql"

# ----- ACTIVE URL -----
url = p_url

# ----- STD HEADERS -----
headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {os.getenv('BEARER')}"
}

# ----- TOKEN EXP -----
if os.getenv('TOKEN_EXP') == '':
    token_exp = datetime.now() - timedelta(minutes=60)
    dotenv.set_key(f_dotenv, 'TOKEN_EXP', datetime.strftime(token_exp, '%Y-%m-%d %H:%M:%S.%f'))
    dotenv.load_dotenv(override=True)
else:
    token_exp = datetime.strptime(os.getenv('TOKEN_EXP'), '%Y-%m-%d %H:%M:%S.%f')



def get_token():
    print("running get_token")
    headers.pop('Authorization')

    payload = k_payloads['get_token']
    payload['variables'] = {
        'clientId': os.getenv('API_KEY'),
        'secretKey': os.getenv('SECRET')
    }

    response = requests.post(url, headers=headers, json=payload)
    print(response)
    data = response.json()

    new_sess_token = data['data']['createSessionToken']

    token_exp = datetime.now() + timedelta(minutes=50)
    print(datetime.strftime(token_exp, '%Y-%m-%d %H:%M:%S.%f'))

    dotenv.set_key(f_dotenv, 'BEARER', new_sess_token)
    dotenv.set_key(f_dotenv, 'TOKEN_EXP', datetime.strftime(token_exp, '%Y-%m-%d %H:%M:%S.%f'))
    dotenv.load_dotenv(override=True)

    headers['Authorization'] = f"Bearer {os.getenv('BEARER')}"


def get_balance():
    payload = k_payloads['get_bal']

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
        # if card['status'] != "TERMINATED":
        print(card)
        
        card_ct += 1

    print(f"\nrun complete: {card_ct} cards processed")


def get_trans():
    payload = k_payloads["trx_list"]
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    t_list = data['data']['transactions']

    print(f"\n\n--- TRANSACTIONS ---\n")
    for t in t_list:
        print(t)


def get_trans_p():
    payload = k_payloads["trx_list_p"]
    tx_filter = {}
    tx_filter["transactionStatus"] = ["PENDING", "SETTLED"]
    payload["variables"]["filter"] = tx_filter
    payload["variables"]["sortOrder"] = "UPDATED_DATE_DESC"

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    print(data)



# ----- MENU SUBS -----
menu = {
    "T": get_token,
    "B": get_balance,
    "CL": get_cards,
    "XL": get_trans,
    "XP": get_trans_p
}



# ----- MAIN ----- #
def main():

    prompt = "\n\nSelect task: (T = token, B = balance, CL = card list, XL = transaction list, XP = transaction_list w params, Q = quit): "

    while True:
        curr_task = input(prompt)
        curr_task = curr_task.upper()

        # print("checking for end program menu choice")
        if curr_task == "Q":
            print("\n As you wish, exiting ...")
            break
        elif curr_task not in menu.keys():
            print("\n** ERR: invalid task, exiting ...")
            break

        # print("checking for stale token")
        if curr_task != "T":
            if ((token_exp - datetime.now()).total_seconds())/60 < 10:
                get_token()
        
        menu[curr_task]()





if __name__ == "__main__":
    main()
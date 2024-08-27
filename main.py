#"https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json"

import requests
def get_crypto_coin():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    return response.json()


get_crypto_response = get_crypto_coin()
get_user_coin = input("Plase enter a coin name")

for cryto in get_crypto_response:
    if cryto["currency"] == get_user_coin:
        print(f"{cryto['currency']} price is {cryto['price']}")

import requests

def get_info():
    responce = requests.get(url="https://yobit.net/api/3/info")

    with open ("info.txt", "w") as file:
        file.write(responce.text)

    return responce.text

def get_ticker(coin1 = "mana", coin2 = "usd"):
    #responce = requests.get(url="https://yobit.net/api/3/ticker/eth_btc-eth_usdt")
    responce = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}-btc_usdt")

    with open("ticker.txt", "w") as file:
        file.write(responce.text)

    return responce.text

def get_depth(coin1 = "mana", coin2 = "usd", limit = 150):
    #Информация о выставленных на продажу и покупку ордерах
    responce = requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

    with open("deps.txt", "w") as file:
        file.write(responce.text)

    #bids - списки с ордерами на покупку
    bids = responce.json()[f"{coin1}_usd"]["bids"]
    total_bids_amount = 0

    for item in bids:
        price = item[0]
        coin_amount = item[1]

        total_bids_amount += price * coin_amount

    return f"Total bids: {total_bids_amount} $"

def main():
    #print(get_info())
    #print(get_ticker())
    print(get_depth())

if __name__ == "__main__":
    main()
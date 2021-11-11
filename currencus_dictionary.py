import requests

def currencus():
    currencus = ["btc", "eth", "mana", "ltc"]
    start = 0
    for ct in currencus:
        print(ct)
        print(get_depth(coin1=ct))


def get_depth(coin1 = "mana", coin2 = "usd", limit = 150):
    #Информация о выставленных на продажу и покупку ордерах
    responce = requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")


    bids = responce.json()[f"{coin1}_usd"]["bids"]
    total_bids_amount = 0

    for item in bids:
        price = item[0]
        coin_amount = item[1]

        total_bids_amount += price * coin_amount

    print(round(total_bids_amount, 2))
    return bids

def main():
    #print(get_info())
    #print(get_ticker())
    print(currencus())

if __name__ == "__main__":
    main()
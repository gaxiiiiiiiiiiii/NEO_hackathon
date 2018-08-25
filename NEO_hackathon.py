import requests
import json


get_transaction  = "https://neoscan.io/api/main_net/v1/get_address_abstracts/%s/%d"
get_balance = "https://neoscan.io/api/main_net/v1/get_balance/%s"
add1 = "AXDt2hzT35knLnV3MB3dR9rAvYmadUfVdb"
add2 = "AKnbvRwL1MSPFWoS6bdD5v2SNHq2uta5tm"
block_height = 2640000
NEO_hash = "c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b"


def get_amouont(add):
    data = requests.get(get_balance % add).json()["balance"]
    for line in data:
        if line["asset"] == "NEO":
            balance = line["amount"]
    return balance

def caluculate(add,balance):    
    transactions = requests.get(get_transaction % (add, 1)).json()["entries"]
    for trs in transactions:
        if trs["asset"] != NEO_hash:
            continue
        if trs["block_height"] < block_height:
            break
        amount = trs["amount"]
        if trs["address_to"] == add:
            balance -= float(amount)
        else:
            balance += float(amount)
    return balance

if __name__ == '__main__':
    for i,add in enumerate([add1,add2]):
        balance = get_amouont(add)
        balance = caluculate(add,balance)
        print(f"残高{i}:{add}:{balance}")
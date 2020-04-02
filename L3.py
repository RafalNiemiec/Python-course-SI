import requests

def ordersList():
    buy, sell = [], []
    orders = requests.get('https://bitbay.net/API/Public/LTCUSD/trades.json')

    for i in orders.json():
        if i['type'] == 'sell':
            sell.append(i)
        else:
            buy.append(i)

    print('Buy offers: ')
    show(buy)
    print('Sell offers: ')
    show(sell)


def show(data):
    for i in data:
        print(i)


ordersList()
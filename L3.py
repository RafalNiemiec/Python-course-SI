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


def getData():
    coinbaseBuy = float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy.json').json()['data']['amount'])
    coinbaseSell = float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell.json').json()['data']['amount'])

    bitbaySell = float(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['bid'])
    bitbayBuy = float(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['ask'])

    if coinbaseSell>bitbaySell:
        print("We recommend to sell on Coinbase.")
    else:
        print('We recommend to sell on BitBay.')

    if coinbaseBuy>bitbayBuy:
        print("We recommend to buy on BitBay.")
    else:
        print('We recommend to buy on Coinbase.')

getData()
ordersList()
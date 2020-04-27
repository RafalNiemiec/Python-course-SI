import requests



def getData():
    buyList = [
        float(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['ask']),
        float(requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()['result']['Ask']),
        float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy').json()['data']['amount']),
        float(requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy").json()['data']['amount'])
    ]
    sellList = [
        float(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['bid']),
        float(requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()['result']['Bid']),
        float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell').json()['data']['amount']),
        float(requests.get("https://api.coinbase.com/v2/prices/BTC-USD/sell").json()['data']['amount'])
    ]

    trading(min(buyList), max(sellList), 0.01)


def trading(buy, sell, amountMoney):
    arbitrage = 0
    arbitrage += amountMoney * (sell - buy - sell*0.001)
    global walet
    if arbitrage > 0:
        print('Arbitrage is possible, with income on level: ', arbitrage)
        walet += arbitrage
    else:
        print('Arbitrage is not possible. \nArbitragee level: ', arbitrage)

    print('Money in walet: ', walet, '\n', 15*'-')



walet = 0
while True:
    getData()
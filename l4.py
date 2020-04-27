import requests

wallet = 0

def getData(amountMoney):
    buyList = [
        float(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['ask']),
        float(requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()['result']['Ask']),
        float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy').json()['data']['amount']),
        float(requests.get('https://www.bitstamp.net/api/ticker').json()['ask'])
    ]
    sellList = [
        float(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['bid']),
        float(requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()['result']['Bid']),
        float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell').json()['data']['amount']),
        float(requests.get('https://www.bitstamp.net/api/ticker').json()['bid'])
    ]
    #fees = [BitBay, BitTrex, CoinBase, BitStamp]
    fees = [0.01, 0.002, 0.005, 0.005]

    trading(min(buyList), max(sellList), amountMoney, fees[buyList.index(min(buyList))])


def trading(buy, sell, amountMoney, fee):
    arbitrage = 0
    arbitrage += amountMoney * (sell - buy - sell*fee)
    global wallet
    if arbitrage > 0:
        print('Arbitrage is possible, with income on level: ', arbitrage)
        wallet += arbitrage
    else:
        print('Arbitrage is not possible. \nArbitragee level: ', arbitrage)

    print('Money in walet: ', wallet, '\n', 15 * '-')


def makeMoney(amountBTC):
    while True:
        getData(amountBTC)


makeMoney(0.2)
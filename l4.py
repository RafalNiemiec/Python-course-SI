import requests

wallet = 0

def getData(amountMoney):

    bitbay = requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()
    bittrex = requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()
    coinbase = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy').json()
    bitstamp = requests.get('https://www.bitstamp.net/api/ticker').json()


    buyList = [
        float(bitbay['ask']),
        float(bittrex['result']['Ask']),
        float(coinbase['data']['amount']),
        float(bitstamp['ask'])
    ]
    sellList = [
        float(bitbay['bid']),
        float(bittrex['result']['Bid']),
        float(coinbase['data']['amount']),
        float(bitstamp['bid'])
    ]
    #fees = [BitBay, BitTrex, CoinBase, BitStamp]
    fees = [0.001, 0.002, 0.0025, 0.005]

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
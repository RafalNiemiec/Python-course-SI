import requests

#BitBay
#print('BitBay sell: ', requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['bid'])
#print('BitBay buy: ', requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['ask'])

#BITTREX
#print("Bittrex buy: ", requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()['result']['Bid'])
#print("Bittrex sell: ", requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()['result']['Ask'])

#dane wyciągane z COINBASE
#print('Coinbase buy: ', requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy').json()['data']['amount'])
#print('Coinbase sell: ', requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell').json()['data']['amount'])


buyList = [
    float(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['ask']),
    float(requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()['result']['Ask']),
    float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy').json()['data']['amount'])
]

sellList = [
    float(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['bid']),
    float(requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()['result']['Bid']),
    float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell').json()['data']['amount'])
]

buy = min(buyList)
sell = max(sellList)
print(buy)
print(sell)

print(0.1*buy-0.1*sell)


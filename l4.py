import requests


btc = requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()
print(btc['max'])
print(btc['min'])
btcProfit = (btc['max']/btc['min'] - 1)*100
print(round(btcProfit,2))

eth = requests.get('https://bitbay.net/API/Public/ETHUSD/ticker.json').json()
print(eth['max'])
print(eth['min'])
ethProfit = (eth['max']/eth['min'] - 1)*100
print(round(ethProfit,2))

ltc = requests.get('https://bitbay.net/API/Public/LTCUSD/ticker.json').json()
print(ltc['max'])
print(ltc['min'])
ltcProfit = (ltc['max']/ltc['min'] - 1)*100
print(round(ltcProfit,2))

dash = requests.get('https://bitbay.net/API/Public/DASHUSD/ticker.json').json()
print(dash['max'])
print(dash['min'])
dashProfit = (dash['max']/dash['min'] - 1)*100
print(round(dashProfit,2))
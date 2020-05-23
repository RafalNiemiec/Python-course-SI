import time
import requests

def getData(timer, crypto):
    volumens = []
    difference = []
    url = "https://www.bitstamp.net/api/v2/ohlc/btcusd?step=86400&limit=10&start={timer}".format(timer=timer)
    print(url)
    dailyData = requests.get(url).json()['data']['ohlc']


    for day in dailyData:
        volumens.append([float(day['volume']), time.ctime(float(day['timestamp']))])

    for i in range(0, len(volumens)):
        difference.append((volumens[i][0]-volumens[i-1][0])/volumens[i][0])

    print(difference)






timer = int(time.time())-86400*20

getData(str(timer), 'BTC')


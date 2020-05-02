import requests

def getData():
    btc = requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()
    eth = requests.get('https://bitbay.net/API/Public/ETHUSD/ticker.json').json()
    neu = requests.get('https://bitbay.net/API/Public/NEUUSD/ticker.json').json()
    lsk = requests.get('https://bitbay.net/API/Public/LSKUSD/ticker.json').json()

    profitList = []

    #btcProfit
    profitList.append([round((btc['max']/btc['min'] - 1)*100, 2), 'BTC'])

    #ethProfit
    profitList.append([round((eth['max']/eth['min'] - 1)*100, 2), 'ETH'])

    #neuProfit
    profitList.append([round((neu['max']/neu['min'] - 1)*100, 2), 'LTC'])

    #lskProfit
    profitList.append([round((lsk['max']/lsk['min'] - 1)*100, 2), 'LSK'])

    sort(profitList)


def sort(profitList):
    for j in range(len(profitList)-1):
        for i in range(len(profitList)-1):
            if profitList[i][0] < profitList[i+1][0]:
                profitList[i], profitList[i+1] = profitList[i+1], profitList[i]
    write(profitList)


def write(profitList):
    for i in profitList:
        print(i[1], ' ', i[0], '%')

getData()
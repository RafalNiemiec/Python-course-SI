import requests
import time
import pandas
import numpy
from pandas import read_csv


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

def userData():
    crypto = ''
    amount = -1
    while crypto.upper() not in ['BTC', 'ETH', 'LTC', 'LSK']:
        print('Please insert Your cryptocurrency (BTC/ETH/LTC/LSK): ')
        crypto = str(input())
        if crypto.upper() not in ['BTC', 'ETH', 'LTC', 'LSK']:
            print('You insert incorrect input. Please use BTC or ETH or LTC or LSK. \n', 30*'-', '\n')

    while amount < 0:
        print("Please insert amount of cryptocurrency (f.e. 0.001): ")
        amount = float(input())
        if amount < 0:
            print('Are You really have negative money? Please insert positive value. . \n', 30*'-', '\n')




def info():
    url = 'https://api.bitbay.net/rest/trading/transactions/BTC-USD?fromTime={time}'.format(time = 1543410325000)
    transList = requests.get(url).json()['items']
    sum = 0

    for trans in transList:
        sum += float(trans['r'])

    print(sum)
    print(sum/len(transList))


def portmonetka_scv():
    file = read_csv('resources.csv')
    print(file)
    return file

#portmonetka_scv()

#info()
#getData()

userData()
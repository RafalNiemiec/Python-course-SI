from os import system
import requests
import time
from pandas import read_csv
import numpy as np
import csv


def userData():
    crypto = verify()
    while amount < 0:
        print("Please insert amount of cryptocurrency (f.e. 0.001): ")
        amount = float(input())
        if amount < 0:
            print('Are You really have negative money? Please insert positive value. . \n', 30 * '-', '\n')
    data[crypto] = amount
    saveData()

def saveData():
    with open('wallet.csv', 'w', newline="") as csv_file:
        writer = csv.writer(csv_file)
        for crypto, amount in data.items():
            writer.writerow([crypto, amount])
    print(50 * '=', '\n Information saved! \n ', 50 * '=')

def verify():
    crypto = ''
    while crypto.upper() not in ['BTC', 'ETH', 'LTC', 'LSK']:
        print('Please insert Your cryptocurrency (BTC/ETH/LTC/LSK): ')
        crypto = str(input())
        if crypto.upper() not in ['BTC', 'ETH', 'LTC', 'LSK']:
            print('You insert incorrect input. Please use BTC or ETH or LTC or LSK. \n', 30 * '-', '\n')
    return crypto.upper()

def wallet():
    global data
    with open('wallet.csv') as csv_file:
        reader = csv.reader(csv_file)
        data = dict(reader)
    return data

def info(time, crypto):
    transList, sum = [], 0
    url = 'https://api.bitbay.net/rest/trading/transactions/{cryptos}-USD?fromTime={times}'.format(times=time,
                                                                                               cryptos=crypto)
    transList = requests.get(url).json()['items']
    for trans in transList:
        sum += float(trans['r'])
    return (float(sum / len(transList)))

def dailyIncome():
    currency = verify()
    past = input("From what time (h) You want to calculate income (insert float): ")
    pastRate = info(str(int(time.time() - float(past)*3600000)), currency)
    actualRate = info(str(int(time.time())), currency)

    income = float(data[currency]) * (actualRate - pastRate)
    print(('Your income from {cur} is equal {inc}').format(cur=currency, inc=income))
    time.sleep(1)

def allMoney():
    moneySum = 0
    for currency in data:
        moneySum += info(int(time.time()), currency)
    print('On that moment, You have',moneySum,'USD in cryptocurrencies.')


def interface():
    global data
    wallet()
    while True:
        print(60*'=')
        print('Welcome in CryptoWallet! \n 1) Edit data \n 2) Calculate income \n 3) Wallet \n 4) Sum money \n 5) Exit')
        key = int(input('Choose number: '))
        print(60 * '=')
        if key == 1:
            userData()
        if key == 2:
            dailyIncome()
        if key == 3:
            print('Your actual founds: ', wallet())
        if key == 4:
            allMoney()
        if key == 5:
            exit('Thanks for visit!')

interface()

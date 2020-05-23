import time
import requests
from scipy.stats import norm
import matplotlib.pyplot as plt
from random import *
from statistics import median
from numpy import *

predictList, vol, difference = [], [], []

def getData(pastDays, crypto):
    url = "https://www.bitstamp.net/api/v2/ohlc/{crypto}usd?step=86400&limit=100&start={timer}".format(
        timer=str(int(time.time()) - 86400 * pastDays), crypto=crypto)
    return requests.get(url).json()['data']['ohlc']


def information(dailyData):
    for i in range(0, len(dailyData) - 1):
        vol.append(float(dailyData[i]['volume']))
        difference.append(absolute((vol[i] - vol[i - 1]) / vol[i]))
    return difference, vol


def absolute(num):
    if num > 1:
        return num - 1
    if num < -1:
        return num + 1
    return num


def simulation(data, volumens):
    avg, std = norm.fit(data)
    predict = absolute(gauss(avg, std))
    predictList.append(predict * volumens[-1] + volumens[-1])
    plt.plot(arange(0, len(volumens)), volumens, color='g')
    plt.plot(arange(len(volumens), len(predictList) + len(volumens)), predictList, color='b')
    plt.grid(True)
    plt.xlabel("Days")
    plt.ylabel("Volume")
    plt.title("Prediction of volume")
    plt.legend(['Historical data','Predicted data'])


def pointer(predictList):
    med = median(predictList)
    avg, std = norm.fit(predictList)
    print('One simulation: ', predictList[0])
    print('Madian: ', med, '\nAvarange: ', avg, '\nStd: ', std)


def calculate(daysAnalyst, currency):
    difference, vol = information(getData(daysAnalyst, currency))
    for i in range(daysAnalyst):
        simulation(difference, vol)
    pointer(predictList)
    plt.show()


#calculate(how many days You want to calculate, currency)
calculate(100, 'btc')

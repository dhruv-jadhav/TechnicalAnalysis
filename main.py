# Performs technical analysis on stocks
from executor import DeciderBuy, DeciderHold, DeciderSell
from plots import Plot
import os

portfolio = ['ITC']

for o in portfolio:
    try:
        os.mkdir('image')
    except:
        pass
    try:
        os.mkdir(f'image/{o}')
    except:
        pass


for i in portfolio:
    try:
        period = input('What is the period you want to analyze?[Check README.md for allowed inputs]: ')
        interval = input('What is the interval for the period?[Check README.md for allowed inputs]: ')

        Plot(i, period=period, interval=interval)
        print(DeciderBuy(i, period=period, interval=interval))
        print(DeciderSell(i, period=period, interval=interval))
        print(DeciderHold(i, period=period, interval=interval))
    except Exception as e:
        print(f'The analysis did not succeed due to: {e}')
        print('Check README.md for usage of the program!')

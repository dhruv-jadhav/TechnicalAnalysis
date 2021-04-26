# Performs technical analysis on stocks
import os
from time import perf_counter

from executor import DeciderBuy, DeciderHold, DeciderSell, TruncateStuff
from plots import Plot

TruncateStuff()

# <---------------Stuff You Need to Define----------------->
portfolio = ['ticker1', 'ticker2', 'ticker3...']  # Can handle any number of tickers
email = 'abcxyz@gmail.com'  # Valid email
period = ''  # Check README.md for valid inputs
interval = ''  # Check README.md for valid inputs
# <---------------Stuff You Need to Define----------------->

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
        start = perf_counter()

        Plot(i, period=period, interval=interval)
        print(DeciderBuy(i, period=period, interval=interval, receiver=email))
        print(DeciderSell(i, period=period, interval=interval, receiver=email))
        print(DeciderHold(i, period=period, interval=interval))

        end = perf_counter()

        print(f"\nThe analysis took: {end - start} seconds\n")
    except Exception as e:
        print(f'The analysis did not succeed due to: {e}')
        print('Check README.md for the usage of the program!')

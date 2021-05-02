# Performs technical analysis on stocks
import os
from time import perf_counter, sleep

from executor import DeciderBuy, DeciderHold, DeciderSell, TruncateStuff
from indicators.plots import Plot

TruncateStuff()

# <---------------Stuff You Need to Define----------------->
portfolio = ['ITC', 'LT', 'RELIANCE', 'COALINDIA', 'HINDCOPPER', 'HINDPETRO', 'HDFCBANK', 'ICICIBANK']  # Can handle any number of tickers
email = os.getenv('email')  # Valid email
period = os.getenv('period')  # Check README.md for valid inputs
interval = os.getenv('interval')  # Check README.md for valid inputs
# <---------------Stuff You Need to Define----------------->

while True:
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

    sleep(10800)

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
    Plot(i)
    print(DeciderBuy(i))
    print(DeciderSell(i))
    print(DeciderHold(i))

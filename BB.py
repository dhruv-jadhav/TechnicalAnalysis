import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ta.trend import sma_indicator
from ta.volatility import BollingerBands

plt.style.use('Solarize_Light2')


def get_signal(data):
    positions = []

    for i in range(len(data['Close'])):
        # If the closing price is above Upper_2 band. [SELL]
        if data['Close'][i] > data['Upper_2'][i]:
            positions.append(-1)
        # If closing price is below lower_2 band. [BUY]
        elif data['Close'][i] < data['Lower_2'][i]:
            positions.append(1)
        # The first few values for Bollinger Bands will be NaN as the SMA hasn't been calculated for the given time period.
        else:
            positions.append(0)

    return positions


def BBands(close, window, deviation_1, deviation_2):
    # Getting values of Bollinger Bands and SMA from the `ta` module
    BBD1 = BollingerBands(close=close, window=int(window), window_dev=deviation_1, fillna=False)
    BBD2 = BollingerBands(close=close, window=int(window), window_dev=deviation_2, fillna=False)
    SMA = sma_indicator(close=close, window=int(window), fillna=False)

    BB_Upper_1 = BBD1.bollinger_hband().dropna()
    BB_Lower_1 = BBD1.bollinger_lband().dropna()

    BB_Upper_2 = BBD2.bollinger_hband().dropna()
    BB_Lower_2 = BBD2.bollinger_lband().dropna()

    # Creating DataFrame
    df = pd.DataFrame()

    # Adding all the required columns to the DataFrame
    df['Close'] = close.dropna()
    df['Upper_2'] = BB_Upper_2
    df['Upper_1'] = BB_Upper_1
    df['SMA'] = SMA
    df['Lower_1'] = BB_Lower_1
    df['Lower_2'] = BB_Lower_2
    df['Positions'] = get_signal(df)

    return df['Close'], df['Positions']

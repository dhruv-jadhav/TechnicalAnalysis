# >2D: Sell and short
# +2D - +1D: Hold -> Sell
# +1D - -1D: Hold
# -1D - -2D: Hold -> Buy
# <-2D: Buy and cover at +2D

import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from ta.trend import sma_indicator
from ta.volatility import BollingerBands
import numpy as np

itc = yf.Ticker(str('FB'))

# stfr: yyyy-mm-dd
stock_df = itc.history(period='1y', interval='1d')


def get_signal(data):
    buy_signal = []  # buy list
    sell_signal = []  # sell list

    for i in range(len(data['Close'])):
        if data['Close'][i] > data['Upper_2'][i]:  # Then you should sell
            # print('SELL')
            buy_signal.append(np.nan)
            sell_signal.append(data['Close'][i])
        elif data['Close'][i] < data['Lower_2'][i]:  # Then you should buy
            # print('BUY')
            sell_signal.append(np.nan)
            buy_signal.append(data['Close'][i])
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)

    return buy_signal, sell_signal


def MarginChecker(close, upper, lower, sma):
    global percentage

    df = pd.DataFrame()
    df['Upper_2'] = upper
    df['Lower_2'] = lower
    df['Close'] = close
    df['SMA'] = sma
    df['percentage'] = 0
    df['Warn_Low'] = False
    df['Warn_Up'] = False

    df.loc[df['SMA'] >= 2000, 'percentage'] = 0.5
    df.loc[(df['SMA'] >= 1000) & (df['SMA'] < 2000), 'percentage'] = 1
    df.loc[(df['SMA'] < 1000) & (df['SMA'] > 500), 'percentage'] = 2
    df.loc[df['SMA'] <= 500, 'percentage'] = 3

    df['adj_upper'] = (df['Upper_2'] - (df['Upper_2'] * (df['percentage'] / 100)))

    df['adj_lower'] = (df['Lower_2'] + (df['Lower_2'] * (df['percentage'] / 100)))

    df.loc[(df['Close'] < df['adj_lower']), 'Warn_Low'] = True
    df.loc[(df['Close'] > df['adj_upper']), 'Warn_Up'] = True

    return df['Warn_Up'], df['Warn_Low']


def BBands(close, window, deviation_1, deviation_2):
    BBD1 = BollingerBands(close=close, window=window, window_dev=deviation_1, fillna=False)
    BBD2 = BollingerBands(close=close, window=window, window_dev=deviation_2, fillna=False)
    SMA = sma_indicator(close=close, window=window, fillna=False)

    BB_Upper_1 = BBD1.bollinger_hband().dropna()
    BB_Lower_1 = BBD1.bollinger_lband().dropna()

    BB_Upper_2 = BBD2.bollinger_hband().dropna()
    BB_Lower_2 = BBD2.bollinger_lband().dropna()

    df = pd.DataFrame()
    df['Close'] = close.dropna()
    df['Upper_2'] = BB_Upper_2
    df['Upper_1'] = BB_Upper_1
    df['SMA'] = SMA
    df['Lower_1'] = BB_Lower_1
    df['Lower_2'] = BB_Lower_2
    df['Buy'], df['Sell'] = get_signal(df)

    fig = plt.figure(figsize=(12.2, 6.4))  # width = 12.2 inches and height = 6.4 inches
    # Add the subplot
    ax = fig.add_subplot(1, 1, 1)  # Number of rows, cols, & index
    # Get the index values of the DataFrame
    x_axis = df.index
    # Plot and shade the area between the upper band and the lower band Grey
    ax.fill_between(x_axis, df['Upper_2'], df['Lower_2'], color='grey')
    # Plot the Closing Price and Moving Average
    ax.plot(x_axis, df['Close'], color='gold', lw=3, label='Close Price', alpha=0.5)
    ax.plot(x_axis, df['SMA'], color='blue', lw=3, label='Moving Average', alpha=0.5)
    ax.scatter(x_axis, df['Buy'], color='green', lw=3, label='Buy', marker='^', markersize=15, alpha=1)
    ax.scatter(x_axis, df['Sell'], color='red', lw=3, label='Sell', marker='v', markersize=15, alpha=1)
    # Set the Title & Show the Image
    ax.set_title('Bollinger Band For Tesla')
    ax.set_xlabel('Date')
    ax.set_ylabel('USD Price ($)')
    plt.xticks(rotation=45)
    ax.legend()
    plt.show()



BBands(stock_df['Close'], 20, 1, 2)

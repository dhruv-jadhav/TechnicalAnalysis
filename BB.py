import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ta.trend import sma_indicator
from ta.volatility import BollingerBands

plt.style.use('Solarize_Light2')


def get_signal(data):
    buy_signal = []  # buy list
    sell_signal = []  # sell list

    for i in range(len(data['Close'])):
        # If the closing price is above Upper_2 band. [SELL]
        if data['Close'][i] > data['Upper_2'][i]:
            buy_signal.append(np.nan)
            sell_signal.append(data['Close'][i])
        # If closing price is below lower_2 band. [BUY]
        elif data['Close'][i] < data['Lower_2'][i]:
            sell_signal.append(np.nan)
            buy_signal.append(data['Close'][i])
        # The first few values for Bollinger Bands will be NaN as the SMA hasn't been calculated for the given time period.
        else:
            buy_signal.append(np.nan)
            sell_signal.append(np.nan)

    return buy_signal, sell_signal


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
    df['Buy'], df['Sell'] = get_signal(df)

    # Initialising matplotlib
    fig = plt.figure(figsize=(12, 6))

    ax = fig.add_subplot(1, 1, 1)
    x_axis = df.index

    # Plotting Bollinger Bands, Closing price  and SMA
    ax.fill_between(x_axis, df['Upper_2'], df['Lower_2'], color='#ffe59e')
    ax.plot(x_axis, df['Close'], color='#a8ff26', lw=3, label='Close Price')
    ax.plot(x_axis, df['SMA'], color='#f7b21b', lw=3, label='Simple Moving Average')

    len_list = df[df['Sell'].notna()].index.tolist()

    # Getting SELL data points
    for i, j in zip(range(0, len(len_list)), df['Sell'].dropna().tolist()):
        date = df[df['Sell'].notna()].index[i]
        date = date.to_pydatetime()
        x_axis = date
        y_axis = j

        # Annotating the chart at sell points
        ax.annotate(text='S', xy=(x_axis, y_axis), arrowprops=dict(facecolor='red', shrink=0.05))

    # Getting BUY data points
    for i, j in zip(range(0, len(len_list)), df['Buy'].dropna().tolist()):
        date = df[df['Buy'].notna()].index[i]
        date = date.to_pydatetime()
        x_axis = date
        y_axis = j

        # Annotating the chart at buy points
        ax.annotate(text='B', xy=(x_axis, y_axis), arrowprops=dict(facecolor='green', shrink=0.05))

    plt.ylabel('Price', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    plt.title('Bollinger Bands', fontsize=20)
    plt.show()


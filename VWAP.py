import matplotlib.pyplot as plt
import pandas as pd
from ta.trend import sma_indicator
from ta.volume import volume_weighted_average_price

plt.style.use('Solarize_Light2')


def VWAPrice(high, low, close, volume, window):
    # Getting values of Volume Weighted Average Price from the `ta` module
    VWAP = volume_weighted_average_price(high=high, low=low, close=close, volume=volume, window=int(window), fillna=False)

    # Creating DataFrame
    df = pd.DataFrame()

    # Adding all the required columns to the DataFrame
    df['High'] = high
    df['Low'] = low
    df['Close'] = close
    df['volume'] = volume
    df['SMA'] = sma_indicator(close=close, window=14)
    df['VWAP'] = VWAP

    # Initialising matplotlib
    fig = plt.figure(figsize=(12, 6))

    ax = fig.add_subplot(1, 1, 1)
    x_axis = df.index

    ax.plot(x_axis, df['VWAP'], color='#a8ff26', lw=3, label='VWAP')  # lw = line width
    ax.plot(x_axis, df['SMA'], color='#f7b21b', lw=3, label='Simple Moving Average')

    plt.ylabel('Price', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    plt.title('Volume Weighted Average Price', fontsize=20)
    plt.legend()
    plt.show()

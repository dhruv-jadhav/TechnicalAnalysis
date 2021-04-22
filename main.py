import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from ta.momentum import RSIIndicator
from ta.trend import ema_indicator, sma_indicator
from ta.volatility import BollingerBands

itc = yf.Ticker(str('^GSPC'))

# stfr: yyyy-mm-dd
stock_df = itc.history(period='1y', interval='1d')


def Warnings(close, window_RSI, windows_BB, deviation):
    RSI = RSIIndicator(close=close, window=int(window_RSI), fillna=False)
    RSI = RSI.rsi().dropna()

    BB = BollingerBands(close=close, window=windows_BB, window_dev=deviation, fillna=False)
    SMA = sma_indicator(close=close, window=windows_BB, fillna=False)

    BB_Upper = BB.bollinger_hband().dropna()
    BB_Lower = BB.bollinger_lband().dropna()

    df = pd.DataFrame()
    df['RSI'] = RSI
    df['SMA'] = SMA.dropna()
    df['Upper'] = BB_Upper
    df['Lower'] = BB_Lower
    df['State'] = 0


    df.loc[df['RSI'] <= 30, 'State'] = 'Oversold'
    df.loc[(df['RSI'] > 30) & (df['RSI'] < 70), 'State'] = 'Neutral'
    df.loc[df['RSI'] >= 70, 'State'] = 'Overbought'

    pd.set_option('display.max_rows', df.shape[0])
    print(df)


def EMAvg(close, window_long, window_short):
    EMA_Long = ema_indicator(close=close, window=int(window_long), fillna=False)
    EMA_Short = ema_indicator(close=close, window=int(window_short), fillna=False)
    EMA_Long = EMA_Long.dropna()
    EMA_Short = EMA_Short.dropna()

    df = pd.DataFrame()
    df['Close'] = close
    df['EMA_Long'] = EMA_Long
    df['EMA_Short'] = EMA_Short
    df['Signal'] = 0

    df.loc[(df['EMA_Short'] > df['EMA_Long']), 'Signal'] = 1
    df['Position'] = df['Signal'].diff()

    # Plot EMA's wrt Close price
    plt.figure(figsize=(50, 40))
    df['Close'].plot(color='k', lw=1, label='Close Price')
    df['EMA_Short'].plot(color='b', lw=1, label=f'{window_short}-period EMA')
    df['EMA_Long'].plot(color='g', lw=1, label=f'{window_long}-period EMA')

    # Buy/Sell Indicators
    plt.plot(df[df['Position'] == 1].index, df['EMA_Short'][df['Position'] == 1], '^',
             markersize=15, color='g', label='buy')

    plt.plot(df[df['Position'] == -1].index, df['EMA_Short'][df['Position'] == -1], 'v',
             markersize=15, color='r', label='sell')

    plt.ylabel('Price in Rupees', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    plt.title('EMA Crossover', fontsize=20)
    plt.legend()
    plt.grid()
    plt.show()


def BBands(close, window, deviation):
    BB = BollingerBands(close=close, window=window, window_dev=deviation, fillna=False)
    SMA = sma_indicator(close=close, window=window, fillna=False)

    BB_Upper = BB.bollinger_hband().dropna()
    BB_Lower = BB.bollinger_lband().dropna()

    df = pd.DataFrame()
    df['Close'] = close.dropna()
    df['SMA'] = SMA.dropna()
    df['Upper'] = BB_Upper
    df['Lower'] = BB_Lower
    df['Signal'] = 0

    df.loc[df['Close'] > df['Upper'], 'Signal'] = 1
    df['Position'] = df['Signal'].diff()

    pd.set_option('display.max_rows', df.shape[0])
    print(df)

    fig = plt.figure(figsize=(12, 6))

    ax = fig.add_subplot(1, 1, 1)  # Number of rows, cols, & index
    # Get the index values of the DataFrame
    x_axis = df.index
    # Plot and shade the area between the upper band and the lower band Grey
    ax.fill_between(x_axis, df['Upper'], df['Lower'], color='#ffe59e')
    # Plot the Closing Price and Moving Average
    ax.plot(x_axis, df['Close'], color='#a8ff26', lw=3, label='Close Price')  # lw = line width
    ax.plot(x_axis, df['SMA'], color='#f7b21b', lw=3, label='Simple Moving Average')
    # Plotting Buy/Sell Signals


    plt.ylabel('Price in Rupees', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    plt.title('Bollinger Bands', fontsize=20)
    plt.show()


Warnings(stock_df['Close'], 14, 20, 2)
# EMAvg(stock_df['Close'], 50, 20)
# BBands(stock_df['Close'], 20, 2)

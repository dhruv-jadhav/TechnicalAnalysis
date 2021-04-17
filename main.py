import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from ta.momentum import RSIIndicator
from ta.trend import ema_indicator

itc = yf.Ticker(str('ITC.NS'))

# stfr: yyyy-mm-dd
itc_df = itc.history(period='20y', interval='1d')


def RSIIndicators(close, window):
    RSI = RSIIndicator(close=close, window=int(window), fillna=False)
    RSI = RSI.rsi().dropna()

    df = pd.DataFrame()
    df['RSI'] = RSI
    df['Rating'] = 0

    df.loc[df['RSI'] <= 30, 'Rating'] = 'Oversold'
    df.loc[(df['RSI'] > 30) & (df['RSI'] < 70), 'Rating'] = 'Neutral'
    df.loc[df['RSI'] >= 70, 'Rating'] = 'Overbought'

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
    plt.figure(figsize=(30, 20))
    df['Close'].plot(color='k', lw=1, label='Close Price')
    df['EMA_Short'].plot(color='b', lw=1, label=f'{window_short}-day EMA')
    df['EMA_Long'].plot(color='g', lw=1, label=f'{window_long}-day EMA')

    # Buy/Sell Indicators
    plt.plot(df[df['Position'] == 1].index, df['EMA_Short'][df['Position'] == 1], '^',
             markersize=15, color='g', label='buy')


    plt.plot(df[df['Position'] == -1].index, df['EMA_Short'][df['Position'] == -1], 'v',
             markersize=15, color='r', label='sell')

    plt.ylabel('Price in Rupees', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    plt.title('ITC Limited[NSE: ITC] - EMA Crossover', fontsize=20)
    plt.legend()
    plt.grid()
    plt.show()


# RSIIndicators(itc_df['Close'], 14)
EMAvg(itc_df['Close'], 50, 20)

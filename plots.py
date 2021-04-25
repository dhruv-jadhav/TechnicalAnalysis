import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from ta.momentum import RSIIndicator
from ta.trend import ema_indicator, sma_indicator
from ta.volatility import BollingerBands

plt.style.use('Solarize_Light2')


def Plot(stock):
    def PlotEMA(ticker, close, window_long, window_short):
        try:
            os.mkdir(ticker)
        except:
            pass
        # Getting values of EMA from the `ta` module
        EMA_Long = ema_indicator(close=close, window=int(window_long), fillna=False)
        EMA_Short = ema_indicator(close=close, window=int(window_short), fillna=False)

        # Creating DataFrame
        df = pd.DataFrame()

        # Adding all the required columns to the DataFrame
        df['Close'] = close
        df['EMA_Long'] = EMA_Long.dropna()
        df['EMA_Short'] = EMA_Short.dropna()
        df['Signal'] = 0

        # Giving buy signals
        df.loc[(df['EMA_Short'] > df['EMA_Long']), 'Signal'] = 1
        df['Position'] = df['Signal'].diff()

        # Plot EMA's wrt Close price
        plt.figure(figsize=(6, 5.5))
        df['Close'].plot(color='k', lw=1, label='Close Price')
        df['EMA_Short'].plot(color='b', lw=1, label=f'{window_short}-period EMA')
        df['EMA_Long'].plot(color='g', lw=1, label=f'{window_long}-period EMA')

        # Plot Buy/Sell Indicators
        plt.plot(df[df['Position'] == 1].index, df['EMA_Short'][df['Position'] == 1], '^',
                 markersize=15, color='g', label='buy')

        plt.plot(df[df['Position'] == -1].index, df['EMA_Short'][df['Position'] == -1], 'v',
                 markersize=15, color='r', label='sell')

        plt.ylabel('Price in Rupees', fontsize=15)
        plt.xlabel('Date', fontsize=15)
        plt.title(f'EMA Crossover: {ticker}', fontsize=20)
        plt.legend()
        plt.grid()
        try:
            plt.savefig(f'image/{ticker}/EMA_{ticker}.png', bbox_inches='tight')
        except:
            directory = f'image/{ticker}'
            for f in os.listdir(ticker):
                os.remove(os.path.join(directory, f))
            plt.savefig(f'image/{ticker}/EMA_{ticker}.png', bbox_inches='tight')

    def PlotRSI(ticker, close, window):
        try:
            os.mkdir(ticker)
        except:
            pass
        # Getting values of Relative Strength Index from the `ta` module
        RSI = RSIIndicator(close=close, window=int(window), fillna=False)

        # Creating DataFrame
        df = pd.DataFrame()

        # Adding all the required columns to the DataFrame
        df['RSI'] = RSI.rsi().dropna()

        # Initialising matplotlib
        fig = plt.figure(figsize=(6, 5.5))

        ax = fig.add_subplot(1, 1, 1)
        x_axis = df.index

        # Plotting 70 and 30 RSI lines
        ax.plot(x_axis, [70] * len(x_axis), label="overbought")
        ax.plot(x_axis, [30] * len(x_axis), label="oversold")

        # Plotting RSI
        ax.plot(x_axis, df['RSI'], label="RSI")
        ax.legend()

        plt.ylabel(f'RSI: {ticker}', fontsize=15)
        plt.xlabel('Date', fontsize=15)
        plt.title(f'Relative Strength Index: {ticker}', fontsize=20)
        plt.legend()
        try:
            plt.savefig(f'image/{ticker}/RSI_{ticker}.png', bbox_inches='tight')
        except:
            directory = f'image/{ticker}'
            for f in os.listdir(ticker):
                os.remove(os.path.join(directory, f))
            plt.savefig(f'image/{ticker}/RSI_{ticker}.png', bbox_inches='tight')

    def PlotBB(ticker, close, window, deviation_1, deviation_2):
        try:
            os.mkdir(ticker)
        except:
            pass

        def GetSignal(data):
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
        df['Buy'], df['Sell'] = GetSignal(df)

        # Initialising matplotlib
        fig = plt.figure(figsize=(6, 5.5))

        ax = fig.add_subplot(1, 1, 1)
        x_axis = df.index

        # Plotting Bollinger Bands, Closing price  and SMA
        ax.fill_between(x_axis, df['Upper_2'], df['Lower_2'], color='#ffe59e')
        ax.plot(x_axis, df['Close'], color='#a8ff26', lw=3, label='Close Price')
        ax.plot(x_axis, df['SMA'], color='#f7b21b', lw=3, label=f'SMA: {window} periods')

        len_list = df[df['Sell'].notna()].index.tolist()

        # Getting SELL data points
        for k, j in zip(range(0, len(len_list)), df['Sell'].dropna().tolist()):
            date = df[df['Sell'].notna()].index[k]
            date = date.to_pydatetime()
            x_axis = date
            y_axis = j

            # Annotating the chart at sell points
            ax.annotate(text='S', xy=(x_axis, y_axis), arrowprops=dict(facecolor='red', shrink=0.05))

        # Getting BUY data points
        for k, j in zip(range(0, len(len_list)), df['Buy'].dropna().tolist()):
            date = df[df['Buy'].notna()].index[k]
            date = date.to_pydatetime()
            x_axis = date
            y_axis = j

            # Annotating the chart at buy points
            ax.annotate(text='B', xy=(x_axis, y_axis), arrowprops=dict(facecolor='green', shrink=0.05))

        plt.ylabel('Price', fontsize=15)
        plt.xlabel('Date', fontsize=15)
        plt.title(f'Bollinger Bands {ticker}', fontsize=20)
        plt.legend()
        plt.grid()
        try:
            plt.savefig(f'image/{ticker}/BB_{ticker}.png', bbox_inches='tight')
        except:
            directory = f'image/{ticker}'
            for f in os.listdir(ticker):
                os.remove(os.path.join(directory, f))
            plt.savefig(f'image/{ticker}/BB_{ticker}.png', bbox_inches='tight')


    ticker_ = yf.Ticker(f"{stock}.NS")
    stock_df = ticker_.history(period='1y', interval='1d')

    PlotEMA(ticker=stock, close=stock_df['Close'], window_long=50, window_short=20)
    PlotBB(ticker=stock, close=stock_df['Close'], window=20, deviation_1=1, deviation_2=2)
    PlotRSI(ticker=stock, close=stock_df['Close'], window=14)

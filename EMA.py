import matplotlib.pyplot as plt
import pandas as pd
from ta.trend import ema_indicator

plt.style.use('Solarize_Light2')


def EMAvg(close, window_long, window_short):
    # Getting values of EMA from the `ta` module
    EMA_Long = ema_indicator(close=close, window=int(window_long), fillna=False)
    EMA_Short = ema_indicator(close=close, window=int(window_short), fillna=False)
    EMA_Long = EMA_Long.dropna()
    EMA_Short = EMA_Short.dropna()

    # Creating DataFrame
    df = pd.DataFrame()

    # Adding all the required columns to the DataFrame
    df['Close'] = close
    df['EMA_Long'] = EMA_Long
    df['EMA_Short'] = EMA_Short
    df['Signal'] = 0

    # Giving buy signals
    df.loc[(df['EMA_Short'] > df['EMA_Long']), 'Signal'] = 1
    df['Position'] = df['Signal'].diff()

    # Plot EMA's wrt Close price
    plt.figure(figsize=(20, 10))
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
    plt.title('EMA Crossover', fontsize=20)
    plt.legend()
    plt.grid()
    plt.show()

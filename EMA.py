import matplotlib.pyplot as plt
import pandas as pd
from ta.trend import ema_indicator
import os

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

    return df['Close'], df['Position']

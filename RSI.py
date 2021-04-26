import pandas as pd
from ta.momentum import RSIIndicator


def RSIndex(close, window):
    # Getting values of Relative Strength Index from the `ta` module
    RSI = RSIIndicator(close=close, window=int(window), fillna=False)
    RSI = RSI.rsi().dropna()

    # Creating DataFrame
    df = pd.DataFrame()

    # Adding all the required columns to the DataFrame
    df['Close'] = close
    df['RSI'] = RSI
    df['Positions'] = 0

    # Analysing market conditions from RSI value
    df.loc[df['RSI'] <= 35, 'Positions'] = 1
    df.loc[(df['RSI'] > 35) & (df['RSI'] < 65), 'Positions'] = 0
    df.loc[df['RSI'] >= 65, 'Positions'] = -1

    return df['Close'], df['Positions']

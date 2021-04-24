import matplotlib.pyplot as plt
import pandas as pd
from ta.momentum import RSIIndicator

plt.style.use('Solarize_Light2')


def RSIndex(close, window):
    # Getting values of Relative Strength Index from the `ta` module
    RSI = RSIIndicator(close=close, window=int(window), fillna=False)
    RSI = RSI.rsi().dropna()

    # Creating DataFrame
    df = pd.DataFrame()

    # Adding all the required columns to the DataFrame
    df['RSI'] = RSI
    df['State'] = 0

    # Analysing market conditions from RSI value
    df.loc[df['RSI'] <= 30, 'State'] = 'Oversold'
    df.loc[(df['RSI'] > 30) & (df['RSI'] < 70), 'State'] = 'Neutral'
    df.loc[df['RSI'] >= 70, 'State'] = 'Overbought'

    # Initialising matplotlib
    fig = plt.figure(figsize=(12, 6))

    ax = fig.add_subplot(1, 1, 1)
    x_axis = df.index

    # Plotting 70 and 30 RSI lines
    ax.plot(x_axis, [70] * len(x_axis), label="overbought")
    ax.plot(x_axis, [30] * len(x_axis), label="oversold")

    # Plotting RSI
    ax.plot(x_axis, df['RSI'], label="RSI")
    ax.legend()

    plt.ylabel('RSI: (%)', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    plt.title('Relative Strength Index', fontsize=20)
    plt.show()

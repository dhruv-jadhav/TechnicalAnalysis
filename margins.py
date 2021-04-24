import pandas as pd


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

#
# for i in tqdm(range(1000), desc="Calculating EMA..."):
#     time.sleep(0.000001)
# EMAvg(close=stock_df['Close'], window_long=50, window_short=20)
#
# for i in tqdm(range(1000), desc="Calculating VWAP..."):
#     time.sleep(0.000001)
# VWAPrice(high=stock_df['High'], low=stock_df['Low'], close=stock_df['Close'], volume=stock_df['Volume'], window=14)
#
# for i in tqdm(range(1000), desc="Calculating Bollinger Bands..."):
#     time.sleep(0.000001)
# BBands(close=stock_df['Close'], window=20, deviation_1=1, deviation_2=2)
#
# for i in tqdm(range(1000), desc="Calculating RSI..."):
#     time.sleep(0.000001)
# RSIndex(close=stock_df['Close'], window=14)

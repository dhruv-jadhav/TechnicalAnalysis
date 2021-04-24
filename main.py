# Performs technical analysis on stocks
# TODO: Make system for Buy/Sell positions
# TODO: Make and run UnitTests on all functions
# TODO: Integrate all indicators for final buy/sell signal
# TODO: Calculate average returns from all indicators
import yfinance as yf
from BB import BBands
from EMA import EMAvg
from RSI import RSIndex
from VWAP import VWAPrice

ticker_stock = input("What stock do you want to perform technical analysis on?[Input the ticker]: ")

ticker = yf.Ticker(str(ticker_stock))

# stfr: yyyy-mm-dd
period = input("What is the period for the technical analysis? ")
interval = input("What is the interval for the technical analysis? ")
print(f"Analysing data of {ticker_stock} for {period} with {interval} as interval")

stock_df = ticker.history(period=period, interval=interval)

EMAvg(close=stock_df['Close'], window_long=50, window_short=20)
VWAPrice(high=stock_df['High'], low=stock_df['Low'], close=stock_df['Close'], volume=stock_df['Volume'], window=14)
BBands(close=stock_df['Close'], window=20, deviation_1=1, deviation_2=2)
RSIndex(close=stock_df['Close'], window=14)

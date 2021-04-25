import logging

import pandas as pd
import yfinance as yf

from BB import BBands
from EMA import EMAvg
from RSI import RSIndex

logging.basicConfig(filename='logs.log', filemode='a', format='%(levelname)s - %(asctime)s: %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def EMASignal(ticker_ema):
    ticker = yf.Ticker(f"{ticker_ema}.NS")
    stock_df = ticker.history(period='1y', interval='1d')

    df = pd.DataFrame()
    df['Close'] = EMAvg(close=stock_df['Close'], window_long=50, window_short=20)[0]
    df['Signal'] = EMAvg(close=stock_df['Close'], window_long=50, window_short=20)[1]

    for i in range(len(df['Signal'])):
        if df['Signal'][i] == 1:
            logger.info(f"EMA Signal[{ticker_ema}]: BUY")
            return 'Buy'
        elif df['Signal'][i] == -1:
            logger.info(f"EMA Signal[{ticker_ema}]: SELL")
            return 'Sell'
        else:
            logger.info(f"EMA Signal[{ticker_ema}]: HOLD")
            return 'Hold'


def BBSignal(ticker_bb):
    ticker = yf.Ticker(f"{ticker_bb}.NS")
    stock_df = ticker.history(period='1y', interval='1d')

    df = pd.DataFrame()
    df['Close'] = BBands(close=stock_df['Close'], window=20, deviation_1=1, deviation_2=2)[0]
    df['Signal'] = BBands(close=stock_df['Close'], window=20, deviation_1=1, deviation_2=2)[1]

    for i in range(len(df['Signal'])):
        if df['Signal'][i] == 1:
            logger.info(f"Bollinger Bands Signal[{ticker_bb}]: BUY")
            return 'Buy'
        elif df['Signal'][i] == -1:
            logger.info(f"Bollinger Bands Signal[{ticker_bb}]: SELL")
            return 'Sell'
        else:
            logger.info(f"Bollinger Bands Signal[{ticker_bb}]: HOLD")
            return 'Hold'


def RSISignal(ticker_rsi):
    ticker = yf.Ticker(f"{ticker_rsi}.NS")
    stock_df = ticker.history(period='1y', interval='1d')

    df = pd.DataFrame()
    df['Close'] = RSIndex(close=stock_df['Close'], window=14)[0]
    df['Signal'] = RSIndex(close=stock_df['Close'], window=14)[1]

    for i in range(len(df['Signal'])):
        if df['Signal'][i] == 1:
            logger.info(f"RSI Signal[{ticker_rsi}]: BUY")
            return 'Buy'
        elif df['Signal'][i] == -1:
            logger.info(f"RSI Signal[{ticker_rsi}]: SELL")
            return 'Sell'
        else:
            logger.info(f"RSI Signal[{ticker_rsi}]: HOLD")
            return 'Hold'

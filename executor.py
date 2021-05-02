from emails import FireEmail
from signals import EMASignal, BBSignal, RSISignal


def DeciderBuy(ticker, period, interval, receiver):
    if (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval) and RSISignal(ticker, period=period, interval=interval)) == 'Buy':

        FireEmail(stock=ticker, signal='Strong Buy', sender='analysis.technical.in@gmail.com', receiver=receiver, period=period, interval=interval)

        return f'Strong Buy!: {ticker}\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n3. RSI signal: {RSISignal(ticker, period=period, interval=interval)}'

    # -------------------------------------------------------------------------------------------------------------- #

    elif (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval)) == 'Buy' and RSISignal(ticker, period=period, interval=interval) != 'Buy':

        FireEmail(stock=ticker, signal='Buy', sender='analysis.technical.in@gmail.com', receiver=receiver, period=period, interval=interval)

        return f'Buy!: {ticker}\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n3. RSI signal: {RSISignal(ticker, period=period, interval=interval)}'


# -------------------------------------------------------------------------------------------------------------- #


def DeciderSell(ticker, period, interval, receiver):
    if (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval) and RSISignal(ticker, period=period, interval=interval)) == 'Sell':

        FireEmail(stock=ticker, signal='Strong Sell', sender='analysis.technical.in@gmail.com', receiver=receiver, period=period, interval=interval)

        return f'Strong Sell!: {ticker}\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n3. RSI signal: {RSISignal(ticker, period=period, interval=interval)}'

    # -------------------------------------------------------------------------------------------------------------- #

    elif (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval)) == 'Sell' and RSISignal(ticker, period=period, interval=interval) != 'Sell':

        FireEmail(stock=ticker, signal='Sell', sender='analysis.technical.in@gmail.com', receiver=receiver, period=period, interval=interval)

        return f'Sell!: {ticker}\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n3. RSI signal: {RSISignal(ticker, period=period, interval=interval)}'


# --------------------------------------------------------------------------------------------------------------


def DeciderHold(ticker, period, interval):
    if (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval) and RSISignal(ticker, period=period, interval=interval)) == 'Hold':

        return f'Strong Hold!: {ticker}\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n3. RSI signal: {RSISignal(ticker, period=period, interval=interval)}'

    # -------------------------------------------------------------------------------------------------------------- #

    elif (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval)) == 'Hold' and RSISignal(ticker, period=period, interval=interval) != 'Hold':

        return f'Hold!: {ticker}\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n3. RSI signal: {RSISignal(ticker, period=period, interval=interval)}'

    # -------------------------------------------------------------------------------------------------------------- #


def TruncateStuff():
    with open('logs.log', 'r+', encoding='utf-8') as file:
        count = len(file.readlines())

        if count > 500:
            file.seek(0)
            file.truncate(0)
            file.close()
        else:
            pass

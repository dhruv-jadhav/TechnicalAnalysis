from emails import FireEmail
from signals import EMASignal, BBSignal, RSISignal


def DeciderBuy(ticker, period, interval):
    if (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval) and RSISignal(ticker, period=period, interval=interval)) == 'Buy':

        FireEmail(stock=ticker, signal='Strong Buy', sender='analysis.technical.in@gmail.com', receiver='dhruvjadhav225@gmail.com', period=period, interval=interval)

        return f'Strong Buy!\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n\nRSI signal: {RSISignal(ticker, period=period, interval=interval)}'

    # -------------------------------------------------------------------------------------------------------------- #

    elif (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval)) == 'Buy' and RSISignal(ticker, period=period, interval=interval) != 'Buy':

        FireEmail(stock=ticker, signal='Buy', sender='analysis.technical.in@gmail.com', receiver='dhruvjadhav225@gmail.com', period=period, interval=interval )

        return f'Buy!\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n\nRSI signal: {RSISignal(ticker, period=period, interval=interval)}'


# -------------------------------------------------------------------------------------------------------------- #


def DeciderSell(ticker, period, interval):
    if (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval) and RSISignal(ticker, period=period, interval=interval)) == 'Sell':

        FireEmail(stock=ticker, signal='Strong Sell', sender='analysis.technical.in@gmail.com', receiver='dhruvjadhav225@gmail.com')

        return f'Strong Sell!\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n\nRSI signal: {RSISignal(ticker, period=period, interval=interval)}'

    # -------------------------------------------------------------------------------------------------------------- #

    elif (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval)) == 'Sell' and RSISignal(ticker, period=period, interval=interval) != 'Sell':

        FireEmail(stock=ticker, signal='Sell', sender='analysis.technical.in@gmail.com', receiver='dhruvjadhav225@gmail.com')

        return f'Sell!\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n\nRSI signal: {RSISignal(ticker, period=period, interval=interval)}'


# --------------------------------------------------------------------------------------------------------------


def DeciderHold(ticker, period, interval):
    if (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker) and RSISignal(ticker, period=period, interval=interval)) == 'Hold':

        FireEmail(stock=ticker, signal='Hold', sender='analysis.technical.in@gmail.com', receiver='dhruvjadhav225@gmail.com')

        return f'Strong Hold!\n\n1. EMA Crossover: {EMASignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n\nRSI signal: {RSISignal(ticker, period=period, interval=interval)}'

    # -------------------------------------------------------------------------------------------------------------- #

    elif (EMASignal(ticker, period=period, interval=interval) and BBSignal(ticker, period=period, interval=interval)) == 'Hold' and RSISignal(ticker, period=period, interval=interval) != 'Hold':

        return f'Hold!\n\n1. EMA Crossover: {RSISignal(ticker, period=period, interval=interval)}\n2. Bollinger Bands: {BBSignal(ticker, period=period, interval=interval)}\n\nRSI signal: {RSISignal(ticker, period=period, interval=interval)}'

    # -------------------------------------------------------------------------------------------------------------- #

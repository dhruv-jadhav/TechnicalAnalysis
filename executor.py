from emails import FireEmail
from signals import EMASignal, BBSignal, RSISignal


def DeciderBuy(ticker):
    if (EMASignal(ticker) and BBSignal(ticker) and RSISignal(ticker)) == 'Buy':
        FireEmail(stock=ticker, signal='Strong Buy', sender='analysis.technical.in@gmail.com',
                  receiver='dhruvjadhav225@gmail.com')
        return f'Strong Buy!\n\n1. EMA Crossover: {RSISignal(ticker)}\n2. Bollinger Bands: {BBSignal(ticker)}\n\nRSI signal: {RSISignal(ticker)}'

    elif (EMASignal(ticker) and BBSignal(ticker)) == 'Buy' and RSISignal(ticker) != 'Buy':
        FireEmail(stock=ticker, signal='Buy', sender='analysis.technical.in@gmail.com',
                  receiver='dhruvjadhav225@gmail.com')
        return f'Buy!\n\n1. EMA Crossover: {RSISignal(ticker)}\n2. Bollinger Bands: {BBSignal(ticker)}\n\nRSI signal: {RSISignal(ticker)}'

    # elif (EMASignal(ticker) or BBSignal(ticker) or RSISignal(ticker)) == 'Buy':
    #     FireEmail(stock=ticker, signal='Buy', sender='analysis.technical.in@gmail.com', receiver='dhruvjadhav225@gmail.com')
    #     return f'Buy!\n\n1. EMA Crossover: {RSISignal(ticker)}\n2. Bollinger Bands: {BBSignal(ticker)}\n\nRSI signal: {RSISignal(ticker)}'


def DeciderSell(ticker):
    if (EMASignal(ticker) and BBSignal(ticker) and RSISignal(ticker)) == 'Sell':
        FireEmail(stock=ticker, signal='Strong Sell', sender='analysis.technical.in@gmail.com',
                  receiver='dhruvjadhav225@gmail.com')
        return f'Strong Sell!\n\n1. EMA Crossover: {RSISignal(ticker)}\n2. Bollinger Bands: {BBSignal(ticker)}\n\nRSI signal: {RSISignal(ticker)}'


    elif (EMASignal(ticker) and BBSignal(ticker)) == 'Sell' and RSISignal(ticker) != 'Sell':
        FireEmail(stock=ticker, signal='Sell', sender='analysis.technical.in@gmail.com',
                  receiver='dhruvjadhav225@gmail.com')
        return f'Sell!\n\n1. EMA Crossover: {RSISignal(ticker)}\n2. Bollinger Bands: {BBSignal(ticker)}\n\nRSI signal: {RSISignal(ticker)}'

    #
    # elif (EMASignal(ticker) or BBSignal(ticker) or RSISignal(ticker)) == 'Sell':
    #     return f'Sell!\n\n1. EMA Crossover: {RSISignal(ticker)}\n2. Bollinger Bands: {BBSignal(ticker)}\n\nRSI signal: {RSISignal(ticker)}'


def DeciderHold(ticker):
    if (EMASignal(ticker) and BBSignal(ticker) and RSISignal(ticker)) == 'Hold':
        FireEmail(stock=ticker, signal='Hold', sender='analysis.technical.in@gmail.com',
                  receiver='dhruvjadhav225@gmail.com')
        return f'Strong Hold!\n\n1. EMA Crossover: {RSISignal(ticker)}\n2. Bollinger Bands: {BBSignal(ticker)}\n\nRSI signal: {RSISignal(ticker)}'


    elif (EMASignal(ticker) and BBSignal(ticker)) == 'Hold' and RSISignal(ticker) != 'Hold':
        return f'Hold!\n\n1. EMA Crossover: {RSISignal(ticker)}\n2. Bollinger Bands: {BBSignal(ticker)}\n\nRSI signal: {RSISignal(ticker)}'

    # elif (EMASignal(ticker) or BBSignal(ticker) or RSISignal(ticker)) == 'Hold':
    #     return f'Hold!\n\n1. EMA Crossover: {RSISignal(ticker)}\n2. Bollinger Bands: {BBSignal(ticker)}\n\nRSI signal: {RSISignal(ticker)}'

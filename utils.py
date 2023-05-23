import pandas as pd
from ta import momentum

def loop_candlesticks(data):
    closePrices = []
    for kline in data:
        time = kline[0]
        openPrice = float(kline[1])
        highPrice = float(kline[2])
        lowPrice = float(kline[3])
        closePrice = float(kline[4])
        volume = float(kline[5])
        closePrices.append(float(kline[4]))
        if len(closePrices) > 14:
            close_series = pd.Series(closePrices)
            # I am not sure if the RSI indicator is correct here.
            # Additionaly it makes sense to add more idicators like SMA, EMA, MACD, etc.
            # to help the model to learn the patterns.
            rsiSeries = momentum.RSIIndicator(close_series, 14).rsi()
            rsi = rsiSeries.get(key=rsiSeries.index[-1])
            yield [time, openPrice, highPrice, lowPrice, closePrice, volume, rsi]

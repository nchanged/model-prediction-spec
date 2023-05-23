from binance import  get_klines
import pandas as pd
from ta import momentum
from utils import loop_candlesticks
def predict(dataset):
    # load the model from disk


    # calculate the result
    next10Candles = []
    trendIsUp = False
    return next10Candles, trendIsUp


def main():
    # get live data
    data = get_klines('LINKUSDT', '15m', limit=1000)
    dataset = []
    for list in loop_candlesticks(data):
        dataset.append(list)
    predict(dataset)
            

if __name__ == '__main__':
    main()
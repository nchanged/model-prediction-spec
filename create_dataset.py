import os
from ta import momentum
from binance import  get_klines_range
import csv
import pandas as pd
root = os.path.dirname(os.path.abspath(__file__))



symbols = [
	"DOGEUSDT",
	# "NEOUSDT",
	# "LTCUSDT",
	# "ADAUSDT",
	# "ICXUSDT",
	# "VETUSDT",
	# "LINKUSDT",
	# "WAVESUSDT",
	# "HOTUSDT",
	# "IOSTUSDT",
	# "CELRUSDT",
	# "DASHUSDT",
	# "ENJUSDT",
	# "MATICUSDT",
	# "ATOMUSDT",
	# "ONEUSDT",
	# "ANKRUSDT",
	# "PERLUSDT",
	# "KEYUSDT",
	# "FUNUSDT",
	# "NKNUSDT",
	# "STXUSDT",
	# "KAVAUSDT",
	# "ARPAUSDT",
	# "IOTXUSDT",
	# "MDTUSDT",
	# "STMXUSDT",
	# "JSTUSDT",
	# "DOTUSDT",
	# "LUNAUSDT",
	# "RSRUSDT",
	# "YFIIUSDT",
	# "KSMUSDT",
	# "UNIUSDT",
	# "ORNUSDT",
	# "UTKUSDT",
	# "ALPHAUSDT",
	# "ROSEUSDT",
	# "REEFUSDT",
	# "DODOUSDT",
	# "OMUSDT",
	# "ALICEUSDT",
	# "LINAUSDT",
	# "TLMUSDT",
	# "BAKEUSDT",
	# "BURGERUSDT",
	# "SLPUSDT",
	# "ICPUSDT",
]
if __name__ == '__main__':
    
	start_date = '2021-01-01'
	end_date = '2023-05-21'
	for symbol in symbols:
		data = get_klines_range(symbol, "15m", start_date, end_date)

		f = os.path.join(root, 'dataset', f'{symbol}.csv')
		csvfile = open(f, 'w', newline='') 
		
		csvfile.truncate()
		writer = csv.writer(csvfile)
		# write headers
		writer.writerow(['time', 'open', 'high', 'low', 'close', 'volume'])
		closePrices = []
		for klines in data:
			for kline in klines:
				time = kline[0]
				openPrice = float(kline[1])
				highPrice = float(kline[2])
				lowPrice = float(kline[3])
				closePrice = float(kline[4])
				volume = float(kline[5])

				closePrices.append(float(kline[4]))
				strRsi = "-1"
				if len(closePrices) > 14:
					close_series = pd.Series(closePrices)
				
					rsiSeries = momentum.RSIIndicator(close_series, 14).rsi()
					latestRsi = rsiSeries.get(key=rsiSeries.index[-1])
					strRsi = str(latestRsi)
					
					writer.writerow([time, openPrice, highPrice, lowPrice, closePrice, volume, strRsi])
            
		csvfile.close()
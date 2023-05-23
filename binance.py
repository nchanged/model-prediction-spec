import requests
from datetime import datetime
def get_klines(symbol, interval, startTime=None, endTime=None, limit=500):
    """
    Retrieves Kline/candlestick data for a symbol from Binance.

    Parameters:
    symbol (str): The symbol to retrieve Kline/candlestick data for.
    interval (str): The interval of the Kline/candlestick data (e.g. '1m', '1h', '1d').
    startTime (int): The start time of the Kline/candlestick data in milliseconds (optional).
    endTime (int): The end time of the Kline/candlestick data in milliseconds (optional).
    limit (int): The maximum number of Kline/candlestick data points to retrieve (optional, default=500).

    Returns:
    list: A list of Kline/candlestick data points.
    """
    # Define the API endpoint and parameters
    url = 'https://api.binance.com/api/v3/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }

    # Add the start and end times to the parameters if they are specified
    if startTime is not None:
        params['startTime'] = startTime
    if endTime is not None:
        params['endTime'] = endTime

    # Send the API request and get the response
    response = requests.get(url, params=params)

    # Parse the response as JSON and return the Kline/candlestick data
    return response.json()

import time

def get_klines_range(symbol, interval, start_time, end_time):
    """
    Retrieves all Kline/candlestick data for a symbol within a specified time range from Binance.

    Parameters:
    symbol (str): The symbol to retrieve Kline/candlestick data for.
    interval (str): The interval of the Kline/candlestick data (e.g. '1m', '1h', '1d').
    start_time (int): The start time of the Kline/candlestick data in milliseconds.
    end_time (int): The end time of the Kline/candlestick data in milliseconds.

    Returns:
    list: A list of Kline/candlestick data points.
    """

    start_time = int(datetime.strptime(start_time, '%Y-%m-%d').timestamp() * 1000)
    end_time = int(datetime.strptime(end_time, '%Y-%m-%d').timestamp() * 1000)
    

    # Define the maximum number of data points to retrieve per request
    limit = 1000

    # Initialize the list of Kline/candlestick data points
    klines = []

    # Initialize the start time to the specified start time
    current_time = start_time

    # Loop until the current time is greater than or equal to the end time
    while current_time < end_time:
        # Calculate the end time for the current request
        
        start = current_time
        # where and we should add one 24hours
        end = current_time + 24 * 60 * 60 * 1000
        # Retrieve the Kline/candlestick data for the current time range
        response = get_klines(symbol, interval, start, end, limit)


        firstTime = response[0][0]
        lastTime = response[len(response)-1][0]
        # convert to readable time
        firstTime = datetime.fromtimestamp(firstTime/1000).strftime('%Y-%m-%d %H:%M:%S')
        lastTime = datetime.fromtimestamp(lastTime/1000).strftime('%Y-%m-%d %H:%M:%S')
        print(f'firstTime: {firstTime}, lastTime: {lastTime}')

        # Add the Kline/candlestick data to the list
        

        # Update the current time to the end time of the current request
        current_time = end


        yield response
        # Throttle the requests to avoid exceeding the rate limit
        time.sleep(0.2)

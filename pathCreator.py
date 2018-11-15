# Creates a general path for the AlphaVantage API
def createPath (variables, key):
    path = 'http://www.alphavantage.co/query?'
    needed = False
    for key in variables:
        if needed:
            path += '&'
        path += key + '=' + str(variables[key])
        needed = True
    path += '&apikey=' + key
    return path

# Creates the path for the api to call for the SMA
def createRawDataPath (ticker, full, key):
    path = createPath({
        "function": 'TIME_SERIES_DAILY',
        "symbol": ticker
    }, key)
    if not full:
        path += '&outputsize=compact'
    return path

# Creates the path for the SMA indicator
def createSMAPath (ticker, length, key):
    path = createPath({
        'function': 'SMA',
        'symbol': ticker,
        'interval': 'daily',
        'time_period': length,
        'series_type': 'close'
    }, key)
    return path

# Creates the path for the EMA indicator
def createEMAPath (ticker, length, key):
    path = createPath({
        'function': 'EMA',
        'symbol': ticker,
        'interval': 'daily',
        'time_period': length,
        'series_type': 'close',
    }, key)
    return path

def createMACDPath (ticker, key):
    path = createPath({
        'function': 'MACD',
        'symbol': ticker,
        'interval': 'daily',
        'series_type': 'close'
    }, key)
    return path

def createRSIPath (ticker, length, key):
    path = createPath({
        'function': 'RSI',
        'symbol': ticker,
        'interval': 'daily',
        'time_period': length,
        'series_type': 'close'
    }, key)
    return path

def createBBandsPath (ticker, length, key):
    path = createPath({
        'function': 'BBANDS',
        'symbol': ticker,
        'interval': 'daily',
        'time_period': length,
        'series_type': 'close'
    }, key)
    return path

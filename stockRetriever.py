import requests
import json

key = '4DGGMTKG1BP3H37J'

# Standard http GET request
def get (url):
    r = requests.get(url)
    return r.content

# Gets up to 20 years of historical data for the given ticker
# AlphaVantage offers to give a full dataset (up to 20 years of data) or
# you can get a compact dataset (last 100 data points roughly 5 months)
def getStockData (ticker, full=False):
    r = json.loads(get(createPath(ticker, full)))
    data = formatData(r)
    return data

# Changes the data from AlphaVantages format to an easier to handle format
def formatData (dataIn):
    data = {
        'metadata': dataIn['Meta Data'],
        'data': []
    }
    for key in dataIn['Time Series (Daily)'].keys():
        metrics = dataIn['Time Series (Daily)'][key]
        dataPoint = {
            'day': key,
            'open': metrics['1. open'],
            'high': metrics['2. high'],
            'low': metrics['3. low'],
            'close': metrics['4. close'],
            'volume': metrics['5. volume']
        }
        data['data'].append(dataPoint)
    return data

# Creates the path for the api to call
def createPath (ticker, full):
    path = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + str(ticker) + '&apikey=' + key
    if full:
        path += '&outputsize=full'
    return path

# Just an example usage
if __name__ == '__main__':
    results = getStockData('MSFT')
    print(results['data'][0])
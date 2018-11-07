import requests
import json

key = '4DGGMTKG1BP3H37J'

def get (url):
    r = requests.get(url)
    return r.content

# Gets up to 20 years of historical data for the given ticker
# AlphaVantage offers to give a full dataset (up to 20 years of data) or
# you can get a compact dataset (last 100 data points roughly 5 months)
def getStockData (ticker, full=False):
    r = json.loads(get(createPath(ticker, full)))
    return r

def createPath (ticker, full):
    path = 'http://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + str(ticker) + '&apikey=' + key
    if full:
        path += '&outputsize=full'
    return path

# Just an example usage
if __name__ == '__main__':
    results = getStockData('MSFT')
    print(results)
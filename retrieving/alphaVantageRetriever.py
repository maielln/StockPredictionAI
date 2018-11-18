import retrieving.alphaVantageConnector as avc
import time
import retrieving.stockDataFormatter as dataFormatter
import retrieving.cacher as cacher

api_wait = 5    # wait time of 5 seconds after failed call

def getSMA (ticker, length, addedData=None):
    res = avc.retrieveSMA(ticker, length)
    while 'Note' in res:
        print('Waiting for API limits')
        time.sleep(api_wait)
        res = avc.retrieveSMA(ticker, length)
    res = dataFormatter.formatData(res, 'Technical Analysis: SMA', addedData)
    return res

def getEMA (ticker, length, addedData=None):
    res = avc.retrieveEMA(ticker, length)
    while 'Note' in res:
        print('Waiting for API limits')
        time.sleep(api_wait)
        res = avc.retrieveEMA(ticker, length)
    res = dataFormatter.formatData(res, 'Technical Analysis: EMA', addedData)
    return res

def getMACD (ticker, length, addedData=None):
    res = avc.retrieveMACD(ticker)
    while 'Note' in res:
        print('Waiting for API limits')
        time.sleep(api_wait)
        res = avc.retrieveMACD(ticker)
    res = dataFormatter.formatData(res, 'Technical Analysis: MACD', addedData)
    return res

def getRSI (ticker, length, addedData=None):
    res = avc.retrieveRSI(ticker, length)
    while 'Note' in res:
        print('Waiting for API limits')
        time.sleep(api_wait)
        res = avc.retrieveRSI(ticker, length)
    res = dataFormatter.formatData(res, 'Technical Analysis: RSI', addedData)
    return res

def getBBANDS (ticker, length, addedData=None):
    res = avc.retrieveBBANDS(ticker, length)
    while 'Note' in res:
        print('Waiting for API limits')
        time.sleep(api_wait)
        res = avc.retrieveBBANDS(ticker, length)
    res = dataFormatter.formatData(res, 'Technical Analysis: BBANDS', addedData)
    return res

# Gets up to 20 years of historical data for the given ticker
# AlphaVantage offers to give a full dataset (up to 20 years of data) or
# you can get a compact dataset (last 100 data points roughly 5 months)
def getStockRawData (ticker, full=False):
    res = avc.retrieveStockRawData(ticker, full)
    while 'Note' in res:
        print('Waiting for API limits')
        time.sleep(5)
        res = avc.retrieveStockRawData(ticker, full)
    res = dataFormatter.formatData(res, 'Time Series (Daily)')
    res = dataFormatter.formatRawData(res)
    # Cache in the file system to help limit the amount of calls to API
    cacher.cacheRawData(ticker, res)
    return res

# Gets indicator data (SMA, EMA, MACD, RSI, BBANDS)
def getStockMetaData (ticker, addedData=None):
    res = getSMA(ticker, 50, addedData)
    res = getEMA(ticker, 50, res)
    res = getMACD(ticker, res)
    res = getRSI(ticker, 50, res)
    res = getBBANDS(ticker, 50, res) 
    # Cache in the file system to help limit the amount of calls to API
    cacher.cacheMetaData(ticker, res)
    return res

# Just an example usage
if __name__ == '__main__':
    results = getStockMetaData('MSFT')
    print(results[results.keys()[0]])
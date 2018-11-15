import json
import httpHelper as http
import pathCreator as pc
import stockDataFormatter as dataFormatter
import cacher

'''
API limitations:
- 5 calls per minute
- 500 calls per day
'''
key = '4DGGMTKG1BP3H37J'

def getRawData (ticker, full=False):
    return http.get(pc.createRawDataPath(ticker, full, key))

def getSMA (ticker, length):
    return http.get(pc.createSMAPath(ticker, length, key))

def getEMA (ticker, length):
    return http.get(pc.createEMAPath(ticker, length, key))

def getMACD (ticker):
    return http.get(pc.createMACDPath(ticker, key))

def getRSI (ticker, length):
    return http.get(pc.createRSIPath(ticker, length, key))

def getBBANDS (ticker, length):
    return http.get(pc.createBBandsPath(ticker, length, key))

# Gets up to 20 years of historical data for the given ticker
# AlphaVantage offers to give a full dataset (up to 20 years of data) or
# you can get a compact dataset (last 100 data points roughly 5 months)
def getStockRawData (ticker, full=False):
    res = getRawData(ticker, full)
    res = dataFormatter.formatData(res, 'Time Series (Daily)')
    res = dataFormatter.formatRawData(res)
    # Cache in the file system to help limit the amount of calls to API
    cacher.cacheRawData(ticker, res)
    return res

# Gets indicator data (SMA, EMA, MACD, RSI, BBANDS)
def getStockMetaData (ticker, addedData=None):
    res = dataFormatter.formatData(getSMA(ticker, 50), 'Technical Analysis: SMA', addedData)
    res = dataFormatter.formatData(getEMA(ticker, 50), 'Technical Analysis: EMA', res)
    res = dataFormatter.formatData(getMACD(ticker), 'Technical Analysis: MACD', res)
    res = dataFormatter.formatData(getRSI(ticker, 50), 'Technical Analysis: RSI', res)
    res = dataFormatter.formatData(getBBANDS(ticker, 50), 'Technical Analysis: BBANDS', res)
    # Cache in the file system to help limit the amount of calls to API
    cacher.cacheMetaData(ticker, res)
    return res

# Just an example usage
if __name__ == '__main__':
    results = getStockMetaData('MSFT')
    print(results[results.keys()[0]])
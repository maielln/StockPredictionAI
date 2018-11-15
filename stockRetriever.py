import alphaVantageConnector as av
import cacher

def getStockRawData (ticker):
    data = cacher.retrieveRaw(ticker)
    if data == None:
        print('Not found in cache. Calling AlphaVantage API')
        data = av.getStockRawData(ticker)
    return data

def getStockMetaData (ticker):
    data = cacher.retrieveMeta(ticker)
    if data == None:
        print('Not found in cache. Calling AlphaVantage API')
        data = av.getStockMetaData(ticker)
    return data


if __name__ == '__main__':
    results = getStockMetaData('MSFT')
    print(results)

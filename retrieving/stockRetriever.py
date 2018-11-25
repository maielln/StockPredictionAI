import retrieving.alphaVantageRetriever as av
import retrieving.cacher as cacher

# Gets the raw stock data (open, hi, low, close, volume)
def getStockRawData (ticker):
    data = cacher.retrieveRaw(ticker)
    if data == None:
        print('Not found in cache. Calling AlphaVantage API')
        data = av.getStockRawData(ticker)
    return data

# Gets the indicator values (SMA, EMA, MACD, RSI, BBANDS)
def getStockMetaData (ticker):
    data = cacher.retrieveMeta(ticker)
    if data == None:
        print('Not found in cache. Calling AlphaVantage API')
        data = av.getStockMetaData(ticker)
    return data

def getStockPredictionData (ticker):
    data = cacher.retrievePred(ticker)
    if data == None:
        print('Not found in cache. Calling AlphaVantage API')
        data = av.getStockPredData(ticker)
    return data

if __name__ == '__main__':
    results = getStockMetaData('MSFT')
    print(results)

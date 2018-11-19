import retrieving.stockRetriever as sr
import argparse
import json
#import ai.neuralNetwork as nn      Currently commented out because it is broken
import ai.stocks as stocks

parser = argparse.ArgumentParser(description='Stock Predictor')
parser.add_argument('ticker')
parser.add_argument('time')
args = parser.parse_args()

def predict (ticker, time):
    stockRawData = sr.getStockRawData(ticker)
    stockMetaData = sr.getStockMetaData(ticker)
    '''
    This is the method that will start all of the predicting logic.
    This method should pull all the data for the given stock and call
    the neural network to get the likelihood that the stock price is 
    going to go up in value
    '''

if __name__ == '__main__':
    print('Predicting ' + args.ticker + ' for ' + str(args.time) + ' days in the future')
    if not args.ticker in stocks.getStocks():
        print('WARM: Ticker symbol not in recommended stock list.')
        print('Stock List: ' + json.dumps(stocks.getStocks()))
    predict(args.ticker, args.time)
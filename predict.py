import retrieving.stockRetriever as sr
import retrieving.trainingDataTransformer as trans
import argparse
import json
import ai.stocks as stocks

parser = argparse.ArgumentParser(description='Stock Predictor')
parser.add_argument('ticker')
args = parser.parse_args()

def predict (ticker):
    stockPredictionData = trans.getTrainingData(ticker)
    print(stockPredictionData)
    '''
    This is the method that will start all of the predicting logic.
    This method should pull all the data for the given stock and call
    the neural network to get the likelihood that the stock price is 
    going to go up in value
    '''

if __name__ == '__main__':
    print('Predicting ' + args.ticker)
    if not args.ticker in stocks.getStocks():
        print('WARM: Ticker symbol not in recommended stock list.')
        print('Stock List: ' + json.dumps(stocks.getStocks()))
    predict(args.ticker)
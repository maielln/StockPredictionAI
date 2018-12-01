import retrieving.trainingDataTransformer as trans
import argparse
import json
import ai.stocks as stocks
import ai.neuralNetwork as NN
import numpy as np

parser = argparse.ArgumentParser(description='Stock Predictor')
parser.add_argument('ticker')
parser.add_argument('load')
args = parser.parse_args()

def predict (ticker, load):
    NN.NN(load)
    current = [trans.getTrainingData(ticker)['x'][0]]
    print(current)
    print(NN.predict(np.array(current)))


if __name__ == '__main__':
    print('Predicting ' + args.ticker)
    if not args.ticker in stocks.getStocks():
        print('WARM: Ticker symbol not in recommended stock list.')
        print('Stock List: ' + json.dumps(stocks.getStocks()))
    predict(args.ticker, args.load)
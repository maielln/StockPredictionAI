import retrieving.trainingDataTransformer as trans
import ai.stocks as stocks
import ai.neuralNetwork as NN
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--load')
args = parser.parse_args()

def train (saveFile=None):

    data = {
        'x':[],
        'y':[]
    }
    stockTickers = stocks.getStocks()
    for ticker in stockTickers:
        tickerData = trans.getTrainingData(ticker)
        data['x'].extend(tickerData['x'])
        data['y'].extend(tickerData['y'])

    NN.NN(args.load)
    #print(data['x'])
    #print(data['y'])
    NN.train(np.array(data['x']), np.array(data['y']))

    
if __name__ == '__main__':
    print('Training')
    print(args.load)
    train()
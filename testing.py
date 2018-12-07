'''
THIS HAS NOT BEEN TESTED

This is a file for demo purposes. The goal is to run this and make a graph
of sorts to show how successful the program is.
'''

import retrieving.trainingDataTransformer as trans
import ai.stocks as stocks
import ai.neuralNetwork as NN
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('load')
parser.add_argument('ticker')
args = parser.parse_args()

def test ():

    tickerData = trans.getTrainingData(args.ticker)

    NN.NN(args.load)
    correct = 0
    total = 0
    for data in tickerData:
        total += 1
        output = NN.predict(data[x])
        if output > 0.5:
            if data['y'] > 0:
                correct += 1
        else:
            if data['y'] < 0:
                correct += 1
    print('Predicted ' + str(correct) + ' correct out of ' + str(total) + ' : ' + str(float(correct) / total))
    
if __name__ == '__main__':
    test()
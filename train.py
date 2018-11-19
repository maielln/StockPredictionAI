import retrieving.stockRetriever as sr
import argparse
#import ai.neuralNetwork as nn          Commented out because it is broken
import ai.stocks as stocks

parser = argparse.ArgumentParser(description='Trainer for the stock predictor')
parser.add_argument('time')
args = parser.parse_args()

def train (time):
    '''
    This is the method that will start training the neural network
    '''

if __name__ == '__main__':
    print('Training for ' + str(args.time) + ' days in the future')
    train(args.time)
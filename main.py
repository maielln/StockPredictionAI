import retrieving.stockRetriever as sr
import argparse

# Just and example list for blue chip tech stocks
stockList = [
    'AAPL',     # Apple
    'ADBE',     # Adobe
    'ADSK',     # Autodesk
    'ATVI',     # Activision Blizzard
    'FB',       # Facebook
    'GOOGL',    # Alphabet (Google)
    'MSFT',     # Microsoft
    'PFE',      # Pfizer
    'RHT',      # Red Hat
    'VZ',       # Verizon
    'XEROX'     # Xerox
]

parser = argparse.ArgumentParser(description='Stock predicter')
parser.add_argument('function')
parser.add_argument('ticker')
parser.add_argument('--time', default=2)
args = parser.parse_args()

def getStockData (ticker): 
    # Just and example call to get Microsoft stock data
    res = sr.getStockMetaData(ticker)
    print(res)
    res = sr.getStockRawData(ticker)
    print(res)

def predict (ticker, time):
    print('Predicting ' + ticker + ' for ' + str(time) + ' days in the future')
    getStockData(ticker)

def train (ticker, time):
    print('Training ' + ticker + ' for ' + str(time) + ' days in the future')

if __name__ == '__main__':
    if args.function == 'predict':
        predict(args.ticker, args.time)
    elif args.function == 'train':
        train(args.ticker, args.time)



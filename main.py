import stockRetriever as sr

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

# Creating the training and testing sets
testingSet = stockList[:2]
trainingSet = stockList[2:]

if __name__ == '__main__':
    # Just and example call to get Microsoft stock data
    res = sr.getStockData('MSFT', full=True)
    print(res)
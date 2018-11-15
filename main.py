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

if __name__ == '__main__':
    # Just and example call to get Microsoft stock data
    res = sr.getStockMetaData('AAPL')
    print(res)
    res = sr.getStockRawData('AAPL')
    print(res)
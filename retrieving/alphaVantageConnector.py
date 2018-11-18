import json
import retrieving.httpHelper as http
import retrieving.pathCreator as pc

'''
API limitations:
- 5 calls per minute
- 500 calls per day
'''
key = '4DGGMTKG1BP3H37J'

def retrieveStockRawData (ticker, full=False):
    return http.get(pc.createRawDataPath(ticker, full, key))

def retrieveSMA (ticker, length):
    return http.get(pc.createSMAPath(ticker, length, key))

def retrieveEMA (ticker, length):
    return http.get(pc.createEMAPath(ticker, length, key))

def retrieveMACD (ticker):
    return http.get(pc.createMACDPath(ticker, key))

def retrieveRSI (ticker, length):
    return http.get(pc.createRSIPath(ticker, length, key))

def retrieveBBANDS (ticker, length):
    return http.get(pc.createBBandsPath(ticker, length, key))

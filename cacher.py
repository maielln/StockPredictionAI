import os.path as osPath
import json
import time
import os
import stat

CACHE_LOCATION = 'cachedCalls/'
RAW_EXTENSION = '_RAW.json'
META_EXTENSION = '_META.json'
MAX_CACHE_AGE = 60 * 60 * 24  # One day

def cacheRawData (ticker, res):
    filePath = CACHE_LOCATION + ticker + RAW_EXTENSION
    f = open(filePath, 'w')
    f.write(json.dumps(res))
    f.close()
    print('File [' + filePath + '] has been cached')

def cacheMetaData (ticker, res):
    filePath = CACHE_LOCATION + ticker + META_EXTENSION
    f = open(filePath, 'w')
    f.write(json.dumps(res))
    f.close()
    print('File [' + filePath + '] has been cached')

def retrieveRaw (ticker):
    data = None
    path = CACHE_LOCATION + ticker + RAW_EXTENSION
    if osPath.isfile(path) and os.stat(path).st_mtime > time.time() - MAX_CACHE_AGE:
        print('Retrieving from cache')
        f = open(path, 'r')
        data = json.loads(f.read())
    return data

def retrieveMeta (ticker):
    data = None
    path = CACHE_LOCATION + ticker + META_EXTENSION
    if osPath.isfile(path) and os.stat(path).st_mtime > time.time() - MAX_CACHE_AGE:
        print('Retrieving from cache')
        f = open(path, 'r')
        data = json.loads(f.read())
    return data
import retrieving.stockRetriever as sr

def getTrainingData (ticker):
    predictionData = sr.getStockPredictionData(ticker)
    arrayData = transformToArray(predictionData)
    inputData = []
    targetData = []
    for i in range(1, len(arrayData) - 5):
        past = arrayData[i - 1]
        current = arrayData[i]
        future = arrayData[i + 5]
        inputData.append(getInputPoint(current, past))
        targetData.append(getOutputPoint(current, future))
    returnData = {
        'x': inputData,
        'y': targetData
    }
    return returnData

def getInputPoint (current, past):
    current['close'] = float(current['close'])
    current['volume'] = float(current['volume'])
    current['RSI'] = float(current['RSI']) / 100
    current['MACD'] = float(current['MACD'])
    past['volume'] = float(past['volume'])
    past['close'] = float(past['close'])

    closeChange = (past['close'] - current['close']) / current['close']
    closeChange = closeChange * 10 + 0.5
    if closeChange > 1:
        closeChange = 1
    elif closeChange < 0:
        closeChange = 0
    volumeChange = (past['volume'] - current['volume']) / current['volume']
    volumeChange += 0.5
    if volumeChange > 1:
        volumeChange = 1
    elif volumeChange < 0:
        volumeChange = 0
    macd = current['MACD']
    rsi = current['RSI']
    point = [
        closeChange,
        volumeChange,
        macd,
        rsi
    ]
    return point

def getOutputPoint (current, future):
    current['close'] = float(current['close'])
    future['close'] = float(future['close'])

    change = (future['close'] - current['close']) / current['close']
    output = change * 10 + 0.5
    if output > 1:
        output = 1
    elif output < 0:
        output = 0
    '''
    For Binary outputs
    if output > 0.5:
        output = 1
    else:
        output = 0
    '''
    point = [
        output
    ]
    return point

def transformToArray (data):
    keys = data.keys()
    orderedKeys = sorted(keys)
    outputArray = []
    for key in orderedKeys:
        outputArray.append(data[key])
    return outputArray
import retrieving.stockRetriever as sr

def getTrainingData (ticker):
    predictionData = sr.getStockPredictionData(ticker)
    arrayData = transformToArray(predictionData)
    inputData = []
    for point in arrayData:
        newPoint = [
            float(point['close']),
            float(point['volume']),
            float(point['MACD']),
            float(point['RSI'])
        ]
        inputData.append(newPoint)
    targetData = []
    for i in range(len(arrayData) - 5):
        current = float(inputData[i][0])
        future = float(inputData[i + 5][0])
        change = (future - current) / current
        fittedValue = change * 10 + 0.5
        if (fittedValue > 1):
            fittedValue = 1
        elif (fittedValue < 0):
            fittedValue = 0
        targetData.append(fittedValue)
    inputData = inputData[:len(arrayData) - 5]
    returnData = {
        'x': inputData,
        'y': targetData
    }
    return returnData

def transformToArray (data):
    keys = data.keys()
    orderedKeys = sorted(keys)
    outputArray = []
    for key in orderedKeys:
        outputArray.append(data[key])
    return outputArray
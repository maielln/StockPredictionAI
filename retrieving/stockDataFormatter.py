def formatData (dataIn, location, startData=None):
    data = {}
    if not startData == None:
        data = startData
    if not location in dataIn:
        print('"' + location + '" Not found in input.')
        print('Input:')
        print(dataIn)
    for date in dataIn[location]:
        if not date in data:
            data[date] = {}
        for key in dataIn[location][date]:
            data[date][key] = dataIn[location][date][key]
    return data

def formatRawData (dataIn):
    dataOut = {}
    for date in dataIn:
        dataOut[date] = {}
        for key in dataIn[date]:
            dataOut[date][key[3:]] = dataIn[date][key]
    return dataOut
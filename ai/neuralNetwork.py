import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
#from keras.optimizers import SGD
import os

#utilizing a linear model
model = Sequential()
#bias initialization is automatically zero
model.add(Dense(256, input_dim = 4, activation = 'relu'))
model.add(Dense(256, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

#opt = SGD(lr=0.01)

model.compile(optimizer = 'adam',
              loss = 'mean_squared_error')
              #metrics = ['accuracy']) - removed for regression

def NN (saveFile=None):
    if saveFile == None: 
        return
    #checking if file exists
    exists = os.path.isfile(saveFile)
    if exists:
        model.load_weights(saveFile)
        print("Loading model weights from disk. " + saveFile)
    else:
        print("Weights not found, creating new model.")

def train(dataIn, dataOut):
    print("Beginning training.")
    mc = keras.callbacks.ModelCheckpoint('weights/weights{epoch:08d}.h5', save_weights_only=True, period=500)
    model.fit(x=dataIn, y=dataOut, epochs = 5000000000, verbose = 2, callbacks=[mc])
    model.save_weights('model.h5')
    print("Training complete... predicting.")

def predict(dataIn):
    return model.predict(dataIn)
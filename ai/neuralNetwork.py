import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
import os

#utilizing a linear model
model = Sequential()

#creating model with 2 hidden layers
#bias initialization is automatically zero
model.add(Dense(8, input_dim = 4, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

#binary classification
model.compile(optimizer = 'rsmprop',
              loss = 'binary_crossentropy',
              metrics = ['accuracy'])

def NN (dataIn):
    #checking if file exists
    exists = os.path.isfile('model.hdf5')
    if exists:
        model.load_weights('model.hdf5')
        print("Loading model weights from disk.")
    else:
        print("Weights not found, creating new model.")
    
    train(dataIn)
    print(predict(dataIn))
    print("Session complete, saving model weights to disk.")
    #saving the weights
    model.save_weights('model.hdf5')
    print("Successfully saved model weights to disk.")

def train(dataIn):
    print("Beginning training.")
    i = 0
    for i in range(0,8):
        model.fit(dataIn[i], nb_epoch = 500, verbose = 2)
    print("Training complete... predicting.")

def predict(dataIn):
    i = 9
    results = []
    for i in range (9,10):
        results.append(model.predict(dataIn).round())
    return results
#importing TensorFlow and Keras
import tensorflow as tf
import stockDataFormatter.py #can pull from a main instead
from tensorflow import keras

#Libraries that may be useful
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#designing to work with stockDataFormatter.py
#tf.Variable is used in the graph for tensorflow
#tf.random_normal outputs random values from a normal distribution

#some parameters for now, change later
learning_rate = 0.1
num_steps = 500
batch_size = 128
display_step = 100

#NN parameters
num_input = len(stockDataFormatter.formatRawData)
n_hiddenNeurons_1 = 256
n_hiddenNeurons_2 = 256 #random numbers for now

#tf Graph input - placeholders
X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, 784])

#initializing weights
weights = {
    'h1': tf.Variable(tf.random_normal[num_input, n_hiddenNeurons_1]),
    'h2': tf.Variable(tf.random_normal[n_hiddenNeurons_1, n_hiddenNeurons_2]),
    'out': tf.Variable(tf.random_normal[n_hiddenNeurons_2, 10])
}

biases = {
    'b1': tf.Variable(tf.random_normal([n_hiddenNeurons_1])),
    'b2': tf.Variable(tf.random_normal([n_hiddenNeurons_2])),
    'out': tf.Variable(tf.random_normal([10]))
}

#dataset holds: date, raw stock data
#2 layer neural network for now
def neural_net():
#code for neural network here

def train_sess():
#code for training sessions
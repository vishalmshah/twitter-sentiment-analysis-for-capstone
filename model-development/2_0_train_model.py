# This is where we will train our model
# The model will be saved in a .pkl file in the model directory
# We will put the model in the production pipeline after its done

from __future__ import absolute_import, division, print_function
import pprint
import pandas as pd
import os

import tensorflow as tf
from tensorflow import keras

import numpy as np

total_data = pd.read_csv('./model-development/data/training_data.csv', encoding="ISO-8859-1")
# read_csv('file', encoding = "ISO-8859-1")

train = total_data.sample(frac=.5, axis=0)
test = total_data.drop(train.index)

# Setting training and testing data -- there's probably a better way to do this

# print(train.head())
# print(test.head())
x_train = train[['SKL_Sentiment', 'Vader_Neg', 'Vader_Neu', 'Vader_Pos', 'Vader_Compound', 'Sentlex_Pos', 'Sentlex_Neg']].values
y_train = train[['Sentiment']].values
x_test = test[['SKL_Sentiment', 'Vader_Neg', 'Vader_Neu', 'Vader_Pos', 'Vader_Compound', 'Sentlex_Pos', 'Sentlex_Neg']].values
y_test = test[['Sentiment']].values

# Making the tensorflow model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=x_train[0].shape))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',  metrics=['accuracy'])
# running the model
model.fit(x_train, y_train, epochs=2)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

model.save('./model-development/model/twitter_sentiment.model')

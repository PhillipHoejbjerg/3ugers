#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:21:46 2020

@author: Jacobsen
"""


#predicter





import cv2
import tensorflow as tf
CATEGORIES = ["happy", "neutral", "sad"]
def prepare(file):
    IMG_SIZE = 50
    img_array = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
model = tf.keras.models.load_model("CNN.model")
image = 'vh6to.jpg' #your image path
prediction = model.predict(['vh6to.jpg'])
prediction = list(prediction[0])
print(CATEGORIES[prediction.index(max(prediction))])







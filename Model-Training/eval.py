#EVALUATION

#Importing
from tensorflow.keras.applications.resnet import ResNet50, preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import PATHS as PATHS
import pandas as pd
import numpy as np
import ast
import os

#Navigating into the try1 folder
os.chdir(PATHS.TRY2_VAL_05)

#Initialising the generators - test generator is also included
train_gen = ImageDataGenerator(preprocessing_function=preprocess_input).flow_from_directory(PATHS.TRAIN, target_size=(640,480), batch_size=32)
valid_gen = ImageDataGenerator(preprocessing_function=preprocess_input).flow_from_directory(PATHS.VALID, target_size=(640,480), batch_size=32)
test_gen = ImageDataGenerator(preprocessing_function=preprocess_input).flow_from_directory(PATHS.TEST, target_size=(640,480), batch_size=1)

#Creating labels
train_labels = train_gen.classes
valid_labels = valid_gen.classes
test_labels = test_gen.classes

#Loading the saved model
model = load_model('/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition/Model-Training/try2-dropout/value-0.5/weights-improvement-08-0.181.h5')

#Getting the Score
score = model.evaluate(test_gen)
loss = score[0]
accuracy = score[1] * 100

print("The Score on the test set is:")
print("Loss:", loss)
print("Accuracy:", accuracy)

#Plotting and Analysing the Loss and Accuracy Curves
#Opening and Readnb
with open('/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition/Model-Training/try2-dropout/value-0.5/training_history.txt') as f:
    data = f.read()

#Evaluating the string of data and returning as a list
saved_history = ast.literal_eval(data)

#Allocating variables to the loss and accuracy values
training_loss = saved_history['loss']
val_loss = saved_history['val_loss']

training_accuracy = saved_history['categorical_accuracy']
val_accuracy = saved_history['val_categorical_accuracy']

#Range of the x axis in the plot
epochs = range(1,(21))


#Plotting the Loss Curves
plt.plot(epochs, training_loss, 'g', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Loss Curves')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('try2-loss-curve.png')
plt.show()

#Plotting the Accuracy Curves
plt.plot(epochs, training_accuracy, 'g', label='Training Accuracy')
plt.plot(epochs, val_accuracy, 'b', label='Validation Accuracy')
plt.title('Accuracy Curves')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('try2-accuracy-curve.png')
plt.show()




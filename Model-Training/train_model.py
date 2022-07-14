#MODEL TRAINING - TRANSFER LEARNING
#----------------------------------

#Importing the libraries
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, MobileNetV2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from tensorflow.keras import Input
from tensorflow.keras import Model
import PATHS as PATHS
import json
import os


#LOADING THE DATA
#Initialising the Generators
train_gen = ImageDataGenerator(preprocessing_function=preprocess_input).flow_from_directory(PATHS.TRAIN, target_size=(640,480), batch_size=32)
valid_gen = ImageDataGenerator(preprocessing_function=preprocess_input).flow_from_directory(PATHS.VALID, target_size=(640,480), batch_size=32)

#Viewing the classes and the allocated indices
print("Classes in train:", train_gen.class_indices)

#INITIALISING THE MODEL 
"""
When the parameter include_top = False, an input_tensor value muct be given. When include_top = False
it means that the fully connected output layers that make predictions are not loaded, hence, a new 
classifier block consisting new layers can be added to classify according to the problem.

The output of the base_model is the activations of the convolutional layers Conv_1 (Conv2D) directly.
These activations can be used in a classifier or as a feature vector representation. In order for it 
to be used as mentioned above, the first layer of the classifier should be a Pooling layer either max
or avg in order to consolidate all the activations in the form of a vector (feature descriptor) as an
input.

"""
#Initialising the base model
input_tensor = Input(shape=(640,480,3))
base_model = MobileNetV2(weights='imagenet', include_top=False, input_tensor=input_tensor)

#Classifier
x = base_model.output 
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(128, activation='relu')(x)
preds = Dense(26, activation='softmax')(x) # has 26 nodes for 26 classes

#Combining the MobileNetV2 and the coded classifier
model = Model(inputs=base_model.input, outputs=preds)

#Freezes all the layers except for the classifier layers, this means that only the last 5 layers
#interpret the learned features, while the remaining layers use the weights from imagenet.
for layers in model.layers[:-5]:
    layers.trainable = False

#getting the summary of the model
model.summary()

print(os.getcwd())

#Navigating to the correct directory
os.chdir('/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition/Model-Training/try1-overfitting')

#COMPILING AND FITTING THE MODEL
epochs = 20 
optimizer = Adam()
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['categorical_accuracy'])

check_point = ModelCheckpoint(filepath='weights-improvement-{epoch:02d}-{val_categorical_accuracy:.3f}.h5',
                                           monitor="val_categorical_accuracy", mode="max", save_best_only=True)

#Training the model
history = model.fit(train_gen, validation_data=valid_gen, epochs=epochs, callbacks=check_point)

#saving the model
model.save('mobilenetv2_sign_lang.h5')

#saving the history variable into a text file
f = open("training_history.txt","w")
f.write(str(history.history))
f.close()

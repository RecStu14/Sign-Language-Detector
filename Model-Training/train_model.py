#TRAINING PROCESS

#Importing
import tensorflow as tf
import matplotlib.pyplot as plt
import PATHS as PATHS

#Processes records written in TFRecord Format
raw_train_dataset = tf.data.TFRecordDataset(PATHS.TRAIN_TFR)

# Create a dictionary describing the features.
feature_description = {
    'label': tf.io.FixedLenFeature([], tf.int64),
    'features': tf.io.FixedLenFeature([], tf.string),
}


for images, labels in raw_train_dataset.take(1):  # only take first element of dataset
    numpy_images = images.numpy()
    numpy_labels = labels.numpy()


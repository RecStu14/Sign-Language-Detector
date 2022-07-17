#PATHS
import os

#Dataset Paths
TRAIN = '/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition/American Sign Language Letters/train'
VALIDATION = '/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition/American Sign Language Letters/valid'
TEST = '/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition/American Sign Language Letters/test'

#LABEL MAP FILES
TRAIN_LABEL_MAP = os.path.join(TRAIN, 'Letters_label_map.pbtxt')
VALID_LABEL_MAP = os.path.join(VALIDATION, 'Letters_label_map.pbtxt')
TEST_LABEL_MAP = os.path.join(TEST, 'Letters_label_map.pbtxt')

#TFRECORDS 
TRAIN_TFR = os.path.join(TRAIN, 'Letters.tfrecord')
VALID_TFR = os.path.join(VALIDATION, 'Letters.tfrecord')
TEST_TFR = os.path.join(TEST, 'Letters.tfrecord')
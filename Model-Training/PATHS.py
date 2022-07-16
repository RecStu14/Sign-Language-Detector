#PATHS
#Consolidated Paths that can be imported 
import os

ROOT_DIR = '/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition'

#DATASET DIRECTORY
DATASET_DIR = "/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition/American-Sign-Language-Letters"
TRAIN = "/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition/American-Sign-Language-Letters/train"
VALID = "/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition/American-Sign-Language-Letters/valid"
TEST = "/Users/sankeerthana/Documents/GitHub/Sign-Language-Recognition/American-Sign-Language-Letters/test"

#MODEL TRAINING DIRECTORY
MODEL_TRAINING = os.path.join(ROOT_DIR,'Model-Training')
TRY1 = os.path.join(MODEL_TRAINING, 'try1-overfitting')
TRY2 = os.path.join(MODEL_TRAINING, 'try2-dropout')
TRY2_VAL_02 = os.path.join(TRY2, 'value-0.2')
TRY2_VAL_05 = os.path.join(TRY2, 'value-0.5')
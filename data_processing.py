#DATA PROCESSING 
#This code contains the step by step functions to run after downloading the COCO JSON version of 
#the dataset.

import os
import helper_fxns as HELPER

"""
After downloading the COCO JSON version of the dataset, you would need to group all the images into
folders where the folder name is the label as we intent to use ImageDataGenerator in the later stages.

"""

#creating the folders
HELPER.create_folders(path='/Users/sankeerthana/Documents/sign_lang_detector/American Sign Language Letters/test')
HELPER.create_folders(path='/Users/sankeerthana/Documents/sign_lang_detector/American Sign Language Letters/train')
HELPER.create_folders(path='/Users/sankeerthana/Documents/sign_lang_detector/American Sign Language Letters/valid')

"""
After which, we would need to move these images into the folders just created. 
Tip: Save a backup before moving the images, just in case, any images get lost.
"""

#moving the images
HELPER.moving_imgs(path='/Users/sankeerthana/Documents/sign_lang_detector/American Sign Language Letters/test')
HELPER.moving_imgs(path='/Users/sankeerthana/Documents/sign_lang_detector/American Sign Language Letters/train')
HELPER.moving_imgs(path='/Users/sankeerthana/Documents/sign_lang_detector/American Sign Language Letters/valid')

#MOVING IMAGES
#This python consists of code to move the images into their labelled folders in order to use
#ImageDataGenerator.

#Importing
import os, shutil


path = '/Users/sankeerthana/Documents/sign_lang_detector/American Sign Language Letters/test'

#getting the contents of the folder
contents = os.listdir(path)

#removing the annotations.json from the list
contents.remove('_annotations.coco.json')

images = {}

for file in contents:
    label = file[0]
    print(label)




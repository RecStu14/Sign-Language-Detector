#HELPER FUNCTIONS
import os, shutil

#deleting all the .jpg files 
def delete_jpg(path):
    contents = os.listdir(path)
    counter = 0

    for img in contents:
        if img[-4:] == '.jpg':
            os.remove(img)
            counter += 1

    print('Successfully deleted ',counter,'JPG Images!')

#to create folders which work as labels in the classifier in train, test and valid folders
def create_folders(path):
    folder_names = ['A', 'B', 'C', 'D', 'E','F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y','Z']

    os.chdir(path)
    counter = 0

    for folder in folder_names:
        os.mkdir(str(path + str(folder)))
        counter += 1

    print('Successfully created',counter,'folders!')

#counts the number of .jpg images in the folder
def count_jpg(path):
    contents = os.listdir(path)
    counter = 0

    for img in contents:
        if img[-4:] == '.jpg':
            counter += 1

    print('There are a total of',counter,'JPG Images in this folder!')

count_jpg('/Users/sankeerthana/Documents/sign_lang_detector/American Sign Language Letters/valid')


##to move the images into their labelled folders in order to use ImageDataGenerator.
def moving_imgs(path):
    #getting the contents of the folder
    contents = os.listdir(path)

    #removing the annotations.json from the list
    contents.remove('_annotations.coco.json')
    counter = 0 

    for file in contents:
        label = file[0]

        if file[-4:] == '.jpg':
            source = os.path.join(path, file)
            destination = os.path.join(path,label,file)
            shutil.move(source,destination)
            counter += 1
        else:
            pass

    print('Successfully moved',counter,'Images into their respective folders!')
    


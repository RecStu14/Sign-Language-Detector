#HELPER FUNCTIONS
import os

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

#sounts the number of .jpg images in the folder
def count_jpg(path):
    contents = os.listdir(path)
    counter = 0

    for img in contents:
        if img[-4:] == '.jpg':
            counter += 1

    print('There are a total of',counter,'JPG Images in this folder!')




    


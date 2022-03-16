import os
from random import choice
import shutil

#arrays to store file names
imgs =[]
xmls =[]

#setup dir names
trainPath = 'C:/Users/Desktop/split_data/images/train'
valPath = 'C:/Users/Desktop/split_data/images/valid'
testPath = 'C:/Users/Desktop/split_data/images/test'
crsPath = 'C:/Users/Desktop/split_data' #dir where images and annotations stored

#setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
train_ratio = 0.70
val_ratio = 0.20
test_ratio=0.10
#total count of imgs
totalImgCount = len(os.listdir(crsPath))/2

#soring files to corresponding arrays
for (dirname, dirs, files) in os.walk(crsPath):
    for filename in files:
        if filename.endswith('.txt'):
            xmls.append(filename)
        else:
            imgs.append(filename)
#counting range for cycles
countForTrain = int(len(imgs)*train_ratio)
countForVal = int(len(imgs)*val_ratio)
countFortest = int(len(imgs)*test_ratio)
print("training images are : ",countForTrain)
print("Validation images are : ",countForVal)
print("test images are : ",countFortest)

trainimagePath = 'C:/Users/Desktop/split_data/images/train'
trainlabelPath = 'C:/Users/Desktop/split_data/labels/train'
valimagePath = 'C:/Users/Desktop/split_data/images/valid'
vallabelPath = 'C:/Users/Desktop/split_data/labels/valid'
valimagetest = 'C:/Users/Desktop/split_data/images/test'
vallabeltest = 'C:/Users/Desktop/split_data/labels/test'
# cycle for train dir
for x in range(countForTrain):
    fileJpg = choice(imgs)  # get name of random image from origin dir
    fileXml = fileJpg[:-4] + '.txt'  # get name of corresponding annotation file

    # move both files into train dir
    shutil.move(os.path.join(crsPath, fileJpg), os.path.join(trainimagePath, fileJpg))
    shutil.move(os.path.join(crsPath, fileXml), os.path.join(trainlabelPath, fileXml))
    # shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(trainimagePath, fileJpg))
    # shutil.copy(os.path.join(crsPath, fileXml), os.path.join(trainlabelPath, fileXml))

    # remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)

# cycle for test dir
for x in range(countForVal):
    fileJpg = choice(imgs)  # get name of random image from origin dir
    fileXml = fileJpg[:-4] + '.txt'  # get name of corresponding annotation file

    # move both files into train dir
    shutil.move(os.path.join(crsPath, fileJpg), os.path.join(valimagePath, fileJpg))
    shutil.move(os.path.join(crsPath, fileXml), os.path.join(vallabelPath, fileXml))
    # shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(valimagePath, fileJpg))
    # shutil.copy(os.path.join(crsPath, fileXml), os.path.join(vallabelPath, fileXml))
    # remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)

for x in range(countFortest):
    fileJpg = choice(imgs)  # get name of random image from origin dir
    fileXml = fileJpg[:-4] + '.txt'  # get name of corresponding annotation file

    # move both files into train dir
    shutil.move(os.path.join(crsPath, fileJpg), os.path.join(valimagetest, fileJpg))
    shutil.move(os.path.join(crsPath, fileXml), os.path.join(vallabeltest, fileXml))
    # shutil.copy(os.path.join(crsPath, fileJpg), os.path.join(trainimagePath, fileJpg))
    # shutil.copy(os.path.join(crsPath, fileXml), os.path.join(trainlabelPath, fileXml))

    # remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)

# rest of files will be validation files, so rename origin dir to val dir
# os.rename(crsPath, valPath)
#shutil.move(crsPath, valPath)
print('completed')

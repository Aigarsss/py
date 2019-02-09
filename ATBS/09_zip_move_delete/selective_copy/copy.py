#! python3
# Selective Copy
# Write a program that walks through a folder tree and searches 
# for files with a certain file extension (such as .pdf or .jpg). 
# Copy these files from whatever location they are in to a new folder.

import os, shutil

def copyExt(folder, ext, dest):
# change the working dir to folder provided
    os.chdir(folder)
# get the folder and its path usin os
    newDir = os.getcwd()

# Check if new dir exists
    if not os.path.exists(dest):
        os.mkdir(dest)

# walk the folder with os.walk() and look for files woth certain ext
    for foldername, subfolders, filenames in os.walk(newDir):
        for filename in filenames:
            if filename.endswith(ext):
                # print text for safety
                print(filename + ' is being copied to ' + dest)
                # copy the files from the location to a new folder using shutil
                shutil.copy((os.path.join(foldername, filename)), dest)


copyExt('.\\', '.txt', 'C:\\Users\\AA\\Desktop\\copied_files')


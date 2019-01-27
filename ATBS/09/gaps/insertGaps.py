#! python3

#follow up on removeGaps.py

# As an added challenge, write another program that can insert gaps into 
# numbered files so that a new file can be added.
# insertGap(folder to change, word that file starts with, starter char - if 3, 3 will be gapped, length of the gap - if 2 - 1 2  5 6):

import os, shutil, re

def insertGap(folder, word, starter, length):
    # define path
    absPath = os.path.abspath(folder)
    
    files = []
    for foldername, subfolders, filenames in os.walk(absPath):
        #BACKUPS
        bakFolder = os.path.join(absPath, foldername + '_bak_insert')
        if not os.path.exists(bakFolder):
            os.mkdir(bakFolder)
        for filename in filenames:
            shutil.copy(os.path.join(absPath, filename), bakFolder)
        
        for filename in filenames:
            if filename.startswith(word):
                files.append(filename)

    print('You selected to start the gap at number ' + str(starter) + ' and have ' + str(length) + ' gaps in between')


    files = files[starter-1:]
    
    #renaming files, so that the contents arent overwritten
    tempFilenameList = []
    for i in range(len(files)):
        # define the regex
        regex = re.compile(r'\d{3}')
        # get the old file names
        oldFilePath = os.path.join(absPath, files[i])
        tempFilename = re.sub(regex, regex.search(files[i]).group().lstrip('0'), files[i])
        tempFilepath = os.path.join(absPath, tempFilename)
        # temporary rename the files, so that namings dont clash
        tempFilenameList.append(tempFilename)
        shutil.move(oldFilePath, tempFilepath)

    #loop through the new list of files
    for i in range(len(tempFilenameList)):
        # define the regex
        regex = re.compile(r'\d{1,3}')
        # get the old file names
        oldFilePath = os.path.join(absPath, tempFilenameList[i])
        replacedFilename = re.sub(regex, str(int(regex.search(tempFilenameList[i]).group()) + length).rjust(3, '0'), tempFilenameList[i])

        # create the new file names
        newFilePath = os.path.join(absPath, replacedFilename)
        print(files[i] + ' is being renamed to ' + os.path.basename(newFilePath))
        
        # print(os.path.basename(oldFilePath) +' to ' + os.path.basename(tempFilepath))
        #move the files to create the gap
        shutil.move(oldFilePath, newFilePath)

insertGap('.\\gapinsert', 'spam', 3, 2)
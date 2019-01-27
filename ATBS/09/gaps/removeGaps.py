#! python3

# Write a program that finds all files with a given prefix, such as 
# spam001.txt, spam002.txt, and so on, in a single folder and 
# locates any gaps in the numbering (such as if there is a spam001.txt 
# and spam003.txt but no spam002.txt). Have the program rename all the 
# later files to close this gap.

# As an added challenge, write another program that can insert gaps into 
# numbered files so that a new file can be added.

#folder gets backed up before, but make sure it does not exist.

import os, shutil, re

def fillGaps(folder, word):
    absPath = os.path.abspath(folder)
    # give the folder and walk it
    files = []
    for foldername, subfolders, filenames in os.walk(absPath):
        #BACKUPS
        bakFolder = os.path.join(absPath, foldername + '_bak')
        if not os.path.exists(bakFolder):
            os.mkdir(bakFolder)

        for filename in filenames:
            shutil.copy(os.path.join(absPath, filename), bakFolder)

            # find all files with a certain prefix
            if filename.startswith(word):
                files.append(filename)
        #print(files)

# regex. get the last correct number in sequence. 
    i = 0
    while i <= len(files):
        regex = re.compile(r'\d{3}')
        if int(regex.search(files[i]).group()) + 1 == int(regex.search(files[i+1]).group()):
            i += 1
            continue
        lastOkNum = int(regex.search(files[i]).group().lstrip('0'))
        lastOkIndex = i
        break


# with shutil 'move' the files so that they are renamed according to the gap
    for i in range(lastOkIndex+1,len(files)):
        #absolute path of files:
        absPath = os.path.abspath(folder)
        oldFilePath = os.path.join(absPath, files[i])

        #assign new name to the filenames
        regex = re.compile(r'\d{3}')
        replacedName = re.sub(regex, str(i).rjust(3,'0'), files[i])

        #print(replacedName)
        #define new file path and name
        newFilePath = os.path.join(absPath, replacedName)
        
        #move the files
        print(oldFilePath + ' is being renamed to ' + newFilePath)
        shutil.move(oldFilePath, newFilePath)



fillGaps('.\\gap', 'spam')
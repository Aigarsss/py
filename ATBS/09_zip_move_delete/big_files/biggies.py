#! python

# It’s not uncommon for a few unneeded but humongous files or folders to 
# take up the bulk of the space on your hard drive. If you’re trying to free 
# up room on your computer, you’ll get the most bang for your buck by deleting 
# the most massive of the unwanted files. But first you have to find them.

# Write a program that walks through a folder tree and searches for exceptionally 
# large files or folders—say, ones that have a file size of more than 100MB. 
# (Remember, to get a file’s size, you can use os.path.getsize() from the os module.) 
# Print these files with their absolute path to the screen.

import os

def biggies(folder):
    #change working dir
    #folder = os.path.abspath(folder)
    os.chdir(folder)
    workDir = os.getcwd()


    #walk the dir with os.walk()
    for foldername, subfolders, filenames in os.walk(workDir):
        for filename in filenames:
            filesize = os.path.getsize(filename)
            if filesize > 1000000:
                print(filename + ' size is ' + str(round(filesize/1024, 2)) + ' KB')


biggies('C:\Downloads\php\Adobe XD CC 2018 v1.0.12 + Crack (Working Exclusive)')
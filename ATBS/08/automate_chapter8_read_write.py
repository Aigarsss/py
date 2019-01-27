#! python

################## Chapter 8 – Reading and Writing Files

#import os
# print(os.path.join('usr','bin','spam'))

# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
#     print(os.path.join('C:\\Users\\Aigars', filename))

# print(os.getcwd()) # get working dir
# os.chdir('C:\\Windows\\System32') # change dir
# print(os.getcwd())

#os.makedirs('C:\\New_folder') makes a new dir

#http://docs.python.org/3/library/os.path.html

# print(os.path.abspath('.'))
# print(os.path.abspath('.\\.vscode'))
# print(os.path.isabs('.'))

# print(os.path.relpath('C:\\Windows', 'C:\\')) # how to get to 1 from 2 using reltive path
# print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
# print(os.path.relpath('C:\\Windows'))

# path = 'C:\\Windows\\System32\\calc.exe'
# print(os.path.basename(path))
# print(os.path.dirname(path))
# print(os.path.split(path)) # gives a tuple with both values

# print(path.split(os.path.sep)) #seperates the directories in a list

## sizes
# path1 = os.path.join(os.getcwd(), 'automate.py')
# print(os.path.getsize(path1)) # get size
# path2 = os.getcwd()
# print(os.listdir(path2)) # get list of dirs/files

#total size of folder
# totalSize = 0
# for file in os.listdir('C:\\Users\\AA\\Dropbox\\code\\code\\py'):
#     totalSize += os.path.getsize(os.path.join('C:\\Users\\AA\\Dropbox\\code\\code\\py', file))
# print(totalSize)

# path = 'C:\\Users\\AA\\Dropbox\\code\\code\\py'
# print(os.path.exists(path))
# print(os.path.isdir(path))
# print(os.path.isfile(path))

# helloFile = open('C:\\Users\\AA\\Dropbox\\code\\code\\py\\hello.txt', 'r')
# helloContent = helloFile.read()
# print(helloContent)

# helloFile = open('C:\\Users\\AA\\Dropbox\\code\\code\\py\\hello.txt', 'r')
# helloContent = helloFile.readlines()
# print(helloContent)

# baconFile = open('bacon.txt', 'w') #write to file, if no file exists, create new
# baconFile.write('Hello world!\n')
# baconFile.close()
# baconFile = open('bacon.txt', 'a') # append to file
# baconFile.write('Bacon is not a vegetable')
# baconFile.close()
# baconFile = open('bacon.txt')
# content = baconFile.read()
# baconFile.close()
# print(content)

######## shelving variables
# import shelve
# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close() # this creates the mydata.bak/dat/dir files

# shelfFile = shelve.open('mydata')
# print(type(shelfFile))
# print(shelfFile['cats'])
# shelfFile.close()

#### Saving variables with the pprint.pformat() function
# import pprint
# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# print(pprint.pformat(cats))

# fileObj = open('myCats.py', 'w')
# fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
# fileObj.close()

# import myCats
# print(myCats.cats[0]['name'])






#! python3

# the program finds al the lines that contain the user input
# python reg_search.py

import os, re

def searchForLines(folder, term):
    # change dir to the folder
    os.chdir(folder)
    newDir = os.getcwd()
    result = ''

    # get all txt files
    files = [a for a in os.listdir(newDir) if '.txt' in a]
       
    # loop through the text files contents 
    for i in files:
        contents = open(i, 'r')
           # add lines that have term to the result
        for line in contents.readlines():
            if term in line:
                result += line.rstrip() + ': Found in {}'.format(i) + '\n'
        #print(contents.read())
        contents.close()

    return result


print(searchForLines('.\\', '22'))
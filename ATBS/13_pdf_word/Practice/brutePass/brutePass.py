#! python3

#Using the file-reading skills you learned in Chapter 8, 
# create a list of word strings by reading this file. 
# Then loop over each word in this list, passing it to the 
# decrypt() method. If this method returns the integer 0, 
# the password was wrong and your program should continue to 
# the next password. If decrypt() returns 1, then your program 
# should break out of the loop and print the hacked password. You 
# should try both the uppercase and lower-case form of each word. (On my 
# laptop, going through all 88,000 uppercase and lowercase words from the dictionary 
# file takes a couple of minutes. This is why you shouldn’t use a simple English word 
# for your passwords.)

import PyPDF2

file = open('dictionary.txt', 'r')
pdfFile = open('encryptedminutes.pdf', 'rb')
pdfRead = PyPDF2.PdfFileReader(pdfFile)

for passw in file.readlines():
    passw = passw.strip('\n')
    if pdfRead.decrypt(passw.lower()):
        print('Correct pass is ' + passw.lower())
        break
    elif pdfRead.decrypt(passw.upper()):
        print('Correct pass is ' + passw.upper)
        break
    else:
        continue
    


file.close()
pdfFile.close()

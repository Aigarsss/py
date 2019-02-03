# Write a program that finds all encrypted PDFs in a folder 
# (and its subfolders) and creates a decrypted copy of the PDF 
# using a provided password. If the password is incorrect, the 
# program should print a message to the user and continue to the 
# next PDF.

#  python pdfParanoia2.py

import os, PyPDF2, sys



for foldernames, subfolders, filenames in os.walk('.\\'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            name = os.path.join(os.path.abspath(foldernames), filename)
            if PyPDF2.PdfFileReader(open(name, 'rb')).isEncrypted:
                print('do x with ' + filename)
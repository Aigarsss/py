# Using the os.walk() function from Chapter 9, write a script 
# that will go through every PDF in a folder (and its subfolders) 
# and encrypt the PDFs using a password provided on the command 
# line. Save each encrypted PDF with an _encrypted.pdf suffix 
# added to the original filename. Before deleting the original file, 
# have the program attempt to read and decrypt the file to ensure that 
# it was encrypted correctly.

# python pdfParanoia.py sword

import os, PyPDF2, sys, shutil

# put the pass in a variable
if len(sys.argv) < 1:
    print('Please provide an CMD argument for pass')
else:
    password = ''.join(sys.argv[1:])
    #print(password)
    # go through all the pdfs and get the list
    files = []
    for foldername, subfolders, filenames in os.walk('.\\'):
        for filename in filenames:
            if filename.endswith('.pdf'):
                files.append(os.path.join(os.path.abspath(foldername), filename))
    #print(files)

    # get the pdfs
    for file in files:
        pdfFile = open(file, 'rb')
        readPdf = PyPDF2.PdfFileReader(pdfFile)
        writePdf = PyPDF2.PdfFileWriter()

        # copy the pages from opened file to new
        for pageNum in range(readPdf.numPages):
            writePdf.addPage(readPdf.getPage(pageNum))
        # encrypt pdf
        writePdf.encrypt(password)
        # save as new file with same name, but with _encrypted
        resultPdf = open(file.strip('.pdf') + '_encrypted.pdf', 'wb')
        writePdf.write(resultPdf)
        # pdfFile.close()
        resultPdf.close()

        # program must read the file and check that it can be decrypted
        if PyPDF2.PdfFileReader(open(file.strip('.pdf') + '_encrypted.pdf', 'rb')).decrypt(password):
            print('Decription of file ' + os.path.basename(file.strip('.pdf') + '_encrypted.pdf') + ' fine, removing originals')
            # shutil.remove(file) # I will leave this commented out.
        else:
            print('Problem found wiht the encryption')

   

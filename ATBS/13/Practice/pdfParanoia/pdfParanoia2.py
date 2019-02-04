# Write a program that finds all encrypted PDFs in a folder 
# (and its subfolders) and creates a decrypted copy of the PDF 
# using a provided password. If the password is incorrect, the 
# program should print a message to the user and continue to the 
# next PDF.

#  python pdfParanoia2.py

import os, PyPDF2


for foldernames, subfolders, filenames in os.walk('.\\'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            name = os.path.join(os.path.abspath(foldernames), filename)
            if PyPDF2.PdfFileReader(open(name, 'rb')).isEncrypted:
                    print('File ' + os.path.basename(name) +  ' found.')
                    password =  input('Enter pass to use for decrypt: ')

                    pdfFile = open(name, 'rb')
                    readPdf = PyPDF2.PdfFileReader(pdfFile)
                    writePdf = PyPDF2.PdfFileWriter()

                    if readPdf.decrypt(password):
                        for pageNum in range(readPdf.numPages):
                            writePdf.addPage(readPdf.getPage(pageNum))
                        
                        resultPdf = open(name.strip('.pdf') + '_unencrypted.pdf' , 'wb')
                        writePdf.write(resultPdf)
                        resultPdf.close()
                        print(os.path.basename(name.strip('.pdf')) + '_unencrypted.pdf is now available'  )

                    else:
                        print('Password provided was wrong.')

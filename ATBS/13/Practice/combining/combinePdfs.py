#! python3
# python combinePdfs.py
# combinePdfs.py - Combines all the PDFs in the current working directory into
# into a single PDF.

# Find all PDF files in the current working directory.
# Sort the filenames so the PDFs are added in order.
# Write each page, excluding the first page, of each PDF to the output file.
# In terms of implementation, your code will need to do the following:
# Call os.listdir() to find all the files in the working directory and remove any non-PDF files.
# Call Python’s sort() list method to alphabetize the filenames.
# Create a PdfFileWriter object for the output PDF.
# Loop over each PDF file, creating a PdfFileReader object for it.
# Loop over each page (except the first) in each PDF file.
# Add the pages to the output PDF.
# Write the output PDF to a file named allminutes.pdf.

import os, PyPDF2

# Get all pdf name & sort
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower) # this is so that the capital letters dont get sorted deifferently

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the pdf files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        # loop through all the pages (except first) and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

            
# Save the resuting pdf to file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
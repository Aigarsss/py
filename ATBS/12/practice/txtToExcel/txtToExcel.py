#! python3

import openpyxl, os

# get the filenames in a list
files = os.listdir('.\\')
files = [i for i in files if i.endswith('.txt')]

# create the excel
wb = openpyxl.Workbook()
sheet = wb.active

# create counter for the column
counter = 0

for file in files:
    counter += 1 # so that column starts at 1
    readFile = open(file, 'r')
    read = readFile.readlines()
    readFile.close()

    for line in range(len(read)):
        sheet.cell(row = line + 1 , column = counter).value = read[line]

wb.save('txtToExcel.xlsx')






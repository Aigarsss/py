#! python3
# Write a program that performs the tasks of the previous 
# program in reverse order: The program should open a spreadsheet 
# and write the cells of column A into one text file, the cells of 
# column B into another text file, and so on.

import os, openpyxl


wb = openpyxl.load_workbook('txtToExcel.xlsx')
sheet = wb.active

colCount = sheet.max_column
rowCount = sheet.max_row
fileCounter = 0

for col in range(1, colCount + 1):
    fileCounter +=1
    contents = []
    for row in range(1, rowCount + 1):
        contents.append(sheet.cell(row = row, column = col).value)
    # # writing a file
    file = open('Excel_to_file_' + str(fileCounter) + '.txt', 'w')
    file.write(''.join(contents))
    file.close()

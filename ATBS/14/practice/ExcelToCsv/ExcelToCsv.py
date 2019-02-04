#! python3
# Excel-to-CSV Converter
# write a program that reads all the Excel files in the current working directory and outputs them as CSV files.
# A single Excel file might contain multiple sheets; you’ll have to create 
# one CSV file per sheet. The filenames of the CSV files should be 
# <excel filename>_<sheet title>.csv, where <excel filename> is the filename 
# of the Excel file without the file extension (for example, 'spam_data', 
# not 'spam_data.xlsx') and <sheet title> is the string from the Worksheet 
# object’s title variable.

#python ExcelToCsv.py

import csv, os, openpyxl

# get a list of the excel files in the dir
files = [i for i in os.listdir(os.getcwd()) if i.endswith('.xlsx')]

for file in files:
    # read an excel file
    wb = openpyxl.load_workbook(file)

    for sheetname in wb.sheetnames:
        sheet = wb[sheetname]
        # open the csv for writing
        outputFile = open(file.rstrip('.xlsx') + '_' + sheetname + '.csv', 'w', newline='')
        outputWriter = csv.writer(outputFile)
        # get the first row values and put them in a list

        for row in range(1, sheet.max_row + 1):
            line = []
            for col in range(1, sheet.max_column + 1):
                line.append(sheet.cell(row = row, column = col).value) 
    
            # write the csv file
            outputWriter.writerow(line)
        #outputFile.close()
#! python3
# python removeCsvHeader.py

# The program will need to open every file with the .csv extension
# in the current working directory, read in the contents of 
# the CSV file, and rewrite the contents without the first row 
# to a file of the same name. This will replace the old contents 
# of the CSV file with the new, headless contents.

import os, csv
os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory
for csvFilename in os.listdir('.\\'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvFilename)

    # Read the csv file in (skipping first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # skip
        csvRows.append(row)
    csvFileObj.close()

    # Write out the csv file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()

# Chapter 14 – Working with CSV Files and JSON Data
'''
import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
print(exampleData[0][1])

# Reading data from reader in a for loop
import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))


# Writer objects
import csv
outputFile = open('output.csv', 'w', newline='') # For technical reasons, if you forget to set the newline argument, the rows in output.csv will be double-spaced
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam, spam', 'eggs'])
outputWriter.writerow([1, 2])
outputFile.close()

# The delimiter and lineterminator Keyword Arguments
import csv
csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])


### JSON and APIs
# Reading JSON with the loads() Function
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}' # string and double quotes
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)




'''



# Writing JSON with the dumps() Function
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
import json
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
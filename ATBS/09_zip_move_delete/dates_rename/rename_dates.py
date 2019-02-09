#! python3

# rename_dates.py - renames filenames with american MM-DD-YYYY date format 
# to european DD-MM-YYYY

import os, re, shutil

# Create a regex that matches the files with US formats
datePattern = re.compile(r'''
        ^(.*?)
        ((0|1)?\d)- # starts with 0 or 1 + digit
        ((0|1|2|3)?\d)- # starts with 0 or 1 or 2 or 3 + digit
        ((19|20|)\d{2}) # year, starts wit 19 or 20 + 2 digits
        (.*)$ # ends with anything
''', re.VERBOSE)

# loop over the files in the working directory

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # skip files without a date
    #print(mo.group())
    if mo == None:
        continue
    
    #get the different prts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the european style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
    # get the full, absolute paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    
    # rename the files
    print('Renaming {} to {}'.format(amerFilename, euroFilename))
    #shutil.move(amerFilename,euroFilename)
    #shutil.copy(amerFilename,euroFilename) # this is safer

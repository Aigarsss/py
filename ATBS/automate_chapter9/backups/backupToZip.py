#! python3
# backupToZip.py - copies an entire folder and its contents into a zip
# file whose filename increments
# python backupToZip.py

import zipfile, os

def backupToZip(folder):
    #backup the entire contents of the folder into a zip

    folder = os.path.abspath(folder)
    # figure out the filename this code should use based on
    # what files already exist

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    # create zip file
    print('Creating {}'.format(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # walk the entire foder tree and compress the files in each folder
    for folderName, subfolder, filenames in os.walk(folder):
        print('Adding files in {}'.format(folderName))
        # add the current folder to the zip file
        backupZip.write(folderName)
        # add all the files in this folder to the zip file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # skip the zip fies
            backupZip.write(os.path.join(folderName, filename))
    backupZip.close()
    print('Done')


backupToZip('.')
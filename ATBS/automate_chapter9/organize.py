############### chapter 9 - Organizing Files

# import shutil, os

# shutil.copy('..\\file_for_copy.txt', '.\\') # copies
# shutil.copy('..\\file_for_copy.txt', '.\\file_for_copy_renamed.txt') # copies and renames

# shutil.copytree('<dir>','<target dir>') # copies the whole folder, can be used for backup

# shutil.move('<dir>','<target dir>') # moves to target

# os.remove(path) #same as os.unlink(path). deletes file at path
# os.rmdir(path) # deletes folder at path. must be empty
# shutil.rmtree(path) # deletes the folder at path and files in it

### deleting to trash (not permanent)
# import send2trash #needs to be iported pip install send2trash
# file = open('bacon.txt', 'a')
# file.write('what?')
# file.close()
# send2trash.send2trash('bacon.txt')

# import os
# #print(list(os.walk('.\\delicious')))

# for folderName, subfolders, filenames in os.walk('.\\delicious'):
#     print('The current folder is ' + folderName)

#     for subfolder in subfolders:
#         print('subfolder of ' + folderName + ': ' + subfolder)
#     for file in filenames:
#         print('file inside ' + folderName + ': '+ file)
    
#     print('')

# import zipfile, os

# exampleZip = zipfile.ZipFile('zips.zip')
# print(exampleZip.namelist())
# spamInfo = exampleZip.getinfo('spam.txt')
# print(spamInfo.file_size) # real size
# print(spamInfo.compress_size) # zipped size
# exampleZip.close()

# import zipfile, os
# exampleZip = zipfile.ZipFile('zips.zip') 
# #exampleZip.extractall() #extracting all the files
# exampleZip.extract('spam.txt') # a folder can be added to extract it somewhere else
# exampleZip.close()

# import zipfile
# newZip = zipfile.ZipFile('new.zip', 'w') # to add files, do 'a'
# newZip.write('bacon.txt', compress_type=zipfile.ZIP_DEFLATED) # compression type can be selected
# newZip.close()


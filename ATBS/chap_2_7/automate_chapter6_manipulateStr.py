################ Chapter 6 – Manipulating Strings

#raw string ignores escape chars
# print('That is Carol\'s car')
# print(r'That is Carol\'s car')

# print('''This is a multi line string

#  '

# 123''')
# print('Hello' in 'Hello world')
# spam = 'Hello World'
# print(spam.upper())
# print(spam.upper().isupper())

# while True:
#     print('Enter your age: ')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age')

# while True:
#     print('Select a new password (Letters and numbers only):')
#     password = input()
#     if password.isalnum():
#         break
#     print('Passwords can only have letters and nubers.')

# spam = 'Hello World'
# print(spam.startswith('Hell'))
# print('***'.join(['cat', 'dog', 'mouse']))
# print(spam.split())

# print('Hello'.rjust(10))
# print('Hello'.ljust(10, '-'))
# print('Hello'.center(10, '*'))

# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

# picnicItems = {'sandwitches': 4, 'apples': 12, 'cups': 4, 'cookies':8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# spam = '      Hello        '
# print(spam.strip()) #lstrip, rstrip
# spam1 = 'SpamSpamBaconSpamEggsSpamSpam'
# print(spam1.strip('Spam')) #order doesnt matter ampS would work

# import pyperclip
# pyperclip.copy('Hello World!')
# pyperclip.paste()


#pw.py - Am insecure password locker program.

# passwords = {'email': '3rqefasd3r3$F32R',
#             'blog': '13refw23rf13rf241324',
#             'luggage': '12345'}

# import sys, pyperclip
# if len(sys.argv) < 2:
#     print('Usage: python pw.py [account] - copy account password')
#     sys.exit()

# account = sys.argv[1] #this wil give the command line arg

# if account in passwords:
#     pyperclip.copy(passwords[account])
#     print('Password for ' + account + ' copied to clipboard')
# else:
#     print('There is no account named ' + account)

#bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line

# import pyperclip
# text = pyperclip.paste()

# #seperate lines and add stars
# lines = text.split('\n')
# for i in range(len(lines)):
#     lines[i] = '* ' + lines[i] #add star to each lines list item

# text = '\n'.join(lines)

# pyperclip.copy(text)

######################### project
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]

# def printTable(data):
#     # newData = []
#     # for n in data: #concat the strings into one long string for max
#     #     newData += n
#     # width = len(max(newData, key=len)) # get the max len string
    
    
#     width = [0] * len(data)
#     for n in range(len(data)):
#         if len(max(data[n], key=len)) > width[n]:
#             width[n] = len(max(data[n], key=len))
    
#     for e in range(4):
#         for i in range(len(data)):
#             print(data[i][e].rjust(width[i]), end = " ")   
#         print()

# printTable(tableData)
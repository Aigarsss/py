#! python

######################### Chapter 2 – Flow Control #########################
# spam = True
# print("spam")
# print(2 != 4)
# print(True and True)

# name = ""
# while name != 'your name':
#     print("Please provide your name")
#     name = input()
# print("thanks")

# while True:
#     print("Pease provide your name")
#     name = input()
#     if name == 'your name':
#         break
# print("thanks")

# while True:
#     print("enter your name")
#     name = input()
#     if name != "aaa":
#         continue
#     print("Whats your pass?")
#     passw = input()
#     if passw == "bbb":
#         break
# print("You are in")

# name = ""
# while not name:
#     print("what is your name")
#     name = input()
#     print("how many guests?")
#     guests = input()
#     if guests:
#         print("buy something for them")
# print("Done")

# for i in range(0,5):
#     print(i)

# total = 0
# for i in range (101):
#     total += i
# print(total)

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# for i in range(0,11,2):
#     print(i)

# for i in range(5,-1, -1):
#     print(i)

# import random, sys
# print(random.randint(5,10)) # takes the between
# while True:
#     print("type exit to exit")
#     response = input()
#     if response == "exit":
#         sys.exit()
#     print("you entered" + response)

##############################Chapter 3 – Functions

# def hello():
#     print("hello")
#     print("WHaaat","what", sep="*")

# print(hello())

# import random
# def fortune(a):
#     if a<=3:
#         return "Lucky you!"
#     elif 4<=a<=8:
#         return "Could be worse"
#     elif a>=9:
#         return "Jackpot"

# a = random.randint(1,10)
# fortune = fortune(a)
# print(fortune)

# print("hello", " world", sep="****", end = "")
# print(", shoud be a new line")

# def spam(divBy):
#     try:
#         return 42 / divBy
#     except ZeroDivisionError:
#         return "Dont divide by 0"

# print(round(spam(2)))
# print(spam(0))
# print(spam(3))

#numbers guessing game

# import random
# number = random.randint(1,20)
# choice = 0
# counter = 0
# print("Guess a number between 1-20")
# while counter <= 5:
#     choice = int(input("Please choose a number: "))
#     if choice < number:
#         print("Think bigger")
#         counter +=1
#     if choice > number:
#         print("Think smaller")
#         counter +=1
#     if choice == number:
#         counter +=1
#         print ("That is correct. The number was " + str(choice) + ". It took you " + str(counter) + " tries!")
#         break
#     if counter == 5:
#         print("You failed, number was " + str(number))
#         break

# def collatz(number):
#     if number % 2 == 0:
#         result = number // 2
#         print(result)
#         return result
#     else:
#         result = 3 * number + 1
#         print(result)
#         return result

# num = int(input("Give me a number: "))
# while num != 1:
#     num = collatz(num)

###############Chapter 4 – Lists

# li1 = [1,2,3]
# li2 = ["four", "five", "six"]
# new = li1 + li2

# print(new)

# del li1[2]
# print(li1)

# li.index(value)
# li.insert(value, spot)
# li.append(value) # adds to end
# li.remove(value) # adds to end

# spam = ['a', 'z', 'A', 'Z']
# spam.sort()
# print(spam)
# spam.sort(key=str.lower)
# print(spam)

# import copy

# list1 = ["a", "b", "c"]
# list2 = copy.copy(list1)
# list2[1] = 4
# print(list1)
# print(list2)

# #copy.deepcopy() for nested lists

# spam = ['apples', 'bananas', 'tofu', 'cats']

# def string(li):
#     nli = ''
#     for i in li:
#         if i == li[-1]:
#             nli += "and " + i
#         else:   
#             nli += i + ", "
#     return nli

# print(string(spam))

# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]

# def tree(li):
#     val = ''
#     for x in range(6) :
#         for i in range(len(li)):
#             if i == len(li)-1:
#                 val += grid[i][x] + "\n"
#             else:
#                 val += grid[i][x]
#     return val

# print(tree(grid))

################# Chapter 5 Dictionaries and Structuring Data

# myCat = {"size": "fat", "color": "gray", "disposition": "loud"}

# print(myCat["size"])
# birthday ={"Aigars": "2nd June", "Janis": "8th August"}

# while True:
#     print("Enter the name to get birthday, blank to quit: ")
#     name = input()
#     if name == "":
#         break
#     if name in birthday:
#         print("{0} is the birthday of {0}".format(birthday[name]), name)
#     else:
#         print("I dont have this information, please enter the date: ")
#         bday = input()
#         birthday[name] = bday
#         print("db updated")

# spam = {"name": "Pooka", "age": 5}
# if "color" not in spam:
#     spam["color"] = "black"
# print(spam)
# spam.setdefault("weight", 40)
# print(spam)


# import pprint

# message = "It was a bright cold day in April, and the clocks were triking thirteen."
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] += 1

# pprint.pprint(count)
# print(pprint.pformat(count))

# theBoard = {"tL": " ", "tM": " ", "tR": " ",
#             "mL": " ", "mM": " ", "mR": " ",
#             "lL": " ", "lM": " ", "lR": " "}

# def printBoard(board):
#     print(board["tL"] + "|" + board["tM"] + "|" + board["tR"])
#     print("-+-+-")
#     print(board["mL"] + "|" + board["mM"] + "|" + board["mR"])
#     print("-+-+-")
#     print(board["lL"] + "|" + board["lM"] + "|" + board["lR"])

# turn = "X"
# for i in range(9):
#     printBoard(theBoard)
#     print("Turn for " + turn + ". Move on which space (tL/mR/lM etc)")
#     move = input()
#     theBoard[move] = turn
#     if turn == "X":
#         turn = "O"
#     else:
#         turn = "X"
# printBoard(theBoard)

# allGuests = {"Alice": {"apples": 5, "pretzels": 12},
#             "Bob": {"ham sandwitches": 3, "apples": 2},
#             "Carol": {"cups": 3, "apple pies": 1}}

# #print(allGuests["Alice"].get("apples"))

# def totalBrought(guests, item):
#     numBrought = 0
#     for k,v in guests.items():
#         print(v.get(item,0))
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought

# print("- Apples " + str(totalBrought(allGuests, "apples")))

# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# def displayInventory(inventory):
#     print('Inventory:')
#     item_total = 0
#     for k, v in inventory.items():
#         print(str(v) + " " + k)
#         item_total += inventory.get(k, 0)
#     print('Total number of items: ' + str(item_total))

#displayInventory(stuff)

#### second part

# def addToInventory(inventory, addedItems):
#     #code
#     for i in addedItems:
#         inv.setdefault(i,0)
#         inv[i] += 1
#     return inv

# inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)

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

################ Chapter 7 – Pattern Matching with Regular Expressions

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False
#     return True

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
# print('Done')

r'''
REGEX
\d digit character 0 - 9
\D any character that is not numeric
\w any letter, numeric digit or the underscore
\W any character that is not a letter, numeric digit or underscore
\s space, tab or newline
\S any character that is not space, tab or newline
. any char except new line
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a nongreedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.


{x} match the previous pattern x times (like \d{2})
import re regex module
regex_object = re.compile(r'\d{3}-\d{3}') # this would match 444-552
result = regex_object.search('444-552')
print(result.group()) # returns the match 444-552
print(re.compile(r'\d{3}-\d{3}').search('444-552').group()) #together

() creates groups - (\d{2})(\d{3})
import re
regex_object = re.compile(r'(\d{3})-(\d{4})')
result = regex_object.search('345-2345')
print(result.group(1))
print(result.group(2))
print(result.group())
print(result.groups())
first_group, second_group = result.groups()
print(first_group)

import re
regex_object = re.compile(r'(\(\d{3}\)) (\d{2}-\d{2})') # escaping parentheses
result = regex_object.search('This is my number (123) 12-24')
print(result.group())

| # this is OR. 1|2 == 1 or 2 returns first occurence
import re
regex_object = re.compile(r'Batman|Tina Fey')
result = regex_object.search('Batman and Tina Fey')
print(result.group())
result = regex_object.search('Tina Fey and Batman')
print(result.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
result = batRegex.search('Batmobile lost a wheel')
print(result.group(), result.group(1), sep="**")

batRegex = re.compile(r'Bat(wo)?man') # ? is an optional part
result = batRegex.search('The adventures of Batman')
print(result.group())
result = batRegex.search('The adventures of Batwoman')
print(result.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
result = phoneRegex.search('My number is 415-555-4242')
print(result.group())
result = phoneRegex.search('My number is 555-4242')
print(result.group())

batRegex = re.compile(r'Bat(wo)*man') # * can repeat 0 or infinite times
result = batRegex.search('The Adventures of Batman')
print(result.group())
result = batRegex.search('The Adventures of Batwowowoman')
print(result.group())

batRegex = re.compile(r'Bat(wo)+man') # + means mach 1 or more
result = batRegex.search('Adventures of Batman')
print(result == None)
result = batRegex.search('Adventures of Batwowowoman')
print(result.group())

haRegex = re.compile(r'(Ha){3}')
result = haRegex.search('HaHaHa')
print(result.group())

haRegex = re.compile(r'(Ha){3,5}') # greedy. will return longest match by def
result = haRegex.search('HaHaHaHa') # HaHaHaHa
print(result.group())
haRegex = re.compile(r'(Ha){3,5}?') #non greedy because of ?. will return shortest match
result = haRegex.search('HaHaHaHa') # HaHaHa
print(result.group())

findall() will find all matches vs search() will find the first one
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
result = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(result.group())

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # Cannot have groups for findall
result = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # Has groups
result = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result) # returns tuples within list

#character classes
xmasReg = re.compile(r'\d+\s\w+')
result = xmasReg.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(result)

vowelRegex = re.compile(r'[aeiouAEIOU?]') # custom character class, will match these. special chars dont need to be escaped, see ?
result = vowelRegex.findall('Robocop eats baby food. BABY FOOD?.')
print(result)

vowelRegex = re.compile(r'[^aeiouAEIOU?]') # ^ will match the opposite
result = vowelRegex.findall('Robocop eats baby food. BABY FOOD?.')
print(result)

beginsWithHello = re.compile(r'^Hello') # ^ states that it must begin
result = beginsWithHello.search('Hello world')
print(result)

beginsWithHello = re.compile(r'world$') # $ states that it must end
result = beginsWithHello.search('Hello world')
print(result)

beginsWithHello = re.compile(r'^\d+$') # entire string must match if ^ $ is used
result = beginsWithHello.search('14151x24123') # none, must be all numbers
print(result)

atRegex = re.compile(r'.at') #. is a wildcard (for one char)
result = atRegex.findall('The cat in the hat sat on the flat mat.')
print(result)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') #match everyhting
result = nameRegex.search('First Name: Al Last Name: Sweigart')
print(result.group(1), result.group(2))

nongreedyRegex = re.compile(r'<.*?>') #non greedy
result = nongreedyRegex.search('<To serve man> for dinner.>')
print(result.group())

nongreedyRegex = re.compile(r'<.*>') # greedy
result = nongreedyRegex.search('<To serve man> for dinner.>')
print(result.group())

noNewlineRegex = re.compile(r'.*', re.DOTALL) # include \n
result = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(result.group())

robocop = re.compile(r'robocop', re.IGNORECASE) # or re.I . ignores case
result = robocop.search('RobOCop is part man, part machine, all cop.')
print(result.group())

namesRegex = re.compile(r'Agent \w+') #replacing matches
result = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(result)

agentNamesRegex = re.compile(r'Agent (\w)\w*') # replacing matcches with group results
result = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(result)


'''
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?            # area code
#     (\s|-|\.)?                    # separator
#     \d{3}                         # first 3 digits
#     (\s|-|\.)                     # separator
#     \d{4}                         # last 4 digits
#     (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
#     )''', re.VERBOSE) # re.VERBOSE lets you have multi line regex

# someRegexValue = re.compile(r'foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) # to combine all

### project: Phone Number and Email Address Extractor

# import pyperclip, re
# # phone regex
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?
#     (\s|-|\.)?
#     (\d{3})
#     (\s|-|\.)
#     (\d{4})
#     (\s*(ext|x|ext.)\s*(\d{2,5}))?
# )''', re.VERBOSE)

# # email regex
# emailRegex = re.compile(r'''(
#     [a-zA-Z0-9._%+-]+ #username
#     @                  #@
#     [a-zA-Z0-9.-]+      #domain
#     (\.[a-zA-Z]{2,4})
# )''', re.VERBOSE)

# # TODO: Find matches in clipboard text.
# text = str(pyperclip.paste())
# matches = []
# for groups in phoneRegex.findall(text):
#     phoneNum = '-'.join([groups[1],groups[3],groups[5]])
#     if groups[8] != '':
#         phoneNum += ' x' + groups[8]
#     matches.append(phoneNum)
# for groups in emailRegex.findall(text):
#     matches.append(groups[0])

# # TODO: Copy results to the clipboard.
# if len(matches) > 0:
#     pyperclip.copy('\n'.join(matches))
#     print('copied to clipboard')
#     print('\n'.join(matches))
# else:
#     print('No match found')



# import re

# # nakamotoRegex = re.compile(r'[A-Z][a-z]*\sNakamoto')
# # result = nakamotoRegex.search('Mr Nakamoto')
# # print(result.group())

# regex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
# result = regex.search('Carol throws baseballs.')
# print(result.group())

########### practice projects

## strong password detection
# import re
# text = 'Password1'

# def validatePass(passw):
#     regex_num = re.compile(r'[0-9]+')
#     regex_len = re.compile(r'(.*){8,}')
#     regex_cap = re.compile(r'[A-Z]+')
#     regex_small = re.compile(r'[a-z]+')
#     # print(regex_num.search(passw).group())
#     # print(regex_len.search(passw).group())
#     # print(regex_cap.search(passw).group())
#     # print(regex_small.search(passw).group())

#     if bool(regex_num.search(passw)) and bool(regex_len.search(passw)) and bool(regex_cap.search(passw)) and bool(regex_small.search(passw)):
#         return 'Pass is considered strong' # if matched
#     else:
#         return 'consider a different pass' # id no match

# print(validatePass(text))


## Regex Version of strip()
# import re
# string1 = '    strip     '
# print('*' + string1.strip() + '*')

# string2 = '***24f qas2    '
# def stripped(text, char):
#     if char == '':
#         regex_left = re.compile(r'^[\s]*')
#         text = regex_left.sub('', text)
#         regex_right = re.compile(r'[\s]*$')
#         text = regex_right.sub('', text)
#         return text
#     else:
#         regex_left = re.compile(r'^[{}]*'.format(char))
#         text = regex_left.sub('', text)
#         regex_right = re.compile(r'[{}]*$'.format(char))
#         text = regex_right.sub('', text)
#         return text

# print('*' + stripped(string2, '*') + '*')


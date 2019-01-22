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
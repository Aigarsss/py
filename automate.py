#! python
#print([i for i in range(10)])

#https://automatetheboringstuff.com

####################chapter3

# try:
#     print(1/2)
#     print(1/0)
# except ZeroDivisionError:
#     print("exception")

#guess the number game. enter a number between 1-20. 6 tries. report if 
# too large or too small

# import random
# num = random.randint(1,20)
# print(num)
# print("Number guessing game 1-20")
# for i in range(1,7):
#     print(num)
#     guess = int(input("Guess a number: "))
#     if guess > num:
#         print("Guess is too big")
#     elif guess < num:
#         print("Guess is too small")
#     else:
#         break

# if guess == num:
#     print("{} is correct. It took you {} tries".format(guess, i))
# else:
#     print("Tries are up, you used {}".format(i))        
    



# Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return 
# this value. If number is odd, then collatz() should print and 
# return 3 * number + 1.
# 
# Then write a program that lets the user type in an integer and 
# that keeps calling collatz() on that number until the function 
# returns the value 1. (Amazingly enough, this sequence actually works 
# for any integer—sooner or later, using this sequence, you’ll arrive at 1! 
# Even mathematicians aren’t sure why. Your program is exploring what’s 
# called the Collatz sequence, sometimes called “the simplest impossible 
# math problem.”)
# Remember to convert the return value from input() to an integer 
# with the int() function; otherwise, it will be a string value.
# Hint: An integer number is even if number % 2 == 0, and it’s odd 
# if number % 2 == 1.
# The output of this program could look something like this:

# Enter number:
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1

# Add try and except statements to the previous project to detect 
# whether the user types in a noninteger string. Normally, the int() 
# function will raise a ValueError error if it is passed a noninteger 
# string, as in int('puppy'). In the except clause, print a message 
# to the user saying they must enter an integer.

# def collatz(number):
#     if number % 2 == 0:
#         return number // 2
#     if number % 2 == 1:
#         return 3 * number + 1

# def user_goes():
#     result = ""
#     try:
#         user_choice = int(input("Enter an integer: "))
#         while collatz(user_choice) != 1:
#             user_choice = collatz(user_choice)
#             result += str(collatz(user_choice)) + "\n"
#         return result
#     except ValueError:
#         return "Exception caught"

# print(user_goes())

####################chapter4

# spam = ['a', 'z', 'A', 'Z']
# spam.sort(key=str.lower)
# print(spam)

### Comma Code
# Say you have a list value like this:

# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument 
# and returns a string with all the items separated by a comma 
# and a space, with and inserted before the last item. 
# For example, passing the previous spam list to the function 
# would return 'apples, bananas, tofu, and cats'. But your 
# function should be able to work with any list value passed to it.

# spam = ["apples", "bananas", "tofu", "cats"]

# def stringify(li):
#     result = ""
#     for i in spam:
#         if i == spam[-1]:
#             result += " and " + i
#         elif i == spam[-2]:
#             result += i
#         else:
#             result += i + ", "
#     return result

# print(stringify(spam))

#######Character Picture Grid
# Say you have a list of lists where each value in the inner lists is 
# a one-character string, like this:

# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]

# You can think of grid[x][y] as being the character at the 
# x- and y-coordinates of a “picture” drawn with text characters. 
# The (0, 0) origin will be in the upper-left corner, the x-coordinates 
# increase going right, and the y-coordinates increase going down.

# Copy the previous grid value, and write code that uses it to print 
# the image.


# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....
# Hint: You will need to use a loop in a loop in order to 
# print grid[0][0], then grid[1][0], then grid[2][0], and so on, 
# up to grid[8][0]. This will finish the first row, so then print 
# a newline. Then your program should print grid[0][1], then grid[1][1], 
# then grid[2][1], and so on. The last thing your program will print is 
# grid[8][5].

# Also, remember to pass the end keyword argument to print() if you 
# don’t want a newline printed automatically after each print() call.

# new_grid = grid.copy()
# for i in range(len(new_grid[0])):
#     for a in range(len(new_grid)):
#         if a+1 == len(new_grid):
#             print((new_grid[a][i]))
#         else:
#             print((new_grid[a][i]), end = "")


############### chapter 5

# spam = {"first": "1", "second": "2"}
# print("first" in spam)
# print(spam["first"])
# print(spam.get("second", 0))
# spam.setdefault("thrid", "3")
# print(spam)

# import pprint

# the_board = {"top-L": " ", "top-M": " ", "top-R": " ", 
#             "mid-L": " ", "mid-M": " ", "mid-R": " ", 
#             "low-L": " ", "low-M": " ", 'low-R': " "}


# #//print(the_board)
# # print(pprint.pprint(the_board))

# def print_board(board):
#     print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
#     print("-+-+-")
#     print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
#     print("-+-+-")
#     print(board["low-L"] + "|" + board["mid-L"] + "|" + board["low-R"])

# turn = "X"
# print("Tic Tac Toe. Enter your choices (mid-L, low-R etc")
# for i in range(len(the_board)):
#     print_board(the_board)
#     choice = input(turn + " please enter your choice: ")
#     the_board[choice] = turn
#     if the_board[choice] == "X":
#         turn = "0"
#     else:
#         turn = "X"


###Fantasy Game Inventory
# You are creating a fantasy video game. The data structure to model the 
# player’s inventory will be a dictionary where the keys are string values
#  describing the item in the inventory and the value is an integer value 
#  detailing how many of that item the player has. For example, the 
#  dictionary value 
#  {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
#  means the player has 1 rope, 6 torches, 42 gold coins, and so on.

# Write a function named displayInventory() that would take any possible 
# “inventory” and display it like the following:

# Inventory:
# 12 arrow
# 42 gold coin
# 1 rope
# 6 torch
# 1 dagger
# Total number of items: 62
# Hint: You can use a for loop to loop through all the keys in a dictionary.

# inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 

# def display_inventory(inv):
#     li = ""
#     counter = 0
#     li += "Inventory: \n"
#     for item, count in inv.items():
#         li += str(count) + " " + item + "\n"
#         counter += count
#     li += "Total number of items:" + str(counter)
#     return li


# print(display_inventory(inventory))

########## Imagine that a vanquished dragon’s loot is represented as a list of 
# strings like this:


# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# Write a function named addToInventory(inventory, addedItems), where the 
# inventory parameter is a dictionary representing the player’s inventory 
# (like in the previous project) and the addedItems parameter is a list 
# like dragonLoot. The addToInventory() function should return a dictionary 
# that represents the updated inventory. Note that the addedItems list can 
# contain multiples of the same item. 

# The previous program (with your displayInventory() function from the 
# previous project) would output the following:

# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger

# Total number of items: 48

# inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# new_inventory = {}

# Display only new items 
# def addToInventory(inventory, addedItems):
#     new_inventory = {}
#     result = "Inventory: \n"
#     total = 0
#     for item in dragonLoot:
#         new_inventory.setdefault(item, 0)
#         new_inventory[item] = new_inventory[item] + 1
#     for k, i in new_inventory.items():
#         result += str(i) + " " + k + "\n" 
#         total += i
#     result += "Total number of items: " + str(total)
#     return result

#Display with all the previous ites as well
# def addToInventory(inventory, addedItems):
#     result = "Inventory: \n"
#     for item in addedItems:
#         inventory.setdefault(item, 0)
#         inventory[item] += 1
#     #print(inventory)
#     total = inventory[item]
#     for k, i in inventory.items():
#         result += str(i) + " " + k + "\n" 
#         total +=  i
#     result += "Total number of items: " + str(total)
#     return result

# print(addToInventory(inventory, dragonLoot))

################# chapter 6
# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# import pyperclip

# pyperclip.copy("Hello World")
# pyperclip.paste()

### Project: Password Locker

# import pyperclip, pprint, sys
# password_lib = {
#             "email": "123fe14email", 
#             "fb": "fwf32r2fb", 
#             "twitter": "twit123"
#             }

# if len(sys.argv) < 2:
#     print("Usage: python autoate.py [account] - copy account password")
#     sys.exit()

# account = sys.argv[1] # first command line arg is the account name

# if account in password_lib:
#     pyperclip.copy(password_lib[account])
#     print("Password for {} copied to clipboard".format(account))
# else:
#     print("No account found for {}".format(account))

########## Project: Adding Bullets to Wiki Markup

# import pyperclip

# text = pyperclip.paste()
# lines = text.split("\n")
# for i in range(len(lines)):
#     lines[i] = "* " + lines[i]
# text = "\n".join(lines)
# pyperclip.copy(text)


############### Table Printer
# Write a function named printTable() that takes a list of lists of 
# strings and displays it in a well-organized table with each column 
# right-justified. Assume that all the inner lists will contain the 
# same number of strings. For example, the value could look like this:


# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]
# Your printTable() function would print the following:

# Hint: Your code will first have to find the longest string in 
# each of the inner lists so that the whole column can be wide enough 
# to fit all the strings. You can store the maximum width of each column 
# as a list of integers. The printTable() function can begin 
# with colWidths = [0] * len(tableData), which will create a 
# list containing the same number of 0 values as the number of 
# inner lists in tableData. That way, colWidths[0] can store the 
# width of the longest string in tableData[0], colWidths[1] can 
# store the width of the longest string in tableData[1], and so on. 
# You can then find the largest value in the colWidths list to find out 
# what integer width to pass to the rjust() string method.

#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose

# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#              ['Alice', 'Bob', 'Carol', 'David'],
#              ['dogs', 'cats', 'moose', 'goose']]


# def printTable(table):
#     ## 1st version for max width
#     biggest = 0
#     for i in range(len(table)):
#         for a in range(len(table[i])):
#             if biggest < len(table[i][a]):
#                 biggest = len(table[i][a])
#     return biggest

#     ## 2nd version for max width
#     # colWidth = [0]*len(table)
#     # for i in range(len(table)):
#     #     length = 0
#     #     for x in range(len(table[i])):
#     #         if len(table[i][x]) > length:
#     #             length = len(table[i][x])
#     #             colWidth[i] = length
#     # max_width = max(colWidth)+2
    
#     for i in range(0,4):
#         for a in range(0,3):
#             if a == 2:
#                 print(table[a][i].rjust(max_width))
#             else:
#                 print(table[a][i].rjust(max_width), end="")


# print(printTable(tableData))

######### Chapter 7 – Pattern Matching with Regular Expressions

import re

# phone_num_regex = re.compile(r"\d{3}-\d{3}-\d{4}") #regexes need to be raw
# mo = phone_num_regex.search("this is the num 333-333-3333")
# print(mo.group())

# phone_num_regex = re.compile(r"(\d{3})-\d{3}-\d{4}") #regexes need to be raw
# mo = phone_num_regex.search("this is the num 333-333-3333")
# print(mo.group(1))

reg = re.compile(r"bat(man|woman|child)")
mo = reg.search("batwoman")
print(mo.group(1)) #finds woman


#print(phone_num_regex)
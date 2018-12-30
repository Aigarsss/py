#https://www.w3resource.com/python-exercises/python-basic-exercises.php

############### 1 ################
# print(
# '''
# "Twinkle, twinkle, little star, 
#     How I wonder what you are! 
#         Up above the world so high, 
#         Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
#     How I wonder what you are"
# '''
# )

# #answer
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

############### 2 ################
#Write a Python program to get the Python version you are using.

# import sys
# print("Version:")
# print(sys.version_info[3])
# print("V:")
# print(sys.version[0])

############### 3 ################
# Write a Python program to display the current date and time.
# Sample Output : 
# Current date and time : 
# 2014-07-05 14:34:14

# import datetime
# time = datetime.datetime.now()

# def datetime():
#     return time

# print(datetime())

############### 4 ################
# Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output : 
# r = 1.1
# Area = 3.8013271108436504

# import math
# def radius():
#     rad = input("Provide the radius: ")
#     return float(rad)**2*float(math.pi)

# print(radius())

############### 5 ################
#Write a Python program which accepts the user's first and 
# last name and print them in reverse order with a space between them.

# a = input("enter your first and last name: ")
# a = a.split()
# print(a[1] + " " + a[0])

############### 6 ################
# Write a Python program which accepts a sequence of comma-separated numbers 
# from user and generate a list and a tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output : 
# List : ['3', ' 5', ' 7', ' 23'] 
# Tuple : ('3', ' 5', ' 7', ' 23')

# a = input("Enter some numbers (1, 2, 5 ... etc): ")
# #a = "3, 5, 7, 23"
# li = a.split(", ")
# print(li)
# tup = tuple(li)
# print(tup)

############### 7 ################
# Write a Python program to accept a filename from the user and print the extension of that. 
# Sample filename : abc.java 
# Output : java
# file = "abc.java"
# ext = file[file.find(".")+1:]
# print(ext)

############### 8 ################
# Write a Python program to display the first and last 
# colors from the following list. 
# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0] + ", " + color_list[-1])

############### 9 ################
# Write a Python program to display the examination schedule. 
# (extract the date from exam_st_date). 
# Sample Output : The examination will start from : 11 / 12 / 2014
# exam_st_date = (11, 12, 2014)
# exam_st_date = list(exam_st_date)
# #print(str(exam_st_date[0]) + "1")
# print("The examination will start from : " + str(exam_st_date[0]) + " / " + str(exam_st_date[1]) + " / " + str(exam_st_date[2]))

# #example:
# exam_st_date = (11,12,2014)
# print( "The examination will start from : %i / %i / %i" %exam_st_date)

############### 10 ################
# Write a Python program that accepts an integer (n) 
# and computes the value of n+nn+nnn. 
# Sample value of n is 5 
# Expected Result : 615
# a = input("Integer: ")
# #a = '5'
# a2 = a + a
# a3 = a + a + a
# print(int(a)+ int(a2) + int(a3))

############### 11 ################
# Write a Python program to print the documents (syntax, description etc.) 
# of Python built-in function(s). 
# Sample function : abs()
# Expected Result : 
# abs(number) -> number
# Return the absolute value of the argument.

# print(abs.__doc__)

############### 12 ################
# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module. 
# import calendar
# y = int(input("Provide year: "))
# m = int(input("Provide month: "))
# print(calendar.month(y, m))

############### 13 ################
# Write a Python program to print the following here document. 
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# print('''
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# ''')

############### 14 ################
#  Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days 

# import datetime
# date1 = datetime.datetime(2014, 4, 2)
# date2 = datetime.datetime(2014, 7, 11)
# dif = abs(date1 - date2)
# print(dif)

############### 15 ################
#Write a Python program to get the volume of a 
# sphere with radius 6.
# r = 6
# c = 4.19
# print(round((r**3*c), 2))

############### 16 ################
# Write a Python program to get the difference between a given number 
# and 17, if the number is greater than 17 return double the absolute 
# difference. 
# choice = abs(int(input("Provie a number: ")))
# compare = 17
# if choice > compare:
#     print((choice - compare)*2)
# else:
#     print((choice - compare))

############### 17 ################
# Write a Python program to test whether a number is 
# within 100 of 1000 or 2000.

# def near_k(number):
#     if 1000 - abs(number) <= 100 or 2000 - abs(number) <= 100:
#         return True
#     else:
#         return False

# print(near_k(1990))

############### 18 ################
# Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return thrice of their sum. 

# def calc_sum(a, b, c):
#     if a == b == c:
#         return (a + b + c)*3
#     return a + b + c

# print(calc_sum(3,3,3))

############### 19 ################
# Write a Python program to get a new string from a given string where 
# "Is" has been added to the front. If the given string already 
# begins with "Is" then return the string unchanged.

# change = "Is"
# def prov_str(strn):
#     if strn[0:2] == change:
#         return strn
#     return change + strn

# print(prov_str("Is super"))
# print(prov_str("super"))

############### 20 ################
# Write a Python program to get a string which is n 
# (non-negative integer) copies of a given string

# def str_cop(str, num):
#     return str*num

# print(str_cop("what", 4))

############### 21 ################
# Write a Python program to find whether a given number (accept from the user) 
# is even or odd, print out an appropriate message to the user

# number = int(input("Please provide a number: "))
# if number % 2 == 0:
#     print("This is an even number!")
# else:
#     print("This is an odd number!")

############### 22 ################
#Write a Python program to count the number 4 in a given list.

############### 23 ################


############### 24 ################


############### 25 ################


############### 26 ################


############### 27 ################


############### 28 ################


############### 29 ################


############### 30 ################

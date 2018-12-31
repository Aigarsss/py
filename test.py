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
# array = [4, 1, 2, 4]
# counter = 0
# for i in array:
#     if i == 4:
#         counter += 1
# print(counter)

############### 23 ################
# Write a Python program to get the n (non-negative integer) 
# copies of the first 2 characters of a given string. 
# Return the n copies of the whole string if the length is less than 2.

# def char_copy(str, n):
#     if len(str) < 2:
#         return str*n
#     else:
#         return str[0:2]*n

# print(char_copy("abcd", 4))

############### 24 ################
#Write a Python program to test whether a passed letter is a vowel or not. 
# vowels = ["a", "e", "i", "o", "u"]
# letter = input("Enter a letter: ")
# #letter = "a"
# if str.lower(letter) in vowels:
#     print("This is a vowel")
# else:
#     print("This is not vowel")

# #solution
# def is_vowel(char):
#     all_vowels = 'aeiou'
#     return char in all_vowels
# print(is_vowel('c'))
# print(is_vowel('e'))

############### 25 ################
# Write a Python program to check whether a specified value is 
# contained in a group of values. 
# Test Data : 
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# def check_group(list, value):
#     if value in list:
#         return True
#     return False

# print(check_group([1, 5, 8, 3], 3))

############### 26 ################
#Write a Python program to create a histogram from a given list of integers.

# def histogram(range, char):
#     result = ""
#     for i in range:
#         result += i*char + "\n"
#     return result

# print(histogram([1, 2, 3], "@"))

############### 27 ################
# Write a Python program to concatenate all elements in a 
# list into a string and return it.
# def concat(list):
#     result = ""
#     for i in list:
#        result += str(i)
#     return result

# print(concat([1, "312", "ad"]))

############### 28 ################
# Write a Python program to print all even numbers from a 
# given numbers list in the same order and stop the printing 
# if any numbers that come after 237 in the sequence. 
# Sample numbers list :

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# for i in numbers:
#     if i == 237:
#         print(i)
#         break
#     else:
#         if i % 2 == 0:
#             print(i)

############### 29 ################
# Write a Python program to print out a set containing all the colors 
# from color_list_1 which are not present in color_list_2. 
# Test Data : 
# color_list_1 = set(["White", "Black", "Red"]) 
# color_list_2 = set(["Red", "Green"])
# # Expected Output : 
# # {'Black', 'White'}
# new_set = set() 
# for i in color_list_1:
#     if i not in color_list_2:
#         new_set.add(i)
# print(new_set)

##solution
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print(color_list_1.difference(color_list_2))

############### 30 ################
# Write a Python program that will accept the base and height of a 
# triangle and compute the area.

# def area(base,height):
#     return base * height / 2

# print(round(area(4.2, 5),2))

############### 31 ################
# Write a Python program to compute the greatest common divisor (GCD) 
# of two positive integers.

# def greatest_devisor(a, b):
#     greatest = 0
#     smallest = min(a, b)
#     count = 1
#     while count < smallest:
#         if a % count == 0 and b % count == 0:
#             greatest = count
#         count += 1
#     return greatest

# print(greatest_devisor(21, 15))

############### 32 ################
# Write a Python program to get the least common multiple (LCM) 
# of two positive integers. 

# def smallest_multiple(a, b):
# # get a, get b
# # get ultiple number between the two
# # get a number that can be devied by a and b in the range of the multiple
#     total = a*b
#     count = 1
#     while count <= total:
#         if count % a == 0 and count % b == 0:
#             return count
#         count += 1


# print(smallest_multiple(4, 6)) #12
# print(smallest_multiple(15, 17)) #255

############### 33 ################
# Write a Python program to sum of three given integers. 
# However, if two values are equal sum will be zero

#get the three integers
#assign sum value
#check if a == b or a == c or b == c

# def sum_three(a, b, c):
#     total = 0
#     if a == b or a == c or b == c:
#         return total
#     else:
#         total = a +  b + c
#         return total


# print(sum_three(1,1,2))
# print(sum_three(5,1,2))
############### 34 ################
# Write a Python program to sum of two given integers. However, 
# if the sum is between 15 to 20 it will return 20.

# get the integers (input or function)
# if 15 <= sum <= 20 return 0
# else sum

# def sum_20(a, b):
#     total = a + b
#     if 15 <= total <= 20:
#         return 20
#     else:
#         return total

# print(sum_20(17,2))
# print(sum_20(4,2))

############### 35 ################
# Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5.
# def two(a, b):
#     if a == b or a + b == 5 or abs(a-b) == 5:
#         return True
#     return False

# print(two(2,2))
# print(two(5,10))
# print(two(2,99))

############### 36 ################
# Write a Python program to add two objects 
# if both objects are an integer type.

# def add_int(a, b):
#     if type(a) == type(b) == int:
#         return a + b
#     else:
#         return "one of the inpts is not an int"

# print(add_int(1, 5))
# print(add_int("tab", 5))

#solution
# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#          raise TypeError("Inputs must be integers")
#     return a + b

# print(add_numbers(10, 20))

############### 37 ################
# Write a Python program to display your details like name, age, 
# address in three different lines. 

# def details():
#     name = input("Your name: ")
#     age = input("Your age: ")
#     address = input("Your address: ")
#     print("###################" + "\n" + "Your name is " + name + "\n" + "Your age is " + age + "\n" + "Yor address is " + address)

# details()

#solution
# def personal_details():
#     name, age = "Simon", 19
#     address = "Bangalore, Karnataka, India"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

# personal_details()

############### 38 ################
# # Write a Python program to solve (x + y) * (x + y). 
# # Test Data : x = 4, y = 3
# # Expected Output : (4 + 3) ^ 2) = 49
# x = 4
# y = 3
# result = (x + y) * (x + y)

# print("({} + {}) ^ 2 = {}".format(x,y,result))

############### 39 ################
# Write a Python program to compute the future value of a specified 
# principal amount, rate of interest, and a number of years. 
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

# def future_value():
#     amt = 10000
#     intr = 0.035
#     y = 7
#     count = 1
#     while count <= y:
#         interest = amt*intr
#         #print("interest amount below")
#         #print(interest)
#         amt += interest
#         #print("amount below")
#         #print(amt)
#         count += 1
#     return round(amt, 2)

# print(future_value())

#solution
# amt = 10000
# int = 3.5
# years = 7

# future_value  = amt*((1+(0.01*int)) ** years)
# print(round(future_value,2))

############### 40 ################
# Write a Python program to compute the distance between 
# the points (x1, y1) and (x2, y2).
# from math import sqrt
# x1, x2, y1, y2 = 1, 2, 3, 4

# print(sqrt((x2-x2)**2 + (y2-y1)**2))

# #solution
# import math

# p1 = [4, 0]
# p2 = [6, 6]
# distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

# print(distance)

############### 41 ################
#Write a Python program to check whether a file exists
#solution
# import os.path
# path = "./test.py"
# print(os.path.exists(path))

############### 42 ################
# Write a Python program to determine if a Python shell 
# is executing in 32bit or 64bit mode on OS.
#solution
#solution
# For 32 bit it will return 32 and for 64 bit it will return 64
# import struct
# print(struct.calcsize("P") * 8)

############### 43 ################
#Write a Python program to get OS name, platform and release information. 
#solution
# import platform
# import os
# print(os.name)
# print(platform.system())
# print(platform.release())

############### 44 ################
# Write a Python program to locate Python site-packages.
#solution
# import site
# print(site.getsitepackages())

############### 45 ################
#Write a python program to call an external command in Python
#solution
# from subprocess import call
# call(["ls", "-l"])

############### 46 ################
# Write a python program to get the path 
# and name of the file that is currently executing
#solution
# import os
# print("Current File Name : " + os.path.realpath(__file__))

############### 47 ################
# Write a Python program to find out the number of CPUs using.
# import multiprocessing
# print(multiprocessing.cpu_count())

############### 48 ################
#Write a Python program to parse a string to Float or Integer.

# def parser(a):
#     a = float(a)
#     return a

# print(parser("5"))
# print(int(parser("5")))

############### 49 ################
#Write a Python program to list all files in a directory in Python. 
# import os
# path = "./"
# print(os.listdir(path))

#solution
from os import listdir
from os.path import isfile, join
path = "./"
files_list = [f for f in listdir(path) if isfile(join(path, f))]
print(files_list)

############### 50 ################


############### 51 ################


############### 52 ################


############### 53 ################


############### 54 ################


############### 55 ################


############### 5 ################


############### 57 ################


############### 58 ################


############### 59 ################


############### 60 ################


############### 61 ################


############### 62 ################
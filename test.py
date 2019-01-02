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
# from os import listdir
# from os.path import isfile, join
# path = "./"
# files_list = [f for f in listdir(path) if isfile(join(path, f))] #didnt get te join bit
# print(files_list)

############### 50 ################
#Write a Python program to print without newline or space.

# for i in range(0,10):
#     print(i, end = "")
# print(end = "\n")

############### 51 ################
# Write a Python program to determine profiling of Python programs. 
# Note: A profile is a set of statistics that describes how 
# often and for how long various parts of the program executed. 
# These statistics can be formatted into reports via the pstats 
# module. 

# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')

############### 52 ################
# Write a Python program to print to stderr.

# ?????????????????????


############### 53 ################

# import os

# print(os.environ['HOME'])
# print(os.environ['PATH'].split(";"))

# for i in os.environ['PATH'].split(";"):
#     print(i)


############### 54 ################
#Write a Python program to get the current username

# import getpass
# print(getpass.getuser())


############### 55 ################
#Write a Python to find local IP addresses using Python's stdlib

# ????????????????????? something with socket import


############### 56 ################

# Write a Python program to get height and width of the console window.

# ?????????????????????

############### 57 ################
# import time
# start = time.time()
# end = time.time()
# took = end - start

# def time_function(n):
#     start
#     s = 0
#     for i in range(1,n+1):
#         s += i
#     end
#     return s, took

# print(time_function(9))

############### 58 ################
# Write a python program to sum of the first n positive integers.

# def int_sum():
#     n = input("Enter an integer: ")
#     result = 0
#     for i in range(1,int(n)+1):
#         result += i
#     return result

# print(int_sum())

############### 59 ################
# Write a Python program to convert height 
# (in feet and inches) to centimeters

# def converter(ft, inch):
#     # ft to cm
#     cm_in_foot = 30.48
#     cm_in_inch = 2.54
#     cm = ft * cm_in_foot + inch * cm_in_inch
#     return "{} feet is {}cm ".format(ft, cm)

# print(converter(5, 3))

############### 60 ################
# Write a Python program to calculate the hypotenuse of a right 
# angled triangle.

# from math import sqrt

# def hip(a, b):
#     return sqrt(a**2 + b**2)

# print(round(hip(2,5), 2))

############### 61 ################
#Write a Python program to convert the distance (in feet) 
# to inches, yards, and miles

# def converter_dist(feet):
#     inch = 12*feet
#     yards = round(feet/3,2)
#     miles = round(feet/5280, 2)

#     return "{} feet is the same as {} inches or {} yards or {} miles".format(feet, inch, yards, miles)

# print(converter_dist(100))

############### 62 ################
#Write a Python program to convert all units of time into seconds. 

#units days, hours, minutes, seconds

# days, hours, minutes, seconds = 4, 5, 20, 10

# d = days * 3600 * 24
# h = hours * 3600
# m = minutes * 60
# s = seconds

# print(d + h + m + s)

############### 63 ################
#Write a Python program to get an absolute file path.
# from os import path

# print(path.abspath("test.py"))

############### 64 ################
#  Write a Python program to get file creation 
#  and modification date/times.

############### 65 ################
#solution
# import os.path, time
# print("Last modified: %s" % time.ctime(os.path.getmtime("test.py")))
# print("Created: %s" % time.ctime(os.path.getctime("test.py")))

############### 66 ################
#  Write a Python program to convert seconds to day, 
#  hour, minutes and seconds.
# sec = 1234565

# days = sec // (3600 * 24)
# time = sec % (3600 * 24)
# hours = time // 3600
# time = time % 3600
# minutes = time // 60
# time = time % 60
# secs = time

# print("{} seconds is {} days, {} hours, {} minutes, {} seconds".format(sec, days, hours, minutes, secs))

# #solution:
# time = float(input("Input time in seconds: "))
# day = time // (24 * 3600)
# time = time % (24 * 3600)
# hour = time // 3600
# time %= 3600
# minutes = time // 60
# time %= 60
# seconds = time
# print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

############### 67 ################
#Write a Python program to calculate body mass index.
# def bmi(w, h):
#     return round(w/h**2, 2)

# print(bmi(75, 1.8))

############### 68 ################
# Write a Python program to convert pressure in kilopascals to 
# pounds per square inch, a millimeter of mercury (mmHg) 
# and atmosphere pressure

# to convert from PSI = KPA * 0.14503773773020923
# kpa = 12.35
# const = 0.14503773773020923
# converted = kpa * const
# print(round(converted, 2))

############### 69 ################
#Write a Python program to sort three integers without using 
#conditional statements and loops. 
# def sort(a, b, c):
#     li = []
#     if a < b and a < c:
#         li.append(a)
#         if b < c:
#             li.append(b)
#             li.append(c)
#         else:
#             li.append(c)
#             li.append(b)
#         return li
#     elif b < a and b < c:
#         li.append(b)
#         if a < c:
#             li.append(a)
#             li.append(c)
#         else:
#             li.append(c)
#             li.append(a)
#         return li
#     elif c < a and c < b:
#         li.append(c)
#         if a < b:
#             li.append(a)
#             li.append(b)
#         else:
#             li.append(b)
#             li.append(a)
#         return li


# print(sort(1,2,4))
# print(sort(1,3,2))
# print(sort(5,2,1))

# #solution:
# x = int(input("Input first number: "))
# y = int(input("Input second number: "))
# z = int(input("Input third number: "))

# a1 = min(x, y, z)
# a3 = max(x, y, z)
# a2 = (x + y + z) - a1 - a3
# print("Numbers in sorted order: ", a1, a2, a3)

############### 70 ################
#Write a Python program to sort files by date.

# import glob
# import os

# files = glob.glob("*.py")
# print(files)
# files.sort(key=os.path.getmtime)
# print("\n".join(files))

############### 71 ################
#Write a Python program to get a directory listing, sorted by creation date.

#???????????????

############### 72 ################

#Write a Python program to get the details of math module.
# import math
# print(help(math))

# #solution
# # Imports the math module
# import math            
# #Sets everything to a list of math module
# math_ls = dir(math) # 
# print(math_ls)

############### 73 ################
#Write a Python program to calculate midpoints of a line
#solution
# print('\nCalculate the midpoint of a line :')

# x1 = float(input('The value of x (the first endpoint) '))
# y1 = float(input('The value of y (the first endpoint) '))

# x2 = float(input('The value of x (the first endpoint) '))
# y2 = float(input('The value of y (the first endpoint) '))

# x_m_point = (x1 + x2)/2
# y_m_point = (y1 + y2)/2
# print();
# print("The midpoint of line is :")
# print( "The midpoint's x value is: ",x_m_point)
# print( "The midpoint's y value is: ",y_m_point)
# print();

############### 74 ################
#Write a Python program to hash a word.

# import hashlib
# #print(hashlib.algorithms_available)
# #print(hashlib.algorithms_guaranteed)
# hash_object = hashlib.sha256(b'Hello World')
# print(hash_object)
# hex_dig = hash_object.hexdigest()
# print(hex_dig)

# It is important to note the "b" preceding the string literal, 
# this converts the string to bytes, because the hashing function only 
# takes a sequence of bytes as a parameter. In previous versions of the library, 
# it used to take a string literal. So, if you need to take some input from the 
# console, and hash this input, do not forget to encode the string in a 
# sequence of bytes
# https://www.pythoncentral.io/hashing-strings-with-python/

# solution

# soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
 
# word=input("Input the word be hashed: ")
 
# word=word.upper()
 
# coded=word[0]
 
# for a in word[1:len(word)]:
#     i=65-ord(a)
#     coded=coded+str(soundex[i])
# print() 
# print("The coded word is: "+coded)
# print()

############### 75 ################
#Write a Python program to get the copyright information.
# from sys import copyright

# print(copyright)

############### 76 ################
# Write a Python program to get the command-line arguments 
# (name of the script, the number of arguments, arguments) passed to a script.

# import sys
# print("This is the name/path of the script:"),sys.argv[0]
# print("Number of arguments:",len(sys.argv))
# print("Argument List:",str(sys.argv))


############### 77 ################
# Write a Python program to test whether the system is a big-endian 
# platform or little-endian platform
# import sys
# print()
# if sys.byteorder == "little":
#     #intel, alpha
#     print("Little-endian platform.")
# else:
#     #motorola, sparc
#     print("Big-endian platform.")
# print()

############### 78 ################
#Write a Python program to find the available built-in modules.
# import sys
# mod = sys.modules
# print(mod)

# import sys
# import textwrap
# module_name = ', '.join(sorted(sys.builtin_module_names))
# print(module_name)

############### 79 ################
#Write a Python program to get the size of an object in bytes.

# import sys
# x = 100
# print(sys.getsizeof(x))

############### 80 ################
#Write a Python program to get the current value of the recursion limit.
# import sys
# print()
# print("Current value of the recursion limit:")
# print(sys.getrecursionlimit())
# print()

############### 81 ################
# colors = ["White", "Brown", "Green"]

# print(", ".join(colors))

############### 82 ################
#Write a Python program to calculate the sum over a container.

# x = [1, 2, 3]

# print(sum(x))

############### 83 ################
# Write a Python program to test whether all numbers of a 
# list is greater than a certain number. 
# test = 6
# li = [7, 8, 9]
# if min(li) > test:
#     print(True)
# else:
#     print(False)

############### 84 ################
# Write a Python program to count the number occurrence of a specific 
# character in a string.

# string = "something something"
# char = "s"
# counter = 0
# for i in string:
#     if i == char:
#         counter += 1
# print(counter)

# # solution
# s = "The quick brown fox jumps over the lazy dog."
# print()
# print(s.count("q"))
# print()

############### 85 ################
# Write a Python program to check if a file path is a file or a directory.
# import os
# path = "./test.py"
# if os.path.isdir(path):
#     print("path")
# else:
#     print("file")

############### 86 ################
#Write a Python program to get the ASCII value of a character. 

# char = "@"

# print(ord(char))

############### 87 ################
# Write a Python program to get the size of a file.
# import os

# print(os.path.getsize("./test.py"))

############### 88 ################
# Given variables x=30 and y=20, write a Python program to print t "30+20=50".

# x = 30
# y = 20
# total = x + y

# print("{} + {} = {}".format(x,y,total))

#solution:
# x = 30
# y = 20
# print("\n%d+%d=%d" % (x, y, x+y))
# print()

############### 89 ################
# Write a Python program to perform an action if a condition is true. 
# Given a variable name, if the value is 1, display the string 
# "First day of a Month!" and do nothing if the value is not equal.

# x = 1
# if x == 1:
#     print("First day of a Month!")


############### 90 ################
# Write a Python program to create a copy of its own source code.
# print()
# print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())
# print()

############### 91 ################
# Write a Python program to swap two variables.

# variables = ["a", "b"]
# variables = [variables[1], variables[0]]
# print(variables)

# solution
# a = 30
# b = 20
# print("\nBefore swap a = %d and b = %d" %(a, b))
# a, b = b, a
# print("\nAfter swaping a = %d and b = %d" %(a, b))
# print()

############### 92 ################
# Write a Python program to define a string containing special 
# characters in various forms

#solution
# print()
# print("\#{'}${\"}@/")
# print("\#{'}${"'"'"}@/")
# print(r"""\#{'}${"}@/""")
# print('\#{\'}${"}@/')
# print('\#{'"'"'}${"}@/')
# print(r'''\#{'}${"}@/''')
# print()

############### 93 ################
# Write a Python program to get the identity of an object. 

# x = "identity"
# print(id(x))

############### 94 ################
#Write a Python program to convert a byte string to a list of integers.

# #solution
# x = b'Abc'
# print(x)
# print()
# print(list(x))
# print()

############### 95 ################
# Write a Python program to check if a string is numeric. 
# def is_int(a):
#     try:
#         a = float(a)
#         if isinstance(a, float):
#             return True
#     except (ValueError, TypeError):
#         return '\nNot numeric'

# print(is_int("1"))

############### 96 ################
# Write a Python program to print the current call stack.

#import tracebck

############### 97 ################
# Write a Python program to list the special variables used within the language.

# #solution
# s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
# print()
# print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
# print()

############### 98 ################
# Write a Python program to get the system time.
#solution
# import time
# print()
# print(time.ctime())
# print()

############### 99 ################
# Write a Python program to clear the screen or terminal.

# #solution
# import os
# import time
# # for windows
# os.system('cls')
# # os.system("ls")
# # time.sleep(2)
# # Ubuntu version 10.10
# # os.system('clear')

############### 100 ################
# Write a Python program to get the name of the 
# host on which the routine is running.
# import socket
# host_name = socket.gethostname()
# print()
# print("Host name:", host_name)
# print()


############### 101 ################


############### 102 ################


############### 103 ################


############### 104 ################


############### 105 ################


############### 106 ################


############### 107 ################


############### 108 ################


############### 109 ################


############### 110 ################
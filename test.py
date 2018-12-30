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

def smallest_multiple(a, b):
    return a, b


print(smallest_multiple(12, 6))

############### 33 ################


############### 34 ################


############### 35 ################


############### 36 ################


############### 37 ################


############### 38 ################


############### 39 ################


############### 40 ################

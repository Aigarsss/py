# bubble sort. check out https://www.calhoun.io/lets-learn-algorithms-implementing-bubble-sort/

# li = [4, 6, 1, 2, 5, 13, 46]

# def bubble_sort(a):
#     for x in range(len(a)):
#         for i in range(len(a)-1):
#             if a[i] > a[i+1]:
#                 a[i], a[i+1] = a[i+1], a[i]
#     return a  


# print(li)
# print(bubble_sort(li))


###################### KATAs https://www.codewars.com ###################
#Kata 1
# def disemvowel(string):
#     vowel = ["a", "e", "i", "o", "u"]
#     new_str = ""
#     for i in range(len(string)):
#         if string[i].lower() not in vowel:
#             new_str += string[i]
#     return new_str

# print(disemvowel("This website is for losers LOL!"))

# Kata 2
# Implement the function unique_in_order which takes as 
# argument a sequence and returns a list of items without 
# any elements with the same value next to each other and 
# preserving the original order of elements.
# def unique_in_order(iterable):
#     dic = []
#     counter = 0
#     for i in iterable:
#         if counter == 0:
#             dic.append(i)
#             counter +=1
#         elif dic[counter-1] != i:
#             dic.append(i)
#             counter +=1
#     return dic

# print(unique_in_order('AAAABBBCCDAABBB'))
# print(unique_in_order('ABBCcAD'))
# print(unique_in_order([1,2,2,3,3]))

# Kata 3
# def getCount(inputStr):
#     num_vowels = 0
#     vow = ["a", "e", "i", "o", "u"]
#     for i in inputStr.lower():
#         if i in vow:
#             num_vowels += 1    
#     return num_vowels

# print(getCount("abracadabra"))

# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")

################ Kata 4 ################
# Your goal in this kata is to implement a difference function, 
# which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b.

# def array_diff(a, b):
#     result = [i for i in a if i not in b]
#     return result
# # alt
#     li = []
#     for i in a:
#         if i not in b:
#             li.append(i)
#     return li

# print(array_diff([1,2,2], [1]))


# new_range  = [i * i for i in range(5) if i % 2 == 0]
# print(new_range)

################ Kata 5 ################
# Count the number of Duplicates
# Write a function that will return the count of distinct 
# case-insensitive alphabetic characters and numeric digits 
# that occur more than once in the input string. The input 
# string can be assumed to contain only alphabets (both uppercase 
# and lowercase) and numeric digits.

# def duplicate_count(text):
#     text = text.lower()
#     dic = {}
#     count = 0
#     for letter in text:
#         dic.setdefault(letter, 0)
#         dic[letter] += 1
#     for k, v in dic.items():
#         if v > 1:
#             count +=1
#     return count

#print(duplicate_count("abcde"))
# #print(duplicate_count("abcsdfSDAFea"))
# print(duplicate_count("aaaabbbbbb"))
#print(duplicate_count("indivisibility"))

################### Kata 6
# Build Tower
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).

# Tower block is represented as *
# import pprint

# def tower_builder(n_floors):
#     # build here
#     drawing = []
#     width = n_floors*2-1 #lvl + lvl-1
#     for i in range(1, width, 2):
#         brick = i*'*'
#         drawing.append(brick.center(width, " "))
#     drawing = '\n'.join(drawing)
#     return drawing

# #pprint.pprint(tower_builder(3))
# print(tower_builder(5))

# # print('*'.center(5, " "))
# # print('***'.center(5, " "))
# # print('*****'.center(5, " "))


################### Kata 6
# If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples 
# of 3 or 5 below the number passed in.

# Note: If the number is a multiple of both 3 and 5, only count it once.

# def solution(number):
#     nums = []
#     for i in range(1,number):
#         if i % 3 == 0 and i % 5 == 0: 
#             nums.append(i)
#         elif i % 3 == 0 or i % 5 == 0:
#             nums.append(i)
#     return sum(nums)

# print(solution(10))


################### Kata 7
# Complete the method/function so that it converts dash/underscore 
# delimited words into camel casing. The first word within the output 
# should be capitalized only if the original word was capitalized.


# def to_camel_case(text):
#     li = list(text)
#     for i in range(len(li)):
#         if li[i] == "-" or li[i] == "_":
#             li[i+1] = li[i+1].upper()
#     stri = "".join(li)
#     newstri = stri.replace("-", "").replace("_", "")
#     return newstri

# print(to_camel_case("the-stealth-warrior")) # returns "theStealthWarrior"
# print(to_camel_case("The_Stealth_Warrior")) # returns "TheStealthWarrior"

#################### Kata 8
# Write a function that takes an integer as input, and returns the 
# number of bits that are equal to one in the binary representation 
# of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the 
# function should return 5 in this case

# def countBits(n):
#     value = format(n, "08b")
#     count = 0
#     for i in value:
#         if i == str(1):
#             count +=1
#     return count

# print(countBits(1234))

################## Kata 8
# Does my number look big in this?
# A Narcissistic Number is a number which is the sum of its own digits, 
# each raised to the power of the number of digits in a given base. 
# In this Kata, we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits):
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1634 (4 digits):
#     1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
# The Challenge:

# Your code must return true or false depending upon whether the given 
# number is a Narcissistic number in base 10.

# Error checking for text strings or other invalid inputs is not required, 
# only valid integers will be passed into the function.

# def narcissistic(value):
#     le = len(str(value))
#     stringify = str(value)
#     total = 0
#     for i in range(le):
#         total += int(stringify[i])**le
#     if total == value:
#         return True
#     else:
#         return False

# print(narcissistic(153))

###################### Kata 9

# def song_decoder(song):
#     x = song.replace("WUB", " ")
#     spl =  x.split()
#     return " ".join(spl)

# print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
#   # =>  WE ARE THE CHAMPIONS MY FRIEND

################## Kata 9
# Enough is enough!
# Alice and Bob were on a holiday. Both of them took many pictures 
# of the places they've been, and now they want to show Charlie their 
# entire collection. However, Charlie doesn't like this sessions, 
# since the motive usually repeats. He isn't fond of seeing the Eiffel 
# tower 40 times. He tells them that he will only sit during the session 
# if they show the same motive at most N times. Luckily, Alice and Bob are 
# able to encode the motive as a number. Can you help them to remove numbers 
# such that their list contains each number only up to N times, without 
# changing the order?

# Task
# Given a list lst and a number N, create a new list that contains 
# each number of lst at most N times without reordering. For example 
# if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], 
# drop the next [1,2] since this would lead to 1 and 2 being in the 
# result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

# def delete_nth(li, num):
#     dic = {}
#     new = []
#     for i in li:
#         dic.setdefault(i,0)
#         if dic[i] < num:
#             new.append(i)
#         dic[i] += 1
#     return new

# print(delete_nth([1,1,1,1],2)) # return [1,1]
# print(delete_nth([20,37,20,21],1)) # return [20,37,21]

################## KATA 10
# Complete the function scramble(str1, str2) that returns 
# true if a portion of str1 characters can be rearranged to match 
# str2, otherwise returns false.
# Notes:
# Only lower case letters will be used (a-z). No punctuation or 
# digits will be included.
# Performance needs to be considered
# Input strings s1 and s2 are null terminated.

# import re

# def scramble(s1, s2):
#     status = True
#     for i in s2:
#         if i not in s1:
#             status = False
#             break
#     return status


# print(scramble('rkqodlw', 'world')) # ==> True
# print(scramble('cedewaraaossoqqyt', 'codewars')) # ==> True
# print(scramble('katas', 'steak')) # ==> False

# #passed, but perf tests failed.

################# Kata 11
# My friend John and I are members of the "Fat to Fit Club (FFC)". 
# John is worried because each month a list with the weights of members 
# is published and each month he is the last on the list which means he 
# is the heaviest.

# I am the one who establishes the list so I told him: "Don't worry any 
# more, I will modify the order of the list". It was decided to attribute 
# a "weight" to numbers. The weight of a number will be from now on the 
# sum of its digits.

# For example 99 will have "weight" 18, 100 will have "weight" 1 so in 
# the list 100 will come before 99. Given a string with the weights of 
# FFC members in normal order can you give this string ordered by "weights"
#  of these numbers?

# Example:
# "56 65 74 100 99 68 86 180 90" ordered by numbers weights 
# becomes: "100 180 90 56 65 74 68 86 99"

# When two numbers have the same "weight", let us class them as if 
# they were strings and not numbers: 100 is before 180 because its 
# "weight" (1) is less than the one of 180 (9) and 180 is before 90 
# since, having the same "weight" (9) it comes before as a string.

# All numbers in the list are positive numbers and the list can be empty.

# Notes
# it may happen that the input string have leading, trailing 
# whitespaces and more than a unique whitespace between two 
# consecutive numbers
# Don't modify the input
# For C: The result is freed.

# def order_weight(strng):
#     li = strng.split(" ")
#     return li

# print(order_weight("103 123 4444 99 2000"))
# # "2000 103 123 4444 99")
# #print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
# # "11 11 2000 10003 22 123 1234000 44444444 9999")

# #dont know

################ kata 12
# There is a queue for the self-checkout tills at the supermarket. 
# Your task is write a function to calculate the total time required 
# for all the customers to check out!

# The function has two input variables:

# customers: an array (list in python) of positive integers 
# representing the queue. Each integer represents a customer, 
# and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# The function should return an integer, the total time required.

# EDIT: A lot of people have been confused in the comments. To try to 
# prevent any more confusion:

# There is only ONE queue, and
# The order of the queue NEVER changes, and
# Assume that the front person in the queue (i.e. the first element in 
# the array/list) proceeds to a till as soon as it becomes free.
# The diagram on the wiki page I linked to at the bottom of the description 
# may be useful.
# So, for example:

# queue_time([5,3,4], 1)
# # should return 12
# # because when n=1, the total time is just the sum of the times

# queue_time([10,2,3,3], 2)
# # should return 10
# # because here n=2 and the 2nd, 3rd, and 4th people in the 
# # queue finish before the 1st person has finished.

# queue_time([2,3,10], 2)
# # should return 12
# N.B. You should assume that all the test input will be valid, 
# as specified above.

# P.S. The situation in this kata can be likened to the
#  more-computer-science-related idea of a thread pool, 
#  with relation to running multiple processes at the same 
#  time: https://en.wikipedia.org/wiki/Thread_pool

# def queue_time(customers, n):
#     return customers, n

# print(queue_time([], 1)) # 0, "wrong answer for case with an empty queue")
# print(queue_time([5], 1)) # 5, "wrong answer for a single person in the queue")
# print(queue_time([2], 5)) #2, "wrong answer for a single person in the queue")
# print(queue_time([1,2,3,4,5], 1)) #15, "wrong answer for a single till")
# print(queue_time([1,2,3,4,5], 100)) #5, "wrong answer for a case with a large number of tills")
# print(queue_time([2,2,3,3,4,4], 2)) #9, "wrong answer for a case with two tills")

# # did not get it

################# 12 Kata
# The rgb() method is incomplete. Complete the method 
# so that passing in RGB decimal values will result in a
#  hexadecimal representation being returned. The valid 
#  decimal values for RGB are 0 - 255. Any (r,g,b) argument 
#  values that fall out of that range should be rounded to the 
#  closest valid value.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

#print('#%02x%02x%02x' % (0, 128, 64))

# def rgb(r, g, b):
#     if r < 0:
#         r = 0
#     if g < 0:
#         g = 0
#     if b < 0:
#         b = 0
#     if r > 255:
#         r = 255
#     if g > 255:
#         g = 255
#     if b > 255:
#         b = 255
#     var = '%02X%02X%02X' % (r, g, b)
#     return var

# print(rgb(255, 255, -90))

###################### 13 kata
# Greed is a dice game played with five six-sided dice. 
# Your mission, should you choose to accept it, is to score a 
# throw according to these rules. You will always be given an array 
# with five six-sided dice values.

#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, 
# a "5" can only count as part of a triplet (contributing to the 500 
# points) or as a single 50 points, but not both in the same roll.

# Example scoring

#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   50 + 2 * 100 = 250
#  1 1 1 3 1   1000 + 100 = 1100
#  2 4 4 5 4   400 + 50 = 450
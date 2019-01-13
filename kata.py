

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

# def score(dice):
#     sum = 0
#     c1 = dice.count(1)
#     c5 = dice.count(5)

#     if c1 >= 3:
#         c1 -= 3
#         sum += 1000
#     sum += c1 * 100

#     if c5 >= 3:
#         c5 -= 3
#         sum += 500
#     sum += c5 * 50

#     if dice.count(2) >= 3: sum += 200
#     if dice.count(3) >= 3: sum += 300
#     if dice.count(4) >= 3: sum += 400
#     if dice.count(6) >= 3: sum += 600

#     return sum


# print(score([2, 3, 4, 6, 2])) # 0)
# print(score([4, 4, 4, 3, 3]))#, 400)
# print(score([2, 4, 4, 5, 4])) #, 450)
# print(score([1, 1, 1, 3, 3]))#, 1000)
# print(score([1, 1, 1, 5, 5]))

################# kata
# We want to create a function that will add numbers together 
# when called in succession.

# add(1)(2);
# // returns 3
# We also want to be able to continue to add numbers to our chain.

# add(1)(2)(3); // 6
# add(1)(2)(3)(4); // 10
# add(1)(2)(3)(4)(5); // 15
# and so on.

# A single call should return the number passed in.

# add(1); // 1
# We should be able to store the returned values and reuse them.

# var addTwo = add(2);
# addTwo; // 2
# addTwo + 5; // 7
# addTwo(3); // 5
# addTwo(3)(5); // 10
# We can assume any number being passed in will be valid whole number.

# class add(int):
#     def __call__(self, value):
#         return add(self + value)
# #return lambda y = None: x if y is None else add(x+y)

# print(add(5))

############################ Kata
# The maximum sum subarray problem consists in finding the maximum 
# sum of a contiguous subsequence in an array or list of integers:

# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and 
# the maximum sum is the sum of the whole array. If the list is made 
# up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the 
# empty list or array is also a valid sublist/subarray.

# def maxSequence(arr):
#     current = 0
#     max = 0
#     for i in arr:
#         current += i
#         if current < 0: current = 0
#         if current > max: max = current
#     return max


# print(maxSequence([])) # 0)
# print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6)

####################### Kata

# def solution(string, ending):
#     if string.endswith(ending):
#         return True
#     else:
#         return False

# print(solution('abc', 'bc'))

####################### Kata
# isogram
# An isogram is a word that has no repeating letters, 
# consecutive or non-consecutive. Implement a function that 
# determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.

# def is_isogram(string):
#     string = string.lower()
#     for i in range(len(string)):
#         if string[i] in string[i+1:]:
#             print(string[i], string[i+1:])
#             return False
#     return True

# def is_isogram(string):
#     print(len(string))
#     print()
#     print(len(set(string.lower())))
#     print(set(string.lower()))
#     return len(string) == len(set(string.lower()))

# #print(is_isogram("Dermatoglyphics"))# true
# #print(is_isogram("aba" ))# false
# #print(is_isogram("moOse" ))#false # -- ignore letter case

################### Kata
# Sum of Pairs
# Given a list of integers and a single sum value, return the first 
# two values (parse from the left please) in order of appearance that 
# add up to form the sum.

# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]

# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]

# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)

# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]
# Negative numbers and duplicate numbers can and will appear.

# There will also be lists tested of lengths upwards of 
# 10,000,000 elements. Be sure your code doesn't time out.

# def sum_pairs(ints, s):
#     li =[]
#     for i in range(len(ints)):
#         for a in range(i+1,len(ints)):
#             if ints[i] + ints[a] == s:
#                 li.append(ints[i])
#                 li.append(ints[a])
#                 return li

# print(sum_pairs([4, 3, 2, 3, 4], 6)) # 4, 2

# #Times out.

############## pete the baker kata
# Pete likes to bake some cakes. He has some recipes and ingredients. 
# Unfortunately he is not good in maths. Can you help him to find out, 
# how many cakes he could bake considering his recipes?

# Write a function cakes(), which takes the recipe (object) and the 
# available ingredients (also an object) and returns the maximum number 
# of cakes Pete can bake (integer). For simplicity there are no units for 
# the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
# Ingredients that are not present in the objects, can be considered as 0.


def cakes(recipe, available):
    li = []
    counter =[]
    if recipe.keys() == available.keys() or available.keys() - recipe.keys():
        for key in recipe.keys():
            if key in available.keys():
                counter.append(int(available[key]/recipe[key]))
        return min(counter)
    else:
        li = 0
        return li


# recipe = {'flour': 300, 'oil': 100, 'milk': 100, 'apples': 3, 'sugar': 150} 
# available = {'flour': 2000, 'milk': 2000, 'sugar': 500}

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5}

print(cakes(recipe, available)) 


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


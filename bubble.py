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
# Sort the odd
# You have an array of numbers.
# Your task is to sort ascending odd numbers but even 
# numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. 
# If you have an empty array, you need to return it.

# Example

# sort_array([0, 5, 3, 2, 8, 1, 4]) == [0, 1, 3, 2, 8, 5, 4]

def sort_array(source_array):
    # Return a sorted array.
    # create dictionary. place = key, value = value
    dic = {}
    for i in source_array:
        dic.setdefault(source_array.index(i), i)
    for x, y in dic.items():
        if y % 2 != 0:
            print(x, y)
    return dic

print(sort_array([0, 5, 3, 2, 8, 1, 4]))
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
# An isogram is a word that has no repeating letters, consecutive or 
# non-consecutive. Implement a function that determines whether a 
# string that contains only letters is an isogram. Assume the empty 
# string is an isogram. Ignore letter case.

def is_isogram(string):
    #your code here
    stri = []
    prev = None
    for i in range(len(string)):
        print(i)
    return string

#print(is_isogram("Dermatoglyphics")) #== true
print(is_isogram("aba")) #== false
#print(is_isogram("moOse")) #== false # -- ignore letter case
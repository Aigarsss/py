###############Chapter 4 – Lists

# li1 = [1,2,3]
# li2 = ["four", "five", "six"]
# new = li1 + li2

# print(new)

# del li1[2]
# print(li1)

# li.index(value)
# li.insert(value, spot)
# li.append(value) # adds to end
# li.remove(value) # adds to end

# spam = ['a', 'z', 'A', 'Z']
# spam.sort()
# print(spam)
# spam.sort(key=str.lower)
# print(spam)

# import copy

# list1 = ["a", "b", "c"]
# list2 = copy.copy(list1)
# list2[1] = 4
# print(list1)
# print(list2)

# #copy.deepcopy() for nested lists

# spam = ['apples', 'bananas', 'tofu', 'cats']

# def string(li):
#     nli = ''
#     for i in li:
#         if i == li[-1]:
#             nli += "and " + i
#         else:   
#             nli += i + ", "
#     return nli

# print(string(spam))

# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]

# def tree(li):
#     val = ''
#     for x in range(6) :
#         for i in range(len(li)):
#             if i == len(li)-1:
#                 val += grid[i][x] + "\n"
#             else:
#                 val += grid[i][x]
#     return val

# print(tree(grid))
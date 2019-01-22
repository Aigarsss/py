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

############################ bubble sort again

# # Sweep part non optimized
# example = [5, 4, 2, 3, 1, 0]

# def sweep(numbers):
#     n = len(numbers)
#     first_index = 0
#     second_index = 1
    
#     while second_index < n:
#         first_number = numbers[first_index]
#         second_number = numbers[second_index]
        
#         if first_number > second_number:
#             numbers[first_index] = second_number
#             numbers[second_index] = first_number

#         first_index += 1
#         second_index += 1


# def bubble_sort(numbers):
#     n = len(numbers)
#     for i in range(n):
#         sweep(numbers)
#     return numbers

# #print(sweep(example))
# print(bubble_sort(example))


# Sweep part optimized
# example = [5, 4, 2, 3, 1, 0]

# def sweep(numbers, prevPasses): # prev passess added
#     n = len(numbers)
#     first_index = 0
#     second_index = 1
    
#     while second_index < (n - prevPasses): # prev passess added
#         first_number = numbers[first_index]
#         second_number = numbers[second_index]
        
#         if first_number > second_number:
#             numbers[first_index] = second_number
#             numbers[second_index] = first_number
        
#         first_index += 1
#         second_index += 1


# def bubble_sort(numbers):
#     n = len(numbers)
#     for i in range(n):
#         sweep(numbers, i) # i passess added
#     return numbers

# #print(sweep(example))
# print(bubble_sort(example))

########################################
# 1. Sort a list of 25 numbers in REVERSE order
# Given the array of numbers:

# nums = [21, 4, 2, 13, 10, 0, 19, 11, 7, 5, 23, 18, 9, 14, 6, 8, 1, 20, 17, 3, 16, 22, 24, 15, 12]

# def sort_desc(nums):
#     n = len(nums)
#     for i in range(n):
#         first_index = 0
#         second_index = 1
#         while second_index < n:
#             a = nums[first_index]
#             b = nums[second_index]
#             if nums[first_index] < nums[second_index]:
#                 nums[second_index] = a
#                 nums[first_index] = b
#             first_index += 1
#             second_index += 1
#     return nums

# print(sort_desc(nums))

#################
# print('a'>'b')

# houses = ['Tim', 'Tommy', 'Brad']

# def deliver_presents_iteratively():
#     for i in houses:
#         print("Present delivered to: " + i)

# print(deliver_presents_iteratively())

# print(5//2)

# recursion
# 1 + + 3 ... 10

# def sum_recursive(current_number, accumulated_sum):
#     #base case
#     if current_number == 11:
#         return accumulated_sum
#     else:
#         return sum_recursive(current_number + 1, accumulated_sum + current_number)

# print(sum_recursive(1,0))

#### factorial 5! = 5x4x3x2x1
# num = 5
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num-1)

# print(factorial(num))

# print(factorial(num))
# 1 1 2 3 5 8 13 21 34 55
# 1 2 3 4 5 6  7  8  9 10

def fib(n):
    return n


print(fib(5))

print([i for i in range(10) if i>6])

f = lambda a: a+a

print(f(5))
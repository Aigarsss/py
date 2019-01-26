##############################Chapter 3 – Functions

# def hello():
#     print("hello")
#     print("WHaaat","what", sep="*")

# print(hello())

# import random
# def fortune(a):
#     if a<=3:
#         return "Lucky you!"
#     elif 4<=a<=8:
#         return "Could be worse"
#     elif a>=9:
#         return "Jackpot"

# a = random.randint(1,10)
# fortune = fortune(a)
# print(fortune)

# print("hello", " world", sep="****", end = "")
# print(", shoud be a new line")

# def spam(divBy):
#     try:
#         return 42 / divBy
#     except ZeroDivisionError:
#         return "Dont divide by 0"

# print(round(spam(2)))
# print(spam(0))
# print(spam(3))

#numbers guessing game

# import random
# number = random.randint(1,20)
# choice = 0
# counter = 0
# print("Guess a number between 1-20")
# while counter <= 5:
#     choice = int(input("Please choose a number: "))
#     if choice < number:
#         print("Think bigger")
#         counter +=1
#     if choice > number:
#         print("Think smaller")
#         counter +=1
#     if choice == number:
#         counter +=1
#         print ("That is correct. The number was " + str(choice) + ". It took you " + str(counter) + " tries!")
#         break
#     if counter == 5:
#         print("You failed, number was " + str(number))
#         break

# def collatz(number):
#     if number % 2 == 0:
#         result = number // 2
#         print(result)
#         return result
#     else:
#         result = 3 * number + 1
#         print(result)
#         return result

# num = int(input("Give me a number: "))
# while num != 1:
#     num = collatz(num)
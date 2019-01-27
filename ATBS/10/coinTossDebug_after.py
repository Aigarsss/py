#! python3

# The following program is meant to be a simple coin toss guessing game. 
# The player gets two guesses (it’s an easy game). However, 
# the program has several bugs in it. Run through the program a few times 
# to find the bugs that keep the program from working correctly.

# import random, logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# # logging.disable(logging.CRITICAL) # to disable logging

# guess = ''
# while guess not in ('heads', 'tails'):
#     print('Guess the coin toss! Enter heads or tails:')
#     guess = input().lower()
# if guess == 'heads':
#     guess = 1
# else:
#     guess = 0
# toss = random.randint(0, 1) # 0 is tails, 1 is heads
# if toss == guess:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = input().lower()
#     if guess == 'heads':
#         guess = 1
#     else:
#         guess = 0
#     if toss == guess:
#        print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')


# https://github.com/IFinners/automate-the-boring-stuff-projects/blob/master/Chapter%2010/debug_toss.py
"""Debug Coin Toss Program."""

import random

guess = input('Guess the coin toss! Enter heads or tails: ')
if guess != 'heads' and guess != 'tails':
    raise Exception('Guess must be heads or tails!')

GUESS_CONVERTER = {0: 'heads', 1: 'tails'}
toss = GUESS_CONVERTER[random.randint(0, 1)] # 0 is tails, 1 is heads

if toss == guess:
    print('You got it!')
else:
    guess = input('Nope! Guess again!: ')
    if guess != 'heads' and guess != 'tails':
        raise Exception('Guess must be heads or tails!')
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
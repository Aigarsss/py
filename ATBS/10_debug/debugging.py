#! python3

# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be 1 char')
#     if width <= 2:
#         raise Exception('Width must be more than 2')
#     if height <= 2:
#         raise Exception('Height must be more than 2')
#     print(symbol * width)
#     for i in range(height-2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)

# for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
#     try:
#         boxPrint(sym, w, h)
#     except Exception as err:
#         print('An eception occured: ' + str(err))

# def spam():
#     bacon()
# def bacon():
#     raise Exception('This is an error msg')

# spam()

# TRACEBACK

# import traceback, os
# try:
#     raise Exception('This is the error msg')
# except:
#     errorFile = open(os.path.join(os.getcwd(), 'errorInfo.txt'), 'w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to the errorInfo.txt')

# ASSERT
# podBayDoorStatus = 'open'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open"'
# podBayDoorStatus == 'I\'m sorry, Dave. I\'m afraid I can\'t do that.'
# assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open"'

# assert with stoplights
# market_2nd = {'ns': 'green', 'ew': 'red'}
# mission_1th = {'ns': 'red', 'ew': 'green'}

# def switchLights(stoplight):
#     for key in stoplight.keys():
#         if stoplight[key] == 'green':
#             stoplight[key] = 'yellow'
#         elif stoplight[key] == 'yellow':
#             stoplight[key] = 'red'
#         elif stoplight[key] == 'red':
#             stoplight[key] = 'green'

#     assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

# print(switchLights(market_2nd))

#### Using the logging Module

# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# # logging.disable(logging.CRITICAL) # to disable logging

# logging.debug('Start program')
# def factiorial(n):
#     total = 1
#     logging.debug('Start of factorial({})'.format(n))
#     for i in range(1, n+1):
#         total *= i
#         logging.debug('i is ' + str(i) + ', total is ' + str(total))
#     logging.debug('end of factorial{}'.format(n))
#     return total

# print(factiorial(5))


## logging levels
# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('message')
# logging.info('message')
# logging.warning('message')
# logging.error('message')
# logging.critical('message')

# ## logging to a file 
# logging.basicConfig(filename='myProgramLog.txt',....)

import random
heads = 0 
for i in range(1, 1001):
    if random.randint(0,1):
        heads += 1
    if i == 500:
        print('Halfway there')
print('Heads came up ' + str(heads) + ' times')
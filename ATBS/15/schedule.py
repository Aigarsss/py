# Chapter 15 – Keeping Time, Scheduling Tasks, and Launching Programs
# python schedule.py

'''
##### Time module 

import time
#print(time.time()) # returns seconds since epoch (1970)

def calcProd():
    # Calculate the prodct of first 100 000 numbers
    product = 1
    for i in range(1, 100000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is {} digits long'.format(len(str(prod))))
print('Took {} seconds to calculate'.format(endTime - startTime))

### Sleep
import time
for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)

### rounding

import time
now = time.time()

print(round(now, 2))
print(round(now))

##### The datetime Module
import datetime
print(datetime.datetime.now())
dt = datetime.datetime(2015,10,21,16,29,0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

import datetime, time
# convert epoch time to date stamp
print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))


import datetime, time
# compare dates
small = datetime.datetime.fromtimestamp(1000000)
large = datetime.datetime.fromtimestamp(time.time())
print(small < large) # true

# datetime.timedelta
import datetime
delta = datetime.timedelta(days = 11, hours = 10, minutes = 9, seconds = 8)
print(delta.days, delta.seconds, delta.microseconds) # 11 36548 0
print(delta.total_seconds()) # 986948.0
print(str(delta))  # 11 days, 10:09:08

dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

# caluclations with dates
import datetime
oct21t = datetime.datetime(2015,10,21,16,29,0)
aboutThirtyYears = datetime.timedelta(days = 365 * 30)
print(oct21t) # 2015-10-21 16:29:00
print(oct21t - aboutThirtyYears) # 1985-10-28 16:29:00
print(oct21t - (2 * aboutThirtyYears)) # 1955-11-05 16:29:00

# pausing until date time.sleep()
import datetime, time
halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2019:
    time.sleep(1) # sleep in seconds

# Converting datetime Objects into Strings
import datetime
oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st) # 2015-10-21 16:29:00
print(oct21st.strftime('%Y/%m/%d %H:%M:%S')) # 2015/10/21 16:29:00
print(oct21st.strftime('%I:%M %p')) # 04:29 PM
print(oct21st.strftime("%B of '%y")) # October of '15

# Converting Strings into datetime Objects
import datetime
print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')) # 2015-10-21 00:00:00


### Multithreading

import threading, time
print('Start program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target = takeANap)
threadObj.start()

print('End of program.')


# Passing Arguments to the Thread’s Target Function
import threading
# print('Cats', 'Dogs', 'Frogs', sep=' & ') equals to below
threadObj = threading.Thread(target=print, args = ['Cats', 'Dogs','Frogs'], kwargs={'sep': ' & '})
threadObj.start()


'''








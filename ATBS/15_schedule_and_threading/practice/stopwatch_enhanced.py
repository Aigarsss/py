#! python3
# python stopwatch.py

# At a high level, here’s what your program will do:
# Track the amount of time elapsed between presses of the 
# ENTER key, with each key press starting a new “lap” on the timer.
# Print the lap number, total time, and lap time.

# This means your code will need to do the following:
# Find the current time by calling time.time() and store it as a 
# timestamp at the start of the program, as well as at the start of each lap.
# Keep a lap counter and increment it every time the user presses ENTER.
# Calculate the elapsed time by subtracting timestamps.
# Handle the KeyboardInterrupt exception so the user can 
# press CTRL-C to quit.

# Expand the stopwatch project from this chapter so that it uses the 
# rjust() and ljust() string methods to “prettify” the output. 
# (These methods were covered in Chapter 6.) 

import time, pyperclip
# display programs instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" stopwatch. CTRL+C to quit')
input()
print('Started')
startTime = time.time() # get first laps start time
lastTime = startTime
lapNum = 1

# Start tracking the laps
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        #print('Lap #{}: total: {}, last laptime: {}'.format(lapNum, totalTime, lapTime), end='') # end to avoid doublel space
        output ='Lap #' + str(lapNum).rjust(3, ' ') + ': ' + str(totalTime).rjust(6,' ') + ' (' +  str(lapTime).rjust(6, ' ') + ')' # end to avoid double space
        print(output, end='')
        pyperclip.copy(output)
        lapNum += 1
        lastTime = time.time() # reset laptime
except KeyboardInterrupt:
    # Handle the ctrl+c exception to keep its error msg from displaying
    print('\nDone.')

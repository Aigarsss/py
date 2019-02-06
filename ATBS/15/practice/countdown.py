#! python3
# python countdown.py

# At a high level, here’s what your program will do:
# Count down from 60.
# Play a sound file (alarm.wav) when the countdown reaches zero.

# This means your code will need to do the following:
# Pause for one second in between displaying each number in the 
# countdown by calling time.sleep().
# Call subprocess.Popen() to open the sound file with the default 
# application.

 ## this does not work. need to check

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft  -= 1

# play a sound
subprocess.Popen(['start', 'alarm.wav'], shell=True)
#! python3
# python mouseNow.py

# At a high level, here’s what your program should do:
# Display the current x- and y-coordinates of the mouse cursor.
# Update these coordinates as the mouse moves around the screen.

# This means your code will need to do the following:
# Call the position() function to fetch the current coordinates.
# Erase the previously printed coordinates by printing \b backspace characters to the screen.
# Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit.

import pyautogui
print('Press Ctrl-C to quit.')

# get the coordinates
try:
    while True:
        # get the coordinates
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end = '')
        print('\b' * len(positionStr), end = '', flush=True)
except KeyboardInterrupt:
    print('\nDone')
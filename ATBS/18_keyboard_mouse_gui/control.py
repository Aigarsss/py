# python control.py
# pip install pyautogui

'''

# failsafes and cancelling
import pyautogui
pyautogui.PAUSE = 1 # pauses every second
pyautogui.FAILSAFE = True # if you move mouse to upper left corner, excepts
print(pyautogui.size()) # gets screen res tuple Size(width=1366, height=768)

# controling the mouse
import pyautogui
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25) # duration is not manditory
    pyautogui.moveTo(200, 100, duration=0.25) 
    pyautogui.moveTo(200, 200, duration=0.25) 
    pyautogui.moveTo(100, 200, duration=0.25) 

# move cursor relative to location
import pyautogui
for i in range(10):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)

# getting the mouse position
import pyautogui
print(pyautogui.position()) # Point(x=1101, y=354)

# clicking the mouse
import pyautogui
pyautogui.click(50,5) # this clicks, file in vs code. can also use mouseUp(), mouseDown()

# dragging the mouse
import pyautogui, time
# drawing with these commands
time.sleep(5)
pyautogui.click() # to put drawing program in focus
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2) # dragTo is alternative, but it will not be relative
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance -= 5
    pyautogui.dragRel(0, - distance, duration=0.2)


# scrolling the mouse
import pyautogui
pyautogui.scroll(200)

import time, pyautogui
time.sleep(5); pyautogui.scroll(100) #doesnt work

# Getting a Screenshot
import pyautogui
im = pyautogui.screenshot()
print(im.getpixel((50, 200))) # (30, 31, 28)

# matching the screen color
print(pyautogui.pixelMatchesColor(50, 200, (30, 31, 28))) # true

# Image Recognition
import pyautogui
print(list(pyautogui.locateAllOnScreen('submit.png'))) # just returns object, not tuple as in book. Needs to be used with list() even with single vaue
# [Box(left=81, top=244, width=123, height=46)]
print(pyautogui.center((81,244,123,46))) # Point(x=142, y=267)
pyautogui.click(142, 267)

# controlling the keyboard
import pyautogui
pyautogui.click(100,100) # open notepad in upper left corner
pyautogui.typewrite('Hello world', interval=0.2) # second argument for time in between strokes
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y']) # XYab, because of 2 * left
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')

# hotkeys and combos
import pyautogui
pyautogui.hotkey('ctrl', 'c')


moveTo(x, y). Moves the mouse cursor to the given x and y coordinates.

moveRel(xOffset, yOffset). Moves the mouse cursor relative to its current position.

dragTo(x, y). Moves the mouse cursor while the left button is held down.

dragRel(xOffset, yOffset). Moves the mouse cursor relative to its current position while the left button is held down.

click(x, y, button). Simulates a click (left button by default).

rightClick(). Simulates a right-button click.

middleClick(). Simulates a middle-button click.

doubleClick(). Simulates a double left-button click.

mouseDown(x, y, button). Simulates pressing down the given button at the position x, y.

mouseUp(x, y, button). Simulates releasing the given button at the position x, y.

scroll(units). Simulates the scroll wheel. A positive argument scrolls up; a negative argument scrolls down.

typewrite(message). Types the characters in the given message string.

typewrite([key1, key2, key3]). Types the given keyboard key strings.

press(key). Presses the given keyboard key string.

keyDown(key). Simulates pressing down the given keyboard key.

keyUp(key). Simulates releasing the given keyboard key.

hotkey([key1, key2, key3]). Simulates pressing the given keyboard key strings down in order and then releasing them in reverse order.

screenshot(). Returns a screenshot as an Image object. (See Chapter 17 for information on Image objects.)

'''





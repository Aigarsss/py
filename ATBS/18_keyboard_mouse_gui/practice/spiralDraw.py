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
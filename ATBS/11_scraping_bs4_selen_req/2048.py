# 2048 is a simple game where you combine tiles by sliding them up, 
# down, left, or right with the arrow keys. You can actually 
# get a fairly high score by repeatedly sliding in an up, right, 
# down, and left pattern over and over again. Write a program that 
# will open the game at https://gabrielecirulli.github.io/2048/ 
# and keep sending up, right, down, and left keystrokes to 
# automatically play the game.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://play2048.co/')

element = browser.find_element_by_tag_name('html')
elementAgain = browser.find_element_by_class_name('retry-button')

i = 0
while i < 100: # ketchy way to do it, but i dont know how to do the 'while' for the javascript 'popup'
    element.send_keys(Keys.ARROW_RIGHT)
    element.send_keys(Keys.ARROW_DOWN)
    element.send_keys(Keys.ARROW_LEFT)
    element.send_keys(Keys.ARROW_UP)
    i += 1

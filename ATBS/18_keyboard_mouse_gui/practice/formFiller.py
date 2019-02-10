#! python3

# At a high level, here’s what your program should do:
# Click the first text field of the form.
# Move through the form, typing information into each field.
# Click the Submit button.

# Repeat the process with the next set of data.
# This means your code will need to do the following:
# Call pyautogui.click() to click the form and Submit button.
# Call pyautogui.typewrite() to enter text into the fields.
# Handle the KeyboardInterrupt exception so the user can press CTRL-C to quit.

# you need to have the http://autbor.com/form form open and active on main monitor 

import time, pyautogui, webbrowser


# modify these to work on your pc
nameField = (400, 550)
# submitButton = (651, 817)
# submitButtonColor = (75,141, 249)
submitAnotherLink = (400, 430)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
           ]

pyautogui.PAUSE = 0.5

try:
    for person in formData:
        # give the user a chance to kill the script.
        print('>>> 5 second pause to let user press ctrl-c')
        time.sleep(5)

        # need to think about this, the form has changed
        # while not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1], submitButtonColor):
        #   time.sleep(0.5) 

        pyautogui.typewrite(['tab', 'tab'])
        print('Entering {} info ...'.format(person['name']))
        pyautogui.click(nameField[0], nameField[1])
        # fill out the name field       
        pyautogui.typewrite(person['name'] + '\t')
        # fill out the greatest fear
        pyautogui.typewrite(person['fear'] + '\t')

        # fill out the source of wizard powers field
        if person['source'] ==  'wand':
            pyautogui.typewrite(['down', 'enter', '\t'], interval=0.5)
        elif person['source'] ==  'amulet':
            pyautogui.typewrite(['down','down', 'enter', '\t'], interval=0.5)
        elif person['source'] ==  'crystal ball':
            pyautogui.typewrite(['down','down','down','enter', '\t'], interval=0.5)
        elif person['source'] ==  'money':
            pyautogui.typewrite(['down','down','down','down','enter', '\t'], interval=0.5)

        # fill out the robocop field
        if person['robocop'] == 1:
            pyautogui.typewrite([' ', '\t'])
        if person['robocop'] == 2:
            pyautogui.typewrite(['right', '\t'])
        if person['robocop'] == 3:
            pyautogui.typewrite(['right', 'right', '\t'])
        if person['robocop'] == 4:
            pyautogui.typewrite(['right', 'right','right', '\t'])
        if person['robocop'] == 5:
            pyautogui.typewrite(['right', 'right','right','right' '\t'])

        # fill out comment
        pyautogui.typewrite(person['comments'] + '\t')
        
        # submit
        pyautogui.typewrite(['enter'])

        # wait until page oaded
        print('Clicked submit')
        time.sleep(5)

        # click to submit another response
        pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
except KeyboardInterrupt:
    print('Filling was stopped by user')
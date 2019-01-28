#! python3
# $ python mapit.py 870 Valencia St, San Francisco, CA 94110

import webbrowser, sys, pyperclip

# get address from command line
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    # get the addres from clipboard
    address = pyperclip.paste()

# open the browser
webbrowser.open('https://www.google.com/maps/place/' + address)


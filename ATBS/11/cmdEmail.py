#! python3

# Write a program that takes an email address and string of 
# text on the command line and then, using Selenium, logs into 
# your email account and sends an email of the string to the provided 
# address. (You might want to set up a separate email account for 
# this program.)

# This would be a nice way to add a notification feature to your 
# programs. You could also write a similar program to send messages 
# from a Facebook or Twitter account.

# python cmdEmail.py example@email.com This is some text
# python cmdEmail.py email@email.com this is some text

# not exactly what was asked, but dont want to mess with email passes etc.

import sys
from selenium import webdriver

# assign the url
emailUrl = 'https://mdn.github.io/learning-area/html/forms/your-first-HTML-form/first-form-styled.html'
name = 'Tester'

# get the variables
if len(sys.argv) > 2:
    eMail = sys.argv[1]
    mailText = ' '.join(sys.argv[2:])

    # open browser
    browser = webdriver.Chrome()
    browser.get(emailUrl)
    htmlName = browser.find_element_by_id('name').send_keys(name)
    htmlEmail = browser.find_element_by_id('mail')
    htmlEmail.send_keys(eMail)
    htmlText = browser.find_element_by_id('msg')
    htmlText.send_keys(mailText)
    htmlSub = browser.find_element_by_css_selector('button[type=submit')
    htmlSub.submit()

else:
    print('plese provide valid email and string')



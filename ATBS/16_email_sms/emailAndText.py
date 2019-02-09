# Sending Email and Text Messages
# python emailAndText.py

'''
import smtplib
smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('user@user.com', 'pass')
smtpObj.sendmail('bob@bob.com', 'alice@alice.com, 'subject \n text)
smtpObj.quit()

import smtplib
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(type(smtpObj)) # <class 'smtplib.SMTP'>
smtpObj.ehlo()
print(smtpObj.ehlo()) # <class 'smtplib.SMTP'>
# (250, b'smtp.gmail.com at your service, # 250 for success
# [46.109.114.152]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
print(smtpObj.starttls()) # (220, b'2.0.0 Ready to start TLS')
smtpObj.starttls()
smtpObj.login('my_email_address@gmail.com', ' MY_SECRET_PASSWORD')
smtpObj.sendmail(' my_email_address@gmail.com ', ' recipient@example.com ', 'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
smtpObj.quit()

# getting mails from IMAP. imapclient and pyzmail (cant be installed) needs to be pip installed
# didnt do this part, as module couldnt be installed


# needed to pip install twilio
# this needs to be redone, it doesnt work as described

from twilio.rest import TwilioRestClient
accountSID = ''
authToken = ''
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = ''
myCellPhone = ''
# below marks as error, so pack must have changed
message = twilioCli.messages.create(body = 'This is a test msg', from_ = myTwilioNumber, to = myCellPhone)


'''

# example project (has no been ran and doesnt work)

# defines textmyself() function that texts a message passed to it as a string

 # preset values
accountSid = ''
authToken = ''
myNumber = '1245'
twilioNumber = '12345'

from twilio.rest import TwilioRestClient

def textyself(message):
    twilioCli = TwilioRestClient(accountSid, authToken)
    twilioCli.messages.create(body = message, from_ = twilioNumber, to = myNumber)
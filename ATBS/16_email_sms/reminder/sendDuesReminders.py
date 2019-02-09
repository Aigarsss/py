#! python3

# At a high level, here’s what your program will do:
# Read data from an Excel spreadsheet.
# Find all members who have not paid dues for the latest month.
# Find their email addresses and send them personalized reminders.

# This means your code will need to do the following:
# Open and read the cells of an Excel document with the openpyxl module. (See Chapter 12 for working with Excel files.)
# Create a dictionary of members who are behind on their dues.
# Log in to an SMTP server by calling smtplib.SMTP(), ehlo(), starttls(), and login().
# For all members behind on their dues, send a personalized reminder email by calling the sendmail() method.
# python sendDuesReminders.py

import smtplib, openpyxl, sys

# open te sheet and get the latest month
wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb.active

lastCol = sheet.max_column()
latestMonth = sheet.cell(row = 1, column = lastCol).value

# check each members payment status
unpaidMembers = {}
for r in range(2, sheet.max_row() + 1):
    payment = sheet.cell(row = r, column = lastCol).value
    if payment != 'paid':
        name = sheet.cell(row = r, column = 1).value
        email = sheet.cell(row = r, column = 2).value
        unpaidMembers[name] = email


# log in to email

smtpObj = smtplib.SMTP('smtp.gmail.com', 787)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('email', 'pass')

# send out reminder
for name, email in unpaidMembers.items():
    body = 'Subject: {} dues unpaid.\nDear {}, \nRecords show unpaid dues for {}. Please pay them.'.format(latestMonth, name, latestMonth)
    print('Sending email to ' + email)
    sendmailStatus = smtpObj.sendmail('myemail', email, body) # method will return a nonempty dictionary value if the SMTP server reported an error sending that particular email

    if sendmailStatus != {}:
        print('Problem detected with email to ' + email)

smtpObj.quit()
################ Chapter 7 – Pattern Matching with Regular Expressions

# def isPhoneNumber(text):
#     if len(text) != 12:
#         return False
#     for i in range(3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '-':
#         return False
#     for i in range(4,7):
#         if not text[i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8,12):
#         if not text[i].isdecimal():
#             return False
#     return True

# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
# print('Done')

r'''
REGEX
\d digit character 0 - 9
\D any character that is not numeric
\w any letter, numeric digit or the underscore
\W any character that is not a letter, numeric digit or underscore
\s space, tab or newline
\S any character that is not space, tab or newline
. any char except new line
The ? matches zero or one of the preceding group.
The * matches zero or more of the preceding group.
The + matches one or more of the preceding group.
The {n} matches exactly n of the preceding group.
The {n,} matches n or more of the preceding group.
The {,m} matches 0 to m of the preceding group.
The {n,m} matches at least n and at most m of the preceding group.
{n,m}? or *? or +? performs a nongreedy match of the preceding group.
^spam means the string must begin with spam.
spam$ means the string must end with spam.
The . matches any character, except newline characters.
\d, \w, and \s match a digit, word, or space character, respectively.
\D, \W, and \S match anything except a digit, word, or space character, respectively.
[abc] matches any character between the brackets (such as a, b, or c).
[^abc] matches any character that isn’t between the brackets.


{x} match the previous pattern x times (like \d{2})
import re regex module
regex_object = re.compile(r'\d{3}-\d{3}') # this would match 444-552
result = regex_object.search('444-552')
print(result.group()) # returns the match 444-552
print(re.compile(r'\d{3}-\d{3}').search('444-552').group()) #together

() creates groups - (\d{2})(\d{3})
import re
regex_object = re.compile(r'(\d{3})-(\d{4})')
result = regex_object.search('345-2345')
print(result.group(1))
print(result.group(2))
print(result.group())
print(result.groups())
first_group, second_group = result.groups()
print(first_group)

import re
regex_object = re.compile(r'(\(\d{3}\)) (\d{2}-\d{2})') # escaping parentheses
result = regex_object.search('This is my number (123) 12-24')
print(result.group())

| # this is OR. 1|2 == 1 or 2 returns first occurence
import re
regex_object = re.compile(r'Batman|Tina Fey')
result = regex_object.search('Batman and Tina Fey')
print(result.group())
result = regex_object.search('Tina Fey and Batman')
print(result.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
result = batRegex.search('Batmobile lost a wheel')
print(result.group(), result.group(1), sep="**")

batRegex = re.compile(r'Bat(wo)?man') # ? is an optional part
result = batRegex.search('The adventures of Batman')
print(result.group())
result = batRegex.search('The adventures of Batwoman')
print(result.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
result = phoneRegex.search('My number is 415-555-4242')
print(result.group())
result = phoneRegex.search('My number is 555-4242')
print(result.group())

batRegex = re.compile(r'Bat(wo)*man') # * can repeat 0 or infinite times
result = batRegex.search('The Adventures of Batman')
print(result.group())
result = batRegex.search('The Adventures of Batwowowoman')
print(result.group())

batRegex = re.compile(r'Bat(wo)+man') # + means mach 1 or more
result = batRegex.search('Adventures of Batman')
print(result == None)
result = batRegex.search('Adventures of Batwowowoman')
print(result.group())

haRegex = re.compile(r'(Ha){3}')
result = haRegex.search('HaHaHa')
print(result.group())

haRegex = re.compile(r'(Ha){3,5}') # greedy. will return longest match by def
result = haRegex.search('HaHaHaHa') # HaHaHaHa
print(result.group())
haRegex = re.compile(r'(Ha){3,5}?') #non greedy because of ?. will return shortest match
result = haRegex.search('HaHaHaHa') # HaHaHa
print(result.group())

findall() will find all matches vs search() will find the first one
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
result = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(result.group())

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}') # Cannot have groups for findall
result = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # Has groups
result = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result) # returns tuples within list

#character classes
xmasReg = re.compile(r'\d+\s\w+')
result = xmasReg.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(result)

vowelRegex = re.compile(r'[aeiouAEIOU?]') # custom character class, will match these. special chars dont need to be escaped, see ?
result = vowelRegex.findall('Robocop eats baby food. BABY FOOD?.')
print(result)

vowelRegex = re.compile(r'[^aeiouAEIOU?]') # ^ will match the opposite
result = vowelRegex.findall('Robocop eats baby food. BABY FOOD?.')
print(result)

beginsWithHello = re.compile(r'^Hello') # ^ states that it must begin
result = beginsWithHello.search('Hello world')
print(result)

beginsWithHello = re.compile(r'world$') # $ states that it must end
result = beginsWithHello.search('Hello world')
print(result)

beginsWithHello = re.compile(r'^\d+$') # entire string must match if ^ $ is used
result = beginsWithHello.search('14151x24123') # none, must be all numbers
print(result)

atRegex = re.compile(r'.at') #. is a wildcard (for one char)
result = atRegex.findall('The cat in the hat sat on the flat mat.')
print(result)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') #match everyhting
result = nameRegex.search('First Name: Al Last Name: Sweigart')
print(result.group(1), result.group(2))

nongreedyRegex = re.compile(r'<.*?>') #non greedy
result = nongreedyRegex.search('<To serve man> for dinner.>')
print(result.group())

nongreedyRegex = re.compile(r'<.*>') # greedy
result = nongreedyRegex.search('<To serve man> for dinner.>')
print(result.group())

noNewlineRegex = re.compile(r'.*', re.DOTALL) # include \n
result = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(result.group())

robocop = re.compile(r'robocop', re.IGNORECASE) # or re.I . ignores case
result = robocop.search('RobOCop is part man, part machine, all cop.')
print(result.group())

namesRegex = re.compile(r'Agent \w+') #replacing matches
result = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(result)

agentNamesRegex = re.compile(r'Agent (\w)\w*') # replacing matcches with group results
result = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(result)


'''
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?            # area code
#     (\s|-|\.)?                    # separator
#     \d{3}                         # first 3 digits
#     (\s|-|\.)                     # separator
#     \d{4}                         # last 4 digits
#     (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
#     )''', re.VERBOSE) # re.VERBOSE lets you have multi line regex

# someRegexValue = re.compile(r'foo', re.IGNORECASE | re.DOTALL | re.VERBOSE) # to combine all

### project: Phone Number and Email Address Extractor

# import pyperclip, re
# # phone regex
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?
#     (\s|-|\.)?
#     (\d{3})
#     (\s|-|\.)
#     (\d{4})
#     (\s*(ext|x|ext.)\s*(\d{2,5}))?
# )''', re.VERBOSE)

# # email regex
# emailRegex = re.compile(r'''(
#     [a-zA-Z0-9._%+-]+ #username
#     @                  #@
#     [a-zA-Z0-9.-]+      #domain
#     (\.[a-zA-Z]{2,4})
# )''', re.VERBOSE)

# # TODO: Find matches in clipboard text.
# text = str(pyperclip.paste())
# matches = []
# for groups in phoneRegex.findall(text):
#     phoneNum = '-'.join([groups[1],groups[3],groups[5]])
#     if groups[8] != '':
#         phoneNum += ' x' + groups[8]
#     matches.append(phoneNum)
# for groups in emailRegex.findall(text):
#     matches.append(groups[0])

# # TODO: Copy results to the clipboard.
# if len(matches) > 0:
#     pyperclip.copy('\n'.join(matches))
#     print('copied to clipboard')
#     print('\n'.join(matches))
# else:
#     print('No match found')



# import re

# # nakamotoRegex = re.compile(r'[A-Z][a-z]*\sNakamoto')
# # result = nakamotoRegex.search('Mr Nakamoto')
# # print(result.group())

# regex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
# result = regex.search('Carol throws baseballs.')
# print(result.group())

########### practice projects

## strong password detection
# import re
# text = 'Password1'

# def validatePass(passw):
#     regex_num = re.compile(r'[0-9]+')
#     regex_len = re.compile(r'(.*){8,}')
#     regex_cap = re.compile(r'[A-Z]+')
#     regex_small = re.compile(r'[a-z]+')
#     # print(regex_num.search(passw).group())
#     # print(regex_len.search(passw).group())
#     # print(regex_cap.search(passw).group())
#     # print(regex_small.search(passw).group())

#     if bool(regex_num.search(passw)) and bool(regex_len.search(passw)) and bool(regex_cap.search(passw)) and bool(regex_small.search(passw)):
#         return 'Pass is considered strong' # if matched
#     else:
#         return 'consider a different pass' # id no match

# print(validatePass(text))


## Regex Version of strip()
# import re
# string1 = '    strip     '
# print('*' + string1.strip() + '*')

# string2 = '***24f qas2    '
# def stripped(text, char):
#     if char == '':
#         regex_left = re.compile(r'^[\s]*')
#         text = regex_left.sub('', text)
#         regex_right = re.compile(r'[\s]*$')
#         text = regex_right.sub('', text)
#         return text
#     else:
#         regex_left = re.compile(r'^[{}]*'.format(char))
#         text = regex_left.sub('', text)
#         regex_right = re.compile(r'[{}]*$'.format(char))
#         text = regex_right.sub('', text)
#         return text

# print('*' + stripped(string2, '*') + '*')
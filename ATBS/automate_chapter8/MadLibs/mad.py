#! python3
# Program to create madlibs. it reads Source_lib.txt and offers to replace adjective,
# noun, verb, noun


# open and read a file
openSource = open('Source_lib.txt', 'r')
readSource = openSource.read()
openSource.close()

# get user input for the words that need to be replaced and replace in the strin
adj = input('Enter a adjective: ')
readSource = readSource.replace('ADJECTIVE', adj)

noun = input('Enter a noun: ')
readSource = readSource.replace('NOUN', noun, 1)

verb = input('Enter a verb: ')
readSource = readSource.replace('VERB', verb)

noun2 = input('Enter another noun: ')
readSource = readSource.replace('NOUN', noun2)

# create file with the string and print
print(readSource)
newFile = open('NewLib.txt', 'w')
newFile.write(readSource)
newFile.close()
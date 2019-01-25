#! python3

# mcb.pyw - Saves and loads pieces of tet to the clipboard
# usage: py.exe mcb.pyw save <keywoard> - saves clipboard to keyword
#       py.exe mcb.pyw <keyword> - loads keyword to clipboard
#       py.exe mcb.pyw list - loads all the keywords to clipboard


import shelve, sys, pyperclip

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save': # it is 1 by default + save (2) + keyword (3)
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
# List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()


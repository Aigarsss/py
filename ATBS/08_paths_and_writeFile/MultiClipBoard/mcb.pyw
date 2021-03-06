#! python3

# mcb.pyw - Saves and loads pieces of tet to the clipboard
# usage: py.exe mcb.pyw save <keywoard> - saves clipboard to keyword
#       py.exe mcb.pyw <keyword> - loads keyword to clipboard
#       py.exe mcb.pyw list - loads all the keywords to clipboard
#       py.exe mcb.pyw delete - deletes all entries
#       py.exe mcb.pyw delete <keyword> - deletes the keyword


import shelve, sys, pyperclip

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save': # it is len 1 by default + save (2) + keyword (3)
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        pyperclip.copy('Entry {} deleted'.format(sys.argv[2]))
        del (mcbShelf[sys.argv[2]])
elif len(sys.argv) == 2:
# List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()


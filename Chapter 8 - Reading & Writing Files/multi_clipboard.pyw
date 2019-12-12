# .pyw means Python will not show a Terminal window when it runs this program

# program saves each piece of clipboard text under a keyword
# this can be specified when running the program via command line
# python multi_clipboard spam

# Usage: py.exe multi_clipboard <save> <keyword> - saves clipboard contents to keyword
#        py.exe multi_clipboard save <keyword> - loads keyword to clipboard
#        py.exe multi_clipboard list - loads all keywords to clipboard

import sys
import pyperclip as p
import shelve

# check number of arguments is valid
if len(sys.argv) < 2:
    print("Error: Not enough in-line arguments.")
    
    sys.exit()

# save clipboard contents onto a shelve file
shelf = shelve.open("multi_clipboard")

# saving content to keyword
if sys.argv[1].lower() == "save":
    if len(sys.argv) != 3:
        print("Error: Missing keyword to save to.")
        print("Usage: python multi_clipboard save <keyword>")
    else:
        shelf[sys.argv[2]] = p.paste()  # save clipboard contents to keyword (saved in dict)
        print("Clipboard contents saved to keyword '", sys.argv[2], "'.", sep='')

elif sys.argv[1].lower() == "list":
    p.copy(str(list(shelf.keys())))
    print("List of keys copied to clipboard.")
    print("Keys:", str(list(shelf.keys())))

# delete a keyword from the shelf
elif sys.argv[1].lower() == "delete":
    del shelf[sys.argv[2]]

# assume default is to copy keyword to shelf
elif sys.argv[1] in shelf:
    print("No argument specified. Loading matching contents to clipboard.")
    p.copy(shelf[sys.argv[1]])  # assume this is the keyword e.g. python multiclipboard potato

else:
    print("Keyword not found. Please try again.")

shelf.close()

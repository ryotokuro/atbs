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
    keyword = sys.argv[1]   # capture keyword from user command-line arg
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
        print(shelve)

elif sys.argv[1].lower() == "list":
    print("Command: List requested")
    print(shelf.keys())
    p.copy(str(list(shelf.keys())))

# assume default is to copy keyword to shelf
else:
    print("No argument specified. Copying keyword to shelve.")
    p.copy(shelf[sys.argv[1]])

shelf.close()

# .pyw means Python will not show a Terminal window when it runs this program

# program saves each piece of clipboard text under a keyword
# this can be specified when running the program via command line
# python multi_clipboard spam

# Usage: py.exe multi_clipboard <save> <keyword> - saves clipboard contents to keyword
#        py.exe multi_clipboard save <keyboard> - loads keyword to clipboard
#        py.exe multi_clipboard list - loads all keywords to clipboard

import sys
import pyperclip as p
import shelve

# check number of arguments is valid
if len(sys.argv) < 2:
    keyword = sys.argv[1]   # capture keyword from user command-line arg
    print("Error: Not enough in-line arguments.")
    
    sys.exit()

shelf = shelve.open("multi_clipboard")

keywords = {}
if sys.argv[1].lower() == "save":
    keywords[sys.argv[2]] = p.paste()  # save clipboard contents to keyword (saved in dict)
    print(keywords)

elif sys.argv[1].lower() == "list":
    print("Command: List requested")
    print(keywords)
    if keywords:
        p.copy(keywords.keys())  # copy keywords to clipboard
    else:
        print("There are currently no stored keywords.")

shelf.close()

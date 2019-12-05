# .pyw means Python will not show a Terminal window when it runs this program

# program saves each piece of clipboard text under a keyword
# this can be specified when running the program via command line
# python multi_clipboard spam

import sys

if len(sys.argv) > 1:
    keyword = sys.argv[1]
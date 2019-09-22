#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

# 1. paste text from the keyboard
text = (pyperclip.paste()).split('\r\n')

# 2. add bullet points to it
print(text)
text = ['*'+text[i] for i, v in enumerate(text)]
print(text)

# 3. copy new text to the clipboard
pyperclip.copy(text)

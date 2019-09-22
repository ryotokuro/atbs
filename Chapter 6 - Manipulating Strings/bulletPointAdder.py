#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

# 1. paste text from the keyboard
text = (pyperclip.paste()).split('\n')

# 2. add bullet points to it
print(text)
text = [i.push('*') for i in text]
print(text)

# 3. copy new text to the clipboard
pyperclip.copy()

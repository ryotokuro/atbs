#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import re
import pyperclip as py

# get the text off the clipboard
text = py.paste()

# regex magix (133) 788-2233 and 234-2343
# find all phone numbers
phoneFilter = re.compile(r'''(
                        (\d{3}(\s|-|\.)?|\(\d{3}\)(\s|-|\.)?)?  # area code + separator
                        (\d{3})             # 3 digits
                        (\s|-|\.)           # separator
                        (\d{4})             # 4 digits
                        )''', re.VERBOSE)

numbers = []
for groups in phoneFilter.findall(text):
    numbers.append(groups[0])

if not numbers:  # if empty list
    print('No phone numbers were found in the text :(')
else:
    numbers = '\n'.join(numbers)
    py.copy(numbers) 

# find all emails 
emailFilter = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+   # username
                        @  # @ symbol
                        [a-zA-Z0-9.-]+  # domain
                        (\.[a-zA-Z]+)  # tld
                        (\.[a-zA-Z]+)?  # area domain
                        )''', re.I | re.VERBOSE)

emails = []
for groups in emailFilter.findall(text):
    emails.append(groups[0])

if not emails:
    print('No emails were found in the text :(')
else:
    emails = '\n'.join(emails)
    py.copy(emails.lower())  # convert to lower and copy to clipboard
    



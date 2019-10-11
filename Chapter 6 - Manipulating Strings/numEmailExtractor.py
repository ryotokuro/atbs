#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import re
import pyperclip as py

# get the text off the clipboard
text = py.paste()

# regex magix (133) 788-2233 and 234-2343
# find all phone numbers
phone_filter = re.compile(r'''(
                        (\d{3}(\s|-|\.)?|\(\d{3}\)(\s|-|\.)?)?  # area code + separator
                        (\d{3})             # 3 digits
                        (\s|-|\.)           # separator
                        (\d{4})             # 4 digits
                        )''', re.VERBOSE)

# i could save this as a GUI using tkintker
# then user could choose which list to save
# numbers = []
matches = []
for groups in phone_filter.findall(text):
    matches.append(groups[0])

if not matches:  # if empty list
    print('No phone numbers were found in the text :(')

num_numbers = len(matches)

# find all emails 
email_filter = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+   # username
                        @  # @ symbol
                        [a-zA-Z0-9.-]+  # domain
                        (\.[a-zA-Z]+)  # tld
                        (\.[a-zA-Z]+)?  # area domain
                        )''', re.I | re.VERBOSE)

for groups in email_filter.findall(text):
    matches.append(groups[0])

if len(matches) == num_numbers:
    print('No emails were found in the text :(')

matches = '\n'.join(matches)  # convert to string and join by new line
py.copy(matches.lower())  # convert to lower and copy to clipboard
print('Copied to clipboard:')
print(matches.lower())

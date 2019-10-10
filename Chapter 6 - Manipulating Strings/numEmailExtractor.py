#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import re
import pyperclip as py

# get the text off the clipboard
text = py.paste()

# regex magix 788-2233 and 234-2343
# find all phone numbers
phoneFilter = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?  # area code
                        (\s|-|\.)?          # separator
                        (\d{3})             # 3 digits
                        (\s|-|\.)           # separator
                        (\d{4})             # 4 digits
                        )''', re.VERBOSE)
phoneBuffer = phoneFilter.findall(text)
if phoneBuffer:
    print(phoneBuffer)
    # phoneList = ', '.join(phoneBuffer)
    # py.copy(phoneList) 
else:
    print('No phone numbers were found in the text :(')

# find all emails 
emailFilter = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+   # username
                        @  # @ symbol
                        [a-zA-Z0-9.-]+  # domain
                        (\.[a-zA-Z])  # tld
                        (\.[a-zA-Z])?  # area code
                        )''', re.I | re.VERBOSE)
emailsBuffer = emailFilter.findall(text)
if emailsBuffer:
    emailList = ', '.join(emailsBuffer)
    py.copy(emailList.lower())  # convert to lower and copy to clipboard
else:
    print('No emails were found in the text :(')



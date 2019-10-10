import re
import pyperclip as py

# get the text off the clipboard
text = py.paste()

# regex magix 788-2233 and 234-2343
# find all phone numbers
phoneFilter = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?  # area code
                        (\s|-)?
                        (\d{3})
                        (\s|-)
                        (\d{4})
                        )''', re.VERBOSE)
phoneBuffer = phoneFilter.findall(text)
if phoneBuffer:
    print(phoneBuffer)
    # phoneList = ', '.join(phoneBuffer)
    # py.copy(phoneList)
else:
    print('No phone numbers were found in the text :(')

# find all emails 
emailFilter = re.compile(r'\w+@\w+\.com', re.I)
emailsBuffer = emailFilter.findall(text)
if emailsBuffer:
    emailList = ', '.join(emailsBuffer)
    py.copy(emailList.lower())  # convert to lower and copy to clipboard
else:
    print('No emails were found in the text :(')



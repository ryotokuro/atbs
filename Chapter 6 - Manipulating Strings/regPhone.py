# regex
# \d\d\d-\d\d\d-\d\d\d\d
# is the same format as:
# \d{3}-\d{3}-\d{4}

import re  # import regex module

# r signals to use RAW strings (disregards the \)
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
string = 'My phone number is 941-436-7273!'
mo = phoneNumRegex.search(string)  # finds and creates match object
print('Phone number found: ' + mo.group())

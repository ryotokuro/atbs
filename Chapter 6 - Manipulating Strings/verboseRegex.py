# ignore spaces

import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # area code
    (\s|-|\.)? # separator
    \d{3} # first 3 digits
    (\s|-|\.) # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension
    )''', re.VERBOSE)

phone = phoneRegex.search('(132) 322-5358')
print(phone.group())

rapRegex = re.compile(r'''(
    (Mr\.\s\w+|Mrs\.\s\w+)  # title + optional space
    #(\w+)?  # name
    )''', re.VERBOSE)

rap = rapRegex.findall('Mr. Doubtfire and Mrs. Doubtfire')
print(rap[0])

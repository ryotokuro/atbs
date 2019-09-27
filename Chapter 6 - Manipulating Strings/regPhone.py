# regex
# \d\d\d-\d\d\d-\d\d\d\d
# is the same format as:
# \d{3}-\d{3}-\d{4}

import re  # import regex module

# r signals to use RAW strings (disregards the \)
phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})|\d{3}-\d{3}-\d{4}')
string = 'My phone number is (111) 111-1111 and 222-222-2222'
mo = phoneNumRegex.search(string)  # finds and creates match object
print(mo)
print('Area code found:', mo.group(1))
print('Phone number found:', mo.group(2))
print('Full number:', mo.group())

heroRegex = re.compile(r'Spiderman|Superman')
heroBase = heroRegex.findall('Spidermane vs. Superman')
print(heroBase[0], heroBase[1])

batRegex = re.compile(r'Bat(mobile|car|plane|signal|copter|man)')
batFind = batRegex.search('batman has a Batmobile and a batplan')
print(batFind.group())


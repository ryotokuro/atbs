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

# having different options |
heroRegex = re.compile(r'Spiderman|Superman')
heroBase = heroRegex.findall('Spidermane vs. Superman')
print(heroBase[0], heroBase[1])

# having multiple compound words (|)
batRegex = re.compile(r'Bat(mobile|car|plane|signal|copter|man)')
batFind = batRegex.search('batman has a Batmobile and a batplan')
print(batFind.group(), batFind.group(1))

# matching zero or one times ()?
batRegex = re.compile(r'Bat(wo)?man')
batFind = batRegex.search('Batman is a new man')
print(batFind.group())
batFind = batRegex.search('Batwoman is a new (wo)man')
print(batFind.group())

# matching zero or more times ()*
batRegex = re.compile(r'Bat(wo)*man')
batFind = batRegex.search('Batwowowowoman')
print(batFind.group())

# matching AT LEAST ONCE or MORE times ()+
batRegex = re.compile(r'Bat(MAN)+ loves')
batFind = batRegex.search('Bat loves pizza')
print(batFind)
batFind = batRegex.search('BatMAN loves pizza')
print(batFind.group())

# specific number of repeats
batRegex = re.compile(r'(na){8,24} batman!')
batFind = batRegex.search('nananananananananananananananananananananananana batman!')
print(batFind.group())

# non-greedy match
batRegex = re.compile(r'(na){8,24}?')
batFind = batRegex.search('nananananananananananananananana batman!')
print(batFind.group())

# findall() method
string = 'Home: (54) 4524-331 | Work: (61) 9342-100'
phoneRegex = re.compile(r'\(\d{2}\) \d{4}-\d{3}')
phoneFind = phoneRegex.findall(string)
print('Phone:', phoneFind[0], phoneFind[1])

string = 'Home: 9473-323 | Work: (61) 2344-234'
phoneRegex = re.compile(r'(\(\d{2}\))? (\d{4}-\d{3})')
phoneFind = phoneRegex.findall(string)
# print(phoneFind)
print('Phone:', *phoneFind[0], *phoneFind[1])

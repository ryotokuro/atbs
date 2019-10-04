import re

wildcard_match = re.compile(r'..l')
wildcard = wildcard_match.findall('There are all of the louder world is ours better hundred thousand like a safe hole my area looking like a bank code champagne popping options and caviar fishes and toxins this aint for the energisd like the drug money bunny')
print(wildcard)

# match all
nameRegex = re.compile('First Name: (.*) Last Name: (.*)')
names = nameRegex.search('First Name: Jesus Last Name: Christ')
print(names.group(1))
print(names.group(2))
print('It\'s Jason Bourne')

import re

consonantRegex = re.compile(r'[^aeiouAEIOU ]')
consonants = consonantRegex.findall('Note that inside the square brackets, the normal regular expressionsymbols are not interpreted as such')

print(consonants)

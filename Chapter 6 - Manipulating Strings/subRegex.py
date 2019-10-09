# substituting strings with the sub() method
import re

code_regex = re.compile(r'Agent \w+', re.I)
code_names = code_regex.sub('CENSORED', 'Agent John is reporting to AGENT Smith - the alpha virus of the Matrix.')
print(code_names)

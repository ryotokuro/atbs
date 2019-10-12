# substituting strings with the sub() method
import re

code_regex = re.compile(r'Agent \w+', re.I)
code_names = code_regex.sub('CENSORED', 'Agent John is reporting to AGENT Smith - the alpha virus of the Matrix.')
print(code_names)

code_regex = re.compile(r'Agent (\w)\w*')
code_names = code_names = code_regex.sub(r'\1***', 'The agent of secret stuff is actually Agent Ryan and Agent Arden')
print(code_names)

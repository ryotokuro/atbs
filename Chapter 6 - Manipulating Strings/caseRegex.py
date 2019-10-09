import re

no_case_regex = re.compile('Dragon Ball', re.I)  # ignores case sensitivity
no_case = no_case_regex.search('Naruto, DRAGON BALL, Bleach, One Piece')
print(no_case.group())

no_case = no_case_regex.search('Next time on Dragon Ball Z...')
print(no_case.group())

no_case = no_case_regex.search('We need to find the dragon balls!')
print(no_case.group())

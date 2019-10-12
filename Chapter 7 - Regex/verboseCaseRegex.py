import re

byeE = re.compile(r'''(
    [aeiou]
    )''', re.I | re.VERBOSE)

noE = byeE.sub(r'*', 'The dot-star will match everything except a newline.')
print(noE)

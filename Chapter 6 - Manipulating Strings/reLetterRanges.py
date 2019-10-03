import re

lettersRegex = re.compile(r'[a-zA-Z]')
letters_used = lettersRegex.findall('He// 0n 3arth @nd th3 c1ty\'5 on f1r3, in Hell, in Hell, there\'s Heaven!')

print(letters_used)

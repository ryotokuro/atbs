import re

# matches everything up till the new line
noNewLine = re.compile('.*')
text = noNewLine.search('There is no cake.\nIt is a lie.').group()
print(text)

print('%%%%%%%%%%%%%%%%%%')

# matching everything including new lines
literallyAll = re.compile('.*', re.DOTALL)
text = literallyAll.search('There is no cake.\nIt is a lie.').group()
print(text)

def commaCode(l):
    return ', '.join(l[:-1]) + ' and ' + l[-1]


spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaCode(spam))
spam = ['sasquatch', 'godzilla', 'king king', 'loch ness', 'goblin', 'ghoul', 'a zombie with no conscience']
print(commaCode(spam))
print('Question: What do all these things have in common?')

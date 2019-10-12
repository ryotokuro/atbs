import re

lettersRegex = re.compile(r'[a-zA-Z]')
# letters_used = lettersRegex.findall('He// 0n 3arth @nd th3 c1ty\'5 on f1r3, in Hell, in Hell, there\'s Heaven!')
plaintext = input("Enter something: ").upper()
letters_used = lettersRegex.findall(plaintext)

letters_dict = {}
for i in letters_used:
    if i not in letters_dict:
        letters_dict[i] = 1
    else:
        letters_dict[i] += 1

print('Letter Frequencies')
print('-'*len('Letter Frequencies'))
# letters_dict = sorted(letters_dict, key=lambda item: item[1])
for k, v in letters_dict.items():
    print(k + ':', v)

# print(letters_dict.keys())
for i in plaintext:
    #if i in [*letters_dict.keys()]:
    if i in letters_used:
        print('_', end=' ')
    else:
        print(i, end='')

# now i want to display the letters beneath the underscores like a sub cipher game

# then i want implementation to enable guessing :)
# while not_guessed:

    

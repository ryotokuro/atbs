def separatedList(spam):
    print(spam)
    string = ''
    for i in range(len(spam)):
        if i == len(spam)-1:
            string += 'and ' + spam[i]
        else:
            string += spam[i] + ', '
    return string


spam = ['apples', 'bananas', 'tofu', 'cats']
print(separatedList(spam))

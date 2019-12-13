import os
import re

text = open('lib.txt')
contents = text.read()
# count occurences
words = re.split('\s|,\s|\.|\.\s|\n', contents)
for word in words:
    if word == 'NOUN':
        new_word = input("Enter a noun: ")
        contents = contents.replace("NOUN", new_word, 1)
        
    elif word == 'ADJECTIVE':
        new_word = input("Enter a adjective: ")
        contents = contents.replace("ADJECTIVE", new_word, 1)
        
    elif word == 'VERB':
        new_word = input("Enter a verb:")
        contents = contents.replace("VERB", new_word, 1)

# need to ask for input in order anyway, so it's useless
# num_nouns = contents.count('NOUN')
# num_adj = contents.count('ADJECTIVE')
# num_verbs = contents.count('VERB')
# print(num_nouns, num_adj, num_verbs)

print(contents)

import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowels = vowelRegex.findall('There is no love in the GUITAR.')

vowel_dict = {}

for i in vowels:
    if i not in vowel_dict:
        vowel_dict[i] = 1
    else:
        vowel_dict[i] += 1

for k, v in vowel_dict.items():
    print(k + ":", v)

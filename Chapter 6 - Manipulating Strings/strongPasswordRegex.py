#! python3
# strongPasswordRegex.py - checks if you meet the minimum password standard

import re
import pyperclip as py

password = py.paste()

# at least 8 characters long
if len(password) >= 8:
    # contains uppercase
    upper_filter = re.compile(r'[A-Z]')
    if upper_filter.findall(password):  # if there is a uppercase letter
        # contains lowercase
        lower_filter = re.compile(r'[a-z]')
        if lower_filter.findall(password):
            # has at least 1 digit
            digit_filter = re.compile(r'\d')
            if digit_filter.findall(password):
                print("Awesome, your password passes all the tests!")
            else:
                print("Y0ur p455w0rd d035n't h4v3 4 d1g1t")
        else:
            print("you are missing a lowercase letter!")
    else:
        print("YOU DON'T HAVE AN UPPERCASE LETTER!")
else:
    print("Password is not long enough!")



def isPhoneNumber(text):
    print(text + ' is a phone number:', end=' ')
    
    # format XXX-XXX-XXXX
    return len(text) == 12 and (text[:3] + text[4:7] + text[8:]).isdecimal() and text[3] == text[7] == '-'


print(isPhoneNumber('415-555-4242'))
print(isPhoneNumber('Moshi moshi'))
print(isPhoneNumber('000-000-00001'))

def isPhoneNumber(text):
    # format XXX-XXX-XXXX
    if len(text) != 12:
        return False
    
    return (text[:3] + text[4:7] + text[8:]).isdecimal() and text[3] == text[7] == '-'


print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

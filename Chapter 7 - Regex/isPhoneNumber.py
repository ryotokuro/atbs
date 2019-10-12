def isPhoneNumber(text):
    # print(text + ' is a phone number:', end=' ')
    
    # format XXX-XXX-XXXX
    return len(text) == 12 and (text[:3] + text[4:7] + text[8:]).isdecimal() and text[3] == text[7] == '-'

def findNumber(message):
    found = False
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found:', chunk)
            found = True
    if not found:
        print('No phone number found.')
    print('Done.')

# print(isPhoneNumber('415-555-4242'))
# print(isPhoneNumber('Moshi moshi'))
# print(isPhoneNumber('000-000-00001'))
findNumber('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
findNumber('Here\'s my number: 315-643-283')

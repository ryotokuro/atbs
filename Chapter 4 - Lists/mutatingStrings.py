originalString = 'The cake is real.'

location = originalString.find('s')
print(location)  # printing just to make sure it works

mutatedString = originalString[:location+2] + 'a lie.'

print(mutatedString)

# Alternatively
originalString = 'The cake is not a lie.'

mutatedString = originalString[:originalString.find('s+2')] + originalString[originalString.find('a'):]

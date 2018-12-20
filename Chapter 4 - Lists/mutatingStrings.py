originalString = 'The cake is real.'

location = originalString.find('s')
print(location)  # printing just to make sure it works

mutatedString = originalString[:location+2] + 'a lie.'

print(mutatedString)

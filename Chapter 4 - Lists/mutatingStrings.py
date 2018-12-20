originalString = 'The cake is real.'

location = originalString.find('s')
print(location)  # printing just to make sure it works

mutatedString = originalString[:location]
mutatedString.append(' is a lie.')

print(mutatedString)

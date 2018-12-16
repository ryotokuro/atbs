# Methods: same as functions but are "called on" a value
# i.e. spam.index('hello') where index() is the method

spam = ['hello', 'hi', 'howdy', 'heya']
print("Index of 'hello' string is:", spam.index('hello'))

print("Index of 'heya' string is:", spam.index('heya'))

try:
    print("Index of 'howdy howdy howdy' string is:", spam.index('howdy howdy howdy') )

except ValueError:
    print('Error: Invalid argument. String not found inside list.')

# In the case of dduplicates returns the FIRST instance
duplicates = ['cat', 'dog', 'cow', 'cat', 'girl', 'cow']

print("Index of 'cat':", duplicates.index('cat'))

print("Index of 'cow':", duplicates.index('cow'))

# Adding values to the list
newEntry = str(input('Enter a desired string to be INSERTED anywhere into the list: '))
spam.insert(2, newEntry)
print(spam)

newEntry = str('Enter a desired string to be APPENDED onto the list:')
spam.append(newEntry)
print(spam)

# Removing values from a list
removeEntry = str(input('Enter a string you wish to remove from the list: '))
spam.remove(removeEntry)
print(spam)

removeEntry = str(input('Enter an invalid string to remove from the list: '))
try:
    spam.remove(removeEntry)

except ValueError:
    print('Error: String not found in list. Can not be removed if it does not exist.')

# Sorting Values
numbers = [1, 642, 42, -32, 21, 24, 73, 9116, 324]
print(numbers)
print(numbers.sort())
print(numbers.sort(reverse=True))

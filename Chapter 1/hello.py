# Greetings from stdout
print('Hello World!')

# Receive name from input() and store
myName = input('What is your name? ')

# Note: myName is a STRING
print('It is good to meet you, ' + myName)

# Uses len() function
print('The length of your name is:')
print(len(myName))

print('What is your age?')
myAge = input() # receives a STRING

# since myAge is a string:
# 1. convert->int before adding
# 2. convert->str before printing
print('In one year, you will be', str(int(myAge)+1), 'years old.')

# Greetings from stdout
print('Hello World!')

# Receive name from input() and store
myName = None
while not(isinstance(myName, str)):  # while myName is NOT a string, keep asking
    try:
        myName = str(input('What is your name? '))

    except ValueError:
        print('Enter your real name!')

# Note: myName is a STRING
print('It is good to meet you, ' + myName)

# Uses len() function
print('The length of your name is:')
print(len(myName))

myAge = None
while not(isinstance(myAge, int)):  # while myAge is NOT an integer, keep asking
    try:
        print('What is your age?')
        myAge = int(input())  # receives a STRING

    except ValueError:
        print("Invalid input. That isn't a number!")
        # myAge = input('Enter your real age please: ')
        # while isinstance(myAge, int) is False:
            # print(isinstance(myAge, int))

# since myAge is a string:
# 1. convert->int before adding
# 2. convert->str before printing
print('In one year, you will be', str(int(myAge)+1), 'years old.')

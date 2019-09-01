birthdays = {'Alice':'Apr 1', 'Bob':'Dec 12', 'Carol':'Mar 4'}

while True:
    name = input('Enter a name (nothing to quit): ')

    if not name:
        break
    
    try:
        print(birthdays[name])
    except KeyError:
        print('I do not have birthday information on', name)
        print('Would you like to update the database with their information (yes/no)?')
        answer = input()
        if answer.lower() == 'yes':
            birthday = input('What is their birthday: ')
            birthdays[name] = birthday
        else:
            print('Okay then :(')

print('Shutting down...')
print('Goodbye.')

name = input('Enter your name: ')

age = None
while not(isinstance(age, int)):
	try:
		age = int(input('Enter your age: '))
		
	except ValueError:
		print('Invalid input. Please try again.')
		
if name == "Alice":
	print('Hi, Alice :)')

elif age < 12:
	print('You are NOT Alice, kiddo >:(')

else:
	print('Who are you?')
	
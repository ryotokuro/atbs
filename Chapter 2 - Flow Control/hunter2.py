while True:
	name = input('Enter your name: ')
	
	if name != 'Tai':
		print('Invalid user.')
		continue
	
	while True:
		password = input('Hello Tai, please enter the password: ')
		
		if password == 'hunter2':
			break
			
		else:
			print('Incorrect password. Try again.')
	break
		
print('Access granted.')

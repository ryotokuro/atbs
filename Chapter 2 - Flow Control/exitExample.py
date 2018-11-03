import sys

while True:
	response = input('Type "exit" to exit the program\n')
	if response == 'exit':
		sys.exit()
		
	print(response, 'is not a registered command.')
	
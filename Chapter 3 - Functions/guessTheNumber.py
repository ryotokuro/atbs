def guessTheNumber():
	print('I am thinking of a number between 1 and 20. \n Take a guess.')

	number = 12
	while input() != number:
		if input() < number:
			print('Your guess is too low.')
		if input() > number:
			print('Your guess is too high.')
			
import random

number = random.randint(1, 20)

print('I am thinking of a number between 1 and 20. \n Take a guess.')

guess = int(input())
while guess != number:
	if guess < number:
		print('Your guess is too low.')
	else: # guess is bigger than the number
		print('Your guess is too high.')

	guess = int(input('Take a guess.'))

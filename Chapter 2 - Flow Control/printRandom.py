import random as r

x = list()
y = list()

for i in range(5):
	x.append(r.randint(1,5))
	y.append(r.randint(1,5))
	
print("Shoot if row =", x, "and col =", y)

for row in range(1,6):
	for col in range(1,6):
		if row == x[row-1] and col == y[col-1]:
			print('O', end="    ")
		else:
			print('X', end="    ")
	
	print('\n')
print(x[row-1], y[col-1])
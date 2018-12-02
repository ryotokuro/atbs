def collatz():
    if number % 2 == 0:
        # number is even
        return number // 2

    else:
        # number is odd
        return 3 * (number+1)

print(collatz)

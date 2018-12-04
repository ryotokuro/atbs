def collatz(number):
    if number % 2 == 0:
        # number is even
        return number // 2

    else:
        # number is odd
        return 3 * number + 1


# MAIN
number = None

while number is None:
    try:
        number = int(input())

    except ValueError:
        print("Please enter an integer.")

while number != 1:
    number = collatz(number)
    print(number)

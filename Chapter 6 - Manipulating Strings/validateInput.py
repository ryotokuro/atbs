while True:
    age = input("Enter your age: ")
    if age.isdecimal():
        break
    print("Please enter a number for your age")

while True:
    password = input("Select a new passwords (letters and numbers only): ")
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers")

print("Nice! That's perfectly valid thank you.")

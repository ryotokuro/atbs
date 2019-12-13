import re
import os

# navigate to cwd / specified folder
path = os.path.abspath('.')
while True:
    cwd = "Current directory: " + path
    print(cwd)
    print('-'*len(cwd))
    print("1. back - moves back down one level")
    print("2. move <folder name> - moves forward to specified folder")
    print("3. confirm - selects current directory to search in")
    command = input("Enter command: ")

    if command == "confirm":
        break
    elif command == "back":
        path = os.path.abspath(path + '\..')
    elif command == "move":
        break
    else:
        print("Invalid command. Try again.")
        

# search for .txt files in the directory


term = input("Enter a regular expression to search for: ")

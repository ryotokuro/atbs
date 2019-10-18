import os

# os.path.exists(path)
paths = ["C:\\", "C:\\Windows\\PogChamp", "C:\\Windows\\Diagtrack"]
for path in paths:
    print(path, ": ", os.path.exists(path), sep='')

print("\n===========\n")

# os.path.isdir(path) and os.path.isfile(file)
# note you can see it's not case-sensitive!
query = ["c:\\", "C:\\Users\\autum\\Downloads", "C:\\Users\\autum\\Downloads\\2017.pdf", "D:\\"]
for q in query:
    if os.path.isdir(q):
        print(q, "is a directory!")
    elif os.path.isfile(q):
        print(q, "is a file!")
    else:
        print("Requested file/directory does not exist!")

# D:\\ tells you that a flash drive is connected!

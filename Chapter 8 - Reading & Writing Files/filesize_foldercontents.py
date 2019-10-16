import os

# getsize() - returns size of file in bytes
print("C:\\Windows\\System32\\calc.exe:", os.path.getsize("C:\\Windows\\System32\\calc.exe"), "bytes", end="\n\n")
print(os.path.abspath("filesize_foldercontents.py") + ":", os.path.getsize(".\\filesize_foldercontents.py"), "bytes", end="\n\n")

# os.listdir(arg) - returns files in the path
print(os.listdir(), end="\n\n")
print(os.listdir("..\..\..\.."), end="\n\n")

# combining getsize() and listdir to get size of directory files
size = 0
for file in os.listdir():
    size += os.path.getsize(file)

print(os.path.abspath("") + ":", size)

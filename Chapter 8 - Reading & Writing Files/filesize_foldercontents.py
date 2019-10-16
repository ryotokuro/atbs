import os

# getsize() - returns size of file in bytes
print("C:\\Windows\\System32\\calc.exe:", os.path.getsize("C:\\Windows\\System32\\calc.exe"), "bytes", end="\n\n")
print(os.path.abspath("filesize_foldercontents.py") + ":", os.path.getsize(".\\filesize_foldercontents.py"), "bytes", end="\n\n")

# os.listdir(arg) - returns files in the path
print(os.listdir(), end="\n\n")
print(os.listdir("..\..\..\.."), end="\n\n")

# combining getsize() and listdir to get size of directory files
size = 0
for file in os.listdir(".."):  # use join to get size of full file?
    size += os.path.getsize(os.path.join(os.path.abspath(".."), file))
    print(os.path.join(os.path.abspath(".."), file))

print("Size:", size)

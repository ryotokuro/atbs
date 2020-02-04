import os

for folderName, subFolders, fileNames in os.walk("..\\.."):
    if ".git" in folderName:
        continue
    print(folderName)

    for folder in subFolders:
        print("folder:", folder)
        
    for file in fileNames:
        print("file:", file)

    print()  # split walk into sections

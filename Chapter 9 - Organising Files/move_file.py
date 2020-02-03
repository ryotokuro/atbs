import shutil, os

os.chdir("C:\\Users\\autum\\OneDrive\\Documents")
try:
    shutil.move(".\\spam.txt", ".\\Notes")
except shutil.Error:
    print("File already exists, moving file under a different name")
    shutil.move(".\\spam.txt", ".\\Notes\\spam1.txt")

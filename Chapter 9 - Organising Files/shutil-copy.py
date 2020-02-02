import shutil, os

os.chdir("C:\\Users\\autum\\OneDrive\\Documents")
print(os.getcwd())
shutil.copy(".\\spam.txt", ".\\Notes")

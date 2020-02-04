import shutil, os

# !!! TEST FIRST !!!
# Note: These are PERMANENT deletes (not recycle bin)

# OS
# 1. delete the file at path
# os.unlink(path)

# 2. delete folder at path
# os.rmdir(path)

# SHUTIL
# 1. remove folder and children
# shutil.rmtree(path)


# prints files that would be deleted
os.chdir("..\\..\\Notes")
for file in os.listdir():
    if file.endswith(".txt"):
        print("Delete:", file)

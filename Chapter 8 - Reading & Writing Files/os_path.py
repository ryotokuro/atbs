import os

# adjusts depending on what OS the script is running on
raw_path = 'C:\\Users\\autum\\Desktop\\Pizza'

# path = os.path.join(raw_path) for os dependent config

# printing path script is running from
print("Before:", os.getcwd())

# attempt to navigate to path
try:
    os.chdir(raw_path)
    print("After:", os.getcwd())
except FileNotFoundError:  # if it doesn't exist
    print("Let's try create the directory then!")
    

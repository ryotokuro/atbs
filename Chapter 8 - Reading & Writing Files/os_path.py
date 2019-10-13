import os

# adjusts depending on what OS the script is running on
raw_path = 'C:\\Users\\autum\\Desktop\\Pizza'
# raw_path = '..\\..'  # navigating backwards (relative)

# path = os.path.join(raw_path) for os dependent config

# printing path script is running from
print("Before:", os.getcwd())

# attempt to navigate to path
try:
    os.chdir(raw_path)
    print("After:", os.getcwd())
except FileNotFoundError:  # if it doesn't exist
    print("Directory does not exist. Creating directory...")
    os.makedirs(raw_path)
    os.chdir(raw_path)
    print(os.getcwd())

#os.chdir('atbs')
#print(os.getcwd())
#os.makedirs('.\\Pizza')

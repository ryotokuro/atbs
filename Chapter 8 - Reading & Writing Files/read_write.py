# open file to get a file object
text_file = open(".\\hello.txt")
print("before:", text_file.read())

# specify I want to open the file in "read" (r) mode
new_file = open("C:\\Users\\autum\\OneDrive\\Documents\\atbs\\Chapter 8 - Reading & Writing Files\\cheese.txt", 'r')
l = new_file.read().split('\n')
print(l)

# overwrite file content write()
file = ".\\hello.txt"
if open(file, 'r') == "hello": # first read the contents
    text_file = open(".\\hello.txt", 'w')  # open as writeable file
    text_file.write("goodbye")
else:
    text_file = open(".\\hello.txt", 'w')  # open as writeable file
    text_file.write("hello")
    
text_file = open(".\\hello.txt", 'r')  # then open in read mode
print("after:", text_file.read())

doesnt_exist = open(".\\ghost.txt", 'w')
doesnt_exist.write("SPOOOOKY")

doesnt_exist = open(".\\ghost.txt", 'r')
print(doesnt_exist.read())

# append mode, pass 'a'
doesnt_exit = open(".\\hello.txt"

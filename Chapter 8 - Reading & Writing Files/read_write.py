# open file to get a file object
text_file = open(".\\hello.txt")
print(text_file.read())

# specify I want to open the file in "read" (r) mode
new_file = open("C:\\Users\\autum\\OneDrive\\Documents\\atbs\\Chapter 8 - Reading & Writing Files\\cheese.txt", 'r')
l = new_file.read().split('\n')
print(l)

# overwrite file content write()
file = ".\\hello.txt"
text_file = open(file, 'r')  # then open in read mode
initial_content = 
text_file = open(".\\hello.txt", 'w')  # open as writeable file
text_file.write("hello")
text_file = open(".\\hello.txt", 'r')  # then open in read mode
okay = text_file.read()
print(okay)

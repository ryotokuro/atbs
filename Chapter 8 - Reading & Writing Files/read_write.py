# open file to get a file object
text_file = open(".\\hello.txt")
print(text_file.read())

# specify I want to open the file in "read" (r) mode
new_file = open("C:\\Users\\autum\\OneDrive\\Documents\\atbs\\Chapter 8 - Reading & Writing Files\\cheese.txt", 'r')
l = new_file.read().split('\n')
print(l)

import shelve

shelfFile = shelve.open('mydata')
print(type(shelfFile))  # check type of file

print(shelfFile['cats'])  # call list of cats using key
shelfFile.close()

import zipfile, os

# create zip file object
exampleZip = zipfile.ZipFile('example.zip')

# print files within zip file
# print(exampleZip.namelist())

# obtain information about a certain file
# fileInfo = exampleZip.getinfo('__MACOSX/Twitter Social Icons/._Twitter_Brand_Guidelines_V2.0.pdf')
# print("Compressed file is %sx smaller!" % (round(fileInfo.file_size / fileInfo.compress_size, 2)))

# print information about all the files inside the zip
for i in exampleZip.namelist():
    fileInfo = exampleZip.getinfo(i)
    try:
        print("Compressed file [", i[-16:], "] is %sx smaller!" % (round(fileInfo.file_size / fileInfo.compress_size, 2)))
    except ZeroDivisionError:
        pass

exampleZip.close()

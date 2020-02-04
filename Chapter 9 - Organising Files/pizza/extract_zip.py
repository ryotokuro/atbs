import zipfile, os

exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()

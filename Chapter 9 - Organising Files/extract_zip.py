import zipfile, os

# if zip file is in another directory
# os.chdir('.\\data')

# first create a zipfile object
exampleZip = zipfile.ZipFile('example.zip')

print("available files:", exampleZip.namelist())

# extract in working directory
# exampleZip.extractall()

# extract in another directory
exampleZip.extractall('.\\pizza')

# extract a single file
# exampleZip.extract('extract_zip.py', '.\\pizza')

exampleZip.close()

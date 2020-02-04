import zipfile, os

# opens in write mode to create a NEW zip (overwrites!)
newZip = zipfile.ZipFile('new.zip', 'w')

# opens in append mode to add to existing zips
# newZip = zipfile.ZipFile('new.zip', 'a')

# adds file in with specified compression type
# newZip.write('create_zip.py', compress_type=zipfile.ZIP_DEFLATED)
newZip.write('copy_file.py', compress_type=zipfile.ZIP_DEFLATED)

newZip.close()

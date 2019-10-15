import os

# abspath()
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))

# isabs()
print("Absolute ?:", os.path.isabs('.'))
print("Absolute ?:", os.path.isabs(os.path.abspath('.')))

# relpath()
print(os.path.relpath('.'))
print(os.path.relpath('C:\\', os.getcwd()))
print(os.path.relpath('C:\\Users\\autum\\My Documents\\Python', os.getcwd()))

# basename()
path = os.path.abspath('.')
print(os.path.basename(path))

# dirname()
print(os.path.dirname(path))

# os.split()
print(os.path.split(path))

# same by combining basename() and dirname()
print((os.path.dirname(path), os.path.basename(path)))

# split
print(path.split(os.path.sep))

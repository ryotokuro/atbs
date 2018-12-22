tuple = ('hello', 42, 0.5)

try:
    tuple[1] = 'bye'

except TypeError:
    print('Error: tuples cannot be mutated.')
    
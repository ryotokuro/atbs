# Write a function named printTable() that:
# - takes a list of lists of strings
# - and displays it in a well-organized table with each column right-justified.
# Assume that all the inner lists will contain the same number of strings.

# EXAMPLE
# tableData = [['apples', 'oranges', 'cherries', 'banana'],
#               ['Alice', 'Bob', 'Carol', 'David'],
#               ['dogs', 'cats', 'moose', 'goose']]

# OUTPUT
#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose

import itertools as it

def printTable(table):
    lengths = {}  # stores lengths per column
    index = 0
    for col in table:
        lengths[index] = len(max(col, key=len))
        index += 1  # tracks the column number for the hashmap
    # print(lengths)
    
    table = list(zip(*reversed(table[::-1])))  # flip table for printing
    # print the 2d array
    for item in table:
        col = 0
        for inner in item:  # adding largest column spacing
            print(inner.rjust(lengths[col], ' '), end=' ')
            col += 1
        print()

printTable([['apples', 'oranges', 'cherries', 'banana'],
                    ['Alice', 'Bob', 'Carol', 'David'],
                    ['dogs', 'cats', 'moose', 'goose']])
print()
printTable([['maximumvoltage', 'shahkhan', 'zerolimiT'],
                    ['carrots', 'carricatures', 'superman'],
                    ['zezima', 'goku', 'vegeta']])

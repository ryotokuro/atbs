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
    table = list(zip(*reversed(table[::-1])))
    temp = list(zip(*reversed(table[::-1])))

    lengths = {}
    index = 0
    for col in temp:
        lengths[index] = len(max(col, key=len))
        index += 1
    # print(lengths)
        
    for item in table:
        col = 0
        for inner in item:
            print(inner.rjust(lengths[col], ' '), end=' ')
            col += 1
        print()

printTable([['apples', 'oranges', 'cherries', 'banana'],
                    ['Alice', 'Bob', 'Carol', 'David'],
                    ['dogs', 'cats', 'moose', 'goose']])

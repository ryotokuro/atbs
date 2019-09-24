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

def printTable(table):
    length = 0
    for item in table:
        for inner in item:
            length = max(length, len(inner))
    print(length)

    for item in table:
        for inner in item:
            print(inner.rjust(length, ' '), end=' ')
        print()

print(printTable([['apples', 'oranges', 'cherries', 'banana'],
                    ['Alice', 'Bob', 'Carol', 'David'],
                    ['dogs', 'cats', 'moose', 'goose']]))

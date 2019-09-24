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
    table = list(zip(*reversed(table[::-1])))
    # print(table)

    for item in table:
        length = len(max(item, key=len))
        print(length)
        for inner in item:
            print(inner.rjust(length, ' '), end=' ')

print(printTable([['apples', 'oranges', 'cherries', 'banana'],
                    ['Alice', 'Bob', 'Carol', 'David'],
                    ['dogs', 'cats', 'moose', 'goose']]))

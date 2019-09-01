grid =  [['.', '.', '.', '.', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['.', 'O', 'O', 'O', 'O', 'O'],
         ['O', 'O', 'O', 'O', 'O', '.'],
         ['O', 'O', 'O', 'O', '.', '.'],
         ['.', 'O', 'O', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.']]

# reversed first flips the sublist order
# then * unwraps each of the lists, such that zip only takes the first column of each sublist
# and zip then combines them into their own sublists so now it is rotated!
grid = zip(*reversed(grid))

for i in grid:
    for j in i:
        print(j, end=' ')
    print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# grid[x][y] are the x and y coordinates of the 2d grid drawn
# [0][0] is the origin
# need to print:
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

for y in range(len(grid)):
    for x in range(len(grid)):
        print(grid[x][y])


if x == 0 or x == len(grid):
    grid[x] = '.'

elif y == 1:
    grid[x] = 'o'

elif y == len(grid):
    print('no')

# note: 2 is same as 1

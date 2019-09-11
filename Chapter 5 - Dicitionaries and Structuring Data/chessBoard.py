import pprint
board = [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
         ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
         ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
         ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
         ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
         ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
         ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
         ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]

print('-'*41)
for y in board:
    print('| ', end='')
    for x in y:
        print(x, '|', end=' ')
    print('','-'*41,sep='\n')

player_black = {'BK': 1, 'BQ': 1, 'BB': 2, 'BN': 2, 'BR' : 2, 'BP': 8}
player_white = {'WK': 1, 'WQ': 1, 'WB': 2, 'WN': 2, 'WR' : 2, 'WP': 8}

play = [['BR', 'BN', 'BB', 'BK', 'BQ', 'BB', 'BN', 'BR'],
        ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
        ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
        ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
        ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
        ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
        ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
        ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'wR']]

print('-'*41)
for y in play:
    print('| ', end='')
    for x in y:
        print(x, '|', end=' ')
    print('','-'*41,sep='\n')

# define a moveset
# pawns can move up or attack diag
# blk pawns: move (same col -1), attack (different col -1)

#while 'K' in player_black and 'K' in player_white:
    

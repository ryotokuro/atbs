import pprint

def printBoard(board):
    print(' ', end='')
    for k, v in board.items():
        if k[-1] == 'R':
            if v == ' ':
                print(k)
            else:
                print(v)
                
            if k[0] != 'B':
                print('-'*4+'+'+'-'*4+'+'+'-'*4)
                print(' ', end='')
        else:
            if v == ' ':
                print(k, '|', end=' ')
            else:
                print('', v, '|', end=' ')
            

board = {'TL' : ' ', 'TM' : ' ', 'TR' : ' ',
         'ML' : ' ', 'MM' : ' ', 'MR' : ' ',
         'BL' : ' ', 'BM' : ' ', 'BR' : ' '}

start = input('Choose a starting piece (O/X): ')
if start.lower() == 'x':
    x = True
else:
    x = False

while True:
    printBoard(board)
    pos = input('Enter position to play : ').upper()
    if x:
        board[pos] = 'X'
    else:
        board[pos] = 'O'
    x = not x

    # win conditions
    if board['TL'] == board['TM'] == board['TR'] or board['TL'] == board['ML'] == board['BL'] or board['TL'] == board['MM'] == board['BR']:
        winner = board['TL']
        break

printBoard(board)    
print('Congratulations,', winner, 'won!')

from service import make_move

board = ' x       '
while True:
    print('Computer plays: <{0}>'.format(make_move(board)))
    board = input('Type your move: ')
from validity import BoardLengthCheck, BoardCharacterCheck, GameUnfinishedCheck, ValidNaughtsMoveCheck, \
    ValidBoardCheck, GameAlreadyWonCheck
from strategy import FindNaughtsWin, FindCrossesWin, FindFirstDefense, FindCentreMove, FindCornerMove, FindAnyMove
from game import TicTacToeGame
from flask import Flask, request

validations = [
    BoardLengthCheck(),
    BoardCharacterCheck(), 
    GameUnfinishedCheck(), 
    ValidNaughtsMoveCheck(),
    ValidBoardCheck(),
    GameAlreadyWonCheck()
]

strategies = [
    FindNaughtsWin(),
    FindCrossesWin(),
    FindFirstDefense(),
    FindCentreMove(),
    FindCornerMove(),
    FindAnyMove()
]

def get_response(board):
        
    # Validate the board - raise an exception if the board is not valid
    for validation in validations:
        if not validation.validate(board):
            raise ValueError("Validation checked failed during request: {0}".format(validation.check_description()))
        
    # Create a "game" and loop the strategies
    game = TicTacToeGame(board)
    for strategy in strategies:
        move = strategy.get_move(game)
        if move is not None:
            index = move[0] * 3 + move[1]
            return board[:index] + TicTacToeGame.NAUGHTS + board[index + 1:]
        
    # There is an error with the board we have not yet noticed/ understand
    raise ValueError('Unspecified error with the board (no available moves)')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def play():
    board = request.args.get('board')
    if board is None or len(board.strip()) == 0:
        return 'The URL parameter -board- is required', 400
    
    try:
        revised_board = get_response(board)
        return revised_board, 200
    except Exception as e:
        return str(e), 400

@app.errorhandler(500)
def all_exception_handler(error):
    return 'Malformed URL', 404

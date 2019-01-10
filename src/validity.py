from game import TicTacToeGame
from abc import ABC, abstractmethod
import collections

class IValidityCheck(ABC):
    
    @abstractmethod
    def check_description(self):
        pass
    
    @abstractmethod
    def validate(self, board:str) -> bool:
        pass
    
class BoardLengthCheck(IValidityCheck):
    
    def check_description(self):
        return 'The board in the request is the correct number of characters'
    
    def validate(self, board: str) -> bool:
        return len(board) == 9
    
class BoardCharacterCheck(IValidityCheck):
    
    def check_description(self):
        return 'The board in the request is made up of valid characters'
    
    def validate(self, board: str) -> bool:
        return len([b for b in board.lower() if b not in TicTacToeGame.VALID_CHARACTERS]) == 0
    
class GameUnfinishedCheck(IValidityCheck):
    
    def check_description(self):
        return 'The board in the request is not a completed game'
    
    def validate(self, board: str) -> bool:
        return len([b for b in board.lower() if b == TicTacToeGame.EMPTY]) > 0
    
class ValidNaughtsMoveCheck(IValidityCheck):
    
    def check_description(self):
        return 'The board in the request is in a valid state for naughts to move'
    
    def validate(self, board: str) -> bool:
        counter = collections.Counter(board)
        return counter[TicTacToeGame.NAUGHTS] <= counter[TicTacToeGame.CROSSES]
    
class ValidBoardCheck(IValidityCheck):
    
    def check_description(self):
        return 'The board is in a valid state (there are the correct number of turns for each player)'
    
    def validate(self, board: str) -> bool:
        counter = collections.Counter(board)
        return abs(counter['o'] - counter['x']) < 2
    
class GameAlreadyWonCheck(IValidityCheck):
    
    def check_description(self):
        return 'The board in the request does not have a winner'
    
    def validate(self, board: str) -> bool:
        game = TicTacToeGame(board)
        return not game.has_winner()

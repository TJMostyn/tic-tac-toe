from abc import ABC, abstractmethod
from game import TicTacToeGame

class StrategyRule(ABC):
    
    @abstractmethod
    def get_move(self, game:TicTacToeGame) -> tuple:
        pass
    
class FindNaughtsWin(StrategyRule):
    
    def get_move(self, game:TicTacToeGame) -> tuple:
        winning_moves = game.get_winning_positions(TicTacToeGame.NAUGHTS)
        if len(winning_moves) > 0:
            return winning_moves[0]
        return None
    
class FindCrossesWin(StrategyRule):
    
    def get_move(self, game:TicTacToeGame) -> tuple:
        winning_moves = game.get_winning_positions(TicTacToeGame.CROSSES)
        if len(winning_moves) > 0:
            return winning_moves[0]
        return None
    
class FindFirstDefense(StrategyRule):
    
    def get_move(self, game:TicTacToeGame) -> tuple:
        crosses_moves = game.get_all_moves(TicTacToeGame.CROSSES)
        if len(crosses_moves) == 1 and crosses_moves[0] in TicTacToeGame.CORNERS:
            for corner in TicTacToeGame.CORNERS:
                if game.is_position_empty(corner[0], corner[1]):
                    return corner
        return None

class FindCentreMove(StrategyRule):
    
    def get_move(self, game:TicTacToeGame) -> tuple:
        if game.is_position_empty(1, 1):
            return (1, 1)
        return None

class FindCornerMove(StrategyRule):
    
    def get_move(self, game:TicTacToeGame) -> tuple:
        for corner in game.CORNERS:
            if game.is_position_empty(corner[0], corner[1]):
                return corner
        return None

class FindAnyMove(StrategyRule):
    
    def get_move(self, game:TicTacToeGame) -> tuple:
        moves = game.get_all_moves(TicTacToeGame.EMPTY)
        if len(moves) > 0:
            return moves[0]
        return None
        
        
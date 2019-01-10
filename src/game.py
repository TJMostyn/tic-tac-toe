import numpy as np
import collections

class TicTacToeGame:
    
    CORNERS = [(0, 0), (0, 2), (2, 0), (2, 2)]
    CENTRE = (1, 1)
    NAUGHTS = 'o'
    CROSSES = 'x'
    EMPTY = ' '
    VALID_CHARACTERS = [NAUGHTS, CROSSES, EMPTY]
    
    def __init__(self, board:str):
        self._board = board
        self._mboard = self._convert_to_matrix(board)
        rows = self._mboard
        columns = np.rot90(self._mboard)
        diagonals = np.append(np.diagonal(rows), np.diagonal(columns)).reshape(2, 3)
        self._flattened_board = np.concatenate([rows, columns, diagonals]).reshape(8, 3)
    
    def has_winner(self) -> bool:
        for row in self._flattened_board:
            if len(set(row)) == 1 and row[0] != self.EMPTY:
                return True
        return False
    
    def get_winning_positions(self, player_char:str) -> list:
        if player_char not in [self.NAUGHTS, self.CROSSES]:
            raise ValueError('Invalid board character')
        
        winning_positions = []
        for i in range(len(self._flattened_board)):
            counts = collections.Counter(self._flattened_board[i])
            if counts[player_char] == 2 and counts[self.EMPTY] == 1:
                empty_char_index = list(self._flattened_board[i]).index(self.EMPTY)
                
                # Because we have flattened the matrix into possibilities, we have to calculate the position
                # after the first 3 rows (because 4-6 are columns and 7-8 diagonals
                if i <= 2:
                    winning_positions.append((i, empty_char_index))
                elif i <= 5:
                    winning_positions.append((empty_char_index, (i - 5) * -1))
                elif i == 6:
                    winning_positions.append((empty_char_index, empty_char_index))
                elif i == 7:
                    winning_positions.append((empty_char_index, (empty_char_index - 2) * -1))
                    
        return winning_positions
    
    def get_all_moves(self, player_char:str) -> list:
        moves = []
        for i in range(len(self._mboard)):
            for j in range(len(self._mboard[i])):
                if self._mboard[i][j] == player_char:
                    moves.append((i, j))
        return moves
    
    def is_position_empty(self, i, j) -> bool:
        return self._mboard[i][j] == self.EMPTY
    
    def _convert_to_matrix(self, board:str):
        return np.array(list(board)).reshape(3, 3)
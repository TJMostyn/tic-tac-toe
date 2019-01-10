import unittest
from game import TicTacToeGame

class TestTicTacToeGame(unittest.TestCase):
    
    def test_winning_position_row_column(self):
        board = 'o xx xo  '
        game = TicTacToeGame(board)
        
        naughts_win = game.get_winning_positions(game.NAUGHTS)
        self.assertEqual(len(naughts_win), 0)
        
        crosses_win = game.get_winning_positions(game.CROSSES)
        self.assertEqual(len(crosses_win), 2)
        for win in crosses_win:
            self.assertTrue(win in [(1, 1), (2, 2)])
    
    def test_winning_position_diagonal(self):
        board = 'o xxo    '
        game = TicTacToeGame(board)
        
        naughts_win = game.get_winning_positions(game.NAUGHTS)
        self.assertEqual(len(naughts_win), 1)
        for win in naughts_win:
            self.assertTrue(win in [(2, 2)])
        
        crosses_win = game.get_winning_positions(game.CROSSES)
        self.assertEqual(len(crosses_win), 0)
        
    def test_has_no_winner(self):
        board = 'xoxxxooxo'
        game = TicTacToeGame(board)
        self.assertFalse(game.has_winner())
        
    def test_has_winner(self):
        board = 'xo ox  ox'
        game = TicTacToeGame(board)
        self.assertTrue(game.has_winner())
import unittest
from ttt import check_rows
from ttt import check_cols
from ttt import check_diags
from ttt import convert_num_to_board
from ttt import convert_board_to_num
from ttt import minimax
from ttt import eligible_moves


class TestCheckRows(unittest.TestCase):
    '''def check_rows'''

    def test_check_rows(self):

        board = [['X', 'X', 'X'], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(check_rows(board))
        board = [[1, 2, 3], [4, 5, 6], ['O', 'O', 'O']]
        self.assertTrue(check_rows(board))
        board = [[1, 2, 'X'], [4, 5, 'X'], [7, 8, 'X']]
        self.assertFalse(check_rows(board))


class TestCheckCols(unittest.TestCase):
    '''def check_cols'''

    def test_check_cols(self):

        board = [['X', 'X', 'X'], [4, 5, 6], [7, 8, 9]]
        self.assertFalse(check_cols(board))
        board = [[1, 2, 'O'], [4, 5, 'O'], ['X', 'X', 'O']]
        self.assertTrue(check_cols(board))
        board = [['X', 2, 'O'], ['X', 'O', 'X'], ['X', 8, 9]]
        self.assertTrue(check_cols(board))


class TestCheckDiags(unittest.TestCase):
    '''def check_diags'''

    def test_check_diags(self):

        board = [['X', 'O', 'X'], ['O', 'X', 6], ['O', 8, 'X']]
        self.assertTrue(check_diags(board))
        board = [['O', 2, 3], [4, 'O', 'X'], ['X', 'X', 'O']]
        self.assertTrue(check_diags(board))
        board = [['X', 'X', 'X'], [4, 5, 'X'], [7, 8, 'X']]
        self.assertFalse(check_diags(board))


class TestConvertNumToBoard(unittest.TestCase):
    '''def convert_num_to_board'''

    def test_convert_num_to_board(self):

        self.assertTupleEqual(convert_num_to_board(5), (1, 1))
        self.assertTupleEqual(convert_num_to_board(1), (0, 0))
        self.assertTupleEqual(convert_num_to_board(9), (2, 2))


class TestEligibleMoves(unittest.TestCase):
    '''def eligible_moves'''

    def test_eligible_moves(self):

        board = [['X', 'X', 'X'], [4, 5, 6], [7, 8, 9]]
        self.assertListEqual(eligible_moves(board), [4, 5, 6, 7, 8, 9])
        board = [[1, 2, 'O'], [4, 5, 'O'], ['X', 'X', 'O']]
        self.assertListEqual(eligible_moves(board), [1, 2, 4, 5])
        board = [['X', 'O', 'O'], ['X', 'O', 'X'], ['X', 'O', 'O']]
        self.assertListEqual(eligible_moves(board), [])


class TestConvertBoardToNum(unittest.TestCase):
    '''def minimax'''

    def test_convert_board_to_num(self):

        self.assertEqual(convert_board_to_num(0, 0), 1)
        self.assertEqual(convert_board_to_num(1, 2), 6)
        self.assertEqual(convert_board_to_num(2, 1), 8)


class TestMinimax(unittest.TestCase):
    '''def minimax'''

    def test_minimax(self):

        board = [['O', 2, 'X'], [4, 'X', 6], [7, 8, 9]]
        self.assertTupleEqual(minimax(board, True, 10), (7, 3))
        board = [['X', 2, 'X'], ['O', 'O', 6], ['X', 8, 9]]
        print(type(minimax(board, True, 10)))
        self.assertTupleEqual(minimax(board, True, 10), (6, 110))


if __name__ == '__main__':
    unittest.main()

import unittest
# target = __import__("ttt.py")
# check_rows = target.check_rows
from ttt import check_rows


class TestCheckRows(unittest.TestCase):
    '''x'''

    def test_check_rows(self):
        '''x'''

        board = [['X', 'X', 'X'], [4, 5, 6], [7, 8, 9]]
        self.assertTrue(check_rows(board))
        board = [[1, 2, 3], [4, 5, 6], ['O', 'O', 'O']]
        self.assertTrue(check_rows(board))
        board = [[1, 2, 'X'], [4, 5, 'X'], [7, 8, 'X']]
        self.assertFalse(check_rows(board))

if __name__ == '__main__':
    unittest.main()


# def check_rows(board_map):
#     '''three in a row on rows'''
#     win = False
#     row = 0
    
#     while row < 3:
#         if board_map[row][0] == board_map[row][1] == board_map[row][2]:
#             win = True
#         row += 1
    
#     return win

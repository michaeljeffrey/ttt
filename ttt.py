#!/usr/bin/env python3

def draw_board(board_map):
    print(f" 1 | 2 | 3\n - - - - -\n 4 | 5 | 6\n - - - - -\n 7 | 8 | 9")

def ttt():
    board_map =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    draw_board(board_map)

if __name__ == "__main__":
    ttt()

"""
 1 | 2 | 3 
 - - - - -
 4 | 5 | 6
 - - - - -
 7 | 8 | 9
"""
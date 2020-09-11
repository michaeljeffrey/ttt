#!/usr/bin/env python3

"""
next:
accept valid inputs
check for win
clear screen ?
AI for computer turn
"""

def draw_board(board_map):
    '''draw the TTT board'''
    counter = 0
    row = 0
    while counter < 5:
        if counter % 2 == 0:
            print(f" {board_map[row][0]} | {board_map[row][1]} | {board_map[row][2]}")
            counter += 1
            row += 1
        else:
            print(f"- - - - -")
            counter += 1
    return
"""
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 1 | 2 | 3 
 - - - - -
 4 | 5 | 6
 - - - - -
 7 | 8 | 9
"""

def choose_position(board_map, human_turn):
    '''choose a position on the board either by human input or AI'''
    if human_turn:
        position = input ("Enter position number: ")
        valid = False
        for row in range(3):
            for col in range(3):
                if int(position) == board_map[row][col]:
                    board_map[row][col] = 'X'
                    valid = True

        # for row in board_map:
        #     print(row)
        #     for col in row:
        #         print(col)
        #         print(row.index(col))
        #         # print(col, row.index(col))
    return

def ttt():
    ''' main '''
    board_map =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    game_over = False
    draw_board(board_map)
    while not game_over:
        human_turn = True
        choose_position(board_map, human_turn)
        draw_board(board_map)
    return

if __name__ == "__main__":
    ttt()

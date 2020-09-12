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

def check_rows(board_map):
    win = False
    row = 0
    while row < 3:
        if board_map[row][0] == board_map[row][1] == board_map[row][2]:
            win = True
        row += 1
    return win

def check_cols(board_map):
    win = False
    col = 0
    while col < 3:
        if board_map[0][col] == board_map[1][col] == board_map[2][col]:
            win = True
        col +=1
    return win

def check_diags(board_map):
    win = False
    slash_cols = [1, 5, 9]
    backslash_cols = [3, 5, 7]
    for diag in [slash_cols, backslash_cols]: 
        print(board_map[0][diag[0]])    
        # if board_map[0][diag[0]] == board_map[1][diag[1]] == board_map[2][diag[2]]:
        #     win = True
    return win

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
    return

def determine_win(board_map):
    # return True if any([check_rows(board_map),check_cols(board_map), check_diags(board_map)]) else False
    return True if any([check_rows(board_map),check_cols(board_map)]) else False


def ttt():
    ''' main '''
    board_map =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    game_over = False
    draw_board(board_map)
    while not game_over:
        human_turn = True
        choose_position(board_map, human_turn)
        draw_board(board_map)
        if determine_win(board_map) == True:
            game_over = True
            print(f"win!")
    return

if __name__ == "__main__":
    ttt()

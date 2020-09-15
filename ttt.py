#!/usr/bin/env python3
from copy import deepcopy

"""
next:
clear screen
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
    if (board_map[0][0] == board_map[1][1] == board_map[2][2]) or (board_map[0][2] == board_map[1][1] == board_map[2][0]):
        win = True
    return win

def convert_num_to_board(num):
    row = (num-1)//3
    col = (num-1)%3
    return (row, col)

"""
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 1 | 2 | 3 
 - - - - -
 4 | 5 | 6
 - - - - -
 7 | 8 | 9
"""

def convert_board_to_num(row, col):
    return ((row*3)+(col+1))

def choose_position(board_map, human_turn):
    '''choose a position on the board either by human input or AI'''
    if human_turn:
        valid = False
        while not valid:
            position_raw = input("Enter position number: ")
            try:
                position = int(position_raw)
                if position in eligible_moves(board_map):
                    print("eligible!")
                    # for row in range(3):
                    #     for col in range(3):
                    #         if int(position) == board_map[row][col]:
                    #             board_map[row][col] = 'X'
                    #             valid = True
                    (row, col) = convert_num_to_board(position)
                    set_position(board_map, row, col, human_turn)
                    valid = True
                else:
                    print(f"That position is taken!")
            except:
                print(f"That was not an integer!")
    else:
        minimax(board_map, 10, True)
    return

def set_position(board_map, row, col, human_turn):
    if human_turn:
        board_map[row][col] = 'X'
    else:
        board_map[row][col] = 'O'
    return

def eligible_moves(board):
    '''provides flattened list of eligible moves'''
    return [position for row in board for position in row if isinstance(position, int)]


def minimax(board_node, depth, ai):
    print(board_node, depth, ai)
    parent = deepcopy(board_node)
    value = 0
    if depth == 0 or determine_win(parent):
        return value
    if ai:
        value = 100000
        for c in eligible_moves(parent):
            (row, col) = convert_num_to_board(c)
            value = max(value, minimax(set_position(parent, row, col, False), depth-1, False))
        return value
    else:
        for c in eligible_moves(parent):
            value = max(value, minimax(set_position(parent, row, col, True), depth-1, True))
        return value

def determine_win(board_map):
    return True if any([check_rows(board_map),check_cols(board_map), check_diags(board_map)]) else False


def ttt():
    ''' main '''
    board_map =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    game_over = False
    human_turn = True
    draw_board(board_map)
    while not game_over:
        choose_position(board_map, human_turn)
        draw_board(board_map)
        if determine_win(board_map) == True:
            game_over = True
            print(f"win!")
        human_turn^=True # toggle
    return

if __name__ == "__main__":
    ttt()

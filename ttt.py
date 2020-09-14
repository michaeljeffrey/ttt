#!/usr/bin/env python3

"""
next:
clear screen
AI for computer turn
    > available position
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
    if (board_map[0][0] == board_map[1][1] == board_map[2][2]) or (board_map[0][2] == board_map[1][1] == board_map[2][0]):
        win = True
    return win

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
                    for row in range(3):
                        for col in range(3):
                            if int(position) == board_map[row][col]:
                                board_map[row][col] = 'X'
                                valid = True
                else:
                    print(f"That position is taken!")
            except:
                print(f"That was not an integer!")
    return

def eligible_moves(board):
    '''provides flattened list of eligible moves'''
    flat_list = [position for row in board for position in row if isinstance(position, int)]
    return flat_list


# def minimax(board_node, depth, ai):
#     if depth == 0 or determine_win(board_node):
#         return value
#     if ai:
#         value = 100000
#         for c in eligible_moves(board_node):
#             value = max(value, minimax(child, depth-1, FALSE))
#         return value
#     else:
#         for c in eligible_moves(board_node):
#             value = min(value, minimax(child, depth-1, TRUE))
#         return value

def determine_win(board_map):
    return True if any([check_rows(board_map),check_cols(board_map), check_diags(board_map)]) else False


def ttt():
    ''' main '''
    board_map =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    game_over = False
    draw_board(board_map)
    while not game_over:
        human_turn = True
        choose_position(board_map, human_turn)
        draw_board(board_map)
        print(eligible_moves(board_map))
        if determine_win(board_map) == True:
            game_over = True
            print(f"win!")
        # minimax(board_map, 10, True)
    return

if __name__ == "__main__":
    ttt()

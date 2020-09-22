from copy import deepcopy
from os import system, name 

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
    '''three in a row on rows'''
    win = False
    row = 0
    
    while row < 3:
        if board_map[row][0] == board_map[row][1] == board_map[row][2]:
            win = True
        row += 1
    
    return win

def check_cols(board_map):
    '''three in a row on columns'''
    win = False
    col = 0
    
    while col < 3:
        if board_map[0][col] == board_map[1][col] == board_map[2][col]:
            win = True
        col +=1
    
    return win

def check_diags(board_map):
    '''three in a row on the diags'''
    win = False  
    if (board_map[0][0] == board_map[1][1] == board_map[2][2]) or (board_map[0][2] == board_map[1][1] == board_map[2][0]):
        win = True
    return win

def convert_num_to_board(num):
    '''convert from flat numbers to matrix'''
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
    '''convert from matrix to flat numbers'''
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
                    (row, col) = convert_num_to_board(position)
                    set_position(board_map, row, col, True)
                    valid = True
                else:
                    print(f"That position is taken!")
            except:
                print(f"That was not an integer!")
    
    else:
        (position, value) = minimax(board_map, True) # don't need value
        (row, col) = convert_num_to_board(position)
        set_position(board_map, row, col, False)
    
    return

def set_position(board_map, row, col, human_turn):
    '''set the move on the TTT board'''
    if human_turn:
        board_map[row][col] = 'X'
    else:
        board_map[row][col] = 'O'
    return

def eligible_moves(board):
    '''provides flattened list of eligible moves'''
    return [position for row in board for position in row if isinstance(position, int)]


def minimax(board_node, ai):
    '''minimax algorithm -- figure out the best move or worst-case''' 
    if determine_win(board_node):
        if ai:
            return (0, -100)
        else:
            return (0, 100)

    if not eligible_moves(board_node):
        return (0, 0)

    if ai:
        best_move = 0
        best_score = -100
        
        for move in eligible_moves(board_node):
            node = deepcopy(board_node)
            (row, col) = convert_num_to_board(move)
            set_position(node, row, col, False)
            (node_move, node_score) = minimax(node, False)
            
            if node_score > best_score:
                best_move = move
                best_score = node_score

    else:
        best_move = 0
        best_score = 100
        
        for move in eligible_moves(board_node):
            node = deepcopy(board_node)
            (row, col) = convert_num_to_board(move)
            set_position(node, row, col, True)
            (node_move, node_score) = minimax(node, True)
            
            if node_score < best_score:
                best_move = move
                best_score = node_score

    return (best_move, best_score)


def determine_win(board_map):
    '''determine three in a row?'''
    return True if any([check_rows(board_map),check_cols(board_map), check_diags(board_map)]) else False


def ttt():
    ''' main '''
    board_map =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    human_turn = True
    system('clear' if name =='posix' else 'cls') 
    draw_board(board_map)
    print(f"\nYou go first... you'll be 'X':\n")
    
    while eligible_moves(board_map) and not determine_win(board_map):
        choose_position(board_map, human_turn)
        system('clear' if name =='posix' else 'cls') 
        draw_board(board_map)
        if determine_win(board_map):
            if human_turn:
                print(f"\nYou win!\n")
            else:
                print("\nComputer wins!\n")
        human_turn^=True # toggle

    if not eligible_moves(board_map) and not determine_win(board_map):
        print(f"Tie!\n")
    
    return

if __name__ == "__main__":
    ttt()

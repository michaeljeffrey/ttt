#!/usr/bin/env python3

def draw_board(board_map):
    print(f" {board_map[0][0]} | {board_map[0][1]} | {board_map[0][2]}\n - - - - -\n {board_map[1][0]} | {board_map[1][1]} | {board_map[1][2]}\n - - - - -\n {board_map[2][0]} | {board_map[2][1]} | {board_map[2][2]}")
    return

"""
 1 | 2 | 3 
 - - - - -
 4 | 5 | 6
 - - - - -
 7 | 8 | 9
"""

def myfunc():
    # row = " {num1} | {num2} | {num3}"
    # line = "- - - - -"
    counter = 0
    while counter < 5:
        if counter % 2 == 0:
            num = 4
            print(f" {num} | {num} | {num}")
            counter += 1
        else:
            print(f"- - - - -")
            counter += 1


def choose_position(board_map, human_turn):
    if human_turn:
        position = input ("Enter position number: ")
        # print(position)
        valid = False
        for row in range(3):
            for col in range(3):
                # print(row, col)
                # print(board_map[row][col])
                if int(position) == board_map[row][col]:
                    board_map[row][col] = 'X'
                    valid = True
        # print(board_map)

        # for row in board_map:
        #     print(row)
        #     for col in row:
        #         print(col)
        #         print(row.index(col))
        #         # print(col, row.index(col))
    return

def ttt():
    board_map =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    draw_board(board_map)
    game_over = False
    myfunc()
    while not game_over:
        human_turn = True
        choose_position(board_map, human_turn)
        draw_board(board_map)


if __name__ == "__main__":
    ttt()

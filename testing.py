#!/usr/bin/env python3
# list = ['a', 'b', 'c']

# def changelist(list2):
#     list2[1] = 'X'
#     print(f"print {list2} in function")

# print(f"{list} before")
# changelist(list)
# print(f"{list} after")

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


print(convert_board_to_num(0, 0))
print(convert_board_to_num(1, 1))
print(convert_board_to_num(2, 2))


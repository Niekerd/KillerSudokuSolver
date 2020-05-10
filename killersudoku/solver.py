import json
import sys
from helper_functions import print_board, transform_json_to_tuples, check_input
from solve_functions import valid

def solve(board, cage_index):
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for num in range(1, 10):
                    if valid(y, x, num, board, cage_index):
                        board[y][x] = num
                        solve(board, cage_index)
                        board[y][x] = 0
                return
    print_board(board)
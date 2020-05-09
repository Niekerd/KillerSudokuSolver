from helper_functions import print_board, transform_json_to_tuples, check_input
from solve_functions import valid
from solver import solve
import json

filename = 'killersudoku/sudoku_1.json'
sudoku_cages_from_json = json.load(open(filename))

transformed_sudoku_cages = transform_json_to_tuples(sudoku_cages_from_json)

check_input(transformed_sudoku_cages)
input('This is the killer sudoku you are trying to solve. Press enter to solve.')

board = [[0 for i in range(0,9)] for i in range(0,9)]

cage_index = {tile: cage for cage in transformed_sudoku_cages for tile in cage['tiles']}

solve(board, cage_index)
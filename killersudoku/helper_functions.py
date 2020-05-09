def print_board(board, zfill=1):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(str(board[i][j]).zfill(zfill))
            else:
                print(str(board[i][j]).zfill(zfill) + " ", end="")

def transform_json_to_tuples(json):
    # This function transforms the json from 'tiles' into tuples
    for cage in json:
        cage['tiles'] = [tuple(tile) for tile in cage['tiles']]
    return json

def check_input(cages):
    # Check if there are no double coordinates by creating a list with all the coordinates and transforming it to a set.
    cages_cells = [item for cage in cages for item in cage['tiles']]
    if len(cages_cells) != len(set(cages_cells)):
        print('There are double coordinates in your json. Fix this before continuing')

    # Adds all the totalSum values to an empty board to easily display them
    board = [[0 for i in range(0, 9)] for i in range(0, 9)]
    for cage in cages:
        for tile_y, tile_x in cage['tiles']:
            board[tile_y][tile_x] = cage['sumOfTiles']
    print_board(board, zfill=2)
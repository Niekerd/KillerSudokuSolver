def valid(y, x, num, board, cage_index):
    # Check cage
    current_cage = cage_index[(y, x)]
    cage_values = list()

    # Adds all values to cage_values list
    for tile_y, tile_x in current_cage['tiles']:
        if tile_y == y and tile_x == x:
            cage_values.append(num)
        else:
            cage_values.append(board[tile_y][tile_x])

    # Check if current sum is larger than the allowed sumOfTiles
    current_sum = sum(cage_values)
    if current_sum > current_cage['sumOfTiles']:
        return False

    # Check if this is the last empty tile in the cage and see if it fits
    all_valued = 0 not in cage_values
    if all_valued:
        # Check if currentSum equals sumOfTiles
        if current_sum != current_cage['sumOfTiles']:
            return False
        # Check for double values in a cage
        double_values = len(cage_values) != len(set(cage_values))
        if double_values:
            return False

    # Check row
    for i in range(0, 9):
        if board[y][i] == num:
            return False

    # Check column
    for i in range(0,9):
        if board[i][x] == num:
            return False
        
    # Check box
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if board[y0 + i][x0 + j] == num:
                return False
    return True

# TO DO: Proper function to get the next best tile to solve.

# Sort cages on amount of tiles
# Find next smallest cage with empty tile

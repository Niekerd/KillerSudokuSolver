from time import process_time

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

expertBoard = [
    [0,5,0,0,0,0,0,0,0],
    [4,6,9,0,0,0,0,0,5],
    [0,0,0,0,0,9,3,0,0],
    [0,0,0,5,0,7,2,0,0],
    [1,0,0,0,3,0,0,0,0],
    [0,0,0,0,0,0,0,1,0],
    [6,0,0,0,0,0,0,0,7],
    [7,0,4,2,0,0,1,0,0],
    [8,0,0,6,0,0,0,4,2]
]

steps = 0

def solve(bo, pos):
    find = find_next(bo, pos)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo, (row, col)):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    global steps

    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    steps += 1
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

# simpler version of find_next, slower than find_next
# def find_empty(bo):
#     for i in range(len(bo)):
#         for j in range(len(bo[0])):
#             if bo[i][j] == 0:
#                 return (i, j)  # row, col
#     return None

def find_next(bo, pos):
    # find_next remembers the previous tile and finds the next in order, instead of starting from 0,0 again like find_empty.
    p0 = pos[0]
    p1 = pos[1] 
    if bo[p0][p1] == 0:
        return (pos)
    else:
        if pos[1] == 8 and pos[0] != 8:
            nextRow = pos[0] + 1
            return find_next(bo, (nextRow, 0))

        if pos[1] == 8 and pos[0] == 8:
            return None
        else: 
            nextColumn = pos[1] + 1
            return find_next(bo, (pos[0], nextColumn))

    
print_board(expertBoard)
t = process_time()
solve(expertBoard, [0,0])
print("_______________________")
print_board(expertBoard)
elapsed_time = process_time() - t
elapsed_ms = elapsed_time * 1000.0
print("Solving this puzzle took " + str(steps) + " steps and " + str(elapsed_ms) + "ms.")


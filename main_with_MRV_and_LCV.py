from board import *
import math
import time


# Return an empty cell with the minimum remaining values (MRV) if it exists
def find_empty_mrv(board):
    n = len(board)
    min_remaining_values = n + 1
    min_pos = None

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                remaining_values = sum(is_valid(board, value, (i, j)) for value in range(1, n + 1))
                if remaining_values < min_remaining_values:
                    min_remaining_values = remaining_values
                    min_pos = (i, j)

    return min_pos

# Return a list of values sorted by the least constraining value (LCV) heuristic
def get_lcv_values(board, pos):
    n = len(board)
    lcv_values = [(value, sum(is_valid(board, value, neighbor) for neighbor in get_neighbors(pos, n))) for value in range(1, n + 1)]
    lcv_values.sort(key=lambda x: x[1], reverse=True)
    return [value for value, _ in lcv_values]

# Check if the number being considered violates any constraints
def is_valid(board, num, pos):
    n = len(board)
    box_size = int(math.sqrt(n))

    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // box_size
    box_y = pos[0] // box_size
    for i in range(box_y * box_size, box_y * box_size + box_size):
        for j in range(box_x * box_size, box_x * box_size + box_size):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

# The solve function uses the Backtracking algorithm with MRV and LCV heuristics to solve the Sudoku puzzle
def solve(board):
    empty = find_empty_mrv(board)
    if not empty:
        return True
    row, col = empty

    for i in get_lcv_values(board, (row, col)):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def get_neighbors(pos, n):
    neighbors = []
    box_size = int(math.sqrt(n))

    # Row and column neighbors
    for i in range(n):
        neighbors.append((pos[0], i))
        neighbors.append((i, pos[1]))

    # Box neighbors
    box_x = pos[1] // box_size
    box_y = pos[0] // box_size
    for i in range(box_y * box_size, box_y * box_size + box_size):
        for j in range(box_x * box_size, box_x * box_size + box_size):
            neighbors.append((i, j))

    # Remove duplicates and the cell itself
    neighbors = list(set(neighbors))
    neighbors.remove(pos)

    return neighbors

# Implementing the Arc-3 algorithm for constraint satisfaction problems
def ac3(board):
    n = len(board)

    queue = [(i, j) for i in range(n) for j in range(9) if board[i][j] == 0]

    while queue:
        pos = queue.pop(0)
        neighbors = get_neighbors(pos, n)
        for neighbor in neighbors:
            if revise(board, pos, neighbor):
                if board[pos[0]][pos[1]] == 0:
                    return False
                queue.extend([(pos[0], pos[1]) for pos in neighbors if pos not in queue])

    return True

def revise(board, pos1, pos2):
    revised = False
    if board[pos2[0]][pos2[1]] != 0:
        if is_valid(board, board[pos2[0]][pos2[1]], pos1):
            board[pos1[0]][pos1[1]] = board[pos2[0]][pos2[1]]
            revised = True
    return revised

def solve_with_ac3(board):
    if not ac3(board):
        return False
    return solve(board)

if __name__ == "__main__":

    start_time = time.time()
    # Open the file and read the contents
    with open('sudoku_board.txt', 'r') as f:
        lines = f.readlines()

    # Get the board size and initialize the board
    n = int(lines[0])
    board = [[0] * n for _ in range(n)]

    # Fill in the constant values
    for i in range(2, int(lines[1]) + 2):
        row, col, val = map(int, lines[i].split())
        board[row][col] = val

    bd = Board(board)
    if solve_with_ac3(board):
        bd.print_board()
    else:
        print("Unsolvable CSP!")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time} seconds")
from board import *
import math

# Return an empty cell if it exist
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

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

# The solve function uses the Backtracking algorithm to solve the Sudoku puzzle
def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

# Finding the neighbors of a cell on the board
def get_neighbors(pos, n):
    neighbors = []
    box_size = int(math.sqrt(n))
    
    # Row and column neighbors
    for i in range(9):
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
    #box_size = int(math.sqrt(n))

    queue = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

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
    # Read input from user
    n = int(input().strip())  # size of the board
    c = int(input().strip())  # number of cells to fill

    # Initialize the board with zeros
    board = [[0] * n for _ in range(n)]

    # Fill in the cells with given values
    for _ in range(c):
        i, j, value = map(int, input().strip().split())
        board[i-1][j-1] = value
    
    bd = Board(board)
    if solve_with_ac3(board):
        bd.print_board()
    else:
        print("Unsolvable CSP!")

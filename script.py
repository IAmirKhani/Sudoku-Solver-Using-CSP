board = [
         [8, 15, 0, 1, 6, 2, 0, 0, 0, 0, 13, 3, 16, 9, 4, 0],
         [10, 6, 0, 0, 12, 5, 8, 4, 14, 15, 1, 9, 2, 11, 7, 13],
         [0, 5, 9, 0, 0, 0, 0, 0, 8, 0, 0, 4, 0, 0, 0, 6],
         [0, 13, 0, 0, 0, 9, 7, 0, 0, 0, 5, 11, 3, 0, 8, 14],
         [9, 0, 6, 0, 14, 1, 0, 7, 3, 0, 10, 0, 4 ,8 ,0 ,0],
         [3, 0, 0, 8, 2, 4, 6, 9, 0, 0, 7, 0, 0, 0, 0, 0],
         [11, 0, 5, 0, 0, 12, 3, 0, 1, 9, 0, 0, 7, 6, 14, 0],
         [1, 4, 7, 0, 0, 10, 0, 5, 0, 0, 8, 0, 9, 2, 3, 11],
         [0, 7, 0, 0, 9, 6, 1, 0, 0, 8, 3, 0, 0, 14, 0, 4],
         [0, 12, 0, 0, 7, 0, 14, 0, 5, 4, 6, 15, 0, 13, 9, 10],
         [0, 3, 0, 4, 0, 0, 0, 8, 7, 0, 9, 0, 0, 0, 0, 2],
         [0, 1, 0, 9, 4, 11, 5, 0, 0, 16, 0, 0, 8, 0, 6, 0],
         [0, 0, 4, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 5 ,0 ,0],
         [0, 0, 13, 2, 3, 8, 4, 6, 0, 0, 15, 0, 14, 0, 12, 9],
         [7, 9, 0, 6, 15, 14, 12, 0, 0, 3, 2, 5, 13, 4, 0, 8],
         [0, 14, 0, 10, 5, 13, 9, 0, 0, 12, 0, 0, 6, 7, 0, 3],
    ]

# Get the length of the board
n = len(board)

# Flatten the board and get the number of non-zero values
flat_board = [num for row in board for num in row]
c = len([num for num in flat_board if num != 0])

# Write the board to a text file
with open("sudoku_board.txt", "w") as f:
    # Write the length of the board to the first line
    f.write(str(n) + "\n")

    # Write the number of non-zero values to the second line
    f.write(str(c) + "\n")

    # Write the indices and values of the non-zero cells to the subsequent lines
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                f.write(f"{i} {j} {board[i][j]}\n")

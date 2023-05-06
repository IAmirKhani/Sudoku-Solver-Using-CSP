import math

class Board:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        n = len(self.board)
        box_size = int(math.sqrt(n))

        for i in range(n):
            if i % box_size == 0 and i != 0:
                print("-" * (n * 2 + box_size - 1))
            for j in range(n):
                if j % box_size == 0 and j != 0:
                    print("| ", end="")
                if j == n - 1:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
    
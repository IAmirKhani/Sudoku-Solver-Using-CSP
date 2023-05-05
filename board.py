class Board:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")
    
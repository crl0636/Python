class TicTacToe:
    def __init__(self, n):
        self.grid = [[' '] * n for i in range(n)]

    def move(self, row, col, player):
        if player == 1:
            mark = 'X'
        else:
            mark = 'O'

        self.grid[row][col] = mark
        n = len(self.grid)

        sum_row = sum([self.grid[row][c] == mark for c in range(n)])
        sum_col = sum([self.grid[c][col] == mark for c in range(n)])
        sum_left_d = sum([self.grid[i][i] == mark for i in range(n)])
        sum_right_d = sum([self.grid[i][n - 1 -i] == mark for i in range(n)])

        if sum_row == n or sum_col == n or sum_left_d == n or sum_right_d == n:
            return player
        else:
            return 0
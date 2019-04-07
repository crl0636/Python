class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if not board or len(board) == 0 or len(board[0]) == 0:
            return

        m = len(board)
        n = len(board[0])

        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][n - 1] == 'O':
                self.dfs(board, i, n - 1)

        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[m - 1][j] == 'O':
                self.dfs(board, m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 'O':
            return

        board[i][j] = 'Y'
        self.dfs(board, i - 1, j)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)


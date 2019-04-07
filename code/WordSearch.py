class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, m, n, i, j):
                    return True
        return False


    def dfs(self, board, word, m, n, i, j):
        if len(word) == 0:
            return True

        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[0]:
            return False

        if board[i][j] == word[0]:
            board[i][j] = 0

            val = (self.dfs(board, word[1:], m, n, i-1, j) or
                    self.dfs(board, word[1:], m, n, i, j-1) or
                    self.dfs(board, word[1:], m, n , i+1, j) or
                   self.dfs(board, word[1:], m, n, i, j+1))
            board[i][j] = word[0]

        return val
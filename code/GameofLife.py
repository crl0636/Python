class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        board_new = []
        for i in range(m):
            tmp =[]
            for j in range(n):
                sum = self.helper(i - 1, j, board) + self.helper(i + 1, j, board) + self.helper(i, j - 1, board) + \
                    self.helper(i, j + 1, board) + self.helper(i - 1, j - 1, board) + self.helper(i - 1, j + 1, board) + \
                    self.helper(i + 1, j - 1, board) + self.helper(i + 1, j + 1, board)

                if board[i][j] == 1 and (sum < 2 or sum > 3):
                    tmp.append(0)
                elif board[i][j] == 0 and sum == 3:
                    tmp.append(1)
                else:
                    tmp.append(board[i][j])
            board_new.append(tmp)

        for i in range(m):
            for j in range(n):
                board[i][j] = board_new[i][j]




    def helper(self, i, j, board):
        if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[i]) - 1 or board[i][j] == 0:
            return 0
        return 1

if __name__ == '__main__':
    so = Solution()
    print so.gameOfLife([
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
])
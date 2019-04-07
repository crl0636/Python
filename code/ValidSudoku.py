class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for r in range(9):
            row = []
            col = []
            grid = []

            for c in range(9):
                element = board[r][c]
                if element != '.':
                    if element in row:
                        return False
                    else:
                        row.append(element)

                element = board[c][r]
                if element != '.':
                    if element in col:
                        return False
                    else:
                        col.append(element)

                element = board[r //3 * 3 + c // 3][r % 3 * 3 + c % 3]
                if element != '.':
                    if element in grid:
                        return False
                    else:
                        grid.append(element)

            return True


if __name__ == '__main__':
    so  =  Solution()
    if so.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]):
        print "True"
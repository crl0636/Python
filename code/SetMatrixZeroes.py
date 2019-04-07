class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        is_first_row = False
        is_first_column = False
        for i in range(m):
            if matrix[i][0] == 0:
                is_first_column = True

        for j in range(n):
            if matrix[0][j] == 0:
                is_first_row = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if is_first_row:
            for j in range(n):
                matrix[0][j] = 0

        if is_first_column:
            for i in range(m):
                matrix[i][0] = 0
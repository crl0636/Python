class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2
            if target in matrix[mid]:
                return True
            else:
                if len(matrix[mid]) != 0 and matrix[mid][0] > target:
                    end -= 1
                else:
                    start += 1
        return False

if __name__ == '__main__':
    so = Solution()
    so.searchMatrix(
        [[1]], 1)